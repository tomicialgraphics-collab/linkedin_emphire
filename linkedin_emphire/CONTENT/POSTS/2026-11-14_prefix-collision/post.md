---
deliverable: post
id: 2026-11-14_prefix-collision
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 19:00 WAT WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: no
template: T1
headline: The hash was wrong in 48 characters and the check passed anyway.
headline_alt: My verifier passed a manifest I had forged on purpose.
headline_alt2: A check that compares 16 of 64 characters cannot fail.
subheadline: A truncated comparison cannot fail, which is why I now test the test.
box: cannot fail
box_alt: green is not proof
hashtags: "#AIEngineering #SoftwareEngineering #AIEvals #AIRedTeam"
visual_link: https://drive.google.com/file/d/18VIGpfcMBlIhdVbeubKOZEqtt6n2eAP-/view
premise_checked: >-
  checked: every number in this post was produced on 14 November in two checkouts of the pinned
  harness at 80fa2cf and is copied from logs kept in the repository. The forged manifest keeps the
  true digest for sixteen characters and replaces the last forty eight, and the published verifier
  passed it, 50 checks to 0 failures. The corrected verifier fails that row, 53 to 1, and passes the
  true manifest 54 to 0. The failure-path suite runs six cases and 13 checks, one of them a simulated
  crash between the two renames. The three defects are the three the reviewer wrote down on
  14 November, in his words rather than a summary of them.
sources_read: >-
  read: the reviewer's message of 14 November at 17:01, the verifier's output before and after the
  change, and the failure-path log. No page was opened and no link sits in the post body.
profile_checked: >-
  The reviewer is not named. He wrote his findings in a private exchange about a pinned harness, and
  naming a private individual in a feed post to borrow his credibility is the move this post argues
  against. The recommendation from the tool's author belongs in Featured, where a visitor looks after
  reading something substantive, not in the body of a post that would then be about being praised.
---

## Post, paste this

<!-- gate:body:start -->
The hash was wrong in 48 characters and the check passed anyway.

A truncated comparison cannot fail, which is why I now test the test.

I built a verifier for a five-test AI red team suite. It compared the first 16 characters of every SHA-256 instead of all 64. So I forged a manifest: the real digest, first 16 characters kept, the other 48 replaced with f. It passed. Fifty checks, zero failures.

An independent reviewer found the same hole in ten minutes with the same test. That's the part I keep thinking about, because I wrote the tool and never tried to break it.

I fixed the comparison. The fix I care about more is the one that keeps the hole closed: the verifier now exits non-zero unless it can prove it rejects a digest that matches on a prefix. A test that can't fail is decoration.

The same review found two more defects in the run record. Archiving before publishing is ordering, not atomicity, so the record and the package are now bound by a digest and an interrupted pair is detectable. And a results file from an earlier run could be archived after an unrelated non-zero exit, because the rule tested existence instead of authorship.

Both carry failure-path tests now: six cases, thirteen checks, including a simulated crash between the two renames.

The general lesson is the uncomfortable one. A green suite tells you the checks ran. It doesn't tell you they compare what they claim to compare. Only a test built to fail can show you that.

#AIEngineering #SoftwareEngineering #AIEvals #AIRedTeam
<!-- gate:body:end -->
