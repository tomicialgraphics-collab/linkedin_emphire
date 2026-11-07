# Preparing for Aithos: Research Engineer

Written 1 November 2026, ten days before the follow-up window closes on 14 November. Everything
below is either from Aithos's own publications or from the process already recorded in this file.
Where something is my inference rather than their statement, it says so.

---

## 1. What the role actually is

From their own hiring post for the research engineer seat, the work is described as exploratory,
research-driven development: multi-agent collaboration, and building new AI safety tools for testing
and benchmarking. Amsterdam office or remote, with monthly visits to the office.

That sentence matters more than the title. They are not hiring a paper machine. They are hiring
someone who can turn a normative question into a tool that other people can run, which is the whole
of your public work so far. The publications line in the researcher advert is a preference, not a
gate for this seat, and the honest framing of your record is: an open-source test rig, a public
article series, and a benchmark with an independent external review. Say exactly that.

Two practical notes. Amsterdam and Lagos are both UTC+1 in November, so there is no clock gap to
explain in any scheduling conversation, and that stays true until their clocks go forward in March.
Remote with monthly visits is an offer they have made in public, so relocation does not need to be
settled before the first conversation, and should not be raised by you first.

### The monthly visit, before it comes up

The advertised shape is remote with monthly visits. You cannot commit to that cadence yet, and the
reason is administrative rather than personal. A Nigerian passport needs a Schengen short-stay visa
for the Netherlands, that needs an invitation letter from the employer, and the appointment calendar
is the bottleneck rather than the paperwork. Add the cost of each trip against a first-year
non-profit salary and monthly is not a promise you can keep in year one.

What you can offer, in this order:

1. Week one in Amsterdam, a week rather than a day, so onboarding happens in a room.
2. Quarterly visits of four or five days, timed to a release, an external review, or a partner
   session.
3. Between visits, a standing call in their morning and a written weekly update.
4. Relocation open to discussion on their timeline, once there is a reason for it.

The rules. Do not raise it first. If they raise it, say the constraint once, in the middle of the
answer, without apologising, and propose the cadence rather than asking permission. If they say
monthly is fixed, ask what the visits are for, because the answer tells you whether it is a real
requirement or a habit. The spoken version is in `AITHOS-SCRIPT.md` section 7.


## 2. The process, and what each stage is really testing

As recorded in your file: a 30 minute screen, a take-home of roughly three hours on a real
evaluation, then 60 minutes of technical conversation.

- **The screen** is testing whether you understand the difference between alignment as a training
  problem and alignment as an institutional one. If you arrive talking about RLHF you are answering a
  question they did not ask.
- **The take-home** is testing whether you can build a measurement in three hours that someone else
  could check. Not whether you can run an eval. Whether the thing you hand back is evidence.
- **The technical hour** is testing whether you have opinions that survive contact with a lawyer, a
  philosopher and an engineer in the same room. Their whole output lives at that intersection.

## 3. Read these five things, in this order

1. **The homepage**, for the three pillars in their own words: human agency, systemic alignment,
   procedural legitimacy. Learn the sentences, because they are the vocabulary the interview will be
   conducted in.
2. **Introducing Aithos LARA** (Substack, 27 May 2026, Daan Henselmans). Ten scenarios anchored to
   four GDPR principles and six AI Act provisions, an agent with tools in a simulated workplace, an
   auditor model that steers toward the violation, and three judge models scoring against the verbatim
   text of the law.
3. **No one is holding the line** (Substack, 14 August 2026). The most important document for your
   preparation, because it shows how they think. They ran two follow-up studies, found that telling
   the agent to obey the law only lifted average compliance from 31 to 44 percent, found nine of
   sixteen models violating their own provider's usage policy in the majority of runs, and then
   changed their headline methodology in public: the instructed condition becomes the default because
   "the instructed result is the harder one to argue with."
4. **Two transcripts, end to end**, from lara.aithos.org. Not the leaderboard. One where the model
   complied and one where it refused, so you can say what the difference looked like in the tool calls
   rather than in the prose.
5. **The two Paris papers** on verdict consistency, coherence and comprehensibility, referenced in
   Nadia Kadhim's post. Skim for what they claim about judge reliability, since that is where your
   contribution is closest to their open work.

## 4. The numbers to have cold

All theirs, all quotable with a source, and all of them dated, because the figures moved during the
year and quoting the superseded ones is a small tell.

| Claim | Figure | Source |
| --- | --- | --- |
| Scenarios at release | 10, across 4 GDPR principles and 6 AI Act provisions | LARA intro, May |
| Runs at release | 3,000+, 12 frontier models | LARA intro, May |
| Compliance range at release | 7 to 54 percent | LARA intro, May |
| Judges | three models, verdicts reviewed by human experts across 50+ hours | LARA intro, May |
| Judge agreement with human annotation | 96.7 percent | LARA intro, May |
| Range after expansion | 14 to 56 percent across 18 models | No one is holding the line, August |
| Instruction effect | average compliance 31 to 44 percent when told the rules | same, August |
| Provider-policy violations | 2 to 79 percent, nine of sixteen models in the majority of runs | same, August |

One nuance worth carrying into the room: their own stated limitation is that the adversarial auditor
is designed to bypass resistance and can read the target's reasoning, so the rates compare models
against pressure rather than forecasting real deployment behaviour. That admission is a strength, and
the fastest way to show you read the paper rather than the press coverage is to cite it before
anybody asks.

## 5. The take-home, as a three hour plan

Assume it is one scenario, one provision, and a request to evaluate a model. Structure the three
hours the way an auditor would, not the way a researcher would.

