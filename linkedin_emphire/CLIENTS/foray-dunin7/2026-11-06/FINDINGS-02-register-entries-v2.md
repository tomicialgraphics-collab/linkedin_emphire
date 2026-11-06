# FORAY adversarial review, item 1: three register entries

**Subject:** FORAY stream continuity, as specified and as built.

**Reviewer:** Olusanya Timothy, independent. Private until the author agrees what enters the register.

**Date:** 6 November 2026. Supersedes the version of 4 November.

**Text referred to:** Verifier Specification v0.4 §3 and §8.5; amendment v0.25 §5.5.4, §7.3, §7.4, and the outcome taxonomy at §10.1.

**Code referred to:** WP-1 verifier `b890d2c357b4b2a06f7db440157c33c7f311c4df`, archive SHA-256 `45a624e4dfbbc9280e59a9538fcf52e4c05f25b606a6c43fc35d95090958e5c9`; conformance suite `25a856fff788e7ef72490cb180b4453a6fa3dad0`, archive SHA-256 `bf02a2e2ea8a9940a5c4cb1867bfb607753fd12b943cb47fb345ebf7190f427c`.

**Probe:** `foray-probe.mjs`, 171 lines, no dependencies, SHA-256 `07963743bddb09cb5df2d8e38d381add50fc28b249a566e29266d454d23d9309`. Run it as shown at the end of this file; it prints one line per case and never throws on a wrong path.

---

## What reproduced, and where

Stated exactly, because the distinction matters to what these entries are worth.

**On shipped vectors, with nothing changed but `context.streamHistory`:**

- `negative/N10-backdated-insert-fork` returns INVALID, check 10, continuity FORK. Remove the one record that proves the fork and the same bundle returns VALID. Empty the history and it returns VALID.
- `positive/rotated-chain-seam` returns VALID as shipped, and still returns VALID with the tail record removed, with the head record removed, and with the history emptied.

**On W-01c, which the author found during his own reproduction:** a bundle whose `stream_context.prev_tx_hash` is falsified, history untouched and internally continuous, returns VALID.

**W-01a, W-01b and W-01d were originally observed at walk level only, not through the full verifier.** That limit is now removed, with a caveat. The vector packet ships no bundle that carries both a `stream_context` and a populated `header_echo.stream_segments`, so a case with an anchored extent has to be constructed. I constructed one: `rotated-chain-seam` with a single segment added to the header claiming `first_seq 0, last_seq 412`, the anchored value recomputed from the new header, and both canned chain sources updated to match. The frozen meaning of the record's declared predecessor is preserved, so the bundle is internally consistent.

Those cases are marked SYNTH. The control matters more than any of them: with a complete history 0..412 whose last record is the segment's `head_hash`, the constructed bundle returns VALID. The probe is capable of passing, so the failures below are not manufactured by the construction.

**Against that bundle, all of the following return VALID:** history 0..400; history 300..412; a single record at 412; an empty history; and a complete history whose head contradicts the anchored `head_hash`.

**Not yet run: the author's patch.** It was not present in the shared files when this was written. The same script runs against it with one command, and the expected column below is what it should print.

---

## W-01. The walk ignores the anchored extent, ignores the record's declared position, and passes when there is no history at all. High.

### What the text intends

Amendment v0.25 §7.3 and §7.4 make the continuity walk run against anchored segment ranges. The intent is legible: a consumer holding records compares what it holds against the extent a producer anchored, and answers CONTINUOUS, or names the missing range, or shows two records claiming one slot. That comparison has two sides. The build implements one side.

### What the implementation does

`lib/streams.mjs`, `walkContinuity()`, does three things and omits three things.

It sorts `context.streamHistory` by `seqNo`, then walks adjacent pairs checking that sequence numbers increment by one and that `cur.prevTxHash === prev.txHash`. The loop does not run for zero records or one record, and the caller treats a non-throwing walk as continuous, so an empty history is indistinguishable from a clean stream.

It never reads `header_echo.stream_segments`, so the extent anchored in the covering header has no bearing on the result. It never compares `stream_context.prev_tx_hash` with the history, so the record's own declared position is unchecked. And it has no notion of the walk being impossible, so there is no path from "I could not look" to any outcome other than silence.

### Reproductions

