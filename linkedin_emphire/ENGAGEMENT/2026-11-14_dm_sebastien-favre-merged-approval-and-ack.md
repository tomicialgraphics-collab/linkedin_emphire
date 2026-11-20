---
deliverable: dm
id: 2026-11-14_dm_sebastien-favre-merged-approval-and-ack
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:49 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: vendor
status: ready
approved: no
warm: yes
profile_checked: >-
  Sébastien Favre is waiting on one decision and has just published a recommendation. He merges only
  with approval and said so at 10:45, and the recommendation went up before he heard back, so both
  threads are open with the same person and both are about attribution. Sending two long messages in an
  hour would read as admin; one message that answers the blocking question first and the public one
  second reads as a person.
premise_checked: >-
  checked: the draft pull request still returns 404 from here, so the approval remains conditional on
  three statements a reader can check in a minute rather than on wording that was read. The
  recommendation's account of the recheck matches Timothy's message of 06:43, and the one sentence that
  needs a correction is the strict-mode attribution, which the release notes themselves disprove.
  Nothing else in the recommendation is wrong, and nothing in this message claims the corpus was
  validated.
sources_read: >-
  read: the recommendation as pasted on 14 November, the thread messages of 10:45 and 10:48, and
  Timothy's message of 06:43 which carries the recheck numbers. No repository was opened.
---

## DM, paste this

<!-- gate:body:start -->
Two things in one message, since both are about who gets credit for what, and one of them is holding up your merge.

The draft. I still can't open it, because the repository gives me a 404 without access, so I haven't read the wording and I won't approve text I haven't seen. What I can approve is three statements you can check against your own body in a minute. One: this was a contract change, not a defect fix, and the interesting part is that incomplete and failed are different states. Two: the re-run was at 1.3.0, on the release rather than on my branch, which is what makes the acknowledgement accurate instead of generous. Three: credit isn't endorsement, so nothing in it says the review closed, validated or signed off on the corpus. If the body already does all three, merge it and treat this as the approval. If one's missing, send me the sentence and I'll approve the edit rather than the intention.

The recommendation. Thank you, and one correction I'd rather make now than leave sitting on your profile. The strict-mode value that no run had ever measured came out of your own release notes. I read them and propagated the flag, which is ordinary reviewing. Uncovering it was your work, done in public before I got there, so if you revise the recommendation that sentence should say I found it in your notes rather than that I found it. The rest stands, including the dependency diagnostics, because that one was mine.

What I'll do with it: cite it as your words about a review, not as an endorsement of the corpus. Those are different claims and the second one is yours to make. Anyone who reads it and then asks me for evidence gets the same answer as before, which is open items, the gap on the record, nothing closed.

I'm not sending one back this week. A recommendation published the same day as yours would read as a trade and would be worth less than the work it described. It goes out when the write-up is public, so the reason is the work and not the gesture.

The write-up follows regardless: both designs, both reasons, the disagreement attributed to you, and the strict-mode gap recorded as yours.
<!-- gate:body:end -->