- **Twenty minutes, scope.** Write down what would make the result wrong before you build anything:
  judge choice, run count, model version, whether the auditor's pressure is held constant across
  models.
- **Eighty minutes, build.** One harness file, one scenario, a fixed number of runs, the auditor
  prompt and the judge prompt both in the repository with versions, and the transcripts written out
  in full. Pin the model identifiers. If they give you no API access, ask early rather than discovering
  it at hour two.
- **Forty minutes, run and record.** Report the rate with n, the interval, and the raw transcript
  count. Never a bare percentage.
- **Forty minutes, write.** Half a page: what you measured, what it does not show, and the one check a
  reviewer could re-run without you. Name the threats to validity yourself, in their vocabulary.

What separates a strong hand-in is not a better scenario. It is that the submission can be checked by
someone who was not in the room, which is the argument your whole public record is built on.

## 6. The one technical position to bring

Judge independence, and re-runnable verdicts. Their judges are three models from three labs, and the
96.7 percent agreement figure is measured against human-annotated cases from their own scenario
distribution. That is a real result, and it is also a calibration on a friendly sample. Three
models from three labs still share training data, refusal style, and a tendency to be persuaded by
confident prose.

Say it as a proposal rather than a criticism, and offer the two concrete things that would strengthen
their next paper:

1. **A blind human slice.** A held-out set of transcripts judged by two annotators who do not see the
   model name or the judge's verdict, with disagreements published as a rate rather than resolved
   silently.
2. **A re-run button.** Freeze the transcripts, pin the judge version, and let a third party recompute
   the leaderboard from the frozen record. Their leaderboard already toggles between AI and
   human-corrected scores, which is most of the way there, and the remaining step is the one that turns
   a published result into an audit.

That is your thesis pointed at their tool, and it is the kind of contribution they hire for.

## 7. The strongest thing in your file, and how to use it

You have something almost no applicant for this seat will have: a benchmark that went through an
independent external technical review, with a findings register, a disposition for every finding, a
reproduction of 23 of the reviewer's 36 outcome defects before the fix and 9 after, and a disputed
finding settled by building a better test rather than by arguing. The reviewer is named in the record
at his own request, which is itself the proof that the review was real.

Use it exactly once, in the technical hour, as the answer to "tell me about something you built and
what went wrong". A person who can describe an external reviewer disagreeing with them and how it was
resolved is rare, and it lands on their pillar about procedural legitimacy without you having to name
the pillar.

Do not lead with it. It is one benchmark against a small host-failure model class, and the honest
version of the claim is narrower than the impressive version. The narrow one is what makes them trust
the rest.

## 8. Questions to ask them

Ask three, no more, and pick from these according to how the conversation goes.

1. Of the two halves of the job, building the tools and writing the papers, which one does this seat
   own this year?
2. How do you decide that a scenario is a fair test of a provision rather than a test of whether a
   model will push back on a confident user? The auditor pressure setting looks like the hardest design
   choice in the tool.
3. When you moved the instructed condition to the headline number in August, was that contested
   internally? It reads like the kind of decision a research team argues about and then documents.
4. What compute and model access does the role get for evaluations, and who decides which models get
   benchmarked next?
5. What would make you say, at six months, that this hire worked?

## 9. Traps

- **Do not call the work "red teaming"** as your opening frame. Their word is evaluation, and LARA is
  a compliance instrument, not an attack. Red teaming is your route in, not the destination.
- **Do not pitch.** You are not selling an audit to Aithos. They are a non-profit hiring a builder, and
  the moment the conversation sounds like business development it stops being a hiring conversation.
- **Do not overstate the record.** Two published articles in a series, one open harness, one benchmark
  with an external review. Accurate and strong. "Published research" is a claim they will check.
- **Do not critique LARA before crediting what it established.** The defensible sequence is: they built
  the first public instrument that puts agents inside European law and publishes every transcript,
  and here is the next increment.
- **Do not raise salary, relocation or the visa in the screen**, and do not dodge them if they do.
  Amsterdam, remote with monthly visits, and a non-profit budget are all reasons to let them raise it
  first. If they ask, the answer is the cadence in section 1, said once, without an apology.
- **Do not agree to a monthly cadence you cannot keep.** It is the cheapest sentence in the call and
  the most expensive one to walk back, and it is the one thing in your file that a start date would
  expose within a month.

## 10. The 14 November follow-up, if the silence holds

One message, same subject line as the original, three sentences, no attachment.

> Following up on my application for the Research Engineer role, in case it arrived at a busy moment.
> Since applying I have finished a benchmark of host failure modes and put it through an independent
> external review, with the findings register and the disposition published. If it is useful I can send
> the two page summary, and either way I would welcome the chance to talk about the LARA work.

Attach nothing. Link once. Bump once, and if that is silent, the answer is no for this cycle, and the
right response is to keep publishing where they will see it rather than to write a third message.

## 11. What to do this week, in order

1. Read the five sources in section 3 and write the numbers table from memory. Two hours.
2. Run LARA yourself on one scenario and read your own transcript end to end. One hour. Being a user
   of their tool is worth more in the screen than any amount of commentary on it.
3. Build the take-home rehearsal in section 5 on a scenario of your own, three hours, and time it.
   The point is to discover that three hours is short, in your own time, not theirs.
4. Re-read your own benchmark disposition until you can summarise the V04 and N13 outcomes in two
   sentences each. Half an hour.
5. Write the 14 November message now and set it aside. Drafting it in advance is what stops it becoming
   a fourth paragraph of anxiety in a fortnight.