| case | setup | observed | expected |
| --- | --- | --- | --- |
| W-01a | header declares `first_seq 0, last_seq 412`; history holds contiguous 0 to 400 | VALID | MATERIAL_UNAVAILABLE: the history does not cover the anchored extent |
| W-01b | same header; history holds contiguous 300 to 412 | VALID | MATERIAL_UNAVAILABLE: the anchored start is not covered |
| W-01c | bundle declares a falsified `stream_context.prev_tx_hash`; history internally continuous | VALID | INVALID: the declared predecessor is contradicted by the history |
| W-01d | history holds a single record at 412 against an extent of 0 to 412 | VALID | MATERIAL_UNAVAILABLE: one record cannot evidence 413 |
| W-01e | complete history 0 to 412; segment `head_hash` falsified | VALID | INVALID: the anchored head is contradicted by the history |

W-01c was found by the author during his own reproduction, not by me. It is credited to him.

### Why the two outcomes are not interchangeable

§3 does not let a contradiction and an absence share a verdict, and the difference is the difference between "this record is lying" and "I was not given enough to say". A falsified `prev_tx_hash`, or a history head that disagrees with the anchored `head_hash`, is a contradiction: the material in hand cannot all be true together, so the outcome is INVALID. An absent or short history is not a contradiction; nothing in it is false, there is simply less of it than the anchored extent claims, so the outcome is MATERIAL_UNAVAILABLE, naming the missing range and the sequence numbers that are missing.

Any fix that routes both to one verdict trades a false accusation for a false acquittal. The taxonomy already carries both outcomes; nothing new needs inventing.

### Why this is High

The property being sold is that omission inside a registered stream breaks visibly. In this build the walk cannot distinguish a stream that ended at 400 from one that was cut at 400, cannot tell that it began at 300, cannot see a record whose declared predecessor is not the one it follows, and cannot see a head that disagrees with the range anchored over it. The one thing the walk is for is the one thing it cannot do.

### Minimal fix

Bind the walk to both sides before walking. Read the covering segment from `header_echo.stream_segments` and compare four things: the history's first and last sequence numbers against `first_seq` and `last_seq`; the last record's hash against `head_hash`; `stream_context.prev_tx_hash` against the record at `seq_no - 1`; and, separately, whether the walk ran at all. Contradictions return INVALID. A shortfall in coverage, or an absent history against a known extent, returns MATERIAL_UNAVAILABLE with the missing range named.

**One ordering hazard, found while testing a throwaway fix of exactly this shape.** Returning MATERIAL_UNAVAILABLE for an empty history before the rest of check 10 has run breaks a shipped vector. `negative/N11-ref-postdates-claim` carries a `stream_context`, an empty history, a `_ref` that postdates the claimed timestamp, and expects INVALID with sub-verdict INVALID-CHRONOLOGY. A patch that returns on emptiness first turns N11 into MATERIAL_UNAVAILABLE and fails the suite, 28 pass and 1 fail on my copy. Contradictions found in check 10 must be evaluated before the material return.

`Accepts as closed when` regression modes exist for the five cases above, each returning the outcome in the expected column on the current tree, and the suite stays at 36 of 36.

---

## W-02. Missing history returns VALID, and the text does not yet say what it should return. Medium, and partly textual.

### What happens

`const history = context.streamHistory ?? []; if (history.length > 0) { ...walk... }`. Zero records means the walk is skipped, and a skipped walk is indistinguishable from a clean one. Nothing in the build produces MATERIAL_UNAVAILABLE for absent stream state.

The sharpest form of this is on a shipped vector. `negative/N10-backdated-insert-fork` exists to catch a fork at check 10. As shipped it returns INVALID, check 10, continuity FORK. Remove the record that proves the fork and the same bundle returns VALID. Empty the history and it returns VALID.

### Why this is a text question as much as a code question

The outcome taxonomy at amendment v0.25 §10.1 defines MATERIAL_UNAVAILABLE for a missing blob, a missing tree and a missing salt. It does not name missing stream history. A verifier implementer reading the published text therefore has no instruction that an absent history maps to MATERIAL_UNAVAILABLE, and the reference implementation's silence is consistent with the text as written.

That makes this a specification question first and an implementation gap second, which is why the entry asks for a ruling rather than only a patch. I do not know which way it should go, and I am not asserting what the author's position is; I record it as open. What I can say is that §3 requires the outcomes not to be conflated, and that a stream whose history is entirely absent currently reaches the same verdict as a stream that was checked and found clean.

### Minimal fix

If the ruling is that absence maps to MATERIAL_UNAVAILABLE, name stream history alongside the missing material in §10.1, with the same custodian-naming requirement, and return MATERIAL_UNAVAILABLE when `stream_context` is present and no history is supplied. If the ruling is otherwise, the entry becomes a text clarification only, and the code stays as it is.

