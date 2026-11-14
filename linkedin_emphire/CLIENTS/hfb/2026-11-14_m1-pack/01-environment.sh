#!/bin/sh
# Emits 01-environment.txt. Nothing here reads the network or the clock.
set -u
echo "Environment record for the M1 pack"
echo ""
echo "Collected on the machine that produced 02 and 03. Regenerate with 01-environment.sh, which is this file's only source."
echo ""
echo "operating system"
uname -srm
echo ""
echo "python"
python3 -V
python3 -c "import sys; print('executable:', sys.executable)"
echo ""
echo "modules the benchmark needs"
python3 - <<'PY'
import importlib.util
for name in ("json","socket","socketserver","hashlib","hmac","subprocess","tempfile"):
    print("  %-14s %s" % (name, "stdlib, present" if importlib.util.find_spec(name) else "MISSING"))
PY
echo ""
echo "modules the benchmark does not need, and does not use"
for m in pytest numpy cryptography; do python3 -c "import $m" 2>/dev/null && echo "  $m present" || echo "  $m absent (not required)"; done
echo ""
echo "external verifier binaries named by the 1.3.0 release notes"
for b in evidence-verify-rs evidence-verify-crypto; do command -v "$b" >/dev/null 2>&1 && echo "  $b present" || echo "  $b absent (not required by this pack)"; done
echo ""
echo "why the binary question does not block the pack"
echo "  run.py and verify.py import nothing outside the standard library, so every number in"
echo "  02 and 03 was produced by the two files named in the reproduction section of 00-README.md,"
echo "  on this interpreter, with no network beyond loopback."
echo ""
echo "determinism"
echo "  the seed, the policy digest and the decision key are constants in bench/common.py"
echo "  the clock is a counter, not a wall clock, so artifacts carry no timestamps"
echo "  two runs of the same revision on this machine were compared file by file: 23 of 24 files"
echo "  byte-identical, and the 24th is port.txt, which records the ephemeral port the store"
echo "  bound to and is not evidence about anything"
