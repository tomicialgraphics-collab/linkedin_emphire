---
deliverable: doc
id: 70-weekly-review
date: 2026-11-10
audience: internal
status: ready
---

# The weekly review, and the kill list

Twenty minutes, Sunday evening, before the week's posts are drafted. One file out:
`STATE/REVIEWS/<date>_week-<n>.md`. The output is three decisions, not a summary.

The repo polices what goes out. Nothing in it reads what came back, and forty rules with no
removal loop end up ignored, which is worse than twenty that are kept. This is the loop.

## In order, twenty minutes

| Minutes | Read | Ask |
| --- | --- | --- |
| 0 to 5 | `python3 TOOLING/pace.py` | Is this week's number real, and which checkpoint is next |
| 5 to 10 | `STATE/DELIVERY-LOG.md`, last seven days | Which artefact produced a measured outcome, and which produced nothing |
| 10 to 15 | `STATE/OPEN-LOOPS.md`, `STATE/REPLY-QUEUE.md` | What is older than seven days, and who is waiting |
| 15 to 20 | the week's posts and comments | Which single piece would I keep if I could keep one |

## The three decisions

1. **Name the week's best and worst by measured outcome, not by feel.** Impressions, follower
   change, replies from the people worth reaching. If nothing was measured, that is the finding and
   it goes in the file.
2. **Kill one thing.** A thread type, a template, a posting slot, a habit, or a rule. Every week.
   Something goes. The review that only adds is the review that fills the repo with unread files.
3. **Point the next week at three things.** Not five. Each names the artefact and the day.

## The template

```
# Week <n>, ending <date>

## Pace
followers <n>, net <n>, projected 25 Dec <n>, checkpoint <name> <met|not met>

## Measured
best: <artefact> <number>
worst: <artefact> <number>
nothing measured: <why, if that is the answer>

## Killed
<one thing, and what replaces the time it took>

## Next week, three things
1. <artefact>, <day>
2. <artefact>, <day>
3. <artefact>, <day>

## Rules touched
<added, changed or retired, with the failure behind the change>
```

## What this is not

Not a planning session. The plan exists in `STRATEGY/2026-11-06_follower-plan_1007-to-5000.md` and
is not rewritten here. Not a journal. Every line in the file is either a number, a name or a decision,
because those are the only three things a later session can act on.
