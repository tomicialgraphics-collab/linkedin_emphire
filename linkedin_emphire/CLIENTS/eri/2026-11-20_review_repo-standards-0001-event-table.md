---
deliverable: internal
id: 2026-11-20_review_repo-standards-0001-event-table
date: 2026-11-20
audience: internal
status: ready
approved: no
title: The eri-test repository read before Monday, the standards, decision 0001 and the event table branch
time_checked: >-
  checked: 2026-11-20 18:48 WAT, read from the system clock in the sandbox before this file was written.
sources_read: >-
  read: DUNIN7/eri-test cloned into the session on 20 November at main a7021a3. Read in full: CLAUDE.md,
  docs/ERI-Standards-v0_1.md (147 lines), docs/decisions/0000 to 0002, and every file on feat/event-table at 733db7a
  (four migrations, the runner, the 16-test file, package.json, the handoff note). Also the ref list, the other three
  branches by diff, and closed pull request 5 with its one added line masked. No test was run, because the session has
  no Postgres.
---

# eri-test, read before Monday

What this is: the findings from reading the repository end to end on 20 November. Who it is for: the owner, before
cycle one starts on Monday 23 November. What to do next: settle items 1 to 3 with Marvin, then open the pull requests
in the order at the end.

The repository is private and belongs to DUNIN7. This file summarises it and quotes nothing longer than a line, because
this repository is public. Do not copy the standards, the requirements or the code in here.

## Before Monday

**1. F6 and the purge door disagree.** Fixed rule F6 says nothing is edited or deleted once fingerprinted, and fixed
rules do not move. Migrations 0002 to 0004 on `feat/event-table` open one deliberate door, delete only, when a session
sets `eri.purge` to on, for the 30-day purge that `DATA-RULES.md` asks for. The door is built well: every purge writes a
`purge_log` row, that log refuses update, delete and truncate, the app role cannot insert into it, and the app role has
no delete grant at all. It still breaks F6 as written. Marvin rules on it in writing, as a decision note or as a sentence
added to F6, before pull request 6 merges.

**2. Standards section 2.4 wants hash-chained audit rows, and the tables have no chain.** Each item carries its own
SHA-256, but no event names the one before it, so a removed or reordered event cannot be detected from the rows alone.
The tables refuse updates, so a chain column added after real rows exist can never be filled for them. This week is the
cheapest it will ever be.

**3. Which role the app connects as is undecided.** `eri_app` is a no-login role, so the app needs a login role that
belongs to it, and migrations run as the owner. If the Mac mini setup has the app connect as the owner, the grant layer
stops applying and only the triggers remain, and the owner can open the purge door. The handoff note lists it as an open
question. It belongs in `docs/DEPLOYMENT.md` with a test of the connected role.

**4. Decision 0001.** It is agreed by Marvin alone and open to a counter-proposal only before cycle one code starts. The
owner accepted it in the 16:51 message with two conditions. The written note is number 0003, because 0002 is taken
(where documents live). Its conditions: the NIPOST key only in server code, tested by searching the built page, the
responses and browser storage; one shared SHA-256 function for browser and server; Stele sessions verified on the server
by a signed token, with a test that a forged or expired one is refused; REQ v0.4 replaces the Tech Stack section. The
append-only condition is already met in `0001_event_store.sql`.

## Smaller gaps

- Commit label: `CHORE: event store` is requirement work and should carry its `REQ-NNN`.
- No task file in `docs/tasks/` and no report in `docs/reports/` for the event store, which CLAUDE.md requires.
- Naming, section 2.3: `purge_log` is singular with a `bigserial` key, and `sealed_at` and `purged_at` stand where
  `created_at` is the default. Minor, and cheaper now than after the tables are frozen.
- `package.json` carries a pasted line as its description, and there is no `tsconfig.json`, though the standard says
  TypeScript strict.

## What is right

- Sixteen tests, each inside a transaction that is rolled back, so the count cannot drop under F8.
- The F11 guard refuses any database not ending in `_test` on localhost, and names the database without the password.
- Update, delete and truncate are refused for the app role and for the owner; a seal cannot name another file's event;
  the purge log cannot be forged; and a test confirms no saved setting leaves `eri.purge` open.
- Sample data is labelled as invented, as CLAUDE.md and `DATA-RULES.md` require.
- Both commits are by `Teamthy` with the outbound address. Nothing outward carries the retired identity (R03).

## Branches and pull requests, as read at 18:40 WAT

| Ref | State |
| --- | --- |
| PR 4, `docs/done-definition` | Open. Puts Marvin's 16:51 sentence into CLAUDE.md. He said he would approve it tonight |
| PR 5 | Closed. One commit adding `.env` with a local database URL. The password was changed the same day. The commit stays fetchable by anyone with repo access until GitHub Support purges it |
| PR 6, `feat/event-table` | Open. Waits on item 1 |
| `claude/adoring-babbage-jng35n` | A phased build plan by an agent signed only "Claude", branched before PR 3, no pull request. Moves files back to the old layout. Ask whose it is; do not merge as it stands |
| `setup/first-files`, `docs/claude-md-and-deploy-plan` | Already merged |

## For the structure call, not for Monday

Decision 0002 keeps a copy of every Ẹ̀rí document in `dunin7-docs`, standards section 4 sends good ideas into the DUNIN7
standards, and the repository sits in DUNIN7's account. That is three places where work for the 51 to 49 company flows
into DUNIN7. Raise it when his structure proposal arrives, with the joint organisation the owner proposed at 16:52.

## Order of work, each through a pull request the owner sees before it is pushed

1. REQ v0.4: REQ-052 (sample label), REQ-053 (a file that matches nothing anywhere), and the Tech Stack section. Promised
   to Marvin for the weekend.
2. Decision 0003, the four conditions.
3. A note on F6 and the purge door, for Marvin to rule on.
4. The hash chain migration, written test first, on its own branch.
