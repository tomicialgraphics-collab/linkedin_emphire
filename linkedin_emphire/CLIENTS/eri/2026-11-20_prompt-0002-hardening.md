---
deliverable: internal
id: 2026-11-20_prompt-0002-hardening
date: 2026-11-20
audience: internal
status: ready
title: Five tests pass, six holes remain, and the purge rule decides how to close them
time_checked: >-
  checked: 2026-11-20 18:00 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer, who will read this pull request on a plane or tomorrow. Every choice that needs
  his agreement is named as a question in the pull request body rather than buried in SQL.
premise_checked: >-
  checked: the five passing tests and the six objections are the agent's report of 5:57 PM. The 30 day purge rule is from
  DATA-RULES.md as pasted on 20 November: demo data is deleted 30 days after the review, while fingerprints and anchor
  references stay. That rule is what makes a blanket trigger wrong, and it is the reason for the escape hatch below.
sources_read: >-
  read: the agent's report of 5:57 PM and DATA-RULES.md. No page opened.
---

# Say this much first

The commit is good. Five tests, a role check that survives a second database, and a report that named six holes rather
than declaring success. That is the pattern to keep.

Do not rewrite `0001`. It is applied. The fixes go in `0002` as an alter, which is what a migration is for, and it gives
Marvin a second, short file to review instead of asking him to re-read the first one.

# The one design question in here

`DATA-RULES.md` says demo data is deleted 30 days after a review, and fingerprints and anchor references stay. So something
must be able to delete events, and a trigger that refuses every delete makes that rule impossible to keep. The fix is a
deliberate door: the trigger allows a delete only when the session has set `eri.purge` to `on`, which a purge script does
explicitly and nobody does by accident.

That is a judgement call and it goes in the pull request body as a question, not as a footnote.

# The migration

`drizzle/0002_append_only_hardening.sql`

```sql
/* Close the three ways around the trigger, extend it to the seal batch, and leave one
   deliberate door for the 30 day purge that DATA-RULES.md requires. */

drop trigger events_no_update on events;
drop trigger events_no_delete on events;
drop function events_are_append_only();

create function eri_append_only() returns trigger language plpgsql as $$
begin
  if coalesce(current_setting('eri.purge', true), 'off') = 'on' then
    if tg_op = 'DELETE' then
      return old;
    end if;
    if tg_op = 'UPDATE' then
      return new;
    end if;
    return null;
  end if;
  raise exception '% on % refused: this table is append only. Set eri.purge to on only to delete demo data.',
    tg_op, tg_table_name using errcode = '42501';
end
$$;

create trigger events_no_update before update on events
  for each row execute function eri_append_only();
create trigger events_no_delete before delete on events
  for each row execute function eri_append_only();
create trigger events_no_truncate before truncate on events
  for each statement execute function eri_append_only();

create trigger evidence_files_no_update before update on evidence_files
  for each row execute function eri_append_only();
create trigger evidence_files_no_delete before delete on evidence_files
  for each row execute function eri_append_only();
create trigger evidence_files_no_truncate before truncate on evidence_files
  for each statement execute function eri_append_only();

create trigger seals_no_update before update on seals
  for each row execute function eri_append_only();
create trigger seals_no_delete before delete on seals
  for each row execute function eri_append_only();
create trigger seals_no_truncate before truncate on seals
  for each statement execute function eri_append_only();

create trigger seal_events_no_update before update on seal_events
  for each row execute function eri_append_only();
create trigger seal_events_no_delete before delete on seal_events
  for each row execute function eri_append_only();
create trigger seal_events_no_truncate before truncate on seal_events
  for each statement execute function eri_append_only();

/* A seal may only name events from its own file. Two composite keys, no application code. */
alter table events add constraint events_id_file_unique unique (id, evidence_file_id);
alter table seals  add constraint seals_id_file_unique  unique (id, evidence_file_id);

alter table seal_events add column evidence_file_id uuid not null;
alter table seal_events
  add constraint seal_events_seal_same_file
    foreign key (seal_id, evidence_file_id) references seals (id, evidence_file_id),
  add constraint seal_events_event_same_file
    foreign key (event_id, evidence_file_id) references events (id, evidence_file_id);
```

The superuser point is the one thing that cannot be fixed in SQL. A superuser can disable a trigger, so nothing in the
database can stop one. That belongs in the pull request body as a known limit with the fix named: deployment migrates as a
non-superuser owner role, and only the purge script runs with the purge flag. It also belongs in the decision note Marvin
suggested, if he wants one.

# Tests to add

6. `truncate events` as the owner is refused with 42501
7. `update seals` as the owner is refused with 42501
8. a seal whose `seal_events` row names an event from a different file is refused with 23503
9. with `set local eri.purge = 'on'`, a delete on events succeeds, which proves the door exists and is the only way through

Test 9 is the one that keeps the design honest. A rule with no documented way to do the legitimate thing gets worked around
in production by someone with a psql prompt at midnight.

# The prompt

```
All five pass and every one of your six objections is right. We are not editing 0001, because it is applied. The fixes go
in drizzle/0002_append_only_hardening.sql, as an alter, and 0001 stays exactly as it is.

Something you could not know: DATA-RULES.md says demo data is deleted 30 days after a review, so a trigger that refuses
every delete makes one of our own rules impossible to keep. The trigger therefore allows a delete only when the session has
set eri.purge to on. That is a deliberate door, and the purge script is the only thing that will open it.

The migration, exactly this:

<paste the SQL above>

Tests to add to the same file:
  6. truncate events as the owner is refused with 42501
  7. update seals as the owner is refused with 42501
  8. insert into seal_events an event from a different file is refused with 23503
  9. set local eri.purge = 'on', then delete from events succeeds, then rollback

Test 8 needs two files, one event each, a seal on the first file, and an attempt to put the second file's event in that
seal.

Then run the whole sequence again from an empty database: drop eri_test, create it, npm run db:migrate, npm test, and show
me every test result.

Then stop, show git status and the diff, and do not commit. Tell me only what you still think is wrong.
```

# Meanwhile, two things outside the code

**Close PR #5.** Tell the agent to close it without merging and leave the branch alone. It carries the old password, it has
been rotated, and an open pull request with a dead credential in it is a question waiting to be asked.

**Send Marvin the message tonight.** It is written and it is accurate now. A first report that arrives before he asks reads
as a system working. The same report after he asks reads as a problem found by chance.
