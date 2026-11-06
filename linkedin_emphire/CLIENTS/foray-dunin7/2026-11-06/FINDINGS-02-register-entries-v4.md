# FORAY adversarial review, item 1: three register entries

**Subject:** FORAY stream continuity, as specified and as built.

**Reviewer:** Olusanya Timothy, independent. Private until the author agrees what enters the register.

**Date:** 6 November 2026, third revision. Supersedes the version of 4 November and both revisions of today. Two additions: the patch results in the section after next, and a status column against the author's merge commit `05267a36a57edf31bae2c2b9390f85df9c899a43` at the head of the open items. The identifier W-04 below is the author's, assigned to what this document called W-01g.

**Text referred to:** Verifier Specification v0.4 §3 and §8.5; amendment v0.25 §5.5.4, §7.3, §7.4, and the outcome taxonomy at §10.1.

**Code referred to:** WP-1 verifier `b890d2c357b4b2a06f7db440157c33c7f311c4df`, archive SHA-256 `45a624e4dfbbc9280e59a9538fcf52e4c05f25b606a6c43fc35d95090958e5c9`; conformance suite `25a856fff788e7ef72490cb180b4453a6fa3dad0`, archive SHA-256 `bf02a2e2ea8a9940a5c4cb1867bfb607753fd12b943cb47fb345ebf7190f427c`.

**Patch tested:** `foray-streams-fix-b890d2c-v0_3.patch`, 4,677 bytes, SHA-256 `3fca8c725b589b9e5a8748d38e3a8a30ecea6bd6d7ded9db8e5675c6c1ac41e0`, from commit `63bcd0201864844c3db2f171a87040a332510014`.

**Probe:** `foray-probe.mjs`, 292 lines, no dependencies, 23 cases, SHA-256 `c91be299ff59076f0a49f43fd6a4f01e1f98fad7fe478e46b9b2225efecaa326`. Run it as shown at the end of this file; it prints one line per case and never throws on a wrong path.

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

**The author's patch has been run.** See "Results against the patch" below. The expected column in the W-01 table is now the observed column against that patch.

---

## Results against the patch

The patch applies to a clean copy of the archive with `git apply`: no fuzz, no rejected hunks, one file changed. `lib/streams.mjs` moves from `c834ea28ed66cc74fdd9610d6e31ef736b39fa020d24485d7847981a0d7b9237` to `f7512ee231f92ca93ab685598c55d9a5e5209af031a33470a1e7626e175c1690`.

**The suite does not move.** Same 29 tests before and after, 29 pass and 0 fail. N11 still returns INVALID with INVALID-CHRONOLOGY, because the new check runs after the existing body of check 10. The patch header says that ordering is deliberate, and the suite agrees with the header.

| case | before the patch | after the patch |
| --- | --- | --- |
| rotated-chain-seam, as shipped | VALID | VALID |
| rotated-chain-seam, tail record removed | VALID | MATERIAL_UNAVAILABLE, `(self) [[1,1]]` |
| rotated-chain-seam, head record removed | VALID | MATERIAL_UNAVAILABLE, `(predecessor) [[0,0]]` |
| rotated-chain-seam, history emptied | VALID | MATERIAL_UNAVAILABLE, `(history) null` |
| rotated-chain-seam, `prev_tx_hash` falsified | VALID | INVALID, contradiction |
| N10, as shipped | INVALID, FORK at 1 | INVALID, FORK at 1 |
| N10, fork record removed | VALID | MATERIAL_UNAVAILABLE, `(self) [[1,1]]` |
| N10, head record removed | VALID | MATERIAL_UNAVAILABLE, `(predecessor) [[0,0]]` |
| N10, history emptied | VALID | MATERIAL_UNAVAILABLE, `(history) null` |
| N10, `prev_tx_hash` falsified | INVALID, FORK at 1 | INVALID, FORK at 1 |
| SYNTH-C, ids agree, 0..412, head matches | VALID | VALID |
| SYNTH-C, ids agree, 0..412, head falsified | VALID | INVALID, head contradicts `head_hash` |
| SYNTH-C, ids agree, 0..400 | VALID | MATERIAL_UNAVAILABLE, `(extent) [[401,412]]` |
| SYNTH-C, ids agree, 0..1 only | VALID | MATERIAL_UNAVAILABLE, `(extent) [[2,412]]` |
| SYNTH-C, ids agree, 300..412 | VALID | MATERIAL_UNAVAILABLE, `(self) [[1,1]]` |

