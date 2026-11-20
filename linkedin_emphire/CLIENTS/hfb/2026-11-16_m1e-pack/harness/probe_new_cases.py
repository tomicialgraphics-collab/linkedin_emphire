#!/usr/bin/env python3
"""M1c probe: the two cases the reviewer raised after the 15 November rebuild.

Case C, duplicate sequence numbers after an unconfirmed rollback. A batch write stops halfway,
leaving one whole record on disk and half of the next. The rollback is refused, so the store
answers that it cannot tell what reached the disk. That answer is right. What the store may not
then do is number the retry from memory: the record already on disk spent its number, and the
retry spends the same one again, so two records share a store_seq and nothing can say which
came first.

Case D, a malformed line before an unterminated final record. The whole record at the end is
readable and is reported as a gap. A repair that removes the malformed line must not also
remove that record, from the journal or from the quarantine, and the gap must still be reported
on the next restart. On the revision of 15 November the repair rewrote the file without it, so
restart 2 saw a clean file and the gap went quiet.

Usage:
    python3 probe_new_cases.py --repo /path/to/checkout [--json out.json]

Exit codes: 0 both cases hold, 2 a case failed, 1 the probe could not run.
"""

import argparse
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def load(repo):
    bench = os.path.join(repo, "bench")
    if bench not in sys.path:
        sys.path.insert(0, bench)
    import store  # noqa: E402
    return store


def case_c(store):
    """A partial batch, a rollback that is refused, then a retry."""
    if not hasattr(store, "JournalStateUnknown") or not hasattr(store.Store, "record_batch"):
        return {"case": "C duplicate sequence numbers after an unconfirmed rollback",
                "applicable": False,
                "note": "this revision has no unconfirmed-rollback state and no batch write, "
                        "so the case cannot be arranged on it",
                "checks": {"c_not_applicable": True},
                "holds": True}
    work = tempfile.mkdtemp(prefix="m1c-c-")
    journal = os.path.join(work, "store.jsonl")
    s = store.Store(store.Journal(journal))
    s.handle({"cmd": "issue", "action_id": "M1C-C1"})
    short = [{"kind": "expectation", "action_id": "M1C-C2"}]
    long = [{"kind": "expectation", "action_id": "M1C-C3", "descriptor_sha": "e" * 400}]
    s.journal.failpoint = "write-partial+rollback"
    try:
        s.record_batch(short + long)
        reply = {"raised": False, "note": "the failpoint did not fire"}
    except store.JournalStateUnknown as exc:
        reply = {"raised": True, "reason": str(exc)[:160]}
    except Exception as exc:  # noqa: BLE001
        reply = {"raised": False, "error": repr(exc)}
    after_failure = open(journal, "rb").read()
    s.journal.failpoint = ""
    retried = s.handle({"cmd": "issue", "action_id": "M1C-C4"})
    rows = [json.loads(line) for line in open(journal, encoding="utf-8") if line.strip()]
    seqs = [row["store_seq"] for row in rows]
    checks = {
        "c_reply_says_unknown": bool(reply.get("raised")),
        "c_records_on_disk_after_failure": len([ln for ln in after_failure.splitlines() if ln.strip()]),
        "c_retry_replied": retried.get("ok") is True,
        "c_retry_seq": retried.get("store_seq"),
        "c_unique_seq": len(seqs) == len(set(seqs)),
    }
    return {"case": "C duplicate sequence numbers after an unconfirmed rollback",
            "applicable": True, "reply": reply, "all_seq": seqs, "checks": checks,
            "holds": (checks["c_reply_says_unknown"] and checks["c_unique_seq"]
                      and checks["c_retry_replied"])}


def case_d(store):
    """A malformed line before an unterminated final record, then two restarts."""
    if not hasattr(store.Journal, "_unterminated_tail"):
        return {"case": "D a malformed line before an unterminated final record",
                "applicable": False,
                "note": "this revision has no unterminated-tail state, so the case cannot be "
                        "arranged on it",
                "checks": {"d_not_applicable": True},
                "holds": True}
    work = tempfile.mkdtemp(prefix="m1c-d-")
    journal = os.path.join(work, "store.jsonl")
    s = store.Store(store.Journal(journal))
    s.handle({"cmd": "issue", "action_id": "M1C-D1"})
    tail = {"kind": "expectation", "action_id": "M1C-D2", "store_seq": 2}
    tail["digest"] = store.frame(tail)
    held = json.dumps(tail, sort_keys=True).encode("utf-8")
    with open(journal, "ab") as fh:
        fh.write(b'{"this line": is not json\n')
        fh.write(held)
    one = store.Store(store.Journal(journal))
    after_one = open(journal, "rb").read()
    two = store.Store(store.Journal(journal))
    after_two = open(journal, "rb").read()
    directory = os.path.dirname(journal)
    names = [n for n in os.listdir(directory) if ".quarantine-" in n]
    quarantined = b"".join(open(os.path.join(directory, n), "rb").read() for n in names)
    gap_one, gap_two = one.journal.gap, two.journal.gap
    checks = {
        "d_gap_on_restart_1": bool(gap_one),
        "d_gap_on_restart_2": bool(gap_two),
        "d_gap_same_sha": bool(gap_one and gap_two
                                and gap_one.get("sha256") == gap_two.get("sha256")),
        "d_gap_names_seq": bool(gap_one and gap_one.get("store_seq") == 2),
        "d_record_in_journal": held in after_one and held in after_two,
        "d_record_in_quarantine": held in quarantined,
        "d_damage_in_quarantine": b"is not json" in quarantined,
        "d_journal_stable_across_restarts": after_one == after_two,
        "d_record_not_indexed": "M1C-D2" not in one.handle({"cmd": "state"})["expectations"],
    }
    return {"case": "D a malformed line before an unterminated final record",
            "gap_restart_1": gap_one, "gap_restart_2": gap_two,
            "quarantine": one.journal.quarantine, "checks": checks,
            "holds": all(value for value in checks.values())}


def main():
    parser = argparse.ArgumentParser(description="The two cases raised on 15 November.")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--json", default=None)
    args = parser.parse_args()
    try:
        store = load(os.path.abspath(args.repo))
    except Exception as exc:  # noqa: BLE001
        print("could not import the store: %r" % (exc,))
        return 1
    results = [case_c(store), case_d(store)]
    for result in results:
        print(result["case"])
        for name, value in result["checks"].items():
            if isinstance(value, bool):
                flag = "hold" if value else "FAIL"
            else:
                flag = "note"
            print("  %-32s %s  %s" % (name, flag, value))
        print("  %-32s %s" % ("holds", "yes" if result["holds"] else "no"))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=1, default=str)
    ok = all(result["holds"] for result in results)
    print("")
    print("both cases hold" if ok else "a case failed")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
