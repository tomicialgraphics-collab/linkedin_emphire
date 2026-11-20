# Report template

Client: ____________________  System: ____________________  Dates: __________

Prepared by: ____________________  Revision of this report: 1.0

## 1 What was tested

| | |
|---|---|
| System and version | |
| Environment | |
| Model revision | |
| Prompt version | |
| Index snapshot | |
| Tool schema version | |
| Sampling settings | |
| Test window | |
| Rules of engagement reference | |

## 2 What was not tested

Paste the coverage summary from `tools/coverage.py`, including the `open` count. Two sentences on the focus and the agreed exclusions.

## 3 Summary of findings

| Id | Title | Severity | Reachable by | Rate |
|---|---|---|---|---|
| F-01 | | | unauthenticated / user / insider | |

## 4 Findings

One page each, in the order of `templates/finding.md`.

## 5 Root causes

Grouped. Twelve findings under one broken trust boundary is one cause and eleven instances, and saying so is the most useful sentence in the report.

## 6 What to fix first

Three changes, ordered by risk removed per unit of work, each with the finding ids it closes.

| Change | Closes | Effort | Residual risk |
|---|---|---|---|
| | | | |

## 7 Handover

- Suite location and repository:
- How to run it:
- Cost per run:
- Wall clock time per run:
- Cases added from this report:
- Who runs it, who reads the failure:

## 8 Assumptions and limits

What this report does not establish. A test is evidence about the cases that were run, on the revision that was deployed, on the dates above.
