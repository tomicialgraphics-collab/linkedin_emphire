---
deliverable: internal
id: 2026-11-20_first-commit-the-event-table
date: 2026-11-20
audience: internal
status: ready
title: The first real commit, tonight, with no Next.js and no screens
time_checked: >-
  checked: 2026-11-20 17:12 WAT, read from the system clock before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer, who approves every pull request and asked for the REQ changes to arrive that
  way. Nothing here needs his approval to start, because it is one branch, one migration and one test.
premise_checked: >-
  checked: the three tables and the revoke statement are copied from the day-one plan in this folder, which was written
  from REQ v0.3 and the v0.4 amendments. The stack is decision 0001, Next.js, TypeScript strict, Drizzle, Vitest, but none
  of that is needed for this commit and adding it now would hide the schema behind a scaffold. The repo has no package.json
  at first clone, so the project starts here.
sources_read: >-
  read: CLIENTS/eri/2026-11-20_day-one-what-to-build-first.md, this folder. No page opened.
---

# Why not Next.js tonight

The plan says it plainly: not the skeleton first. Next.js, Drizzle and Vitest are decision 0001 and they will be there on
Monday. Tonight is the one decision in this build that is expensive to reverse, and it is three tables and one permission.
A scaffold built before the schema means the schema arrives as something a generator produced, and a wrong schema that
looks finished is the failure this project is about.

So this commit is: a package, a database, three tables written by hand, one test that proves the database refuses to let
the application rewrite history.

# 0. Check what is on the machine

```powershell
node --version
npm --version
docker --version
```

Node 20 or newer. Docker Desktop installed and started, which is how Postgres arrives without installing anything else.
The test below needs a real Postgres with real roles, and no in-memory database can prove a permission.

On this laptop Docker was installed but the engine was not running, and every command failed with a named-pipe error that
reads like a broken install. Start Docker Desktop, wait for `docker ps` to answer, and only then run the container.

There is already a container on this machine called `nuvora-prod-postgres-1`. It does not publish its port, so it does not
collide with the one below, but it does mean one habit matters: name the container in every command that touches a
database. `docker exec eri-pg psql` and never a bare `psql`, and never `drop database` against anything you have not just
confirmed is called `eri_test`.

# 1. Branch

```powershell
cd "$env:USERPROFILE\Desktop\PROJECTS\eri-test"
git switch main
git pull --ff-only
git switch -c feat/event-table
```

# 2. A small package, no framework

```powershell
npm init -y
npm i drizzle-orm pg
npm i -D typescript tsx vitest @types/pg @types/node
```

# 3. Postgres in Docker

```powershell
docker run -d --name eri-pg -e POSTGRES_PASSWORD=eri_dev -e POSTGRES_DB=eri_test -p 5432:5432 postgres:16
docker ps --filter name=eri-pg
```

`eri_dev` is a password for a container on one laptop holding no real data. It is not a key and it must never be reused
for staging. `DATA-RULES.md` bars real data, not a local database password.

If port 5432 is already taken by another Postgres, use `-p 5433:5432` and change the port in the string below.

# 4. The connection string, not committed

Create `.env.local` in the repository root:

```
DATABASE_URL=postgres://postgres:eri_dev@localhost:5432/eri_test
```

`.gitignore` already excludes `.env*`. Confirm with `git status` after writing it: if `.env.local` shows up as an untracked
file, stop and fix `.gitignore` before going further.

# 5. The migration, written by hand

`db/migrations/0001_event_store.sql`

```sql
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

/* The application role. NOLOGIN on purpose: the test switches into it rather than
   holding a second password anywhere, and the day it needs to log in it gets one. */
do $$
begin
  if not exists (select 1 from pg_roles where rolname = 'eri_app') then
    create role eri_app nologin;
  end if;
end
$$;

grant usage on schema public to eri_app;
grant select, insert on evidence_file to eri_app;
grant select, insert on seal to eri_app;
grant select, insert on event to eri_app;
grant usage, select on sequence event_id_seq to eri_app;
grant usage, select on sequence seal_id_seq to eri_app;

revoke update, delete on event from eri_app;
```

What actually enforces the rule is the grant list: `eri_app` is given select and insert and nothing else, so an update is
refused for want of a privilege rather than for want of a rule. The `revoke` line is a guard for later, the day someone
adds `grant all on event to eri_app` to fix an unrelated problem and quietly removes the whole property. It costs one line
and it makes that mistake fail loudly instead of silently.

Three additions beyond the plan's version, each one a decision you can defend or drop, and none of them generated:
`check (address_source in ('sample','live'))` because REQ-052 makes that field load-bearing; `sample_needs_capture_time`
because a sample with no capture date cannot be trusted as a sample; `check (seq > 0)` and the kind list because a typo in
a kind string should fail at the database, not silently become a sixth event type.

# 6. A tiny migration runner

`db/migrate.mjs`

```js
import { readFileSync, readdirSync } from 'node:fs'
import { join } from 'node:path'
import { Client } from 'pg'

const dir = join(process.cwd(), 'db', 'migrations')
const client = new Client({ connectionString: process.env.DATABASE_URL })
await client.connect()

await client.query(`create table if not exists schema_migrations (
  name text primary key,
  applied_at timestamptz not null default now()
)`)

const done = new Set((await client.query('select name from schema_migrations')).rows.map(r => r.name))

for (const file of readdirSync(dir).filter(f => f.endsWith('.sql')).sort()) {
  if (done.has(file)) { console.log('skip', file); continue }
  console.log('apply', file)
  await client.query('begin')
  try {
    await client.query(readFileSync(join(dir, file), 'utf8'))
    await client.query('insert into schema_migrations (name) values ($1)', [file])
    await client.query('commit')
  } catch (err) {
    await client.query('rollback')
    throw err
  }
}

await client.end()
```

