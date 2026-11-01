#!/usr/bin/env python3
"""Render the Arcezia report and one-pager to PDF.

Markdown in, clean A4 out. Handles the subset these two documents use: headings,
paragraphs, bullets, horizontal rules, pipe tables, bold and inline code. Nothing else,
because nothing else is in them.

    python render_report_pdf.py

Needs reportlab. The venv used to build these lives outside the repo.
"""

import os
import re
import xml.sax.saxutils as sax

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, HRFlowable)

HERE = os.path.dirname(os.path.abspath(__file__))

INK = colors.HexColor("#111827")
NAVY = colors.HexColor("#0F2A43")
MUTED = colors.HexColor("#4B5563")
LINE = colors.HexColor("#D1D5DB")
PANEL = colors.HexColor("#F8FAFC")

S = {
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=20, leading=25,
                         textColor=INK, spaceBefore=6, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=13, leading=17,
                         textColor=NAVY, spaceBefore=16, spaceAfter=4),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11, leading=15,
                         textColor=INK, spaceBefore=12, spaceAfter=3),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.8, leading=14.4,
                           textColor=INK, spaceAfter=7),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.8, leading=14.4,
                             textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=3),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9, leading=12.5,
                           textColor=INK),
    "cell_head": ParagraphStyle("cell_head", fontName="Helvetica-Bold", fontSize=9,
                                leading=12.5, textColor=colors.white),
}


def inline(text):
    """Escape for reportlab, then re-apply the two inline marks these docs use."""
    text = sax.escape(text, entities={})
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r'<font face="Courier">\1</font>', text)
    return text.replace("`", "")


def parse_table(lines):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") and c for c in cells):
            continue
        rows.append(cells)
    if not rows:
        return None
    # A table whose header row is blank is a key-value block, not a grid with a header.
    has_head = any(c for c in rows[0])
    body = rows[1:] if has_head else rows
    data = []
    if has_head:
        data.append([Paragraph(inline(c), S["cell_head"]) for c in rows[0]])
    for row in body:
        data.append([Paragraph(inline(c), S["cell"]) for c in row])
    table = Table(data, hAlign="LEFT", repeatRows=1 if has_head else 0)
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if has_head:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PANEL]),
        ]
    else:
        style += [("ROWBACKGROUNDS", (0, 0), (-1, -1), [PANEL, colors.white])]
    table.setStyle(TableStyle(style))
    return table


def build(md_path, pdf_path, title):
    with open(md_path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    story = []
    para, bullets, table = [], [], []
    quote_block = False

    def flush_para():
        nonlocal para
        if para:
            story.append(Paragraph(inline(" ".join(para)), S["body"]))
            para = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            for item in bullets:
                story.append(Paragraph(inline(item), S["bullet"], bulletText="\u2022"))
            story.append(Spacer(1, 4))
            bullets = []

    def flush_table():
        nonlocal table
        if table:
            built = parse_table(table)
            if built is not None:
                story.append(Spacer(1, 4))
                story.append(built)
                story.append(Spacer(1, 8))
            table = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("|"):
            flush_para()
            flush_bullets()
            table.append(line)
            continue
        flush_table()

        if not line.strip():
            flush_para()
            flush_bullets()
            continue
        if line.startswith("### "):
            flush_para()
            flush_bullets()
            story.append(Paragraph(inline(line[4:]), S["h3"]))
        elif line.startswith("## "):
            flush_para()
            flush_bullets()
            story.append(Paragraph(inline(line[3:]), S["h2"]))
        elif line.startswith("# "):
            flush_para()
            flush_bullets()
            story.append(Paragraph(inline(line[2:]), S["h1"]))
        elif line.strip() == "---":
            flush_para()
            flush_bullets()
            story.append(HRFlowable(width="100%", thickness=0.6, color=LINE,
                                    spaceBefore=8, spaceAfter=10))
        elif line.startswith("- "):
            flush_para()
            bullets.append(line[2:])
        else:
            flush_bullets()
            para.append(line.strip())
    flush_para()
    flush_bullets()
    flush_table()

    doc = BaseDocTemplate(pdf_path, pagesize=A4,
                          leftMargin=19 * mm, rightMargin=19 * mm,
                          topMargin=17 * mm, bottomMargin=18 * mm,
                          title=title, author="Olusanya Timothy",
                          subject="Arcezia action gate, default-state findings")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")

    def footer(canvas, doc_):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, 10 * mm, "Arcezia, private. Not for publication.")
        canvas.drawRightString(A4[0] - doc.rightMargin, 10 * mm, "%d" % canvas.getPageNumber())
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="page", frames=[frame], onPage=footer)])
    doc.build(story)
    return pdf_path


if __name__ == "__main__":
    jobs = [
        ("REPORT_2026-11-01_arcezia-default-state.md",
         "Arcezia-Action-Gate_Findings_2026-11-01.pdf",
         "Arcezia Action Gate: default-state findings"),
        ("ONE-PAGER_default-state_2026-11-01.md",
         "Arcezia_default-state_one-pager_2026-11-01.pdf",
         "What the Arcezia gate does in the default state"),
        ("WRITE-UP-DRAFT_public_2026-11-01.md",
         "Arcezia_write-up_DRAFT_not-for-publication.pdf",
         "Draft: what a fail-closed action gate cannot see"),
    ]
    for src, out, title in jobs:
        path = build(os.path.join(HERE, src), os.path.join(HERE, out), title)
        print("wrote %s (%d bytes)" % (os.path.basename(path), os.path.getsize(path)))
