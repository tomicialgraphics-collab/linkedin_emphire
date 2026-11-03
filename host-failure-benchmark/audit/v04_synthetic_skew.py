#!/usr/bin/env python3
"""V04 as a synthetic clock-skew variant. Tests the binding property only.

Why this file exists
--------------------
The review's V04 mutation re-stamps ``decision_ts`` on replay with the replay clock's own step
and re-signs the record. In this benchmark's natural scenario B the replay step and the decision
step are the same number (both 2), so the mutation writes back the value the field already held.
The record comes out byte-identical to the WAL record and every check holds. The mutation is
therefore inert in that fixture: it cannot distinguish a verifier that binds the timestamp from
one that does not, because there is nothing to bind.

This script constructs the case the property needs. A synthetic skew advances the replay clock
before the record is re-stamped, so two different values exist and the binding either catches the
difference or does not.

What this does NOT claim
------------------------
It does not attest that the timestamp came from an independent clock, and nothing in this
benchmark provides independent timestamp attestation. The property under test is narrower: a
record whose timestamp changed between the decision and the ship must not be accepted as the
decision. The skew is artificial and is labelled as such everywhere it appears, so that no later
reader mistakes it for a case that occurred naturally.

Run
---
    python3 audit/v04_synthetic_skew.py            # control then variant, exit 0 only if both pass
    python3 audit/v04_synthetic_skew.py --skew 5   # the size of the synthetic divergence

The script copies the repository to a temporary directory for each case, so the checkout it is
run from is never modified.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import regressions as R  # noqa: E402  (the runner, the copier and the report reader)

ANCHOR = '''        for record in records:
            self.emit("replay_read", action_id=record["action_id"],
                      decision_ts=record["decision_ts"])
            aid = record["action_id"]
'''

PATCH = '''        self.clock.step += {skew}   # SYNTHETIC V04-SKEW: artificial divergence, not observed naturally
        for record in records:
            self.emit("replay_read", action_id=record["action_id"],
                      decision_ts=record["decision_ts"])
            aid = record["action_id"]
            # The mutation under review: replay re-stamps the decision timestamp with its own
            # clock step and re-signs, so the signature covers the new value.
            record["decision_ts"] = self.clock.step + 1
            record["signature"] = sign(record_payload(record))
'''


def patched_copy(repo: str, skew: int, name: str) -> str:
    """A copy of the tree with the mutation applied and the replay clock skewed by ``skew``."""
    tree = R.fresh_copy(repo, name)
    path = os.path.join(tree, "bench", "host.py")
    with open(path, encoding="utf-8") as fh:
        source = fh.read()
    if ANCHOR not in source:
        raise SystemExit("the replay loop in bench/host.py is not in the expected shape")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(source.replace(ANCHOR, PATCH.format(skew=skew), 1))
    return tree


def timestamps(rundir: str) -> dict:
    """The two numbers the property is about, read from the artifacts rather than the report."""
    wal_path = os.path.join(rundir, "wal-B.jsonl")
    store_path = os.path.join(rundir, "store.jsonl")
    with open(wal_path, encoding="utf-8") as fh:
        wal_record = json.loads(fh.read().splitlines()[0])
    stored_record = None
    if os.path.exists(store_path):
        with open(store_path, encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                row = json.loads(line)
                if row.get("kind") == "verdict" and row.get("action_id") == "B-2001":
                    stored_record = row.get("record") or stored_record
    return {
        "wal_ts": wal_record.get("decision_ts"),
        "stored_ts": (stored_record or {}).get("decision_ts"),
        "wal_record": wal_record,
        "stored_record": stored_record,
        "record_identical_to_wal": bool(stored_record) and stored_record == wal_record,
    }


def run_case(repo: str, skew: int, name: str) -> dict:
    tree = patched_copy(repo, skew, name)
    work = os.path.dirname(tree)
    try:
        rundir = R.run_suite(tree)
        proc = subprocess.run([sys.executable, "verify.py", rundir], cwd=tree,
                              capture_output=True, text=True)
        failed, note = R.failed_checks(rundir)
        report_path = os.path.join(rundir, "verify-report.json")
        holds = []
        if os.path.exists(report_path):
            with open(report_path, encoding="utf-8") as fh:
                report = json.load(fh)
            holds = [row["id"] for row in report["checks"] if row["result"] != "fails"]
        return {
            "skew": skew,
            "verify_exit": proc.returncode,
            "last_line": (proc.stdout or "").strip().splitlines()[-1:],
            "failed": sorted(failed),
            "note": note,
            "checks_that_hold": holds,
            **timestamps(rundir),
        }
    finally:
        import shutil
        shutil.rmtree(work, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="V04 as a synthetic clock-skew variant.")
    parser.add_argument("--skew", type=int, default=5,
                        help="synthetic steps of divergence between decision and replay (default 5)")
    parser.add_argument("--repo", default=os.path.dirname(HERE),
                        help="checkout under test (default: the one this file sits in)")
    args = parser.parse_args(argv)
    if args.skew <= 0:
        raise SystemExit("--skew must be positive; zero is the control and is run separately")
    repo = os.path.abspath(args.repo)

    print("V04-SKEW  synthetic clock-skew variant  (tests the binding property only)")
    print("")
    print("PRECONDITIONS")
    print("  1. The tree under test is this checkout; run.py drives scenario B, initial then replay.")
    print("  2. The clock is the benchmark's deterministic step counter. No wall clock is used.")
    print("  3. The mutation under review is applied to the replay path only: the record's")
    print("     decision_ts is re-stamped with the replay clock's own step and re-signed.")
    print("  4. The fixtures use the deterministic test key. This says nothing about key security.")
    print("  5. The divergence is SYNTHETIC: %d replay steps are injected before the re-stamp."
          % args.skew)
    print("")
    print("EXPECTED")
    print("  control (skew 0)   : the two timestamps are equal, the record is byte-identical to the")
    print("                       WAL record, every check holds, verify exits 0")
    print("  variant (skew %-4d): the two timestamps differ, the record is not the WAL record" % args.skew)
    print("                       the binding check B and the independent WAL comparison B.wal")
    print("                       both fail, and verify exits 1")
    print("")
    print("  Neither case attests that the timestamp came from an independent clock. No such")
    print("  attestation exists in this design, and the variant does not imply one.")
    print("")

    control = run_case(repo, 0, "v04-control")
    variant = run_case(repo, args.skew, "v04-variant")

    for label, case in (("control", control), ("variant", variant)):
        print("OBSERVED, %s (skew %d)" % (label, case["skew"]))
        print("  wal_ts=%s  stored_ts=%s  record_identical_to_wal=%s"
              % (case["wal_ts"], case["stored_ts"], case["record_identical_to_wal"]))
        print("  verify exit=%d  failed=%s"
              % (case["verify_exit"], ", ".join(case["failed"]) or "nothing"))
        print("  last line: %s" % (case["last_line"][0] if case["last_line"] else ""))
        print("")

    checks: list[tuple[str, bool, str]] = [
        ("control leaves the mutation inert",
         control["wal_ts"] == control["stored_ts"] and control["record_identical_to_wal"],
         "wal_ts=%s stored_ts=%s identical=%s"
         % (control["wal_ts"], control["stored_ts"], control["record_identical_to_wal"])),
        ("control passes every check",
         control["verify_exit"] == 0 and not control["failed"],
         "exit=%d failed=%s" % (control["verify_exit"], ", ".join(control["failed"]) or "nothing")),
        ("variant produces two different timestamps",
         variant["stored_ts"] is not None and variant["stored_ts"] != variant["wal_ts"],
         "stored_ts %s != wal_ts %s" % (variant["stored_ts"], variant["wal_ts"])),
        ("variant record is not the WAL record",
         variant["record_identical_to_wal"] is False,
         "identical=%s" % variant["record_identical_to_wal"]),
        ("variant is caught by the binding check and by the WAL comparison",
         {"B", "B.wal"} <= set(variant["failed"]),
         "failed=%s" % (", ".join(variant["failed"]) or "nothing")),
        ("variant fails the suite",
         variant["verify_exit"] == 1,
         "exit=%d" % variant["verify_exit"]),
    ]

    print("ASSERTIONS")
    for text, ok, detail in checks:
        print("  %s  %s  (%s)" % ("PASS" if ok else "FAIL", text, detail))
    print("")
    ok = all(item[1] for item in checks)
    print("RESULT: %s" % ("PASS" if ok else "FAIL"))
    print("Scope: the record must not be accepted when its timestamp changed between the decision")
    print("and the ship. Independent timestamp attestation is out of scope and is not claimed.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
