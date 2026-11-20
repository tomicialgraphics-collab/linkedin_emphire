---
deliverable: internal
id: 2026-11-20_day-one-what-to-build-first
date: 2026-11-20
audience: internal
status: ready
title: What to start with, in order, and what not to touch until Monday afternoon
sources_read: >-
  read: ERI-REQ-v0_3.pdf with its extracted text, the v0.4 amendments, and the cycle-one plan in this folder. No page
  opened.
---

# The short answer

Not the skeleton. Start with the four things that decide whether the skeleton is the right shape, then build it.

1. Run the anchor probe. `CLIENTS/eri/spike/anchor_probe.py`. Twenty lines of output that decide whether cycles three
   and four survive, and a JSON line that proves whatever it says.
2. Write the event table before any endpoint. It is the only decision in this build that is expensive to reverse.
3. Put the three outside services behind three adapters, and build the sample one first.
4. Only then the screens, and the translation and brand files before the first screen, not after.

# 1. The anchor probe, which you can run tonight

    cd CLIENTS/eri/spike
    python3 anchor_probe.py --url <FORAY endpoint> --dry-run
    python3 anchor_probe.py --url <FORAY endpoint>

It sends three known fingerprints, records the exact response with a sha256 of the body and the headers, and exits 2 if
no transaction id or block time came back. Add `--explorer https://.../tx/{tx}` and it will also fetch the explorer page
and record the status, which is the difference between "we got an id" and "a stranger can open it".

`--dry-run` writes nothing and sends nothing, so it is safe in a terminal with him watching.

The output file is `anchor-probe.jsonl`. Keep it, because in three weeks it is the difference between remembering what
FORAY said and knowing.

# 2. The event table is the build's spine

Everything in the requirements that matters is one rule: an item is never edited, and a correction, an attestation, a
counter-attestation or a withdrawal is a new event that points at an earlier one. If that lives only in application
code, one careless query breaks it. Put it in the schema and enforce it with a permission.

```sql
create table evidence_file (
  id                 uuid primary key default gen_random_uuid(),
  postcode           text not null,
  address            jsonb not null,          -- exactly what the source returned, unedited
  address_source     text not null,           -- 'sample' or 'live'   (REQ-052)
  source_captured_at timestamptz,             -- when the sample was recorded
  created_at         timestamptz not null default now(),
  created_by         uuid not null,           -- the Stele principal
  agency_id          uuid not null
);

create table event (                          -- append only
  id          bigserial primary key,
  file_id     uuid not null references evidence_file(id),
  seq         int  not null,                  -- per file, gapless, unique together
  kind        text not null,                  -- item | attestation | counter | withdrawal | seal
  refers_to   bigint references event(id),    -- the event being attested, corrected or withdrawn
  payload     jsonb not null,                 -- kind specific
  fingerprint text,                           -- sha256 of content, null for non items
  created_at  timestamptz not null default now(),
  created_by  uuid not null,
  unique (file_id, seq)
);

create table seal (
  id          bigserial primary key,
  file_id     uuid not null references evidence_file(id),
  event_ids   bigint[] not null,              -- exactly the items in this batch
  tx_id       text not null,
  block_time  timestamptz not null,
  sealed_at   timestamptz not null default now()
);
```

Then, and this is the part that answers REQ-020 and REQ-048 without a single line of application logic:

```sql
revoke update, delete on event from eri_app;
```

The application cannot mutate or remove an event even if it tries. A test that runs `update event` and gets a
permission error is worth more than a test that checks the UI hides a button, because the second one is a claim and the
first one is a fact.

# 3. Three adapters, sample first

    sources/     nipost_sample.py  |  nipost_live.py     one interface, chosen by config   (REQ-052)
    anchor/      foray.py                                the probe above, as a module
    auth/        stele.py        |  dev_session.py      until Stele mounts

Nothing in the core imports any of those three directly. Every one of them is unconfirmed: no NIPOST key, unknown
FORAY behaviour until Monday, and Stele unasked for the third time. If the core talks to an interface, the worst case is
a swapped implementation. If it talks to a service, the worst case is a rewrite in week three.

`dev_session.py` is a fifteen-minute stub, behind a flag that cannot be turned on in staging without an environment
variable that is not set there. It exists so a blocked Stele does not block the build, and it must be impossible to
mistake for the real thing.

# 4. The order after that

- The two translation sets and the brand file, before the first screen (REQ-002, REQ-003). Doing them afterwards means
  touching every screen twice.
- The postcode format check, which needs no network (REQ-005).
- The sample-backed lookup, then the three screens it feeds: valid, refused, unreachable (REQ-006 to REQ-009).
- The file creation, which is where the agency statement lands (REQ-010, REQ-050).

# What not to touch before Monday afternoon

Do not write the capture screens, the sealing code or the certificate. All three depend on an answer that arrives
Monday morning, and all three are cheap to write after it and expensive to rewrite before it.

Do not wire the app to a real FORAY endpoint with a real fee attached until the probe has been run in dry mode and then
once for real, because rate limits and charges are things we find out about deliberately.

And do not put anything in the repository until it is private. That is still the only item on the list that costs nothing
and is still open.
