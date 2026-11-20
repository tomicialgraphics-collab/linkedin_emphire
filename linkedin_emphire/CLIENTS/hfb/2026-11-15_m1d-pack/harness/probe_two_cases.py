#!/usr/bin/env python3
"""M1b probe: the two cases the reviewer raised on 15 November.

Case A, missing terminator. A conflict journal with only the final newline removed. The record's
bytes are whole and its digest agrees with them, so the record is readable; the file does not say
the write finished. On restarts 1, 2 and 5 of the same journal the store must report the same
named gap, name the withheld sequence number, and leave the file byte-identical, because a repair
that rewrites the file is what made the second restart go quiet the first time.

Case B, unknown disk state. A batch write that fails partway and a rollback that fails too. The
reply must not say `durable: false`, which claims the bytes will not survive. It must say
`durable: unknown` with `disk_state: unknown` and a reason, because the process cannot tell.

Usage:
    python3 probe_two_cases.py --repo /path/to/checkout [--json out.json]

Exit codes: 0 both cases hold, 2 a case failed, 1 the probe could not run.
"""

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import probe_conflict_crash as base  # noqa: E402

# Case A uses the action the shared producer writes; case B its own, so the two never mix.

ACTION_B = "M1B-7101"
RESTARTS = (1, 2, 3, 4, 5)
CHECKED = (1, 2, 5)


