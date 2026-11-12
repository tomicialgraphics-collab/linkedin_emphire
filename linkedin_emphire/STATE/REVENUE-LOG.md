---
deliverable: internal
id: revenue-log
date: 2026-11-12
audience: internal
status: ready
approved: no
---

# Revenue log

One row per deal. `./emphire revenue` reads this table and nothing else, so a deal that is not a row does not
exist for the arithmetic.

States: `prospect` (talking, no number agreed), `proposed` (scope and price in writing), `won` (agreed, not yet
paid), `paid` (money received), `lost`, `free` (delivered at no fee, recorded so it is not mistaken for revenue).

| Date | Deal | Client | Amount USD | State | Note |
|---|---|---|---|---|---|
| 2026-10-24 | Action Gate review, seven findings | Arcezia (Praveen) | 0 | free | Fee waived in writing in the scope. The write-up is the asset, not the fee. |
| 2026-10-12 | Tutoring session plus Upwork booking | Sudhir | 90 | paid | About 83.50 net after the platform fee. The only money in the record. |
| 2026-11-12 | W-04 probe re-run, one week | FORAY (Marvin Percival) | 1500 | prospect | Scope drafted in REPLY-14, not yet sent. Price fixed, invoice on delivery, one revision included. |
| 2026-11-12 | Protocol anchoring review, six weeks unpaid | FORAY (Marvin Percival) | 0 | free | Case study permission granted, named, read-first. A paid engagement is a separate conversation and has not been had. |

## How to add a row

Append above the separator line and keep the columns. A deal that moves state gets a new row rather than an
edit, so the history of the ask is visible: a `proposed` row followed by a `won` row is how you learn whether
your price is landing, and an edited row teaches nothing.
