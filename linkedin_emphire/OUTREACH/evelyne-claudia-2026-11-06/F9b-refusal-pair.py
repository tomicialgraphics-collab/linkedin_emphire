#!/usr/bin/env python3
"""F9b-refusal-pair.py - the two refusals measured side by side, sources pinned by hash.

Why this exists
---------------
The first runner patched store.py by matching one line of text. Evelyne-Claudia pointed out the hole:
a matching line proves the expected text is present, and says nothing about the rest of the file. This
script therefore verifies the SHA-256 of every benchmark file it touches before it does anything, and
verifies the patched result against the hash the earlier run printed. If either check fails it refuses
to run rather than measuring a tree it cannot name.

It also measures both refusals in one run, so the comparison is not made across machines or days.

Usage
-----
    python3 F9b-refusal-pair.py --bench <folder containing bench/> --out ./pair
"""

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

# The bytes this case is defined against. Verified before use, not after.
SOURCE_SHA256 = {
    "bench/store.py": "99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982",
    "bench/host.py": "97aa10fc8dca799db7f089d782376e782bde8e7c1fdb8fe4ff3568bd62f8b32f",
    "bench/common.py": "c4039b867b287388e7f90126ea78db2489836bf78a815c7805b64f1473cead45",
}
PATCHED_STORE_SHA256 = "a57d8bf7df51538c46d502b3c25697f1b1eae5bb2c1ed8453875a25726dd1add"

FAILPOINT_BEFORE = '        if self.failpoint == "verdict" and record.get("kind") == "verdict":'
FAILPOINT_AFTER = ('        if (self.failpoint in ("verdict", "conflict")\n'
                   '                and self.failpoint == record.get("kind")):')


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def guard(bench, rel, expected):
    """Refuse to touch a file whose bytes are not the ones this case names."""
    path = os.path.join(bench, rel)
    if not os.path.exists(path):
        raise SystemExit("missing %s under %s" % (rel, bench))
    got = sha256_file(path)
    if got != expected:
        raise SystemExit("refusing to run: %s is %s, expected %s" % (rel, got, expected))
    return path


