---
deliverable: doc
id: 2026-11-10_systems-to-add
date: 2026-11-10
audience: internal
status: ready
---

# Four systems that would drive the objectives harder than more rules

The diagnostic first. The repo is strong at output: forty rules, a gate that blocks, a delivery log,
an index, a reply queue. It is close to empty on outcome. There is a follower log with one row in it,
a performance tracker with snapshots through October, a growth plan with checkpoints, and nothing that
reads any of them and says whether the week worked.

Effort is not the constraint. Feedback is. Every system below exists to shorten the distance between
doing the work and knowing what it did.

## 1. A pace instrument

**Built.** `TOOLING/pace.py`, run at the start of a session. It reads `analytics/follower-log.md`,
prints the rate, the projection to 25 December, and which checkpoint is next, and says when the log has
no row for the day. It is thirty lines of arithmetic against numbers the owner already has.

Why this one first: the 6 November plan says the single most important growth event of the year
produced 522 followers and left no trace to copy. The log was created to fix that and got one row. A
ledger nobody opens is a diary. This reads it back in one screen, which is the difference between a
habit and a document.

## 2. A weekly review with a mandatory kill

**Built as a template.** `PIPELINE/70-WEEKLY-REVIEW.md`, output to `STATE/REVIEWS/`. Twenty minutes,
three decisions, and one of them is always what to stop. Forty rules have gone in and none has come
out. The same is true of templates, thread types and posting slots.

Why it matters more than another rule: a system that cannot remove things cannot stay honest. The kill
line is the only part of the review that is not optional, and it is the part that keeps the other
thirty nine rules read.

## 3. A borrowed audience pipeline

**Not built, because it starts with the owner's voice.** The plan ranks borrowed audiences fourth by
effort and first by size per event: one appearance in front of twenty thousand people does what a
month of posting cannot, and the lead time is weeks. Nothing in the repo tracks a single ask.

What it needs to be: one board, six to ten named shows, newsletters and podcasts in the eval and
security lane, each with the person, the route to them, the ask, the date sent and the date to follow
up. Two asks a week, and the follow-up is a row rather than a memory. The hard part is the list, and
the list has to be the owner's, because a pitch to the wrong show is worse than no pitch.

Against 25 December this is the only lever with a chance of moving the number in a step rather than a
slope. It is also the one that fails silently if it starts in December.

## 4. A case-study system, for the objective behind the follower objective

Five thousand followers is not the objective. Work is. The two client engagements in this repo, the
FORAY register and the Evelyne recomputation, are the strongest artefacts the owner has produced, and
they are visible to two people.

What it needs to be: after each engagement milestone, one de-identified page, cleared with the client in
writing, filed under the client directory and indexed for reuse. The rule already exists and is not in
question: client work stays private until they agree otherwise (R19). What is missing is the ask, made
once, early, and the habit of producing the page while the work is fresh rather than reconstructing it
eight months later.

## What I would not add

**A content calendar with more slots.** There is already a calendar and a plan with three posts a week.
Adding slots adds output, and output is not the bottleneck.

**A CRM.** Four clients and a handful of leads do not need one. `STATE/PIPELINE-BOARD.md` would do if
the folders ever stop being enough, and that day has not arrived.

**A second analytics stack.** The tracker exists and LinkedIn's own numbers are the only ones that
count. More measurement of the same thing is displacement activity, and it is the most comfortable
kind.

## Order

Pace first because it is built and it makes the rest readable. Weekly review second, because it is the
loop that keeps the other three alive. Borrowed audiences third, because of the lead time. Case studies
fourth, because they convert work already done rather than starting new work.
