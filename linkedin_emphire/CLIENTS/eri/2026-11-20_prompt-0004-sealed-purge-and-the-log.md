---
deliverable: internal
id: 2026-11-20_prompt-0004-sealed-purge-and-the-log
date: 2026-11-20
audience: internal
status: ready
title: The purge cannot touch a sealed file, and the log is easier to fake than what it records
time_checked: >-
  checked: 2026-11-20 18:11 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer, who is about to receive a pull request rather than a session log. After 0004
  the branch is ready and the remaining limits are deployment rules, not schema rules.
premise_checked: >-
  checked: the twelve passing tests and the two new objections are the agent's report of 6:09 PM. The seal_events key
  problem is the agent's, found by running it: seal_events has no id column, so old.id fails with 42703. The fix is a row
  key derived from the row itself rather than a column that only four of the tables have.
sources_read: >-
  read: the agent's report of 6:09 PM. No page opened.
---

# Two fixes, and then it ships

The first is a bug, not a refinement: `old.id` does not exist on `seal_events`, so the 30 day purge fails on the first
table of a sealed file, which is most of them. The row key becomes whatever identifies the row: `id` where there is one,
and `seal_id:event_id` where there is not.

The second is the one that matters for the product's own argument. A log that anyone with an insert right can write, and
that the owner can delete, is not a record. So `purge_log` loses its insert grant for `eri_app`, and gains the same
never-rewrite triggers the other tables have, with no door of any kind.

And a test for the thing nobody can prevent: the door left open permanently with `alter database ... set eri.purge`. It
cannot be stopped, but it can be noticed, because the settings live in `pg_db_role_setting` and a test can assert that
nothing is there.

# The migration

`drizzle/0004_purge_and_the_log.sql`

```sql
/* A purge has to work on a sealed file, and the record of a purge has to be as hard to
   change as the thing it records. */

create or replace function eri_append_only() returns trigger language plpgsql as $$
declare
  row_key text;
begin
  if tg_op = 'DELETE' and coalesce(current_setting('eri.purge', true), 'off') = 'on' then
    row_key := coalesce(
      to_jsonb(old)->>'id',
      concat_ws(':', to_jsonb(old)->>'seal_id', to_jsonb(old)->>'event_id')
    );
    insert into purge_log (table_name, row_id) values (tg_table_name, row_key);
    return old;
  end if;
  raise exception '% on % refused: this table is append only. Only a delete, with eri.purge set to on, is allowed.',
    tg_op, tg_table_name using errcode = '42501';
end
$$;

revoke insert on purge_log from eri_app;

create function eri_never_rewrite() returns trigger language plpgsql as $$
begin
  raise exception '% on % refused: this table is a record and never changes.', tg_op, tg_table_name
    using errcode = '42501';
end
$$;

create trigger purge_log_no_update before update on purge_log
  for each row execute function eri_never_rewrite();
create trigger purge_log_no_delete before delete on purge_log
  for each row execute function eri_never_rewrite();
create trigger purge_log_no_truncate before truncate on purge_log
  for each statement execute function eri_never_rewrite();
```

# Tests to add

13. a whole sealed file purges in order, `seal_events`, `seals`, `events`, `evidence_files`, and the log gets one line per
    row, including `seal_events` with a `seal_id:event_id` key
14. a delete on `purge_log` is refused with 42501
15. `eri_app` inserting into `purge_log` is refused with 42501
16. `select count(*) from pg_db_role_setting` where any setting starts with `eri.purge` is zero, so the door is not standing
    open

Test 16 is the only defence available against the one thing SQL cannot prevent, and it belongs in the test file rather than
in a comment.

# The prompt

```
Both are right, and the seal_events one is a bug rather than a refinement. One more migration, then this branch ships.

drizzle/0004_purge_and_the_log.sql, exactly this:

<paste the SQL above>

Tests to add:
  13. a whole sealed file purges in order, seal_events, seals, events, evidence_files, and the log gets one line per row,
      including seal_events with a seal_id:event_id key
  14. a delete on purge_log is refused with 42501
  15. eri_app inserting into purge_log is refused with 42501
  16. no setting in pg_db_role_setting starts with eri.purge, which is how we notice if someone left the door open

Test 13 is the one that proves the 30 day rule in DATA-RULES.md can actually be kept for a sealed file, so make it a full
file: one item, one attestation, one seal, two seal_events rows, then purge.

Then run from an empty database again: drop eri_test, create it, migrate, npm test, second migrate. Show all sixteen.

Then stop, show git status and the diff, do not commit, and tell me only what is still wrong.
```

# After it passes

Commit, push, open the pull request with Marvin as reviewer, and use the body in
`2026-11-20_prompt-0003-the-door-and-the-record.md` with these four changes: sixteen tests not twelve, a paragraph on the
sealed-file purge and the log, the superuser limit kept, and a line saying the purge script is still to be written and what
order it must run in.

Then stop. It is quarter past six on a Friday, the branch is green, and the next thing that should happen to this code is
a review, not another migration.
