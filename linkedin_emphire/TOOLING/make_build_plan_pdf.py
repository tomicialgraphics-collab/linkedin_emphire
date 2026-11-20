#!/usr/bin/env python3
"""Render the scoped build plan for the Eri practice build as a PDF.

House system: white ground, an identity chip, heavy black type, one yellow accent,
nothing else. A4, because this one gets read on a desk and printed, not scrolled.

    python3 TOOLING/make_build_plan_pdf.py
    python3 TOOLING/make_build_plan_pdf.py --out CLIENTS/eri/exports/plan.pdf
"""

from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT.parent / "manual" / "build" / "fonts"
AVATAR = ROOT / "VISUAL" / "assets" / "avatar.jpg"

INK = HexColor("#111111")
GREY = HexColor("#6E6E6E")
LIGHT = HexColor("#E8E8E8")
PALE = HexColor("#F4F4F2")
YELLOW = HexColor("#F5C64B")

NAME = "Olusanya Timothy"
ROLE = "AI systems testing and verification"
CONTACT = "linkedin.com/in/olusanya-timothy"
DOC_TITLE = "Eri practice build: scoped plan"

W, H = A4
MARGIN = 54
COL = W - 2 * MARGIN

pdfmetrics.registerFont(TTFont("House", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("House-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFontFamily("House", normal="House", bold="House-Bold")


def style(name, size, leading, colour=INK, font="House", before=0, after=0, **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading,
                          textColor=colour, spaceBefore=before, spaceAfter=after,
                          alignment=TA_LEFT, **kw)


S_H1 = style("h1", 20, 24, font="House-Bold", before=2, after=4)
S_H2 = style("h2", 11, 14, font="House-Bold", before=16, after=5)
S_LEAD = style("lead", 11, 16.5, INK, after=6)
S_BODY = style("body", 9.2, 13.8, INK, after=5)
S_SMALL = style("small", 7.8, 11.2, GREY, after=3)
S_CELL = style("cell", 8.2, 11.4, INK)
S_CELLB = style("cellb", 8.2, 11.4, INK, font="House-Bold")
S_HEAD = style("thead", 7.4, 10, GREY, font="House-Bold", after=0)


def para(text, s=S_BODY):
    return Paragraph(text, s)


def rule(width=COL, thickness=0.7, colour=LIGHT, before=2, after=8):
    t = Table([[""]], colWidths=[width], rowHeights=[0.1])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), thickness, colour),
                           ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    t.spaceBefore = before
    t.spaceAfter = after
    return t


def accent(text, size=9.2):
    """A sentence the reader must not miss: yellow edge, pale ground."""
    t = Table([[Paragraph(text, style("accent", size, size * 1.5, INK))]],
              colWidths=[COL])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("LINEBEFORE", (0, 0), (0, -1), 3, YELLOW),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    t.spaceBefore = 6
    t.spaceAfter = 8
    return t


def table(rows, widths, header=True, align_right=()):
    data = [[Paragraph(str(c), S_HEAD if (header and r == 0) else
                       (S_CELLB if c and str(c).startswith("**") else S_CELL))
             for c in row] for r, row in enumerate(rows)]
    # strip the bold marker
    data = [[Paragraph(str(c).replace("**", ""), S_HEAD if (header and r == 0)
                       else (S_CELLB if str(c).startswith("**") else S_CELL))
             for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        cmds += [("LINEBELOW", (0, 0), (-1, 0), 0.9, INK),
                 ("TOPPADDING", (0, 0), (-1, 0), 0)]
    cmds += [("LINEBELOW", (0, 1), (-1, -1), 0.4, LIGHT)]
    t.setStyle(TableStyle(cmds))
    return t


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("House", 7.2)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, 30, f"{NAME} · {ROLE}")
    canvas.drawRightString(W - MARGIN, 30, f"{DOC_TITLE} · {doc.page - 1}")
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 42, W - MARGIN, 42)
    canvas.restoreState()


def draw_cover(canvas, doc):
    canvas.saveState()
    # top rule and chip
    canvas.setFillColor(YELLOW)
    canvas.rect(0, H - 10, W, 10, stroke=0, fill=1)

    canvas.setFillColor(GREY)
    canvas.setFont("House-Bold", 8)
    canvas.drawString(MARGIN, H - 46, "ERI  ·  PRACTICE BUILD  ·  PROPOSED SCOPE")
    canvas.setFillColor(INK)
    canvas.setFont("House", 8)
    canvas.drawRightString(W - MARGIN, H - 46, "20 NOVEMBER 2026")

    # title
    canvas.setFillColor(INK)
    y = H - 132
    canvas.setFont("House-Bold", 40)
    for line in ["Four cycles,", "forty-five", "requirements."]:
        canvas.drawString(MARGIN, y, line)
        y -= 46

    # yellow block
    canvas.setFillColor(YELLOW)
    canvas.rect(MARGIN, y - 6, 190, 12, stroke=0, fill=1)

    # standfirst
    canvas.setFillColor(INK)
    canvas.setFont("House", 11.5)
    y -= 42
    for line in ["A scoped plan for the practice build agreed on 20 November:",]:
        canvas.drawString(MARGIN, y, line)
    canvas.setFillColor(GREY)
    y -= 17
    for line in [
        "what gets built, in what order, what counts as done,",
        "and the one test that decides whether any of it means anything.",
    ]:
        canvas.drawString(MARGIN, y, line)
        y -= 15

    # contents
    canvas.setFillColor(GREY)
    canvas.setFont("House-Bold", 7.6)
    canvas.drawString(MARGIN, H - 452, "INSIDE")
    items = [
        ("What this is, and the test that comes first", "1"),
        ("Scope: what is in and what stays out", "2"),
        ("The order: four cycles and what each ends with", "3"),
        ("The changes I am proposing, and what they cost", "4"),
        ("What could stop us, how we work, sign-off", "5"),
    ]
    y = H - 470
    for label, page_no in items:
        canvas.setStrokeColor(LIGHT)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN, y - 6, W - MARGIN, y - 6)
        canvas.setFillColor(INK)
        canvas.setFont("House", 9.4)
        canvas.drawString(MARGIN, y, label)
        canvas.setFillColor(GREY)
        canvas.setFont("House-Bold", 9.4)
        canvas.drawRightString(W - MARGIN, y, page_no)
        y -= 24

    # meta block
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 168, W - MARGIN, 168)

    canvas.setFillColor(INK)
    canvas.setFont("House-Bold", 9)
    canvas.drawString(MARGIN, 148, NAME)
    canvas.setFont("House", 8.2)
    canvas.setFillColor(GREY)
    canvas.drawString(MARGIN, 135, ROLE)
    canvas.drawString(MARGIN, 122, CONTACT)

    canvas.setFillColor(INK)
    canvas.setFont("House-Bold", 8.2)
    canvas.drawRightString(W - MARGIN, 148, "7.45 build days, about 60 hours")
    canvas.setFillColor(GREY)
    canvas.setFont("House", 8.2)
    canvas.drawRightString(W - MARGIN, 135, "Proposed, not agreed: v0.4 draft for review")
    canvas.drawRightString(W - MARGIN, 122, "Supersedes the four-week schedule in v0.3")

    # avatar, circular
    if AVATAR.exists():
        size = 58
        x, y0 = W - MARGIN - size, 190
        canvas.saveState()
        p = canvas.beginPath()
        p.circle(W - MARGIN - size / 2, y0 + size / 2, size / 2)
        canvas.clipPath(p, stroke=0, fill=0)
        canvas.drawImage(str(AVATAR), x, y0, size, size, mask="auto")
        canvas.restoreState()
    canvas.restoreState()


