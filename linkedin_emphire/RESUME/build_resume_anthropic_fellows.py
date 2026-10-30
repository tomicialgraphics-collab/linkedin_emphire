#!/usr/bin/env python3
"""Build Timothy's Anthropic Fellows Program (AI Safety & Security) resume.

One page, ATS-safe PDF + DOCX twin. Research-forward: artifacts and research
interests lead, backend work is compressed. Only verified, first-hand content
from the repo (ai-redteam-five-tests, Breaking AI 1 and 2, Teamart.inc,
YKAY ConsultingHub, NOUN enrolment, NIST bootcamp).

Target: Anthropic Fellows Program, AI Safety & Security, January 2027 cohort.
Job board: job-boards.greenhouse.io/anthropic/jobs/5183044008
Application: Constellation / Airtable form linked from bit.ly/afpsafety
"""
from fpdf import FPDF
import os

OUT = "/home/user/linkedin_emphire/RESUME"
os.makedirs(OUT, exist_ok=True)
FONT = "/usr/share/fonts/truetype/dejavu/"
NAVY = (12, 26, 52)
INK = (30, 34, 40)
GREY = (95, 104, 118)


class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


pdf = CV(orientation="P", unit="pt", format="A4")
pdf.set_auto_page_break(auto=False)
pdf.set_margins(44, 34, 44)
pdf.add_font("DJV", "", FONT + "DejaVuSans.ttf")
pdf.add_font("DJV", "B", FONT + "DejaVuSans-Bold.ttf")
pdf.add_page()
W = pdf.w - 88


def line(text, size=8.6, style="", color=INK, gap=1.4, indent=0, lead=10.6):
    pdf.set_font("DJV", style, size)
    pdf.set_text_color(*color)
    pdf.set_x(44 + indent)
    pdf.multi_cell(W - indent, lead, text)
    pdf.ln(gap)


