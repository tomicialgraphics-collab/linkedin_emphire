# Reply to Marvin, second message, 6 November

LinkedIn message. Attach `FINDINGS-02-register-entries-v3.md` and `foray-probe.mjs`.

---

Marvin,

Got it. `foray-streams-fix-b890d2c-v0_3.patch`, SHA-256 `3fca8c72...41e0`, matches the one you gave me. Applied clean with `git apply` to a fresh copy of `b890d2c`, no fuzz, one file changed.

**The suite does not move.** 29 tests before, 29 after, 0 fail. N11 stays INVALID with INVALID-CHRONOLOGY, which is the ordering you built in and it holds.

**Closed on my probe: W-01a, b, c, d, e, and W-02 in code.**

- History emptied: MATERIAL_UNAVAILABLE, `(history)`, custodian named.
- Tail removed or declared record missing: MATERIAL_UNAVAILABLE, `(self) [[1,1]]`.
- Head removed: MATERIAL_UNAVAILABLE, `(predecessor) [[0,0]]`.
- Extent 0..412 with the history stopping at 400: MATERIAL_UNAVAILABLE, `(extent) [[401,412]]`, with a control case at full coverage returning VALID so the probe can pass.
- `prev_tx_hash` falsified: INVALID, contradiction. Head contradicting `head_hash`: INVALID, contradiction.

Contradiction and absence are separate, as §3 requires. That was the point of the exercise and it is now true of the code.

**Three items still open. Two are run, one is read.**

W-01f. The extent block only runs when a segment contains the declared `seq_no`. Declare `seq_no` 500, anchor one segment covering 0..412, supply a continuous history of 100..500, and the answer is VALID while a hundred records of the anchored extent are missing. `seq_no` is never checked against the segments at all.

W-01g, and this one matters more. `header_echo.stream_segments[].stream_id` is validated as 16 bytes. `stream_context.stream_id` is a readable name in your own vectors, `rotated-seam-stream`, `n10-stream`. You match them with `===`, so on the packet's encoding no segment is ever found and the extent branch never runs. I have two fixtures that differ only in the identifier: one returns VALID, the other returns MATERIAL_UNAVAILABLE naming 2..412. This needs a ruling at §2 and §5.5.4 on the encoding in both places, and one vector carrying a `stream_context` with a populated extent. Until then the strongest part of the fix cannot be exercised, and a producer that emits the two in different shapes gets silence instead of a diagnosis.

W-01h, read from the code, not run. The binding compares against `anchor.chain_tx_id` guarded only by `undefined`, and your repository vectors carry the literal `unused-for-repository-class` there. A `checkpointed_repository` bundle with a `stream_context` would return INVALID whatever its history held. No vector carries that combination, so nothing catches it.

One wording point. The reason names `context.custodian`, which is the archival node operator. The missing material is stream history, whose custodian may be the producer. Say in the text which one the consumer should ask, because the reason string is the only actionable part.

Before you read my file: my first synthetic fixtures replaced the history wholesale, and your anchor binding correctly rejected them as `record at seq_no 1 is not the anchored transaction`. Those rows are labelled a fixture artefact, not a finding. The fixtures I quote are the ones that keep the vector's own records.

Probe now carries 23 cases, SHA-256 `c91be299...a326`. Say the word on f, g and h: register them separately or fold them into this fix.

Olusanya
