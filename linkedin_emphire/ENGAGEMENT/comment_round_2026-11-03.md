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

## Seventh comment: Martin Šafránek, 3 November, evening

A quote post of Zach Wilson's Snowflake and Databricks "souls" satire. Martin's own paragraph is the
commentable part: the events feel different, migrations are a culture upgrade as much as a technical one,
run several POCs with both platforms, listen to users and business representatives first.

**Profile read.** Prague. Roughly twenty years of DWH and migration work. Head of DWH at Czech Airlines
and J&T, delivery projects at Javlin (now CloverDX), and the last six years on Czech National Bank
regulatory reporting, Anacredit and Resolution Reporting, plus migrations for acquired banks. SnowPro Core
since August 2024, Data Vault 2.1 practitioner since March 2025, Datavault Builder certified since
September 2025. At Ness Czech, contact address on the Sophia Solutions domain. Co-hosts Data Vault bez
předsudků on the Data Talk podcast and runs AI prototyping for a public education nonprofit. Writes method
and practice, not announcements, so the comment goes at the failure side of a POC and stays off his
employer and off the podcast.

**Deliberately absent.** Zach Wilson's satire is the parent post. Replying to it would be arguing with a
joke, and Martin's paragraph is where the substance sits. No mention of the benchmark or the review. No
Data Vault citation, because he holds three certifications in it and does not need one explained.

Draft, 96 words, lint clean, gate 100: `2026-11-03_comments/07_martin_safranek.txt`.

## Eighth comment: Kyle Bartlett, 3 November, late evening

His `connect-ready` gate rejected one of his own drafts for repeating a closing line sent to someone else
earlier that day. He runs twenty-odd agents on Claude Code. He ends by asking what other people's checks
compare against.

**Profile read.** Greater Houston, runs Bartlett Labs, Purdue, former US AI Lead at Anker, ex-Apple,
first-degree connection. Headline is AI Architect and Forward Deployed Engineer, building production agent
systems for enterprise ops, with evals and governance in the description. He is asking a real question,
not performing one, so the comment answers it directly and hands back a failure he will recognise.

**Angle.** The question assumes the comparison set is trustworthy. In the work here it usually is not: when
the record of what already went out fails to write, the cross-piece check compares against nothing and
returns clean. So the check that matters is not only whether the draft passes, but whether the log grew.
That is his finding one layer down, and it is the honest limit of this side's tooling rather than a boast
about it.

**Deliberately absent.** No mention of the benchmark, the review, or the Aithos application. No pitch. He
is first degree and worth a DM later, but the comment should be the whole contact for now. There is also a
Udemy course with an almost identical title in the search results, whose instructor describes a JPMorgan
and untapt history that does not match this profile, so nothing in the comment references a course.

Draft, 104 words, lint clean, gate 100: `2026-11-03_comments/08_kyle_bartlett.txt`.

## Ninth comment: Ethan Mollick, 3 November, night

He suggests proving to yourself that a current model gives substantive, intellectually interesting feedback
on your own paper, and notes the improvement is that critiques now read like a good, slightly eccentric peer
rather than a list of nitpicks.

**Profile read.** Wharton associate professor of management, co-director of the Wharton Generative AI Labs
with Lilach Mollick, author of *Co-Intelligence* (2024) and *Co-Existence: The Next Phase of AI*, published
20 October 2026 by Penguin, writes One Useful Thing, TIME 100 in AI for 2024. He is a careful, evidence-led
writer who has been publicly sceptical of both hype and dismissal. Nothing here needs telling to him, and
nothing should sound like a correction of him.

**Angle.** Take his "prove it to yourself" one step further without contradicting it: a substantive critique
is persuasive before it is checked, and the eccentric-sounding ones are where that gets tested. Anchoring
each objection to a line and a document version makes the claim checkable against the text rather than
against memory. The parting observation, that the objections which fail to survive checking are usually the
ones that sounded sharpest, is the honest version of the phenomenon he describes.

**Deliberately absent.** No opinion on the specific models he names, because capabilities in that post are
his observation and cannot be verified from here. No mention of the benchmark, the review or the manuscript
work. No compliment on the book.

Draft, 98 words, lint clean, gate 100: `2026-11-03_comments/09_ethan_mollick.txt`.

## Tenth comment: Jeff Cohen, 3 November, late night

