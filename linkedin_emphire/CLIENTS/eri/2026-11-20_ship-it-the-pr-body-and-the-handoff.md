---
deliverable: internal
id: 2026-11-20_ship-it-the-pr-body-and-the-handoff
date: 2026-11-20
audience: internal
status: ready
title: Sixteen tests, four migrations, and the four things that are not schema problems
time_checked: >-
  checked: 2026-11-20 18:16 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer, who is at an airport or asleep and will read this pull request once. Everything
  that needs his answer is in the body as a question, and everything that is unfinished is named as unfinished.
premise_checked: >-
  checked: sixteen passing tests, four applied migrations and the four remaining objections are the agent's report of
  6:14 PM. Nothing here claims a requirement is met: REQ-020 also needs a server refusal and a screen, neither of which
  exists. The deployment limits are deployment limits and are labelled as such rather than left out.
sources_read: >-
  read: the agent's report of 6:14 PM. No page opened.
---

# Stop building, start shipping

The four things left are not schema problems and no further migration fixes them. The owner is a superuser, the purge has
to connect as the owner, the door check only ever sees a test database, and `eri_app` keeps a sequence grant it no longer
needs. Three of those are deployment rules for when there is a server, and the fourth is one line.

Continuing tonight would mean opening the code again for a change nobody has reviewed, on a branch that has been green for
ten minutes. Commit it.

# Commit and push

```powershell
git add .gitignore package.json package-lock.json drizzle tests
git status --short
git commit -m "CHORE: event store, append only, with the proof"
git push -u origin feat/event-table
```

`git status` before the commit should list six files and no `.env`. If `.env` appears, stop: the ignore is wrong and you
are about to do tonight twice.

# The pull request

Title: `CHORE: event store, append only, with the proof`

```
The event store, and the proof that it cannot be rewritten.

**What changed:** four migrations and one test file. Tables evidence_files, events, seals and seal_events, with uuid keys,
plural names, foreign keys named evidence_file_id and migrations in drizzle/, per the standards. Triggers refuse update,
delete and truncate on all four, for the owner as well as for eri_app. A seal can only name events from its own file. A
purge can only delete, only with a session flag set, and every row it removes writes a line into purge_log, which nothing
can update or delete and eri_app cannot write.

**Why:** REQ-020 and REQ-030 are the same rule from two directions, that a correction is a new event pointing at an earlier
one and that a sealed batch never changes. Both are enforced in the schema, so a careless query cannot break them.

**How it was checked:** from an empty database, twice. Migrations apply, sixteen tests pass, the second run skips all four
files. Tests 6, 7, 8 and 13 through 15 were written first and run against the previous schema, where they failed.

**Standards:** plural names, uuid keys, evidence_file_id, drizzle/ for migrations, the F11 guard refusing anything that is
not a local *_test database, single worker per section 2.5.

**One decision I would like your view on.** DATA-RULES.md says demo data is deleted 30 days after the review, so a trigger
that refuses every delete makes one of our own rules impossible to keep. The trigger allows a delete only when the session
sets eri.purge to on, and every delete it allows is recorded in purge_log. The alternative is no door at all and the purge
run as a psql session that disables triggers by hand. I picked the recorded door.

**Known limits, named rather than hidden.**
- The owner is a superuser, and a superuser can disable a trigger or drop one. Deployment should migrate as a
  non-superuser owner role, with the app connecting as eri_app and never as the owner.
- The purge has to connect as the owner, because only the owner can write purge_log. A security definer function would let
  a purge-only role work; that is Monday's decision, not tonight's.
- The "is the door open" test only ever sees a local test database, by design of F11. On the Mac mini that check belongs in
  a health check or the purge script's preflight.
- The purge script is not written. It must delete seal_events, then seals, then events, then evidence_files, in that order.

**REQ numbers:** partial for REQ-020, and REQ-030. REQ-048 is in the v0.4 amendments and is not in this repository yet, so
it is not cited.
```

Reviewer: Marvin. Assignee: yourself. Then stop pressing buttons.

# The handoff note, in notes/

`notes/2026-11-20-olusanya.md`

```
Done: event store live in schema, four migrations, sixteen tests, append-only enforced by grants and triggers, purge recorded.
Next: the three adapters with the sample one first, then the postcode format check that needs no network.
Blocked: nothing. Open questions for Marvin: the recorded purge door, the deployment owner role, and the v0.4 amendments.
```

# Then the two messages

Marvin, the password: `ENGAGEMENT/2026-11-20_dm_marvin-the-password.md`, unsent as far as anything here shows. Send it
before the pull request lands in his inbox.

Marvin, the pull request: the link, one line saying it is green and what you would most like him to look at, which is the
purge door. Nothing more.

# Tomorrow

The anchor probe first, dry run, because it is twenty minutes and it decides whether cycles three and four survive. Then the
three adapters, sample first. No screens, no capture, no sealing, no certificate before Monday afternoon.
