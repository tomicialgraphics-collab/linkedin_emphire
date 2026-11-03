#!/usr/bin/env python3
"""Write the ATS CV as a minimal, single-column .docx with no wizardry.

Built by hand rather than through a template so the file stays small enough to attach:
no styles part, no numbering part, no theme, no images. Literal bullet characters with a
hanging indent, which parses at least as well as Word's list numbering.
"""

import zipfile
from xml.sax.saxutils import escape

OUT = "Mate_Oluwatunmise_CV.docx"
FONT = "Calibri"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def run(text, size=10.5, bold=False):
    half = int(round(size * 2))
    props = f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}"/>'
    if bold:
        props += "<w:b/><w:bCs/>"
    props += f'<w:sz w:val="{half}"/><w:szCs w:val="{half}"/>'
    return (f'<w:r><w:rPr>{props}</w:rPr>'
            f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r>')


def para(text="", size=10.5, bold=False, before=0, after=0, bullet=False):
    spacing = f'<w:spacing w:before="{before}" w:after="{after}" w:line="240" w:lineRule="auto"/>'
    ind = '<w:ind w:left="360" w:hanging="180"/>' if bullet else ""
    body = run(("\u2022  " + text) if bullet else text, size=size, bold=bold) if text else ""
    return f"<w:p><w:pPr>{spacing}{ind}</w:pPr>{body}</w:p>"


def heading(text):
    return para(text, size=12, bold=True, before=240, after=120)


def role(title, org, dates, bullets):
    parts = [para(title, bold=True, before=160),
             para(org),
             para(dates, after=80)]
    parts += [para(b, bullet=True, after=40) for b in bullets]
    return "".join(parts)


parts = []
parts.append(para("MATE OLUWATUNMISE OLAMILESI", size=18, bold=True, after=60))
parts.append(para("Lagos, Nigeria | +234 814 947 2486 | gabriellamate04@gmail.com | Instagram: @mate_oluwatunmise"))

parts.append(heading("PROFESSIONAL SUMMARY"))
parts.append(para(
    "Social media manager, content creator and certified voice artist with hands-on experience running "
    "Instagram and TikTok accounts for an agency, a podcast and a mobile app. Grew an agency account from "
    "1,500 to 8,200 followers in six months and raised engagement rate by 70% through interactive formats "
    "and trend-led short video. Trained in digital marketing strategy and in three professional voice-over "
    "programmes, with working command of short-form video production, scriptwriting, community management "
    "and audio editing."))

parts.append(heading("CORE COMPETENCIES"))
parts.append(para("Social Media Management: Content Calendar Planning | Page Management | Engagement Growth "
                  "Strategy | Hashtag Research and Optimization | Analytics and Key Performance Indicator (KPI) "
                  "Reporting | Community Management | Audience Segmentation | Trend Forecasting | Social Media "
                  "Advertising", after=80))
parts.append(para("Content Creation: Short-Form Video Production | Scriptwriting and Copywriting | Trend Research "
                  "| Video Editing | User-Generated Content (UGC) | Brand Storytelling | Reels and TikTok Content "
                  "| Caption Writing | A/B Content Testing | Content Repurposing", after=80))
parts.append(para("Voice-Over and Audio Production: Commercial Voice-Over | Narration and Storytelling | Brand "
                  "Intros and Explainer Videos | Audio Editing and Mastering | Character Voice Work | Script "
                  "Interpretation", after=80))
parts.append(para("Tools and Platforms: Canva | CapCut | InShot | Meta Business Suite | TikTok | Instagram Reels "
                  "| Audacity | Google Analytics | Later | Notion | Hootsuite"))

parts.append(heading("PROFESSIONAL EXPERIENCE"))
parts.append(role(
    "Social Media Manager and Content Creator", "Iconfess App | Lagos, Nigeria", "August 2026 \u2013 Present",
    ["Produce video content and voice-over recordings for brand advertisements and promotional campaigns.",
     "Write advertisement scripts, captions and calls to action that drive app downloads and user engagement.",
     "Develop platform-specific content strategies for Instagram and TikTok to reach target demographics.",
     "Collaborate with product and marketing teams to keep content aligned with campaign goals and launch timelines.",
     "Report monthly on content performance metrics with recommendations for the next content cycle."]))
parts.append(role(
    "Social Media Manager", "Agboye Ree Podcast | Lagos, Nigeria", "January 2026 \u2013 September 2026",
    ["Managed end-to-end content creation, scheduling and publishing for the podcast's social media channels.",
     "Produced short-form clips from full episodes, including one Reel that passed 50,000 organic views.",
     "Increased average video completion rate by 35% by repurposing long-form episodes into platform-native snippets.",
     "Researched trending audio and formats across each release cycle, then matched clips to the formats with reach.",
     "Answered direct messages, comments and mentions within two hours, holding community response standards across the release cycle.",
     "Aligned social media messaging with episode themes and guest promotions in coordination with the host."]))
parts.append(role(
    "Social Media Manager", "Digitblue Media Agency | Lagos, Nigeria", "December 2025 \u2013 August 2026",
    ["Built and executed monthly content calendars across Instagram and TikTok, publishing four to five posts per week against brand objectives.",
     "Grew the agency account from 1,500 to 8,200 followers in six months through trend-driven Reels and a consistent publishing rhythm.",
     "Increased engagement rate by 70% by introducing interactive formats including polls, question and answer sessions and community challenges.",
     "Analysed performance weekly in Meta Business Suite and TikTok Analytics, then adjusted format, hook and posting time to improve organic reach.",
     "Coordinated with design and copy teams to hold one brand voice and one visual identity across both platforms."]))
parts.append(role(
    "Freelance Voice Artist", "Self-Employed | Lagos, Nigeria", "2025 \u2013 Present",
    ["Deliver voice-over recordings for social media advertisements, explainer videos, brand intros and corporate narration.",
     "Work across warm commercial, energetic promotional and authoritative narrative styles.",
     "Edit and master audio in Audacity to a broadcast-quality standard before delivery.",
     "Interpret scripts and adjust pace, emphasis and tone to written or verbal client direction.",
     "Completed client projects across lifestyle, technology and entertainment brands."]))

parts.append(heading("EDUCATION"))
parts.append(para("Diploma in Pharmacy Technology", bold=True, before=80))
parts.append(para("College of Health Technology (CHT), Offa | Kwara State, Nigeria"))
parts.append(para("Graduated: 2024"))

parts.append(heading("CERTIFICATIONS"))
parts.append(para("AVOA Voiceover Masterclass 2.0 Certificate", bold=True, before=80))
parts.append(para("AVOA | October 2026", after=100))
parts.append(para("Digital Marketing Strategy Certification", bold=True))
parts.append(para("Simplilearn SkillUp | June 2026", after=100))
parts.append(para("Voice-Over Acting Course Certification", bold=True))
parts.append(para("Voiceover Workshop | February 2025"))

parts.append(heading("LANGUAGES"))
parts.append(para("English: Fluent (Written and Spoken)", after=40))
parts.append(para("Yoruba: Native Proficiency"))

document = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f'<w:document xmlns:w="{W_NS}"><w:body>'
    + "".join(parts)
    + '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
      '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
      'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
      "</w:body></w:document>"
)

content_types = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/docProps/core.xml" '
    'ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
    "</Types>"
)

rels = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" '
    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
    'Target="word/document.xml"/>'
    '<Relationship Id="rId2" '
    'Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" '
    'Target="docProps/core.xml"/>'
    "</Relationships>"
)

doc_rels = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
)

core = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
    'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
    'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
    "<dc:title>Mate Oluwatunmise Olamilesi \u2013 Curriculum Vitae</dc:title>"
    "<dc:creator>Mate Oluwatunmise Olamilesi</dc:creator>"
    "<dc:subject>Social Media Manager, Content Creator and Voice Artist</dc:subject>"
    "<cp:keywords>social media management, content creation, Instagram, TikTok, voice-over, "
    "content calendar, community management, analytics</cp:keywords>"
    "</cp:coreProperties>"
)

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", document)
    z.writestr("word/_rels/document.xml.rels", doc_rels)
    z.writestr("docProps/core.xml", core)

print("saved", OUT)
