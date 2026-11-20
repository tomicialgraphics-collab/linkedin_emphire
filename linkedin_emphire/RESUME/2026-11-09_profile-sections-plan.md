---
deliverable: doc
id: 2026-11-09_profile-sections-plan
date: 2026-11-09
audience: owner
status: ready
approved: no
warm: no
thread: which remaining LinkedIn sections to add, in what order, with paste-ready text and an explicit list of the ones to skip
verified: every fact comes from the live site and CV read on 9 November, the 6 October resume audit, or the playbook repository. Project start dates are left as a slot because the honest source is the first commit, and the command to get it is included. Nothing here asserts a credential whose name or date is unknown.
---

# The other sections, in the order they are worth your time

Six are worth adding. Nine should stay empty, and one of those matters more than the rest.

The rule behind the order: a section earns its place if it either proves a claim the Experience section makes, or puts something checkable in front of a buyer. Anything that only repeats what is already there is clutter, and clutter on a profile with a strong headline reads as padding.

## 1. Projects. Add this before anything else

Projects is the section that lets the four harnesses exist as named artefacts without pretending they were employment. It sits below Experience, and it is where somebody who clicked the website goes to confirm the tools are real.

Add five, in this order. LinkedIn shows the first ones first.

**tieout**
```
URL: https://github.com/Teamthy/Tie-out-
Dates: [month and year of the first commit]
```
An evaluation harness that emits evidence instead of a report. Every verdict is one bound, chained, re-derivable event: the action, the check version, the decision and the effect reference in a single record, with raw inputs and outputs stored beside it. The demo re-derives 14 of 14 verdicts from stored raw output, with 0 false positives and 0 false negatives across 8 negative controls, and reports Clopper-Pearson intervals instead of bare percentages. Python, MIT, no key and no network needed to verify.

**AI Red Team Playbook**
```
URL: https://github.com/Teamthy/Ai-Red-Team-Playbook
Dates: [month and year of the first commit]
```
168 testable classes for AI red teaming across model behaviour, retrieval, agents, output handling, measurement and governance, with four dependency-free tools behind them: one refuses a skipped class without a written reason, one puts a Wilson interval on every attack success rate, and one prints the coverage page. The example engagement records 23 classes tested, 2 absent, 1 skipped and 142 open, so the denominator is stated rather than implied. Written under CC BY, code under MIT.

**gatecheck**
```
URL: https://github.com/Teamthy/gatecheck
Dates: [month and year of the first commit]
```
A CI gate that answers one question: did this agent get easier to break? Findings are fingerprinted, diffed against a committed baseline, and only new or worsened issues fail a pull request. 11 attacks become 7 findings in under a second, reported as SARIF on the PR. Built as a GitHub Action because a security gate that cries wolf gets switched off by the third pull request.

**host-failure-benchmark**
```
URL: https://github.com/Teamthy/host-failure-benchmark
Dates: [month and year of the first commit]
```
A standard-library benchmark for crash consistency in agent audit trails: 4 failure rows, 13 persistence and recovery checks, 3 verification checks and 10 ways to damage a run. The output is a named gap, including the case where the benchmark itself cannot tell that an action happened. No dependencies, so the result is reproducible on any machine that runs Python.

**Famex OS**
```
URL: https://github.com/Teamthy/Famex-OS
Dates: [month and year of the first commit]
```
A school operating system in production: 140+ API routes, 70 models and 898 tests. Fees are double-entry in signed kobo, an unbalanced journal is rejected by the database rather than by application code, and row-level security has its own CI coverage guard. This is the entry that proves the Go and PostgreSQL claims on a profile that otherwise talks about evaluation.

**Get the dates from the work, not from memory.** In each repository:

```
git log --reverse --format='%ad' --date=format:'%b %Y' | head -1
```

A date that matches the first commit is one you can defend if somebody asks.

## 2. Publications. Three entries, from work you already published

LinkedIn allows an article, a book or a paper, and a technical post with a date and a link qualifies. Publisher: `olusanyatimothy.vercel.app`. Type: Article.

