---
deliverable: doc
id: 2026-11-15_upwork-talent-paste-analysis
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 10:26 WAT, read from the system clock in the sandbox before this file was opened for gate.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner ran eight talent searches and pasted nine screenshots, including two full profile pages. This file
  reads only what those screenshots show. The first finding is unwelcome and load-bearing: the searches did not measure
  supply, because the search engine ignores the syntax and ORs the words. So the analysis keeps the composition of
  page one, which is real, and throws away the result counts, which are not.
sources_read: >-
  read: nine pasted screenshots, listed in the pack section below, covering talent search for AI red teaming, ai
  securiy, AI evaluation, AI integration, three boolean variants, and one policy query, plus the full profiles of
  Eugene T. and Kunal N. Cross-read against the four-lane brief of the same date and the live profile state file.
---

# What the nine pastes say, and which lane to lead with

Short version: the searches tell us almost nothing about how many people do this work, and a great deal about what the
people who surface look like. Two things came out of that, one of them changes your title and one changes how you
price.

## 1. None of these searches measured what it was asked to measure

Every count you pasted is a count of profiles containing the word AI somewhere, not a count of specialists.

| query you ran | pages of results | what the first page actually contains |
|---|---|---|
| `AI RED TEAMING` | 2,771 | AI engineers and automators at $5 to $69, then a few genuine security profiles |
| `ai securiy` (typo) | 2,141 | the same population: an AI engineer at $10, one at $5, one at $69 |
| `AI EVALUATION` | 6,171 | annotators, translators, QA testers, one research consultant, one Claude Code specialist |
| `AI INTEGRATION` | 10,001, the cap | integration developers from $3 to $95 |
| `(AI AND INTEGRATION) AND (AI OR red OR teaming …)` | 10,001, the cap | agents, RAG, MCP, one LLM testing profile, one $95 Claude agent specialist |
| `(AI OR security OR LLM security OR …)` | 10,001, the cap | AI automation, a PhD thesis editor, a DevOps engineer, an academic writer |
| `(agentic OR MCP OR Claude Code … OR AI usage policy OR AI incident)` | 10,001, the cap | SEO writers, content writers, a $200 brand strategist |

Three proofs that the counts are noise, in your own screenshots:

| proof | what you pasted | what it means |
|---|---|---|
| A typo cost 23% of the count | `ai securiy` returned 2,141 pages against 2,771 for `AI RED TEAMING` | a search that loses only a fifth of its results to a misspelling is matching on `ai`, not on the phrase |
| The boolean syntax was not executed | `no AI policy` returned eight profiles: SEO at $5, content at $3, brand strategy at $200, SEO at $75, content at $25 twice, content at $6, SEO at $40 | the operators arrived as words, and the `·` tokens in the URL are the parser splitting them apart |
| The cap swallows the distinction | four different queries, four different populations, all "1 of 10001" | when the ceiling is identical for `MCP` and for `no AI policy`, the ceiling is not measuring the query |

What survives the noise is the composition of page one, because that is what a client sees. That is what the rest of
this file uses.

One more caveat that matters for what page one means: several cards carry a **Boosted** label. Position on page one is
partly paid placement, which is why a $5 profile with $20K+ earned and a $69 profile with $200K+ earned sit above a
$60 red-team profile. Read the whole page, never the first three cards.

## 2. What the supply actually looks like, lane by lane

### Red teaming: the specialism is thin, and its practitioners are mostly new

Ten profiles on the first page of `AI RED TEAMING`, and only four name red teaming, AI security or adversarial work:

| profile | headline | rate | badge | earnings | note |
|---|---|---|---|---|---|
| Mark P. | Senior AI & Security Engineer, AI Agents, LLM, Cybersecurity, HIPAA | $150 | Rising Talent | $0 | 30+ years, two books, test counts in the copy, zero Upwork earnings |
| Ahmad P. | Penetration Tester, Ethical Hacker, Red Team | $65 | Top Rated | $9K+ | CTF organiser, PNPT and CRTO, AI mentioned once |
| Abhishek G. | Algorithmic Trading Developer, Gen AI Red Teaming | $60 | Top Rated Plus | $600K+ | trading first, red teaming second |
| Carmen M. | vCISO, Pentester, AI Security & LLM Red Teaming Specialist, AI-SPM | $50 | Top Rated | not shown | 25 years, Copilot Studio and Azure AI, NIST AI RMF and ATLAS in the copy |
| Foysal H. | Penetration Tester, OSCP, CEH, CREST, Web, API, Mobile & AI Security | $29 | Top Rated | not shown | 200+ engagements, LLM security is one line in a long VAPT list |
| Kunal N. | Penetration Tester, Web, API, Cloud & AI Security, Red Teaming | $20 | Top Rated | $2K+ | 7 jobs, 95 hours, LLM security assessment in his portfolio |