def load_runner():
    """The first runner's cell functions, imported rather than copied."""
    path = os.path.join(HERE, "F9b-conflict-write.py")
    spec = importlib.util.spec_from_file_location("f9b_runner", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def verdicts(cell):
    return [r for r in cell["journal"] if r.get("kind") == "verdict"]


def conflicts(cell):
    return [r for r in cell["journal"] if r.get("kind") == "conflict"]


def refused_reply(cell):
    """Which reply belongs to the operation that was refused.

    In the conflict cell the first verdict is accepted and the conflict annotation is refused, so the
    refused reply is the second. In the verdict cell the first write is already refused. Comparing
    verdict_1 across the two cells compares an accepted reply against a refused one, which measures
    nothing.
    """
    if cell["verdict_1"].get("ok") is False:
        return "verdict_1", cell["verdict_1"], 0
    return "verdict_2", cell["verdict_2"], 1


def surface(cell):
    """The five surfaces, read off one cell, in Evelyne's order."""
    vs = verdicts(cell)
    which, refused, accepted = refused_reply(cell)
    return {
        "refused_operation": {
            "refused_reply_key": which,
            "accepted_verdict_writes": accepted,
            "journal_verdict_count": len(vs),
            "journal_conflict_count": len(conflicts(cell)),
        },
        "durable_records": [
            {"store_seq": v.get("store_seq"),
             "verdict": (v.get("record") or {}).get("verdict"),
             "descriptor": ((v.get("record") or {}).get("descriptor_sha") or "")[:20],
             "decision_ts": (v.get("record") or {}).get("decision_ts")}
            for v in vs
        ],
        "refused_reply": refused,
        "first_reply": cell["verdict_1"],
        "reply_retry": cell["verdict_2_retry"],
        "replayed_state": cell["lookup_after_restart"].get("verdict_state"),
        "replayed_conflict": cell["lookup_after_restart"].get("conflict"),
        "host_events": [e.get("kind") for e in cell.get("host_events", [])],
        "host_stderr": (cell.get("host_stderr") or "").strip()[:400],
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--bench", required=True, help="folder containing bench/store.py")
    ap.add_argument("--out", default="pair", help="where the evidence goes")
    args = ap.parse_args(argv)

    bench = os.path.abspath(args.bench)
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)

    # 1. the guard: name the bytes before touching them
    for rel, want in SOURCE_SHA256.items():
        guard(bench, rel, want)
    verified = {"source": dict(SOURCE_SHA256), "patched_store": None}

    runner = load_runner()
    work = tempfile.mkdtemp(prefix="f9b-pair-")

    # 2. the conflict refusal, on a patched copy whose patched hash is also checked
    conflict_copy = os.path.join(work, "conflict", "benchmark")
    shutil.copytree(bench, conflict_copy, ignore=shutil.ignore_patterns("__pycache__", "artifacts", ".git"))
    store_py = os.path.join(conflict_copy, "bench", "store.py")
    host_py = os.path.join(conflict_copy, "bench", "host.py")
    source = open(store_py, encoding="utf-8").read()
    if FAILPOINT_BEFORE not in source:
        raise SystemExit("refusing to patch: the failpoint line is not where this case says it is")
    with open(store_py, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(source.replace(FAILPOINT_BEFORE, FAILPOINT_AFTER, 1))
    got = sha256_file(store_py)
    if got != PATCHED_STORE_SHA256:
        raise SystemExit("refusing to run: patched store.py is %s, expected %s" % (got, PATCHED_STORE_SHA256))
    verified["patched_store"] = got

    common = runner.load_common(os.path.join(conflict_copy, "bench"))
    conflict = runner.wire_cell(store_py, common, os.path.join(work, "c-wire"), "conflict", "F9-P0001")
    conflict.update(runner.host_cell(store_py, host_py, os.path.join(work, "c-host"), "conflict", "F9-P0002"))

    # 3. the verdict refusal, on the unpatched store, which is what the benchmark ships
    verdict_copy = os.path.join(work, "verdict", "benchmark")
    shutil.copytree(bench, verdict_copy, ignore=shutil.ignore_patterns("__pycache__", "artifacts", ".git"))
    v_store = os.path.join(verdict_copy, "bench", "store.py")
    v_host = os.path.join(verdict_copy, "bench", "host.py")
    v_common = runner.load_common(os.path.join(verdict_copy, "bench"))
    verdict = runner.wire_cell(v_store, v_common, os.path.join(work, "v-wire"), "verdict", "F9-V0001")
    verdict.update(runner.host_cell(v_store, v_host, os.path.join(work, "v-host"), "verdict", "F9-V0002"))

    a, b = surface(conflict), surface(verdict)

    checks = []

    def check(name, ok, detail):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    check("P1 both cells ran with the source hashes pinned",
          verified["source"] == SOURCE_SHA256 and verified["patched_store"] == PATCHED_STORE_SHA256,
          json.dumps(verified, sort_keys=True))
    check("P2 the conflict refusal left two signed verdicts on disk",
          a["refused_operation"]["journal_verdict_count"] == 2,
          "verdict records: %d" % a["refused_operation"]["journal_verdict_count"])
    check("P3 the verdict refusal left none",
          b["refused_operation"]["journal_verdict_count"] == 0,
          "verdict records: %d" % b["refused_operation"]["journal_verdict_count"])
    check("P4 the refused replies carry the same text, which is the finding",
          json.dumps(a["refused_reply"], sort_keys=True) == json.dumps(b["refused_reply"], sort_keys=True),
          json.dumps({"conflict": a["refused_reply"], "verdict": b["refused_reply"]}, sort_keys=True))
    check("P5 the replayed state differs: conflicted against not",
          a["replayed_state"] == "conflicted" and b["replayed_state"] != "conflicted",
          json.dumps({"conflict": a["replayed_state"], "verdict": b["replayed_state"]}, sort_keys=True))
    # The written expectation said the host would differ here. It does not, and this records the
    # measurement rather than the prediction: the host event kinds are identical across both refusals.
    check("P6 the host event kinds are identical, against my written expectation",
          a["host_events"] == b["host_events"],
          json.dumps({"conflict": a["host_events"], "verdict": b["host_events"]}, sort_keys=True))
    check("P7 the accepted-write count differs, which is where a reader could notice",
          a["refused_operation"]["accepted_verdict_writes"] != b["refused_operation"]["accepted_verdict_writes"],
          json.dumps({"conflict": a["refused_operation"]["accepted_verdict_writes"],
                      "verdict": b["refused_operation"]["accepted_verdict_writes"]}, sort_keys=True))

    result = {"verified_hashes": verified,
              "surfaces": {"conflict_refusal": a, "verdict_refusal": b},
              "checks": checks,
              "checks_failed": [c["check"] for c in checks if not c["ok"]]}
    with open(os.path.join(out, "result.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)

    for c in checks:
        print(("ok   " if c["ok"] else "FAIL ") + c["check"])
    print()
    print("conflict refused reply:", json.dumps(a["refused_reply"], sort_keys=True))
    print("verdict  refused reply:", json.dumps(b["refused_reply"], sort_keys=True))
    print("conflict state:", a["replayed_state"], "| verdict state:", b["replayed_state"])
    print("conflict host :", a["host_events"])
    print("verdict  host :", b["host_events"])
    print()
    print("%d check(s) failed" % len(result["checks_failed"]))
    print("evidence:", os.path.join(args.out, "result.json"))
    return 0 if not result["checks_failed"] else 1


if __name__ == "__main__":
    sys.exit(main())
