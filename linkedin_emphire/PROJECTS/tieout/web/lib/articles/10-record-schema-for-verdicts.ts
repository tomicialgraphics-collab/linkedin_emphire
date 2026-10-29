const body = `
## One record per decision, append-only

The bundle format is a design exercise in making a verdict tamper-evident and re-derivable. The shape: one JSONL file. Line one is the manifest. Every subsequent line is a record: a verdict event, a control event, a judge audit, or a named gap. Each record carries the hash of the record before it and its own hash. Nothing is ever edited in place. Corrections are new records, or they are gaps.

## Pre-assigned ids

Every item in a suite has an id assigned before the attempt, and the manifest lists both the expected ids and the emitted ids. That single decision does three jobs:

- a run cannot be silently trimmed. A missing id is a named gap, G-MISSING, not a quieter pass rate,
- two runs of the same suite align by construction. The stability diff is a join on ids, with nothing to match heuristically,
- the report and the record cannot drift apart. The manifest's event count has to equal the file's line count, and verify checks it.

## Canonicalization is part of the format

Hashing is only as strong as the serialization it hashes. The canonical form is defined in the code: JSON keys sorted, whitespace fixed, and, because it cost a real bug, the line-separator characters U+2028 and U+2029 explicitly escaped. json.dumps does not escape them, and str.splitlines() splits on them, so an unescaped separator would let one logical record span two physical lines while every hash still checked out, until something line-oriented read the file. The invariant is enforced at the writer: one record, one line, always. The v1 demo bundles predate the fix and verify unchanged, which is the test that the canonical form is backward-compatible, not just convenient.

## Versioning without breaking the past

The format is versioned in the manifest (tieout-bundle/v1, then v1.1). v1.1 added the statistics block (per-family counts, pass rates, exact intervals) and the provenance packages plus their hash. The verifier branches on the declared version: v1 records verify against the v1 field set, v1.1 against the full set. The committed repository carries both: the v1 demo run and the v1.1 family and stability runs, all four passing the same verify procedure. A schema that cannot verify its own history is not a schema, it is a migration debt.
`;

export { body };
