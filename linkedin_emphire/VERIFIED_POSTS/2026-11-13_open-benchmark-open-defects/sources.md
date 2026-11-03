# Figures used, and where each one comes from

All figures are from my own benchmark run, recorded in `host-failure-benchmark/audit/FINDINGS-REGISTER.md` and `DISPOSITION-2026-11-01.md`. Nothing here is quoted from another source.

| Claim in the post | Value | Source |
| --- | --- | --- |
| Failure modes tested | 19 | register, mode list |
| Class P suite | 13 of 13 | register, run of 2026-11-01 |
| Class V suite | 3 of 3 | register, run of 2026-11-01 |
| Documentation conformance | 22 of 36 | AS-DOC run |
| Negative cases | 12 of 13 | N-case run |
| Open defects | 8 (V23, V24, V28, V29, V30, V31, V32, V33) | register, open list |

## Rules applied

- The post does not claim the suite is an industry standard. It says the opposite in the body.
- No result is described as reviewed or endorsed by anyone else. The independent review is private and stays out of the post.
- Link points at the public repository only, not at any other project.
- "Nineteen ways for the layer below you to lie" is a description of the fixture, not a claim of exhaustiveness.

## Stale-risk

The counts move as defects close. If this is posted after any of V23, V24 or V28-V33 is fixed, re-run the suites and update the two numbers before publishing, or the post will be the first thing in the register that is wrong.
