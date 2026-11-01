#!/usr/bin/env python3
"""Reproduce the audit's counterexamples against a local checkout of the benchmark.

This is review equipment, not part of the benchmark. It never touches the
checkout it is pointed at: every mode copies the tree to a temporary
directory, applies one change, runs the suite there, and reports what
`verify.py` said afterwards.

    python3 repro_audit.py --repo /path/to/host-failure-benchmark --list
    python3 repro_audit.py --repo /path/to/host-failure-benchmark f1

Each mode is one of the findings in the 1 November audit. The mode name is
what the audit calls the finding, so the output can be pasted next to the
finding it tests.

Written against commit 25cd57f of Teamthy/host-failure-benchmark.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

# Applied to the end of a fresh run, after the artifacts exist.
MODES = {
    "f1": ("WAL verdict flipped BLOCK -> ALLOW, signature left stale, then replayed",
           "mid-run"),
    "f2": ("WAL decision_ts changed from 2 to 7, store untouched",
           "after-run"),
    "f3": ("an unsigned verdict for C-3003 appended to the store journal, frame recomputed",
           "after-run"),
    "f5": ("the seven host journals that prove scenarios ran deleted",
           "after-run"),
    "f8": ("D-4004 actor and policy replaced and the record re-signed with the fixture key",
           "after-run"),
    "f13": ("host-B.jsonl cut mid-line, as a crash during append would leave it",
           "after-run"),
    "f14": ("D-4004 decision_ts replaced with a Unix epoch value, re-signed and reframed",
           "after-run"),
}

TAMPER_HOOK = '''

def _audit_tamper(rundir):
    """Review hook: applies the audit's change at the moment the run reaches it."""
    mode = os.environ.get("AUDIT_TAMPER", "")
    if not mode:
        return
    if mode == "f1":
        path = os.path.join(rundir, "wal-B.jsonl")
        lines = open(path, encoding="utf-8").read().splitlines()
        rec = json.loads(lines[0])
        print("  [tamper] WAL verdict %r -> 'ALLOW', signature left stale" % rec["verdict"])
        rec["verdict"] = "ALLOW"
        open(path, "w", encoding="utf-8", newline="\\n").write(
            json.dumps(rec, sort_keys=True) + "\\n")
    elif mode == "f3":
        import sys as _sys
        _sys.path.insert(0, BENCH)
        from common import frame
        path = os.path.join(rundir, "store.jsonl")
        rows = [json.loads(l) for l in open(path, encoding="utf-8").read().splitlines()
                if l.strip()]
        seq = max(r.get("store_seq", 0) for r in rows) + 1
        forged = {"action_id": "C-3003", "kind": "verdict", "store_seq": seq,
                  "record": {"action_id": "C-3003", "decided_by": "nobody",
                             "decision_ts": 2, "descriptor_sha": None,
                             "policy_sha": None, "rule": None, "signature": None,
                             "verdict": "ALLOW"}}
        forged["digest"] = frame(forged)
        with open(path, "a", encoding="utf-8", newline="\\n") as fh:
            fh.write(json.dumps(forged, sort_keys=True) + "\\n")
        print("  [tamper] unsigned verdict for C-3003 appended, frame recomputed")
