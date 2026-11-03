import json, os, subprocess, sys, shutil, tempfile
HERE = os.path.abspath("audit")
sys.path.insert(0, HERE)
import regressions as R

repo = os.path.abspath(".")
tree = R.fresh_copy(repo, "n13")
work = os.path.dirname(tree)
try:
    rundir = R.run_suite(tree)
    before = R.fingerprint(rundir)
    names_before = sorted(os.listdir(rundir))
    proc = subprocess.run([sys.executable, "challenge.py", rundir], cwd=tree,
                          capture_output=True, text=True, timeout=300)
    after = R.fingerprint(rundir)
    names_after = sorted(os.listdir(rundir))
    print("N13 preservation check: challenge.py against the evidence directory")
    print("")
    print("PRECONDITIONS")
    print("  1. A completed run's artifact directory, produced by run.py on this tree.")
    print("  2. challenge.py is pointed at that directory with one argument.")
    print("  3. The property is evidence preservation: the tool may read the directory, and it")
    print("     may write nothing into it, including no passing report.")
    print("")
    print("EXPECTED")
    print("  - challenge.py exits 0.")
    print("  - It prints its own assurance line for the directory.")
    print("  - No file is created, removed or modified in the evidence directory.")
    print("  - In particular no verify-report.json appears, which is the file his N13 opens.")
    print("")
    print("OBSERVED")
    print("  exit=%d" % proc.returncode)
    tail = [l for l in (proc.stdout or "").strip().splitlines() if l.strip()]
    print("  last line: %s" % (tail[-1] if tail else "(no output)"))
    print("  files before=%d after=%d  new=%s  removed=%s"
          % (len(names_before), len(names_after),
             sorted(set(names_after) - set(names_before)) or "none",
             sorted(set(names_before) - set(names_after)) or "none"))
    print("  report present: %s" % ("yes" if os.path.exists(os.path.join(rundir, "verify-report.json")) else "no"))
    print("  directory fingerprint unchanged: %s" % (before == after))
    print("")
    ok = (proc.returncode == 0 and before == after
          and not os.path.exists(os.path.join(rundir, "verify-report.json")))
    print("ASSERTIONS")
    print("  %s  challenge exits 0" % ("PASS" if proc.returncode == 0 else "FAIL"))
    print("  %s  evidence directory is unchanged" % ("PASS" if before == after else "FAIL"))
    print("  %s  no report is left behind for his check to open"
          % ("PASS" if not os.path.exists(os.path.join(rundir, "verify-report.json")) else "FAIL"))
    print("")
    print("RESULT: %s" % ("PASS" if ok else "FAIL"))
    print("Reading: under the current implementation the property his N13 was testing is asserted")
    print("by the tool itself, and the check must be rewritten to confirm that assertion and the")
    print("absence of new files, not the presence of a report.")
    sys.exit(0 if ok else 1)
finally:
    shutil.rmtree(work, ignore_errors=True)
