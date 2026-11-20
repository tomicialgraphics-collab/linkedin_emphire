#!/usr/bin/env bash
# Builds the three content images and the cover for the HFB portfolio item.
# Every image carries the owner's name and portrait, per the 2026-11-15 rule.
# Canvas height is measured from the text rather than fixed, so nothing floats in dead space.
#
# usage: ./build_images.sh

set -euo pipefail

HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT="$HERE/../../.."
PACK="$ROOT/CLIENTS/hfb/2026-11-14_m1-pack"
CUT="$ROOT/ASSETS/brand/portrait_cutout.png"
F=/usr/share/fonts/truetype/dejavu
BOLD="$F/DejaVuSans-Bold.ttf"
REG="$F/DejaVuSans.ttf"
MONO="$F/DejaVuSansMono.ttf"
MONOB="$F/DejaVuSansMono-Bold.ttf"

PAPER="#0F0F0E"
TEXT="#E9E9E4"
DIM="#8A8A82"
YELLOW="#F9D811"

W=1600
PAD=96
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# footer avatar, 44px, keyed from the flat white ground
convert "$CUT" -fuzz 8% -fill none -draw "color 0,0 floodfill" -draw "color 1023,0 floodfill" \
  -trim +repage -resize 44x44^ -gravity north -extent 44x44 "$TMP/a.png"
convert -size 44x44 xc:black -fill white -draw "circle 22,22 22,1" "$TMP/am.png"
convert "$TMP/a.png" "$TMP/am.png" -alpha off -compose CopyOpacity -composite "$TMP/avatar.png"

# render_one <body.txt> <title> <out.png>
render_one () {
  local body="$1" title="$2" out="$3"
  local TXT; TXT=$(cat "$body")
  convert -background "$PAPER" -fill "$TEXT" -font "$MONO" -pointsize 19 \
    -size $((W - 2*PAD))x label:"$TXT" "$TMP/body.png"
  local BH; BH=$(identify -format %h "$TMP/body.png")
  local H=$((150 + BH + 130))

  convert -size ${W}x${H} xc:"$PAPER" \
    -fill "$YELLOW" -font "$MONOB" -pointsize 26 -gravity northwest -annotate +${PAD}+64 "$title" \
    "$out"
  convert "$out" "$TMP/body.png" -gravity northwest -geometry +${PAD}+140 -composite "$out"

  convert "$out" \
    -fill "$DIM" -draw "line 0,$((H-96)) $W,$((H-96))" \
    -fill "$YELLOW" -font "$BOLD" -pointsize 20 -gravity southwest -annotate +96+48 "Olusanya Timothy" \
    -fill "$DIM" -font "$REG" -pointsize 19 -gravity southwest -annotate +330+49 "AI Security and LLM Testing" \
    "$out"
  convert "$out" "$TMP/avatar.png" -gravity southwest -geometry +36+34 -composite "$out"
  echo "wrote $out (${W}x${H})"
}

# 1. the manifest
{
  echo "A manifest that lets a client prove the file they tested is the file that was delivered."
  echo ""
  head -n 14 "$PACK/05-SHA256SUMS.txt"
  echo ""
  echo "   ... 10 more files in the same manifest"
  echo ""
  tail -n 4 "$PACK/05-SHA256SUMS.txt"
  echo ""
  echo "24 files     36,215 bytes     rebuilt twice, hash matched both times"
} > "$TMP/manifest.txt"
render_one "$TMP/manifest.txt" "05-SHA256SUMS.txt" "$HERE/01_manifest.png"

# 2. the structure
{
  echo "One pinned revision, one baseline failure, one recorded change, one log."
  echo ""
  echo "  00-README.md               the question, the property, the terms"
  echo "  01-environment.sh          how the pack is reproduced"
  echo "  02-baseline-failure/       the failure, before any change"
  echo "  03-change/                 the patch, and the same suite after it"
  echo "  04-classification-log.md   which layer broke, and what did not move"
  echo "  05-SHA256SUMS.txt          every file, hashed"
  echo "  harness/                   the probes"
  echo "  rebuild.sh  make_zip.sh    one command to redo all of it"
} > "$TMP/tree.txt"
render_one "$TMP/tree.txt" "the pack" "$HERE/02_structure.png"

# 3. the classification log, table aligned rather than piped raw
python3 - "$PACK/04-classification-log.md" > "$TMP/log.txt" <<'PY'
import re, sys
src = open(sys.argv[1], encoding="utf-8").read().splitlines()
body = [l for l in src if not l.startswith(("---", "deliverable:", "id:", "date:", "audience:", "status:", "approved:", "contents:"))]
out, rows = [], []
for line in body:
    if line.startswith("|"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    else:
        if rows:
            out.extend(rows); out.append("")
            rows = []
        out.append(line)
if rows:
    out.extend(rows)
w = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))] if rows else []
fixed = []
for r in rows:
    fixed.append("  ".join(c.ljust(w[i]) for i, c in enumerate(r)))
# replace the raw rows in the output with the aligned ones
res, idx = [], 0
for line in out:
    if line.startswith("| "):
        continue
    res.append(line)
    if line.strip() == "## All twenty-two checks":
        res.append("")
        res.extend(fixed)
res.extend(["", "Both runs exit 0, both print VERDICT: every check holds, and the two verifier", "outputs are byte-identical."])
print("\n".join(res).replace("\n\n\n", "\n\n").strip())
PY
render_one "$TMP/log.txt" "04-classification-log.md" "$HERE/03_classification-log.png"

# 4. the cover card, brand layout
"$ROOT/ASSETS/brand/make_card.sh" "$HERE/04_cover.png" \
  "REPRODUCIBLE" "AGENT FAILURES" "HASHED, PINNED" "Olusanya Timothy" "EVALS AND VERIFICATION"

ls -l "$HERE"/*.png
