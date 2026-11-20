#!/usr/bin/env python3
"""Draw the repository banner and the social preview card.

Both are plain SVG, written here so the artwork is reproducible and editable
rather than a binary nobody can change. The dot grid is the coverage argument
drawn as an image: most squares dim, a minority lit, because most classes are
open at the start of an engagement.

    python3 assets/make-banner.py
"""

from __future__ import annotations

import random
from pathlib import Path

INK = "#0b0b0c"
PAPER = "#f4f1ec"
ACCENT = "#d9541f"
MUTED = "#8a8580"
DIM = "#242427"

FONT = "DejaVu Sans, Helvetica, Arial, sans-serif"


def dot_grid(x0: int, y0: int, cols: int, rows: int, size: int, gap: int, seed: int = 7) -> str:
    rng = random.Random(seed)
    parts = []
    for row in range(rows):
        for col in range(cols):
            x = x0 + col * (size + gap)
            y = y0 + row * (size + gap)
            lit = rng.random() < 0.14
            fill = ACCENT if lit else DIM
            opacity = "1" if lit else "0.55"
            parts.append(
                f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="1.5" fill="{fill}" opacity="{opacity}"/>'
            )
    return "\n    ".join(parts)


def card(width: int, height: int, title_size: int, sub_size: int, grid_cols: int, grid_rows: int,
         grid_x: int, grid_y: int, small: bool, cell: int = 12, gap: int = 7) -> str:
    rule_y = int(height * 0.60)
    foot_y = height - (46 if small else 58)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="AI Red Team Playbook">
  <rect width="{width}" height="{height}" fill="{INK}"/>
  <rect x="0" y="0" width="{width}" height="6" fill="{ACCENT}"/>

  <text x="80" y="{int(height * 0.30)}" font-family="{FONT}" font-size="{title_size}" font-weight="bold" fill="{PAPER}" letter-spacing="-3">AI Red Team</text>
  <text x="80" y="{int(height * 0.30) + int(title_size * 1.02)}" font-family="{FONT}" font-size="{title_size}" font-weight="bold" fill="{ACCENT}" letter-spacing="-3">Playbook</text>

  <rect x="82" y="{rule_y}" width="120" height="4" fill="{ACCENT}"/>

  <text x="82" y="{rule_y + int(sub_size * 1.9)}" font-family="{FONT}" font-size="{sub_size}" fill="{MUTED}">168 testable classes. Six categories.</text>
  <text x="82" y="{rule_y + int(sub_size * 2.9)}" font-family="{FONT}" font-size="{sub_size}" fill="{MUTED}">A coverage argument, with intervals.</text>

  <text x="82" y="{foot_y}" font-family="{FONT}" font-size="{18 if small else 20}" fill="#55524e" letter-spacing="3">OWASP LLM TOP 10 / MITRE ATLAS / NIST AI RMF</text>

  <g>
    {dot_grid(grid_x, grid_y, grid_cols, grid_rows, cell, gap)}
  </g>
</svg>
"""


def render_png(svg_path: Path, png_path: Path, width: int, height: int, title_size: int,
               sub_size: int, cols: int, rows: int, gx: int, gy: int, small: bool,
               cell: int = 12, gap: int = 7) -> bool:
    """Optional PNG render, for the GitHub social preview which cannot take an SVG.

    Needs Pillow and the DejaVu fonts. If either is missing the script says so and
    carries on, because the SVG is the artwork and the PNG is a convenience.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print(f"skipped {png_path.name}: Pillow not installed")
        return False

    fonts = {
        "bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "regular": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    }
    if not Path(fonts["bold"]).exists():
        print(f"skipped {png_path.name}: DejaVu fonts not found")
        return False

    img = Image.new("RGB", (width, height), INK)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, 6], fill=ACCENT)

    title_font = ImageFont.truetype(fonts["bold"], title_size)
    sub_font = ImageFont.truetype(fonts["regular"], sub_size)
    tag_font = ImageFont.truetype(fonts["regular"], 18 if small else 20)

    draw.text((80, int(height * 0.30) - int(title_size * 0.78)), "AI Red Team", font=title_font, fill=PAPER)
    draw.text((80, int(height * 0.30) + int(title_size * 0.24)), "Playbook", font=title_font, fill=ACCENT)

    rule_y = int(height * 0.60)
    draw.rectangle([82, rule_y, 202, rule_y + 4], fill=ACCENT)

    draw.text((82, rule_y + int(sub_size * 1.6)), "168 testable classes. Six categories.", font=sub_font, fill=MUTED)
    draw.text((82, rule_y + int(sub_size * 2.6)), "A coverage argument, with intervals.", font=sub_font, fill=MUTED)

    draw.text((82, height - (54 if small else 66)), "OWASP LLM TOP 10 / MITRE ATLAS / NIST AI RMF",
              font=tag_font, fill="#55524e")

    rng = random.Random(7)
    size = cell
    for row in range(rows):
        for col in range(cols):
            x = gx + col * (size + gap)
            y = gy + row * (size + gap)
            lit = rng.random() < 0.14
            colour = ACCENT if lit else "#2b2b2f"
            draw.rectangle([x, y, x + size, y + size], fill=colour)

    img.save(png_path)
    print(f"wrote {png_path.name} ({width}x{height})")
    return True


def main() -> int:
    out = Path(__file__).resolve().parent

    banner = card(1280, 420, 84, 26, grid_cols=16, grid_rows=13, grid_x=880, grid_y=104, small=True)
    (out / "banner.svg").write_text(banner, encoding="utf-8")

    social = card(1280, 640, 100, 32, grid_cols=18, grid_rows=15, grid_x=820, grid_y=150, small=False)
    (out / "social-preview.svg").write_text(social, encoding="utf-8")

    render_png(out / "banner.svg", out / "banner.png", 1280, 420, 84, 26, 16, 13, 880, 104, True)
    render_png(out / "social-preview.svg", out / "social-preview.png", 1280, 640, 100, 32, 18, 15, 820, 150, False)

    print("wrote assets/banner.svg and assets/social-preview.svg")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
