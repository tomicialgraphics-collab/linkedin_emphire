#!/usr/bin/env bash
# Brand card, 1080x1350, rebuilt to the reference layout the owner supplied on
# 2026-11-15: off-white ground, cut-out portrait standing over a desk, centred
# condensed headline, yellow follow pill, yellow name tag.
#
# The name is the owner's, Olusanya Timothy, and it is a variable here so a
# design can never supply one again.
#
# usage:
#   ./make_card.sh out.png "LINE ONE" "LINE TWO" "LINE THREE" [NAME] [TAG2]

set -euo pipefail

OUT=${1:?out path}
L1=${2:-}
L2=${3:-}
L3=${4:-}
NAME=${5:-Olusanya Timothy}
TAG2=${6:-AI RED TEAMING}

HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
CUT="$HERE/portrait_cutout.png"
F=/usr/share/fonts/truetype/dejavu
BOLD="$F/DejaVuSans-Bold.ttf"
REG="$F/DejaVuSans.ttf"

BG="#FCFCFA"
INK="#0B0B0B"
GREY="#4E4E4E"
YELLOW="#F9D811"

W=1080
H=1350
M=86
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# 1. portrait, keys the flat white ground out, then trims to the figure
convert "$CUT" -fuzz 8% -fill none -draw "color 0,0 floodfill" -draw "color 1023,0 floodfill" \
  -trim +repage -modulate 100,90 -resize x600 "$TMP/figure.png"
FW=$(identify -format %w "$TMP/figure.png")
FH=$(identify -format %h "$TMP/figure.png")
FX=$(( (W - FW) / 2 ))
FY=$(( 1248 - FH ))

# 2. desk, a warm gradient with a lit edge
convert -size ${W}x110 gradient:'#7A4E2A-#2E1A0C' -fill '#8A5B33' -draw "rectangle 0,0 ${W},3" "$TMP/desk.png"

# 3. header avatar
convert "$CUT" -resize 66x66^ -gravity north -extent 66x66 "$TMP/a.png"
convert -size 66x66 xc:black -fill white -draw "circle 33,33 33,1" "$TMP/am.png"
convert "$TMP/a.png" "$TMP/am.png" -alpha off -compose CopyOpacity -composite "$TMP/avatar.png"

# 4. the card
convert -size ${W}x${H} xc:"$BG" \
  -stroke none \
  -font "$BOLD" -pointsize 104 -fill "$INK" -gravity north \
  -annotate +0+190 "$L1" \
  -annotate +0+318 "$L2" \
  -annotate +0+446 "$L3" \
  -gravity northwest \
  "$TMP/figure.png" -geometry +${FX}+${FY} -composite \
  "$TMP/desk.png" -geometry +0+1240 -composite \
  -fill "$YELLOW" -draw "roundrectangle ${M},700 404,812 18,18" \
  -fill "$INK" -draw "circle 120,730 120,720" -draw "roundrectangle 102,744 138,778 17,17" \
  -draw "rectangle 146,720 158,725" -draw "rectangle 149,717 155,728" \
  -font "$BOLD" -pointsize 14 -fill "$INK" -annotate +162+740 "Follow @${NAME}" \
  -font "$REG" -pointsize 14 -fill "$INK" -annotate +162+766 "for more insight on" \
  -annotate +162+788 "agent security" \
  -fill "$YELLOW" -draw "rectangle 700,800 1024,892" \
  -font "$BOLD" -pointsize 25 -fill "$INK" -annotate +722+842 "$(echo "$NAME" | tr '[:lower:]' '[:upper:]')" \
  -font "$REG" -pointsize 17 -fill "$INK" -annotate +722+872 "$TAG2" \
  -font "$BOLD" -pointsize 30 -fill "$INK" -annotate +$((M + 80))+108 "$NAME" \
  "$TMP/avatar.png" -geometry +${M}+68 -composite \
  "$OUT"

echo "wrote $OUT"
