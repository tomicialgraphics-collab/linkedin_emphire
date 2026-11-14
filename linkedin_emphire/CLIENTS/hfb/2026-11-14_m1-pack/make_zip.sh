#!/bin/sh
# Builds the delivery zip deterministically: same bytes in, same bytes out.
#
#   ./make_zip.sh            writes ./M1-pack-host-failure-benchmark-2026-11-14.zip
#
# Fixed entry order, fixed timestamps, fixed permissions. A zip whose hash changes every time
# it is built cannot be checked against a hash printed in a message.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
OUT=${1:-$HERE/M1-pack-host-failure-benchmark-2026-11-14.zip}
python3 - "$HERE" "$OUT" <<'PY'
import os, sys, zipfile
root, out = sys.argv[1], sys.argv[2]
paths = []
for base, dirs, files in os.walk(root):
    dirs.sort()
    for name in sorted(files):
        full = os.path.join(base, name)
        rel = os.path.relpath(full, root)
        if rel.endswith(".zip") or "__pycache__" in rel or ".pyc" in rel:
            continue
        paths.append(rel)
paths.sort()
with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for rel in paths:
        info = zipfile.ZipInfo(rel, date_time=(2026, 11, 14, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        with open(os.path.join(root, rel), "rb") as fh:
            zf.writestr(info, fh.read())
print("%d files" % len(paths))
PY
sha256sum "$OUT"
