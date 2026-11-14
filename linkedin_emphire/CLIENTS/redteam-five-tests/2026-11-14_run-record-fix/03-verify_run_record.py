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
        if got == want:
            self.ok(label, str(got)[:24])
        else:
            self.bad(label, "got %s, manifest says %s" % (str(got)[:24], str(want)[:24]))


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
        c.compare("%s digest of the stored object" % name, got[:16], digest[:16])
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
        c.compare("%s served digest" % name, hashlib.sha256(served).hexdigest()[:16], want[:16])
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
    c.compare("harness digest at the run commit", hashlib.sha256(raw).hexdigest()[:16], h["digest"][:16])
    c.compare("harness byte count", len(raw), h["bytes"])
    if run:
        c.compare("harness blob id matches the run commit", blob_at(repo, run, h["name"]), blob)
    if m["harness_windows"]:
        c.compare("harness digest through crlf",
                  hashlib.sha256(raw.replace(b"\n", b"\r\n")).hexdigest()[:16],
                  m["harness_windows"][:16])


def check_builder_order(c: Checks, repo: str) -> None:
    path = os.path.join(repo, "package", "build_package.py")
    if not os.path.exists(path):
        c.bad("builder present", path + " not found")
        return
    with open(path, encoding="utf-8") as fh:
        source = fh.read()
    lines = source.splitlines()
    calls = [(i + 1, l) for i, l in enumerate(lines)
             if "archive_run(" in l and not l.lstrip().startswith("def ")]
    archive_line = calls[0][0] if calls else None
    write_line = next((i + 1 for i, l in enumerate(lines) if "package.write_text(text" in l), None)
    if archive_line is None or write_line is None:
        c.bad("builder archives before it publishes", "could not find both statements")
        return
    if archive_line < write_line:
        c.ok("builder archives before it publishes", "archive line %d, write line %d"
             % (archive_line, write_line))
    else:
        c.bad("builder archives before it publishes",
              "archive line %d comes after write line %d" % (archive_line, write_line))
    if "record = archive_run" in source:
        c.ok("the archive result is held, not discarded", "record = archive_run(...)")
    else:
        c.bad("the archive result is held, not discarded", "return value is ignored")

    # The real function, against a harness with no results, must refuse and leave the package
    # exactly as it was. This is the defect as a test rather than as a comment.
    spec = importlib.util.spec_from_file_location("build_package", path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001 - any failure to import is a failure to test
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
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=".", help="path to the ai-redteam-five-tests checkout")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST, help="corrected manifest to check against")
    args = ap.parse_args()
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

    print("\n%d passed, %d failed" % (c.passed, c.failed))
    return 0 if c.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