Fiddler AI's acquisition by CrowdStrike, announced the same day at Fal.Con Europe in Barcelona. Jeff's post
is a career account that contains one sentence worth answering: manual evaluation of their own agents was
one of the things that broke Leadoff operationally, and they never solved it.

**Profile read.** Building trust into AI at Fiddler, previously a long run at UserTesting through its IPO,
acquisition and merger with UserZoom, UCLA Anderson MBA, co-founded Leadoff and shut it down after about two
and a half years. Sales operator turned founder, writing to a vendor and enterprise audience on the day of
the announcement. He is not asking a question, so the comment answers the sentence rather than the news.

**News checked.** CrowdStrike press release, 3 November 2026, definitive agreement, closing expected in
FY27 Q4, Fiddler to be sold as Falcon Observe with GA planned in the same quarter. Reported at roughly 400
million for Fiddler and 95 million for Dreadnode in the same announcement. None of that goes in the comment.

**Angle.** Manual eval fails on artifacts, not speed: a spreadsheet verdict cannot tell you later whether
the agent moved or the reviewer did, and a guardrail exporting pass and fail keeps that blindness while
cutting the latency. The closing line answers George Kurtz's "the model did it is not an answer" without
quoting it back at him, because "the reviewer said so" fails the same way.

**Deliberately absent.** No congratulations paragraph. He has a hundred of those already today and the
comment would be invisible in them. No mention of the benchmark, the review, or Aithos, since this thread
is a vendor and enterprise audience on an acquisition day.

Draft, 110 words, lint clean, gate 100: `2026-11-03_comments/10_jeff_cohen.txt`.

## Eleventh comment: Vivian Fu, 3 November, night

She names four AI governance gaps in Australia and ends by asking which ones people meet most often, and
where the opportunities are. A direct question from someone who writes in this area weekly.

**Profile read.** Sydney. AI governance and assurance, currently building an AI Assurance Evidence and
Decision Chain model: an evidence chain for what was known and done, a decision chain for who decided and
who owns the residual risk. Her repeated line is that governance tells you what should be true and assurance
tells you whether it is true enough to proceed. Around five thousand followers. She has publicly offered
three teams a free independent AI risk and safeguards review of one working product or pilot, and the
questions she lists in that offer are control verification questions, not policy questions.

**Angle.** Answer her question with the one failure this side knows best: control verification collapsing at
the evidence step, where a check reports pass because it never ran and a dashboard cannot tell that apart
from a clean result. The opportunity to rank first follows from her own model, quietly: a control emits a
dated artifact at execution and something confirms the artifact exists before the pass counts. That is the
difference between an evidence chain and a folder of documents, and it is cheaper than a mapping layer.

**Deliberately absent.** No compliment on the framework, no mention of the benchmark, the review or Aithos,
and no reference to her free review offer in public. The offer is the reason to send a direct message if she
replies, not to pitch in a comment thread she is using to find out who does this work.

Draft, 118 words, lint clean, gate 100: `2026-11-03_comments/11_vivian_fu.txt`.

## Twelfth comment: Stephen Klein, 3 November, night

He pulls the media-coverage risk factor out of Anthropic's S-1 and argues the company cannot sell the
apocalypse and then complain that people are frightened.

**Profile read.** Founder of Curiouser.AI, Berkeley lecturer, advises AI companies on positioning and
visibility, keynote speaker, contributing editor. He sells positioning, which means he already knows a risk
factor section is a legal genre drafted by counsel. The post is a deliberate rhetorical move, not a
misreading, so a comment that explains boilerplate to him would be both pedantic and unwelcome.

**Claim checked.** Form S-1 filed 26 October 2026, ticker ANT, Nasdaq, 93 pages of risk factors from page 26
to page 119, against 37 for SpaceX and 40 for Microsoft. The quoted paragraph is verbatim in the filing, and
the "whether accurate or not" clause is really there. Treating the filing date as 26 October, not the AP
piece's 27th.

**Angle.** Agree, then strengthen the evidence and separate the two halves of it. The bulk of the section is
defensive drafting, which is why it is two and a half times SpaceX's. The paragraph he quotes is different:
it names the narratives the company expects to meet, then pre-emptively discounts their accuracy. That
sentence is what a company writes when it has decided an objection cannot be won on argument and will be
survived on reputation instead. Land it in his own language, positioning rather than policy, because that is
the trade he sells.

