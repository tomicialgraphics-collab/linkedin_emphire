#!/usr/bin/env bash
# apply-and-run.sh <patch-or-zip> [verifier-zip]
#
# Applies Marvin's patch (or unpacks his zip) onto a clean copy of the WP-1
# verifier, then runs the conformance suite and foray-probe.mjs against it.
#
# Defaults:
#   verifier zip : /home/user/foray-review/material/foray-wp1-verifier-b890d2c-v0_1.zip
#   probe        : /home/user/foray-review/repro/foray-probe.mjs
#   work dir     : /tmp/foray/patched  (rebuilt on every run)
#
# Exit 0 when the patch applied and both runs completed, whatever they found.
# Exit 3 when the patch did not apply, with the reason printed.

set -u

PATCH="${1:-}"
VERIFIER_ZIP="${2:-/home/user/foray-review/material/foray-wp1-verifier-b890d2c-v0_1.zip}"
PROBE="/home/user/foray-review/repro/foray-probe.mjs"
WORK="/tmp/foray/patched"

if [ -z "$PATCH" ] || [ ! -f "$PATCH" ]; then
  echo "usage: apply-and-run.sh <patch-or-zip> [verifier-zip]"
  exit 3
fi

echo "patch      : $PATCH"
echo "sha256     : $(sha256sum "$PATCH" | cut -d' ' -f1)"
echo "verifier   : $VERIFIER_ZIP"
echo ""

rm -rf "$WORK"
mkdir -p "$WORK/base"
unzip -q "$VERIFIER_ZIP" -d "$WORK/base" || { echo "could not unpack the verifier zip"; exit 3; }

ROOT="$WORK/base"
if [ ! -d "$ROOT/verifier" ] && [ -d "$ROOT/lib" ]; then
  ROOT="$ROOT"
elif [ -d "$ROOT/verifier" ]; then
  ROOT="$ROOT/verifier"
fi
echo "verifier root: $ROOT"

cp -r "$ROOT" "$WORK/tree"
TREE="$WORK/tree"

echo ""
echo "=== applying ==="
APPLIED=0
case "$PATCH" in
  *.zip)
    unzip -q "$PATCH" -d "$WORK/incoming" && echo "unpacked zip" || { echo "bad zip"; exit 3; }
    # a zip of the branch replaces the tree wholesale
    if [ -d "$WORK/incoming/verifier" ]; then
      rm -rf "$TREE"; cp -r "$WORK/incoming/verifier" "$TREE"
    elif [ -f "$WORK/incoming/lib/streams.mjs" ]; then
      rm -rf "$TREE"; cp -r "$WORK/incoming" "$TREE"
    else
      cp -r "$WORK/incoming/." "$TREE/"
    fi
    APPLIED=1
    ;;
  *)
    if ( cd "$TREE" && git apply --check "$PATCH" ) 2>/dev/null; then
      ( cd "$TREE" && git apply "$PATCH" ) && APPLIED=1 && echo "git apply: ok"
    elif ( cd "$TREE" && git apply -p1 --check "$PATCH" ) 2>/dev/null; then
      ( cd "$TREE" && git apply -p1 "$PATCH" ) && APPLIED=1 && echo "git apply -p1: ok"
    elif ( cd "$TREE" && patch -p1 --forward --dry-run < "$PATCH" ) >/dev/null 2>&1; then
      ( cd "$TREE" && patch -p1 --forward < "$PATCH" ) && APPLIED=1 && echo "patch -p1: ok"
    elif ( cd "$TREE" && patch -p0 --forward --dry-run < "$PATCH" ) >/dev/null 2>&1; then
      ( cd "$TREE" && patch -p0 --forward < "$PATCH" ) && APPLIED=1 && echo "patch -p0: ok"
    fi
    ;;
esac

if [ "$APPLIED" -ne 1 ]; then
  echo "the patch did not apply to $TREE"
  echo "first 20 lines of the patch:"
  head -20 "$PATCH"
  exit 3
fi

echo ""
echo "=== changed files ==="
( cd "$ROOT" && diff -rq "$ROOT" "$TREE" 2>/dev/null | head -20 ) || true

echo ""
echo "=== streams.mjs sha256 (base then patched) ==="
sha256sum "$ROOT/lib/streams.mjs" 2>/dev/null
sha256sum "$TREE/lib/streams.mjs" 2>/dev/null

echo ""
echo "=== conformance suite ==="
( cd "$TREE" && node --test test/run-vectors.mjs 2>&1 | grep -E "^# (tests|pass|fail)" )

echo ""
echo "=== foray-probe ==="
node "$PROBE" "$TREE"
