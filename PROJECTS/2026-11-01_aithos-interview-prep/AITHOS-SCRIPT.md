# The Aithos script: read this aloud until it is yours

Read once a day, out loud, from 2 November to the day of the call. Twenty minutes a sitting. The
point is not memorising. It is that the sentences come out of your mouth without you assembling them
first, because fluency under mild pressure is the only thing an interview actually measures that you
cannot fix later.

How to use the page: anything under **SAY** is spoken, roughly as written. Anything under **NOTE** is
for you and is never spoken. Numbers are the ones Aithos published, with their dates, because the
figures moved during the year and the old ones are a small tell.

---

## 1. The ninety second introduction

**SAY**

I'm Olusanya Timothy. I'm a software engineer working on the failure side of AI systems, which is the
part where a model does something that looks reasonable and is wrong, and nobody notices for a month.

Most of that work is building instruments rather than writing opinions. I have a small rig that
probes four things against any OpenAI-compatible model: prompt injection, retrieval poisoning,
tool-description poisoning, and refusal behaviour across languages. I have a benchmark for what
happens when the host process dies in the middle of a decision, which is a boring failure that turns
out to be everywhere. And I publish the parts that did not work, because a tool nobody can check is a
claim rather than a tool.

The reason I applied here is specific. Aithos is the only group I have found that treats evaluation
as a public instrument rather than a private scoreboard. LARA puts an agent inside European law and
publishes every transcript, and then publishes its own methodological corrections. That is the
tradition I want to build tools in.

**NOTE**

Ninety seconds, four ideas: who you are, what you build, what you publish, why here. Do not add a
fifth. Do not say "passionate". Do not say "I've always been fascinated".

---

## 2. How you describe their work, in their own terms

**SAY**

What I took from LARA is the shape of the instrument. You put the model in a simulated workplace with
real tools, an auditor model steers it toward a provision of the AI Act or the GDPR, and three judge
models score the transcript against the verbatim text of the law. Ten scenarios at release across four
GDPR principles and six AI Act provisions, about three thousand runs across twelve models, and the
best performer at the time still breaking the law in 46 percent of cases.

The part that stayed with me is what you did in August. You ran the instructed condition and found
average compliance rising from 31 to 44 percent, which is a real improvement and nowhere near enough.
You checked whether models at least obey their own providers' usage policies and found nine of
sixteen doing so in the majority of runs. Then you changed the headline number to the instructed
condition, in public, on the grounds that it is the harder result to argue with. Most groups would
have kept the flattering baseline and mentioned the rest in a footnote.

**NOTE**

This is the segment that proves you read the paper rather than the coverage. The three numbers to
land are 31, 44 and nine of sixteen. If he or she asks which paper, it is "No one is holding the
line", August 2026, Daan Henselmans.

---

## 3. The line you hold when the conversation gets philosophical

**SAY**

The way I think about it, alignment work splits into two questions that get confused. One is what the
model should do. The other is who gets to decide, and how anyone outside the room finds out whether
it did it. My work is almost entirely the second question. That is why the interest is in evaluation
as an instrument rather than in training methods. A model that behaves well in a lab and cannot be
checked in deployment has not been aligned, it has been reviewed.

**NOTE**

This is your bridge to their third pillar without saying "procedural legitimacy" like a slogan. If
they name it first, agree and move on. Never use the phrase before they do.

---

## 4. The take-home narration, if they ask how you approach a three hour task

**SAY**

I would spend the first twenty minutes writing down what would make the answer wrong. Which judge,
how many runs, which model version, whether the pressure the auditor applies is the same for every
model I test. Then I would build the smallest thing that produces a real number, with the auditor
prompt and the judge prompt both in the repository, versioned, and every transcript written out in
full.

Then I would report the number with its n and an interval rather than as a bare percentage, and I
would write half a page on what the result does not show. If someone can take what I hand back and
re-run the scoring without me, it is evidence. If they cannot, it is a result, and those are
different things.

