---
deliverable: post
id: 2026-11-14_post_prefix-collision
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:56 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: no
premise_checked: >-
  checked: every number in this post was produced on 14 November in two checkouts of the pinned
  harness at 80fa2cf and is copied from logs kept in the repository. The forged manifest keeps the
  true digest for sixteen characters and replaces the last forty eight, and the published verifier
  passed it, 50 checks to 0 failures. The corrected verifier fails that row, 53 to 1, and passes the
  true manifest 54 to 0. The failure-path suite runs six cases and 13 checks. The three defects named
  are the three the reviewer listed in writing on 14 November, in his words rather than a summary.
sources_read: >-
  read: the reviewer's message of 14 November at 17:01, the verifier's own output before and after
  the change, and the failure-path log. No page was linked and no link is in the post.
visual_link: https://drive.google.com/file/d/1AqjPwQvcoGIi16qS8eP-kh_3oufKofSm/view
profile_checked: >-
  The reviewer is not named. He wrote his findings in a private exchange about a pinned harness, and
  naming a private individual in a marketing post to borrow his credibility is the thing this post
  argues against. Anyone who asks can be told, with his agreement, and the recommendation from the
  tool's author belongs in the profile's Featured section rather than in a feed post.
---

## Post, paste this

<!-- gate:body:start -->
My verifier compared 16 of the 64 characters of a SHA-256 and passed a forged manifest.

It printed 50 checks, 0 failures. The manifest disagreed with the file in every character after the sixteenth.

An independent reviewer found it with the negative test I should have written myself: take a real digest, keep the first 16 characters, replace the other 48, and see whether the tool notices. Mine didn't.

I fixed the comparison. Then I did the part that mattered more and took longer: turning the collision into a permanent test. The verifier now exits non-zero unless it can prove it rejects a digest that matches on a prefix, so the hole can't come back quietly.

The same review found two more defects that day. Archiving before publishing is ordering, not atomicity, so the record and the package are now bound by a digest and an interrupted pair is detectable. And a results file from an earlier run could still be archived after an unrelated non-zero exit, because the rule tested existence rather than authorship.

Both now carry failure-path tests rather than assurances. Six cases, 13 checks, including a simulated crash between the two renames.

The lesson isn't about hashes. A green suite tells you the checks ran. It never tells you they compare what they claim to compare. Only a test built to fail can show you that.

So I stopped treating a passing run as evidence and started asking what would have to be true for it to fail.
<!-- gate:body:end -->
