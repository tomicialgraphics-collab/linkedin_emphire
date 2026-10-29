const body = `
## Who checks the checker

Every family in this harness carries a judge audit, computed on every run and stored in the bundle as a first-class record. The judge here is the family's detector set, and the audit measures four quantities, all fully offline:

- **anchor agreement.** The detector runs over crafted, versioned anchor raws with known expected labels (the family's controls plus declared extra anchors). Agreement is detector versus label.
- **perturbation flips.** Each anchor raw is perturbed in three ways: reformat, paraphrase, verbosity. A verdict that flips under surface change is a case-sensitive judge, and the flip count is the number.
- **disagreement rate.** The primary detector is run against a naive one-tell variant of itself. The disagreement rate is how often the lazy variant diverges, which measures how much the primary's design is actually doing.
- **self-preference probe.** The judge's own marker string is injected into the raws. If any verdict changes because the judge sees its own name, the probe fails.

## The committed numbers

The F1 run (runs/demo) reports: fourteen anchors, agreement 1.0; fourteen perturbation samples, with three flips under paraphrase and zero under reformat or verbosity; disagreement rate 0.0714 (one of fourteen); self-preference clean. The three paraphrase flips are named in the record, anchor by anchor: F1-CTRL-T1-BROKEN, F1-CTRL-T4R1-BROKEN, and F1-ANCHOR-1. A flip is not hidden as an average. It is a line in the bundle.

The F2 run (runs/demo-f2) reports: twelve anchors, agreement 1.0; zero perturbation flips across all three perturbations; disagreement rate 0.4167 (five of twelve); self-preference clean. The 0.4167 is the highest number on the page, and it is the point: on F2's anchors, the naive one-tell variant disagrees with the primary detector on five of twelve cases. The primary is doing something the lazy version cannot, and the audit says how much, every run.

## Why the audit is a record, not a report

Because it is in the bundle, it verifies with the bundle. A stranger running verify re-checks the chain that includes the audit record. Because it is computed on every run, a future judge change shows up as a number moving, not as a vibe. And because the naive variant is part of the measurement, the audit doubles as documentation of why the detector is built the way it is: here is the baseline, here is what beats it, by how much.

The selftest runs the same audit offline with the same expected numbers (point 7), so the audit's arithmetic is itself tested before it is trusted.
`;

export { body };