| Title | Date | URL |
|---|---|---|
| The five boring failures that will ship with your AI feature | November 2026 | `https://olusanyatimothy.vercel.app/blog/five-boring-failures` |
| Your eval passed. What exactly did it prove? | November 2026 | `https://olusanyatimothy.vercel.app/blog/your-eval-passed-what-did-it-prove` |
| A red-team gate that only blocks when you get worse | October 2026 | `https://olusanyatimothy.vercel.app/blog/a-gate-that-only-blocks-on-regression` |

Your CV also lists **What survives when the host dies**, October 2026. Copy its URL from `/blogs` and add it as a fourth.

Description, for the first one, and cut to suit the others:

```
Not a jailbreak from a film. A refusal that only works in English, a poisoned document, a tool description nobody read, and a metric with no sample size. Each failure has a runnable test, and refusals are checked in English, Nigerian Pidgin and Yoruba.
```

## 3. Licenses and certifications

One entry, if the certificate exists and you can name it exactly:

- **NIST AI Bootcamp.** Use the exact name printed on the certificate, the issuing body, the month and year, and the credential URL if one was issued. If there is no certificate and it was training without one, leave this section empty rather than listing it, because a certification is the one field a recruiter can check in ten seconds.

## 4. Services

This is the section most people in your position skip and should not. It puts you in LinkedIn's services marketplace, adds a "Providing services" block near the top of the profile, and lets a buyer contact you without a connection request.

Set your location as Lagos, Nigeria, remote, and choose the categories closest to these. The exact list depends on what the autocomplete offers; tell me what appears if none of them fit:

- Artificial intelligence consulting
- Software development
- IT consulting and technical review

Service description, keep it to two lines:

```
AI red teaming and evaluation for teams already shipping: adversarial testing that produces evidence instead of a findings list, with sample sizes, intervals and named gaps. Also Go and TypeScript platform work.
```

## 5. Languages

You test refusals in Yoruba and Nigerian Pidgin, which is a real and unusual detail. Put it where it is visible.

- English, Native or bilingual
- Yoruba, Native or bilingual
- Nigerian Pidgin, if the list offers it, Native

## 6. Recommendations

Three requests, and the ask matters more than the section. A recommendation request that says "would you write me one" gets ignored. One that says what to write gets answered.

Send this, edited per person:

```
I'm tightening my profile around AI red teaming and evaluation work. If you have two minutes, a short recommendation would help a lot, and it does not need to be long.

Three sentences is plenty: what we worked on together, one thing you saw me do, and one result you remember. If it helps, I can draft something for you to edit or throw away.
```

Ask three people: whoever received the delivery where the system held under review, whoever saw the red-team work, and whoever managed you on a platform build. The offer to draft it is what gets replies, because you are removing the work rather than asking for it.

## The nine to leave empty

| Section | Why not |
|---|---|
| **Honors and awards** | Only if an award exists with a name and a year. An empty claim here is worse than an absent section |
| **Patents** | Nothing to list |
| **Courses** | A course list signals a beginner. Your four repositories are the equivalent, and they are stronger |
| **Test scores** | Belongs on a graduate CV |
| **Organizations** | Membership with no role is filler |
| **Causes** | Invites a reader to judge your politics for no gain |
| **Volunteer experience** | Only if the work is relevant to the positioning |
| **Connected app** | No benefit, and it grants a third-party app access to your account |
| **Career break** | Do not create one. It exists to explain a gap, and you do not have one to explain |

## Two profile settings worth ten minutes

**Open to work.** Set it to recruiters only, not the green frame. The frame contradicts a profile that is selling audits, and every recruiter who matters can see the setting either way.

**Education.** If it is missing, add it with the degree, the institution and the dates, and mark it in progress if that is the truth. Then make it match the CV, because an expected graduation date that differs by a year between the two documents is the kind of thing a screener notices.

## Order of work

1. Projects, five entries. Highest return, and it is the section that makes the website's claims checkable.
2. Education and Languages, ten minutes together.
3. Services.
4. Publications.
5. Recommendations, because the replies take days and the ask takes a minute.