**Deliberately absent.** No mention of the Agentic Misalignment paper, since the argument does not need a
second contested fact, and no comment on whether the blackmail experiment was staged. No mention of the
benchmark, the review, or Aithos.

Draft, 121 words, lint clean, gate 100: `2026-11-03_comments/12_stephen_klein.txt`.

## Thirteenth comment: Al Neitsch, 3 November, late night

A governance checklist post: name the custodian, write the access policy, define the request process,
instrument for loss prevention, review the policies. It ends by asking how people prioritise governance in
product development.

**Profile read.** Founder and managing director of TNGC, a Delaware consulting firm running since 2008 with
Fortune 100 and government clients. Headline is data and AI engineering plus governance, and he also writes
and performs comedy and works as a journalist. First-degree connection. The list is the kind of advice an
advisor gives at the top of an engagement, so the comment is worth more if it names where that advice
decays than if it agrees with it.

**Angle.** Answer his question honestly: in small teams governance gets prioritised after an incident, and
the thing that changes that is making a policy into something the system can fail. An access rule becomes a
query that attempts the reads it should refuse, retention becomes a job that reports what it deleted.
Custodians matter, but a custodian without a test is a name on a page, and names get reassigned quietly when
someone changes roles. Dated output over a recurring meeting.

**Deliberately absent.** No mention of data loss prevention by name, because his list already covers it and
the point is about verification rather than tooling. No mention of the benchmark, the review, or Aithos. No
reference to his comedy, which would read as flattery in a governance thread.

Draft, 98 words, lint clean, gate 100: `2026-11-03_comments/13_al_neitsch.txt`.

## Fourteenth comment: Paolo Perrone, 3 November, late night

He summarises an Airbnb talk about a four-person team getting agentic coding to 64% of engineering in a
year: CLI over IDE, MCP over fine-tuning, parallel sessions over flow state, a thin wrapper over lock-in. He
ends by asking what stops teams from shipping this way.

**Profile read.** Writes The AI Engineer on Substack, covering agents, inference and GPU economics for a very
large engineering readership. His pieces explain mechanisms rather than announce products, and the inference
course is the closest thing in his catalogue to the current post. He has technical readers, so a comment
that argues about measurement will be understood at speed and judged by whether it is true.

**Angle.** Answer the question with the step after adoption. The 64% figure is a headcount, and it moves the
constraint to review. Five parallel sessions per power user turns the reviewer into the queue, and the honest
metric stops being pull requests opened and becomes pull requests that survived review unrewritten. Teams
can produce the first number on demand and cannot produce the second, because nothing records what happened
to a change after it merged. Close on why the wrong number is the one that gets quoted.

**Deliberately absent.** No link to the post on the merge rate, even though this is the same argument. In
someone else's thread a link reads as traffic, and the idea carries without it. Also no comment on the
Airbnb numbers themselves, which are his summary of a talk neither of us ran.

Draft, 102 words, lint clean, gate 100: `2026-11-03_comments/14_paolo_perrone.txt`.

## Fifteenth comment: Alex Mashrabov, 3 November, late night

A founder story. One book in the office when Higgsfield started in 2023, Ed Catmull's account of Pixar, ten
of sixteen million seed dollars burned in eighteen months, and a podcast conversation that turned into an
argument about AI video being judged by its jagged edges the way CG was in the 1970s.

**Profile read.** CEO and co-founder of Higgsfield AI, founded October 2023. Previously co-founded AI
Factory, acquired by Snap for 166 million in 2020, then head of generative AI at Snap until September 2023.
Two ICPC world finals. He is telling a founder-formation story to an audience that already knows his numbers,
so a comment that repeats them adds nothing and a comment that argues with the analogy would miss the point.

**Angle.** Take the sentence he quotes from Catmull rather than the analogy around it: every critique became
a list of things to fix. That is the mechanism behind the twenty years, and it is available to AI video teams
today, except that almost nobody writes the defect down next to the prompt and seed that produced it. Without
that record, each release gets judged on feel, and no one can say whether the thing that bothered them in
January is fixed in June.

**Deliberately absent.** No congratulations on the funding, the ARR or the valuation, all of which are in his
profile and his other posts. No mention of the benchmark, the review or Aithos. No reference to the podcast
link, which is in his own comments.

Draft, 109 words, lint clean, gate 100: `2026-11-03_comments/15_alex_mashrabov.txt`.
