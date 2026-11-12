# Sources and claims

## No figure in the post describes the world

Every number in the post is a parameter of a test the reader runs: a 45 minute clock rollback, a 1 hour token
lifetime, an evaluation at minute 59 and at minute 61, a shift of a few minutes. None of them is a measurement,
a statistic or a claim about how often anything happens, so there is nothing here that could be fabricated and
nothing that needs a citation.

The 1 hour lifetime is illustrative and is not attributed to any vendor. Readers who know their own token
lifetimes will substitute them, which is the point of writing the test that way.

## Claims, and their basis

| Claim | Basis |
| --- | --- |
| A freshness check is a comparison between the time on the evidence and the current time | definitional: expiry is a subtraction |
| If the current time comes from the evaluated system, the control measures receiver drift | arithmetic: both operands then come from the party under test |
| A refused request and a parse failure can produce indistinguishable records | a refusal recorded only as "rejected" carries no reason field to separate them |
| Moving a clock is one line in most harnesses | operational: time injection in tests is usually a single seam, though not in every framework |
| A control that cannot name the clock it trusted is not a control | the post's argument, not a measured finding |

## What is not claimed

- No claim that any named product does this wrong.
- No claim about how common the defect is. There is no sample behind that and I am not going to invent one.
- No claim that a trusted clock solves freshness. It makes the comparison meaningful; the window still has to be
  the right one.

## Relationship to the earlier post

This continues the paired-run post from the same day, which covered a change in authority. Age is a different
variable, and the clock is the part of age that most implementations leave undefined.
