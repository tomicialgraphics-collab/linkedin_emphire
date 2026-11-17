---
deliverable: comment
id: 2026-11-17_comment_jerry-liu_the-weights-and-the-judges-error-rate
date: 2026-11-17
audience: public
status: ready
approved: no
warm: yes
surface: >-
  Comment under Jerry Liu's post about benchmark granularity for document parsing. It introduces two instruments, a
  deterministic one split into six dimensions and 330 scenarios with human-defined severity weights, and a protocol of
  140 rules and 516 written checks each measured by a judge prompt.
time_checked: >-
  checked: 2026-11-17 20:09 WAT, read from the system clock before this file was written.
profile_checked: >-
  Jerry Liu, following, building developer tools and publishing benchmarks in public. He states the weaknesses of both
  instruments himself, so the comment does not tell him his benchmark is imperfect. It picks the two decisions that
  survive contact with a reader who will use the numbers, which are the weight table and the judge's error rate.
premise_checked: >-
  checked: every figure used here, six dimensions, 330 scenarios, 140 rules, 516 checks and the wrong-digit example, is
  quoted from his post and attributed to his instruments. Nothing was run and nothing is claimed about either
  benchmark's accuracy. The judge error-rate question is asked rather than answered, because it cannot be answered from
  the post.
sources_read: >-
  read: his post in full. Neither benchmark link was opened, so nothing here describes their internals beyond the
  numbers he gave.
---

## Comment, paste as is

<!-- gate:body:start -->
The severity weights are the most important thing in this post, and they're the part most benchmarks keep in the code rather than in the write-up. A wrong digit costing ten points while stray markup costs nothing is a preference, not a measurement.

Which means the score only means something against the weight table that produced it. The moment two benchmarks weight differently, the leaderboards aren't comparable, and everybody will compare them anyway. Versioning the weights and publishing them beside each result fixes that the way a hash beside a download does, and it moves the disagreement to the useful place: whether a wrong digit should outweigh three layout errors, rather than whether one model is better.

On the 516 judge-coded checks, the number I'd want first is the judge's own false-pass rate on the category you weighted highest. A judge that misses one wrong digit in twenty is a different instrument from one that misses one in two, and an aggregate score hides which one you're holding.

Granularity is what makes that question askable at all, which is the argument for doing it this way. The weights and the judge's error rate are what make the answer trustworthy.
<!-- gate:body:end -->

## Why the weights and not the number of checks

330 scenarios and 516 checks are the impressive figures, and the weights are the one that decides what any of them mean. He already says neither instrument is perfect, so a comment about imperfection would be a sentence he wrote himself. A comment about the weight table is a design proposal he can act on.

The comparability point is the one readers will hit next week, when both of these appear side by side in somebody's slide and the numbers get subtracted from each other.

## Why the judge question is asked and not answered

He calibrates the judge with written checks, and how well his judge detects the failures he cares about most is not in the post and cannot be inferred from it. Asking for a false-pass rate on the highest-weighted category is a question a benchmark author can answer from work he has already done, and the answer is a number his readers can use.

## Why it ends on his argument

The close hands him the credit for the structure, because granularity genuinely is what makes an error-rate question possible. Disagreement about a method is cheaper to receive when the same paragraph says what the method is good for.