def section(title):
    pdf.ln(2.0)
    pdf.set_font("DJV", "B", 9.4)
    pdf.set_text_color(*NAVY)
    pdf.set_x(44)
    pdf.cell(W, 12, title.upper(), new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(180, 195, 215)
    pdf.set_line_width(0.7)
    pdf.line(44, y + 0.5, pdf.w - 44, y + 0.5)
    pdf.ln(4.0)


def bullet(text, size=8.6, lead=10.6):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    pdf.set_x(44)
    pdf.cell(9, lead, "-")
    pdf.set_x(53)
    pdf.multi_cell(W - 9, lead, text)
    pdf.ln(1.2)


# ---------------- header ----------------
pdf.set_font("DJV", "B", 17.5)
pdf.set_text_color(*NAVY)
pdf.set_x(44)
pdf.cell(W, 19.5, "OLUSANYA TIMOTHY", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("DJV", "", 9.8)
pdf.set_text_color(*INK)
pdf.set_x(44)
pdf.cell(W, 13, "AI Safety & Security Research  |  Empirical Evaluation, Red Teaming, Agentic Systems",
         new_x="LMARGIN", new_y="NEXT")

pdf.set_font("DJV", "", 8.4)
pdf.set_text_color(*GREY)
pdf.set_x(44)
pdf.cell(W, 12, "Lagos, Nigeria (UTC+1)  |  olusanyatimothy54@gmail.com  |  github.com/Teamthy  |  linkedin.com/in/olusanya-timothy",
         new_x="LMARGIN", new_y="NEXT")
pdf.ln(3)

# ---------------- summary ----------------
section("Summary")
line("Engineer who builds adversarial test infrastructure for LLM and agentic systems and treats "
     "reproducibility as the deliverable. Published an open-source harness that runs five failure checks "
     "against any OpenAI-compatible model, and a public series documenting failure modes in shipped AI "
     "with the exact inputs and the controls that catch them. Every result traces to a prompt, a model "
     "version and a commit, with the sample size beside each rate.")

# ---------------- research interests ----------------
section("Research Interests")
line("AI security: prompt injection, tool-description and retrieval poisoning, agentic tool abuse. "
     "Adversarial robustness and AI control: whether a scaffold-level check catches what a model-level "
     "refusal misses. Measurement: failure rates with sample sizes, negative controls, and re-runs "
     "across model versions.")

# ---------------- artifacts ----------------
section("Selected Research Artifacts")
bullet("ai-redteam-five-tests (open source, Python): runnable harness that runs five reproducible checks "
       "against any OpenAI-compatible model, covering prompt injection, poisoned retrieval, tool-description "
       "injection, multilingual refusal and failure-rate reporting. Writes raw responses and counts out so a "
       "finding is re-derivable by someone who was not in the room.")
bullet("Breaking AI (public, 21-part series, first two published October 2026): reproducible failure modes in "
       "shipped AI features, with the exact test inputs and the fixes that stop them. Article 2 ships the "
       "scripts, prompts, poisoned document and tool schema alongside the write-up.")
bullet("Chatbot pre-launch red team: built an LLM support bot with its system prompt and tool wiring, ran six "
       "injection tests and four broke it (system prompt leak, an unauthorized refund commitment, a content "
       "policy bypass). Shipped the fixes and turned each finding into a reusable test.")

# ---------------- skills ----------------
section("Technical Skills")
line("Languages: Python (primary), Go, TypeScript, JavaScript, SQL", gap=0.8)
line("AI / LLM: LLM APIs, tool calling, retrieval pipelines, evaluation harnesses, prompt-injection testing, "
     "model evaluation, NIST AI RMF", gap=0.8)
line("Research methods: instrumented experiments, reproducible evaluation, negative controls, failure-rate "
     "reporting with sample sizes", gap=0.8)
line("Backend and data: REST APIs, Node.js, NestJS, JWT and RBAC, PostgreSQL, MongoDB, Docker, Git")

# ---------------- experience ----------------
section("Experience")
pdf.set_font("DJV", "B", 9.2)
pdf.set_text_color(*INK)
pdf.set_x(44)
pdf.cell(W, 11.5, "Software Engineer, AI Integration & Red Teaming  |  Teamart.inc", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("DJV", "", 8.2)
pdf.set_text_color(*GREY)
pdf.set_x(44)
pdf.cell(W, 10.5, "Lagos, Nigeria  |  July 2025 to present", new_x="LMARGIN", new_y="NEXT")
bullet("Build and ship LLM features for client products: chatbots, retrieval pipelines, tool-calling workflows.", size=8.5)
bullet("Run pre-launch red teaming, including prompt injection, unauthorized tool calls and policy bypass, and "
       "deliver prioritized findings with fixes.", size=8.5)

pdf.set_font("DJV", "B", 9.2)
pdf.set_text_color(*INK)
pdf.set_x(44)
pdf.cell(W, 11.5, "Senior Developer  |  YKAY ConsultingHub", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("DJV", "", 8.2)
pdf.set_text_color(*GREY)
pdf.set_x(44)
pdf.cell(W, 10.5, "Lagos, Nigeria  |  November 2024 to June 2025", new_x="LMARGIN", new_y="NEXT")
bullet("Led backend development in Go and Node.js across client-facing products; designed REST APIs and "
       "multi-role authentication with JWT and RBAC.", size=8.5)

# ---------------- links ----------------
section("Code and Writing")
line("Harness: github.com/Teamthy/ai-redteam-five-tests", gap=0.8)
line("Series: linkedin.com/pulse/five-boring-failures-ship-your-ai-feature-olusanya-timothy-pl4oe", gap=0.8)
line("Profile: github.com/Teamthy", gap=0.8)

# ---------------- education ----------------
section("Education and Certifications")
bullet("BSc Computer Science, National Open University of Nigeria, expected April 2028 (distance study "
       "alongside full-time work).", size=8.5)
bullet("Previous study: Medical Laboratory Science. Coursework and training: NIST AI Bootcamp (AI Risk and "
       "Safety Frameworks).", size=8.5)

pdf.output(os.path.join(OUT, "Timothy_Olusanya_Anthropic_Fellows.pdf"))
pages = pdf.page

# ---------------- DOCX twin ----------------
from docx import Document
from docx.shared import Pt

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(9.5)

h = doc.add_paragraph()
r = h.add_run("OLUSANYA TIMOTHY")
r.bold = True
r.font.size = Pt(16)
h.add_run("\nAI Safety & Security Research | Empirical Evaluation, Red Teaming, Agentic Systems").font.size = Pt(10)
h.add_run("\nLagos, Nigeria (UTC+1) | olusanyatimothy54@gmail.com | github.com/Teamthy | linkedin.com/in/olusanya-timothy").font.size = Pt(8.5)


def dsec(t):
    p = doc.add_paragraph()
    r = p.add_run(t.upper())
    r.bold = True
    r.font.size = Pt(9.5)


dsec("Summary")
doc.add_paragraph("Engineer who builds adversarial test infrastructure for LLM and agentic systems and treats reproducibility as the deliverable. Published an open-source harness that runs five failure checks against any OpenAI-compatible model, and a public series documenting failure modes in shipped AI with the exact inputs and the controls that catch them. Every result traces to a prompt, a model version and a commit, with the sample size beside each rate.")

dsec("Research Interests")
doc.add_paragraph("AI security: prompt injection, tool-description and retrieval poisoning, agentic tool abuse. Adversarial robustness and AI control: whether a scaffold-level check catches what a model-level refusal misses. Measurement: failure rates with sample sizes, negative controls, and re-runs across model versions.")

dsec("Selected Research Artifacts")
for b in [
    "ai-redteam-five-tests (open source, Python): runnable harness that runs five reproducible checks against any OpenAI-compatible model, covering prompt injection, poisoned retrieval, tool-description injection, multilingual refusal and failure-rate reporting. Writes raw responses and counts out so a finding is re-derivable by someone who was not in the room.",
    "Breaking AI (public, 21-part series, first two published October 2026): reproducible failure modes in shipped AI features, with the exact test inputs and the fixes that stop them. Article 2 ships the scripts, prompts, poisoned document and tool schema alongside the write-up.",
    "Chatbot pre-launch red team: built an LLM support bot with its system prompt and tool wiring, ran six injection tests and four broke it (system prompt leak, an unauthorized refund commitment, a content policy bypass). Shipped the fixes and turned each finding into a reusable test.",
]:
    doc.add_paragraph(b, style="List Bullet")

dsec("Technical Skills")
for s in [
    "Languages: Python (primary), Go, TypeScript, JavaScript, SQL",
    "AI / LLM: LLM APIs, tool calling, retrieval pipelines, evaluation harnesses, prompt-injection testing, model evaluation, NIST AI RMF",
    "Research methods: instrumented experiments, reproducible evaluation, negative controls, failure-rate reporting with sample sizes",
    "Backend and data: REST APIs, Node.js, NestJS, JWT and RBAC, PostgreSQL, MongoDB, Docker, Git",
]:
    doc.add_paragraph(s, style="List Bullet")

dsec("Experience")
p = doc.add_paragraph(); p.add_run("Software Engineer, AI Integration & Red Teaming | Teamart.inc | Lagos, Nigeria | July 2025 to present").bold = True
for b in [
    "Build and ship LLM features for client products: chatbots, retrieval pipelines, tool-calling workflows.",
    "Run pre-launch red teaming, including prompt injection, unauthorized tool calls and policy bypass, and deliver prioritized findings with fixes.",
]:
    doc.add_paragraph(b, style="List Bullet")
p = doc.add_paragraph(); p.add_run("Senior Developer | YKAY ConsultingHub | Lagos, Nigeria | November 2024 to June 2025").bold = True
doc.add_paragraph("Led backend development in Go and Node.js across client-facing products; designed REST APIs and multi-role authentication with JWT and RBAC.", style="List Bullet")

dsec("Code and Writing")
doc.add_paragraph("Harness: github.com/Teamthy/ai-redteam-five-tests", style="List Bullet")
doc.add_paragraph("Series: linkedin.com/pulse/five-boring-failures-ship-your-ai-feature-olusanya-timothy-pl4oe", style="List Bullet")

dsec("Education and Certifications")
doc.add_paragraph("BSc Computer Science, National Open University of Nigeria, expected April 2028 (distance study alongside full-time work).", style="List Bullet")
doc.add_paragraph("Previous study: Medical Laboratory Science. Coursework and training: NIST AI Bootcamp (AI Risk and Safety Frameworks).", style="List Bullet")

doc.save(os.path.join(OUT, "Timothy_Olusanya_Anthropic_Fellows.docx"))

print("PDF pages:", pages)
print("written:", os.path.join(OUT, "Timothy_Olusanya_Anthropic_Fellows.pdf"))
