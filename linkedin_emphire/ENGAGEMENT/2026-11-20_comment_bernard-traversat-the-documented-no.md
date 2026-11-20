---
deliverable: comment
id: 2026-11-20_comment_bernard-traversat-the-documented-no
date: 2026-11-20
audience: outbound
status: ready
approved: no
recipient: Bernard Traversat, public post
premise: >-
  Oracle's Java platform vice president posted that Primitive Types in Patterns, instanceof and switch has been withdrawn
  from JDK 28 after five previews, because its numeric conversion rules need to line up with Valhalla's direction, with
  parts carried into Constant Patterns. This comment does not argue about the feature. It points at the part that is
  rarer than the decision, which is that the reason is written down, and at the cost comparison that makes a documented
  no cheaper than a late removal.
time_checked: >-
  checked: 2026-11-20 03:00 WAT, read from the system clock before this file was written. That is 22:00 on Thursday in
  New York.
profile_checked: >-
  Bernard Traversat, who wrote about stewardship rather than about performance, and who put the reason for the
  withdrawal in the post itself. The comment takes his own framing, which is that the record matters as much as the
  decision, and does not pretend to know anything about Valhalla's schedule.
premise_checked: >-
  checked: every technical term used here, the five previews, JDK 28, Valhalla, Constant Patterns and the numeric
  conversion rules, comes from his post and none is extended beyond it. No date, no delivery promise and no claim about
  what the rules will eventually be appears in the comment.
sources_read: >-
  read: the post as pasted by the owner, including his link, which was not opened. No page opened.
---

## Comment, paste as is

<!-- gate:body:start -->
The rarer part isn't the withdrawal. It's that the reason is written down where the next person will find it.

Most teams pull something quietly, and five years later somebody rebuilds it, hits the same wall, and no one remembers
it was tried. A preview that ends in a documented no teaches more than one that ends in a quiet yes, because the quiet
one never says what it cost.

Five rounds is also the cheapest possible version of this decision. The expensive one is made after it ships, when the
conversion rules are load-bearing and removing them breaks other people's code.

A preview is a test that admits it might fail. Writing the failure down is what makes the rest of the platform worth
trusting.
<!-- gate:body:end -->
