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
| 2026-11-13 | Agent authorization test pass, scope not yet set | InvisibleAct (Kuldeep Patil) | 0 | prospect | Warm inbound: he read the comment on his post and asked on 13 Nov what I would try to break first in a pre-execution gate. Answered in a DM with four tests and an offer to run them against his n8n setup. No price discussed. |
| 2026-11-13 | Four-scenario gate test, one week | InvisibleAct (Kuldeep Patil) | 1500 | proposed | Sent 13 Nov after he asked for terms. Isolated n8n, synthetic invoices, report plus re-runnable requests, invoice on delivery. A $600 two-scenario option offered in the same message. |
| 2026-11-13 | Independent pass on NeoMundi Evidence, one week | NeoMundi (Sébastien Favre) | 1500 | proposed | First pass already done and reported free: corpus digests check, 40 PASS and 10 ambiguous, two failure-path defects named. Price stated 13 Nov for the full week. |
| 2026-11-13 | Independent pass on NeoMundi Evidence, declined | NeoMundi (Sébastien Favre) | 1500 | lost | Declined 13 Nov, 18:36: self-funded, no budget for external audits. Public write-up offered at no fee, with his review and right of reply. Two fix suggestions offered as patches. |

## How to add a row

Append above the separator line and keep the columns. A deal that moves state gets a new row rather than an
edit, so the history of the ask is visible: a `proposed` row followed by a `won` row is how you learn whether
your price is landing, and an edited row teaches nothing.
