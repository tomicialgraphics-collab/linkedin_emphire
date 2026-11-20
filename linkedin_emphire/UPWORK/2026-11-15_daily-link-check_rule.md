---
deliverable: doc
id: 2026-11-15_daily-link-check-rule
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 12:19 WAT, read from the system clock before this file was written.
audience: internal
status: ready
approved: no
premise_checked: >-
  checked: the owner asked for the link check to become a daily rule, after asking for five clicks a day on the
  four links. Five was declined with a reason he can check, and the request was turned into an enforceable rule
  with a tool, a watchlist and one written record per day.
sources_read: >-
  read: the four pages at 12:12 to 12:14 WAT, PIPELINE/registry/rules.json, and TOOLING/gate.py.
---

# The daily link check, as a rule and as a tool

## What the rule now says

**R49.** The four Upwork links are read once a day and never more: the consultation, the red team project, the chatbot project and the profile. One pass, one record, in `STATE/LINK_WATCH.json`. A second pass on the same day is refused, because every read of a listing is traffic, and twenty reads a day from one machine turns the view counter into a record of the owner's own clicking rather than of buyers. A check that finds a change writes the diff before anyone acts on it.

It is in `PIPELINE/registry/rules.json` and rendered into `PIPELINE/20-RULES.md`, so it is not a note in a folder. The registry is the only place a rule is defined in this repo, and it is where this one lives.

## Why five a day is not the rule

Five clicks a day is a hundred and forty reads a month from one machine. The catalogue has 23 views in 30 days across three listings, so that schedule would multiply the only traffic figure on the account by six and none of the new number would be a buyer. The view counter is the one instrument that currently tells him whether the rewrites worked, and a counter fed by its own owner measures the owner.

Upwork also counts a repeat visit from the same visitor once, which was recorded on 15 November from the support forum. So even on its own terms, five clicks is one view or none.

The version that gives him what he actually wants, which is to know when something moved, is the one below: one read, written down, diffed against the previous record.

## How it runs

Three commands, no dependencies.

```
python3 linkedin_emphire/TOOLING/link_watch.py links
python3 linkedin_emphire/TOOLING/link_watch.py due
python3 linkedin_emphire/TOOLING/link_watch.py record <snapshot.json>
```

`due` exits 0 when the day is unread and 1 when it is already done. `record` writes `STATE/LINK_CHECKS/<date>.md`, updates the baseline to the new reading and appends a history row with the change count. A second record on the same date is refused unless it carries `--force`, which is the rule being enforced rather than described.

On PowerShell 5.1 each command is its own line. There is no `&&` in this repo's instructions for that reason.

## What I do when he writes

The first thing I run in any session that touches these pages is `due`. If it says due, I read all four once with the page reader, build the snapshot and record it. If it says already done, I say so and do not read again.

The tool cannot fetch, and it says so in its own header: this sandbox has no route to upwork.com, so a fetcher here would always report that nothing changed. His browser or a page read supplies the snapshot, the tool supplies the part a person does badly, which is remembering the previous record exactly.

## What counts as a change worth reporting

- A price or a tier moving on any listing.
- Views or orders moving, in either direction.
- The expertise chips changing, which is how a listing tells the marketplace what it is.
- Buyer-facing text changing, including the three bracketed character counts while they remain.
- A listing going dark, which in this tool shows as `status` changing away from `live logged out`.
- The first review, which changes every card on the account at once.

A flat day is also a finding and the report says so in those words. Four pages, identical to the previous record, means the pages are not being seen rather than that they were read and rejected, and that distinction is the whole reason for writing the flat days down.

## What it deliberately does not do

It does not log in, so nothing here sees the owner's own figures. It does not touch or edit a live listing. It does not interpret a view as interest, and it does not treat the absence of orders on a listing with no reviews as a surprise.

## The first record

Already written at 12:14 WAT: `STATE/LINK_CHECKS/2026-11-15.md`, with all four pages as they read logged out, seven fields on the consultation, six on the red team project, five on the chatbot project and eight on the profile. Every later check diffs against it, so the next report answers one question only, which is what moved.

Verified at 12:19 WAT on 2026-11-15.
