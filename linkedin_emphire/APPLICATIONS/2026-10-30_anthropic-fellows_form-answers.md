# Anthropic Fellows form: field-by-field answers

Date: 2026-10-30
Companion to `2026-10-30_anthropic-fellows_application.md`.
Form: Constellation / Airtable, reached via bit.ly/afpsafety.
Status: PREPARED. Nothing submitted.

The live form is bigger than the structure assumed earlier. It asks for residence
and authorization country separately, three references each with a background
paragraph, and a stream choice.

## General information

- First name: Olusanya
- Last name: Timothy
- Email: olusanyatimothy54@gmail.com
- Resume PDF: `RESUME/Timothy_Olusanya_Anthropic_Fellows.pdf`
- AI policy confirmation: Yes. Read anthropic.com/candidate-ai-guidance first, it is short.
- Applied to Anthropic full time, MATS, Astra or this program in the past year: no record in this repo. Confirm from memory. If you did, answer Yes. A mismatch against their own system is worse than the earlier application.
- Previously interviewed at Anthropic: no record here. Confirm.
- Pronunciation and pronouns: optional, skip unless you want them used.
- Constellation sharing opt-in: say yes. It costs nothing and puts you in front of other safety programs.

## Links

- LinkedIn: https://www.linkedin.com/in/olusanya-timothy
- Google Scholar: blank, there is none.
- GitHub: https://github.com/Teamthy
- Personal website: blank, there is none.
- AI safety and security output, one per line:

```
https://github.com/Teamthy/ai-redteam-five-tests
https://github.com/Teamthy
https://www.linkedin.com/pulse/five-boring-failures-ship-your-ai-feature-olusanya-timothy-pl4oe
https://www.linkedin.com/in/olusanya-timothy/recent-activity/articles/
```

The form asks for the profile rather than every post, so the article index is the
right entry for the series. The harness goes first because it is the one link that
answers "can this person run an experiment."

## Stream

Top choice: AI Security & Frontier Red Team.

Additional teams: leave unchecked unless you also rewrite the research answer around
evaluation design. A credible single-stream application beats a spread. If you do
check a second, make it AI Safety & Alignment, and only because the harness is an
evaluation instrument. Do not check mechanistic interpretability. Nothing in the
record supports it and it is the stream where a weak claim shows fastest.

## Why the program (830 characters)

The one I keep coming back to is the Fellows project where AI agents found $4.6M in
smart contract exploits. Not the number, the shape: agents pointed at a real system, a
result nobody could have written by hand, and enough instrumentation that the finding
could be checked afterwards. That is the version of security work I want to do.

My own work sits a few steps behind it. I test LLM features before they ship, and I got
tired of findings only I could reproduce, so I built a harness that writes raw responses
and counts beside every failure. Four months with a mentor and a compute budget is the
difference between running checks on my own client work and running them at a volume
where the result is worth publishing.

I am not coming from a research lab. I would rather say that now than have it found out
in an interview.

## Research areas (766 characters)

AI Security & Frontier Red Team, and the question I care about is where an agent's
authority actually lives. A model can refuse inside a chat window and still act through
a tool call, so an evaluation that only reads the transcript will miss it.

Tool descriptions are the part I think is under-tested. They sit on the same surface as
user input, they are written by the integrating team, and almost nobody attacks them.
My harness already runs a tool-description injection check and it is the one that
surprises people.

The second area is measurement. Most agent security claims rest on one vivid transcript.
I want to work on failure rates with sample sizes, negative controls, and re-runs across
model versions, because a rate without n is a story, not a result.

## Likelihood of accepting a full-time offer (397 characters)

High. Around 85%.

The honest caveat is location rather than intent. I am based in Lagos and I have US work
authorization, so a full-time role would mean being in the US for it. I would rather put
that on the table here than have it surface at offer stage. If the location works, the
answer is yes without much hesitation, because this is the work I already do with less
support than I would like.

