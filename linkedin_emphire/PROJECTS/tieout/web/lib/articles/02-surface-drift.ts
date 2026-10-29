const body = `
## Two runs, one suite, pre-assigned ids

LLM output is stochastic at the surface. The same prompt, the same model, the same temperature can produce different wording on every call. An eval that only looks at the surface will report noise as signal, or worse, signal as noise. The stability pair in this repository is the control for that problem: the same F1 suite, run twice, against the same deterministic sample agent, with only the surface-drift seed changed. Seed 0 in [runs/demo-stability/a](/runs/demo-stability/a), seed 7 in [runs/demo-stability/b](/runs/demo-stability/b).

The comparison is not a diff of text. It is an alignment by pre-assigned id. Every item in a tieout suite has an id assigned before the attempt, so two runs of the same suite line up one-to-one by construction. There is nothing to match heuristically, and nothing that can silently drop.

## The numbers

Aligned: fourteen items. Verdict flips: zero. Transcript drift: ten of fourteen. Stability: 1.000.

Read that again. The wording of ten out of fourteen raw outputs changed between the two runs, and not one verdict moved. The drift is real, it is measured, and it is reported separately from the verdict layer. That separation is the whole design: surface change and decision change are different quantities, and conflating them is how a flaky transcript gets misread as an unstable policy.

The command is one line:

\`\`\`bash
tieout diff runs/demo-stability/a runs/demo-stability/b
\`\`\`

and the output the CI gate checks for is exactly:

\`\`\`
  aligned    : 14 items (by pre-assigned id)
  verdicts   : 0 flipped, 14 stable  ->  stability 1.000
  transcripts: 10 drifted without a verdict flip
\`\`\`

## Why the pair is committed

A stability claim you cannot re-run is a story. The pair is committed to the repository, both bundles verify, and the diff is recomputable from them by anyone. The stability figure, the flip count, and each run's pass rate with its exact confidence interval (13 of 14, interval [0.6613, 0.9982] on both sides) are stored in the manifests, so the site and the pipeline read the same numbers from the same records.

## What it does not claim

Determinism of the sample agent means this pair measures the harness and the record format, not a live model's stability. For a live agent, the same procedure applies: run the suite twice with a recorded seed, align by id, and report verdict flips and transcript drift as two rows. If your verdicts flip on surface change, you do not have a measurement yet. You have a mood.
`;

export { body };
