# Changelog

## [0.1.0] - 2026-11-01

### Added

- Findings with stable fingerprints, so a run can be compared to the last
  accepted state of the same target instead of to nothing.
- Baseline store with `new`, `worse`, `unchanged` and `fixed` deltas, and
  `accept --reason` for risk a team has decided to carry.
- `gatecheck.yml` policy: severity per category, the severities that block,
  and the baseline path. Unknown categories are rejected rather than ignored.
- Three engines: DeepTeam for attack variants, PyRIT for multi-turn
  sequences, promptfoo for HTTP assertion runs. Each is optional and
  reports itself skipped with a reason.
- Outputs: a pull request comment that leads with the delta, SARIF 2.1.0
  for code scanning, and a JSON run record the next run diffs against.
- Exit codes `0` pass and `2` blocked.
- A deliberately broken demo agent and its hardened twin, so the
  before/after claim can be checked in one command.
- 36 tests covering identity, dedupe, policy, baseline deltas, the
  engines, and the three report formats.
