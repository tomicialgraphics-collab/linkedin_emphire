---
deliverable: internal
id: 2026-11-20_prompt-0003-the-door-and-the-record
date: 2026-11-20
audience: internal
status: ready
title: Nine tests pass, the door is too wide, and the purge has to leave a mark
time_checked: >-
  checked: 2026-11-20 18:06 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer, who will read the pull request rather than the session. The one decision that
  needs his view, the purge door, is written into the body as a question with the alternative named.
premise_checked: >-
  checked: the nine passing tests and the six remaining objections are the agent's report of 6:04 PM. The purge rule is
  from DATA-RULES.md as pasted on 20 November. The claim that a unique key in either column order satisfies a composite
  foreign key is the agent's, tested against the database, and this file takes it as correct because it says it ran.
sources_read: >-
  read: the agent's report of 6:04 PM. No page opened.
---

# What 0003 does, and why only three lines of it matter

The door was too wide: with `eri.purge` on, an update was allowed and a truncate was allowed. A purge only ever needs to
delete, so 0003 narrows the door to the `DELETE` branch and leaves update and truncate refused even with the flag set.

The second change is the one worth defending to Marvin. A purge removes the record, so the purge itself has to leave one.
Every deleted row writes a line into `purge_log` with the table, the row id, the time and the user. That way "we deleted
demo data after the review" is a claim with evidence behind it, which is the same standard the product holds other people
to.

The third is a one-line deletion of a duplicate index the agent found.

# The migration

`drizzle/0003_purge_door.sql`

```sql
/* The door opens for DELETE only, and every purge leaves a record of what it removed. */

create table purge_log (
  id         bigserial primary key,
  table_name text not null,
  row_id     text,
  purged_at  timestamptz not null default now(),
  purged_by  text not null default current_user
);

grant select, insert on purge_log to eri_app;
grant usage, select on sequence purge_log_id_seq to eri_app;

create or replace function eri_append_only() returns trigger language plpgsql as $$
begin
  if tg_op = 'DELETE' and coalesce(current_setting('eri.purge', true), 'off') = 'on' then
    insert into purge_log (table_name, row_id) values (tg_table_name, old.id::text);
    return old;
  end if;
  raise exception '% on % refused: this table is append only. Only a delete, with eri.purge set to on, is allowed.',
    tg_op, tg_table_name using errcode = '42501';
end
$$;

alter table events drop constraint events_id_file_unique;
```

# Tests to add

10. with `eri.purge` on, `update events` is still refused with 42501
11. with `eri.purge` on, `truncate events cascade` is still refused with 42501
12. a delete with `eri.purge` on writes exactly one `purge_log` row naming the table and the id, and a refused delete writes none

Test 12 is the one that turns the purge from a private act into a recorded one.

# The prompt

```
All nine pass and all six objections are right. One more migration, then we ship this branch.

What you found about the door is the important one: a purge only needs to delete, so update and truncate stay refused even
with the flag set. And because a purge removes the record, the purge has to leave one, so every deleted row writes a line
into purge_log with the table, the id, the time and the user.

drizzle/0003_purge_door.sql, exactly this:

<paste the SQL above>

Tests to add:
  10. with eri.purge = 'on', update events is still refused with 42501
  11. with eri.purge = 'on', truncate events cascade is still refused with 42501
  12. a delete with eri.purge = 'on' writes exactly one purge_log row naming the table and the row id, and a refused delete
      with the flag off writes none

You were right about events_id_file_unique, so it is dropped, and seal_events_event_same_file still holds because the
unique (evidence_file_id, id) on events already satisfies it. If dropping it breaks that foreign key, stop and tell me
rather than adding an index back.

Then run from an empty database again: drop eri_test, create it, migrate, npm test, second migrate. Show all twelve.

Then stop, show git status and the diff, do not commit, and tell me only what is still wrong.
```

# The pull request body, for after the tests pass

```
The event store, and the proof that it cannot be rewritten.

**What changed:** three migrations and one test file. Tables evidence_files, events, seals and seal_events, all uuid keys,
plural names, foreign keys named evidence_file_id, in drizzle/ per the standards. Triggers refuse update, delete and
truncate on all four tables, for the owner as well as for eri_app. A seal can only name events from its own file. Twelve
tests, including a refusal with Postgres error codes rather than an assertion about the code.

**Why:** REQ-020 and REQ-030 are the same rule from two directions. A correction is a new event pointing at an earlier one,
and a sealed batch never changes. Both hold in the schema, so a careless query cannot break them.

**How it was checked:** from an empty database, twice. Migration applies, twelve tests pass, second run skips both files.
Four of the new tests were run against the previous schema first and failed there, including a truncate and a cross-file
seal that both went through.

**Standards:** plural names, uuid keys, evidence_file_id, migrations in drizzle/, F11 guard in the test file, single worker
per section 2.5.

**One decision I would like your view on.** DATA-RULES.md says demo data is deleted 30 days after the review, so a trigger
that refuses every delete makes one of our own rules impossible to keep. The trigger allows a delete only when the session
sets eri.purge to on, and every delete it allows writes a line into purge_log. The alternative is no door at all and the
purge runs as a psql session that disables triggers by hand. I picked the recorded door.

**Known limits, named rather than hidden.** The owner is a superuser today, and a superuser can disable a trigger, so
nothing in SQL stops one. Deployment should migrate as a non-superuser owner role. The purge script itself is not written
yet; it has to delete seal_events, then seals, then events, then evidence_files, and clear purge_log only on purpose.

**REQ numbers:** partial for REQ-020, and REQ-030. REQ-048 is in the v0.4 amendments and is not in this repository yet, so
it is not cited.
```

# Before you open it

Send Marvin the password message if it is still unsent. A pull request from you will land in his inbox tonight and the
first thing he should not be doing is discovering the closed PR #5 by himself.
