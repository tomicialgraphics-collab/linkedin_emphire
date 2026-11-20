---
deliverable: dm
id: 2026-11-20_dm_marvin-the-rules-the-stack-and-the-phone-gate
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Marvin Percival
premise: >-
  Marvin has finished setting up the repository with protected main, no force-push, merge commits only and one approval
  per pull request, has asked for a view on decision 0001's move from FastAPI to Next.js, and has said he is stepping
  back from day-to-day coding. This reply accepts the stack decision with the two conditions that make it safe, asks the
  one question that decides what done means for cycle one, says how the requirements will be reconciled rather than
  duplicated, and leaves the company structure discussion for the call he proposed.
time_checked: >-
  checked: 2026-11-20 16:49 WAT, read from the system clock before this file was written. His message is stamped 4:20 PM
  in the thread as pasted.
profile_checked: >-
  Marvin Percival, the architect now, who has written the fixed rules and the defaults as separate things, who explicitly
  invites a decision note instead of a quiet change, and who has spent the day building the repository rather than talking
  about it. The reply answers the question he asked, in the order he asked it, and does not reopen anything he has settled.
premise_checked: >-
  checked: the four rules and the two additions are read from his message of 4:20 PM, not assumed. CLAUDE.md's phone and
  iPhone sentence was read in the file itself at 16:42. The stack in decision 0001 was read from the same CLAUDE.md tech
  stack section. Nothing here asserts what is in docs/ERI-Standards-v0_1.md, because it has not been read yet, and the
  reply says it will be read rather than describing it.
sources_read: >-
  read: CLAUDE.md, DATA-RULES.md and the file listing of DUNIN7/eri-test as pasted by the owner at 16:42 on 20 November.
  No page opened.
---

## Message, paste as is

<!-- gate:body:start -->
Good. That is the four rules I asked for plus two I had not thought of, and merge commits only is the right call, because a rebase rewrites the ID a note later points at.

On decision 0001 I would keep your call. Next.js with Drizzle is one runtime, one deploy and one auth surface on a Mac mini, and FastAPI beside a Next front end is two of each in exchange for nothing this product needs. Two conditions I would write into the note, not change the decision for: the NIPOST key and the fingerprint recomputation live in server code that never reaches the client, and the append-only grant on the event table is enforced in the migration rather than in the app.

One thing the rules do not cover, and it decides what done means for cycle one. The instructions file says a requirement is finished only when its criterion has been seen on the Android phone and the iPhone. Half of cycle one never reaches a screen: the event table, the revoke, the three adapters. Do you mean every requirement, or only the ones whose criterion names a device? Whichever you pick, I will put the sentence into the instructions file on the docs branch so the agent reads it on Saturday.

I will read the standards and the v0.4 draft tonight. If that draft is the scoped plan rather than the requirements, I will put my amendments in beside it in number order instead of creating a second v0.4 that disagrees with the first.

And noted on stepping back. I will bring you decisions and evidence rather than build steps. Send the structure proposal when it is ready and we will do it on a call rather than in messages.
<!-- gate:body:end -->
