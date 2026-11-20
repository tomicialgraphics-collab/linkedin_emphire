---
deliverable: comment
id: 2026-11-14_comment_kvn-rajesh-looped-transformer
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 19:45 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: public
status: ready
approved: no
warm: yes
profile_checked: >-
  K.V.N. Rajesh writes careful technical explainers with the numbers in them, which is why this post is
  worth a comment: it publishes a curve rather than a single score, so the reply can work on his own figures
  instead of arguing about the release. He is not selling anything in the post and neither should the reply.
premise_checked: >-
  checked: every number in the comment is his, and the only arithmetic performed on them is subtraction
  between figures he states and the block count formula his own description implies, 8 plus 20k plus 8
  giving 36, 56 and 96 at k of 1, 2 and 4. The release itself was not verified: no page for Dory1.0-4B was
  opened and the comment makes no claim about whether the model exists, only about what his numbers show if
  they are true. The AA-Omniscience figure is quoted at 10.0 as he reports it.
sources_read: >-
  blocked: no accessible source for the NVIDIA release, and the benchmarks named are not reproducible from
  this environment. The comment states a reading of the numbers rather than a verification of them, and
  does not call them confirmed.
---

## Comment, paste this

<!-- gate:body:start -->
The arithmetic in this checks out, and the most useful number in it is the one that won't get quoted.

Eight plus twenty k plus eight gives 36, 56 and 96 at k of 1, 2 and 4, so the block counts match what you describe. But read the SWE-bench line as a curve rather than a destination. 50.3, 59.5, 61.8. The second loop buys 9.2 points. The third and fourth together buy 2.3, for roughly twice the compute per token.

That is the whole decision, and it is why 61.8 is a headline rather than a recommendation. NVIDIA defaulting to 2 is the honest part of the release: they put the shipping default where the curve is still steep, not at the peak, because the peak is a benchmark and 2 is a product.

The AA-Omniscience figure belongs next to it. 10.0 at one loop and 10.0 at four is the cleanest sentence about what looping does not do. It improves what the model does with what it knows and adds nothing to what it knows. Any agentic eval that mixes the two will report a gain that came from the first thing and get credited to the second.
<!-- gate:body:end -->
