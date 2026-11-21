---
deliverable: internal
id: 2026-11-21_thread_linkedin-marvin
date: 2026-11-21
audience: internal
status: ready
approved: no
title: The LinkedIn thread with Marvin Percival, 00:08 to 00:16 WAT on 21 November 2026, as pasted by the owner
time_checked: >-
  checked: 2026-11-21 04:44 WAT, read from the system clock in the sandbox before this file was written.
sources_read: >-
  read: the two messages as pasted into the session by the owner at about 04:40 WAT on 21 November. Nothing opened.
  Times are the times LinkedIn showed, in WAT.
---

# Marvin thread, 21 November

What this is: the record of what Marvin sent on LinkedIn overnight into 21 November. Who it is for: any session working
on Ẹ̀rí or on the Marvin relationship. What to do next: the reply is drafted in
`ENGAGEMENT/2026-11-21_dm_marvin-the-recovery-sheet-is-where-i-test.md`. Nothing is withheld from this copy.

## The thread

**Marvin Percival, 00:08**

> Slow, but getting there.
>
> Just told Claude to make sure all documentation is updated

**Marvin Percival, 00:16**

> Why Stele looks complicated for a simple purpose
>
> Signing in is simple, and it is simple in Stele too: touch a passkey, enter a code. The complexity comes from one
> choice you made, no email and no username. Every other system gets its safety net from email: "forgot password" sends
> a link. Stele has no such net, so losing every passkey means being locked out for good. Everything in the recovery
> work rebuilds that net without email. Each piece comes from a specific case in the 23-case table:
>
> A recovery sheet needs a waiting period, so a stolen sheet can't be used at once.
> The waiting period needs a record, so recoveries are visible.
> Cancelling needs the old sessions ended.
> Limits on guessing need counters.
> A request that survives a restart needs the database-backed stores.
>
> Three more reasons it feels heavy:
>
> Stele stands alone. It can't borrow a host's email, audit log or rate limiter, so it has to carry its own.
> Safe changes to a live system have a fixed overhead. The two passes, halts, engine checks and a documentation sweep
> for each release are discipline, not product complexity. A host's integration code stays small.
> Our own process adds weight. Four CRs where one might do, and a tag for each. I split them because it keeps each
> change small enough to check, not because the code needs it.
>
> The guard against it growing: every addition has to trace to a case in the table. If a piece doesn't, it's scope
> creep, and I should say so.
>
> For the person using it: nothing changes. They sign in with a passkey. If they lose a phone, they use another passkey
> or their recovery sheet.

The 00:16 message reads as an explanation written by Marvin's own Claude session and pasted on; it speaks to Marvin as
"you".

## What it settled

| Point | Time |
| --- | --- |
| Stele's recovery logic is in progress, not done | 00:08 |
| Stele keeps no email and no username; recovery is a sheet with a waiting period, a record, session end on cancel, guessing counters and database-backed stores | 00:16 |
| Every Stele addition must trace to a case in the 23-case table, or it is scope creep | 00:16 |
| Stele work ships as four CRs, each tagged | 00:16 |

## What it left open

- The 23-case table has not been shared with the owner.
- Whether the owner tests Stele's recovery path, offered in the reply.
