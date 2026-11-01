# Changelog

## [0.1.1] - 2026-11-01

Fixed the worst bug in 0.1.0, found by running the package on a machine
with no red-team engines installed: the gate ran nothing, reported PASS,
saved an empty baseline over the real one, and then reported the seven
findings the agent still had as fixed. Nothing below is cosmetic.

### Added

- `gatecheck core` engine. It runs the full corpus, single-turn and
  sequenced, with no third-party dependency, and it is in the default
  `tools:` list. A fresh `pip install -e .` now produces a real result on
  the first command instead of an empty one.
- `--force-baseline`, for the case where you have read the warning and
  still mean to record a partial run.

### Changed

- A run that reaches no engine now has status `error`, not `pass`, and
  exits `3`. Exit codes are `0` pass, `2` blocked, `3` error.
- `--update-baseline` is refused unless every configured tool actually ran
  and at least one attack was executed. A blocked run is still allowed to
  record its findings: adopting the gate on a codebase that already fails
  is the normal first day, and the output says so.
- `gatecheck.yml` defaults to `tools: [gatecheck]`, with deepteam, pyrit
  and promptfoo listed as commented opt-ins. Listing an engine you have
  not installed is not free.
- Tests for optional engines skip when the engine is absent instead of
  failing the suite.

### Fixed

- 43 tests, up from 36: the no-engine run, the partial-run baseline
  refusal, and a complete blocked run recording known findings.

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
