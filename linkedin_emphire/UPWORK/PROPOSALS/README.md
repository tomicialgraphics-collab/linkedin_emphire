# PROPOSALS, the register

One file per proposal, named `YYYY-MM-DD_client-or-jobtitle-slug.md`, mirroring the `OUTREACH/` convention on the
LinkedIn side. `./emphire upwork` reads this folder, so the front matter below is what turns a folder of documents into a
number.

## Front matter the tool reads

```
---
date: 2026-11-14
quoted: 600
connects: 12
status: sent
---
```

- `date` the day it was sent. A draft dated today is not a send.
- `quoted` the dollar figure in the proposal, as a number, no currency symbol and no commas.
- `connects` what Upwork charged to send it.
- `status` one of `draft`, `sent`, `reply`, `interview`, `won`, `lost`, `skipped`. Anything starting `sent` or later is
  counted as sent; `won` is the only one that should become a row in `STATE/REVENUE-LOG.md`.

Older entries in this folder record the same facts as plain lines (`Date:`, `Connects:`). The tool reads both, so nothing
has to be rewritten to be counted.

## Below the front matter

Keep four things, in this order: the job post in the client's own words, the archetype from
`../templates/2026-11-13_four-archetype-proposals.md`, the proposal text exactly as sent, and the outcome with its date.
The outcome line is the only part that changes after the send, and it is the part the next week's targeting reads.

## The rule this folder exists for

A proposal that stays a draft costs nothing and earns nothing. The count that matters is not how many were written, it is
how many entered the market, and only the four fields above can tell the difference.