**NOTE**

If they give you a real eval instead of asking, do exactly this, and write the threats-to-validity
section first if you run short on time. A short honest submission beats a complete confident one.

---

## 5. The one technical position, spoken respectfully

**SAY**

The thing I would want to work on is judge reliability. Three judges from three labs is better than
one, and the 96.7 percent agreement with human annotation is a real result. It is also a calibration
on your own scenario distribution, which is the friendly version of the test. Models from different
labs still share training data, a house style, and a tendency to be persuaded by confident prose.

Two things would make the next set of results harder to argue with. A blind slice, where two
annotators judge transcripts without seeing the model name or the judge's verdict, and the
disagreements are published as a rate rather than quietly resolved. And a re-run button: freeze the
transcripts, pin the judge version, and let someone recompute the leaderboard from the frozen record.
Your leaderboard already toggles between AI and human-corrected scores, so most of the plumbing
exists.

**NOTE**

Offer, never accuse. The phrase to avoid is "your judges are biased". The phrase to use is "the
agreement figure is measured on a friendly sample". If they push back, agree with the pushback and
ask what they would need to see.

---

## 6. "Tell me about something you built and what went wrong"

**SAY**

I built a benchmark for host failure modes, sixteen failure classes across a small decision system,
and then I paid for an independent technical review of it, because a benchmark that grades itself is
worth nothing.

The review came back with 36 outcome tests and 13 input checks. My version reproduced 23 of the 36 as
defects before I fixed anything, and 9 after. Two of the findings I disputed. One said that on replay
the system re-stamps the decision timestamp with its own clock and re-signs the record, which would be
a serious defect if it happened. It did not happen in that fixture, and I could show why: the replay
step and the decision step were the same number, so the mutation wrote back the value the field
already held and the bytes came out identical. That is a defect in the test rather than in the code.

Arguing that would have been cheap. So I built the case the property actually needs. A synthetic
variant that injects a real divergence between the two clocks, with a control run that reproduces the
inert case, so the difference could only come from the divergence and not from me changing the
checker. The timestamp then goes from 2 to 7, the record stops matching the log, and two independent
checks fail. The reviewer accepted it, and the entry is now written in his language rather than mine.

The thing I took from that is that being right is not the same as being checkable. My first version was
right and unhelpful. The variant made it checkable and it settled in one message.

**NOTE**

This is your best story and you get to tell it once. The shape is: I was disagreed with, I did not
defend, I built the better test, it settled. Do not add a moral. The last line is the moral.

---

## 7. The six questions you will probably get, with answers

**Why Aithos, and not a lab?**

**SAY** Because the interesting constraint here is legitimacy rather than capability. A lab can
publish a safety result and nobody outside can check it. Here the output is a public instrument, and
the test of whether I did the job is whether other people can use it.

**You do not have publications. Does that matter?**

**SAY** For this seat I do not think so, and I would rather be direct about the record. Two long-form
articles in a public series, an open-source test rig, and one benchmark with an external review and a
published disposition of every finding. That is not a paper. It is work that other people can run, and
I would rather show you the run than describe it.

**What would you build in your first month?**

**SAY** Whatever makes the next LARA result harder to argue with. My instinct is the re-run path and a
blind human slice, because those are the two things that turn a leaderboard into something a regulator
or a journalist can quote without being wrong.

**What do you do when a reviewer disagrees with you?**

**SAY** I separate the claim from the tone and test the claim. If the test is bad, I say so and build a
better one. If the code is bad, I fix it and add a regression so it cannot come back. In the last
review, two findings were disputed and both ended with a new test rather than an argument.

**Remote, or Amsterdam?**

**SAY** Either works for me, and I understand the shape here is remote with a monthly visit. I would
want the visits, because this kind of work is easier to do badly in isolation.

**What are you weak at?**

