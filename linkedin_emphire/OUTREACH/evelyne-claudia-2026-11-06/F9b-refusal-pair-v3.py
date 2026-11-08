#!/usr/bin/env python3
"""F9b-refusal-pair-v3.py - the same two refusals, with the three new qualifications closed.

What changed from v2, and why
-----------------------------
Evelyne-Claudia ran v2 and reported three things. All three were right, and the first one was a
defect in my instrument rather than in the claim it was measuring.

1. Exact result-file reproduction failed in her run. Both her generated files carried
   "26 calls recorded, 26 distinct replies" where mine carried 25. The recorder keyed every stored
   reply by id(parsed), and CPython reuses object identities once an object is released, so whether
   two parsed replies appeared to be the same object depended on allocator behaviour. The hash of a
   result file cannot depend on the allocator. The recorder now assigns a sequential exchange number
   to each call and returns a dict subclass carrying that number, retaining the request, the parsed
   reply and the raw bytes together under it. Object identity is measured and reported, never used.

2. Execution provenance was mixed. v2 did `conflict.update(host_cell(...))`, which overwrote the wire
   execution's journal and restart lookup with the host execution's. The acknowledged count therefore
   came from the wire execution and the durable-record count from the host execution, and those are
   different executions with different journals: the conflict wire execution writes three verdict
   records after its retry, the conflict host execution writes two. v3 keeps the four executions
   apart and attributes every count and every restart state to the execution that produced it.

3. The host comparison looked at every field of three selected event records, after filtering the
   journal. The claim supported by that is narrower than "the host journals agree". v3 compares the
   full journal of the two host executions, record for record and unfiltered, and keeps the selected
   record comparison beside it, labelled as the narrower claim it is.

Nothing about the benchmark, the imported runner or the patch is changed. The imported runner is
still hash-checked before it is imported.

Usage
-----
    python3 F9b-refusal-pair-v3.py --bench <folder containing bench/> --out ./pair3 --match-host-id
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


class Reply(dict):
    """A parsed reply that carries the number of the exchange that produced it.

    A dict subclass rather than a wrapper, so json.dumps, equality and every consumer in the imported
    runner treat it as the dict it is. The exchange number is what the recorder keys on. It is
    assigned in call order, so it does not depend on memory addresses and cannot change between runs.
    """

    exchange = None


class Recorder:
    """The same socket exchange the imported runner performs, with everything kept.

    call() in the imported runner reads until a newline and returns json.loads(bytes). This performs
    the identical exchange and keeps the request, the parsed reply and the raw bytes together, under
    a sequential exchange number. Nothing is keyed by object identity: id() is measured below so the
    weakness is visible, but no conclusion rests on it.
    """

    def __init__(self):
        self.exchanges = []          # ordered, one entry per call
        self.by_exchange = {}        # exchange number -> request, parsed reply, raw bytes
        self.calls = 0
        self.identity_collisions = 0

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
        exchange = self.calls
        reply = Reply(parsed)
        reply.exchange = exchange
        self.by_exchange[exchange] = {"exchange": exchange, "cmd": req.get("cmd"),
                                      "request": req, "parsed": parsed, "raw": buf}
        self.exchanges.append({"exchange": exchange, "cmd": req.get("cmd"),
                               "bytes": len(buf), "sha256": sha256_bytes(buf)})
        return reply

    def raw_for(self, obj):
        exchange = getattr(obj, "exchange", None)
        if exchange is None:
            return None
        entry = self.by_exchange.get(exchange)
        return None if entry is None else entry["raw"]

    def probe_identity(self):
        """Report how far object identity would have been useable, without using it for anything.

        This exists because v2 keyed on id() and the count it produced was environment-dependent.
        The number is recorded so the reason for the change is visible in the evidence, not asserted
        in a letter.
        """
        seen = {}
        for entry in self.by_exchange.values():
            seen[id(entry["parsed"])] = seen.get(id(entry["parsed"]), 0) + 1
        self.identity_collisions = sum(n - 1 for n in seen.values() if n > 1)
        return {"calls": self.calls, "distinct_by_exchange": len(self.by_exchange),
                "distinct_by_identity": len(seen),
                "identity_collisions": self.identity_collisions}


def wire_view(recorder, obj, label, provenance):
    raw = recorder.raw_for(obj)
    if raw is None:
        raise SystemExit("cannot attribute raw bytes to %s, so this run proves nothing about the wire"
                         % label)
    return {
        "label": label,
        "exchange": getattr(obj, "exchange", None),
        "raw_sha256": sha256_bytes(raw),
        "raw_bytes": len(raw),
        "raw_text": raw.decode("utf-8", "replace"),
        "trailing_newline": raw.endswith(b"\n"),
        "parsed": obj,
        "provenance": provenance,
    }


def journal_view(cell, execution, provenance):
    """Everything this execution's own journal holds, unfiltered."""
    lines = cell.get("journal") or []
    kinds = [r.get("kind") for r in lines]
    return {
        "execution": execution,
        "journal_sha256": cell.get("journal_sha256"),
        "record_count": len(lines),
        "kinds": kinds,
        "verdict_records": len([k for k in kinds if k == "verdict"]),
        "conflict_records": len([k for k in kinds if k == "conflict"]),
        "records": lines,
        "restart_lookup": cell.get("lookup_after_restart"),
        "restart_state": cell.get("state_after_restart"),
        "provenance": provenance,
    }


