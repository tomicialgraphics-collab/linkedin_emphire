#!/usr/bin/env bash
# Brand card, set from the owner's reference template on 2026-11-15.
# Renders a 1080x1350 LinkedIn portrait card: his photo, his name, a headline of
# up to three lines, a proportion bar and the yellow name tag.
#
# usage:
#   ./make_card.sh out.png "LINE ONE" "LINE TWO" "LINE THREE" "sub line" \
#       "CORE LABEL" "REST LABEL" core_count total_count [TAG1] [TAG2]
#
# Every card carries the photo and the name. A visual without them is not this
# brand and should not ship.

set -euo pipefail

OUT=${1:?out path}
L1=${2:-}
L2=${3:-}
L3=${4:-}
SUB=${5:-}
CORELABEL=${6:-}
RESTLABEL=${7:-}
CORE=${8:-0}
TOTAL=${9:-1}
TAG1=${10:-TOLULOPE MICHAEL}
TAG2=${11:-CYBERSECURITY EXPERT}

HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PHOTO="$HERE/headshot_tolulope_michael_400.jpg"
F=/usr/share/fonts/truetype/dejavu
BOLD="$F/DejaVuSans-Bold.ttf"
REG="$F/DejaVuSans.ttf"

BG="#FBFBF9"
INK="#0B0B0B"
GREY="#5A5A5A"
RULE="#E7E4DB"
YELLOW="#F9D811"

W=1080
H=1350
M=72
INNER=$((W - 2 * M))
BAR=$(( INNER * CORE / TOTAL ))
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# 1. circular avatar, 104px, for the header
convert "$PHOTO" -resize 104x104^ -gravity center -extent 104x104 "$TMP/face.png"
convert -size 104x104 xc:black -fill white -draw "circle 52,52 52,1" "$TMP/mask.png"
convert "$TMP/face.png" "$TMP/mask.png" -alpha off -compose CopyOpacity -composite "$TMP/avatar.png"

# 2. circular portrait, 240px, for the lower right
convert "$PHOTO" -resize 240x240^ -gravity center -extent 240x240 "$TMP/face2.png"
convert -size 240x240 xc:black -fill white -draw "circle 120,120 120,1" "$TMP/mask2.png"
convert "$TMP/face2.png" "$TMP/mask2.png" -alpha off -compose CopyOpacity -composite "$TMP/portrait.png"

convert -size ${W}x${H} xc:"$BG" \
  -stroke none \
  -draw "fill $YELLOW rectangle ${M},196 300,232" \
  -draw "fill $RULE rectangle 0,1030 ${W},1031" \
  -draw "fill $RULE rectangle ${M},770 $((M + INNER)),814" \
  -draw "fill $YELLOW rectangle ${M},770 $((M + BAR)),814" \
  -draw "fill $YELLOW roundrectangle ${M},890 632,974 42,42" \
  -draw "fill $YELLOW rectangle ${M},1120 520,1252" \
  -font "$BOLD" -pointsize 26 -fill "$INK" -annotate +$((M + 18))+222 "AI RED TEAMING" \
  -font "$BOLD" -pointsize 108 -fill "$INK" \
  -annotate +${M}+392 "$L1" \
  -annotate +${M}+510 "$L2" \
  -annotate +${M}+628 "$L3" \
  -font "$REG" -pointsize 34 -fill "$GREY" -annotate +${M}+700 "$SUB" \
  -font "$BOLD" -pointsize 26 -fill "$INK" -annotate +${M}+862 "$CORELABEL" \
  -font "$REG" -pointsize 26 -fill "$GREY" \
  -annotate +$(( W - M - ${#RESTLABEL} * 15 ))+862 "$RESTLABEL" \
  -font "$BOLD" -pointsize 27 -fill "$INK" -annotate +$((M + 34))+942 "Follow for more on agent security" \
  -font "$BOLD" -pointsize 30 -fill "$INK" -annotate +$((M + 32))+1172 "$TAG1" \
  -font "$REG" -pointsize 24 -fill "$INK" -annotate +$((M + 32))+1208 "$TAG2" \
  -font "$BOLD" -pointsize 34 -fill "$INK" -annotate +$((M + 128))+112 "Tolulope Michael" \
  -font "$REG" -pointsize 22 -fill "$GREY" -annotate +$((M + 128))+146 "Software engineer, AI red teaming" \
  "$TMP/avatar.png" -geometry +${M}+56 -composite \
  "$TMP/portrait.png" -geometry +$((W - M - 240))+1076 -composite \
  "$OUT"

echo "wrote $OUT"