Run it with `node --env-file=.env.local db/migrate.mjs`. Node 20 reads that flag; if it complains, use
`npm i -D dotenv` and import it instead.

# 7. The test that matters

`tests/event-append-only.test.ts`

```ts
import { describe, it, expect, beforeAll, afterAll } from 'vitest'
import { Client } from 'pg'

const client = new Client({ connectionString: process.env.DATABASE_URL })

beforeAll(async () => { await client.connect() })
afterAll(async () => { await client.end() })

async function seedEvent() {
  const file = await client.query(
    `insert into evidence_file (postcode, address, address_source, source_captured_at, created_by, agency_id)
     values ('100001', '{"line":"test only"}'::jsonb, 'sample', now(), gen_random_uuid(), gen_random_uuid())
     returning id`,
  )
  const fileId = file.rows[0].id
  await client.query(
    `insert into event (file_id, seq, kind, payload, created_by)
     values ($1, 1, 'item', '{"note":"test"}'::jsonb, gen_random_uuid())`,
    [fileId],
  )
  return fileId
}

describe('the event table refuses to be rewritten', () => {
  it('rejects an update from the application role', async () => {
    await client.query('begin')
    const fileId = await seedEvent()

    await client.query('set local role eri_app')

    await expect(
      client.query(`update event set kind = 'withdrawal' where file_id = $1`, [fileId]),
    ).rejects.toMatchObject({ code: '42501' })

    await client.query('rollback')
  })

  it('rejects a delete from the application role', async () => {
    await client.query('begin')
    const fileId = await seedEvent()

    await client.query('set local role eri_app')

    await expect(
      client.query(`delete from event where file_id = $1`, [fileId]),
    ).rejects.toMatchObject({ code: '42501' })

    await client.query('rollback')
  })

  it('still allows an insert from the application role', async () => {
    await client.query('begin')
    const fileId = await seedEvent()

    await client.query('set local role eri_app')
    await client.query(
      `insert into event (file_id, seq, kind, payload, created_by)
       values ($1, 2, 'attestation', '{"note":"second"}'::jsonb, gen_random_uuid())`,
      [fileId],
    )

    const { rows } = await client.query('select count(*)::int as n from event where file_id = $1', [fileId])
    expect(rows[0].n).toBe(2)

    await client.query('rollback')
  })
})
```

Three things about that file that will bite anyone who writes it differently.

`set local role` goes in its own call, never in the same string as the statement under test. Node's `pg` switches to the extended protocol as soon as a query has parameters, and the extended protocol refuses two commands in one string, so the combined version fails with a message about a prepared statement that has nothing to do with permissions.

The client connects once, in `beforeAll`. Calling `connect()` again inside a test throws, and the error looks like a database problem when it is a test problem.

Every test opens a transaction and rolls it back, so the database is left as it was found and the tests can run in any order, as many times as you like.

The third test is there for a reason. Two tests that prove a refusal can both pass on a database where the role has no rights at all, which would mean the application cannot write a single event. One test that proves the insert still works is what separates "the door is locked" from "the door was never installed".

# 8. Wire the test script and run it

In `package.json`, add:

```json
"scripts": {
  "db:migrate": "node --env-file=.env.local db/migrate.mjs",
  "test": "node --env-file=.env.local ./node_modules/vitest/vitest.mjs run"
}
```

```powershell
npm run db:migrate
npm test
```

Expect: migration applied once, then three tests passing. Delete the database and run the migration again
(`docker exec -it eri-pg psql -U postgres -c "drop database eri_test" -c "create database eri_test"`) to prove it runs from
nothing, because a migration that only works on a database it already touched is not a migration.

# 9. Commit and open the pull request

```powershell
git add package.json package-lock.json db tests .gitignore
git commit -m "REQ-048: the event table, append only, enforced by a revoked grant"
git push -u origin feat/event-table
```

Then the pull request, with Marvin as reviewer:

```
The event table, written by hand from the day-one plan.

**What changed:** three tables, evidence_file, event and seal. An eri_app role with select and insert only. The migration
revokes update and delete on event, so the application cannot rewrite history even if the code tries.

**Why:** REQ-020 and REQ-048 are the same rule, that a correction is a new event pointing at an earlier one. Enforcing it
in the database means a careless query cannot break it.

**How it was checked:** three tests. An update as eri_app fails with 42501, a delete fails with 42501, and an insert still
succeeds. Dropped the database and re-ran the migration to prove it applies from nothing.

**REQ numbers:** 020, 048, and part of 052 for the sample capture time.

**Deliberately not done:** no Next.js, no Drizzle client, no screens. Decision 0001 arrives with the first endpoint.
```

# What is next, and what is not

Next, in order: the anchor probe in dry mode, which is twenty minutes and decides whether cycles three and four survive;
then the three adapters with the sample one first; then the translation and brand files before any screen.

Not tonight: capture, sealing, the certificate. Monday afternoon, after the FORAY answer arrives.
