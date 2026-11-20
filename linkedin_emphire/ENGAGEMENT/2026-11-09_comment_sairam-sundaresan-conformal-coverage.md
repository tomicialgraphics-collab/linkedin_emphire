---
deliverable: comment
id: 2026-11-09_comment_sairam-sundaresan-conformal-coverage
date: 2026-11-09
audience: Sairam Sundaresan post recommending a forecasting book
status: ready
approved: no
warm: no
profile_checked: >-
  Sairam Sundaresan, AI engineering leader, author of AI for the Rest of Us, works with engineers landing AI roles, already
  following him. The post recommends Ben Auffarth's second edition of Machine Learning for Time Series with Python, naming the
  new chapters: conformal prediction, foundation models such as TimesFM and Chronos, and production forecasting. Four industry
  examples, and an explicit warning that it is not a beginner book.
thread: forecasting, uncertainty and what a coverage number actually promises
---

## The angle

He has named the new chapters without saying what is dangerous in them. Conformal prediction is the one that gets adopted
fastest and misunderstood soonest, because the guarantee is marginal. It holds across the calibration set, not per series.

In retail, where his first example lives, that means a catalogue can report ninety percent coverage while the high volume
series, the ones a person is actually held to, sit far below it. The number is true and the assurance is misplaced, which is
the worst combination in a production forecast.

## Comment, paste as is

The conformal chapter is the one I'd read first, and the trap inside it is worth naming before anyone takes it to production: the guarantee is marginal. Coverage holds across the calibration set, not per series. A catalogue can hit the headline number while undercovering exactly the high volume items somebody is held to.

The test is cheap. Report coverage by segment, and by series for the top hundred. An aggregate of ninety with the top hundred sitting at seventy means that number was never about them.

It's the chapter that changes how a forecast gets signed off, not how it gets built.

## What not to say

No praise for the book beyond the one line at the end, since he is recommending it and does not need a second endorsement. No
question about the author, no request for a review copy, and no pivot to his own work. The subject is coverage, and the comment
stays on it.

## Why the slot is worth it

Thirteen minutes old, and his readers are working engineers who will buy the book this week. A comment that names the one
failure mode the new chapter introduces is more useful to them than anything else under the post, and it is the sort of reply
that gets remembered when someone is choosing who to ask about evaluation.
