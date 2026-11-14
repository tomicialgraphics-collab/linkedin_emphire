#!/usr/bin/env python3
"""M1 probe: does a conflict survive a crash between the two writes that record it?

It asserts one property and reports everything else it saw.

The property: a store that reports an action as conflicted must be able to name the conflict,
meaning a preserved record carrying both sequence numbers of the two verdicts that disagree.

How it is tested without waiting for a real crash at the right microsecond: the probe runs a
real conflict through a real store, then takes the resulting journal and cuts it at every line
boundary. Each cut is a place where a crash between two fsyncs could have left the file. Every
cut image is handed to a fresh store process, and that store is asked two questions:

    is the action reported conflicted?     state.conflicted_verdicts
    is the conflict named?                 lookup.conflict, with first_seq and second_seq

A cut that leaves the first answer yes and the second answer no is the failure this milestone
is about. It is a state a reader can reach by power loss, not by editing a file.

Usage:
    python3 probe_conflict_crash.py --repo /path/to/host-failure-benchmark
    python3 probe_conflict_crash.py --repo ... --json out.json

Exit codes: 0 the property held at every cut, 2 the property failed at one or more cuts,
1 the probe itself could not run.
"""

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PROBE_ID = "m1-conflict-crash"
ACTION_ID = "M1-7001"


def git_revision(path):
    """The commit being probed, so the log names a revision rather than somebody's directory."""
    try:
        out = subprocess.run(["git", "-C", path, "rev-parse", "HEAD"],
                             capture_output=True, text=True, timeout=20)
        if out.returncode == 0:
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return "no git revision at this path"


def load_common(repo):
    sys.path.insert(0, os.path.join(repo, "bench"))
    from common import DECIDED_BY, POLICY_SHA, record_payload, sign  # noqa: E402
    return DECIDED_BY, POLICY_SHA, record_payload, sign


def verdict_record(action_id, verdict, step, decided_by, policy_sha, record_payload, sign):
    record = {
        "action_id": action_id,
        "policy_sha": policy_sha,
        "decided_by": decided_by,
        "verdict": verdict,
        "rule": None,
        "descriptor_sha": "sha256:" + "0" * 64,
        "decision_ts": {"step": step, "phase": "probe"},
    }
    record["signature"] = sign(record_payload(record))
    return record


class StoreProcess:
    """One store process, its announced port, and one request per line."""

    def __init__(self, repo, journal, workdir):
        self.announce = os.path.join(workdir, "port.txt")
        self.log = os.path.join(workdir, "store.log")
        self.proc = subprocess.Popen(
            [sys.executable, os.path.join(repo, "bench", "store.py"),
             "--journal", journal, "--announce", self.announce],
            stdout=open(self.log, "w", encoding="utf-8"),
            stderr=subprocess.STDOUT,
        )
        deadline = time.time() + 15
        port = None
        while time.time() < deadline:
            if os.path.exists(self.announce):
                text = open(self.announce, encoding="utf-8").read().strip()
                if text:
                    port = int(text)
                    break
            if self.proc.poll() is not None:
                raise RuntimeError("store exited before announcing a port: %s"
                                   % open(self.log, encoding="utf-8").read()[-400:])
            time.sleep(0.02)
        if port is None:
            raise RuntimeError("store never announced a port")
        self.sock = socket.create_connection(("127.0.0.1", port), timeout=15)
        self.stream = self.sock.makefile("rwb")

    def ask(self, request):
        self.stream.write((json.dumps(request, sort_keys=True) + "\n").encode("utf-8"))
        self.stream.flush()
        line = self.stream.readline()
        if not line:
            raise RuntimeError("store closed the connection without a reply")
        return json.loads(line)

    def stop(self):
        try:
            self.stream.close()
            self.sock.close()
        except OSError:
            pass
        if self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait(timeout=10)
        return self.proc.returncode

    def store_log(self):
        try:
            return open(self.log, encoding="utf-8").read()
        except OSError:
            return ""


def produce_conflict_journal(repo, workdir, decided_by, policy_sha, record_payload, sign):
    """One real conflict, through the store's own protocol, leaving a real journal."""
    journal = os.path.join(workdir, "store.jsonl")
    store = StoreProcess(repo, journal, workdir)
    try:
        issued = store.ask({"cmd": "issue", "action_id": ACTION_ID})
        first = store.ask({"cmd": "verdict", "record": verdict_record(
            ACTION_ID, "ALLOW", 1, decided_by, policy_sha, record_payload, sign)})
        second = store.ask({"cmd": "verdict", "record": verdict_record(
            ACTION_ID, "BLOCK", 2, decided_by, policy_sha, record_payload, sign)})
    finally:
        store.stop()
    return journal, {"issue": issued, "first": first, "second": second}


def cut_points(data):
    """Every line boundary except the last, which is the whole file and not a crash."""
    ends = [index + 1 for index, byte in enumerate(data) if byte == 0x0A]
    return ends[:-1] if ends else []