def acknowledged(cell):
    """Verdict requests this execution acknowledged with ok true, counted only from its own replies."""
    n = 0
    for key in ("verdict_1", "verdict_2"):
        reply = cell.get(key)
        if isinstance(reply, dict) and reply.get("ok") is True:
            n += 1
    return n


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="folder containing bench/store.py")
    ap.add_argument("--out", default="pair3", help="where the evidence goes")
    ap.add_argument("--match-host-id", action="store_true",
                    help="give both host cells the same action id, so a full-journal comparison is fair")
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

    work = tempfile.mkdtemp(prefix="f9b-pair-v3-")

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

    # Four executions, kept apart. Nothing is merged: a merged dict is what produced v2's mixed
    # provenance, because update() let the host execution overwrite the wire execution's journal.
    conflict_wire = runner.wire_cell(store_py, common, os.path.join(work, "c-wire"),
                                     "conflict", "F9-P0001")
    conflict_aid = "F9-H0001" if args.match_host_id else "F9-P0002"
    conflict_host = runner.host_cell(store_py, host_py, os.path.join(work, "c-host"),
                                     "conflict", conflict_aid)

    verdict_copy = os.path.join(work, "verdict", "benchmark")
    shutil.copytree(bench, verdict_copy,
                    ignore=shutil.ignore_patterns("__pycache__", "artifacts", ".git"))
    v_store = os.path.join(verdict_copy, "bench", "store.py")
    v_host = os.path.join(verdict_copy, "bench", "host.py")
    v_common = runner.load_common(os.path.join(verdict_copy, "bench"))
    verdict_wire = runner.wire_cell(v_store, v_common, os.path.join(work, "v-wire"),
                                    "verdict", "F9-V0001")
    verdict_aid = "F9-H0001" if args.match_host_id else "F9-V0002"
    verdict_host = runner.host_cell(v_store, v_host, os.path.join(work, "v-host"),
                                    "verdict", verdict_aid)

    wire_prov = ("reply text captured from the socket by the recorder in this file; the parsed object "
                 "and the call itself are %s wire_cell() at %s" % (IMPORTED_RUNNER[0], runner_sha[:16]))
    host_prov = ("host event records read from this execution's own host journal by %s host_cell() at %s"
                 % (IMPORTED_RUNNER[0], runner_sha[:16]))

    def refused(cell):
        if cell["verdict_1"].get("ok") is False:
            return "verdict_1", cell["verdict_1"]
        return "verdict_2", cell["verdict_2"]

    ck, cv = refused(conflict_wire)
    vk, vv = refused(verdict_wire)

    wire = {
        "conflict": wire_view(recorder, cv, "conflict refusal reply (%s)" % ck, wire_prov),
        "verdict": wire_view(recorder, vv, "verdict refusal reply (%s)" % vk, wire_prov),
        "retry": {
            "conflict": wire_view(recorder, conflict_wire["verdict_2_retry"],
                                  "conflict retry reply", wire_prov),
            "verdict": wire_view(recorder, verdict_wire["verdict_2_retry"],
                                 "verdict retry reply", wire_prov),
        },
        "exchange_log": recorder.exchanges,
        "identity_probe": recorder.probe_identity(),
    }

    executions = {
        "conflict-wire": journal_view(conflict_wire, "conflict-wire", wire_prov),
        "conflict-host": journal_view(conflict_host, "conflict-host", host_prov),
        "verdict-wire": journal_view(verdict_wire, "verdict-wire", wire_prov),
        "verdict-host": journal_view(verdict_host, "verdict-host", host_prov),
    }

    # The host's own events, as the host logged them. The journal view above is the whole file,
    # which includes boot records and the seeded verdict; these are different objects and the two
    # comparisons below say which one is being compared.
    conflict_events = conflict_host.get("host_events") or []
    verdict_events = verdict_host.get("host_events") or []
    host = {"conflict": {"execution": "conflict-host",
                         "kinds": [e.get("kind") for e in conflict_events],
                         "records": conflict_events,
                         "provenance": host_prov},
            "verdict": {"execution": "verdict-host",
                        "kinds": [e.get("kind") for e in verdict_events],
                        "records": verdict_events,
                        "provenance": host_prov}}

    selected_equal = (json.dumps(host["conflict"]["records"], sort_keys=True)
                      == json.dumps(host["verdict"]["records"], sort_keys=True))

    # The whole journals are not equal, and they should not be: the injection exists to stop a
    # verdict from landing, so one journal holds two verdict records and the other holds none. The
    # supportable claim is that they are identical apart from the records the injection suppressed,
    # which is what this measures rather than asserts.
    def stable_part(lines):
        """Everything the injection does not touch.

        Two record kinds depend on the injection by construction: the verdict records it suppresses,
        and the boot record written when the store restarts, which counts the records it replayed.
        Comparing the rest is the claim that stands; the parts that move are reported on their own.
        """
        out = [r for r in lines if r.get("kind") != "verdict"]
        if out and out[-1].get("kind") == "boot":
            out = out[:-1]
        return out

    def restart_boot(lines):
        boots = [r for r in lines if r.get("kind") == "boot"]
        return boots[-1] if boots else {}

    c_journal = executions["conflict-host"]["records"]
    v_journal = executions["verdict-host"]["records"]
    c_boot, v_boot = restart_boot(c_journal), restart_boot(v_journal)
    rest_equal = (json.dumps(stable_part(c_journal), sort_keys=True)
                  == json.dumps(stable_part(v_journal), sort_keys=True))
    replay_counts = (c_boot.get("replayed_records"), v_boot.get("replayed_records"))
    journal_comparison = {
        "whole_journals_equal": (json.dumps(c_journal, sort_keys=True)
                                 == json.dumps(v_journal, sort_keys=True)),
        "equal_apart_from_what_the_injection_moves": rest_equal,
        "verdict_records": {"conflict-host": executions["conflict-host"]["verdict_records"],
                            "verdict-host": executions["verdict-host"]["verdict_records"]},
        "replayed_records_on_restart": {"conflict-host": replay_counts[0],
                                        "verdict-host": replay_counts[1]},
        "journal_record_counts": {"conflict-host": len(c_journal),
                                  "verdict-host": len(v_journal)},
        "kinds": {"conflict-host": executions["conflict-host"]["kinds"],
                  "verdict-host": executions["verdict-host"]["kinds"]},
        "why_not_equal": ("the injection suppresses the verdict append in one execution and not the "
                          "other, so both the verdict records and the restart boot record that counts "
                          "them differ, and nothing else does"),
    }

    records = {
        "conflict-wire": {"durable_verdict_records":
                          executions["conflict-wire"]["verdict_records"],
                          "acknowledged_verdict_requests": acknowledged(conflict_wire),
                          "source": "wire execution, this execution's journal and replies"},
        "conflict-host": {"durable_verdict_records":
                          executions["conflict-host"]["verdict_records"],
                          "acknowledged_verdict_requests": None,
                          "source": "host execution, this execution's journal; the host's own verdict "
                                    "reply is not captured here, so no acknowledged count is claimed"},
        "verdict-wire": {"durable_verdict_records":
                         executions["verdict-wire"]["verdict_records"],
                         "acknowledged_verdict_requests": acknowledged(verdict_wire),
                         "source": "wire execution, this execution's journal and replies"},
        "verdict-host": {"durable_verdict_records":
                         executions["verdict-host"]["verdict_records"],
                         "acknowledged_verdict_requests": None,
                         "source": "host execution, this execution's journal; the host's own verdict "
                                   "reply is not captured here, so no acknowledged count is claimed"},
    }

    state = {name: {"verdict_state": (view["restart_lookup"] or {}).get("verdict_state"),
                    "conflict": (view["restart_lookup"] or {}).get("conflict"),
                    "journal_sha256": view["journal_sha256"]}
             for name, view in executions.items()}

    checks = []

    def check(name, ok, detail):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    check("G1 every source hash and the imported runner's hash were verified before use",
          verified["source"] == SOURCE_SHA256 and verified["patched_store"] == PATCHED_STORE_SHA256
          and runner_sha == IMPORTED_RUNNER[1],
          json.dumps({"source": verified["source"], "patched": verified["patched_store"],
                      "runner": runner_sha}, sort_keys=True))

    check("G2 every call has its own sequential exchange number, and no conclusion uses object identity",
          len(recorder.by_exchange) == recorder.calls
          and all(e["exchange"] == i + 1 for i, e in enumerate(recorder.exchanges))
          and [e["exchange"] for e in recorder.exchanges] == list(range(1, recorder.calls + 1)),
          json.dumps(recorder.probe_identity(), sort_keys=True))

    check("G3 the recorder attributed raw bytes to the parsed objects the cells hold",
          recorder.raw_for(cv) is not None and recorder.raw_for(vv) is not None,
          "%d calls, %d exchanges, %d distinct by identity"
          % (recorder.calls, len(recorder.by_exchange),
             recorder.probe_identity()["distinct_by_identity"]))

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

    check("H2 the two host journals are identical apart from the records the injection moves",
          rest_equal
          and (executions["conflict-host"]["verdict_records"],
               executions["verdict-host"]["verdict_records"]) == (2, 0)
          and (replay_counts[0], replay_counts[1]) == (len(c_journal) - 1, len(v_journal) - 1),
          json.dumps(journal_comparison, sort_keys=True))

    check("H3 the selected host event records are identical in full, which is the narrower claim",
          selected_equal,
          "%d selected records against %d selected records"
          % (len(host["conflict"]["records"]), len(host["verdict"]["records"])))

    check("R1 the durable verdict records differ, counted per execution",
          records["conflict-wire"]["durable_verdict_records"]
          != records["verdict-wire"]["durable_verdict_records"]
          and records["conflict-host"]["durable_verdict_records"]
          != records["verdict-host"]["durable_verdict_records"],
          json.dumps({k: v["durable_verdict_records"] for k, v in records.items()}, sort_keys=True))

    check("R2 the acknowledged verdict requests differ, wire executions only",
          records["conflict-wire"]["acknowledged_verdict_requests"]
          != records["verdict-wire"]["acknowledged_verdict_requests"],
          json.dumps({k: v["acknowledged_verdict_requests"] for k, v in records.items()},
                     sort_keys=True))

    check("S1 the replayed state differs, per execution",
          state["conflict-wire"]["verdict_state"] == "conflicted"
          and state["verdict-wire"]["verdict_state"] != "conflicted"
          and state["conflict-host"]["verdict_state"] == "conflicted"
          and state["verdict-host"]["verdict_state"] != "conflicted",
          json.dumps(state, sort_keys=True))

    result = {"host_action_ids": {"conflict": conflict_aid, "verdict": verdict_aid,
                                  "wire_action_ids": {"conflict": "F9-P0001",
                                                      "verdict": "F9-V0001"}},
              "match_host_id": bool(args.match_host_id),
              "verified_hashes": verified,
              "wire": wire,
              "host": host,
              "host_journal_comparison": journal_comparison,
              "executions": executions,
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
    print("  exchanges: %d calls, %d sequential exchanges, %d distinct by object identity"
          % (recorder.calls, len(recorder.by_exchange),
             recorder.probe_identity()["distinct_by_identity"]))
    print("HOST")
    print("  conflict kinds: %s" % host["conflict"]["kinds"])
    print("  verdict  kinds: %s" % host["verdict"]["kinds"])
    print("  whole journals equal: %s" % journal_comparison["whole_journals_equal"])
    print("  equal apart from what the injection moves: %s"
          % journal_comparison["equal_apart_from_what_the_injection_moves"])
    print("  replayed on restart: conflict %s of %d records, verdict %s of %d"
          % (replay_counts[0], len(c_journal) - 1, replay_counts[1], len(v_journal) - 1))
    print("  selected host records equal: %s" % selected_equal)
    print("EXECUTIONS")
    for name in ("conflict-wire", "conflict-host", "verdict-wire", "verdict-host"):
        view = executions[name]
        print("  %-14s records %d, verdict %d, conflict %d, journal %s"
              % (name, view["record_count"], view["verdict_records"],
                 view["conflict_records"], (view["journal_sha256"] or "")[:16]))
    print("RECORDS")
    for k in ("conflict-wire", "conflict-host", "verdict-wire", "verdict-host"):
        print("  %-14s durable verdict records %d, acknowledged requests %s"
              % (k, records[k]["durable_verdict_records"],
                 records[k]["acknowledged_verdict_requests"]))
    print("STATE")
    for name in ("conflict-wire", "conflict-host", "verdict-wire", "verdict-host"):
        print("  %-14s %s" % (name, json.dumps({k: v for k, v in state[name].items()
                                                 if k != "journal_sha256"}, sort_keys=True)))
    print()
    print("%d check(s) failed" % len(result["checks_failed"]))
    print("evidence:", os.path.join(args.out, "result.json"))
    return 0 if not result["checks_failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
