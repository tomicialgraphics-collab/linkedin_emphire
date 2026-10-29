const body = `
## A CLI is a contract

Most evaluation tools treat the command line as a convenience. For a tool whose output is evidence, the CLI is the interface a pipeline will depend on, which means its exit codes are a contract, and a contract has to be written down. This is the full contract for tieout, exactly as the parser defines it:

| command | 0 | 1 | 2 |
|---------|---|---|---|
| verify | PASS | FAIL | no bundle at the path |
| diff | diff computed | (unused) | error: missing or incompatible runs |
| selftest | all 8 points pass | any point failed | (unused) |

Two decisions in that table matter. First, verify distinguishes "the record is broken" (1) from "there is no record to check" (2). A pipeline that conflates them will either ship on a missing artifact or debug a phantom failure. Second, diff's exit code says the computation succeeded, not that the runs agree. The stability number is data, and a 0.99 stability is still a computed diff. Encoding opinion in an exit code is how scripts start making decisions the report never made.

## Machine-readable, human-readable, same run

Every command prints a human report by default, and the diff command takes a --json flag for the machine form. The two forms come from the same in-memory result, so they cannot disagree. There is no flag that changes what was measured, only how it is printed. A flag that changes meaning (a "strict mode" that quietly re-scores) is a fork in the data, and forks in the data are where audits die.

## One definition of pass, shared by site and pipeline

The CI workflow runs the same commands against the committed runs: verify every bundle, diff the stability pair, and gate on the stability line reading 1.000. The site's pages display the same bundles and the same numbers, read from the same files. When a reviewer asks "does your own CI pass on your own artifacts", the answer is not "we think so". It is a workflow that runs verify, diffs, and checks the line, on every push, against the same four committed runs. The command a stranger types and the job the pipeline runs are the same string. That is the whole design.
`;

export { body };
