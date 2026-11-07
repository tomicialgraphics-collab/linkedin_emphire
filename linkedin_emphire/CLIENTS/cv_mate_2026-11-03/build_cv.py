#!/usr/bin/env python3
"""Build the ATS CV for Mate Oluwatunmise Olamilesi as a single-column .docx.

No tables, no text boxes, no columns, no images, no header or footer content.
Calibri throughout, body 10.5pt, headings 12pt bold caps, name 18pt bold.
"""

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

FONT = "Calibri"
OUT = "Mate_Oluwatunmise_CV.docx"

doc = Document()

# Base style: one font, one size, no colour tricks.
style = doc.styles["Normal"]
style.font.name = FONT
style.font.size = Pt(10.5)
rpr = style.element.get_or_add_rPr()
rfonts = rpr.find(qn("w:rFonts"))
if rfonts is None:
    rfonts = rpr.makeelement(qn("w:rFonts"), {})
    rpr.append(rfonts)
for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
    rfonts.set(qn(attr), FONT)

style.paragraph_format.space_before = Pt(0)
style.paragraph_format.space_after = Pt(0)
style.paragraph_format.line_spacing = 1.0

for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)


def para(text="", size=10.5, bold=False, before=0, after=0, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.0
    if align is not None:
        p.alignment = align
    if text:
        r = p.add_run(text)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.bold = bold
    return p


def heading(text):
    para(text, size=12, bold=True, before=12, after=6)


def role(title, org, dates, bullets):
    para(title, bold=True, before=8, after=0)
    para(org, before=0, after=0)
    para(dates, before=0, after=4)
    for b in bullets:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.left_indent = Inches(0.25)
        r = p.add_run(b)
        r.font.name = FONT
        r.font.size = Pt(10.5)


# ---------------------------------------------------------------- header
para("MATE OLUWATUNMISE OLAMILESI", size=18, bold=True, after=2)
para("Lagos, Nigeria | +234 814 947 2486 | gabriellamate04@gmail.com | Instagram: @mate_oluwatunmise", after=0)

# ---------------------------------------------------------------- summary
heading("PROFESSIONAL SUMMARY")
para(
    "Social media manager, content creator and certified voice artist with hands-on experience running "
    "Instagram and TikTok accounts for an agency, a podcast and a mobile app. Grew an agency account from "
    "1,500 to 8,200 followers in six months and raised engagement rate by 70% through interactive formats "
    "and trend-led short video. Trained in digital marketing strategy and in three professional voice-over "
    "programmes, with working command of short-form video production, scriptwriting, community management "
    "and audio editing.",
    after=0,
)

# ---------------------------------------------------------------- skills
heading("CORE COMPETENCIES")
para("Social Media Management: Content Calendar Planning | Page Management | Engagement Growth Strategy | "
     "Hashtag Research and Optimization | Analytics and Key Performance Indicator (KPI) Reporting | "
     "Community Management | Audience Segmentation | Trend Forecasting | Social Media Advertising", after=4)
para("Content Creation: Short-Form Video Production | Scriptwriting and Copywriting | Trend Research | "
     "Video Editing | User-Generated Content (UGC) | Brand Storytelling | Reels and TikTok Content | "
     "Caption Writing | A/B Content Testing | Content Repurposing", after=4)
para("Voice-Over and Audio Production: Commercial Voice-Over | Narration and Storytelling | Brand Intros and "
     "Explainer Videos | Audio Editing and Mastering | Character Voice Work | Script Interpretation", after=4)
para("Tools and Platforms: Canva | CapCut | InShot | Meta Business Suite | TikTok | Instagram Reels | "
     "Audacity | Google Analytics | Later | Notion | Hootsuite", after=0)

# ---------------------------------------------------------------- experience
heading("PROFESSIONAL EXPERIENCE")

role(
    "Social Media Manager and Content Creator",
    "Iconfess App | Lagos, Nigeria",
    "August 2026 – Present",
    [
        "Produce video content and voice-over recordings for brand advertisements and promotional campaigns.",
        "Write advertisement scripts, captions and calls to action that drive app downloads and user engagement.",
        "Develop platform-specific content strategies for Instagram and TikTok to reach target demographics.",
        "Collaborate with product and marketing teams to keep content aligned with campaign goals and launch timelines.",
        "Report monthly on content performance metrics with recommendations for the next content cycle.",
    ],
)

role(
    "Social Media Manager",
    "Agboye Ree Podcast | Lagos, Nigeria",
    "January 2026 – September 2026",
    [
        "Managed end-to-end content creation, scheduling and publishing for the podcast's social media channels.",
        "Produced short-form clips from full episodes, including one Reel that passed 50,000 organic views.",
        "Increased average video completion rate by 35% by repurposing long-form episodes into platform-native snippets.",
        "Researched trending audio and formats across each release cycle, then matched clips to the formats with reach.",
        "Answered direct messages, comments and mentions within two hours, holding community response standards across the release cycle.",
        "Aligned social media messaging with episode themes and guest promotions in coordination with the host.",
    ],
)

role(
    "Social Media Manager",
    "Digitblue Media Agency | Lagos, Nigeria",
    "December 2025 – August 2026",
    [
        "Built and executed monthly content calendars across Instagram and TikTok, publishing four to five posts per week against brand objectives.",
        "Grew the agency account from 1,500 to 8,200 followers in six months through trend-driven Reels and a consistent publishing rhythm.",
        "Increased engagement rate by 70% by introducing interactive formats including polls, question and answer sessions and community challenges.",
        "Analysed performance weekly in Meta Business Suite and TikTok Analytics, then adjusted format, hook and posting time to improve organic reach.",
        "Coordinated with design and copy teams to hold one brand voice and one visual identity across both platforms.",
    ],
)

role(
    "Freelance Voice Artist",
    "Self-Employed | Lagos, Nigeria",
    "2025 – Present",
    [
        "Deliver voice-over recordings for social media advertisements, explainer videos, brand intros and corporate narration.",
        "Work across warm commercial, energetic promotional and authoritative narrative styles.",
        "Edit and master audio in Audacity to a broadcast-quality standard before delivery.",
        "Interpret scripts and adjust pace, emphasis and tone to written or verbal client direction.",
        "Completed client projects across lifestyle, technology and entertainment brands.",
    ],
)

# ---------------------------------------------------------------- education
heading("EDUCATION")
role(
    "Diploma in Pharmacy Technology",
    "College of Health Technology (CHT), Offa | Kwara State, Nigeria",
    "Graduated: 2024",
    [],
)

# ---------------------------------------------------------------- certifications
heading("CERTIFICATIONS")
para("AVOA Voiceover Masterclass 2.0 Certificate", bold=True, before=4, after=0)
para("AVOA | October 2026", after=6)
para("Digital Marketing Strategy Certification", bold=True, before=0, after=0)
para("Simplilearn SkillUp | June 2026", after=6)
para("Voice-Over Acting Course Certification", bold=True, before=0, after=0)
para("Voiceover Workshop | February 2025", after=0)

# ---------------------------------------------------------------- languages
heading("LANGUAGES")
para("English: Fluent (Written and Spoken)", after=2)
para("Yoruba: Native Proficiency", after=0)

# ---------------------------------------------------------------- properties
cp = doc.core_properties
cp.title = "Mate Oluwatunmise Olamilesi – Curriculum Vitae"
cp.author = "Mate Oluwatunmise Olamilesi"
cp.subject = "Social Media Manager, Content Creator and Voice Artist"
cp.keywords = ("social media management, content creation, Instagram, TikTok, voice-over, "
               "content calendar, community management, analytics")

doc.save(OUT)
print("saved", OUT)
