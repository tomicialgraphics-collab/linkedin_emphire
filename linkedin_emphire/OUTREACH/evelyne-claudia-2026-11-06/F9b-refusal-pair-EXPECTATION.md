---
deliverable: expectation
id: F9b-refusal-pair-expectation
date: 2026-11-06
audience: external
status: ready
approved: no
profile_checked: >-
  Evelyne-Claudia Yantony, from her correspondence of 2026-11-06. She separates artifact
  correspondence from independent reproduction, treats a validation finding as earned by evidence and
  open to correction including her own, and asked for the genuine verdict-write refusal as a separate
  cell with five surfaces named. This expectation is written before the run, in her order, so that the
  run can fail it.
thread: F9b, the verdict-write refusal against the conflict-write refusal, one run, five surfaces
---

# Expectation, written before the run

The cell: the benchmark's own failpoint, refusing a verdict write, on the unpatched store. Compared
against the conflict refusal already measured, in the same run and on the same machine, so that no
number in the comparison comes from a different day or a different copy.

Five surfaces, in her order. Each gets a prediction and each prediction is falsifiable.

| Surface | Verdict refusal predicted | Conflict refusal predicted | Differ? |
| --- | --- | --- | --- |
| Refused operation | the first verdict write, `kind` verdict at seq 4 | the conflict annotation, `kind` conflict | yes |
| Durable records | no verdict records at all, the journal holds issue and commitment only | two signed verdict records, no conflict record | yes |
| Reply text | `ok: false`, `durable: false`, error names a refused verdict write | identical text | **no** |
| Host diagnostics | the host's seed is refused, so its own verdict is the first write attempted and is refused as well | the annotation is refused after two verdicts are durable | yes |
| Replayed state | not `conflicted`, because there are no two verdicts to disagree | `conflicted`, recomputed from the two differing records | yes |

## The claim under test

The finding was that a refused conflict write is reported in the words of a refused verdict write. If
the reply surfacing is genuinely the same in both cells, the two refusals are indistinguishable *at the
reply* and distinguishable everywhere else. That is the strongest form of the finding and the one worth
measuring, because it means a client reading the reply cannot tell which write was refused even when
the difference is total.

If instead the replies differ, the finding narrows to a wording defect: the conflict refusal borrows the
verdict refusal's sentence without borrowing its circumstances, and the sentence is wrong only because
it is uninformative, not because it is false about the wrong object.

Both outcomes are results. The second is a smaller claim and I would rather have it than a larger one
that the evidence does not support.

## What this run will not establish

That the patch is correct. That either refusal is right in the specification's terms. That any client,
operator or runbook would retry. It measures what the two refusals look like from the outside, with
pinned source hashes, and nothing more.
