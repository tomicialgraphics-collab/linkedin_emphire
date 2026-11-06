#!/usr/bin/env python3
"""F9b: a refused conflict write is reported as a refused verdict write.

Usage:
    python3 F9b-conflict-write.py --bench /path/to/host-failure-benchmark --out ./run

What this measures, in one sentence: when the store has already written and fsynced a
verdict, and the follow-on conflict record is refused, the reply to the host says nothing
is durable, the conflict record is absent, and the host's own behaviour is identical to a
run in which the conflict record was written.

Design notes, so the result cannot be read for more than it is.

1. The shipped benchmark's failpoint refuses records of kind "verdict" only. That is the
   case probe-durability needs. This script copies the benchmark to the output directory
   and widens the failpoint selector in the copy to "verdict or conflict", so the second
   write of the conflict path can be refused without a full disk. The source tree is not
   touched. Both hashes are printed and written into result.json.

2. Four cells. Control and injected, each measured twice: once through the wire (so the
   store's reply is captured verbatim) and once with the real host process, so the effect
   decision is the host's own and not a reading of the code.

3. Expectations are written as assertions and checked. A run that produces a different
   world prints the difference and exits 2. The point of the artifact is that the numbers
   can disagree with the narrative.

Standard library only. Loopback only. Deterministic: same seed, same keys, same clock.
"""

import argparse
import hashlib
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

REQUIRED = ("bench/store.py", "bench/host.py", "bench/common.py")

FAILPOINT_BEFORE = '        if self.failpoint == "verdict" and record.get("kind") == "verdict":'
FAILPOINT_AFTER = ('        if (self.failpoint in ("verdict", "conflict")\n'
                   '                and self.failpoint == record.get("kind")):')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def wait_port(proc, port_file, seconds=10):
    deadline = time.time() + seconds
    while time.time() < deadline:
        if os.path.exists(port_file):
            with open(port_file, encoding="utf-8") as fh:
                text = fh.read().strip()
            if text:
                return int(text)
        if proc.poll() is not None:
            raise SystemExit("store exited before announcing a port")
        time.sleep(0.02)
    raise SystemExit("store never announced a port")


def call(port, req):
    """One request, one reply. The reply is returned exactly as it arrived."""
    with socket.create_connection(("127.0.0.1", port), timeout=5) as sock:
        sock.sendall((json.dumps(req) + "\n").encode("utf-8"))
        buf = b""
        while not buf.endswith(b"\n"):
            chunk = sock.recv(65536)
            if not chunk:
                break
            buf += chunk
    return json.loads(buf.decode("utf-8"))


def stop(proc):
    if proc is None:
        return
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    for stream in (proc.stdout, proc.stderr):
        if stream:
            stream.close()


def start_store(store_py, workdir, journal, failpoint=None):
    announce = os.path.join(workdir, "port.txt")
    if os.path.exists(announce):
        os.remove(announce)
    env = dict(os.environ)
    env.pop("HFB_FAILPOINT", None)
    if failpoint:
        env["HFB_FAILPOINT"] = failpoint
    proc = subprocess.Popen([sys.executable, store_py, "--journal", journal,
                             "--announce", announce],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                            env=env)
    return proc, wait_port(proc, announce)


