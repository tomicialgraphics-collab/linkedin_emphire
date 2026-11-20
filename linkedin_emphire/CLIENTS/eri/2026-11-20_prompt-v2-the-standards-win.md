---
deliverable: internal
id: 2026-11-20_prompt-v2-the-standards-win
date: 2026-11-20
audience: internal
status: ready
title: The four answers the agent asked for, and the prompt that follows the standards instead of my plan
time_checked: >-
  checked: 2026-11-20 17:28 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, whose standards file turns out to specify migration location, table naming, key types and foreign key
  naming, and whose fixed rule F11 says tests must refuse to run against production. This file changes the plan to match
  his defaults rather than asking for a decision note on four naming questions.
premise_checked: >-
  checked: the eight contradictions and six schema objections are the agent's, from its stop report at 5:25 PM, and they
  are taken as correct because each one is checkable in a file that was read. Nothing here asserts what the standards say
  beyond what that report states. The package.json is the one the owner created at 17:05 with npm init and npm i, which is
  why Drizzle is in it: it is not a mystery file.
sources_read: >-
  read: the agent's stop report of 5:25 PM as pasted. No page opened.
---

# The four answers

**1. Follow the standards, not my plan.** Table names plural, keys uuid, foreign keys named `evidence_file_id`,
migrations in `drizzle/`. The plan I wrote was drawn before the standards were read, and none of those four choices carry a
reason worth a decision note. Rename and move.

Keep the two things the plan got right that the standards do not speak to, because they are additions rather than
departures: the trigger that refuses a rewrite even for the table owner, and the join table that stops a seal from naming
an event twice or an event from another file.

**2. REQ-048 is not a typo, but it is not in the repository.** It is one of the v0.4 amendments, REQ-046 to REQ-053, which
live in this workspace and arrive as the pull request Marvin asked for. Until that merges, the agent is right: a commit
message naming REQ-048 claims a requirement that does not exist in `docs` yet. Commit it as `CHORE:`, and put the mapping
in the pull request body as "partial for REQ-020", which is honest, because REQ-020 also wants a 403 and a screen and this
commit has neither.

**3. Add the F11 guard.** It is a fixed rule and fixed rules have no exceptions. The check is four lines in the test file
and it should fail loudly with the database name in the message.

**4. Yes, edit the existing package.json.** It is yours, from the `npm init` and `npm i` at 17:05 tonight. Drizzle being in
it is not a mystery and not a reason to look at it first. Commit `package.json` and `package-lock.json` as part of this
branch.

# What changes in the schema, and why each one

| The agent's objection | What the new schema does |
| --- | --- |
| `create role` stops the migration on a second database | created inside a `do` block that checks `pg_roles` first, so it runs on any number of databases in one cluster |
| the revoke does nothing | kept, and a trigger now refuses update and delete on `events` even for the table owner, so the property survives a future `grant all` and a psql session as postgres |
| `seal.event_ids` has no foreign key | replaced by `seal_events`, with a primary key so an event cannot sit in a seal twice and a foreign key so it cannot be an event from another file |
| `refers_to` can point into another file | composite foreign key on `(evidence_file_id, refers_to)`, which makes a cross-file reference impossible to store |
| a counter or withdrawal can have no `refers_to` | check constraint: item events have none, every other kind must have one |
| `fingerprint` can be empty | check constraint: an item's fingerprint must be 64 lowercase hex characters |
| seals recorded twice | `seal` is removed from the event kinds. A seal is the seal table and the join table, and there is one place for it |

That is eleven changes and every one of them is a constraint, not a feature. This is the commit where constraints are cheap.

# The migration, v2

`drizzle/0001_event_store.sql`

```sql
create table evidence_files (
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

create table events (
  id               uuid primary key default gen_random_uuid(),
  evidence_file_id uuid not null references evidence_files(id),
  seq              int  not null check (seq > 0),
  kind             text not null check (kind in ('item', 'attestation', 'counter', 'withdrawal')),
  refers_to        uuid,
  payload          jsonb not null,
  fingerprint      text,
  created_at       timestamptz not null default now(),
  created_by       uuid not null,
  unique (evidence_file_id, seq),
  unique (evidence_file_id, id),
  foreign key (evidence_file_id, refers_to) references events (evidence_file_id, id),
  constraint item_has_fingerprint
    check (kind <> 'item' or fingerprint ~ '^[0-9a-f]{64}$'),
  constraint reference_matches_kind
    check ((kind = 'item' and refers_to is null) or (kind <> 'item' and refers_to is not null))
);

create table seals (
  id               uuid primary key default gen_random_uuid(),
  evidence_file_id uuid not null references evidence_files(id),
  tx_id            text not null,
  block_time       timestamptz not null,
  sealed_at        timestamptz not null default now()
);

create table seal_events (
  seal_id  uuid not null references seals(id),
  event_id uuid not null unique references events(id),
  primary key (seal_id, event_id)
);

create function events_are_append_only() returns trigger language plpgsql as $$
begin
  raise exception 'events are append only, % refused', tg_op using errcode = '42501';
end
$$;

create trigger events_no_update before update on events
  for each row execute function events_are_append_only();
create trigger events_no_delete before delete on events
  for each row execute function events_are_append_only();

do $$
begin
  if not exists (select 1 from pg_roles where rolname = 'eri_app') then
    create role eri_app nologin;
  end if;
end
$$;

grant usage on schema public to eri_app;
grant select, insert on evidence_files to eri_app;
grant select, insert on events to eri_app;
grant select, insert on seals to eri_app;
grant select, insert on seal_events to eri_app;
revoke update, delete on events from eri_app;
```

