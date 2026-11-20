---
deliverable: dm
id: 2026-11-20_dm_marvin-decision-0001-in-and-reading
date: 2026-11-20
audience: outbound
status: superseded
approved: no
recipient: Marvin Percival
warm: yes
premise: >-
  Drafted in the session as the answer to Marvin's 16:20 message (the repository is up, decision 0001, the v0.4 pull
  request). The owner answered himself at 16:51 before this draft was seen, covering the same ground with two of the
  four conditions. Kept so the record shows what was proposed and why it was not used.
time_checked: >-
  checked: 2026-11-20 18:48 WAT, read from the system clock in the sandbox before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer on Ẹ̀rí from 20 November, who invited a counter-proposal on 0001 before code
  starts and asked for the REQ changes as a pull request.
premise_checked: >-
  checked: REQ v0.3 names Python with FastAPI for the server, and decision 0001 replaces it with Next.js, TypeScript,
  Drizzle and Vitest. Both read in DUNIN7/eri-test on 20 November.
sources_read: >-
  read: Marvin's 16:20 message and the repository it links, 20 November.
---

## Superseded by the owner's own 16:51 message. Do not send.

What he sent is recorded in `CLIENTS/eri/2026-11-20_thread_linkedin-marvin.md`. The two conditions he did not include,
one shared hash function and server-side Stele session checks, go into decision note 0003 instead of a message.

## Message, as drafted

<!-- gate:body:start -->
Thanks Marvin, I'm in. I'll read the README and the standards over the weekend and send any changes as decision notes.

On 0001 I'm happy with Next.js, TypeScript, Drizzle and Vitest. It lets the phone and the server share one fingerprint
function, which REQ v0.3 needs anyway. I'll write a short note with four conditions: the NIPOST key in a server-only
module with a test that looks for it in the built page, the revoke on the event table in the first migration, the shared
hash function, and the Tech Stack section of the REQ updated in the v0.4 pull request so the document and the code agree.

I'll open the v0.4 pull request before Monday. Looking forward to the structure proposal, and a call on it works for me.
<!-- gate:body:end -->
