---
deliverable: correction-note
id: F9b-CORRECTION-03
date: 2026-11-06
audience: external
status: ready
approved: no
profile_checked: >-
  Evelyne-Claudia Yantony, from her correspondence of 2026-11-06. She keeps three events apart,
  treats validation as earned by evidence and open to correction including her own, prefers a
  terminology that keeps two comparisons distinct, and asks for a cell that examines five named
  surfaces. This note answers in her order and records one falsified prediction of mine.
thread: F9b, terminology, the source-hash guard, and the verdict-write refusal measured against the conflict refusal
---

# F9b, correction 03

Four things. Two are yours and I have taken them, one is a run I had said was worth doing, and one is a
prediction of mine that the run falsified.

## 1. The terminology, adopted

You are right that the two comparisons must not share a phrase.

**Wire cells.** Sequence 4 is BLOCK, sequence 5 is ALLOW. The disagreement is in the **verdict value**.

**Host cells.** Both records carry BLOCK. The disagreement is in the descriptor and the decision time.
These are **different signed verdict records**.

"Different verdict values" is now used only for the wire pair, and "different signed verdict records"
only for the host pair. The sentence in correction 02 that said both pairs were two different verdicts
for one action id is accurate but flat, and it is superseded by this one wherever the two are compared.

## 2. The guard, accepted and built

Your qualification is correct and it was a hole in my method. A matching patch line establishes that the
expected text is present. It says nothing about the rest of the file, and a run that patches by string
match alone would measure a tree it cannot name.

The new runner verifies the SHA-256 of `bench/store.py`, `bench/host.py` and `bench/common.py` against
the hashes this case names, and it verifies the patched `store.py` against the hash the first run
printed, before it measures anything. Both failures are refusals, not warnings.

The negative control is the part that matters, because a guard that has never refused anything proves
nothing. One comment line was appended to a copy of `store.py`, a change no reviewer would see, and the
runner answered `refusing to run: bench/store.py is aecd4aee...77627, expected 99f25cab...1f982`, then
exited 1. The full output is beside this note.

The first runner is unchanged, deliberately. Its hash is already in your hands and in the message that
carried it, and editing it would break the artifact you hold rather than fix it. The guard lives in the
new runner, which is the one to use from here.

## 3. The verdict-write refusal, measured against the conflict refusal

One run, one machine, one copy of the benchmark, both refusals measured side by side so that no number
here comes from a different day. Your five surfaces, in your order.

| Surface | Verdict write refused | Conflict annotation refused |
| --- | --- | --- |
| Refused operation | the first verdict write, at seq 4 | the conflict annotation, after two verdict writes |
| Accepted writes before the refusal | 0 | 1 |
| Durable records | no verdict records at all | two signed verdict records, digests recompute, no conflict record |
| The refused reply | `ok: false, durable: false, error: "injected: the journal refused a verdict write"` | **identical text** |
| Host diagnostics | `wal_commit, reply_rejected, effect_withheld` | **identical** |
| Replayed state | `verdict_state` null, no conflict entry | `conflicted`, recomputed from the two differing records |

## 4. The prediction the run falsified

The expectation was written before the run and it predicted that the host diagnostics would differ
between the two cells. They do not. The host records the same three event kinds when a verdict write is
refused as when a conflict annotation is refused, and that is a stronger form of the original finding
than the one I wrote down.

So the reply is not the only surface that fails to separate the two refusals. The host's own record of
what happened does not separate them either. What does separate them is what a reader has to go looking
for: the durable records, the count of accepted writes, and the state a replay recomputes. Everything a
consumer is handed in the moment looks the same.

The smaller claim survives and is the one to keep: a refused conflict write is reported in the words of
a refused verdict write. The larger claim that the two are indistinguishable is still not one I will
make, because they are distinguishable, just not by anything the system says at the time.

## 5. "Yours to give or withhold", withdrawn

Your wording is better and I have adopted it. Validation is earned by the evidence, bounded by the
tested claim, and open to correction, including your own assessment of your own work. Nothing about
that is mine to hand over, and the sentence in the last reply implied a discretion that neither of us
has.

Correspondence, reproduction and validation remain three events. This note records the first, supplies
what the second needs, and claims nothing about the third.