Read the pattern: the one profile at $150 has never been paid on Upwork. Abhishek's $60 comes from trading, not from security. The
two with real security practices price at $29 and $20. Nobody in that list shows a rerunnable test artifact.

Everything else on that page is not security at all: AI engineers at $10, $5 and $69 whose copy mentions agents, RAG and
automation. That is what the keyword returns, and it is what a client sees when they search it.

### Evaluation: the word is contaminated, exactly as predicted

Ten profiles on the first page of `AI EVALUATION`, sorted by what they actually sell:

| what they sell | profiles | rates |
|---|---|---|
| annotation, localisation, language QA | Septian A., Maximilian H., Sylvia M F., Beatriz S. | $8, $23.75, $30, $17 |
| QA and usability testing of AI output | William Y., Thomas P. | $25, $25 |
| evaluation as part of building and testing agents | Yu Fong C., Chiru A., Anisur Rahman S. | $30, $89.64, $7 |
| adjacent research with AI in the workflow | Muhammad A. | $60 |

Eight of ten are annotation, localisation or manual QA. Only two evaluation profiles price like
engineering: Yu Fong C. at $30, whose copy is specific about measuring answer accuracy and building regression
checks, and Chiru A. at $89.64, who is a Claude Code and MCP specialist with evaluation as one skill among many.

There is a lesson in the two cheapest cards: Anisur Rahman S. lists AI Evaluation as his top skill and charges $7 with
$50K+ earned, and Chiru lists it fourth and charges $89.64. Same skill word. Different product around it.

### Integration: 10,001 pages of it, and the top of the range is agencies

The boolean query gave the cleanest cross-section, because it pulled the agent and RAG builders rather than the
automation shops:

| rate band | profiles on that page |
|---|---|
| $15 to $25 | Rajiv R. $15, Nishant B. $15.99, Dmytro K. $25, Maryna H. $25, Mona C. $25 |
| $26 to $45 | Yu Fong C. $30, Herman T. $30, Mudassir H. $33, Hamza A. $35, Dmitry B. $45 |
| $65 and above | Don D. $95 |
| elsewhere in the pastes | Elena R. $65, Guy P. $65, Orest A. $85, Ahmad A. $85.55 |

The five profiles at or above your $65 are the useful comparison, because those are your actual competitors at that
price, not the $15 band:

- **Don D., $95**, US, Top Rated, $20K+, 16 contracts, and a one-sentence offer: "Give me a task your team repeats
  every week and I'll build a Claude agent that does it."
- **Ahmad A., $85.55**, US, Top Rated, 100% JSS, Siemens and Bank of America background, Anthropic Academy
  certificates, a keyword block that runs to 200 words.
- **Orest A., $85**, US, Top Rated Plus, $3M+ earned, 700+ jobs, a former CIO as a reference, a team behind him.
- **Elena R., $65**, US, Top Rated Plus, HIPAA integrations, 20+ years, McKesson and AstraZeneca in the copy.
- **Guy P., $65**, US, Expert-Vetted, $3M+ earned, 225-person firm.

All five are US-based, all five have a badge, all five earn between $20K and $3M. That is the field at $65. It is not
a price band you enter with 2 jobs; it is a band you enter with a claim nobody else is making.

## 3. Two full profiles, read as benchmarks

### Eugene T., $60/hr, Serbia. The delivery org.

Top Rated Plus, Expert-Vetted, 100% JSS on 72 reviews, **253 jobs, 3,014 hours, $300K+ earned**, 19 pages of work
history, 21 portfolio items, a $60 per 30-minute consultation, an agency behind him, and a closing instruction that
is a sales process: "We start with a focused first milestone: a feasibility check, a working component or a pilot for
one workflow. Further stages are agreed separately, including integrations, evaluation, deployment."

What $60 buys from him is not code. It is a named first milestone, a delivery team, and 253 completed jobs. Your $65 is
one dollar above this. That is defensible only if the thing being compared is narrower and provable, never as "AI
engineer".

### Kunal N., $20/hr, India. The closest analogue to you.

Top Rated, 100% JSS on 4 reviews, 7 jobs, 95 hours, $2K+ earned, 11+ years claimed, an agency, and this in his
portfolio: **"LLM Security Assessment & OWASP Top 10 for LLM Applications."** Certifications: CRTOM and CEH Master.
Billings visible in his history: $660 for 33 hours, $799 for 47 hours, $200 fixed for a "Pen Test Report".