def journal_lines(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def verdict_record(common, aid, verdict, rule, ts, desc_sha):
    record = {"action_id": aid, "policy_sha": common.POLICY_SHA,
              "decided_by": common.DECIDED_BY, "verdict": verdict, "rule": rule,
              "descriptor_sha": desc_sha, "decision_ts": ts}
    record["signature"] = common.sign(common.record_payload(record))
    return record


def wire_cell(store_py, common, workdir, failpoint, aid):
    """Issue, commit, verdict, verdict. Returns the two verdict replies verbatim."""
    os.makedirs(workdir, exist_ok=True)
    journal = os.path.join(workdir, "journal.jsonl")
    desc = "sha256:" + "1" * 64
    proc, port = start_store(store_py, workdir, journal, failpoint)
    out = {}
    try:
        out["issue"] = call(port, {"cmd": "issue", "action_id": aid})
        out["commit"] = call(port, {"cmd": "commit", "action_id": aid, "descriptor_sha": desc})
        first = verdict_record(common, aid, "BLOCK", "R7", 4, desc)
        out["verdict_1"] = call(port, {"cmd": "verdict", "record": first})
        second = verdict_record(common, aid, "ALLOW", None, 5, desc)
        out["verdict_2"] = call(port, {"cmd": "verdict", "record": second})
        # What the reply invites. A client told the write did not land retries it, and this
        # path is not idempotent, so the retry is measured rather than reasoned about.
        out["verdict_2_retry"] = call(port, {"cmd": "verdict", "record": second})
        out["state_in_process"] = call(port, {"cmd": "state"})
        out["lookup_in_process"] = call(port, {"cmd": "lookup", "action_id": aid})
    finally:
        stop(proc)
    # A restart with no failpoint: what a later reader, with only the journal, can see.
    proc, port = start_store(store_py, workdir, journal, None)
    try:
        out["lookup_after_restart"] = call(port, {"cmd": "lookup", "action_id": aid})
        out["state_after_restart"] = call(port, {"cmd": "state"})
    finally:
        stop(proc)
    out["journal"] = journal_lines(journal)
    out["journal_sha256"] = sha256_file(journal)
    return out


def host_cell(store_py, host_py, workdir, failpoint, aid):
    """Seed one verdict, then let the real host send its own as the second."""
    os.makedirs(workdir, exist_ok=True)
    journal = os.path.join(workdir, "journal.jsonl")
    host_journal = os.path.join(workdir, "host-B.jsonl")
    wal = os.path.join(workdir, "wal-B.jsonl")
    for stale in (host_journal, wal):
        if os.path.exists(stale):
            os.remove(stale)
    desc = "sha256:" + "1" * 64
    proc, port = start_store(store_py, workdir, journal, failpoint)
    try:
        seeded = call(port, {"cmd": "issue", "action_id": aid})
        call(port, {"cmd": "commit", "action_id": aid, "descriptor_sha": desc})
        first = verdict_record(load_common(os.path.dirname(store_py)), aid, "BLOCK", "R7", 4, desc)
        seeded_verdict = call(port, {"cmd": "verdict", "record": first})
        host = subprocess.run([sys.executable, host_py, "--scenario", "B",
                               "--port", str(port), "--workdir", workdir,
                               "--journal", "host-B.jsonl", "--action-id", aid],
                              capture_output=True, text=True)
        host_exit = host.returncode
        host_stderr = host.stderr.strip()
    finally:
        stop(proc)
    proc, port = start_store(store_py, workdir, journal, None)
    try:
        after = call(port, {"cmd": "lookup", "action_id": aid})
    finally:
        stop(proc)
    events = [e for e in journal_lines(host_journal)
              if e.get("kind") in ("reply_rejected", "effect_withheld", "ship_ok",
                                   "wal_commit", "ship_failed")]
    return {"seeded_issue": seeded, "seeded_verdict": seeded_verdict,
            "host_exit": host_exit, "host_stderr": host_stderr,
            "host_events": events, "lookup_after_restart": after,
            "journal": journal_lines(journal), "journal_sha256": sha256_file(journal)}


def load_common(bench_dir):
    if bench_dir not in sys.path:
        sys.path.insert(0, bench_dir)
    import common  # noqa: PLC0415 - imported after the path is known
    return common


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="the host-failure-benchmark folder")
    ap.add_argument("--out", default="run", help="where the copy and the evidence go")
    args = ap.parse_args(argv)

    bench = os.path.abspath(args.bench)
    for rel in REQUIRED:
        if not os.path.exists(os.path.join(bench, rel)):
            raise SystemExit("not a benchmark folder, missing %s" % rel)

    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    # The working copy lives in the system temp directory. It is a copy of someone
    # else's benchmark and it does not belong in the evidence folder.
    work = tempfile.mkdtemp(prefix="f9b-copy-")
    copy = os.path.join(work, "benchmark")
    shutil.copytree(bench, copy, ignore=shutil.ignore_patterns("__pycache__", "artifacts", ".git"))

    store_py = os.path.join(copy, "bench", "store.py")
    host_py = os.path.join(copy, "bench", "host.py")
    before = sha256_file(store_py)
    with open(store_py, encoding="utf-8") as fh:
        source = fh.read()
    if FAILPOINT_BEFORE not in source:
        raise SystemExit("the failpoint line has moved; refusing to patch blind")
    with open(store_py, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(source.replace(FAILPOINT_BEFORE, FAILPOINT_AFTER, 1))
    after = sha256_file(store_py)
    common = load_common(os.path.join(copy, "bench"))

    control = wire_cell(store_py, common, os.path.join(work, "control"), None, "F9-0001")
    injected = wire_cell(store_py, common, os.path.join(work, "injected"), "conflict", "F9-0002")
    host_control = host_cell(store_py, host_py, os.path.join(work, "host-control"), None, "F9-0003")
    host_injected = host_cell(store_py, host_py, os.path.join(work, "host-injected"),
                              "conflict", "F9-0004")

    def kinds(cell):
        return [r.get("kind") for r in cell["journal"]]

    def host_kinds(cell):
        return [e.get("kind") for e in cell["host_events"]]

    checks = []

    def check(name, ok, detail):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    # A1 the control world: the conflict is recorded and the reply says so.
    r2 = control["verdict_2"]
    check("A1 control: second verdict accepted as a conflict",
          r2.get("ok") is True and r2.get("stored") is True
          and r2.get("state") == "conflicted" and r2.get("conflict") is True,
          json.dumps(r2, sort_keys=True))
    conflicts = [r for r in control["journal"] if r.get("kind") == "conflict"]
    check("A1b control: the conflict record ties the two verdicts together",
          bool(conflicts) and conflicts[0].get("first_seq") == 4
          and conflicts[0].get("second_seq") == 5 and conflicts[0].get("rule"),
          json.dumps(conflicts[0], sort_keys=True) if conflicts else "no conflict record")

    # A2 the injected world: same two verdicts, no conflict record, a reply that denies durability.
    j2 = injected["verdict_2"]
    verdicts = [r for r in injected["journal"] if r.get("kind") == "verdict"]
    check("A2 injected: reply says nothing is durable",
          j2.get("ok") is False and j2.get("durable") is False
          and "stored" not in j2 and j2.get("error"),
          json.dumps(j2, sort_keys=True))
    check("A2b injected: no conflict record reached the journal",
          kinds(injected).count("conflict") == 0,
          "journal kinds: %s" % kinds(injected))
    seqs = {v.get("store_seq"): (v.get("record") or {}).get("verdict") for v in verdicts}
    check("A2c injected: both decisions are on disk, BLOCK then ALLOW",
          seqs.get(4) == "BLOCK" and seqs.get(5) == "ALLOW",
          "verdict store_seq -> verdict: %s" % json.dumps(seqs, sort_keys=True))
    check("A2d injected: the durable records are intact, not partial",
          all(v.get("digest") == common.frame({k: x for k, x in v.items() if k != "digest"})
              for v in verdicts),
          "digests recomputed over each record")

    # A3 what survives: the state is recomputed, the declared conflict is not.
    check("A3 injected after restart: state recomputed as conflicted",
          injected["lookup_after_restart"].get("verdict_state") == "conflicted",
          json.dumps(injected["lookup_after_restart"].get("verdict_state")))
    check("A3b injected after restart: no conflict entry to read",
          injected["lookup_after_restart"].get("conflict") is None,
          json.dumps(injected["lookup_after_restart"].get("conflict")))
    check("A3c control after restart: the conflict entry survives",
          host_control is not None
          and control["lookup_after_restart"].get("conflict") is not None,
          json.dumps(control["lookup_after_restart"].get("conflict")))

    # A4 the host behaves the same in both worlds. This is her correction, measured.
    check("A4 host effect withheld in both worlds",
          host_control["host_events"] and host_injected["host_events"]
          and [e["reason"] for e in host_control["host_events"]
               if e.get("kind") == "effect_withheld"]
          == [e["reason"] for e in host_injected["host_events"]
              if e.get("kind") == "effect_withheld"],
          "control %s / injected %s" % (host_kinds(host_control), host_kinds(host_injected)))
    check("A4b the host's stated problem differs",
          [e.get("problems") for e in host_control["host_events"] if e.get("kind") == "reply_rejected"]
          != [e.get("problems") for e in host_injected["host_events"]
              if e.get("kind") == "reply_rejected"],
          "the reply is where the two worlds part")

    # A5 the reply invites a retry, and the retry adds a record without adding evidence.
    retry = injected["verdict_2_retry"]
    retry_verdicts = [r for r in injected["journal"] if r.get("kind") == "verdict"]
    check("A5 injected: the retry is refused in the same words",
          retry.get("ok") is False and retry.get("durable") is False,
          json.dumps(retry, sort_keys=True))
    check("A5b injected: the retry leaves three verdict records and still no conflict record",
          len(retry_verdicts) == 3 and kinds(injected).count("conflict") == 0,
          "verdict store_seq: %s, journal kinds: %s"
          % ([v.get("store_seq") for v in retry_verdicts], kinds(injected)))
    check("A5c injected: the third verdict duplicates the second",
          len(retry_verdicts) == 3
          and retry_verdicts[1].get("record") == retry_verdicts[2].get("record"),
          "two records carry the same verdict payload")

    # A5d honesty check: retrying the control's reply also appends. Idempotence is a
    # separate property of this path and this case does not establish anything about it.
    control_verdicts = [r for r in control["journal"] if r.get("kind") == "verdict"]
    check("A5d control: the same retry also appends, so idempotence is not this case",
          len(control_verdicts) == 3 and kinds(control).count("conflict") == 2,
          "control verdicts %d across %d records: %s"
          % (len(control_verdicts), len(control["journal"]), kinds(control)))

    failed = [c for c in checks if not c["ok"]]
    payload = {
        "case": "F9b",
        "measured": "a refused conflict write is reported as a refused verdict write",
        "patched_store_sha256_before": before,
        "patched_store_sha256_after": after,
        "failpoint_patch": {"before": FAILPOINT_BEFORE.strip(), "after": FAILPOINT_AFTER},
        "cells": {"control": control, "injected": injected,
                  "host_control": host_control, "host_injected": host_injected},
        "checks": checks,
        "failed": len(failed),
    }
    with open(os.path.join(out, "result.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)

    print("F9b, a refused conflict write reported as a refused verdict write")
    print("store.py patched, sha256 %s -> %s" % (before[:16], after[:16]))
    print("")
    for c in checks:
        print("%-4s %s" % ("ok" if c["ok"] else "DIFF", c["check"]))
        if not c["ok"]:
            print("     %s" % c["detail"][:300])
    print("")
    print("control  reply to the second verdict: %s"
          % json.dumps(control["verdict_2"], sort_keys=True))
    print("injected reply to the second verdict: %s"
          % json.dumps(injected["verdict_2"], sort_keys=True))
    print("retry    reply: %s" % json.dumps(injected["verdict_2_retry"], sort_keys=True))
    print("injected journal kinds: %s" % kinds(injected))
    print("host control  events: %s" % host_kinds(host_control))
    print("host injected events: %s" % host_kinds(host_injected))
    print("")
    print("%d check(s) differ from the expectation" % len(failed))
    # The path as the caller wrote it. A transcript that names a home directory is a
    # transcript that cannot be sent to anyone.
    print("evidence: %s" % os.path.join(args.out, "result.json"))
    return 0 if not failed else 2


if __name__ == "__main__":
    sys.exit(main())
