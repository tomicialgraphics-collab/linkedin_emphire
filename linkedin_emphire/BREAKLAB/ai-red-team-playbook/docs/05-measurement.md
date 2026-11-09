# 05 Measurement

Covers `ME-01` to `ME-35`.

This is the section that decides whether the rest of the work is worth anything. Breaking a demo is easy and has no market. Turning a break into a number somebody else can rerun is scarce.

## 1. Define the unit before you count

Two defensible units and one indefensible habit.

- **Per attempt.** 3 successes in 20 attempts is 15 percent. Answers: how often does this specific probe work.
- **Per objective.** 3 successes across 5 objectives that were each tried 20 times is 60 percent. Answers: how many of the things we tried to do can be done at all.

Both are true, both are useful, and 15 percent and 60 percent describe the same afternoon of work. Reports that do not say which one they mean are not comparable to anything, including themselves.

Then weight. A rate that averages a leaked greeting with a leaked credential is an average of two different incidents. Either report by severity band or report the worst case, but say which.

## 2. Put an interval on it

Small samples produce wide intervals, and small samples are what engagements produce.

| Result | Rate | 95 percent Wilson interval |
|---|---|---|
| 3 of 20 | 15 percent | 5.2 to 36.0 percent |
| 2 of 5 | 40 percent | 11.8 to 76.9 percent |
| 0 of 20 | 0 percent | 0 to 16.1 percent |
| 20 of 20 | 100 percent | 83.9 to 100 percent |

Three of those four lines are uncomfortable, which is the point. The first says "somewhere between rare and common". The third says "no successes, and still up to one attempt in six could work". The fourth says "consistent, not certain".

```bash
python3 tools/wilson.py 3 20
```

Use Wilson rather than the textbook normal approximation: at small samples and extreme rates the normal approximation produces intervals that cross zero and collapse to a point, which is exactly where most attack success rates live.

## 3. Report the spread, not the mean of one run

Nondeterminism is a property, not a defect. Run the same suite five times and report the range.

> Five runs of the same 20-case suite: 2, 3, 3, 4, 5 successes.

That sentence is worth more than any single number, because it tells the reader how much of the difference between two versions could be noise. If the two versions differ by less than the spread, you have not measured anything.

## 4. Capability and reliability are different questions

- **pass@k**: can it be done at all, given k attempts. A capability question, useful for dangerous capability work and for the "no known technique works" claim.
- **pass^k**: does it work every time, across k attempts. A reliability question, and the one that matters for an agent doing a job.

A system at 90 percent per step and ten steps per task finishes roughly a third of tasks. Reporting the step rate as though it were the task rate is the most common arithmetic error in agent evaluation.

## 5. Judges are instruments, so calibrate them

Nearly all large safety evaluation now runs through a model grader. Model graders have documented biases that will move your number:

- **Position bias.** The answer in position one wins more often.
- **Verbosity bias.** The longer answer scores higher.
- **Self-preference.** A judge favours output from its own family of models.

So:

1. Hand-grade a random sample of at least forty cases.
2. Report agreement, and use kappa rather than raw percentage if the classes are unbalanced.
3. Run the position swap on a slice and see whether verdicts move.
4. Trim one answer and see whether the score follows the length.
5. Record the judge model, its revision and the exact rubric prompt.

If agreement is poor, the judge is the finding. A rubric that cannot be applied consistently by a careful human will not be applied consistently by a model either.

## 6. Compare versions properly

Two independent rates invite the wrong conclusion. Use the same cases for both versions and compare the discordant pairs: cases where A failed and B passed, against cases where A passed and B failed. That is McNemar's test, and the intuition is enough to report honestly: only the cases where the versions disagreed carry information.

Then check power. A 30-case suite cannot detect a five point difference, and claiming it did is the most common form of overclaim in this field.

## 7. The reproducibility contract

Six fields, every case, every time: model revision, prompt version, index snapshot, tool schema version, sampling settings, date. Add the judge version when a model graded it.

The personal test: take a finding from three weeks ago and rerun it exactly. If you cannot, you did not find it.

`GV-30` and `ME-35` exist because this is the field most likely to be skipped and the one a reviewer will ask about first.

## 8. Coverage beats a headline number

A single rate invites the question "out of what". The coverage argument answers it before it is asked. `tools/coverage.py` produces one from a status file:

```
168 classes in the checklist. 23 tested, 2 not present, 1 skipped, 142 open.
```

The `open` row is the honest part and the part most reports omit. A class that was skipped on purpose, with a reason, is a finding about the engagement. A class nobody named is a claim the reader will assume you checked.

## 9. Hand it over

Every confirmed finding becomes a case in a suite that runs on every deploy, owned by the client, runnable without you.

```bash
python3 tools/render.py        # regenerate the printable checklist
python3 tools/validate.py      # check the source is well formed
python3 tools/coverage.py examples/status-example.json
```

A suite nobody can afford to run is a demo. Report the cost per case and the time per run alongside the findings, because both decide whether the thing survives contact with a release schedule.
