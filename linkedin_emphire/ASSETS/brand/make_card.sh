#!/usr/bin/env bash
# Brand card, 1080x1350, for LinkedIn.
# Layout learned from the owner's reference card on 2026-11-15. The name is the
# owner's, Olusanya Timothy. The reference card belonged to somebody else and
# its name was copied across by mistake once, which is why NAME is a variable
# here and why it is never taken from a design.
#
# usage:
#   ./make_card.sh out.png "LINE ONE" "LINE TWO" "LINE THREE" "sub line" \
#       "CORE LABEL" "REST LABEL" core_count total_count [NAME] [SECOND TAG LINE]

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
NAME=${10:-Olusanya Timothy}
TAG2=${11:-SOFTWARE ENGINEER, AI RED TEAMING}
STRAP="Lagos, Nigeria · AI red teaming, in public"

HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PHOTO="$HERE/headshot_400.jpg"
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

circle () { # src size out
  convert "$1" -resize "$2x$2^" -gravity center -extent "$2x$2" "$TMP/f.png"
  convert -size "$2x$2" xc:black -fill white -draw "circle $(( $2 / 2 )),$(( $2 / 2 )) $(( $2 / 2 )),1" "$TMP/m.png"
  convert "$TMP/f.png" "$TMP/m.png" -alpha off -compose CopyOpacity -composite "$3"
}

circle "$PHOTO" 96 "$TMP/avatar.png"
circle "$PHOTO" 372 "$TMP/portrait.png"

convert -size ${W}x${H} xc:"$BG" \
  -stroke none \
  -draw "fill $YELLOW rectangle ${M},196 300,232" \
  -draw "fill $RULE rectangle ${M},792 $((M + INNER)),836" \
  -draw "fill $YELLOW rectangle ${M},792 $((M + BAR)),836" \
  -draw "fill $YELLOW roundrectangle ${M},900 632,984 42,42" \
  -draw "fill $YELLOW rectangle ${M},1104 596,1256" \
  -font "$BOLD" -pointsize 26 -fill "$INK" -annotate +$((M + 18))+222 "AI RED TEAMING" \
  -font "$BOLD" -pointsize 108 -fill "$INK" \
  -annotate +${M}+392 "$L1" \
  -annotate +${M}+510 "$L2" \
  -annotate +${M}+628 "$L3" \
  -font "$REG" -pointsize 34 -fill "$GREY" -annotate +${M}+700 "$SUB" \
  -font "$BOLD" -pointsize 26 -fill "$INK" -annotate +${M}+884 "$CORELABEL" \
  -font "$REG" -pointsize 26 -fill "$GREY" \
  -annotate +$(( W - M - ${#RESTLABEL} * 15 ))+884 "$RESTLABEL" \
  -font "$BOLD" -pointsize 27 -fill "$INK" -annotate +$((M + 34))+952 "Follow for more on agent security" \
  -font "$BOLD" -pointsize 40 -fill "$INK" -annotate +$((M + 36))+1180 "$NAME" \
  -font "$REG" -pointsize 22 -fill "$INK" -annotate +$((M + 36))+1218 "$TAG2" \
  -font "$BOLD" -pointsize 36 -fill "$INK" -annotate +$((M + 120))+108 "$NAME" \
  -font "$REG" -pointsize 22 -fill "$GREY" -annotate +$((M + 120))+144 "$STRAP" \
  "$TMP/avatar.png" -geometry +${M}+60 -composite \
  "$TMP/portrait.png" -geometry +$((W - M - 372))+938 -composite \
  "$OUT"

echo "wrote $OUT"