'''


def patch_driver(repo: str) -> None:
    path = os.path.join(repo, "run.py")
    with open(path, encoding="utf-8") as fh:
        source = fh.read()
    if "_audit_tamper" in source:
        return
    source = source.replace("def main(argv):", TAMPER_HOOK.strip("\n") + "\n\n\ndef main(argv):", 1)
    anchor = '    print("[store] restarting from its journal")'
    if anchor not in source:
        raise SystemExit("run.py does not look like the version this script was written for")
    source = source.replace(anchor, '    _audit_tamper(rundir)\n' + anchor, 1)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(source)


def start_store(repo: str, rundir: str):
    """Start the store on the run's journal; returns (process, port)."""
    store = os.path.join(repo, "bench", "store.py")
    announce = os.path.join(rundir, "port-repro.txt")
    if os.path.exists(announce):
        os.remove(announce)
    proc = subprocess.Popen(
        [sys.executable, store, "--journal", os.path.join(rundir, "store.jsonl"),
         "--announce", announce],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    for _ in range(500):
        if os.path.exists(announce):
            with open(announce, encoding="utf-8") as fh:
                text = fh.read().strip()
            if text:
                return proc, int(text)
        if proc.poll() is not None:
            raise SystemExit("store exited: %s" % proc.stderr.read())
        import time
        time.sleep(0.02)
    raise SystemExit("store did not announce a port")


def stop_store(proc) -> None:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def call(port: int, req: dict) -> dict:
    import socket
    with socket.create_connection(("127.0.0.1", port), timeout=5) as sock:
        sock.sendall((json.dumps(req) + "\n").encode("utf-8"))
        buf = b""
        while not buf.endswith(b"\n"):
            chunk = sock.recv(65536)
            if not chunk:
                break
            buf += chunk
    return json.loads(buf.decode("utf-8"))


def gap_names(port: int) -> set[str]:
    reply = call(port, {"cmd": "reconcile"})
    return {g["action_id"] for g in reply.get("gaps") or []}


def re_sign(record: dict, repo: str) -> dict:
    sys.path.insert(0, os.path.join(repo, "bench"))
    from common import frame, record_payload, sign
    record["signature"] = sign(record_payload(record))
    return record


def apply_after_run(repo: str, rundir: str, mode: str) -> str:
    if mode == "f2":
        path = os.path.join(rundir, "wal-B.jsonl")
        rec = json.loads(open(path, encoding="utf-8").read().splitlines()[0])
        rec["decision_ts"] = 7
        open(path, "w", encoding="utf-8", newline="\n").write(
            json.dumps(rec, sort_keys=True) + "\n")
        return "WAL decision_ts 2 -> 7, every other file untouched"

    if mode == "f5":
        gone = ["host-A.jsonl", "host-Ap.jsonl", "host-C.jsonl", "host-Cp.jsonl",
                "host-Cpp.jsonl", "host-D.jsonl", "host-Dp.jsonl"]
        for name in gone:
            os.remove(os.path.join(rundir, name))
        return "deleted %d host journals, kept host-B.jsonl" % len(gone)

    if mode == "f3":
        sys.path.insert(0, os.path.join(repo, "bench"))
        from common import frame
        path = os.path.join(rundir, "store.jsonl")
        rows = [json.loads(l) for l in open(path, encoding="utf-8").read().splitlines()
                if l.strip()]
        seq = max(r.get("store_seq", 0) for r in rows) + 1
        forged = {"action_id": "C-3003", "kind": "verdict", "store_seq": seq,
                  "record": {"action_id": "C-3003", "decided_by": "nobody",
                             "decision_ts": 2, "descriptor_sha": None,
                             "policy_sha": None, "rule": None, "signature": None,
                             "verdict": "ALLOW"}}
        forged["digest"] = frame(forged)
        with open(path, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(forged, sort_keys=True) + "\n")
        return "unsigned verdict for C-3003 appended, frame recomputed so replay accepts it"

    if mode == "f13":
        path = os.path.join(rundir, "host-B.jsonl")
        data = open(path, "rb").read()
        open(path, "wb").write(data[: len(data) // 2])
        return "host-B.jsonl truncated mid-line, every other file untouched"

    if mode in ("f8", "f14"):
        sys.path.insert(0, os.path.join(repo, "bench"))
        from common import frame
        path = os.path.join(rundir, "store.jsonl")
        rows = [json.loads(l) for l in open(path, encoding="utf-8").read().splitlines()
                if l.strip()]
        for row in rows:
            if row.get("kind") == "verdict" and row.get("action_id") == "D-4004":
                if mode == "f8":
                    row["record"]["decided_by"] = "someone-else"
                    row["record"]["policy_sha"] = "sha256:" + "0" * 64
                else:
                    row["record"]["decision_ts"] = 1767225600
                row["record"] = re_sign(row["record"], repo)
                row["digest"] = frame(row)
        open(path, "w", encoding="utf-8", newline="\n").write(
            "".join(json.dumps(r, sort_keys=True) + "\n" for r in rows))
        return ("D-4004 actor and policy rewritten, re-signed, reframed" if mode == "f8"
                else "D-4004 decision_ts -> 1767225600 (a Unix epoch value), re-signed, reframed")

    raise SystemExit("no after-run change for %r" % mode)


def around(mode: str) -> str:
    return MODES[mode][1]


def run_suite(work: str, env: dict | None = None) -> str:
    """Run the suite in the copy and return the directory it wrote.

    Found by looking at what appeared under artifacts/, not by parsing what
    run.py printed: the printed path uses the platform separator, and a
    Windows run should not need different parsing from a Linux one.
    """
    before = set(os.listdir(os.path.join(work, "artifacts"))) \
        if os.path.isdir(os.path.join(work, "artifacts")) else set()
    proc = subprocess.run([sys.executable, "run.py"], cwd=work, capture_output=True,
                          text=True, env=env)
    artifacts = os.path.join(work, "artifacts")
    after = set(os.listdir(artifacts)) if os.path.isdir(artifacts) else set()
    new_dirs = sorted(name for name in after - before if name.startswith("run-"))
    if not new_dirs:
        sys.stderr.write(proc.stdout[-1500:] + proc.stderr[-1500:])
        raise SystemExit("run.py produced no artifact directory")
    return os.path.join(artifacts, new_dirs[-1])


def verify(work: str, rundir: str) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, "verify.py", rundir], cwd=work,
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("mode", nargs="?", help="one of: " + ", ".join(sorted(MODES)))
    parser.add_argument("--repo", default=".", help="path to a host-failure-benchmark checkout")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--keep", action="store_true", help="keep the temporary copy")
    args = parser.parse_args(argv)

    if args.list or not args.mode:
        for name in sorted(MODES):
            print("%-4s %-8s %s" % (name, MODES[name][1], MODES[name][0]))
        return 0
    if args.mode not in MODES:
        raise SystemExit("unknown mode %r" % args.mode)

    repo = os.path.abspath(args.repo)
    for required in ("run.py", "verify.py", os.path.join("bench", "store.py")):
        if not os.path.exists(os.path.join(repo, required)):
            raise SystemExit("%s is not a benchmark checkout: no %s" % (repo, required))

    work = tempfile.mkdtemp(prefix="hfb-repro-")
    tree = os.path.join(work, "host-failure-benchmark")
    shutil.copytree(repo, tree, ignore=shutil.ignore_patterns("artifacts", ".git", "__pycache__"))

    print("mode %s: %s" % (args.mode, MODES[args.mode][0]))
    env = dict(os.environ)
    if around(args.mode) == "mid-run":
        patch_driver(tree)
        env["AUDIT_TAMPER"] = args.mode
    rundir = run_suite(tree, env)

    detail = ""
    before = None
    if args.mode == "f3":
        recon = json.load(open(os.path.join(rundir, "reconciled.json"), encoding="utf-8"))
        before = {g["action_id"] for g in recon.get("gaps") or []}
    if around(args.mode) == "after-run":
        detail = apply_after_run(tree, rundir, args.mode)
        print("  [tamper] " + detail)
    if args.mode == "f3":
        store_proc, port = start_store(tree, rundir)
        try:
            after = gap_names(port)
        finally:
            stop_store(store_proc)
        print("  [tamper] unsigned verdict appended, store restarted on the journal")
        print("  gaps before the forged verdict was written: %s"
              % (", ".join(sorted(before)) if before else "none"))
        print("  gaps the store reports now:                  %s"
              % (", ".join(sorted(after)) if after else "none"))
        print("  C-3003 named as a gap: %s" % ("yes" if "C-3003" in after else "no"))
        stored = [json.loads(l) for l in
                  open(os.path.join(rundir, "store.jsonl"), encoding="utf-8").read().splitlines()
                  if l.strip()]
        for row in stored:
            if row.get("action_id") == "C-3003" and row.get("kind") == "verdict":
                rec = row["record"]
                print("  the verdict the store now serves: decided_by=%r signature=%r"
                      % (rec.get("decided_by"), rec.get("signature")))

    code, out = verify(tree, rundir)
    verdict = [line for line in out.splitlines() if line.startswith("VERDICT")]
    failed = [line.split()[0] for line in out.splitlines() if " fails " in line]
    if "Traceback" in out:
        last = [l for l in out.strip().splitlines() if l.strip()][-1]
        print("")
        print("verify.py raised, no report written: %s" % last)
        print("report present: %s"
              % os.path.exists(os.path.join(rundir, "verify-report.json")))
    print("")
    print("verify.py exit %d: %s" % (code, verdict[0] if verdict else "(no verdict line)"))
    print("checks that failed: %s" % (", ".join(failed) if failed else "none"))
    if args.mode == "f3" and "B" in failed:
        print("  B fails here as a side effect of the extra store restart this script needs")
        print("  to make the store recompute its gaps; it is not part of the finding.")

    if args.mode == "f1":
        sys.path.insert(0, os.path.join(repo, "bench"))
        from common import record_payload, verify as verify_signature
        rows = [json.loads(l) for l in
                open(os.path.join(rundir, "store.jsonl"), encoding="utf-8").read().splitlines()
                if l.strip()]
        for row in rows:
            if row.get("kind") == "verdict" and row.get("action_id") == "B-2001":
                rec = row["record"]
                print("the verdict the store now holds for B-2001: %r" % rec.get("verdict"))
                print("its signature still verifies: %s"
                      % verify_signature(record_payload(rec), rec.get("signature")))

    print("")
    print("working copy: %s" % (tree if args.keep else "removed"))
    if not args.keep:
        shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
