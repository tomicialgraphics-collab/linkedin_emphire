#!/usr/bin/env python3
"""F9b-refusal-pair-v2.py - the same two refusals, with the two qualifications closed.

What changed from v1, and why
-----------------------------
v1 compared the refused replies by re-serialising the parsed JSON with sorted keys. Evelyne-Claudia
pointed out that this establishes equality of the parsed objects, not equality of the bytes the client
actually received. She was right: the imported runner's call() reads the reply and then discards the
bytes, keeping only json.loads() of them.

v1 also compared host event *kinds* only. She pointed out, again correctly, that the full diagnostic
records were never compared, so any sentence about the host agreeing was broader than the measurement.

This version keeps the same cells and the same imported runner, and changes only where the bytes are
looked at:

1. The imported runner's call() is wrapped by a recorder that performs the identical socket exchange
   and keeps the bytes that the original function reads and throws away. The parsed value returned to
   the caller is the same object. Nothing else in the imported runner is touched, and its hash is
   verified before import, so that claim is checkable rather than asserted.
2. The refused replies are compared as raw bytes, hashed with SHA-256, and separately as parsed JSON.
   The two comparisons are reported as separate results because they are separate claims.
3. The host events are compared as complete records, and separately as kinds.
4. Wire results and host results are emitted in separate sections, each naming the runner and function
   that produced it.
5. The count previously called "accepted verdict writes" is now called "acknowledged verdict requests",
   and is distinguished in the output from the count of durable records.

Usage
-----
    python3 F9b-refusal-pair-v2.py --bench <folder containing bench/> --out ./pair2
"""

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import socket
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

SOURCE_SHA256 = {
    "bench/store.py": "99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982",
    "bench/host.py": "97aa10fc8dca799db7f089d782376e782bde8e7c1fdb8fe4ff3568bd62f8b32f",
    "bench/common.py": "c4039b867b287388e7f90126ea78db2489836bf78a815c7805b64f1473cead45",
}
PATCHED_STORE_SHA256 = "a57d8bf7df51538c46d502b3c25697f1b1eae5bb2c1ed8453875a25726dd1add"
IMPORTED_RUNNER = ("F9b-conflict-write.py",
                   "991e9eec09c291bf0179b6677577c5929b688df0b2b2c10fea2cc163d669e891")

FAILPOINT_BEFORE = '        if self.failpoint == "verdict" and record.get("kind") == "verdict":'
FAILPOINT_AFTER = ('        if (self.failpoint in ("verdict", "conflict")\n'
                   '                and self.failpoint == record.get("kind")):')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def guard(bench, rel, expected):
    path = os.path.join(bench, rel)
    if not os.path.exists(path):
        raise SystemExit("missing %s under %s" % (rel, bench))
    got = sha256_file(path)
    if got != expected:
        raise SystemExit("refusing to run: %s is %s, expected %s" % (rel, got, expected))
    return path


class Recorder:
    """The same socket exchange the imported runner performs, with the bytes kept.

    call() in the imported runner reads until a newline and then returns json.loads(bytes). This
    performs the identical exchange and stores the bytes keyed by the identity of the object it
    returns, so a caller holding that exact object can ask for the bytes it arrived as.
    """

    def __init__(self):
        self.raw_by_id = {}
        self.raw_order = []
        self.calls = 0

    def call(self, port, req):
        with socket.create_connection(("127.0.0.1", port), timeout=5) as sock:
            sock.sendall((json.dumps(req) + "\n").encode("utf-8"))
            buf = b""
            while not buf.endswith(b"\n"):
                chunk = sock.recv(65536)
                if not chunk:
                    break
                buf += chunk
        parsed = json.loads(buf.decode("utf-8"))
        self.calls += 1
        self.raw_by_id[id(parsed)] = buf
        self.raw_order.append({"call": self.calls, "cmd": req.get("cmd"),
                               "bytes": len(buf), "sha256": sha256_bytes(buf)})
        return parsed

    def raw_for(self, obj):
        return self.raw_by_id.get(id(obj))


