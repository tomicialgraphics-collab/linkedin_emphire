const body = `
## The judge cannot write its own grade

Every detector in this harness is a heuristic, and a heuristic judge is only as good as the evidence that it is calibrated. The evidence is not a benchmark run. It is the negative control: items the suite ships that it does not generate, with labels the detector did not produce.

A control comes in two kinds:

- **known-hold.** A crafted raw that must not fire the detector. If it fires, that is a false positive, and the run records it.
- **known-broken.** A crafted raw that must fire it. If it does not, that is a false negative, and the run records it.

All control raws are crafted and versioned. None is model-generated, because the whole point is to test the detector on inputs it had no hand in making. The run's manifest stores the totals: how many controls, how many false positives, how many false negatives. In all four committed runs, the number is the same: eight controls, zero false positives, zero false negatives.

## Why this is the load-bearing part

A green result from a judge with no controls is a self-grade. The detector scored its own homework and reported 100 percent. The control inverts the dependency: the labels exist independently of the detector, so the detector's errors are measurable in the same run as the verdicts it produces. FP and FN per run, next to the pass rate, in the same manifest.

The harness selftest checks the same property from the other side (point 4: negative controls clean, fp=0 fn=0), so a regression that makes a detector sloppy or over-eager fails the pipeline before it can produce a single misleading bundle.

## What a control cost does to a result

It is worth being plain about the trade. Controls add items that are not questions about the agent. They are questions about the judge. A run that spends eight of its twenty-two records on calibration is saying: before you trust the fourteen verdicts, here is the evidence that the thing emitting them can be wrong, and here is how often it was, on inputs where we know the answer.

That is the difference between an eval that grades and an eval that can be graded.
`;

export { body };