def build(out: Path) -> Path:
    doc = BaseDocTemplate(str(out), pagesize=A4,
                          leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=MARGIN, bottomMargin=54,
                          title="Eri practice build: scoped plan",
                          author=NAME, subject="Proposed scope for the Eri practice build")
    cover = PageTemplate(id="cover", frames=[Frame(MARGIN, 54, COL, H - 108, id="c")],
                         onPage=draw_cover)
    body = PageTemplate(id="body", frames=[Frame(MARGIN, 54, COL, H - 108, id="b")],
                        onPage=draw_footer)
    doc.addPageTemplates([cover, body])

    story = [NextPageTemplate("body"), PageBreak()]

    # ---------------- page 1
    story += [
        para("What this is", S_H1),
        rule(),
        para("This is the scope for the practice build, written before the first line of code so "
             "that we are arguing about a document rather than a memory. It takes your v0.3 "
             "requirements as the base, adds the seven amendments I proposed, and puts every "
             "change next to its cost in build days.", S_LEAD),
        para("The arithmetic is yours and it holds. Four cycles of 1.6, 1.5, 1.3 and 2.1 days make "
             "6.5 days, about 52 hours. The amendments add 0.95, so the build is 7.45 days, about "
             "60 hours. Ten requirements in cycle one, forty-five plus six new ones in total.", S_BODY),
        para("It does not cover the register itself, the pitch, or any pricing. Those are your "
             "documents and this one does not contradict them.", S_SMALL),
        para("The one thing that has to work", S_H2),
        para("Everything in this plan exists to make one minute possible: a stranger with a file, no "
             "account and no app, is told whether it matches something sealed, and can open the "
             "anchor herself.", S_BODY),
        accent("REQ-035 with 034 and 036 under it. If that minute fails, the certificate is a "
               "private diary with a QR code on it. Every other requirement is scaffolding for it."),
        para("Which is why the first ninety minutes of cycle one are not spent building anything.", S_BODY),
        para("The first test", S_H2),
        para("Monday morning, before REQ-001: send a batch of three fingerprints to FORAY, read back "
             "a transaction id and a block time, and open that transaction on a public explorer. "
             "Nothing else, until we know.", S_BODY),
    ]
    story.append(table([
        ["Result", "What it means", "What changes"],
        ["Id and block time, and the explorer shows the same id",
         "The design holds", "Cycles three and four go ahead as scoped"],
        ["Id and block time, but the explorer link does not resolve",
         "Half the minute works", "REQ-036 and REQ-031 are re-planned in week one, not week three"],
        ["No id, or no block time",
         "The anchoring as written is not available",
         "Cycles three and four are re-scoped before any capture code is written"],
    ], [150, 120, 213], align_right=()))
    story.append(para("Two answers are needed on the same morning, because they decide whether cycle "
                      "one is real: whether the NIPOST key is live or a test key, and whether Stele "
                      "can be mounted this week.", S_SMALL))
    story += [para("Three things already settled", S_H2)]
    story.append(table([
        ["", "What happens, whatever else changes"],
        ["Where the data comes from", "Every demo person, household and document is invented. Two phones, with camera, microphone and location, and nothing belonging to anyone real"],
        ["What happens to it", "Demo content is deleted thirty days after the review. The fingerprints and anchor references remain, so a copy can still be shown to have existed on a date"],
        ["How anyone signs in", "Passkeys only. No password, no email, no username field, and no NIN stored anywhere in the product"],
    ], [110, 373]))


    # ---------------- page 2
    story += [PageBreak(), para("Scope", S_H1), rule()]
    story += [para("In", S_H2)]
    story.append(table([
        ["Area", "What is in"],
        ["Foundation", "One staging URL, Postgres, English and Yoruba from translation files, "
                       "product name, logo and colour from a brand file"],
        ["Identity", "Stele passkey sign-in for verifiers, no email or username field, no passwords"],
        ["Postcode", "Eleven-character format check, server-side NIPOST Lookup with the key held on "
                     "the server, address shown, refused and unreachable both handled"],
        ["Capture", "Voice up to ten minutes, photos with date and accuracy, document images, "
                    "SHA-256 computed on the phone and recomputed on the server, append-only"],
        ["Attestation", "Four kinds, relationship shown, a speaker cannot attest their own item, "
                        "counter-attestation and withdrawal as new events"],
        ["Anchoring", "One batch per seal, transaction id and block time stored, failure visible, "
                      "never a second version of a sealed batch"],
        ["Public side", "Certificate to one A4 page, QR to a check page with no sign-in, file chosen "
                        "on the checker's own device and never uploaded, anchor opens on an explorer"],
        ["Operability", "Seed and reset with one command, demo data deleted 30 days after the "
                        "review, iPhone Safari run on every Android criterion"],
    ], [62, 421]))

    story += [para("Out", S_H2)]
    story.append(table([
        ["Not in scope", "Why it stays out"],
        ["Any statement that a title is good, a property is safe, or who owns it", "The product cannot say this and must be built so it cannot appear to"],
        ["Land parcels, survey outlines or coordinates as the file's key", "Postcode is a label on a building; the parcel key is the register, not this slice"],
        ["Payments, prices, plans, subscriptions", "Nothing in this build collects money"],
        ["NIN numbers and email addresses", "A verifier checks NIN in person; the number is never stored"],
        ["The NIPOST map widget, autocomplete", "The widget asks for NIN or email, so it is not used at all"],
        ["Real users, real households, real documents", "Every demo person and household is invented"],
        ["Offline capture, account recovery beyond Stele, transcription, other languages, app-store builds", "Each is a project of its own; the prototype runs as an installable mobile web app"],
    ], [190, 293]))


    story.append(Spacer(1, 10))
    story.append(para("If something you expected to see in the In table is missing, say so now. A "
                      "requirement added in cycle one is cheap. The same requirement noticed in cycle "
                      "four arrives at the demo as a hole.", S_SMALL))

    # ---------------- page 3
    story += [PageBreak(), para("The order", S_H1), rule(),
              para("Four cycles, each one ending when its criteria pass rather than when a week ends. "
                   "The days are your estimates plus mine, and they are there to be argued with.", S_LEAD)]
    story.append(table([
        ["Cycle", "What it covers", "Reqs", "Days", "What exists at the end"],
        ["**1. Foundation and postcode",
         "Skeleton, Stele, brand and translation files, format check, server lookup, refused and unreachable, file created; the agency statement recorded",
         "001–010 + 050", "1.70",
         "A phone in Chrome creates a file against a real postcode, and grep finds the API key nowhere in the page or the response"],
        ["**2. Capture",
         "Voice, photos, documents, on-device fingerprints, server recompute, append-only list, no edit or delete; consent in her words; consent to be named",
         "011–020 + 046, 047", "1.85",
         "A ten-minute recording opens with the speaker naming what she allows, four items carry fingerprints, and a direct edit returns 403"],
        ["**3. Attestation and anchoring",
         "Four kinds of attestation, speaker cannot attest his own item, counter-attestation, withdrawal, seal as one batch, anchor reference stored, seal failure visible",
         "021–030 + 048, 049", "1.65",
         "Four attested items are sealed in one batch with a transaction id and block time, and a forced FORAY failure leaves nothing marked sealed"],
        ["**4. Certificate and public check",
         "One-page certificate, QR, check page with no session, match and no-match, explorer links, names and roles, seed, reset, negative control, iPhone run",
         "031–045 + 051", "2.25",
         "A phone with no session scans the QR, matches the original file, and says no match to a copy altered by one byte"],
    ], [94, 148, 58, 30, 153]))
    story.append(Spacer(1, 6))
    story.append(accent("Total 7.45 build days, about 60 hours, across four cycles. The four-week "
                        "calendar is gone by agreement: with no deadline, a cycle ends when it passes, "
                        "and a cycle that takes longer is the build telling us something."))
    story += [Spacer(1, 6)]
    story += [para("What the plan assumes", S_H2)]
    story.append(table([
        ["Assumption", "If it is wrong"],
        ["The FORAY anchoring service returns a transaction id and a block time for a batch of fingerprints",
         "Cycles three and four are re-scoped, and the demo proves less than the design claims"],
        ["NIPOST grants working Lookup access, live or by fixture with the real response shape",
         "Cycle one stops at REQ-006 and the postcode becomes a label the verifier types"],
        ["Stele can be mounted into the server for passkey sign-in",
         "Cycle one stops at REQ-004 and a development-only session is agreed in writing instead"],
        ["One Android phone in Chrome and one iPhone in Safari, each with camera, microphone and location",
         "REQ-044 cannot be met, so every criterion is only half checked"],
            ], [232, 251]))


    # ---------------- page 4
    story += [PageBreak(), para("What I am proposing to change", S_H1), rule(),
              para("Seven gaps and one addition, each written as a new requirement number so your "
                   "v0.3 numbering survives. Full wording is in the amendments document; this is the "
                   "short version and its cost.", S_LEAD)]
    story.append(table([
        ["", "Change", "Why, in one line", "Cycle", "Days"],
        ["050", "The agency records a statement in its own name at registration, shown on the certificate",
         "A name with no statement attached tells a lawyer who touched the file, not who stands behind it", "1", "0.10"],
        ["046", "Consent is spoken, in her language, naming what she is allowing",
         "A tick box records what the person holding the phone says, not what she agreed to", "2", "0.10"],
        ["047", "Consent to be named, per person, dated, revocable, separate from consent to record",
         "REQ-038 needs this consent and nothing in v0.3 captures it", "2", "0.20"],
        ["014", "One caption under every photo: the phone's position, accurate to about N metres, not a boundary",
         "A phone is five to ten metres out, and in a Lagos layout that is the neighbouring plot", "2", "0.05"],
        ["048", "An attestor can withdraw; the withdrawal is an event, never an edit",
         "A record that can hide a withdrawal is worse than no record", "3", "0.20"],
        ["049", "Sealing fails visibly and can be retried; nothing is marked sealed without an anchor reference",
         "NIPOST has refused and unreachable; FORAY had neither", "3", "0.15"],
        ["028 / 043", "One sentence in both places: deletion removes the content and the page, the fingerprints and their anchor remain",
         "The two requirements currently contradict each other", "3, 4", "0.00"],
        ["051", "One seeded item whose stored fingerprint does not match its content, checked on every release",
         "Without it the public check is a test that has never failed", "4", "0.05"],
    ], [42, 168, 196, 38, 39]))
    story.append(Spacer(1, 4))
    story.append(para("0.95 days in total. Nothing here blocks Monday: cycle one takes only REQ-050, "
                      "which is a tenth of a day on top of REQ-010.", S_SMALL))
    story += [para("Where the full wording is", S_H2)]
    story.append(table([
        ["The document", "ERI-REQ-v0.4-amendments.md, which carries six new requirements at 046 to 051, one sentence each for the five that change, and the acceptance test for every one"],
        ["If you reject one", "We build v0.3 as written, the criterion stays exactly as v0.3 wrote it, and the disagreement is recorded in the changelog next to the version number"],
        ["The two that cannot wait", "REQ-046 and REQ-047, because both change the recording screen and it is cheaper to build that screen once. Everything else can be argued with while cycles one and two run"],
    ], [110, 373]))

    # ---------------- page 5
    story += [PageBreak(), para("What could stop us", S_H1), rule(),
              para("Two of these are assumptions inside your own document. I would rather name them now "
                   "than discover them on a Wednesday.", S_LEAD)]
    story.append(table([
        ["Risk", "What it costs if it happens", "What I do"],
        ["The NIPOST key is a test key and resolves no live postcodes",
         "Cycle one stops at REQ-006",
         "Point REQ-006 at a recorded fixture with the real response shape, label it as a fixture in the code and the daily note, and keep the criterion for the day the live key arrives. No fake passes."],
        ["Stele cannot be mounted into the server this week",
         "Cycle one stops at REQ-004",
         "Agree a development-only session in writing, dated, and swap it for Stele the day it mounts. No invented sign-in shipped as if it were the real one."],
        ["FORAY returns no explorer-resolvable transaction id",
         "Cycles three and four are re-scoped",
         "Say so on Monday morning, with the exact response, and propose the smallest thing that still proves the record existed: a signed daily digest published somewhere the checker can reach."],
        ["A criterion passes on a laptop and fails on the phone",
         "A demo that breaks in the room",
         "Every criterion runs on the phone first. A pass on a laptop is not a pass, and the phone run is what goes in the review."],
        ["The phone's position is mistaken for a boundary",
         "A record that overstates what it knows",
         "The caption in REQ-014 plus the certificate's own sentence. The product never claims more than the walk it recorded."],
    ], [128, 108, 247]))
    story += [para("How we work", S_H2)]
    story.append(table([
        ["", "What happens"],
        ["Every evening", "Three lines: done, next, blocked. No prose. If something is blocked it names who can unblock it."],
        ["Every pull request", "One approval from the other person before it merges, no force pushing, no deleting, administrators included. The code obeys the same rule as the product."],
        ["Every Friday, 3 p.m. your time", "The cycle's criteria read in order against a phone, failures named first, then the next cycle's scope confirmed or cut."],
        ["Definition of done", "The criterion is observed on the Android phone and the iPhone before a requirement is called done, and the observation goes in the review, not in a summary."],
    ], [128, 355]))

    # ---------------- page 6
    story += [PageBreak(), para("What I need from you", S_H1), rule()]
    story.append(table([
        ["When", "What"],
        ["By Saturday", "Whether the NIPOST key is live or a test key, and whether Stele can mount this week."],
        ["Before cycle two", "Sign-off or rejection on REQ-046 and REQ-047, because both change the recording screen and it is cheaper to get it right once."],
        ["Before cycle four", "The agency statement text, or confirmation that the proposed default is acceptable."],
        ["Ongoing", "The Friday review, and a decision within a day when something is blocked. A blocked item costs a day; a silent one costs a week."],
    ], [110, 373]))


    story += [para("Sign-off", S_H2),
              para("Scope agreed, or scope annotated and returned. Either is fine; silence is the only "
                   "answer that costs us time.", S_BODY),
              Spacer(1, 14)]
    story.append(table([
        ["", "Name", "Decision", "Date"],
        ["Proposed by", NAME, "", ""],
        ["Reviewed by", "Marvin Percival", "", ""],
    ], [110, 180, 120, 73]))
    story += [para("After the review", S_H2)]
    story.append(table([
        ["", "What happens"],
        ["The demo", "One phone, one postcode, one certificate, one QR, and a file altered by a single byte answered with no match. Recorded, and sent to you the same day"],
        ["The review", "Every criterion against the record, which of the amendments earned their day and which did not, and the plain answer to whether this is worth building at full size"],
        ["Deletion", "Demo content is gone thirty days later. The fingerprints and the anchor references stay, which is the whole argument of the product applied to its own demo"],
        ["The next decision", "Whether the register is next, and on which funding route. This document does not decide it and does not price it"],
    ], [110, 373]))
    story.append(Spacer(1, 22))
    story.append(accent("If we agree this scope, the next thing you get from me is not a document. "
                        "It is Monday morning's FORAY result, with the transaction id in it or the "
                        "failure named in it."))
    story.append(Spacer(1, 18))
    story.append(para("Prepared on 20 November 2026. Build day estimates are taken from the v0.3 "
                      "requirement table; the amendments and their costs are the only additions. "
                      "Nothing in this document prices the work, and nothing in it promises a date.",
                      S_SMALL))

    doc.build(story)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "CLIENTS" / "eri" / "exports" /
                                         "2026-11-20_Eri-practice-build-plan.pdf"))
    args = ap.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    build(out)
    print(f"written: {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
