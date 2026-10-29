# Method note

## The gap, in one paragraph

The 2026 tooling landscape is crowded in three layers and empty in the
fourth. Attacks are commoditized (garak, PyRIT, promptfoo, DeepTeam,
Giskard, AgentDojo). Evals are commoditized at the scoring level
(OpenAI Evals, DeepEval, Inspect AI, LangSmith, Braintrust, Phoenix).
Taxonomy is standardized (OWASP Top 10 for Agentic Applications, MITRE
ATLAS, NIST AI RMF). Evidence is empty: every tool uses a judge that
lives inside the tool. The evaluator and the evaluated share an
operator. A green eval from such a tool is a self-grade, which is
exactly the failure the lane has been naming: no judge is uniformly
reliable (RAND, 2026), verdicts flip on reformatting and verbosity,
judge upgrades are not interchangeable, and where raw outputs were not
shipped, the debate numbers cannot be re-audited. Nobody in the
landscape emits an artifact that survives contact with a stranger.

## The six pillars, as doctrine

1. **Verdict event.** One record per check result, with the four-part
   binding: action, policy version, decision, effect reference. The id
   is assigned before the attempt, so the record can name the absence.
2. **Provenance.** Exact harness version, model, model version, dataset
   hash, environment snapshot, decoding config, seed, and the resolved
   endpoint of every judge call.
3. **Negative controls.** Every suite carries known-pass and
   known-fail items the check does not generate. The check cannot write
   its own grade; the harness's false-positive and false-negative rate
   for the run is in the manifest.
4. **Named gaps.** Anything that could not be verified is recorded with
   reason and scope. A bundle with a named gap is more honest than a
   green bundle; the format makes the difference mechanical.
5. **Re-derivation.** `verify` re-checks the hash chain, re-hashes the
   manifest, re-derives every verdict from the raw outputs, and measures
   judge divergence, without re-running the model. The bundle either
   passes a stranger's verify or it does not exist, as far as this
   project is concerned.
6. **Judge audit.** Every run carries the judge's own numbers:
   agreement on calibration anchors, perturbation flips (reformat,
   paraphrase, verbosity), disagreement rate, self-preference probe.
   Who checks the checker, made mechanical.

## How to read a bundle

1. Read the manifest first: who ran what, under which policy hash, with
   which dataset hash, and how many controls FP/FN.
2. Read the named gaps before the verdicts. A gap is a finding about
   the evidence path, not about the target.
3. Read the metric with the denominator: "1 of 6" is a claim about six
   specific items; the raw for each is in the chain.
4. Read the judge audit last, and treat its numbers as the price of
   trust in the detectors.
5. Verify. The verify output is the only verdict this project attaches
   to its own work: PASS means a stranger, with only the bundle file
   and the check definition, re-derived everything.

## Reproducibility, stated precisely

For a deterministic agent (the sample OrderBot), verdicts and item ids
are stable across runs. Timestamps, record hashes, and the manifest
tail differ per run: a bundle records when it was made. Integrity is the
hash chain; re-derivation is the test; determinism of the timestamps is
not the claim and is not needed.

## What this is not

Not another probe library. Not another dashboard. Not a judge model.
Not a compliance platform. It emits the record those things consume.
