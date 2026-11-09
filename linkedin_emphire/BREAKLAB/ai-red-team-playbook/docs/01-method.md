# 01 The method

## Three axes, and why conflating them breaks the work

Almost every bad AI security report fails in the same way: it reports one thing while the reader hears another.

- **Capability.** What the system can be made to do when someone pushes it hard. Tested with adversarial effort, an adaptive attacker and unlimited attempts.
- **Propensity.** What the system does when nobody is pushing. Tested with realistic traffic and honest usage.
- **Measurement.** Whether the number you produced would survive somebody rerunning it.

A model that *can* be argued into leaking a system prompt and a model that *volunteers* one are different risks with different controls. A rate with no denominator and no revision is not a measurement, it is an anecdote with a percentage sign.

Every finding in this playbook should be expressible in one sentence that covers all three:

> The system returned the full system prompt in 19 of 20 attempts, on revision 4 of the model, prompt v17, on 9 November, judged by a rubric that agreed with hand grading on 38 of 45 sampled cases.

That sentence is worth more than a page of adjectives, and it takes about four times as long to produce.

## The loop

1. **Scope.** Written rules of engagement, authorised targets, a stop condition, a named person who can stop it. See `templates/engagement-scope.md`.
2. **Map.** Every input channel, every tool, every output sink, every credential behind a tool. One diagram. The map is a deliverable, not a step.
3. **Test.** Work the checklist category by category, recording `tested`, `absent`, `skipped` or `open` as you go.
4. **Measure.** Turn the interesting results into cases with a denominator, a revision and an interval.
5. **Report.** Findings with a severity method, then a coverage argument that names what you did not test.
6. **Hand over.** Every finding becomes a case in a suite the client owns and can run without you.

Step 6 is the difference between a report and a repair. It is also the step most engagements skip, which is why the same bug comes back under a new prompt three months later.

## What "done" means for a single case

A case is done when all six of these are recorded:

| Field | Why |
|---|---|
| Model revision | A vendor alias can move under you between the test and the report |
| Prompt version | The system prompt is code, and unversioned code cannot be fixed |
| Index snapshot | Retrieval results depend on the corpus as it stood that day |
| Tool schema version | A tool definition change can change the finding |
| Sampling settings | Temperature and top-p change the spread, not just the output |
| Date | Everything above expires |

If any of those is missing, the case is an observation. Keep it, but do not put its rate in the summary.

## How to choose what to test first

Rank by blast radius, not by novelty:

1. What can an attacker reach without an account.
2. What can a tool do with the credential behind it.
3. What persists after the session ends.
4. What cannot be reconstructed afterwards.

If the answer to the fourth is "very little", stop testing and go fix the logging. A finding nobody can prove is a finding nobody will fix.

## The thing this playbook cannot do

There is no finite checklist that certifies an AI system as safe, because the input space is natural language and the behaviour depends on content nobody controls. What you can do is narrower: declare the classes you tested, count them properly, state the interval, name what you skipped, and leave behind a suite that reruns.

Anyone offering a certificate is selling a number rather than a measurement. The honest version of this work looks like a coverage argument with a large, explicit `open` row, and that is what `tools/coverage.py` exists to produce.