Every MATERIAL_UNAVAILABLE reason names the custodian from the context, `FORAY archival node operator` in these fixtures, which is what the text requires and what the earlier build never did.

**What that closes.** W-01a, W-01b, W-01c, W-01d and W-01e on the probe above, and W-02 in code. Contradictions return INVALID, absences return MATERIAL_UNAVAILABLE, the two are not conflated, and the suite is where it was. On the evidence I can produce, the walk now reads the anchored extent when it can find it, binds the declared position to the history, and refuses to answer over material it does not have.

**One thing the probe had to change to test this fairly.** My first synthetic bundles replaced the whole history with a generated chain. Against the patch those return INVALID, reason `record at seq_no 1 is not the anchored transaction`, because the patch binds the history record at the declared `seq_no` to `bundle.anchor.chain_tx_id`. That is the patch working: the fixture had lost the anchored transaction and the new check said so. The SYNTH-C fixtures keep the vector's own two records and extend from there, which is why they are the ones quoted above. The Group B rows still print INVALID for the same fixture reason and should be read that way, not as findings against the patch.

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

`Accepts as closed when` regression modes exist for the five cases above, each returning the outcome in the expected column on the current tree, and the suite stays at 29 of 29.

---

## Status at the author's merge commit

The author reports three changes at `05267a36a57edf31bae2c2b9390f85df9c899a43` on `main`. They are recorded as reported, not as verified: the run against that commit is the next step, and no entry below moves to closed on the strength of a commit message.

| item | what the author reports | my position |
| --- | --- | --- |
| W-01f | a declared `seq_no` outside every anchored segment for its stream now returns INVALID | accepted as the right direction. `SYNTH-D` is the case that measures it, and it is the only one of the 23 that should change outcome |
| W-01h | `chain_tx_id` is compared only for `public_chain` anchors, so repository-class bundles are no longer rejected | accepted as the right direction. No case in the probe exercises it, because no shipped repository vector carries a `stream_context`. The test for it is specified below and not yet run |
| W-04, formerly W-01g | registered separately as a specification question | agreed. The mapping from a readable `stream_id` to the 16-byte field is decided by the text, not repaired in the code, and my entry becomes evidence for that ruling rather than a defect report |
| custody wording | the custodian named in a MATERIAL_UNAVAILABLE is now the stream-history custodian when the context names one | this is the change the wording point asked for. It is visible in the reason string on the 12 MATERIAL_UNAVAILABLE cases and it is the only expected difference in their text |

---

## Still open in the patch as drafted

Three items. The first two were run against patch v0.3. The third is read from the code and is labelled as read. Each carries the author's report, where one exists.

### W-01f. A declared position outside every anchored segment leaves the extent unchecked. Medium. Addressed at `05267a36`, pending my run.

The new binding looks for a segment that contains the declared `seq_no`:

```
const cover = segments.find((g) => g.stream_id === sc.stream_id && Number(g.first_seq) <= seq && seq <= Number(g.last_seq));
if (cover) { ...coverage and head_hash... }
```

When no segment contains the declared position, that block is skipped and the walk returns VALID. SYNTH-D declares `seq_no` 500, anchors one segment covering 0..412, and supplies a continuous history of 100..500. The anchored extent is missing its first hundred records and the verifier says VALID, because the only segment it would have compared against does not contain 500.

Nothing prevents the shape: `seq_no` is never checked against the segments. A fix is to evaluate every segment for the stream rather than only the one containing the declared position, and to treat a declared position outside every anchored segment as a contradiction rather than as silence.

**Author's report at `05267a36`:** the second half of that fix is in. A declared position outside every anchored segment is now INVALID. The rerun should show `SYNTH-D` moving from VALID to INVALID and the other 22 cases holding. If it does, this entry closes. If `SYNTH-D` returns INVALID with a reason that does not name the stream and the declared position, the outcome is right and the diagnosis is not, and that is worth a second line in the reason.

### W-04. The two stream identifiers are not the same type, and the extent branch cannot run while that is true. Medium, and it blocks the fix for W-01f as well. Re-registered by the author from W-01g as a specification question.

`header_echo.stream_segments[].stream_id` is validated as 16 bytes. `stream_context.stream_id` is a readable name in the packet's own vectors: `rotated-seam-stream`, `n10-stream`. The patch matches the two with `===`, so on the packet's encoding no segment is ever found for a shipped bundle and the extent checks never run.

