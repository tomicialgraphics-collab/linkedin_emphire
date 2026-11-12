#!/usr/bin/env python3
"""Render a cleared case study from its markdown source to a print PDF.

The markdown in CLIENTS/ is the source of truth. This script only sets type; it
never rewrites a sentence, so the PDF cannot drift from the version the client
cleared. Front matter is parsed for the title, the client and the version line,
and the body is rendered heading by heading.

    python3 TOOLING/case_study_pdf.py CLIENTS/foray-dunin7/CASE-STUDY-1_open-protocol-anchoring.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
)

INK = colors.HexColor("#111111")
MUTED = colors.HexColor("#5c5c5c")
RULE = colors.HexColor("#b9b9b9")
ACCENT = colors.HexColor("#1f3a5f")

# The client named on the cover. Kept here rather than in the front matter so the
# cleared markdown keeps the exact bytes and hash the client reviewed.
CLIENT_DISPLAY = {"FORAY (Dunin7)": "Marvin Percival, DUNIN7"}

PAGE_W, PAGE_H = A4
MARGIN_L = 24 * mm
MARGIN_R = 24 * mm
MARGIN_T = 26 * mm
MARGIN_B = 24 * mm


def parse(path: Path) -> tuple[dict, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    if text.startswith("---"):
        _, front, body = text.split("---", 2)
        for line in front.strip().splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip()
    else:
        body = text

    blocks: list[tuple[str, str]] = []
    buffer: list[str] = []
    for raw in body.splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            if buffer:
                blocks.append(("p", " ".join(buffer)))
                buffer = []
            blocks.append(("h1", line[2:].strip()))
        elif line.startswith("## "):
            if buffer:
                blocks.append(("p", " ".join(buffer)))
                buffer = []
            blocks.append(("h2", line[3:].strip()))
        elif not line.strip():
            if buffer:
                blocks.append(("p", " ".join(buffer)))
                buffer = []
        else:
            buffer.append(line.strip())
    if buffer:
        blocks.append(("p", " ".join(buffer)))
    return meta, blocks


def escape(text: str) -> str:
    """Strip inline markdown, then escape for reportlab's mini-markup.

    Backticks are dropped rather than set in a monospace face: an inline hash
    fragment reads worse in Courier than in the body face, and every other run
    in the page is Times.
    """
    text = text.replace("`", "").replace("**", "")
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def styles() -> dict[str, ParagraphStyle]:
    return {
        "title": ParagraphStyle(
            "title", fontName="Times-Bold", fontSize=17.5, leading=23,
            textColor=INK, spaceAfter=10,
        ),
        "standfirst": ParagraphStyle(
            "standfirst", fontName="Times-Italic", fontSize=11.5, leading=17,
            textColor=MUTED, spaceAfter=14,
        ),
        "h2": ParagraphStyle(
            "h2", fontName="Helvetica-Bold", fontSize=9.5, leading=13,
            textColor=ACCENT, spaceBefore=15, spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "body", fontName="Times-Roman", fontSize=11, leading=16.2,
            textColor=INK, alignment=TA_JUSTIFY, spaceAfter=8.5,
            firstLineIndent=0,
        ),
        "meta": ParagraphStyle(
            "meta", fontName="Helvetica", fontSize=8, leading=11,
            textColor=MUTED, alignment=TA_LEFT,
        ),
    }


class Doc(BaseDocTemplate):
    def __init__(self, target: str, title: str, footer_left: str, **kw):
        super().__init__(target, pagesize=A4, title=title, author="Olusanya Timothy",
                         subject="Case study 1, Foray (Dunin7)", **kw)
        self.footer_left = footer_left
        frame = Frame(
            MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R,
            PAGE_H - MARGIN_T - MARGIN_B, id="body",
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=self.decorate)])

    def decorate(self, canv: pdfcanvas.Canvas, doc) -> None:
        canv.saveState()
        canv.setFont("Helvetica", 7.2)
        canv.setFillColor(MUTED)
        baseline = MARGIN_B - 10 * mm
        canv.drawString(MARGIN_L, baseline, self.footer_left)
        canv.drawRightString(PAGE_W - MARGIN_R, baseline, f"{doc.page}")
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.4)
        canv.line(MARGIN_L, baseline + 5 * mm, PAGE_W - MARGIN_R, baseline + 5 * mm)
        canv.restoreState()


def build(src: Path, out: Path) -> Path:
    meta, blocks = parse(src)
    title = next((t for kind, t in blocks if kind == "h1"), src.stem)
    st = styles()
    flow = [Paragraph(escape(title), st["title"])]

    client = meta.get("client", "")
    prepared = f"Prepared for {CLIENT_DISPLAY.get(client, client)}" if client else ""
    version = ""
    for kind, text in blocks:
        if kind == "p" and text.startswith("Version "):
            match = re.match(r"(Version \d+)", text)
            version = match.group(1) if match else ""
            break
    meta_line = "  ·  ".join(x for x in (prepared, version) if x)
    if meta_line:
        flow.append(Paragraph(escape(meta_line), st["meta"]))
    flow.append(Spacer(1, 5 * mm))

    seen_title = False
    for kind, text in blocks:
        if kind == "h1":
            seen_title = True
            continue
        if not seen_title:
            continue
        if kind == "h2":
            flow.append(KeepTogether([Paragraph(escape(text).upper(), st["h2"])]))
        else:
            flow.append(Paragraph(escape(text), st["body"]))

    footer_left = f"Case study 1  ·  {CLIENT_DISPLAY.get(client, client)}  ·  {version}"
    Doc(str(out), title, footer_left).build(flow)
    return out


if __name__ == "__main__":
    source = Path(sys.argv[1] if len(sys.argv) > 1
                  else "CLIENTS/foray-dunin7/CASE-STUDY-1_open-protocol-anchoring.md")
    target = source.with_suffix(".pdf")
    print(build(source, target))
