#!/usr/bin/env python3
"""Build Timothy's AIRT / Microsoft MTS (Agentic AI Security) resume.
ATS-safe one-page PDF + DOCX. Only verified, public or first-hand content.
Tailored to job 1970393557041155 (adversarial AI-agent systems, swarm-like
behavior, instrumented environments, provenance, containment)."""
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
pdf.set_auto_page_break(auto=True, margin=30)
pdf.set_margins(44, 36, 44)
pdf.add_font("DJV", "", FONT + "DejaVuSans.ttf")
pdf.add_font("DJV", "B", FONT + "DejaVuSans-Bold.ttf")
pdf.add_page()
W = pdf.w - 88


def name_block():
    pdf.set_font("DJV", "B", 18)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 21, "OLUSANYA TIMOTHY", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 10.5)
    pdf.set_text_color(*INK)
    pdf.cell(W, 14, "AI Security Researcher  |  Adversarial AI & Agentic Systems",
             new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 8.8)
    pdf.set_text_color(*GREY)
    pdf.cell(W, 13, "Lagos, Nigeria  |  olusanyatimothy54@gmail.com  |  github.com/Teamthy  |  linkedin.com/in/olusanya-timothy",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)


def section(title):
    pdf.ln(1.5)
    pdf.set_font("DJV", "B", 10)
    pdf.set_text_color(*NAVY)
    pdf.cell(W, 13, title.upper(), new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(180, 195, 215)
    pdf.set_line_width(0.8)
    pdf.line(44, y + 1, pdf.w - 44, y + 1)
    pdf.ln(4.5)


def body(text, size=9.0, gap=2.2):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    pdf.multi_cell(W, 11.1, text)
    pdf.ln(gap)


def bullet(text, size=9.0):
    pdf.set_font("DJV", "", size)
    pdf.set_text_color(*INK)
    x = pdf.get_x()
    pdf.cell(10, 11.1, "\u2022")
    pdf.multi_cell(W - 10, 11.1, text)
    pdf.ln(0.5)


def role(title, meta):
    pdf.set_font("DJV", "B", 9.8)
    pdf.set_text_color(*INK)
    pdf.cell(W, 12.5, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DJV", "", 8.6)
    pdf.set_text_color(*GREY)
    pdf.cell(W, 11.5, meta, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.5)


name_block()

section("Summary")
body("AI security engineer who builds adversarial test infrastructure for LLM and "
     "agentic systems and treats reproducibility as the deliverable. Released an "
     "open-source red-team harness and writes a public 21-part series on failure "
     "modes in shipped AI. Work is built around instrumented experiments, provenance, "
     "and findings a stranger can re-derive from the raw output.")

section("Selected Research Artifacts")
bullet("ai-redteam-five-tests (open source, on my GitHub profile): a runnable "
       "red-team harness that runs five reproducible failure checks against any "
       "OpenAI-compatible model: prompt injection, poisoned retrieval, tool-"
       "description injection, multilingual refusal, and failure-rate metrics with "
       "the sample size beside every rate. Ships the method, not pre-baked results "
       ": raw responses and counts are written out so a finding is re-derivable.")
bullet("Breaking AI (public, 21-part, article 1 October 2026): documents "
       "reproducible failure modes in shipped AI features, with the exact test "
       "inputs and the controls that stop them.")
bullet("Chatbot pre-launch red team: built an LLM support bot (system prompt, tool "
       "wiring), ran six injection tests before launch, four succeeded (system "
       "prompt leak, an unauthorized refund commitment, a content policy bypass). "
       "Shipped the fixes and turned every finding into a reusable test checklist.")

section("Technical Skills")
body("Languages: Python, Go, TypeScript, JavaScript, SQL", size=8.8, gap=1.2)
body("AI / LLM: LLM APIs, prompt engineering, prompt-injection testing, agentic "
     "security, tool/function calling, retrieval pipelines, model evaluation, NIST "
     "AI RMF", size=8.8, gap=1.2)
body("Research methods: instrumented experiments, reproducible evaluation, "
     "provenance and attribution, negative controls, behavioral signature analysis",
     size=8.8, gap=1.2)
body("Backend & data: REST APIs, Node.js, NestJS, Go, JWT auth, RBAC, PostgreSQL, "
     "MongoDB, Docker, Git", size=8.8, gap=1.2)

section("Experience")
role("Software Engineer - AI Integration & Red Teaming, Teamart.inc",
     "Lagos, Nigeria  |  July 2025 - Present")
bullet("Build and ship LLM features for client products: chatbots, retrieval "
       "pipelines, tool-calling workflows.")
bullet("Run pre-launch red teaming (prompt injection, unauthorized tool calls, "
       "policy bypass) and deliver prioritized findings with fixes.")
bullet("Develop backend APIs in Go and Node.js, owning design through deployment.")
role("Senior Developer, YKAY ConsultingHub",
     "Lagos, Nigeria  |  Nov 2024 - June 2025")
bullet("Led backend development in Go and Node.js across client-facing products.")
bullet("Designed REST APIs and multi-role authentication (JWT, RBAC) for systems "
       "with distinct permission levels.")
bullet("Set modular architecture standards and ran Git-based review workflows.")

section("Projects")
bullet("Nigeria LandSecure (Go, Next.js, PostgreSQL): document storage and "
       "verification with role-based permissions; fixed concurrency failures under "
       "simultaneous verification using controlled transactions and row locking.")
bullet("EDUos (Node.js, TypeScript, Next.js): multi-role education platform; fixed "
       "an authorization middleware flaw that exposed data across roles, then "
       "hardened the access model.")

section("Education & Certifications")
bullet("BSc Computer Science - National Open University of Nigeria  |  Expected "
       "April 2028 (working while enrolled)")
bullet("Previous: Medical Laboratory Science (healthcare domain background)")
body("NIST AI Bootcamp (AI Risk & Safety Frameworks)  |  AI Engineering & Backend "
     "Development (Udemy)", size=8.8, gap=0)

pdf.output(f"{OUT}/Timothy_Olusanya_AIRT_MTS_Agentic_Security.pdf")

# ---------------- DOCX (editable twin) ----------------
from docx import Document
from docx.shared import Pt

doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10)

h = doc.add_paragraph()
r = h.add_run("OLUSANYA TIMOTHY")
r.bold = True
r.font.size = Pt(17)
h.add_run("\nAI Security Researcher | Adversarial AI & Agentic Systems").font.size = Pt(10.5)
h.add_run("\nLagos, Nigeria | olusanyatimothy54@gmail.com | github.com/Teamthy | linkedin.com/in/olusanya-timothy").font.size = Pt(9)


def dsec(t):
    p = doc.add_paragraph()
    r = p.add_run(t.upper())
    r.bold = True
    r.font.size = Pt(10.5)
    return p


dsec("Summary")
doc.add_paragraph("AI security engineer who builds adversarial test infrastructure for LLM and agentic systems and treats reproducibility as the deliverable. Released an open-source red-team harness and writes a public 21-part series on failure modes in shipped AI. Work is built around instrumented experiments, provenance, and findings a stranger can re-derive from the raw output.")

dsec("Selected Research Artifacts")
for b in [
    "ai-redteam-five-tests (open source, on my GitHub profile): a runnable red-team harness that runs five reproducible failure checks against any OpenAI-compatible model: prompt injection, poisoned retrieval, tool-description injection, multilingual refusal, and failure-rate metrics with the sample size beside every rate. Ships the method, not pre-baked results; raw responses and counts are written out so a finding is re-derivable.",
    "Breaking AI (public, 21-part, article 1 October 2026): documents reproducible failure modes in shipped AI features, with the exact test inputs and the controls that stop them.",
    "Chatbot pre-launch red team: built an LLM support bot (system prompt, tool wiring), ran six injection tests before launch, four succeeded (system prompt leak, an unauthorized refund commitment, a content policy bypass). Shipped the fixes and turned every finding into a reusable test checklist.",
]:
    doc.add_paragraph(b, style="List Bullet")

dsec("Technical Skills")
for s in [
    "Languages: Python, Go, TypeScript, JavaScript, SQL",
    "AI / LLM: LLM APIs, prompt engineering, prompt-injection testing, agentic security, tool/function calling, retrieval pipelines, model evaluation, NIST AI RMF",
    "Research methods: instrumented experiments, reproducible evaluation, provenance and attribution, negative controls, behavioral signature analysis",
    "Backend & data: REST APIs, Node.js, NestJS, Go, JWT auth, RBAC, PostgreSQL, MongoDB, Docker, Git",
]:
    doc.add_paragraph(s, style="List Bullet")

dsec("Experience")
p = doc.add_paragraph(); p.add_run("Software Engineer - AI Integration & Red Teaming, Teamart.inc | Lagos, Nigeria | July 2025 - Present").bold = True
for b in [
    "Build and ship LLM features for client products: chatbots, retrieval pipelines, tool-calling workflows.",
    "Run pre-launch red teaming (prompt injection, unauthorized tool calls, policy bypass) and deliver prioritized findings with fixes.",
    "Develop backend APIs in Go and Node.js, owning design through deployment.",
]:
    doc.add_paragraph(b, style="List Bullet")
p = doc.add_paragraph(); p.add_run("Senior Developer, YKAY ConsultingHub | Lagos, Nigeria | Nov 2024 - June 2025").bold = True
for b in [
    "Led backend development in Go and Node.js across client-facing products.",
    "Designed REST APIs and multi-role authentication (JWT, RBAC) for systems with distinct permission levels.",
    "Set modular architecture standards and ran Git-based review workflows.",
]:
    doc.add_paragraph(b, style="List Bullet")

dsec("Projects")
for b in [
    "Nigeria LandSecure (Go, Next.js, PostgreSQL): document storage and verification with role-based permissions; fixed concurrency failures under simultaneous verification using controlled transactions and row locking.",
    "EDUos (Node.js, TypeScript, Next.js): multi-role education platform; fixed an authorization middleware flaw that exposed data across roles, then hardened the access model.",
]:
    doc.add_paragraph(b, style="List Bullet")

dsec("Education & Certifications")
doc.add_paragraph("BSc Computer Science - National Open University of Nigeria | Expected April 2028 (working while enrolled)", style="List Bullet")
doc.add_paragraph("Previous: Medical Laboratory Science (healthcare domain background)", style="List Bullet")
doc.add_paragraph("NIST AI Bootcamp (AI Risk & Safety Frameworks) | AI Engineering & Backend Development (Udemy)")

doc.save(f"{OUT}/Timothy_Olusanya_AIRT_MTS_Agentic_Security.docx")

print("PDF pages:", pdf.page)
print("written:", f"{OUT}/Timothy_Olusanya_AIRT_MTS_Agentic_Security.pdf")
