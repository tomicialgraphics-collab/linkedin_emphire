#!/usr/bin/env python3
"""Exercise the failure paths, because the retention guarantee was never about the happy path.

    python3 05-failure-paths.py --repo /path/to/ai-redteam-five-tests

Six cases, each one a way the record can be wrong while looking finished:

  T1  no results at all                      the package must not be written
  T2  non-zero exit with a stale results     the archive must refuse
  T3  results that do not parse              the archive must refuse
  T4  crash between the two renames          the pair must be detectably incomplete
  T5  a good run                             record then package, bound by digest, checksums clean
  T6  a digest that matches on 16 characters the verifier must fail it

Exit 0 only when every refusal happens and every pass is real. This is the evidence the reviewer
asked for when he said the guarantee stays open until the failure paths are tested.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

CHECKS = {"passed": 0, "failed": 0}


def ok(label: str, detail: str = "") -> None:
    CHECKS["passed"] += 1
    print("  pass  %-52s %s" % (label, detail))


def bad(label: str, detail: str) -> None:
    CHECKS["failed"] += 1
    print("  FAIL  %-52s %s" % (label, detail))


def expect_refusal(label: str, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except SystemExit as exc:
        ok(label, str(exc).splitlines()[0][:80])
        return True
    except Exception as exc:  # noqa: BLE001
        bad(label, "raised %r instead of SystemExit" % (exc,))
        return False
    bad(label, "returned instead of refusing")
    return False


def harness_dir(root: str, results: dict | None, exit_code: int = 0) -> str:
    h = os.path.join(root, "harness")
    os.makedirs(os.path.join(h, "results"), exist_ok=True)
    with open(os.path.join(h, "redteam.py"), "w", encoding="utf-8") as fh:
        fh.write("raise SystemExit(%d)\n" % exit_code)
    # The builder reads HEAD and the harness blob id, so a stand-in harness has to be a repo.
    env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
               GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
    subprocess.run(["git", "init", "-q"], cwd=h, env=env, capture_output=True)
    subprocess.run(["git", "add", "-A"], cwd=h, env=env, capture_output=True)
    subprocess.run(["git", "commit", "-qm", "harness"], cwd=h, env=env, capture_output=True)
    if results is not None:
        with open(os.path.join(h, "results", "results.json"), "w", encoding="utf-8") as fh:
            json.dump(results, fh)
    return h


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=".", help="checkout with the patched build_package.py")
    ap.add_argument("--verifier", default="03-verify_run_record.py", help="the verifier to self-test")
    args = ap.parse_args()

    repo = os.path.abspath(args.repo)
    builder_path = os.path.join(repo, "package", "build_package.py")
    spec = importlib.util.spec_from_file_location("build_package", builder_path)
    bp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bp)
    print("builder  %s" % builder_path)
    print("clock    %s\n" % __import__("datetime").datetime.now(
        __import__("datetime").timezone(__import__("datetime").timedelta(hours=1))
    ).strftime("%Y-%m-%d %H:%M WAT %A"))

    tmp = tempfile.mkdtemp(prefix="failure-paths-")
    try:
        # T1 no results at all
        print("T1  no results at all")
        root = os.path.join(tmp, "t1"); os.makedirs(root)
        h = harness_dir(root, None)
        pkg = os.path.join(root, "package.md")
        open(pkg, "w").write("placeholder\n")
        expect_refusal("archive refuses with nothing to archive", bp.archive_run, h, pkg, "")
        if open(pkg).read() == "placeholder\n":
            ok("package untouched")
        else:
            bad("package untouched", "the placeholder was overwritten")
        if os.path.exists(os.path.join(root, "run_record")):
            bad("no record published", "run_record exists after a refusal")
        else:
            ok("no record published")

        # T2 non-zero exit with a stale results file
        print("\nT2  non-zero exit, results file left over from before the run")
        root = os.path.join(tmp, "t2"); os.makedirs(root)
        h = harness_dir(root, {"meta": {"model": "old"}, "test1": {"stale": True}}, exit_code=1)
        expect_refusal("run refuses a results file this run did not write",
                       bp.run_harness, __import__('pathlib').Path(h), "test-model", "http://127.0.0.1:9/v1", "none")

        # T3 results that do not parse
        print("\nT3  results that do not parse")
        root = os.path.join(tmp, "t3"); os.makedirs(root)
        h = harness_dir(root, None)
        with open(os.path.join(h, "results", "results.json"), "w", encoding="utf-8") as fh:
            fh.write("{not json")
        pkg = os.path.join(root, "package.md")
        open(pkg, "w").write("placeholder\n")
        expect_refusal("archive refuses unparseable results", bp.archive_run, h, pkg, "console\n")

        # T4 crash between the record rename and the package rename
        print("\nT4  crash between the two renames")
        root = os.path.join(tmp, "t4"); os.makedirs(root)
        h = harness_dir(root, {"meta": {"model": "t4"}, "test1": {"note": "ok"}})
        pkg = os.path.join(root, "package.md")
        open(pkg, "w").write("placeholder\n")
        text = "# filled package\n"
        staged = bp.archive_run(h, pkg, "console\n",
                                package_digest=hashlib.sha256(text.encode()).hexdigest(),
                                run_meta={"started_utc": "2026-11-14T17:00:00+00:00",
                                          "harness_exit": 0,
                                          "package_bytes": len(text.encode())})
        real_replace = os.replace
        calls = {"n": 0}

        def dying_replace(src, dst):
            calls["n"] += 1
            if calls["n"] == 2:
                raise OSError("simulated crash between the record and the package")
            return real_replace(src, dst)

        os.replace = dying_replace
        try:
            bp.publish(staged, pkg, text)
            bad("publish raises on the simulated crash", "it returned")
        except OSError:
            ok("publish raises on the simulated crash", "OSError after the record rename")
        finally:
            os.replace = real_replace

        record = os.path.join(root, "run_record")
        # The template package.md is on disk throughout; what the crash prevents is the new text
        # arriving. So the pair is inconsistent, not half-created, and the inconsistency is what a
        # reader can detect.
        if os.path.isdir(record) and open(pkg, encoding="utf-8").read() == "placeholder\n":
            ok("record published, package still the old text", "the safe direction")
        elif not os.path.isdir(record):
            bad("record published, package still the old text", "no record, so the ordering failed")
        else:
            bad("record published, package still the old text", "the new text arrived anyway")
        if os.path.exists(os.path.join(record, "RUN.json")):
            with open(os.path.join(record, "RUN.json"), encoding="utf-8") as fh:
                run = json.load(fh)
            want = run.get("package_sha256") or ""
            here = hashlib.sha256(open(pkg, "rb").read()).hexdigest()
            if want and want != here:
                ok("the mismatch is detectable from RUN.json", "record names %s, disk has %s"
                   % (want[:16], here[:16]))
            else:
                bad("the mismatch is detectable from RUN.json", "the digests agree, so nothing detects it")
        else:
            bad("the mismatch is detectable from RUN.json", "no RUN.json")

        # T5 a good run
        print("\nT5  a good run, record then package")
        root = os.path.join(tmp, "t5"); os.makedirs(root)
        h = harness_dir(root, {"meta": {"model": "t5"}, "test1": {"note": "ok"}})
        pkg = os.path.join(root, "package.md")
        open(pkg, "w").write("placeholder\n")
        text = "# filled package for t5\n"
        staged = bp.archive_run(h, pkg, "console line\n",
                                package_digest=hashlib.sha256(text.encode()).hexdigest(),
                                run_meta={"started_utc": "2026-11-14T17:00:00+00:00",
                                          "harness_exit": 0,
                                          "package_bytes": len(text.encode())})
        record, pkg_path = bp.publish(staged, pkg, text)
        if os.path.isdir(record) and os.path.exists(pkg_path):
            ok("record and package both published")
        else:
            bad("record and package both published", "one of them is missing")
        with open(os.path.join(record, "RUN.json"), encoding="utf-8") as fh:
            run = json.load(fh)
        got = hashlib.sha256(open(pkg_path, "rb").read()).hexdigest()
        if got == run.get("package_sha256"):
            ok("RUN.json digest equals the package on disk", got[:16])
        else:
            bad("RUN.json digest equals the package on disk", "got %s" % got[:16])
        proc = subprocess.run([sys.executable, "-c",
                               "import subprocess,sys;sys.exit(subprocess.run(['sha256sum','-c','SHA256SUMS.txt']).returncode)"],
                              cwd=record, capture_output=True, text=True)
        if proc.returncode == 0:
            ok("sha256sum -c runs clean in the record")
        else:
            bad("sha256sum -c runs clean in the record", proc.stdout[-120:] + proc.stderr[-120:])
        if os.path.exists(os.path.join(root, "package.md.staging")):
            bad("no staging file left behind", "package.md.staging survived")
        else:
            ok("no staging file left behind")

        # T6 a digest that agrees only on the first 16 characters
        print("\nT6  a digest that matches on a 16 character prefix")
        verifier = os.path.join(os.path.dirname(os.path.abspath(args.verifier)), os.path.basename(args.verifier))
        if not os.path.exists(verifier):
            verifier = os.path.abspath(args.verifier)
        proc = subprocess.run([sys.executable, verifier, "--self-test"], capture_output=True, text=True)
        if proc.returncode == 0:
            ok("verifier self-test fails a prefix collision", "exit 0 from the self-test")
        else:
            bad("verifier self-test fails a prefix collision", proc.stdout[-160:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d passed, %d failed" % (CHECKS["passed"], CHECKS["failed"]))
    return 0 if CHECKS["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
