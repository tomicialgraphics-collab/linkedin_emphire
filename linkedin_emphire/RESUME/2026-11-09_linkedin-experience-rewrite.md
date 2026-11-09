---
deliverable: doc
id: 2026-11-09_linkedin-experience-rewrite
date: 2026-11-09
audience: owner
status: ready
approved: no
warm: no
thread: rewrite of the LinkedIn Experience section so it supports the AI red teaming positioning instead of contradicting it
verified: every fact here comes from the CV audit of 6 October or from the profile screenshot. Numbers that belong to the owner are left as bracketed slots rather than guessed. Where the CV and the profile disagree, the disagreement is named rather than resolved.
---

# LinkedIn Experience, rewritten

## What a recruiter sees in the first eight seconds

Four entries, two of them with no description at all, and a headline that says AI red teaming while the section says computer vision, creative direction and data contracts. The section does not contradict the headline by being wrong. It contradicts it by being quiet about the thing the headline promises.

Three specific problems, in order of cost:

1. **The dates overlap in a way that raises a question nobody wants to ask.** OpenCV is listed as full-time from March 2024 to November 2025, while Corewell runs to July 2025, Idaho sits inside that window, and Teamart starts in May 2025. That reads as three concurrent engagements under one full-time label. It may all be true, and it still needs the labels to say so.
2. **Two entries have no description.** Creative Director and Senior Data Specialist are titles with nothing under them. A blank description is read as filler, and it costs eight seconds to fix.
3. **The strongest evidence is absent.** The playbook, the Breaking AI series and the chatbot test are the only things here that a client cannot get from a hundred other profiles. None of them appear.

## Three questions only you can answer

Answer these before pasting anything. I can write around the rest, not around these.

1. **Which role was actually full-time during 2024 and 2025?** If OpenCV was full-time, then Corewell, Idaho and the start of Teamart were concurrent contract work and the employment type on each must say Contract or Part-time. If Teamart was the main thing from May 2025, then OpenCV should end earlier or be marked contract.
2. **What was Corewell Health, in one sentence?** If it was brand and creative direction on contract, keep it with that label and one line. If the title overstates what it was, delete it: an unexplained Creative Director role in a US health system invites a question you will have to answer on a call, and it buys nothing on an AI security profile.
3. **Does YKAY ConsultingHub belong on this profile?** Your CV has it, November 2024 to June 2025, and LinkedIn has no trace of it. Recruiters cross-check the two documents, so one of them is currently lying by omission. Pick one story and put it in both places.

Recommended shape, assuming OpenCV was full-time: OpenCV stays full-time and gets the most detail, Idaho is relabelled Contract with one line, Corewell is relabelled Contract and either gets one line or goes, Teamart becomes the present independent practice and carries the AI work.

## 1. Software Engineer, Teamart.inc. May 2025 to present

This is the entry that has to carry the positioning. Title suggestion: **Software Engineer, AI Red Teaming**. Keeping the title short helps the search match, and it stops the section from reading as generic.

Description, paste as is:

```
Independent engineering practice. I build AI systems, then attack them on purpose before anyone else does.

What I do: LLM integrations (chatbots, retrieval, tool calling), pre-launch red teaming against them, and the evaluation work that decides whether a fix actually holds.

Recent work:
- Author of the AI Red Team Playbook: 168 testable classes across model behaviour, retrieval, agents, output handling, measurement and governance. Public, with tooling that puts an interval on every attack success rate and a coverage argument that names the classes nobody tested. github.com/Teamthy/Ai-Red-Team-Playbook
- Breaking AI, a public series on reproducible failure modes in shipped AI features.
- Built a customer support chatbot, then ran six prompt injection tests before launch. Four broke it: a system prompt leak, an unauthorised refund commitment, and a content policy bypass. Each finding went back to the build with a test attached, and the set became a repeatable checklist.

Stack: Python, Go, TypeScript, LLM APIs, retrieval, PostgreSQL.
```

Two notes on that text. The chatbot sentence is from your own record, and it is the single most credible line available to you, so make sure the four results are the ones you would stand behind if a client asked you to rerun them. And the playbook link earns its place because it is public and checkable, which no adjective on this list is.

## 2. Computer Vision Engineer, OpenCV. March 2024 to November 2025

Nobody doubts that this is engineering. The problem is that it says nothing about what you did. Three lines, in this order, is enough: what the component was, what you changed, and what it moved.

```
Contributed to [component or module] in the OpenCV ecosystem, working on [what it does] for [who uses it].

Built [specific thing], which [effect: speed, accuracy, coverage, fewer failures]. [One number if you have one: latency, throughput, models shipped, users].

Worked in C++ and Python against a widely used open source codebase, including [review, tests, release work, documentation] alongside [team size] engineers.
```

Fill the slots with what actually happened. Where you have no number, describe the effect in a comparison instead ("cut the time to process a batch from minutes to seconds"), which is honest and still reads as an outcome.

## 3. Creative Director, Corewell Health. February 2023 to July 2025

Pick one of two:

**Keep it**, relabelled Contract or Part-time, with this:

```
Brand and creative direction for [programme or product], delivered remote for a US health system.

Produced [what shipped: campaigns, a design system, product launch material] for [audience], and ran the review process with [clinical, marketing, compliance] stakeholders.

The useful part for engineering work: getting a decision through a regulated organisation, where the constraint is rarely the idea and almost always the approval path.
```

**Or delete it.** If the title overstates the work, this entry costs you more in credibility on first read than it returns, and the three engineering entries are stronger without a question mark next to them.

## 4. Senior Data Specialist, University of Idaho. October 2024 to March 2025

Relabel Contract if it was not full-time. One line under the title:

```
Contract data work for [department or lab]: cleaned and modelled [what dataset] to support [what decision or publication].

Delivered [output: a dataset, a pipeline, a report] against a [deadline or scope] set by [who].
```

## Skills to pin

The three pinned skills show on the profile card, so they should repeat the headline rather than the oldest work. Candidates, and check each against the autocomplete before adding: `Large Language Models (LLM)`, `AI Security`, `Threat Modeling`, `Python`, `Penetration Testing`.

Pin three: one AI, one security, one language. Move Computer Vision and Deep Learning further down. They are true, they are just not the first thing a buyer should read.

## After the rewrite

- **Featured**: the launch post, then the repository link, then the Breaking AI series. Three items, in that order. The first thing on the card should be the thing that is checkable.
- **About section**: the first two lines should say what you do and for whom, in the same words as the headline, because that is what the search ranks on.
- **Consistency pass**: dates in the CV and the profile must be identical. Right now Teamart starts in May 2025 on one and July 2025 on the other, and YKAY appears in one and not the other.

## If someone asks about the overlap

Two sentences, true and short, better than a defensive paragraph:

> OpenCV was my full-time role. The university and the health system work were short remote contracts I took alongside it, and Teamart began as an independent practice before that role ended. The labels on the profile should say so, and I will fix them.

That answer is only available to you if the labels are fixed first. Do that before the next application, not after.