Two things to take from him. First, the AI-security portfolio item is already being used as a differentiator by
someone with a low-volume account, so it is not by itself rare. Second, the price for that combination at 7 jobs is
$20, and the artefacts a buyer can see are a report, a retest and a certificate. Yours would be a pack with hashes and
a rerun. That is the difference worth charging for, and it is the only one on this page.

## 4. What this changes

### The title

The 09:12 WAT brief of 15 November said put "Full-Stack" back. These pastes invert that, and I would rather say so than let the
two files disagree. In a 10,001-page field of full-stack AI engineers, the word distinguishes nobody: it is on
half the cards at $10 to $25. Thin words on that page are the ones you own: red teaming, LLM security,
evals, verifiers.

So the title I would argue for now is the narrow one, and it should name the deliverable rather than the discipline:
something in the shape of `AI Red Teaming & LLM Evals | Rerunnable Test Suites`. Keep "Full-Stack" in the skills and in
the overview, where it answers a search without occupying the headline. That advice was written before this
page existed; this supersedes it, and the live-profile file needs the same correction.

### The price

Do not sell $65 hours into that field. Sell a fixed first milestone, the way Eugene sells one, priced from the
deliverable:

| package | what the client gets | price |
|---|---|---|
| Named-failure review | one system, up to 8 named failures with reproduction, a rerun script, and a written verdict on each | $1,200 |
| Eval suite build | a fixed test set with a written pass definition, a judge, and a rerun on demand | $1,800 |
| Regression pack | the above plus a second model or prompt version compared against the first | $2,600 |

Three of the middle package is $5,400. That is the target cleared with three engagements instead of 77 hours at $65,
and it is the shape the OpenAI and Upwork figures support: bigger scope is where the money moved, not the hourly rate.

### Three gaps between your card and the cards that win here

| gap | what the winning cards do | what your card does |
|---|---|---|
| No portfolio artefact a buyer can open | Kunal shows an LLM security assessment in his portfolio at $20; Eugene shows 21 items at $60 | the HFB pack, which no one else on this page can match, is not published as a portfolio item. Publish it with the zip hash and the rerun instruction |
| No paid consultation | Eugene, Carmen, Don, Dmitry, Monica and most of the credible cards offer one | nothing on the card, so the cheapest conversion path on the platform is closed before anyone clicks |
| Hours and video are empty | availability is filled and a video sits on the card | both are unset, and the title still carries a word that no longer earns its place. One edit and one afternoon, in that order |

## 4a. Amended at 10:44 WAT, after the job feed

The job feed was readable without a login, so the demand side got measured. Two changes follow, and both are recorded
in `UPWORK/2026-11-15_job-feed-corpus_seventeen-posts.md`.

Evals come out of the lead. The $50 to $100 evaluation engineering work is US-resident only, the fixed $10,000 role
says "US based" in its title, and the trainer market requires a US time zone. What is left open to Lagos is the $5 to
$30 benchmark-authoring mill. Evals stay in the offer as the second half of a security review, which is where the feed
puts them anyway: twice as a bullet inside .NET jobs.

The title should say **AI Security**, not red teaming. `AI red team` returns no public postings and `red teaming`
returns sixteen results that are a Red Hat ad and a coating chemist. `AI security` returns 174. Keep the rerun and the
retest in the subtitle, since two buyers asked for the retest before anyone asked for anything else.

## 5. What is still unproven

These are supply-side screenshots. They do not show what clients post, how many proposals a post attracts, or what
anyone was actually paid. Mark P., at $150 with $0 earned, is the reminder that a rate is a wish until a contract
exists. This recommendation rests on the shape of the supply and on your artifact, not on a demand measurement I
have not made.

## 6. Four searches worth running next

Talent search is not built for precision here, so use it only for profile shape, and stop reading the page count.
For demand, use the job feed, where each post carries a proposal count and a client history:

| purpose | where | term | what to record |
|---|---|---|---|
| demand for red teaming | job search | `AI red team`, `LLM red team`, `prompt injection` | proposals, budget range, client spend, hire rate |
| demand for evals | job search | `AI model evaluation`, `eval`, `benchmark` | same, plus whether it is annotation or engineering |
| demand for integration | job search | `MCP server`, `Claude Code`, `RAG pipeline` | same, plus stack |
| supply shape only | talent search | `"red teaming"` in quotes, sorted by earned amount | first page composition, not the count |

Four job searches with proposal counts would settle the lane question better than forty talent searches, because the
job feed is where the money is visible and the talent feed is where the ads are.