SYNTH-E shows it without ambiguity. It keeps the shipped history, adds a segment covering 0..412, and gives the segment an id different from `stream_context.stream_id`. Had the match worked, coverage would have fired and returned MATERIAL_UNAVAILABLE naming 2..412. It returns VALID. SYNTH-C is the same fixture with matching ids and it does return MATERIAL_UNAVAILABLE naming 2..412. The only difference between the two runs is the identifier.

This needs a ruling at §2 and §5.5.4 on the encoding of the field in both places, plus one vector carrying a `stream_context` and a populated extent with matching ids. Without both, the strongest part of the fix cannot be exercised, and a producer that emits the two in different shapes gets silence instead of a diagnosis.

**Author's ruling of 6 November:** this is a specification question and it is registered as W-04. I agree with the split. As a defect it asks the code to guess which of two encodings the author of a bundle meant; as a question it asks the text to say what the field is in each place, which is answerable once, in one place.

Two consequences of the split, both recorded here rather than assumed. `SYNTH-C` establishes that the extent branch works when the identifiers agree, so the ruling has a working branch to describe. `SYNTH-E` establishes that it does nothing when they do not, so the ruling has a failure it removes. Until the ruling lands, `SYNTH-E` returning VALID is the correct observation and not a regression.

### W-01h. The anchor binding compares against a sentinel that repository-anchored bundles carry. Low. Read, not run. Addressed at `05267a36`, and the test for it is specified below.

`bindToDeclaredPosition` compares the history record at the declared `seq_no` with `bundle.anchor.chain_tx_id`, guarded only against `undefined`. The packet's repository-anchored vectors carry the literal `"unused-for-repository-class"` in that field. A `checkpointed_repository` bundle that carried a `stream_context` would therefore return INVALID, reason `history record at seq_no N is not the anchored transaction`, whatever its history held. No vector exercises it, because none of the five repository vectors carries a `stream_context`. The guard should be `assurance_class`, or the presence of a real hash.

**Author's report at `05267a36`:** the comparison now applies only to `public_chain` anchors, which is the second of the two options and the better one, because it keys on what the bundle claims rather than on the shape of a value.

No case in the probe exercises this, and the reason is worth writing down rather than leaving to memory: the packet ships five repository vectors and none of them carries a `stream_context`, so the branch that would have rejected them cannot be reached from the packet as shipped. The test that reaches it is: take `checkpointed_repository/<a vector that validates>`, add the `stream_context` from `rotated-chain-seam` with its history, keep `anchor.chain_tx_id` at `"unused-for-repository-class"`, and expect VALID before the change and VALID after it, with the anchored extent compared normally. Before the change that bundle returns INVALID, reason `history record at seq_no N is not the anchored transaction`, whatever its history holds. That expectation is falsifiable in both directions, so the case is worth adding to the probe the moment a repository vector and a `stream_context` can be put in one bundle.

### One wording point

The custody named in the MATERIAL_UNAVAILABLE reason is `context.custodian`, which in these fixtures is the archival node operator. The material that is missing is stream history, whose custodian may be the producer rather than the node that stores it. The text should say which one the consumer is expected to ask, since the reason string is the only actionable part of the outcome.

**At `05267a36`:** the reason now names the stream-history custodian when the context names one. On the 12 MATERIAL_UNAVAILABLE cases the expected effect is confined to the closing clause, `responsible custodian: FORAY archival node operator` giving way to the named stream-history custodian. The outcome, the check number and the missing range should all hold. The clause is the part to read closely, because it is the part a consumer acts on and the part that no outcome column shows.

---

---

## W-02. Missing history returns VALID, and the text does not yet say what it should return. Medium, and partly textual.

**Status: closed in code by the patch, still open in the text.** The patch returns MATERIAL_UNAVAILABLE when a bundle declares a `stream_context` and supplies no history, and the probe confirms it. What follows is the part the patch cannot settle.

### What happens

`const history = context.streamHistory ?? []; if (history.length > 0) { ...walk... }`. Zero records means the walk is skipped, and a skipped walk is indistinguishable from a clean one. Nothing in the base build produces MATERIAL_UNAVAILABLE for absent stream state; the patch does, which is what closes this entry in code.

The sharpest form of this is on a shipped vector. `negative/N10-backdated-insert-fork` exists to catch a fork at check 10. As shipped it returns INVALID, check 10, continuity FORK. Remove the record that proves the fork and the same bundle returns VALID. Empty the history and it returns VALID.

