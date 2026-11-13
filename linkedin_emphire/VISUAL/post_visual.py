#!/usr/bin/env python3
"""Render the visual that ships with a post, in the house card system.

The system is taken from the templates in the client's Drive folder (September to
December 2025): a white ground, an identity chip at the top of every card, a heavy
black headline that fills the upper half, one yellow accent, and nothing else. The
cards are 1080x1350, the 4:5 ratio LinkedIn renders largest in the feed and uses for
document carousels.

Two outputs per post:

    cover.png       one 1080x1350 card, headline and box, for a text post
    carousel.pdf    cover plus body pages, for a document post

    python3 VISUAL/post_visual.py VERIFIED_POSTS/<slug>/post.md
    python3 VISUAL/post_visual.py VERIFIED_POSTS/<slug>/post.md --pages 6

Nothing here invents a photograph or an illustration. The cards are type-led on
purpose: a stock 3D object would be the one thing on the card that says nothing true.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
EMPIRE = HERE.parent

# The Base Neue files in DESIGN/fonts are trials: every digit is stamped with the
# foundry's watermark, which is both a licence problem and a visible defect on any
# card that carries a number. These cards carry numbers by rule, so the house faces
# are DejaVu, which is free, clean and present on every machine that runs this.
FONT_BOLD = EMPIRE / "manual" / "build" / "fonts" / "DejaVuSans-Bold.ttf"
FONT_REGULAR = EMPIRE / "manual" / "build" / "fonts" / "DejaVuSans.ttf"
AVATAR = HERE / "assets" / "avatar.jpg"

W, H = 1080, 1350
MARGIN = 96

INK = (17, 17, 17)
PAPER = (255, 255, 255)
GREY = (110, 110, 110)
LIGHT = (232, 232, 232)
YELLOW = (245, 198, 75)
VERIFIED = (29, 155, 240)

NAME = "Olusanya Timothy"
ROLE = "AI systems testing and verification"
HANDLE = "linkedin.com/in/olusanya-timothy"

# The templates set their headlines in a compressed heavy grotesque. The house font
# is an expanded one, so it is drawn wide and then squeezed to a fixed ratio. That
# keeps one font file in the repository and still gives the headline the density the
# templates have.
HEADLINE_SQUEEZE = 0.74
LABEL_SQUEEZE = 0.80


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def draw_squeezed(canvas: Image.Image, xy: tuple[int, int], text: str,
                  face: ImageFont.FreeTypeFont, fill, squeeze: float) -> int:
    """Draw text horizontally compressed onto the canvas. Returns the drawn width.

    A separate layer per line is the only way to scale type in PIL without
    scaling the whole card, and it keeps the baseline of every line identical.
    """
    left, top, right, bottom = face.getbbox(text)
    full_w, full_h = max(right - left, 1), max(bottom - top, 1)
    layer = Image.new("RGBA", (full_w, full_h), (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((-left, -top), text, font=face, fill=fill)
    if squeeze < 0.999:
        layer = layer.resize((max(int(full_w * squeeze), 1), full_h), Image.LANCZOS)
    canvas.paste(layer, (xy[0], xy[1]), layer)
    return layer.width


def wrap(text: str, face: ImageFont.FreeTypeFont,
         max_w: float, squeeze: float = 1.0) -> list[str]:
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = (line + " " + word).strip()
        box = face.getbbox(trial)
        if (box[2] - box[0]) * squeeze <= max_w or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit_headline(text: str, max_w: float, max_h: float,
                 start: int = 116, squeeze: float = HEADLINE_SQUEEZE):
    """Largest size at which the headline fits the box, in whole lines."""
    size = start
    while size > 54:
        face = font(FONT_BOLD, size)
        lines = wrap(text, face, max_w, squeeze)
        line_h = int(size * 0.92)
        if len(lines) * line_h <= max_h and len(lines) <= 5:
            return face, lines, line_h
        size -= 4
    face = font(FONT_BOLD, 54)
    return face, wrap(text, face, max_w, squeeze), 50


def identity_chip(canvas: Image.Image, draw: ImageDraw.ImageDraw, y: int = 92) -> int:
    """Avatar, name, verified tick, role. Returns the y below the chip."""
    avatar_size = 92
    name_face = font(FONT_BOLD, 34)
    role_face = font(FONT_REGULAR, 21)

    role_w = draw.textbbox((0, 0), ROLE, font=role_face)[2]
    name_w = draw.textbbox((0, 0), NAME, font=name_face)[2]
    block_w = avatar_size + 22 + max(name_w + 40, role_w)
    x = (W - block_w) // 2

    avatar = Image.new("RGB", (avatar_size, avatar_size), LIGHT)
    if AVATAR.exists():
        photo = Image.open(AVATAR).convert("RGB")
        side = min(photo.size)
        photo = photo.crop(((photo.width - side) // 2, (photo.height - side) // 2,
                            (photo.width + side) // 2, (photo.height + side) // 2))
        avatar = photo.resize((avatar_size, avatar_size), Image.LANCZOS)
    else:
        ad = ImageDraw.Draw(avatar)
        mono = font(FONT_BOLD, 40)
        text = "OT"
        tw = ad.textbbox((0, 0), text, font=mono)[2]
        ad.text(((avatar_size - tw) // 2, 24), text, font=mono, fill=GREY)

    mask = Image.new("L", (avatar_size * 4, avatar_size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, avatar_size * 4 - 1, avatar_size * 4 - 1), fill=255)
    mask = mask.resize((avatar_size, avatar_size), Image.LANCZOS)
    canvas.paste(avatar, (x, y), mask)

    tx = x + avatar_size + 22
    draw.text((tx, y + 8), NAME, font=name_face, fill=INK)
    badge_x = tx + name_w + 14
    draw.ellipse((badge_x, y + 14, badge_x + 28, y + 42), fill=VERIFIED)
    draw.line([(badge_x + 7, y + 28), (badge_x + 12, y + 34), (badge_x + 21, y + 21)],
              fill=PAPER, width=4, joint="curve")
    draw.text((tx, y + 52), ROLE, font=role_face, fill=GREY)
    return y + avatar_size


def accent_box(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str) -> int:
    face = font(FONT_BOLD, 34)
    pad_x, pad_y = 26, 16
    tw = draw.textbbox((0, 0), text.upper(), font=face)[2]
    x, y = xy
    draw.rectangle((x, y, x + tw + pad_x * 2, y + 34 + pad_y * 2), fill=YELLOW)
    draw.text((x + pad_x, y + pad_y), text.upper(), font=face, fill=INK)
    return y + 34 + pad_y * 2


def footer(draw: ImageDraw.ImageDraw, page: int | None = None, total: int | str | None = None) -> None:
    face = font(FONT_REGULAR, 22)
    draw.line([(MARGIN, H - 132), (W - MARGIN, H - 132)], fill=LIGHT, width=2)
    draw.text((MARGIN, H - 104), HANDLE, font=face, fill=GREY)
    if page is not None:
        label = f"{page}/{total}" if total else str(page)
        tw = draw.textbbox((0, 0), label, font=face)[2]
        draw.text((W - MARGIN - tw, H - 104), label, font=face, fill=GREY)


def make_cover(headline: str, box: str | None, total: int | str | None = None) -> Image.Image:
    canvas = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(canvas)
    y = identity_chip(canvas, draw)

    ceiling = y + 96
    floor = H - 200
    face, lines, line_h = fit_headline(headline.upper(), W - MARGIN * 2, floor - ceiling - (150 if box else 0))
    block_h = len(lines) * line_h + (74 if box else 0)
    top = max(ceiling + int((floor - ceiling - block_h) * 0.34), ceiling)

    for i, line in enumerate(lines):
        draw_squeezed(canvas, (MARGIN, top + i * line_h), line, face, INK, HEADLINE_SQUEEZE)
    cursor = top + len(lines) * line_h + 30

    if box:
        cursor = accent_box(draw, (MARGIN, cursor), box) + 40

    footer(draw, 1 if total and total > 1 else None, total)
    return canvas


def body_page(lead: str, rest: str, page: int, total: int) -> Image.Image:
    canvas = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(canvas)
    y = identity_chip(canvas, draw)

    top = y + 110
    face, lines, line_h = fit_headline(lead.upper(), W - MARGIN * 2,
                                       H - top - 480, start=88)
    for i, line in enumerate(lines):
        draw_squeezed(canvas, (MARGIN, top + i * line_h), line, face, INK, HEADLINE_SQUEEZE)
    cursor = top + len(lines) * line_h + 46

    if rest:
        body_face = font(FONT_REGULAR, 40)
        for line in wrap(rest, body_face, W - MARGIN * 2):
            if cursor > H - 220:
                break
            draw.text((MARGIN, cursor), line, font=body_face, fill=INK)
            cursor += 56

    footer(draw, page, total)
    return canvas


def sentences(paragraph: str) -> tuple[str, str]:
    text = paragraph.strip()
    split = re.match(r"(.+?[.!?])\s+(.*)", text, re.S)
    if not split:
        return text, ""
    return split.group(1), split.group(2).strip()


def parse(path: Path) -> tuple[dict, list[str]]:
    raw = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    if raw.startswith("---"):
        _, front, body = raw.split("---", 2)
        for line in front.strip().splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip()
    else:
        body = raw
    match = re.search(r"<!-- gate:body:start -->(.*?)<!-- gate:body:end -->", body, re.S)
    if match:
        body = match.group(1)
    paragraphs = [p.strip().replace("\n", " ") for p in re.split(r"\n\s*\n", body)]
    paragraphs = [p for p in paragraphs if p and not p.startswith("#")]
    return meta, paragraphs


def build(post: Path, pages: int | None) -> dict:
    meta, paragraphs = parse(post)
    headline = meta.get("headline", post.parent.name).strip()
    box = meta.get("box", "").strip() or None
    out = post.parent / "visual"
    out.mkdir(exist_ok=True)
    # A shorter render must not leave last week's pages behind: the PDF would be
    # right and the folder would show more cards than the post has sections.
    for stale in out.glob("page*.png"):
        stale.unlink()

    # Body pages skip the opening pair (that is the cover) and the tag line.
    body = [p for p in paragraphs[2:] if not p.strip().startswith("#")]
    if pages:
        body = body[: pages - 1]
    total = len(body) + 1

    first = make_cover(headline, box, total if body else None)
    first.save(out / "cover.png")

    rendered = [first]
    for i, paragraph in enumerate(body, start=2):
        lead, rest = sentences(paragraph)
        page = body_page(lead, rest, i, total)
        page.save(out / f"page{i}.png")
        rendered.append(page)

    first.save(out / "cover.jpg", quality=92)
    if len(rendered) > 1:
        rendered[0].save(out / "carousel.pdf", save_all=True,
                         append_images=rendered[1:], resolution=144.0)
    return {"out": out, "cover": out / "cover.png",
            "pdf": out / "carousel.pdf" if len(rendered) > 1 else None,
            "pages": len(rendered)}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Render a post's card and carousel.")
    ap.add_argument("post", help="path to post.md")
    ap.add_argument("--pages", type=int, default=None,
                    help="maximum carousel pages, cover included")
    args = ap.parse_args(argv)
    result = build(Path(args.post), args.pages)
    print(f"cover  {result['cover']}")
    if result["pdf"]:
        print(f"pdf    {result['pdf']}  ({result['pages']} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
