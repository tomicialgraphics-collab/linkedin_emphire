# Comment round, 3 November: feed triage

The feed ran to roughly sixty posts. Three are worth a comment, two are worth an application, the rest
are noise, out of lane, or already engaged.

## Three comments, in priority order

### 1. Neil Sahota, "governing AI by autopsy"

In-lane and close to the thesis. He argues the threshold for an AI incident should not be damage but
consequential capability. The comment agrees with the threshold and then names what makes it operable,
which is that a capability nobody knew about leaves no artifact unless the record was built first.

> The threshold is right, and the hard part is that consequential capability is invisible by default.
> Nothing broke, so nothing generated an incident record, and the only artifact is whatever the system
> around the model happened to log before anyone thought to ask.
>
> That is the argument for recording what the model read, not only what it did. A capability nobody knew
> it had is precisely the thing that cannot be reconstructed after the fact, because nobody knew to look.
>
> Governing by capability means building the record before there is a question to answer with it.

96 words, lint clean. No claim of my own about the OpenAI wiki story, since it is his account and the
comment does not need it.

### 2. Hamel Husain, on Vik Paruchuri's benchmark findings

Lands directly on today's post about denominators and on the twelve-day run's fourth theme. He lists
scorer and specification defects across OCR benchmarks. The comment reframes them as benchmark defects
rather than model defects, and asks for the artifact almost nobody publishes.

> Almost nothing in that list is a model problem. A wrong expected value, an unstated formatting
> requirement, a postprocessor worth more than the gaps between the models it ranks, a correct answer
> penalised for following the document.
>
> Those are defects in the benchmark, and they are invisible from the score, because the score is what
> the defect produces.
>
> The artifact I would ask any benchmark for is the one almost none of them publish: its own defect
> register, with the failing example and the date it was found. A published scorer plus a short list of
> known failures catches most of this before a leaderboard has to.

107 words, lint clean. This is the post 21 argument, applied to someone else's evidence, which is why it
belongs in the run rather than against it.

### 3. Rock Lambros, OWASP ACS and the Guardian

He says the quiet part himself: no one verifies a self-declared conformance claim. The comment takes that
sentence as the adoption question and adds the one distinction he has not drawn, which is that a log
produced by the thing being assessed is not independent evidence.

> No one verifies a self-declared conformance claim is the sentence that decides whether ACS travels
> outside the room it was written in. A Guardian that logs an audit trail is necessary and not
> sufficient, because the log is produced by the thing being assessed.
>
> The version that settles it is the one a buyer can run without you: a reference implementation, a fixed
> test set, and a failure that produces a document rather than a support ticket.
>
> Publishing the Guardian limitations requirement by requirement is the part most standards skip, and it
> is the part a buyer will actually read.

100 words, lint clean. He is a repeat surface (he liked the [un]prompted comment), so this is a warm
thread, not a cold one.

## Two applications, not comments

- **Gates Foundation AI Fellows, Africa Regional Offices.** Twelve months, full time, early-career AI
  professionals, embedding into health and development work across Sub-Saharan Africa. This is the
  closest match to his position and location that has appeared all month, and the deadline is not stated
  in the post. Check the link today.
- **NVIDIA, AI and security researcher roles (Leon Derczynski).** US-based including Santa Clara, or
  elsewhere. Worth reading the posting for a remote option before investing time.

Also noted, lower priority: **adaption modelling residency** with Sara Hooker and Simra Shahid, interface
research rather than evaluation, and **Chinasa Okolo** at the World Bank webinar today, 9 to 10 AM ET,
which is 3 to 4 PM Lagos, on AI readiness and the Africa Economic Update. Attend if the afternoon is
free, because it is the policy side of the same argument.

## Skipped, and why

- **Brad Wolfe**, five posts: all finance-transformation angles already worked in previous entries. The
  "nobody removes a control, they calibrate it" one is the only new shape and it would be the fourth
  comment in that thread family this month.
- **Iris Otano**: already commented, 103 reactions, do not return.
- **Rock Lambros' second post** (the [un]prompted II verdict): one comment per person per day.
- **NahamCon, Prompt2Pwn**: event promotion, nothing to add.
- **Bolaji Adebayo, Blossom Affia, Rita Olapade, Oni Funmilayo**: Nigerian creator and job-hunt content,
  not the audience, and commenting there pulls the feed in the wrong direction.
- **Ivan Lee, Endrit Restelica, Alex Banks**: news aggregation and compute-finance commentary, out of
  lane.
- **Iyinoluwa Aboyeji**: worth a follow, not a comment. He is now the source of the Gates fellowship lead.

## Do not

- Do not comment on more than two of these today. Three comments on three different posts in one
  afternoon is the signature of someone working a list.
- Do not mention the benchmark, the review, or the Aithos application in any of them.
- Do not reply to agreement. If Neil or Rock answers with thanks, the thread is finished.

## Status: all three posted, plus three more

All six of the 3 November comments shipped the same afternoon. Verbatim record in
`ENGAGEMENT/published_comments/2026-11-03_verbatim.md`.

## Profiles checked before pasting

- **Neil Sahota.** IBM Master Inventor, former World Wide Business Development Leader for the IBM
  Watson Group, UN AI Advisor, co-founder of the UN AI for Good initiative, Chief Innovation Officer at
  UC Irvine's Samueli School of Engineering, CEO of ACSILabs, author of *Own the A.I. Revolution*. He
  writes for boards and executive committees, so the comment stays concrete and avoids method jargon.
  Do not cite the OpenAI wiki story back at him. It is his account and the comment does not need it.
- **Hamel Husain.** Independent consultant, founder of Parlance Labs, formerly staff ML engineer at
  GitHub and Airbnb, CodeSearchNet before Copilot, co-author of *Evals for AI Engineers*, the person who
  has taught several thousand engineers error analysis. The defect-register ask is in his own register,
  and he is likely to answer it, so be ready to name a failure from the review if he asks for one.
- **Rock Lambros.** Director of AI Standards and Governance at Zenity, OWASP Agentic Security Initiative
  core team, co-lead of the OWASP Top 10 for LLMs and lead of the ACS project, Denver, roughly 24k
  followers. He wrote the standard the comment is about, and his employer sells runtime monitoring for
  agents, which is the independent observer the comment asks for. It reads as agreement with him, not as
  a criticism of Zenity, but read it once more with that in mind before posting.

Paste-ready copies, plain text, no quoting: `ENGAGEMENT/2026-11-03_comments/01_neil_sahota.txt`,
`02_hamel_husain.txt`, `03_rock_lambros.txt`.
