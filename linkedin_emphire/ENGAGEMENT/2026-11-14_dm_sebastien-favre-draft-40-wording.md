---
deliverable: dm
id: 2026-11-14_dm_sebastien-favre-draft-40-wording
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:40 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: vendor
status: ready
approved: no
warm: yes
profile_checked: >-
  Sébastien Favre runs the evidence repository. He answered Timothy's 1.3.0 review on 14 November at
  10:45 by opening a draft pull request to credit the contribution, and said he will merge it only with
  approval, then sent a recommendation at 10:48. He asked for the wording to be reviewed, which makes
  the reply a decision on the text rather than a thank you, and he asked about the write-up, which makes
  it a statement about what is coming rather than a promise of something new.
premise_checked: >-
  checked: revised on 14 November at 18:40 against the full thread, which was re-read rather than
  recalled. Timothy's own message of 06:43 records the re-run at 1.3.0, the 172 conforming digests, the
  121 fixtures reproduced byte for byte, the two missing binaries named with their build commands, the
  eleven green checks, and the sentence that his patches changed a contract rather than repairing a
  defect. The pull request still cannot be opened from here, because the repository returns 404 without
  access, so nothing below claims to have read its wording. Approval is therefore conditional on three
  statements rather than on the text.
sources_read: >-
  read: the pasted thread of 14 November, being Timothy's message of 06:43 and Sébastien's two messages
  at 10:45 and 10:48. The pull request and the recommendation were not opened. The recommendation sits
  behind a sign-in and the request returns a client error page, and the message does not quote it or
  describe what it says.
---

## DM, paste this

<!-- gate:body:start -->
I still can't open the draft. The repository gives me a 404 without access, so I haven't read the wording and I'm not going to approve text I haven't seen. What I can do is say what it has to carry, and approve it the moment it does.

Three statements, and all of them are things you can check against your own body in a minute.

One. This was a contract change, not a defect fix. You know that already, because I said it at 06:43 before your reply, and it's the most interesting thing in the exchange: incomplete and failed are different states. A pull request that calls my patches a repair quietly upgrades them into something they aren't.

Two. The re-run was at 1.3.0, on the release, not on my branch against your tool. That distinction is what makes the acknowledgement accurate rather than generous. I checked 172 digests, reproduced 121 fixtures byte for byte, and found the runner stopping with two missing binaries named and the two build commands given. Eleven checks green. And the CI job you added names the property rather than the symptom, which is why it'll still be useful in a year.

Three. Credit isn't endorsement. Nothing in it should say the review closed, validated, or signed off on the corpus. I credited and questioned, in that order, and the write-up will do the same. One thing belongs to you rather than me: the strict-mode value that no run had ever measured came out of your own release notes, so attribute it there.

If the body already does those three, merge it and treat this message as the approval. If one is missing, send me the sentence and I'll approve the edit rather than the intention. I'd rather argue about a paragraph than hold up a merge over a formality.

On the write-up: it follows, as I said. Both designs, both reasons, the disagreement attributed to you rather than smoothed into agreement, and the strict-mode gap in the harness recorded as yours. It won't be longer than it needs to be.

On the recommendation: thank you. I'm not going to trade one back to keep the ledger level. If I write one it'll be because the work earned it, and it has, so it won't be a formality when it arrives.

That's a yes with a shape, which is the only kind worth sending you.
<!-- gate:body:end --><!-- gate:body:end -->