No sequences to grant, because every key is now a uuid. That is one fewer permission to get wrong, and it is a second
reason the standards' default is the better one here.

# The tests, v2

Four behaviours, plus the fixed rule F11 guard at the top of the file:

1. the file refuses to run unless the connection string names a database ending in `_test` on localhost or 127.0.0.1
2. an update as `eri_app` is refused with 42501
3. a delete as `eri_app` is refused with 42501
4. an update as the table owner, connected as postgres, is refused with 42501 by the trigger
5. an insert as `eri_app` still succeeds and the row count goes up

Test 4 is the one that proves the claim in the commit title. Without it, the commit says the table cannot be rewritten and
what it proves is that one role cannot rewrite it.

# The prompt, v2, paste into Claude Code

```
Good stop, and every one of those is right. Here are the answers. Apply them and write the code.

1. Follow the repository standards, not my prompt, wherever they conflict: plural table names, uuid primary keys,
   foreign keys named evidence_file_id, migrations in drizzle/. Do not write a decision note for naming. Write nothing
   about Drizzle for now either: no repository code uses it in this commit, and the ORM arrives with the first query.
2. REQ-048 is one of the v0.4 amendments and is not in this repository yet. Do not cite it. Commit message will be
   CHORE:, and I will describe the REQ mapping in the pull request.
3. Yes, add the F11 guard.
4. Yes, edit the existing package.json. I created it tonight at 17:05 with npm init and npm i. Commit it and the lockfile.

The migration is drizzle/0001_event_store.sql, exactly this:

create table evidence_files (
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

create table events (
  id               uuid primary key default gen_random_uuid(),
  evidence_file_id uuid not null references evidence_files(id),
  seq              int  not null check (seq > 0),
  kind             text not null check (kind in ('item', 'attestation', 'counter', 'withdrawal')),
  refers_to        uuid,
  payload          jsonb not null,
  fingerprint      text,
  created_at       timestamptz not null default now(),
  created_by       uuid not null,
  unique (evidence_file_id, seq),
  unique (evidence_file_id, id),
  foreign key (evidence_file_id, refers_to) references events (evidence_file_id, id),
  constraint item_has_fingerprint
    check (kind <> 'item' or fingerprint ~ '^[0-9a-f]{64}$'),
  constraint reference_matches_kind
    check ((kind = 'item' and refers_to is null) or (kind <> 'item' and refers_to is not null))
);

create table seals (
  id               uuid primary key default gen_random_uuid(),
  evidence_file_id uuid not null references evidence_files(id),
  tx_id            text not null,
  block_time       timestamptz not null,
  sealed_at        timestamptz not null default now()
);

create table seal_events (
  seal_id  uuid not null references seals(id),
  event_id uuid not null unique references events(id),
  primary key (seal_id, event_id)
);

create function events_are_append_only() returns trigger language plpgsql as $$
begin
  raise exception 'events are append only, % refused', tg_op using errcode = '42501';
end
$$;

create trigger events_no_update before update on events
  for each row execute function events_are_append_only();
create trigger events_no_delete before delete on events
  for each row execute function events_are_append_only();

do $$
begin
  if not exists (select 1 from pg_roles where rolname = 'eri_app') then
    create role eri_app nologin;
  end if;
end
$$;

grant usage on schema public to eri_app;
grant select, insert on evidence_files to eri_app;
grant select, insert on events to eri_app;
grant select, insert on seals to eri_app;
grant select, insert on seal_events to eri_app;
revoke update, delete on events from eri_app;

The runner reads drizzle/*.sql in filename order, records applied names in schema_migrations, applies each file in its own
transaction, and exits non zero on failure. Keep it in drizzle/migrate.mjs. It is temporary and I will say so in the pull
request: it exists so the schema can be written by hand, and drizzle-kit takes over when the first query does.

Tests, five behaviours, all against the real Postgres, connecting once in beforeAll, each test in begin and rollback:
  1. F11, refused to run unless the connection string names a database ending in _test on localhost or 127.0.0.1, with
     the database name in the error message
  2. update events as eri_app is refused with 42501
  3. delete from events as eri_app is refused with 42501
  4. update events as the table owner, still connected as postgres, is refused with 42501 by the trigger
  5. insert into events as eri_app succeeds and the count goes up

Set the role in its own statement, set local role eri_app, never in the same string as the statement under test.

Seed data goes through the constraints: evidence_files wants postcode, address, address_source, source_captured_at,
created_by and agency_id. An event of kind item needs a 64 character lowercase hex fingerprint and no refers_to. Use a
value like 'a' repeated 64 times or sha256 of a fixed string, and say which you chose.

Run npm run db:migrate, npm test, then npm run db:migrate again to show the skip, then drop the database and run the
migration from empty to show it applies cleanly to a fresh one and that the role check does not trip a second time.

Then stop. Show git status and the full diff. Do not commit, do not push. Tell me the five test results, anything you
think is still wrong, and nothing else.
```

# After it returns

Commit as `CHORE: event store, append only, with the proof`, push, open the pull request with Marvin as reviewer, and put
in the body: the standards followed, the one departure (a hand runner instead of drizzle-kit, temporary), the REQ mapping
as partial for REQ-020, and the four constraints added beyond the plan with one line each on what they stop.
