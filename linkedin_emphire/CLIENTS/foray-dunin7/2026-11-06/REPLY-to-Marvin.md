# Reply to Marvin, 6 November

LinkedIn message. Attach `FINDINGS-02-register-entries-v2.md` and `foray-probe.mjs`.

---

Marvin,

All six of your corrections are in. Revised file and the probe attached.

What changed. I state exactly what reproduced and how: N10 and rotated-chain-seam with nothing touched but the context, plus your W-01c. a, b and d were walk-level only in the version you read; that caveat is now in the file, and the table says what each case should return once the walk reads the extent. The W-02 sentence that put a position on you is gone, and that entry is recorded as open rather than resolved. The fix semantics are written the way you put them: a falsified `prev_tx_hash` or a `head_hash` mismatch is a contradiction and returns INVALID, an absent or short history returns MATERIAL_UNAVAILABLE, and §3 does not let the two share a verdict. The Verifier Specification citations are §3 and §8.5; §10.1 is cited only as the outcome taxonomy in the amendment. "The same three lines" now says four, and the four listed are the four there. W-01c is described as contradicting the history it is checked against, not itself. The "reclassified one entry" clause is deleted. W-03 is scoped to foray-api JavaScript outside tests, conformance and vendored code.

Two things to know before you run the probe on the patch.

First, the packet has no bundle carrying both a `stream_context` and a populated `stream_segments`. So a, b and d cannot be run on a shipped vector, and that is why they were walk-level findings. I built one: rotated-chain-seam with a single segment claiming 0..412, the anchored value recomputed from the new header, both canned sources updated to match. Those cases are marked SYNTH. The control is a complete history 0..412 ending on the segment's head, and it returns VALID on the unpatched tree, so the probe is capable of passing. Everything else against that bundle also returns VALID today, including an empty history and a head that contradicts the anchored head_hash. The missing combination is worth a vector in the packet, separately from this.

Second, and this is the one that will bite. If the patch returns MATERIAL_UNAVAILABLE for an empty history before the rest of check 10 has run, N11 goes red. N11 carries a `stream_context`, an empty history, and a `_ref` that postdates the claim, and expects INVALID with INVALID-CHRONOLOGY. I applied a throwaway fix of that shape to test the probe and got 28 pass and 1 fail, the one fail being N11. Contradictions inside check 10 have to be evaluated before the material return.

The patch has not reached me. The WP-1 zip, the conformance zip and the entries file all arrived; nothing since the conformance zip on 4 November, and nothing in the mailbox. Attaching it to this message will get it here. I will check the SHA-256 against the one you sent before I run anything against it.

Probe runs as `node foray-probe.mjs "<folder containing lib and vectors>"`. Sixteen cases, one line each, no dependencies. SHA-256 is in the header of the findings file.

Olusanya
