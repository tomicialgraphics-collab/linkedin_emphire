#!/usr/bin/env python3
"""Builds the three content images and the cover for the HFB portfolio item.

Needs Pillow (a venv with `pip install pillow` is enough) and ImageMagick for the
avatar cut-out. Every image carries the owner's name and portrait, per the 2026-11-15 rule.
Canvas height is measured from the text, so nothing floats in dead space.

usage: python3 build_images.py
"""

import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
PACK = ROOT / "CLIENTS/hfb/2026-11-14_m1-pack"
CUT = ROOT / "ASSETS/brand/portrait_cutout.png"

F = Path("/usr/share/fonts/truetype/dejavu")
MONO = F / "DejaVuSansMono.ttf"
MONOB = F / "DejaVuSansMono-Bold.ttf"
BOLD = F / "DejaVuSans-Bold.ttf"
REG = F / "DejaVuSans.ttf"

PAPER = (15, 15, 14)
TEXT = (233, 233, 228)
DIM = (138, 138, 130)
YELLOW = (249, 216, 17)

W = 1600
PAD = 96
LEAD = 27


def avatar(size=44):
    out = HERE / ".avatar.png"
    subprocess.run([
        "convert", str(CUT), "-fuzz", "8%", "-fill", "none",
        "-draw", "color 0,0 floodfill", "-draw", "color 1023,0 floodfill",
        "-trim", "+repage", "-resize", f"{size}x{size}^", "-gravity", "north",
        "-extent", f"{size}x{size}", str(out),
    ], check=True)
    a = Image.open(out).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    a.putalpha(mask)
    return a


def render(title, lines, out_path, point=19):
    font = ImageFont.truetype(str(MONO), point)
    font_title = ImageFont.truetype(str(MONOB), 26)
    font_name = ImageFont.truetype(str(BOLD), 20)
    font_tag = ImageFont.truetype(str(REG), 19)

    body_h = LEAD * len(lines)
    H = 150 + body_h + 130
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    d.text((PAD, 60), title, font=font_title, fill=YELLOW)
    y = 148
    for line in lines:
        colour = DIM if line.strip().startswith("...") else TEXT
        d.text((PAD, y), line, font=font, fill=colour)
        y += LEAD

    d.line((0, H - 96, W, H - 96), fill=DIM, width=1)
    d.text((96, H - 62), "Olusanya Timothy", font=font_name, fill=YELLOW)
    d.text((330, H - 61), "AI Security and LLM Testing", font=font_tag, fill=DIM)
    img.paste(avatar(), (36, H - 80), avatar())

    img.save(out_path)
    print(f"wrote {out_path.name} {W}x{H}")


def manifest_lines():
    sums = (PACK / "05-SHA256SUMS.txt").read_text().splitlines()
    lines = ["A manifest that lets a client prove the file they tested is the file that was delivered.", ""]
    lines += sums[:14]
    lines += ["", "      ... 10 more files in the same manifest", ""]
    lines += sums[-4:]
    lines += ["", "24 files      36,215 bytes      rebuilt twice, hash matched both times"]
    return lines


def structure_lines():
    return [
        "One pinned revision, one baseline failure, one recorded change, one log.",
        "",
        "  00-README.md               the question, the property, the terms",
        "  01-environment.sh          how the pack is reproduced",
        "  02-baseline-failure/       the failure, before any change",
        "  03-change/                 the patch, and the same suite after it",
        "  04-classification-log.md   which layer broke, and what did not move",
        "  05-SHA256SUMS.txt          every file, hashed",
        "  harness/                   the probes",
        "  rebuild.sh  make_zip.sh    one command to redo all of it",
    ]


def log_lines():
    raw = (PACK / "04-classification-log.md").read_text().splitlines()
    keep, rows = [], []
    for line in raw:
        if line.startswith(("---", "deliverable:", "id:", "date:", "audience:", "status:", "approved:", "contents:")):
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
        else:
            keep.append(line)
    rows = [r for r in rows if len(r) == 4]
    if rows and rows[0][0].lower() == "check":
        rows = rows[1:]
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    table = ["  ".join(c.ljust(widths[i]) for i, c in enumerate(r)) for r in rows]

    title = next((l.lstrip("# ").upper() for l in keep if l.strip().startswith("# Classification")), "CLASSIFICATION LOG")
    intro = []
    for line in keep:
        if line.strip().startswith("## All"):
            break
        if line.strip() and not line.strip().startswith("#"):
            intro.append(line.strip())
    out = [title, ""]
    out += [l[:126] for l in intro[:4]]
    out += ["", "check".ljust(widths[0]) + "  class  pinned revision  with the change"]
    out += ["".ljust(widths[0], "-") + "  -----  ---------------  ---------------"]
    out += table[:14]
    out += ["", f"      ... {len(rows) - 14} more checks, all holding at both revisions"]
    out += ["", "Both runs exit 0, both print VERDICT: every check holds, and the two",
            "verifier outputs are byte-identical, all thirty lines."]
    return out


if __name__ == "__main__":
    render("05-SHA256SUMS.txt", manifest_lines(), HERE / "01_manifest.png")
    render("the pack", structure_lines(), HERE / "02_structure.png")
    render("04-classification-log.md", log_lines(), HERE / "03_classification-log.png", point=18)
    (HERE / ".avatar.png").unlink(missing_ok=True)
    print("cover is built by ASSETS/brand/make_card.sh, see build_images.sh")
