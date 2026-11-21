---
deliverable: dm
id: 2026-11-21_dm_marvin-saturday-plan
date: 2026-11-21
audience: outbound
status: sent
approved: yes
recipient: Marvin Percival
warm: yes
premise: >-
  The owner wants to work on Saturday 21 Nov 2026 and asked for a message to Marvin. On DUNIN7/eri-test, PR 6, 7 and 8
  are open and waiting on Marvin's review, and PR 9, the security plan, is a draft. The PRD says to test FORAY
  anchoring before any other code, and that has not been done. The message lists what waits on him, in order, and
  what the owner does today.
time_checked: >-
  checked: 2026-11-21 07:45 WAT, read from the system clock in the sandbox before this file was written.
profile_checked: >-
  Marvin Percival, architect and reviewer on Ẹ̀rí, who writes short, reads closely and asked for numbered steps when he
  has to act. The message gives him numbered steps and keeps the owner's own work as a short list.
premise_checked: >-
  checked: DUNIN7/eri-test pull requests listed through GitHub on 21 Nov 2026: 6, 7 and 8 open and not merged, 9 open
  as a draft. PRD v0.2 section 11, risk three, says test anchoring first. DATA-RULES.md bans voice recordings of real
  people. Both read on main at 4888b86.
sources_read: >-
  read: the eri-test pull request list, PRD v0.2 and DATA-RULES.md, 21 Nov 2026.
---

## Before sending

Send the password message first if it has not gone yet. This one can follow straight after.

## Message

<!-- gate:body:start -->
Morning Marvin. I know it's Saturday, but I'd like us to keep moving. Here's what's waiting on you and what I'm doing today.

Waiting on you, in this order:

1. PR 7, decision 0003. Once you're happy with it I'll rework PR 6 on top of it.
2. PR 8, REQ v0.4.
3. The FORAY anchoring test. The PRD says to test anchoring before any other code, and we haven't yet. Could you anchor one fingerprint and send me the transaction ID? If it opens on the explorer, cycles 3 and 4 hold.
4. The Stele 23-case table, so I can write the recovery tests.
5. A short written scope for what I'm allowed to test on the Mac mini. It's step 0 in PR 9, the security plan, which is a draft for you to read.

What I'm doing today:

- The threat model, as a PR.
- Task files for cycle 1, so whoever picks up next knows what to build.
- A decision note on the demo voices and photos. The data rules ban recordings of real people, and the demo needs a grandmother's voice, so we need to pick: one of us or an actor with written consent, or a synthetic voice.
- A note for a development sign-in, in case Stele isn't mounted this week.

If the order's wrong for you, tell me and I'll switch it.
<!-- gate:body:end -->