def wire_view(recorder, obj, label, provenance):
    raw = recorder.raw_for(obj)
    if raw is None:
        raise SystemExit("cannot attribute raw bytes to %s, so this run proves nothing about the wire"
                         % label)
    return {
        "label": label,
        "raw_sha256": sha256_bytes(raw),
        "raw_bytes": len(raw),
        "raw_text": raw.decode("utf-8", "replace"),
        "trailing_newline": raw.endswith(b"\n"),
        "parsed": obj,
        "provenance": provenance,
    }


def host_view(cell, provenance):
    events = cell.get("host_events") or []
    return {
        "event_count": len(events),
        "kinds": [e.get("kind") for e in events],
        "records": events,
        "provenance": provenance,
    }


def acknowledged(cell):
    """Verdict requests the store acknowledged with ok true, counted separately from records on disk."""
    n = 0
    for key in ("verdict_1", "verdict_2"):
        reply = cell.get(key)
        if isinstance(reply, dict) and reply.get("ok") is True:
            n += 1
    return n


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="folder containing bench/store.py")
    ap.add_argument("--out", default="pair2", help="where the evidence goes")
    ap.add_argument("--match-host-id", action="store_true",
                    help="give both host cells the same action id, so a full-record comparison is fair")
    args = ap.parse_args(argv)

    bench = os.path.abspath(args.bench)
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)

    for rel, want in SOURCE_SHA256.items():
        guard(bench, rel, want)

    runner_path = os.path.join(HERE, IMPORTED_RUNNER[0])
    runner_sha = sha256_file(runner_path)
    if runner_sha != IMPORTED_RUNNER[1]:
        raise SystemExit("refusing to import: %s is %s, expected %s"
                         % (IMPORTED_RUNNER[0], runner_sha, IMPORTED_RUNNER[1]))

    spec = importlib.util.spec_from_file_location("f9b_runner", runner_path)
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)

    recorder = Recorder()
    runner.call = recorder.call

    verified = {"source": dict(SOURCE_SHA256),
                "patched_store": None,
                "imported_runner": {IMPORTED_RUNNER[0]: runner_sha}}

    work = tempfile.mkdtemp(prefix="f9b-pair-v2-")

    conflict_copy = os.path.join(work, "conflict", "benchmark")
    shutil.copytree(bench, conflict_copy,
                    ignore=shutil.ignore_patterns("__pycache__", "artifacts", ".git"))
    store_py = os.path.join(conflict_copy, "bench", "store.py")
    host_py = os.path.join(conflict_copy, "bench", "host.py")
    source = open(store_py, encoding="utf-8").read()
    if FAILPOINT_BEFORE not in source:
        raise SystemExit("refusing to patch: the failpoint line is not where this case says it is")
    with open(store_py, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(source.replace(FAILPOINT_BEFORE, FAILPOINT_AFTER, 1))
    patched = sha256_file(store_py)
    if patched != PATCHED_STORE_SHA256:
        raise SystemExit("refusing to run: patched store.py is %s, expected %s"
                         % (patched, PATCHED_STORE_SHA256))
    verified["patched_store"] = patched

    common = runner.load_common(os.path.join(conflict_copy, "bench"))
    conflict = runner.wire_cell(store_py, common, os.path.join(work, "c-wire"), "conflict", "F9-P0001")
    conflict_aid = "F9-H0001" if args.match_host_id else "F9-P0002"
    conflict.update(runner.host_cell(store_py, host_py, os.path.join(work, "c-host"),
                                     "conflict", conflict_aid))

    verdict_copy = os.path.join(work, "verdict", "benchmark")
    shutil.copytree(bench, verdict_copy,
                    ignore=shutil.ignore_patterns("__pycache__", "artifacts", ".git"))
    v_store = os.path.join(verdict_copy, "bench", "store.py")
    v_host = os.path.join(verdict_copy, "bench", "host.py")
    v_common = runner.load_common(os.path.join(verdict_copy, "bench"))
    verdict = runner.wire_cell(v_store, v_common, os.path.join(work, "v-wire"), "verdict", "F9-V0001")
    verdict_aid = "F9-H0001" if args.match_host_id else "F9-V0002"
    verdict.update(runner.host_cell(v_store, v_host, os.path.join(work, "v-host"),
                                    "verdict", verdict_aid))

    wire_prov = ("reply text captured from the socket by the recorder in this file; the parsed object "
                 "and the call itself are %s wire_cell() at %s" % (IMPORTED_RUNNER[0], runner_sha[:16]))
    host_prov = ("host event records read from the host journal by %s host_cell() at %s"
                 % (IMPORTED_RUNNER[0], runner_sha[:16]))

    def refused(cell):
        if cell["verdict_1"].get("ok") is False:
            return "verdict_1", cell["verdict_1"]
        return "verdict_2", cell["verdict_2"]

    ck, cv = refused(conflict)
    vk, vv = refused(verdict)

    wire = {
        "conflict": wire_view(recorder, cv, "conflict refusal reply (%s)" % ck, wire_prov),
        "verdict": wire_view(recorder, vv, "verdict refusal reply (%s)" % vk, wire_prov),
        "retry": {
            "conflict": wire_view(recorder, conflict["verdict_2_retry"],
                                  "conflict retry reply", wire_prov),
            "verdict": wire_view(recorder, verdict["verdict_2_retry"],
                                 "verdict retry reply", wire_prov),
        },
        "call_log": recorder.raw_order,
    }
    host = {"conflict": host_view(conflict, host_prov),
            "verdict": host_view(verdict, host_prov)}

    records = {
        "conflict": {"durable_verdict_records": len([r for r in conflict["journal"]
                                                     if r.get("kind") == "verdict"]),
                     "acknowledged_verdict_requests": acknowledged(conflict)},
        "verdict": {"durable_verdict_records": len([r for r in verdict["journal"]
                                                    if r.get("kind") == "verdict"]),
                    "acknowledged_verdict_requests": acknowledged(verdict)},
    }
    state = {"conflict": {"verdict_state": conflict["lookup_after_restart"].get("verdict_state"),
                          "conflict": conflict["lookup_after_restart"].get("conflict")},
             "verdict": {"verdict_state": verdict["lookup_after_restart"].get("verdict_state"),
                         "conflict": verdict["lookup_after_restart"].get("conflict")}}

    checks = []

    def check(name, ok, detail):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    check("G1 every source hash and the imported runner's hash were verified before use",
          verified["source"] == SOURCE_SHA256 and verified["patched_store"] == PATCHED_STORE_SHA256
          and runner_sha == IMPORTED_RUNNER[1],
          json.dumps({"source": verified["source"], "patched": verified["patched_store"],
                      "runner": runner_sha}, sort_keys=True))

    check("G2 the recorder returned the same parsed objects the cells hold",
          all(isinstance(o, dict) for o in (cv, vv)) and recorder.raw_for(cv) is not None
          and recorder.raw_for(vv) is not None,
          "%d calls recorded, %d distinct replies" % (recorder.calls, len(recorder.raw_by_id)))

    check("W1 the two refused replies are the same bytes, not merely equal as parsed JSON",
          wire["conflict"]["raw_sha256"] == wire["verdict"]["raw_sha256"],
          json.dumps({"conflict": wire["conflict"]["raw_sha256"],
                      "verdict": wire["verdict"]["raw_sha256"]}, sort_keys=True))

    check("W2 the two parsed replies are equal objects",
          json.dumps(wire["conflict"]["parsed"], sort_keys=True)
          == json.dumps(wire["verdict"]["parsed"], sort_keys=True),
          json.dumps({"conflict": wire["conflict"]["parsed"],
                      "verdict": wire["verdict"]["parsed"]}, sort_keys=True))

    check("W3 the retried replies are also the same bytes",
          wire["retry"]["conflict"]["raw_sha256"] == wire["retry"]["verdict"]["raw_sha256"],
          json.dumps({"conflict": wire["retry"]["conflict"]["raw_sha256"],
                      "verdict": wire["retry"]["verdict"]["raw_sha256"]}, sort_keys=True))

    check("H1 the host event kinds are identical",
          host["conflict"]["kinds"] == host["verdict"]["kinds"],
          json.dumps({"conflict": host["conflict"]["kinds"],
                      "verdict": host["verdict"]["kinds"]}, sort_keys=True))

    check("H2 the host event records are identical in full, not only in kind",
          json.dumps(host["conflict"]["records"], sort_keys=True)
          == json.dumps(host["verdict"]["records"], sort_keys=True),
          "%d records against %d records"
          % (host["conflict"]["event_count"], host["verdict"]["event_count"]))

    check("R1 the durable verdict records differ: two against none",
          records["conflict"]["durable_verdict_records"] == 2
          and records["verdict"]["durable_verdict_records"] == 0,
          json.dumps({k: v["durable_verdict_records"] for k, v in records.items()}, sort_keys=True))

    check("R2 the acknowledged verdict requests differ: one against none",
          records["conflict"]["acknowledged_verdict_requests"]
          != records["verdict"]["acknowledged_verdict_requests"],
          json.dumps({k: v["acknowledged_verdict_requests"] for k, v in records.items()},
                     sort_keys=True))

    check("S1 the replayed state differs: conflicted against not",
          state["conflict"]["verdict_state"] == "conflicted"
          and state["verdict"]["verdict_state"] != "conflicted",
          json.dumps(state, sort_keys=True))

    result = {"host_action_ids": {"conflict": conflict_aid, "verdict": verdict_aid},
              "match_host_id": bool(args.match_host_id),
              "verified_hashes": verified,
              "wire": wire,
              "host": host,
              "records": records,
              "state": state,
              "checks": checks,
              "checks_failed": [c["check"] for c in checks if not c["ok"]]}

    with open(os.path.join(out, "result.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)

    for c in checks:
        print(("ok   " if c["ok"] else "FAIL ") + c["check"])
    print()
    print("WIRE")
    print("  conflict reply bytes: %d, sha256 %s"
          % (wire["conflict"]["raw_bytes"], wire["conflict"]["raw_sha256"]))
    print("  verdict  reply bytes: %d, sha256 %s"
          % (wire["verdict"]["raw_bytes"], wire["verdict"]["raw_sha256"]))
    print("  conflict text: %s" % wire["conflict"]["raw_text"].rstrip("\n"))
    print("  verdict  text: %s" % wire["verdict"]["raw_text"].rstrip("\n"))
    print("HOST")
    print("  conflict kinds: %s" % host["conflict"]["kinds"])
    print("  verdict  kinds: %s" % host["verdict"]["kinds"])
    print("  full records equal: %s" % (
        json.dumps(host["conflict"]["records"], sort_keys=True)
        == json.dumps(host["verdict"]["records"], sort_keys=True)))
    print("RECORDS")
    for k in ("conflict", "verdict"):
        print("  %s: durable verdict records %d, acknowledged verdict requests %d"
              % (k, records[k]["durable_verdict_records"],
                 records[k]["acknowledged_verdict_requests"]))
    print("STATE")
    print("  conflict: %s | verdict: %s"
          % (json.dumps(state["conflict"], sort_keys=True),
             json.dumps(state["verdict"], sort_keys=True)))
    print()
    print("%d check(s) failed" % len(result["checks_failed"]))
    print("evidence:", os.path.join(args.out, "result.json"))
    return 0 if not result["checks_failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
