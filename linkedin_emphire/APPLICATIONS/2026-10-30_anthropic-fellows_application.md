# Anthropic Fellows Program, AI Safety & Security: application pack

Date: 2026-10-30 (deadline day)
Cohort: January 2027, 4 months full time
Listing: job-boards.greenhouse.io/anthropic/jobs/5183044008 (read in full 10-30)
Application: Constellation / Airtable form, reached via bit.ly/afpsafety
Status: PREPARED, not submitted. Only the owner can submit.

## 1. The gate that decides this

The listing has two separate conditions, and they are easy to read as one:

1. Work authorization in the US, UK or Canada, with no visa sponsorship
   available for fellows.
2. Being located in that country for the whole four months. Remote is
   allowed, but only inside those three countries.

The repo records US work authorization (OUTREACH/2026-10-29_microsoft_airt_application.md,
"US work authorization YES, but physically based in Nigeria"). If that is
unrestricted full-time authorization not tied to an employer, condition 1 is
met. Condition 2 is not met from Lagos, so the application only holds if the
owner can physically be in the US (or UK or Canada) from January through
April 2027.

Do not enter a location that cannot be held for the full program. This is the
same failure mode flagged in the AIRT application: a location premise that
survives the form and dies at onboarding.

## 2. What the form asks (structure published for earlier cohorts, verify on the live form)

- Motivation and fit: why the program, and one or more research areas with reasons
- Optional background and links
- Three references: name, email, background (title, website, Google Scholar), and relationship (what you worked on, when, how closely)
- Logistics: other commitments and hours per week
- Optional: how you heard about it, anything else
- Consent to share details with Constellation, and an accuracy declaration covering work samples and co-authorship

Note on references: the form states they may contact references without
notice and ask for a reply within a week. Warn each referee today.

## 3. Draft answers

### Motivation and fit (about 280 words, trim to the form's limit)

Most of my work has been on the shipping side of AI, not the research side. I build LLM features for client products, and I red team them before they go out. On one support bot I ran six injection tests before launch. Four broke it: the system prompt leaked, the bot committed to a refund it had no authority to make, and a content policy got bypassed. The fixes were straightforward. What stayed with me was how little the model's refusal behaviour told me about the system's behaviour once tools and retrieval were wired in.

That is the question I keep returning to, and it is a security question more than a training question. Whether a scaffold-level check catches what a model-level refusal misses. Where an agent's authority actually lives, and what it takes to show that it did not exceed it.

I built ai-redteam-five-tests because I did not want my own findings to be trust-me results. It runs five checks against any OpenAI-compatible model and writes out the raw responses and counts so someone else can re-derive a failure from the same inputs. Every rate in the report carries its sample size, because a rate without n is a story.

I am applying to the AI Security workstream, with adversarial robustness and AI control as the second choice. My gaps are real: no peer-reviewed papers, and my computer science degree is still in progress. What I have is the habit of building measurement into the thing I am testing. Four months with a mentor and a compute budget is the version of that I cannot build alone.

### Research areas and why (about 150 words)

AI security first. Prompt injection still works because the line between
instructions and data is a convention rather than an enforcement point. Tool
descriptions sit on that same surface and draw far less attention than user
prompts, so I would want to work on how agents fail when their tools are
described dishonestly, and how to test it at a volume where the failure rate
means something.

Adversarial robustness and AI control second. The open question for me is
where to put the check. A model that refuses inside a chat window can still
act through a tool call, and an evaluation that only reads the transcript will
miss it.

Measurement runs through both: failure rates with sample sizes, negative
controls, and re-runs across model versions. A single dramatic transcript is
not evidence of anything.

### Background and links (optional field, about 120 words)

I am a software engineer at Teamart.inc in Lagos, where I build and red team
LLM features. Before that I led backend development at YKAY ConsultingHub.

Public work: github.com/Teamthy/ai-redteam-five-tests (open-source Python
harness, five reproducible failure checks), and Breaking AI, a 21-part series
on failure modes in shipped AI. The first two are published; article 2 ships
its scripts, prompts, poisoned document and tool schema with the write-up:
linkedin.com/pulse/five-boring-failures-ship-your-ai-feature-olusanya-timothy-pl4oe

Code and other writing: github.com/Teamthy

### Logistics (owner must choose the true version)

The program is 40 hours a week for four months. The form asks for other
commitments and hours. Two honest shapes:

- If leaving or pausing Teamart.inc is possible: say when, and that the four
  months are clear.
- If it is not: say that current employment is full time, name the hours per
  week that would remain committed, and let them review it case by case. The
  listing explicitly says to apply anyway and note constraints.

Do not answer this field with a guess. The commitment question is the one an
interviewer checks against the contract.

## 4. References: the one thing not prepared

Three references are required, with background and relationship detail, and
they may be contacted without warning. Nothing in the repo gives three people
who can speak to technical work together, so these must come from the owner.

Strongest candidates, in order of usefulness:

1. A manager or senior engineer at Teamart.inc who saw the red-team findings
   and the shipped fixes.
2. The lead or client contact from YKAY ConsultingHub, on the backend and
   access-control work.
3. An AI safety or security practitioner from the network who has actually
   read the harness or the series and can speak to the work, not just to the
   owner's character. The form says ML research community references are
   preferred if available.

Each entry needs: name, email, their title and public links, what you worked
on together, when, how long, and how closely you collaborated.

### Reference request message (send today, one per referee)

Subject: Anthropic Fellows reference request, reply needed within a week

I am applying to the Anthropic Fellows Program today, in the AI Security
track. They ask for three references and they contact them directly, often
without warning, with a one-week reply window.

Would you be willing to speak to my work on <specific project>? If yes, send
me the best email and I will put it in the form today. Happy to send the
harness and the write-up again so it is fresh.

No pressure if the timing is bad. I would rather ask now than have you
surprised by an email.

## 5. Submission checklist

1. Confirm the location answer is one that can be held for four months.
2. Send the three reference requests. Do not submit with placeholder names.
3. Regenerate the resume if any detail changed: `python linkedin_emphire/RESUME/build_resume_anthropic_fellows.py`
   writes RESUME/Timothy_Olusanya_Anthropic_Fellows.pdf and .docx.
4. Open bit.ly/afpsafety. It goes to the Constellation form, not to LinkedIn.
5. Complete the Constellation form. The Greenhouse page says the Greenhouse
   application is not required and will not be considered on its own.
6. Paste the answers above, adjusted to the form's limits and to the truth
   about commitments.
7. Tick the consent and accuracy boxes, then submit.
8. Save the confirmation and the submitted text back into this file under
   SUBMITTED, so the record shows what was actually sent.

## 6. Resume

`RESUME/Timothy_Olusanya_Anthropic_Fellows.pdf` (one page) and the .docx twin,
built by `linkedin_emphire/RESUME/build_resume_anthropic_fellows.py`.

Research-forward: summary, research interests, then artifacts before backend
work. Content is limited to what the repo can verify: the harness, the series,
the chatbot red team (six tests, four breaks), Teamart.inc, YKAY, NOUN
enrolment expected April 2028, and the NIST bootcamp.

Deliberately omitted: the LandSecure and EDUos depth that fills the AIRT
resume, KwikPOS, and any unpublished claim. Anthropic's security track values
offensive security experience, CVEs and bug bounties; none are on record, so
none are claimed.
