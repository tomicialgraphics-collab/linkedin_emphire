---
deliverable: correction-note
id: F9b-CORRECTION-04
date: 2026-11-06
audience: external
status: ready
approved: no
profile_checked: >-
  Evelyne-Claudia Yantony, from her message of 2026-11-06 22:13. She separates an observation from the
  instrument that produced it, keeps evidentiary status unchanged until reproduction, and reads a result
  at the strength the instrument supports. This note answers her four qualifications in her order and
  reports a measurement that changed one of my sentences.
thread: F9b, wire bytes, full host records, the renamed count, and the provenance of each surface
---

# F9b, correction 04

Four qualifications, all of them right, and one of them changed a sentence rather than a word.

## 1. Parsed JSON is not the wire, and you were right to say so

The comparison in the last package sorted keys and compared the parsed objects. That establishes that two
clients receive equal JSON values. It does not establish that they receive the same bytes, and a client that
reads the raw stream before parsing would be entitled to care about the difference. My sentence said
byte-identical while the instrument measured something weaker, which means the sentence was unsupported
whether or not it happened to be true.

The runner now keeps the bytes. The earlier runner's call reads the reply and discards the bytes, keeping
only the parsed value, so the exchange is performed by a recorder that does the same socket read and retains
what was read. Nothing else in the imported runner is touched, and its hash is verified before import, so
"nothing else changed" is checkable rather than asserted.

**The measurement.** Both refused replies are 90 bytes and hash to
`1ca16a0ad93f2650f6163c9fe128ea84ed4297321c598d6c35ed18fbaa3c01c7`, with the trailing newline included.
The retried replies are equal to each other in the same way. So the stronger claim now stands on a
measurement at the socket rather than on an inference from a parsed object, and the weaker claim it replaces
is withdrawn.

## 2. Kinds are not records, and the first attempt at full records failed

Same correction, second surface, and here the measurement disagreed with me.

The runner now compares complete host event records. The first attempt, with the two cells carrying the
action ids this case assigned them, `F9-P0002` and `F9-V0002`, reports the full records as **different**.
Every field agrees except `action_id` and the `problems` string inside `reply_rejected`, which quotes the
action id in its text. That difference is the fixture, not the system: I gave the two cells different
identities and then compared their fingerprints.

The run is repeated with both host cells carrying the same action id, the work directories and journals
being separate. Under that condition the full records are identical in every field, not merely in kind.

**What this does to the earlier sentence.** "The host records the same three event kinds" was true and
narrow. "The host's own account of what happened does not separate the two" was broader than any
measurement I had, and the record-level comparison is what licenses it, but only for two runs of the same
action id. Both runs ship, with the shared-id run as the comparison and the distinct-id run as the evidence
for why the fixture had to change.

## 3. The count, renamed

"Acknowledged verdict requests" replaces "accepted verdict writes", and it is reported separately from the
durable record count rather than beside it in the same sentence:

| | Conflict refusal | Verdict refusal |
| --- | --- | --- |
| Acknowledged verdict requests | 1 | 0 |
| Durable verdict records | 2 | 0 |

The two numbers answer different questions. The first is what the store told the caller it had accepted.
The second is what survives a restart and can be produced for an auditor.

## 4. Reproduction, named rather than described

The earlier runner this package imports is `F9b-conflict-write.py`, 17,594 bytes, SHA-256
`991e9eec09c291bf0179b6677577c5929b688df0b2b2c10fea2cc163d669e891`. The new runner refuses to import it if
that hash does not match, so the identity of the instrument is enforced rather than stated.

The benchmark source bytes that match the three named hashes travel in the same archive: `bench/store.py`
21,077 bytes, `bench/host.py` 15,652 bytes, `bench/common.py` 3,223 bytes. They are checked before use, and
the patched copy must hash to the value the earlier run printed or nothing is measured.

## 5. Wire and host, kept apart

The result file now has separate `wire`, `host`, `records` and `state` sections, and each surface carries a
`provenance` field naming the file, the function and the hash that produced it. A reader no longer has to
infer which runner produced which number.

## 6. The guard, as you put it

A comment-only change should fail a byte-identity check even when behaviour is unchanged, and the negative
control did exactly that. Its refusal is the guard working, not a false positive, and the useful question is
whether a tree that is genuinely identical can be made to fail. If you find such a tree, the guard is what
is wrong.

## 7. Your two principles

Both are accepted as candidate principles, with the second one naming the mistake I made twice in this
thread. Observational equivalence at one surface does not establish equivalence across the system's
consequential state. A refusal is not fully examined until its observable response, its durable effects and
the subsequent system state have been considered separately.

Nothing here amends frozen REACHABLE™, and nothing here upgrades the evidentiary status of the result.
