---
deliverable: comment
id: 2026-11-17_comment_hannah-westra_the-scorer-and-the-repeat
date: 2026-11-17
audience: public
status: ready
approved: no
warm: yes
surface: >-
  Comment under Hannah Westra's release post for PyRIT 1.2.0. She reports 507 merged pull requests with 108 external
  contributors, 58 percent of the release, and lists workflow, findings capture and new coverage among the changes.
time_checked: >-
  checked: 2026-11-17 20:17 WAT, read from the system clock before this file was written.
profile_checked: >-
  Hannah Westra, senior software engineer on an AI red team, posting a release rather than an argument. So the comment
  is addressed to a maintainer and offers two things missing from the release notes rather than restating what shipped.
  She and a colleague have appeared in this workspace before, and the register stays plainer with people who have already
  seen the method once.
premise_checked: >-
  checked: the three figures used, 507 pull requests, 108 external contributors and 58 percent, are quoted from her
  post. Nothing is claimed about PyRIT's internals, its scorers or its benchmarks, none of which was read. Both points
  offered are proposals about what a release should carry, which is a judgement rather than a claim about her work.
sources_read: >-
  read: her post in full. The release notes, documentation and repository links were not opened.
---

## Comment, paste as is

<!-- gate:body:start -->
The item I'd put at the top of that list is the findings capture, not the coverage. Everything else in the release makes an assessment faster. The human-reviewed finding with its evidence behind it is the only part that survives contact with the team on the other side of it.

Coverage grows the instrument's own attack surface as well, and the number it brings with it is a new scorer's false-negative rate on the cases you already know. A red team that misses quietly is worse than one that reports nothing, because the report gets believed.

Repetition sits underneath that. A finding needs enough to be run again, which means the inputs rather than the transcript: seed, target version, scorer version. Whoever disputes a finding a quarter later disputes it against a report, and a report is only as good as its ability to be repeated by somebody who doesn't trust you.

58% of release PRs from outside is the number worth bragging about, and it's also the one that makes scorer discipline necessary rather than optional. Most of those scorers arrive from somebody else.
<!-- gate:body:end -->

## Why the findings capture leads

It is the least glamorous item on her list and the only one that changes what a customer can do with the output. Speed and coverage are improvements to the instrument. A finding with evidence is an object another team has to answer, and that is the unit the work gets judged by.

## Why the two asks are about the instrument rather than the release

She has just shipped more coverage, which is the right thing for a mature framework and also the thing that makes the failure modes harder to see. New scorers fail silently by nature, and a review that misses reads exactly like a review that found nothing. That makes the scorer's error rate the number that qualifies every other number in the product.

Repetition is the second half of the same idea. A finding nobody can re-run is a claim with a date on it.

## Why the compliment is the last line

Her 58 percent figure is the strongest thing in the post and the one she is proudest of. It also sets up the argument rather than decorating it, because a project whose scorers arrive from outside inherits their error rates along with their coverage.