### Why this is a text question as much as a code question

The outcome taxonomy at amendment v0.25 §10.1 defines MATERIAL_UNAVAILABLE for a missing blob, a missing tree and a missing salt. It does not name missing stream history. A verifier implementer reading the published text therefore has no instruction that an absent history maps to MATERIAL_UNAVAILABLE, and the reference implementation's silence is consistent with the text as written.

That makes this a specification question first and an implementation gap second, which is why the entry asks for a ruling rather than only a patch. I do not know which way it should go, and I am not asserting what the author's position is; I record it as open. What I can say is that §3 requires the outcomes not to be conflated, and that a stream whose history is entirely absent currently reaches the same verdict as a stream that was checked and found clean.

### Minimal fix

The code half is done in the patch: MATERIAL_UNAVAILABLE when `stream_context` is present and no history is supplied. What remains is the text. If the ruling is that absence maps to MATERIAL_UNAVAILABLE, name stream history alongside the missing material in §10.1, with the same custodian-naming requirement. If the ruling is otherwise, the patch's new branch is the thing that has to change, and the entry becomes a text clarification only.

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

Two commands. The first applies the patch to a clean copy of the archive, runs the suite, then the probe:

```
apply-and-run.sh <patch-file>
```

The second runs the probe on any tree, patched or not:

```
node foray-probe.mjs "<folder containing lib and vectors>"
```

Twenty three cases in five groups. Group A holds the bundle internally valid and varies only the history. Groups B to E are synthetic, because the packet ships no bundle that carries both a `stream_context` and a populated `stream_segments`. Group B replaces the history wholesale and is the fixture the patch's anchor binding correctly rejects, so its rows are quoted only as that. Group C keeps the vector's own records and matches the two stream identifiers. Group D puts the declared position outside the anchored segment. Group E mismatches the two identifiers deliberately.

Base archive, `b890d2c`, Node v22.22.3. Every case returns VALID except two: N10 as shipped, and N10 with the declared `prev_tx_hash` falsified. Both return INVALID at check 10 for the FORK in the history, which is the fork the walk does catch.

With the patch applied, 29 of 29 conformance tests pass and the probe prints:

```
rotated-chain-seam: as shipped                        VALID
rotated-chain-seam: tail record removed               MATERIAL_UNAVAILABLE  (self) [[1,1]]
rotated-chain-seam: head record removed               MATERIAL_UNAVAILABLE  (predecessor) [[0,0]]
rotated-chain-seam: history emptied                   MATERIAL_UNAVAILABLE  (history) null
rotated-chain-seam: declared prev_tx_hash falsified   INVALID  contradiction
N10: as shipped                                       INVALID  check=10  FORK at seq_no 1
N10: tail record removed                              MATERIAL_UNAVAILABLE  (self) [[1,1]]
N10: head record removed                              MATERIAL_UNAVAILABLE  (predecessor) [[0,0]]
N10: history emptied                                  MATERIAL_UNAVAILABLE  (history) null
N10: declared prev_tx_hash falsified                  INVALID  check=10  FORK at seq_no 1
SYNTH extent 0..412, history 0..412, head matches     INVALID  anchor binding, fixture artefact
SYNTH extent 0..412, history 0..412, head falsified   INVALID  anchor binding, fixture artefact
SYNTH extent 0..412, history 0..400                   INVALID  anchor binding, fixture artefact
SYNTH extent 0..412, history 300..412                 MATERIAL_UNAVAILABLE  (self)
SYNTH extent 0..412, history [412]                    MATERIAL_UNAVAILABLE  (self)
SYNTH extent 0..412, history []                       MATERIAL_UNAVAILABLE  (history)
SYNTH-C ids agree, history 0..412, head matches       VALID
SYNTH-C ids agree, history 0..412, head falsified     INVALID  head contradicts head_hash
SYNTH-C ids agree, history 0..400                     MATERIAL_UNAVAILABLE  (extent) [[401,412]]
SYNTH-C ids agree, history 0..1 only                  MATERIAL_UNAVAILABLE  (extent) [[2,412]]
SYNTH-C ids agree, history 300..412                   MATERIAL_UNAVAILABLE  (self) [[1,1]]
SYNTH-D declared seq 500 outside segment 0..412       VALID
SYNTH-E segment id and stream_context id differ       VALID
```

Both output files and the patch itself are kept with the review rather than pasted into this document, so that the figures above can be re-derived without trusting the transcription.