def inspect_cut(repo, data, cut, label, workdir, decided_by, policy_sha,
                record_payload, sign):
    """Start a store on the cut image and ask it what it knows."""
    case = os.path.join(workdir, label.replace(" ", "-"))
    os.makedirs(case, exist_ok=True)
    journal = os.path.join(case, "store.jsonl")
    with open(journal, "wb") as handle:
        handle.write(data[:cut])
    store = StoreProcess(repo, journal, case)
    try:
        lookup = store.ask({"cmd": "lookup", "action_id": ACTION_ID})
        state = store.ask({"cmd": "state"})
        log = store.store_log()
    finally:
        store.stop()

    conflicted = ACTION_ID in (state.get("conflicted_verdicts") or [])
    named = lookup.get("conflict") or None
    named_seqs = sorted([named.get("first_seq"), named.get("second_seq")]) if named else []
    verdict_seqs = sorted(
        record.get("store_seq") for record in read_records(journal)
        if record.get("kind") == "verdict" and record.get("action_id") == ACTION_ID)
    repair = "journal repaired" in log
    withdrawn = "batch withheld" in log or "withheld" in log

    holds = (not conflicted) or (named is not None and named_seqs == verdict_seqs)
    return {
        "cut": label,
        "bytes": cut,
        "conflicted": conflicted,
        "conflict_named": named is not None,
        "named_seqs": named_seqs,
        "verdict_seqs": verdict_seqs,
        "repair_reported": repair,
        "batch_withheld": withdrawn,
        "property_holds": holds,
        "records_recovered": len(read_records(journal)),
    }, lookup, state, log


def read_records(path):
    records = []
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                stripped = line.strip()
                if not stripped:
                    continue
                try:
                    record = json.loads(stripped)
                except ValueError:
                    continue
                if isinstance(record, dict):
                    records.append(record)
    except OSError:
        pass
    return records


def main(argv):
    parser = argparse.ArgumentParser(description="M1 conflict-crash probe")
    parser.add_argument("--repo", required=True, help="checkout to probe")
    parser.add_argument("--json", default="", help="write the full result here")
    parser.add_argument("--keep", default="", help="keep the working directory here")
    args = parser.parse_args(argv[1:])

    repo = os.path.abspath(args.repo)
    decided_by, policy_sha, record_payload, sign = load_common(repo)

    workdir = args.keep or tempfile.mkdtemp(prefix="m1-probe-")
    os.makedirs(workdir, exist_ok=True)
    keep = bool(args.keep)
    try:
        origin = os.path.join(workdir, "origin")
        os.makedirs(origin, exist_ok=True)
        journal, responses = produce_conflict_journal(
            repo, origin, decided_by, policy_sha, record_payload, sign)
        if not responses["second"].get("conflict"):
            raise RuntimeError("the store did not record a conflict at all, so the probe has "
                               "nothing to cut: %r" % (responses["second"],))
        data = open(journal, "rb").read()
        lines = len(read_records(journal))

        cuts = cut_points(data)
        results = []
        for index, cut in enumerate(cuts):
            label = "line-%d" % (index + 1)
            result, _, _, _ = inspect_cut(repo, data, cut, label, workdir,
                                          decided_by, policy_sha, record_payload, sign)
            results.append(result)

        # One more cut, in the middle of the final write itself. This is the shape a power loss
        # takes when it lands inside the record rather than between two of them, and it is held
        # to the same property as every other cut.
        torn = None
        if cuts:
            mid = cuts[-1] + max(1, (len(data) - cuts[-1]) // 2)
            torn, _, _, torn_log = inspect_cut(repo, data, mid, "mid-final-line", workdir,
                                               decided_by, policy_sha, record_payload, sign)
            torn["log_tail"] = torn_log.strip().splitlines()[-3:]
            results.append(torn)
    finally:
        if not keep:
            shutil.rmtree(workdir, ignore_errors=True)

    failures = [result for result in results if not result["property_holds"]]
    payload = {
        "probe": PROBE_ID,
        "revision": git_revision(repo),
        "action_id": ACTION_ID,
        "journal_lines": lines,
        "journal_bytes": len(data),
        "store_response_to_second_verdict": responses["second"],
        "cuts": results,
        "torn_final_line": torn,
        "failed_cuts": [failure["cut"] for failure in failures],
        "property_holds": not failures,
    }
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")

    print("M1 probe: a reported conflict must be a named conflict")
    print("revision: %s" % git_revision(repo))
    print("journal: %d lines, %d bytes, from one real conflict on %s"
          % (lines, len(data), ACTION_ID))
    print("")
    print("  cut            bytes  conflicted  named  verdict seqs  named seqs  property")
    for result in results:
        print("  %-13s %6d  %-10s  %-5s  %-12s  %-10s  %s" % (
            result["cut"], result["bytes"], result["conflicted"],
            result["conflict_named"], result["verdict_seqs"], result["named_seqs"],
            "holds" if result["property_holds"] else "FAILS"))
    if torn and torn is results[-1]:
        pass  # already in the table above, which now includes the mid-line cut
    print("")
    if failures:
        print("FAILURE: %d of %d cuts leave the store reporting a conflict it cannot name: %s"
              % (len(failures), len(results), ", ".join(f["cut"] for f in failures)))
        for failure in failures:
            print("  %s at byte %d: conflicted=%s, conflict record=%s, verdict seqs=%s"
                  % (failure["cut"], failure["bytes"], failure["conflicted"],
                     failure["conflict_named"], failure["verdict_seqs"]))
        return 2
    print("Every cut either reports no conflict or reports one it can name with both sequence "
          "numbers. The property held at %d of %d cuts." % (len(results), len(results)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