## Likelihood of continuing in the streams (232 characters)

High. Around 90%.

Adversarial testing of AI systems is what I do now and what I read on my own time. The
security and evaluation streams are the two places where the work I have already
published would compound rather than restart.

## Logistics: the answers only you can give

- Cohort availability: January 2027. Tick it only if the four months are real.
- Current country of residence: Nigeria, unless you are living somewhere else now. This is the field the whole application hangs on, because the authorization field and the workspace field are read against it.
- Work authorization country: USA, if that authorization is unrestricted and valid January to May 2027. Check the document before answering. "None" ends the application.
- Other commitments, adjust to the truth:

  "I am currently employed full time as a software engineer at Teamart.inc in Lagos. The Fellows program is 40 hours a week and I would need to stop or step back from that role to do it properly, which I am prepared to do if I am selected. I have no other ongoing commitments during the program period."

- Workspace: follows from residence. If you will be in the US, Berkeley for the entire program is the strongest true answer. If you will not be, do not select a workspace you cannot attend. Choose Other and state where you would work. The honest version is weaker and the false one is fatal.
- How did you hear: Krish Naik's LinkedIn post, 30 October 2026.
- Anything else, suggested: "The demo repo is small on purpose. It runs in a few minutes against a cheap model and writes the raw outputs, so you can re-derive any failure I report without taking my word for it."

## References: the part that decides this

**SLOT 3 IS FILLED as of 2026-10-31:** Andrey Ekhmenin,
`andrzej.ekhmenin@gmail.com`. Confirmed by DM, full record and paste-ready field values in
`2026-10-31_anthropic-fellows_reference_andrey-ekhmenin.md`. Use Colleague / Collaborator,
Yes on AI research, **knowledge 2**, and state the four days of exchange in the paragraph.
Do not retype the address; it is Polish spelling and the name is not.

Three are required, each with a background paragraph. They may be contacted without
notice and asked to reply within a week. Nothing in the repo supplies three technical
referees, so this section cannot be drafted for you.

Each entry needs: name, email, whether they work in AI research, how you know them,
how well (1 to 4), and a paragraph with title, public links, what you worked on,
when, how long, and how closely.

Ranked by what the form says it values, people who saw technical work:

1. A manager or senior engineer at Teamart.inc who saw the red-team findings and the fixes that shipped. Manager. Knowledge 3.
2. The lead or client contact at YKAY ConsultingHub on the backend and access-control work. Manager or Colleague. Knowledge 3.
3. Someone from the safety or security network who has read the harness or the series and can speak to the work rather than your character. Colleague, Collaborator or Mentor. Knowledge 2 or 3. Be honest on the scale. An inflated 4 that collapses on a five-minute call is worse than an honest 2.

A referee who says "he is a hard worker" is a wasted slot. Brief each one: the program,
the stream, the harness, the date you applied.

## What actually moves the odds

There is no version of this application that reaches 95 percent. The program funds a
small number of people from a global pool, and plenty of applicants arrive with
papers. Any figure I gave you would be invented, and the rule in this repo is that we
do not do that.

What is controllable:

1. The location answer. If residence and authorization do not add up to being in the US, UK or Canada from January to May, nothing else in the form matters.
2. Real referees, briefed and reachable, able to talk about specific technical work.
3. One link that proves you can run an experiment, placed first. The harness does that.
4. A single stream, argued in your own words, with your own numbers in it.
5. Publishing the tool-description injection result today. The form explicitly invites unpublished work to go online and be linked. A short write-up with the test inputs, the sample size and the raw output is the only thing left that changes what a reviewer sees, and it is the closest thing to a research artifact you can still produce before the deadline.

What does not move the odds and costs time: more adjectives, claiming research
experience you do not have, checking all three streams, padding the resume. The form's
accuracy declaration covers work samples, and the interview is a research discussion
with a mentor.