`Accepts as closed when` the text names the case either way, and a mode proves the implementation matches the ruling rather than defaulting to VALID.

---

## W-03. The producer does not write stream segments, and does not number records in streams. High for the coverage claim, and design work rather than a patch.

### What the code does

In `foray-api`, the batch accumulator and the Tier-2 aggregator both serialise every header through `serializeBatchHeaderNoSegments`. The full segments serialiser is not built, which is consistent with §5.5.4. Searching the JavaScript of `foray-api`, outside tests, conformance and vendored code, there is no `seq_no`, no `prev_tx_hash` and no `stream_id`.

### What that means together with W-01 and W-02

Every production anchor carries zero segments, so there is no anchored extent for a walk to read even once the walk is fixed. Registered streams are specified in the text and are not built on the producer side.

This is visible in the packet, not only in the producer. `positive/rotated-chain-seam` carries a `stream_context` and a two-record history, and its header declares no segments. So even with W-01 fixed, truncation of that stream is not detectable, because there is no anchored extent to be short of. The fix and the producer gap meet at the same place: a stream with no anchored range can be walked for adjacency and nothing else.

Two gaps therefore sit between the protocol's claim and the artefacts a holder can present: nothing to walk against, and no walk that reads it when it exists.

The consequence is worth stating plainly, because it is the thing a buyer or an auditor will ask. A record that was never numbered is invisible, and a record whose stream was never registered has no extent to be missing from. That is not a defect in the walk. It is the coverage boundary of the current build, and it is the correct thing to publish rather than to imply otherwise.

### Where the design work belongs

The signed stream inventory I raised on 4 November belongs with this entry, not with the walk fix. In short: an inventory naming which streams exist, which producer must emit each, and the expected cadence or count, anchored periodically and signed, turns "is this stream continuous" into "is this inventory complete for this entity". Without it, a producer can register one narrow stream, stay CONTINUOUS forever, and omit an entire class of event without producing a GAP. The registration contract, not the record, then carries the assurance weight.

This is a proposal, not a finding against the text. It is recorded here so that W-03 has a corrective path attached, and it is explicitly not claimed as agreed.

`Accepts as closed when` a producer anchors at least one header with a non-zero segment range and numbers records in a registered stream, and a walk over that stream returns CONTINUOUS only when it matches the anchored extent.

---

## What these entries do not claim

- They do not claim the protocol's cryptography is weak. The anchors recompute correctly; the class A check of Record A from published material passed byte for byte.
- They do not claim any producer has shipped streams and got them wrong. The producer has not shipped them at all, which is a different and milder statement.
- They do not treat the author's confirmation as admission. He reproduced these results independently and added a case I had missed, which is the behaviour of someone trying to get the document right.
- They do not include the wire 4.3 documentation gap, which belongs to the specification review rather than to the walk, and which he has already recorded as his own gap.

## Reproduction

```
node foray-probe.mjs "<folder containing lib and vectors>"
```

Sixteen cases, grouped. The ten Group A cases hold the bundle internally valid and vary only the history. The six Group B cases are marked SYNTH because they add an anchored extent to a vector that has none.

Output on the archive as delivered, Node v22.22.3:

```
rotated-chain-seam: as shipped                       VALID
rotated-chain-seam: tail record removed              VALID
rotated-chain-seam: head record removed              VALID
rotated-chain-seam: history emptied                  VALID
rotated-chain-seam: prev_tx_hash falsified           VALID
N10: as shipped                                      INVALID  check=10  FORK at seq_no 1
N10: tail record removed                             VALID
N10: head record removed                             VALID
N10: history emptied                                 VALID
SYNTH extent 0..412, history 0..412, head matches    VALID
SYNTH extent 0..412, history 0..412, head falsified  VALID
SYNTH extent 0..412, history 0..400                  VALID
SYNTH extent 0..412, history 300..412                VALID
SYNTH extent 0..412, history [412]                   VALID
SYNTH extent 0..412, history []                      VALID
```

To prove the probe is not a rubber stamp, I applied a throwaway local fix of the shape described in W-01 and reran. Eight cases moved to the outcome the text implies, including `history 0..400` returning MATERIAL_UNAVAILABLE with the covered and expected ranges named, `head falsified` returning INVALID, and `history []` returning MATERIAL_UNAVAILABLE. The same fix broke N11, which is the ordering hazard recorded above. Neither the throwaway fix nor that result is being proposed as a patch.
