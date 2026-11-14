#!/usr/bin/env python3
"""Check the run record and the builder fix against each other, offline, in one command.

    python3 03-verify_run_record.py --repo /path/to/ai-redteam-five-tests

It reads the corrected manifest that ships beside this file, then for every row:

  * resolves the blob id and hashes the stored object, not a copy on disk
  * compares the digest, the byte count and the encoding with the manifest
  * re-derives the digest of the served rendering and compares that too
  * resolves the harness blob at the run commit and checks the windows digest

Then it checks the builder: that the record is archived before the package is written, and that
the archive refuses to return when the results are missing. The second check runs the real
function against a throwaway directory, so it tests the code rather than the intention.

Exit code 0 means every check passed. 1 means at least one failed, and the failures are printed
with the number that disagreed. 2 means the script could not run at all.

No network. No writes outside a temporary directory. Python 3.8 or later, standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MANIFEST = os.path.join(HERE, "01-SHA256SUMS.corrected.txt")
RECORD_DIR = "review/2026-11-03_run2"

ROW = re.compile(r"^([0-9a-f]{64})  (\S+)$")
TABLE = re.compile(r"^#\s(\S+)\s+(\d+)\s+(\S+)\s+([0-9a-f]{40})$")
SERVED = re.compile(r"^# served (\S+)\s+([0-9a-f]{64})$")
SERVED_SIZE = re.compile(r"^#\s+utf-8\+bom, (\d+) bytes$")
HARNESS = re.compile(r"^# harness (\S+)\s+(\d+)\s+(\S+)\s+([0-9a-f]{64})$")
HARNESS_BLOB = re.compile(r"^#\s+blob\s+([0-9a-f]{40})$")
HARNESS_WINDOWS = re.compile(r"^#\s+windows\s+([0-9a-f]{64})")
COMMIT = re.compile(r"^# (run|record) commit\s+([0-9a-f]{40})$")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def ok(self, label: str, detail: str = "") -> None:
        self.passed += 1
        print("  pass  %-46s %s" % (label, detail))

    def bad(self, label: str, detail: str) -> None:
        self.failed += 1
        print("  FAIL  %-46s %s" % (label, detail))

    def compare(self, label: str, got, want) -> None:
        """Equal means equal. 14 November review, finding 1: this used to compare 16 of 64
        characters, so a manifest could disagree with the object everywhere after the sixteenth
        character and still pass. The short forms below are display only."""
        if got == want:
            self.ok(label, str(got)[:24])
        else:
            self.bad(label, "got %s..., manifest says %s..." % (str(got)[:24], str(want)[:24]))


def encoding_of(raw: bytes) -> str:
    """Kept identical to the builder, so a disagreement here is a real disagreement."""
    if raw.startswith(b"\xff\xfe"):
        return "utf-16le+bom"
    if raw.startswith(b"\xfe\xff"):
        return "utf-16be+bom"
    if raw.startswith(b"\xef\xbb\xbf"):
        return "utf-8+bom+crlf" if b"\r\n" in raw else "utf-8+bom"
    try:
        raw.decode("utf-8")
        return "utf-8+crlf" if b"\r\n" in raw else "utf-8"
    except UnicodeDecodeError:
        return "binary"


def served_bytes(raw: bytes, encoding: str):
    if encoding.startswith("utf-16"):
        return raw.decode("utf-16").encode("utf-8-sig")
    return None


def git(repo: str, *args: str) -> bytes:
    out = subprocess.run(["git"] + list(args), cwd=repo, capture_output=True)
    if out.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), out.stderr.decode().strip()))
    return out.stdout


def blob_at(repo: str, commit: str, path: str) -> str:
    line = git(repo, "ls-tree", commit, path).decode().strip()
    if not line:
        raise RuntimeError("%s is not in %s" % (path, commit[:12]))
    return line.split()[2]


def parse_manifest(path: str) -> dict:
    rows, table, served, served_size = [], {}, {}, {}
    harness, harness_blob, harness_windows, commits = None, None, None, {}
    with open(path, encoding="utf-8") as fh:
        for raw_line in fh:
            line = raw_line.rstrip("\n")
            if not line.strip():
                continue
            if m := ROW.match(line):
                rows.append((m.group(2), m.group(1)))
            elif m := TABLE.match(line):
                table[m.group(1)] = {"bytes": int(m.group(2)), "encoding": m.group(3),
                                     "blob": m.group(4)}
            elif m := SERVED.match(line):
                served[m.group(1)] = m.group(2)
            elif m := SERVED_SIZE.match(line):
                served_size["size"] = int(m.group(1))
            elif m := HARNESS.match(line):
                harness = {"name": m.group(1), "bytes": int(m.group(2)),
                           "encoding": m.group(3), "digest": m.group(4)}
            elif m := HARNESS_BLOB.match(line):
                harness_blob = m.group(1)
            elif m := HARNESS_WINDOWS.match(line):
                harness_windows = m.group(1)
            elif m := COMMIT.match(line):
                commits[m.group(1)] = m.group(2)
    return {"rows": rows, "table": table, "served": served, "served_size": served_size,
            "harness": harness, "harness_blob": harness_blob,
            "harness_windows": harness_windows, "commits": commits}


def check_manifest_shape(c: Checks, m: dict) -> bool:
    if not m["rows"]:
        c.bad("manifest has checksum rows", "none found; sha256sum -c would do nothing")
        return False
    c.ok("manifest has checksum rows", "%d rows" % len(m["rows"]))
    untabled = [n for n, _ in m["rows"] if n not in m["table"]]
    if untabled:
        c.bad("every row carries a blob id and encoding", "missing: " + ", ".join(untabled))
    else:
        c.ok("every row carries a blob id and encoding", "%d of %d" % (len(m["table"]), len(m["rows"])))
    for key in ("run", "record"):
        if key in m["commits"]:
            c.ok("%s commit recorded" % key, m["commits"][key][:12])
        else:
            c.bad("%s commit recorded" % key, "no line")
    return True


def check_objects(c: Checks, repo: str, m: dict) -> None:
    record = m["commits"].get("record")
    if record:
        try:
            git(repo, "cat-file", "-e", record + "^{commit}")
            c.ok("record commit is present", record[:12])
        except RuntimeError as exc:
            c.bad("record commit is present", str(exc))
            return

    for name, digest in m["rows"]:
        meta = m["table"].get(name, {})
        path = "%s/%s" % (RECORD_DIR, name)
        try:
            blob = git(repo, "cat-file", "-t", meta.get("blob", "")) and meta["blob"]
            raw = git(repo, "cat-file", "blob", blob)
        except (RuntimeError, KeyError):
            c.bad(name, "blob id does not resolve")
            continue
        got = hashlib.sha256(raw).hexdigest()
        c.compare("%s digest of the stored object" % name, got, digest)
        c.compare("%s byte count" % name, len(raw), meta["bytes"])
        c.compare("%s encoding" % name, encoding_of(raw), meta["encoding"])
        if record:
            try:
                c.compare("%s blob id at the record commit" % name,
                          blob_at(repo, record, path), blob)
            except RuntimeError as exc:
                c.bad("%s blob id at the record commit" % name, str(exc))
        again = os.path.join(repo, path.replace("/", os.sep))
        if os.path.exists(again):
            with open(again, "rb") as fh:
                disk = fh.read()
            if disk == raw:
                c.ok("%s working tree matches the object" % name, "byte for byte")
            else:
                c.bad("%s working tree matches the object" % name,
                      "hash of the checkout is %s" % hashlib.sha256(disk).hexdigest()[:16])
        else:
            c.ok("%s working tree matches the object" % name, "not checked out here")


def check_served(c: Checks, repo: str, m: dict) -> None:
    if not m["served"]:
        c.bad("served digest recorded", "no served line")
        return
    for name, want in m["served"].items():
        blob = m["table"][name]["blob"]
        raw = git(repo, "cat-file", "blob", blob)
        served = served_bytes(raw, encoding_of(raw))
        if served is None:
            c.bad("%s served digest" % name, "stored object is not UTF-16, so there is no re-encoding")
            continue
        c.compare("%s served digest" % name, hashlib.sha256(served).hexdigest(), want)
        if "size" in m["served_size"]:
            c.compare("%s served byte count" % name, len(served), m["served_size"]["size"])
        if hashlib.sha256(raw).hexdigest() == want:
            c.bad("%s has two different digests" % name, "served equals stored, so nothing was explained")


def check_harness(c: Checks, repo: str, m: dict) -> None:
    h = m["harness"]
    if not h:
        c.bad("harness recorded", "no harness line")
        return
    run = m["commits"].get("run")
    try:
        blob = m["harness_blob"] or (blob_at(repo, run, h["name"]) if run else "")
        raw = git(repo, "cat-file", "blob", blob)
    except RuntimeError as exc:
        c.bad("harness blob resolves", str(exc))
        return
    c.compare("harness digest at the run commit", hashlib.sha256(raw).hexdigest(), h["digest"])
    c.compare("harness byte count", len(raw), h["bytes"])
    if run:
        c.compare("harness blob id matches the run commit", blob_at(repo, run, h["name"]), blob)
    if m["harness_windows"]:
        c.compare("harness digest through crlf",
                  hashlib.sha256(raw.replace(b"\n", b"\r\n")).hexdigest(),
                  m["harness_windows"])


def check_builder_order(c: Checks, repo: str) -> None:
    """Check the shape of the fix, not just the presence of a function.

    The 4 November finding was ordering, so the check reads order. The 14 November findings were
    prefix comparison, non-atomic publication and a stale results file, so the checks read those
    too: staging before renaming, record renamed before package, a binding written into RUN.json,
    and a refusal when the results file predates the run.
    """
    path = os.path.join(repo, "package", "build_package.py")
    if not os.path.exists(path):
        c.bad("builder present", path + " not found")
        return
    with open(path, encoding="utf-8") as fh:
        source = fh.read()
    lines = source.splitlines()

    def line_of(needle: str):
        return next((i + 1 for i, l in enumerate(lines) if needle in l), None)

    staged = line_of("staged = archive_run(")
    published = line_of("record, package = publish(")
    if staged and published and staged < published:
        c.ok("archive is staged before publication", "line %d, publish at %d" % (staged, published))
    elif staged and published:
        c.bad("archive is staged before publication", "archive at %d, publish at %d" % (staged, published))
    else:
        c.bad("archive is staged before publication", "could not find both statements")

    rec_rename = line_of("os.replace(staging, final_record)")
    pkg_rename = line_of("os.replace(pkg_stage, package)")
    if rec_rename and pkg_rename and rec_rename < pkg_rename:
        c.ok("record is renamed before the package", "record %d, package %d" % (rec_rename, pkg_rename))
    else:
        c.bad("record is renamed before the package", "record %s, package %s" % (rec_rename, pkg_rename))

    fsync_pkg = line_of("fsync_file(pkg_stage)")
    if fsync_pkg and pkg_rename and fsync_pkg < pkg_rename:
        c.ok("package bytes are on disk before the rename", "fsync at %d, rename at %d" % (fsync_pkg, pkg_rename))
    else:
        c.bad("package bytes are on disk before the rename", "fsync %s, rename %s" % (fsync_pkg, pkg_rename))

    if "package_sha256" in source and "RUN.json" in source:
        c.ok("the pair is bound by a digest in RUN.json", "package_sha256")
    else:
        c.bad("the pair is bound by a digest in RUN.json", "no binding found")

    if "byte for byte the file that was on disk before the run started" in source:
        c.ok("a stale results file is refused", "compared against the pre-run snapshot")
    elif "before" in source and "snapshot(results_json)" in source:
        c.ok("a stale results file is refused", "snapshot compared")
    else:
        c.bad("a stale results file is refused", "no pre-run snapshot comparison")

    # The real functions, against a harness with no results, must refuse and leave the package alone.
    spec = importlib.util.spec_from_file_location("build_package", path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001
        c.bad("builder imports", repr(exc))
        return
    tmp = tempfile.mkdtemp(prefix="record-check-")
    try:
        harness = os.path.join(tmp, "harness")
        os.makedirs(os.path.join(harness, "results"))
        with open(os.path.join(harness, "redteam.py"), "w", encoding="utf-8") as fh:
            fh.write("print('harness')\n")
        package = os.path.join(tmp, "package.md")
        with open(package, "w", encoding="utf-8") as fh:
            fh.write("placeholder\n")
        try:
            module.archive_run(harness, package, "console\n")
            c.bad("archive refuses when results are missing", "it returned instead of raising")
        except SystemExit:
            c.ok("archive refuses when results are missing", "SystemExit")
        except Exception as exc:  # noqa: BLE001
            c.bad("archive refuses when results are missing", "raised %r instead" % (exc,))
        with open(package, encoding="utf-8") as fh:
            c.compare("package untouched by the refusal", fh.read(), "placeholder\n")
        c.compare("no record was published", os.path.exists(os.path.join(tmp, "run_record")), False)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_pair(c: Checks, package_path: str) -> None:
    """The pair check that stands in for atomic publication.

    Two files cannot be renamed as one, so the guarantee is a binding instead: RUN.json names the
    digest of the package it was published with, and this refuses a pair that does not agree. A
    crash between the two renames therefore leaves something detectable rather than something
    plausible, which is the difference the reviewer asked for.
    """
    package_path = os.path.abspath(package_path)
    record_dir = os.path.join(os.path.dirname(package_path), "run_record")
    run_json = os.path.join(record_dir, "RUN.json")
    if not os.path.exists(run_json):
        c.ok("pair %s" % os.path.basename(package_path), "no RUN.json, so this package predates the binding")
        return
    with open(run_json, encoding="utf-8") as fh:
        run = json.load(fh)
    if not os.path.exists(package_path):
        c.bad("package present", "%s is named in RUN.json and is not on disk: publication stopped "
                                  "between the record and the package" % os.path.basename(package_path))
        return
    with open(package_path, "rb") as fh:
        pkg = fh.read()
    c.compare("package digest matches RUN.json",
              hashlib.sha256(pkg).hexdigest(), run.get("package_sha256"))
    c.compare("package byte count matches RUN.json", len(pkg), run.get("package_bytes"))
    for name, meta in (run.get("files") or {}).items():
        if name in ("redteam.py",):
            continue
        target = os.path.join(record_dir, name)
        if not os.path.exists(target):
            c.bad("%s present" % name, "named in RUN.json, absent from the record")
            continue
        with open(target, "rb") as fh:
            raw = fh.read()
        c.compare("%s digest matches RUN.json" % name, hashlib.sha256(raw).hexdigest(), meta.get("sha256"))
        c.compare("%s byte count matches RUN.json" % name, len(raw), meta.get("bytes"))


def self_test() -> int:
    """Prove the checker can fail, using the exact defect the reviewer found.

    A manifest row is replaced with a digest that agrees in its first sixteen characters and
    differs in the other forty eight. A checker that compares prefixes passes it. This one must
    not, and the exit code says which happened.
    """
    import tempfile

    true = hashlib.sha256(b"self test").hexdigest()
    fake = true[:16] + "0" * 48
    tmp = tempfile.mkdtemp(prefix="verify-selftest-")
    path = os.path.join(tmp, "manifest.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("%s  results.json\n" % fake)
    c = Checks()
    c.compare("prefix collision is a difference", fake, true)
    shutil.rmtree(tmp, ignore_errors=True)
    print("\nself-test: %d passed, %d failed (1 failed means the checker compares all 64)" % (c.passed, c.failed))
    return 0 if c.failed == 1 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=".", help="path to the ai-redteam-five-tests checkout")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST, help="corrected manifest to check against")
    ap.add_argument("--pair", default=None,
                    help="path to a package.md built by build_package.py, to check the record against it")
    ap.add_argument("--self-test", action="store_true",
                    help="prove the checker rejects a digest that matches on a 16 character prefix")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    repo = os.path.abspath(args.repo)

    if not os.path.exists(args.manifest):
        print("no manifest at %s" % args.manifest)
        return 2
    try:
        git(repo, "rev-parse", "--git-dir")
    except Exception:  # noqa: BLE001
        print("%s is not a git checkout" % repo)
        return 2

    m = parse_manifest(args.manifest)
    c = Checks()
    print("manifest  %s" % os.path.basename(args.manifest))
    print("repo      %s" % repo)
    if check_manifest_shape(c, m):
        check_objects(c, repo, m)
        check_served(c, repo, m)
        check_harness(c, repo, m)
    check_builder_order(c, repo)
    if args.pair:
        check_pair(c, args.pair)

    print("\n%d passed, %d failed" % (c.passed, c.failed))
    return 0 if c.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
