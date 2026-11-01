# Changelog

## [0.2.0] - 2026-11-01

First support for a target that is a language model rather than a rule
engine. Nothing about the gate's own contract changed: it still fails only
on new or worsened findings against a stored baseline.

### Added

- `groq_target/`: a claims agent with a real model behind the same contract
  the gate already speaks, two prompt modes (`vulnerable`, `guarded`), three
  sandboxed tools, session memory for multi-turn sequences, and a server
  (`python -m groq_target.serve`). Groq is reached over plain urllib, so
  there is still no new dependency.
- `gatecheck.groq.yml`, with its own baseline, because a rule engine and a
  model are different targets and diffing one against the other's record
  would report every difference as a regression.
- Detection from actions: an outbound email to a domain outside
  `INTERNAL_DOMAINS` is data exfiltration, whether or not the model
  mentioned it in prose.
- The fingerprint prefers a canary, then the tool call, then free text. A
  model rewrites its wording every run, and an identity that followed the
  wording would mint new findings forever.
- `--fake` on the target server: a scripted model, so the whole path can be
  tested with no key and no network.

### Changed

- The injection attacks name the token they want echoed
  (`OVERRIDE-CANARY-2B91`, `INJECT-CANARY-9C4D`), so compliance is a string
  match rather than a judgement about tone. The demo agent's behaviour and
  findings are unchanged; only the evidence text differs.
- 56 tests, up from 43.

### Known limits

- Each attack runs once. A model that misbehaves one time in ten will
  produce a finding on some runs and not others, and there is no hit-rate
  column yet.

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
