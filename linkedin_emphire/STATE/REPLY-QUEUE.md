---
deliverable: doc
id: reply-queue
date: 2026-11-09
audience: internal
status: draft
---

# Reply queue

R38: a direct question from a reader is answered within a day, or acknowledged with the day it will be
answered. This file is where that promise is visible. A question with no row here is a question that
was never owed an answer, and that is a thing the owner should be able to check rather than take on trust.

## How a row works

`date received` is the day the question appeared. `date due` is the next day, or the next working day
where the question arrives on a Saturday or Sunday. `state` is `open`, `drafted` or `answered`, and
`answered` rows stay in the file for a week so the record shows the promise was kept rather than
edited away.

## Open

| date received | who | the question, in their words | date due | state | file |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Hitesh Choudhary | replied to the comment on his prompt post: confidence as a hypothesis to review, and isolating deletions by checking callers and tests | 2026-11-12 | open | not drafted |
| 2026-11-11 | Saim Saudagar | replied twice under the Replit post: error strings as input, and whoever triggers the error steering the fix | 2026-11-12 | open | not drafted |

Two inbound replies are open as of 12 November 2026. Both are substantive and both are owed an answer
within the day under R38.

## Threads where the other person holds the last word

Not owed a reply. Listed so a later session does not mistake silence for an unanswered question.

| who | thread | last move |
| --- | --- | --- |
| Sam Illingworth | whether to plan the study as a project | offered a one-page protocol; if he accepts, a design document is owed, not a message |
| Juliet Ugbor | preparedness and who carries the failure | ended on his day-four line; the next word is hers |
| Dr Martha Boeckenfeld | intent versus obligation | one reply given and the thread closed by design, per R34 |
| Evelyne-Claudia Yantony | the F9b record and its section 7 | closed on 10 November with her agreement that section 7 stays open pending the v3 archive; the next message from him is files or nothing |
| Marvin Percival | FORAY stream records | he owes the transaction id; nothing is owed to him |

## What the gate cannot do

R38 is a reading rule. No checker knows that somebody asked a question, so the row is written when the
question is read, which is the only moment it is cheap.
