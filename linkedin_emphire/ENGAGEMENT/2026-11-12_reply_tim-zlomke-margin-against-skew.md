---
deliverable: comment
id: 2026-11-12_reply_tim-zlomke-margin-against-skew
date: 2026-11-12
audience: public reply to Tim Zlomke in this account's own post thread
status: ready
approved: no
warm: yes
profile_checked: 2026-11-12, third exchange today. He accepted the freshness criterion and then specified it himself: a trusted clock rather than the evidence timestamp, permitted skew, issuance time, applicable window, evaluation time, a positive control just inside the window and a negative control just outside, with the skew assumptions frozen before the run, and said he would check existing coverage against those requirements before claiming the specimen established. There is nothing in that list to argue with, so the reply does not argue with it.
thread: the acceptance criteria for a freshness examination, third round
premise_checked: checked: his list is taken as written and is quoted back only in summary. The reply adds one property of the list rather than a new requirement, so it does not depend on the examination records, which have not been read beyond the lineage page earlier today.
sources_read: none: this reply carries no link and depends on no page. The lineage and persistence records were read earlier today for the first reply and are recorded in `2026-11-12_reply_tim-zlomke-age-rather-than-change.md`. BS-003 and BS-004 remain the only failures visible there.
---

## Reply, paste as is

One interaction worth settling while you freeze the skew assumptions: put the positive control at least one permitted skew inside the window, not merely inside it. If the margin is smaller than the skew you have allowed, the same evidence can pass a control it should pass and fail it under an assumption you already accepted, and the examination reports a false negative it cannot defend.

Everything else in your list I would keep exactly as written. I would rather read the coverage than argue about it.

## Why one property and not another list

His list is now a complete specification: trusted clock, permitted skew, issuance time, window, evaluation time, a control either side of the boundary, assumptions frozen before the run. Adding requirements to a complete specification makes it longer rather than better, and a fourth round of me proposing things is how a correspondence turns into a lecture.

What the list does not yet settle is the interaction between two of its own items. The positive control is defined as sitting just inside the window; the skew is defined as permitted, which means the evaluation time can legitimately be read as earlier or later by that amount. If the margin is under the skew, the same evidence can pass the inside control and fail it without any assumption having been violated, and the examination then has a false negative that no one can explain from the record.

The fix is a sentence, not a requirement: the margin is at least one permitted skew. That is worth having before he looks at coverage, because it changes which existing controls qualify.

## Where I stop

This is the last contribution I would make without a result from him. He has the specimen, the criterion and the scoring rule, and he has said he will bring coverage. Anything further from me is agreement dressed as content, and the useful next message in this thread is one with examination records in it.

If he does reply with coverage, the reply owed under R38 is a reading of it: what the trace names, which clock judged it, and whether the control's margin clears the skew.

## If he never comes back

It stays a good exchange. Two of my criteria landed in his examination language and neither cost him a defence of his work, which is the outcome worth having from a public thread with someone senior.
