---
deliverable: internal
id: 2026-11-20_prompt-for-claude-code
date: 2026-11-20
audience: internal
status: ready
title: The prompt to give Claude Code for the first commit, and the template for every one after it
time_checked: >-
  checked: 2026-11-20 17:24 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, whose instructions file the agent must obey: one branch per task, tests from acceptance criteria
  first, no commits to main, handoff note every session. Claude Code v2.1.329 is what is installed, in auto mode.
premise_checked: >-
  checked: the DDL inside the prompt is the version from the day-one plan with the three added constraints, and it is
  copied here so the agent is not asked to design a schema. The test behaviours are the three in the corrected test file.
  The claim about the extended protocol is from the pg driver's own behaviour, and it was the cause of the bug in the first
  version of the test.
sources_read: >-
  read: this folder's day-one plan and first-commit file. No page opened.
---

# Why one prompt cannot be perfect

A prompt is perfect when the agent cannot silently make a wrong decision inside it. That means the two things an agent is
worst at have to be decided before it starts: the schema, and what counts as proof. Everything else, the file layout, the
runner, the failing tests, is work it does better than a person at a keyboard.

So the prompt below hands over the part that is judgment and withholds the part that is invention. It is for tonight's
commit. After it, use the template at the bottom, with the schema line replaced by whatever decision that task turns on.

# The prompt, paste into Claude Code in the repo root

```
You are working in the eri-test repository. Before anything else, read CLAUDE.md and DATA-RULES.md in full, then read
docs/ERI-REQ-v0_3.md looking for REQ-020 and REQ-048, then skim docs/ERI-Standards-v0_1.md for anything that constrains
schema or testing. If any of those files contradict this prompt, stop and tell me before writing code.

Branch: feat/event-table. You are already on it. Do not switch branches, do not commit to main, do not force-push, do not
rebase. When you finish you stop before committing.

Your task, and it is the whole task: create the event store, and prove with tests that the application role cannot rewrite
history.

Scope. Create exactly these four files and change nothing else:
  db/migrations/0001_event_store.sql
  db/migrate.mjs
  tests/event-append-only.test.ts
  package.json (add two scripts only, db:migrate and test, leave every other field alone)

Do not create app/, do not install Next.js, do not install Drizzle, do not write a single screen or endpoint, do not touch
capture, sealing or the certificate. This commit is the database and its proof, nothing more.

The migration is given, not designed. Use this exactly:

create table evidence_file (
  id                 uuid primary key default gen_random_uuid(),
  postcode           text not null,
  address            jsonb not null,
  address_source     text not null check (address_source in ('sample', 'live')),
  source_captured_at timestamptz,
  created_at         timestamptz not null default now(),
  created_by         uuid not null,
  agency_id          uuid not null,
  constraint sample_needs_capture_time
    check (address_source = 'live' or source_captured_at is not null)
);

create table event (
  id          bigserial primary key,
  file_id     uuid not null references evidence_file(id),
  seq         int  not null check (seq > 0),
  kind        text not null check (kind in ('item', 'attestation', 'counter', 'withdrawal', 'seal')),
  refers_to   bigint references event(id),
  payload     jsonb not null,
  fingerprint text,
  created_at  timestamptz not null default now(),
  created_by  uuid not null,
  unique (file_id, seq)
);

create table seal (
  id          bigserial primary key,
  file_id     uuid not null references evidence_file(id),
  event_ids   bigint[] not null,
  tx_id       text not null,
  block_time  timestamptz not null,
  sealed_at   timestamptz not null default now()
);

create role eri_app nologin;
grant usage on schema public to eri_app;
grant select, insert on evidence_file to eri_app;
grant select, insert on event to eri_app;
grant select, insert on seal to eri_app;
grant usage, select on sequence event_id_seq to eri_app;
grant usage, select on sequence seal_id_seq to eri_app;
revoke update, delete on event from eri_app;

The runner db/migrate.mjs connects with process.env.DATABASE_URL, creates a schema_migrations table if it is missing,
and applies every .sql file in db/migrations in filename order inside a transaction, recording each name after it commits.
If a migration throws, roll back and exit non zero. No ORM, no library beyond pg.

The tests are also given, behaviourally. Write three Vitest tests against a real Postgres using pg, connecting once in
beforeAll, each test inside begin and rollback so nothing persists:
  1. an update on event as eri_app is refused with Postgres error code 42501
  2. a delete on event as eri_app is refused with 42501
  3. an insert into event as eri_app still succeeds, and the row count goes up
Put the database into the application role with a statement of its own, set local role eri_app, never in the same string as
the statement under test: with a parameterised query the driver uses the extended protocol and rejects two commands in one
string, and the error it gives has nothing to do with permissions.

The third test is not optional. Two tests that only prove refusal would pass on a database where eri_app can write nothing
at all.

Run it like this and paste me the output: npm run db:migrate, then npm test. Then run npm run db:migrate a second time and
confirm it skips the file it already applied.

Then stop, show me git status and the full diff, and wait. Do not commit. Do not push. Do not open a pull request.

In your reply tell me only: the three test results, whether the migration ran twice cleanly, anything in CLAUDE.md or the
REQ document that this prompt contradicts, and anything you think is wrong with the schema above. If you think a
constraint is wrong, say so plainly and do not change it.
```

# What to do with what comes back

Read the diff. Three files and two scripts, nothing else. If it touched `app/`, a lockfile for Next.js, or a screen, send it
back.

Then commit yourself and open the pull request with Marvin as reviewer. The commit message and PR body are in
`2026-11-20_first-commit-the-event-table.md`, sections 9 and 8.

# The template for every task after this one

```
Read CLAUDE.md and DATA-RULES.md first. Read the acceptance criteria for <REQ numbers> in docs and quote them to me
verbatim before you write anything. If a criterion is missing or ambiguous, stop and ask.

One branch, <branch name>. Do not commit to main, do not force-push, do not rebase.

Scope: <the files, or the one behaviour>. Nothing else. Do not refactor, do not reformat, do not tidy files you were not
asked about.

<The part that is judgment: the schema, the interface, the exact wording, the grant. Given, not designed.>

<The part that is proof: the tests that must exist and the command that shows them passing.>

Write the tests first, run them, show me they fail, then implement until they pass.

Then stop. Show git status and the diff. Do not commit.

Tell me only: test results, contradictions with CLAUDE.md, and anything you think is wrong with what I gave you.
```

The last line is the one that earns its place. An agent that is told to disagree finds real problems, and one that is told
to comply reports success. The stack decision survived scrutiny because it was argued with, and the event table should get
the same treatment.