**SAY** Formal methods and the theory side of alignment. I can read a paper and implement it, and I am
not going to pretend that is the same as being able to derive it. What I am good at is turning a claim
into a test and making the result survive someone else checking it.

**NOTE**

All six are forty to sixty seconds. If an answer runs to ninety, you have started explaining rather
than answering.

---

## 8. Your three questions

Ask three, and only when invited. Pick the ones that fit the conversation.

**SAY**

Of the two halves of the job, building the tools and writing the papers, which one does this seat own
this year?

**SAY**

How do you decide that a scenario is a fair test of a provision, rather than a test of whether a model
will fold to a confident user? The auditor's pressure setting looks like the hardest design choice in
the tool.

**SAY**

What would make you say, at six months, that this hire worked?

**NOTE**

Reserve, if the conversation is technical and long: what compute and model access the role gets, and
who decides which models get benchmarked next. Do not ask about salary, relocation or visa in the
screen.

---

## 9. The recoveries

When you do not know something, the sentence is: "I don't know that, and I would want to read it
before I said anything about it." Then stop. No filler, no guessing.

When someone challenges a number you quoted, the sentence is: "That is the figure from the release
note in May. If it has moved since, use yours, because you would know better than I do."

When someone challenges your record, the sentence is: "You are right that it is not a paper. What it
is, is a tool you can run and a benchmark with a published review. Would it help if I sent both?"

When you have said something clumsy, the sentence is: "Let me put that better." Then say it better.
Nobody remembers the recovery. Everybody remembers the flannel that followed a bad sentence.

---

## 10. The follow-up message, for 14 November if the silence holds

One message, original subject line, three sentences, nothing attached.

> Following up on my application for the Research Engineer role, in case it arrived at a busy moment.
> Since applying I have finished a benchmark of host failure modes and put it through an independent
> external review, with the findings register and the disposition published. If it is useful I can send
> the two page summary, and either way I would welcome the chance to talk about the LARA work.

---

## 11. The seven day readiness plan

**Day 1, 2 November.** Read the homepage three times and write the three pillars from memory. Then
read "Introducing Aithos LARA" and list every design choice you disagree with. Two hours.

**Day 2.** Read "No one is holding the line" twice. Write the numbers table from memory: 10 scenarios,
4 GDPR principles, 6 AI Act provisions, 3,000 runs, 12 models, 7 to 54 percent in May, 14 to 56
percent across 18 in August, 31 to 44 percent instructed, 9 of 16 on provider policy, 96.7 percent
agreement. One hour.

**Day 3.** Run LARA on one scenario yourself. Read your own transcript end to end, then read a second
one where the model refused. Note the difference in the tool calls, not the prose. Two hours.

**Day 4.** Rehearse the take-home on a scenario of your own, timed to three hours, following section 4
of this script exactly. The lesson is how little fits.

**Day 5.** Read your own benchmark disposition, then say the V04 and N13 outcomes out loud in two
sentences each. Record yourself once and listen. Half an hour.

**Day 6.** Read this whole script aloud twice. Do not edit it on the second read, even where it sounds
wrong, because the version you have practised is worth more than the better sentence you invent at
11pm.

**Day 7.** Read sections 1, 2, 6 and 9 aloud once. Then close the file.

---

## 12. Night before, five lines

- The nine numbers from Day 2, out loud, once.
- The three pillars, in their words.
- The names: Daan Henselmans, research director. Nadia Kadhim, executive director. Lauren Toulson,
  AI researcher, the hiring contact.
- The one sentence you want to leave them with: a model that behaves well in a lab and cannot be
  checked in deployment has not been aligned, it has been reviewed.
- Camera, microphone, a glass of water, and the script closed before the call starts.

---

## 13. Three sentences never to say

"AI is my passion." It says nothing and costs you a minute.

"I know this is probably not what you are looking for, but." It makes them agree with you.

"To be honest with you." It implies the rest was not.
