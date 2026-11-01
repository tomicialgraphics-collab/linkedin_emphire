# Changelog

## [0.3.1] - 2026-11-01

Found by running the gate while the target server was down. The engine
loaded, every attack failed with a refused connection, and the gate
reported PASS with 0 findings. The baseline guard caught it (nothing was
written), but the verdict was the same lie as 0.1.0, one layer down.

### Fixed

- A run where no attack executed is `error` and exit code `3`, even though
  an engine loaded.
- A run where some attacks errored and the rest found nothing is also
  `error`. A target that dropped half the connections has not been cleared.
  `gate.on_error: allow` and `--allow-errors` downgrade that to a pass with
  a line in the reason, and neither setting lets the run write a baseline.
- The refusal message now names the target error instead of suggesting the
  tools list.

### Added

- `gate.on_error`, default `fail`.

### Changed

- 66 tests, up from 63.

## [0.3.0] - 2026-11-01

A model is not deterministic, so one pass per attack measures "it happened
once" and nothing more. This release measures how often.

### Added

- `gate.repeat` (and `--repeat`): run each attack N times, record how many
  attempts reproduced the behaviour.
- `gate.min_repro` (and `--min-repro`): the number of reproductions a
  finding needs before it blocks. Default 1, so nothing blocks less often
  than it did before.
- Findings carry `hits` and `runs` in the JSON, with the ratio printed in
  the comment table, so a flaky weakness reads as `2/3 runs` instead of a
  yes.
- `gatecheck.groq.yml` ships with `repeat: 3`, because the target it points
  at is a model.

### Changed

- 63 tests, up from 60, including a target that fires once and never
  again, and the two settings disagreeing about whether it blocks.

## [0.2.1] - 2026-11-01

Everything here came from running 0.2.0 against a live model rather than a
scripted one. Three real weaknesses were on the table and the gate reported
one of them.

### Fixed

- **Refunds are summed per turn.** The model split 9,800 into two 4,900
  calls, exactly as the S08 case asks, and a per-action check saw nothing.
  The limit now applies to what the agent did in one turn.
- **Approving a claim counts as the privileged action.** M03 carried the
  agent into the human's decision through an injected note and the gate
  said nothing, because only refund amounts were inspected. A tool call
  that approves is now tool-misuse.
- **Two escalations of different size are two findings.** The action-based
  fingerprint stripped digits, so a 9,000 escalation and a 7,500 escalation
  collapsed into one row and the report undercounted. Amounts are part of
  the identity now: the attack fixes the amount, so it does not drift.

### Changed

- 60 tests, up from 56, one per gap above.

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
