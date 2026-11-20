---
deliverable: doc
id: findings-02-register-addendum-v8
date: 2026-11-10
audience: Marvin Percival, DUNIN7
status: ready
---

# Register addendum, v8: W-05 closes, and two things it does not cover

Version 7 of the register is unchanged and stays the record of the findings as they stood on 9 November.
This file records what the author's status record and specification v0.12 do to it, and what I checked
myself before agreeing.

## W-05: closed, on the condition I set rather than on the rule that answers it

The condition was narrow on purpose: a producer outside a test anchoring a header with a non-zero
segment range. Section 10 item 9 of v0.11 records that on 10 November, on Kaspa mainnet, through a lane
a client can register: `first_seq` 0 to `last_seq` 2, head `22d4608c...3101`, anchored value
`3b8f2d15...ea2e`. Item 11 of v0.12 anchors a second batch of the same stream, `seq_no` 3 to 5, head
`c6d11133...e145`, and joins the two under §4.4.5.

The close is against item 9, not against finding A11. A11 is the rule the verifier reads a segmented
client header by. Item 9 is the artefact that shows a producer wrote one. Both matter, and only one of
them is evidence.

## What I checked without the repository or the verifier

Published material alone, on 10 November:

- Transaction `6ca065b9...e684` returns from the Kaspa public API, `is_accepted` true, payload exactly
  `3b8f2d15...ea2e`, which is the anchored value in item 9 and nothing else. 32 bytes.
- Transaction `17f8ce56...38cb` returns the same way, payload exactly `32a65667...424f`, the anchored
  value in item 11. 32 bytes.
- The second transaction spends the first one's output: its input `previous_outpoint_hash` is the
  identifier of the first. That is the lane's own chain at the transaction level, independent of the
  header chain claim in item 11, and it is the strongest of the four checks because it does not depend
  on anything the project says about itself.
- Block times from the same source: 12:20:15 and 15:17:42 UTC on 10 November, 2 hours 57 minutes apart.

The last of those bears on the caveat in items 9 and 11 that the verifier's chain source carries the
broadcaster's log time rather than block time. The caveat is correct about the verifier. It is not a
limit on the claim, because a public explorer dates both anchors independently of the project. Worth
saying in the specification: the verifier's timestamp is indicative, and the block time is available to
anyone who looks.

## Two limits, recorded and not scored

**The extent proves order, not content.** `seq_no` and `prev_tx_hash` arrive from the request, so the
anchored extent shows that a producer, given those positions, committed those record hashes in that
order. It does not show that the record body agrees with its position. A client that needs the binding
must carry the position in its own body and check it there. This is a boundary of what is anchored, and
the specification states it plainly in item 10.

**The reachable path is proved by vectors, not by an anchor.** Section 4.4.4 retires the refusal, and
the aggregate now hashes a client header with its segments, so the path no longer refuses a stream
record. No Tier-2 aggregate carrying a segment has been anchored on chain. Read beside the finding this
replaces, the situation has inverted: on 9 November the code was real and unreachable, and today it is
reachable and unanchored. Both are worth the same sentence in a public claim, and neither is a defect.

## W-06, new: the amendment contradicts the specification, and says so about itself

Section 10 item 10 notes that amendment v0.25 §5.5.4 item 2 still states that the full segments
serialiser stays unbuilt, and that the specification does not edit the amendment. A reader who arrives
at the amendment and stops there is told the opposite of what is true, with a citation that looks
authoritative.

This closes on a dated amendment revision that says the serialiser exists and where it is used. The
ruling inside item 2, that segments are not the mechanism for client attribution or cumulative counters,
is unaffected, and I am not disputing it.

## What the register now says

W-01 closed. W-02 closed. W-03 closed, superseded by W-05. W-04 closed in the text, with the probe not
re-run by the author in his own record. W-05 closed on 10 November. W-06 open, and it is a documentation
defect rather than a protocol one.
