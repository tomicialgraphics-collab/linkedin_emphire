const body = `
## A matrix is a claim until it runs

The failure-mode matrix in this repository describes four failure modes of decision-time evidence in an agent:

- **E, evidence at decision time.** The agent decides on evidence it should not have, or without evidence it should have.
- **P, persistence across a session boundary.** A decision re-requested after a boundary (a restart, a compaction) should stand on the same evidence, not reinvent itself.
- **R, recovery from a failed lookup.** When a tool call fails mid-flow, the agent should degrade in a recorded way, not fill the gap with a guess.
- **V, independent verification of an asserted outcome.** When the agent asserts something happened (a refund was issued), the claim should be checkable against an independent signal, not self-certified.

A matrix like this is easy to write and easy to ignore. Family F2 is the same matrix with teeth: each row becomes a check, and each check becomes two items, one where the sample fixture makes the designed break and one where it makes the documented hold.

## Eight items, eight controls, one audit

The committed run, [runs/demo-f2](/runs/demo-f2), executes all eight items: E1-broken, E1-hold, P1-broken, P1-hold, R1-broken, R1-hold, V1-broken, V1-hold. Four fail, four pass. That is the expected result on the sample fixture, because the "broken" items are designed to break: the detector fires, the verdict is fail, and the record says so. The "hold" items pass. The family's eight negative controls report zero false positives and zero false negatives, which is what it means for the detectors to be calibrated on this fixture.

The pass rate on this family is 4 of 8, and the manifest stores the exact interval for it: [0.157, 0.843]. Anyone reading the site sees the width of that interval next to the number. A small family is not a precise measurement, and the record does not pretend otherwise.

## The judge audit travels with the family

F2's judge audit measured 12 anchors, with full agreement between the detector and the expected labels, zero flips under perturbation, and a disagreement rate of 0.4167 against the naive one-tell variant of the detector. That last number is not a defect being hidden. It is the price of a simple judge, measured on every run, in a place where it cannot be smoothed away. See [auditing the judge](/blog/auditing-the-judge) for what each of those four quantities is.

## Point it at a live agent

For a live agent, the same prompts go out and the verdict is the measurement, not the label. The break scenarios stop being "designed breaks on a fixture" and become "did this agent actually hold its evidence discipline". That is the intended use of the family, and it is why the matrix, the items, the controls, and the audit all ship in one executable unit instead of a slide.
`;

export { body };