def sha256_of(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def case_a(repo, workdir, decided_by, policy_sha, record_payload, sign):
    """Strip the final newline from a real conflict journal, then restart five times."""
    action_id = base.ACTION_ID
    src = os.path.join(workdir, "case-a")
    os.makedirs(src, exist_ok=True)
    journal, replies = base.produce_conflict_journal(
        repo, src, decided_by, policy_sha, record_payload, sign)
    with open(journal, "rb") as handle:
        data = handle.read()
    if not data.endswith(b"\n"):
        raise RuntimeError("the conflict journal did not end with a terminator")
    stripped = data[:-1]
    # The record whose terminator was removed, so the gap can be checked against it.
    last = json.loads(stripped.rsplit(b"\n", 1)[-1].decode("utf-8"))
    expected_seq = last.get("store_seq")
    # One journal, restarted in place: restart 2 starts from the file restart 1 left behind,
    # which is what a reviewer does and what the reported failure was. Copying the original
    # again for each restart would hide the loss, because the original still has the record.
    chain = os.path.join(workdir, "case-a", "chain")
    os.makedirs(chain, exist_ok=True)
    path = os.path.join(chain, "store.jsonl")
    with open(path, "wb") as handle:
        handle.write(stripped)
    before = sha256_of(path)

    restarts = []
    for attempt in RESTARTS:
        case = os.path.join(workdir, "case-a", "restart-%d" % attempt)
        os.makedirs(case, exist_ok=True)
        store = base.StoreProcess(repo, path, case)
        try:
            state = store.ask({"cmd": "state"})
            lookup = store.ask({"cmd": "lookup", "action_id": action_id})
            log = store.store_log()
        finally:
            store.stop()
        gap = state.get("journal_gap") or None
        restarts.append({
            "restart": attempt,
            "journal_sha256": sha256_of(path),
            "gap": gap,
            "gap_named_on_startup": "journal gap:" in log,
            "conflicted": action_id in (state.get("conflicted_verdicts") or []),
            "conflict_named": lookup.get("conflict") is not None,
        })

    checks = {}
    for row in restarts:
        checks["r%d_gap_present" % row["restart"]] = bool(row["gap"])
        checks["r%d_gap_names_seq" % row["restart"]] = (
            (row["gap"] or {}).get("store_seq") == expected_seq)
        checks["r%d_gap_reason" % row["restart"]] = (
            (row["gap"] or {}).get("reason") == "unterminated record")
        checks["r%d_journal_unchanged" % row["restart"]] = (
            row["journal_sha256"] == before)
        checks["r%d_not_indexed" % row["restart"]] = (
            not row["conflicted"] and not row["conflict_named"])
        checks["r%d_said_on_startup" % row["restart"]] = row["gap_named_on_startup"]

    holds = all(value for key, value in checks.items()
                if any(key.startswith("r%d_" % attempt) for attempt in CHECKED))
    return {
        "case": "A missing terminator",
        "expected_seq": expected_seq,
        "journal_sha256_before": before,
        "restarts": restarts,
        "checks": checks,
        "holds": holds,
        "replies_before_stripping": replies,
    }


def case_b(repo, workdir, decided_by, policy_sha, record_payload, sign):
    """A write that fails partway and a rollback that fails too."""
    case = os.path.join(workdir, "case-b")
    os.makedirs(case, exist_ok=True)
    journal = os.path.join(case, "store.jsonl")

    store = base.StoreProcess(repo, journal, case)
    try:
        store.ask({"cmd": "issue", "action_id": ACTION_B})
        store.ask({"cmd": "verdict", "record": base.verdict_record(
            ACTION_B, "ALLOW", 1, decided_by, policy_sha, record_payload, sign)})
    finally:
        store.stop()

    failing_dir = os.path.join(case, "failing")
    os.makedirs(failing_dir, exist_ok=True)
    store = base.StoreProcess(repo, journal, failing_dir)
    try:
        # Armed through the protocol so the store can boot cleanly first: a failpoint set at
        # start-up would fail the boot record and there would be no process to ask.
        armed = store.ask({"cmd": "failpoint", "value": "write-partial,rollback"})
        reply = store.ask({"cmd": "verdict", "record": base.verdict_record(
            ACTION_B, "BLOCK", 2, decided_by, policy_sha, record_payload, sign)})
    finally:
        store.stop()

    after_failure_sha = sha256_of(journal)

    # A tree without the failpoint command cannot be made to fail on demand, so the state the
    # case is about does not exist there. What it does have is a refused write, which it answers
    # as `durable: false`; that is the second-best evidence and it is recorded rather than
    # described.
    refused = None
    if not armed.get("ok"):
        os.environ["HFB_FAILPOINT"] = "verdict"
        demo_dir = os.path.join(case, "refused")
        os.makedirs(demo_dir, exist_ok=True)
        demo = base.StoreProcess(repo, journal, demo_dir)
        try:
            refused = demo.ask({"cmd": "verdict", "record": base.verdict_record(
                ACTION_B, "BLOCK", 3, decided_by, policy_sha, record_payload, sign)})
        finally:
            demo.stop()
            os.environ.pop("HFB_FAILPOINT", None)

    recovered_dir = os.path.join(case, "recovered")
    os.makedirs(recovered_dir, exist_ok=True)
    recovered = base.StoreProcess(repo, journal, recovered_dir)
    try:
        state = recovered.ask({"cmd": "state"})
        lookup = recovered.ask({"cmd": "lookup", "action_id": ACTION_B})
        records = base.read_records(journal)
    finally:
        recovered.stop()

    kinds = [record.get("kind") for record in records
             if record.get("action_id") == ACTION_B]
    pair_present = "conflict" in kinds and kinds.count("verdict") >= 2
    # Whatever the restart found, it has to say what it found: either the conflict named, or a
    # repair record naming the bytes it quarantined. Silence is the failure.
    repairs = [record for record in records if record.get("kind") == "repair"]
    quarantine_named = any(record.get("quarantine_sha256") for record in repairs)

    checks = {
        "reply_not_ok": reply.get("ok") is False,
        "durable_is_unknown": reply.get("durable") == "unknown",
        "not_durable_false": reply.get("durable") is not False,
        "disk_state_unknown": reply.get("disk_state") == "unknown",
        "reason_named": bool(reply.get("reason")),
        "restart_names_what_it_found": (
            lookup.get("conflict") is not None or quarantine_named),
    }
    return {
        "case": "B unknown disk state",
        "reply_to_failed_batch": reply,
        "failpoint_command_supported": bool(armed.get("ok")),
        "refused_verdict_reply_on_this_tree": refused,
        "journal_sha256_after_failure": after_failure_sha,
        "kinds_after_restart": kinds,
        "observed_pair_present_after_restart": pair_present,
        "observed_conflict_named_after_restart": lookup.get("conflict") is not None,
        "observed_quarantine_named_after_restart": quarantine_named,
        "observed_recovered_records": len(records),
        "checks": checks,
        "holds": all(checks.values()),
    }


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--json", default=None)
    args = parser.parse_args(argv[1:])

    repo = os.path.abspath(args.repo)
    if not os.path.isdir(os.path.join(repo, "bench")):
        print("no bench directory under %s" % repo, file=sys.stderr)
        return 1
    decided_by, policy_sha, record_payload, sign = base.load_common(repo)
    workdir = tempfile.mkdtemp(prefix="m1b-")
    try:
        a = case_a(repo, workdir, decided_by, policy_sha, record_payload, sign)
        b = case_b(repo, workdir, decided_by, policy_sha, record_payload, sign)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    result = {
        "probe": "m1b-two-cases",
        "revision": base.git_revision(repo),
        "case_a": a,
        "case_b": b,
        "holds": a["holds"] and b["holds"],
    }
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, sort_keys=True)
            handle.write("\n")

    for case in (a, b):
        print("== %s" % case["case"])
        for name, value in sorted(case["checks"].items()):
            print("   %-38s %s" % (name, "hold" if value else "FAIL"))
    if a["holds"] and b["holds"]:
        print("both cases hold: a named gap that survives restarts, and an unknown state said out loud")
        return 0
    print("a case failed")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
