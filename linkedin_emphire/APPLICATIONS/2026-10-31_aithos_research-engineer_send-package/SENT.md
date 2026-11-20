# Send log: Aithos Research Engineer application

Record of what actually went out. This file is the source of truth for any follow-up,
and it stops a future session from rebuilding or re-sending the package.

**Corrected 2026-11-14 23:15 WAT.** The previous version of this file said the
application was sent on 31 October. The thread itself says **14 October**, and it
carries an acknowledgement the tracker recorded as never having arrived. The
sent text is now pasted below, as this file always asked for.

## Sent

| Field | Value |
|---|---|
| Date | **14 Oct 2026**, 09:06 WAT |
| Channel | Email to the role address, not the lnkd.in form |
| To | hiring@aithos.org |
| From | olusanyatimothy54@gmail.com |
| Subject | Application, Research Engineer, Olusanya Timothy |
| Body | the verbatim text at the bottom of this file, not `letter.txt` |
| Attachment | `Olusanya-Timothy-Aithos-Research-Engineer.pdf`, 73,004 B, `6c3b5e38624d` |

The PDF that went out is **not** the file in `RESUME/`. That copy is a different
build at 29,814 B, `1bc812d1de8b`. Anything re-sent from this repo rebuilds the
wrong document; use the sent file.

## Variations actually used

- [x] The body differs from `letter.txt`; the sent text is pasted below and is the record
- [ ] Kept the optional LARA sentence; LARA is not mentioned in the sent text
- [x] "I have not used Inspect yet" was kept, and it is now stale
- [ ] No DOCX, one PDF only
- [x] The five-test harness was the link cited, not the 168-class Playbook

## Reply tracker

| Event | Date | Notes |
|---|---|---|
| Application sent | 14 Oct 2026, 09:06 | to hiring@aithos.org |
| Auto-acknowledgement received | 15 Oct 2026, 12:08 | **human**, from Sicco Pier van Gosliga, sicco@aithos.org |
| Owner replied | 16 Oct 2026, 04:51 | thanks, offers anything useful, no ask |
| Human reply | 15 Oct 2026, 12:08 | confirms CV and letter received; review in the first week of November; they will reach out with next steps |
| Screen call proposed | — | |
| Screen call held | — | |
| Take-home sent to them | — | |
| Take-home returned | — | |
| Technical round | — | |
| Outcome | — | nothing since 16 Oct |

## Where it stands, 2026-11-14

- The review they promised for the **first week of November** (2 to 8 November) ended
  four working days ago. No next-step message has arrived.
- The vacancy page `aithos.org/vacancies/research-engineer/` now reads
  "Open Vacancy: Research Engineer (closed)", with the application line struck
  through. That is a closed intake, not a stated decision on the applications already
  in the pile. Nothing on the page says the role is filled.
- `hiring@aithos.org` reached the team. The earlier worry that it was an unmonitored
  address was wrong; a named person answered from it inside a day.

## Follow-up rule

**One bump only**, sent as a reply in the existing thread to `sicco@aithos.org`,
addressed by name, quoting his own commitment rather than counting days. Draft and
reasoning: `APPLICATIONS/2026-11-14_aithos-status-bump/EMAIL.md`, PASS 0/0, unapproved,
owner sends.

If there is no answer by **21 November**, the round is over. The next contact is a fresh
application when the next research engineer role opens, not another message in this
thread.

## What happens if they say yes

`context.md` section 9 has the flow: 30-minute screen, then a roughly 3-hour take-home
on a real Aithos evaluation, then a 60-minute technical with the Technical Lead,
preferably in person in Amsterdam. The screen is the next thing to prepare for, and
`PROJECTS/2026-11-01_aithos-interview-prep/` already holds the prep.

## The text that was actually sent, verbatim

> To the Aithos team,
>
> I am applying for the Research Engineer role because it is the closest match to what I actually build. I work on AI safety from the build-and-test side: I design and run evaluations that check whether an AI system does what it should under the conditions a real user or a regulator would test, and I build the code so those checks are reproducible, public, and rerunnable by anyone who wants to question them.
>
> The most direct proof is a five-test red-team harness I published (github.com/Teamthy/ai-redteam-five-tests). It runs prompt injection, retrieval poisoning, tool description poisoning, and multilingual refusal tests against any OpenAI-compatible model, resolves tool calls, records the raw responses, and reports each failure with its sample size and rate. It is written to the standard the role asks for: clean, tested, documented Python that others can build on, not a one-off script. Every result traces back to a specific prompt, model, and commit, which is the part I care about most. I would not report a number I could not reproduce.
>
> That reproducibility mindset is why Aithos stands out to me. Turning every piece of research into a benchmark, open tooling, or reproducible methodology, and making work that regulators and other teams can actually use, is the same standard I hold my own work to. It is also the standard your principles describe: the values a model encodes should stay open and contestable rather than converge on one ideal, and a result is only as strong as the method that produced it. That is why I publish the harness and make every run rerunnable, so a finding can be questioned, not just trusted. My public series, Breaking AI, applies it to the question I started from: shipping AI that survives real users. The failures I write about are the boring ones (the prompt is not a wall, retrieved documents are untrusted input, tool descriptions are trusted unread, test sets that only cover one language), and the controls I recommend are engineering controls, not slogans.
>
> A few things I want to be straight about. I am a self-taught practitioner, not a formal ML researcher, so I have no peer-reviewed papers. I have published a public, reproducible body of work instead, and I build with the discipline the role describes: safe sandboxes for code-running agents, careful handling of credentials, and a habit of checking AI coding output rather than trusting it. I have done tool-calling and agentic scaffolding but less formal multi-agent simulation, and I have not used Inspect yet; both are quick for me to pick up given the evaluation work I already do. I am based in Lagos (UTC+1), so my hours line up with Amsterdam, and I can work remotely; I am open to discussing the in-person days.
>
> I would welcome the screening call, and honestly the three-hour take-home on a real Aithos evaluation is the part I would most like to do.
>
> Olusanya Timothy
> olusanyatimothy54@gmail.com · +234 812 786 8211 · linkedin.com/in/olusanya-timothy · github.com/Teamthy

## Their acknowledgement, 15 October, verbatim

> Thank you for applying for the Research Engineer position at Aithos Research Foundation. We have successfully received your CV and motivation letter. We appreciate the time and effort you put into your application. Our team will be reviewing all submissions during the first week of November. Once we have completed this review, we will reach out to you regarding the next steps in the process. Thank you for your patience and for your interest in our work.
