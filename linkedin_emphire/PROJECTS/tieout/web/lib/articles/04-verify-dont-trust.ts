const body = `
## The stranger test

An evaluation result is only as strong as the check a stranger can perform on it. In this repository, the stranger check is a command:

\`\`\`bash
tieout verify runs/demo
\`\`\`

No model. No API key. No network. The verifier reads the bundle, walks the hash chain, re-hashes the manifest, re-runs the detectors on the stored raw inputs and outputs, re-derives the statistics, and prints what it found. The output on the committed F1 run is:

\`\`\`
tieout verify: runs/demo
  format : tieout-bundle/v1
  run    : 20261029T211725Z-bdce11
  agent  : sample:deterministic-orderbot
  chain  : 22 records, intact
  file   : sha256 match
  items  : 14/14 pre-assigned ids present
  re-derive: 14/14 verdicts re-derived from stored raw
  controls: 8 re-derived, 0 FP / 0 FN
  gaps   : none
  VERDICT: PASS (re-derivable by a stranger)
\`\`\`

## What the chain actually is

Every record in the bundle carries the hash of the record before it, and its own hash. The manifest fixes the tail of the chain, and a file-level sha256 sits outside the file. That is three layers, each catching what the others miss:

- one character changed anywhere in the file breaks the chain (G-HASH),
- a dropped line breaks the expected item set and the tail (G-MISSING plus G-HASH),
- a moved or duplicated record shows up as a count or id mismatch.

The harness selftest proves both directions before any run happens. Point 5 takes a clean bundle and tampers one character: the verifier detects it. Point 6 drops a line: the verifier reports the missing item and the broken tail. If verify cannot catch tampering on a bundle the harness itself just wrote, it has no business judging anything else.

## What verify refuses to do

It does not call a model, so a judge upgrade cannot change what a bundle means after the fact. It does not touch the network, so verification works in a review room, an air-gapped lab, or a terminal. It does not rewrite the record: a failing verify prints the named gaps (the G-codes, with scope and reason) and leaves the bundle alone. A gap is a statement of what could not be checked, which is more useful than a silence.

## Why this is a security property

The security claim here is not "the agent is safe". It is "the record is what the record says it is". Every other claim in an evaluation pipeline rests on that floor: if a stranger cannot re-derive your verdicts from your own stored raw, then your verdicts are opinions, however confident the tool that produced them was.
`;

export { body };
