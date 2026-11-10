# Session log, 2026-11-10

## Owner question: what other system should be added to drive the objectives

Answered by auditing what the repo already holds against its own plan, which turned out to be the
substance of the answer. The repo is strong at output and close to empty on outcome: forty one rules,
a gate that blocks, a delivery log, an index, a reply queue, a follower log with one row in it, a
performance tracker with snapshots to October, and a 5,000 follower plan with three dated checkpoints.
Nothing reads any of them.

Built:

- **`TOOLING/pace.py`.** Reads `analytics/follower-log.md`, prints the rate, the projection to
  25 December, the next checkpoint and whether the day has a row. First run on 10 November: last row
  6 November at 1,007, so the projection is 1,007 against 5,007, and the 15 November checkpoint is
  not met with five days left. That is the useful kind of ugly.
- **`PIPELINE/70-WEEKLY-REVIEW.md`.** Twenty minutes, three decisions, and one of them is always what
  to kill. Output to `STATE/REVIEWS/`. Forty one rules have gone in and none has come out; the same is
  true of templates, thread types and posting slots.
- **R41.** A session opens with the pace reading and the reply queue, and no post ships on a day whose
  follower row is missing.

Proposed, not built, because each starts with the owner's voice or his permission:

- **A borrowed audience pipeline.** The plan ranks it fourth by effort and first by size per event, and
  nothing in the repo tracks a single ask. Against 25 December it is the only lever that moves the
  number in a step rather than a slope. The list has to be his.
- **A case-study system.** The FORAY register and the Evelyne recomputation are the strongest artefacts
  here and two people can see them. One de-identified page per engagement milestone, cleared in writing
  first (R19 unchanged).

Rejected: more posting slots (output is not the bottleneck), a CRM (four clients), a second analytics
stack (the most comfortable kind of displacement activity).

## Owner instruction: build and integrate them, ensure they are always implemented

The two systems that were proposals at the end of the last message are now built, and the integration is
the part that makes them survive a session where nobody remembers they exist.

Built:

- **`STATE/BORROWED-AUDIENCE.md`.** Eight named shows and newsletters in the lane and adjacent to it,
  checked against public listings on 10 November, each with a route column that currently reads
  "unknown" because a route that is guessed is a route that fails at the pitch. States run from prospect
  to booked. Reach numbers are deliberately absent.
- **`PIPELINE/80-CASE-STUDIES.md` and `STATE/CASE-STUDY-INDEX.md`.** The permission ladder in front
  matter, the six things a case study contains, the de-identification list, and the argument for asking
  at the first milestone rather than at the end. C1 is the FORAY register, C2 is the Evelyne-Clarke
  recomputation, both drafted-first, neither shared.
- **`TOOLING/board.py`.** Reads the follower log, the reply queue, the two new boards and says what is
  late in four lines.
- **`./emphire board`, and `./emphire start` now prints the brief.** That is the integration: the boot
  brief cannot be skipped without skipping the rules, so the boards are read every session whether or
  not anyone thinks about them. First run says the follower row is four days old and that no borrowed
  ask has gone out.
- **R42 and R43.** The cadence, and the permission check, which blocks a case study at `status: ready`
  without `permission: granted`.
- **Weekly review extended.** `./emphire board` replaces the separate pace and queue reads, one of the
  three weekly decisions must be a borrowed ask when none went out, and a monthly question asks whether
  a finished client milestone has gone thirty days without a page.

## Owner question: what next

Answered by doing the cheapest unblocked thing rather than listing it: C1 of the case-study system is
now a drafted page, `CLIENTS/foray-dunin7/CASE-STUDY-1_open-protocol-anchoring.md`, PASS 0/0, with the
permission ask written beside it as `CASE-STUDY-1_permission-ask.txt`. The ask names the seven things
that would be removed and offers him the choice of being named or not, because the ask is easier to
answer than to postpone.

The page is a draft and stays one. `permission: not-requested`, and R43 will block it the moment anyone
sets it to ready.

Order proposed to the owner, in this order: the follower row for today (thirty seconds, and the pace
line is blind without it), the two borrowed asks for this week (route first, then pitch), the C1 ask
attached to the next Marvin reply, and the day's post.

