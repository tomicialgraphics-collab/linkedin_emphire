# Changelog

All notable changes to this project are documented here. The format is
based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-11-01

### Added

- **The tool layer: PyRIT, promptfoo and DeepTeam behind one record.**
  `tieout adapters run` plans an eight-attack catalog with pre-assigned
  ids, executes it through whichever of the three tools are installed,
  and grades every record with one deterministic judge. 48 records per
  full run, offline, keyless, about ten seconds.
  - PyRIT (Apache 2.0, 1.1.0) runs through its own `PromptTarget` and
    `PromptSendingAttack`, with base64 rendering on a second variant.
  - promptfoo (MIT, 0.125.1) runs a generated YAML suite with a Python
    provider and per-weakness assertion files. Its non-zero exit code on
    failing tests is treated as a result, not an error.
  - DeepTeam (Apache 2.0, 1.0.10) contributes its deterministic attack
    transforms; the generative half is offline-disabled and recorded as
    the named gap `G-DEEPTEAM-SIMULATOR`.
- **Tool verdicts recorded beside the harness verdict**, never instead of
  it: 40 of 48 tool verdicts are `undetermined` in the sample run, which
  is the argument for an external judge stated as a number.
- **`tieout adapters matrix`**: cross-tool coverage, consensus and unique
  catches, per weakness.
- **`tieout adapters verify`**: re-derives a whole adapter bundle with
  none of the three tools installed, re-scores every raw output,
  re-hashes the sidecar and recounts the tools' own verdicts. A test
  asserts the module imports no tool.
- **`limitation` records** (`L-JUDGE-SCOPE`): a verdict that re-derives
  correctly and is still the wrong answer, such as a 9,800 refund split
  into two 4,900s that a per-action judge cannot see. Kept out of the
  gap list, because the record is sound and the judge has a scope.
- **Committed sample run** at `runs/demo-adapters`, verifiable by
  `tieout verify runs/demo-adapters` and `tieout adapters verify`.
- **24 tests** for the adapter layer: catalog stability, detector
  behaviour, sandbox determinism, encoding weakness, pre-assigned ids,
  chain integrity, tool-free re-derivation, tamper detection, the
  missing-tool gap, the dropped-item gap, and the consensus matrix.

### Changed

- The server's run detail now returns `tool_audit` and `limitations`
  when a bundle carries them.

## [Unreleased]

### Added

- **Writing: `/blog` and twelve articles.** A new route group,
  `/blog` plus twelve `/blog/<slug>` pages, statically generated from
  `web/lib/articles/`. The articles cover the five disciplines this
  project sits in: ai red teaming (the prompt is not a wall, surface
  drift, the failure-mode matrix), security (verification, negative
  controls), research engineering (auditing the judge, exact
  confidence intervals), evaluation (provenance as part of the claim,
  the bundle record schema) and software engineering (exit codes as a
  contract, stateless deployment). Every number in them traces to a
  committed artifact in this repository, and each article ends with
  its verified-against list.
- **LinkedIn.** The author's profile
  ([linkedin.com/in/olusanya-timothy](https://www.linkedin.com/in/olusanya-timothy))
  linked at the strategic points: the landing hero, the site footer,
  the top navigation, and every article byline.
- **Vercel deploy adapter** (the repository deploys as-is, one
  project): root ASGI entry (`main.py`), `vercel.json` in the
  Services model (`web` = the Next static export, `api` = the FastAPI
  app, `/api/*` rewritten to the function with the path preserved),
  `.python-version` (3.12) and `uv.lock` for Vercel's
  `uv sync --locked`.
- **Multi-page static site**: the hash router is gone. Thirty-four
  real, prerendered, deep-linkable routes: `/`, `/runs`, one page per
  committed run (`/runs/demo`, `/runs/demo-f2`,
  `/runs/demo-stability/a`, `/runs/demo-stability/b`), `/blog` + the
  twelve `/blog/<slug>` pages, `/compare` (with `?a=`/`?b=` deep links
  from a run page), `/method`, `/format`, `/matrix`, `/harness`,
  `/families` + `/families/f1` + `/families/f2`, `/asi`, `/repro`,
  `/cli`, `/changelog`, `/security`, `/contribute`, `/license`.
- The `/api/docs` endpoint now also serves the repository's own
  records: `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE`.
- `create_app` takes an explicit deployment root: on Vercel the app
  is imported from an installed wheel, so `runs/`, `docs/` and the
  root records are resolved against the deployed tree, not the
  installed package's `__file__`.
- The verify endpoint's `verify_report.json` write is best-effort:
  on ephemeral / read-only serverless filesystems the report is still
  returned complete in the HTTP response.
- Tests: the deployed entry serves health, runs, docs and families
  from the repo tree; nested run ids are routable on detail, verify
  and diff; the report persists when writable; verify stays correct
  on a simulated read-only filesystem; an explicit deployment root
  serves its own content (the wheel-installed layout).

### Fixed

- Static serving of the Next.js export: Starlette's `StaticFiles`
  resolves exact files and directory indexes only, so extensionless
  export routes (`/runs`, `/runs/demo`, `/blog/<slug>`) 404'd when a
  route file shared its name with a directory of detail pages. The
  mount now uses `StaticExport`, which applies the resolution order
  static hosts use (exact file, then `<path>.html`, then
  `<path>/index.html`, then the 404 page), covered by
  `test_static_export_serves_extensionless_routes`.
- `/api/runs` now lists nested runs (`runs/demo-stability/a`), which
  the top-level scan silently hid from the run list and the compare
  page dropdowns.
- Nested run ids 404'd on the detail and verify routes: Starlette's
  default path parameter stops at a slash. Both routes now use the
  `path` converter, so `demo-stability/a` is addressable exactly like
  `demo` (the UI already sent percent-encoded ids).

### Removed

- `requirements.txt`: `pyproject.toml` + `uv.lock` are the single
  source of truth for the function's dependencies.

## [0.3.0] - 2026-10-29

### Added

- **Stability diff** (`tieout diff RUN_A RUN_B`, `/api/diff`, the
  `#/compare` page): aligns two bundles by pre-assigned id and reports
  verdict drift versus transcript drift separately, with each run's
  pass rate and exact CI. Committed stability pair at
  `runs/demo-stability/{a,b}` (seeds 0 and 7) with the diff report
  committed as evidence: 14/14 verdicts stable, 10 transcripts drifted.
- **Exact confidence intervals** (`tieout/stats.py`): Clopper-Pearson
  95% intervals by bisection on the binomial CDF (math.comb only, no
  scipy, no normal approximation). Stored in the manifest before the
  bundle is closed; undetermined counts against the pass rate by
  doctrine.
- **Family F2, state and recovery**: the failure-mode matrix rows made
  executable. Checks E (evidence at decision time), P (persistence),
  R (recovery), V (independent verification); 8 items (designed break +
  documented hold per check on the sample fixture), 8 negative
  controls, its own judge audit with crafted extra anchors and a
  one-tell NAIVE variant. Committed evidence at `runs/demo-f2`
  (4 fail / 4 pass, 0 FP / 0 FN, verify PASS).
- **Environment-locked provenance**: pinned package versions and their
  hash in the manifest (v1.1 field).
- **Sample agent surface-drift seed** (`--seed`): deterministic
  cosmetic variation of the transcripts with the verdicts fixed, so a
  keyless run can demonstrate stability.
- Selftest point 8: two sample runs (seeds 0 and 7) must show zero
  verdict flips and visible transcript drift. The selftest is now
  8-point.
- Test suite: stats properties (including the documented 0/10
  reference interval), diff (alignment, flip detection, dropped items,
  family mismatch, missing bundle), F2 contract, v1.1 backward
  compatibility against the committed 0.2.0 bundle, hostile-input
  chain hardening. 40 tests.
- Docs: format v1.1 addendum (additive fields, backward compatibility
  rule, the one-record-one-line canonicalization invariant), method
  note (stability + statistical rigor), harness spec (families,
  stability diff), matrix (F2 operationalization), README
  (architecture invariants, proving stability, page table).
- CI: the committed demo-f2 and stability-pair runs verify, and the
  stability diff asserts zero verdict flips, on every push.

### Changed

- Bundle format v1.1 (additive; v1.0 bundles still verify, enforced by
  a test on every commit).
- `canonical()` escapes U+2028/U+2029: the one-record-one-line
  invariant now holds in the file bytes for every possible raw.
- Judge audit inputs (extra anchors, NAIVE variant) are declared by the
  family, not imported from a F1-specific module.
- Web: compare page + nav; run detail shows the exact CI, the
  environment packages, and the bundle format; landing capabilities
  section; families page renders F2 and its ASI mapping.

## [0.2.0] - 2026-10-29

### Added

- Full evidence model in code: P1 verdict events on a hash chain with
  pre-assigned ids and effect references; P2 provenance; P3 negative
  controls with per-run FP/FN; P4 named gaps (G-MISSING, G-HASH,
  G-VERDICT-MISMATCH, G-CONTROL, G-RECORD, G-TARGET, G-PROVENANCE);
  P5 stranger-safe re-derivation (`verify`); P6 judge audit (anchor
  agreement, perturbation flips, disagreement rate, self-preference
  probe).
- Family F1: the five failure checks ported unchanged from
  ai-redteam-five-tests (d95a57e); deterministic SampleOrderBot;
  LiveAdapter for any OpenAI-compatible endpoint.
- CLI: `run`, `demo`, `verify`, `gaps`, `judge-audit`, `selftest`,
  `serve`.
- Bundle format v1 with a written spec (`docs/bundle-format-v1.md`).
- Web UI: Next.js (static export, black and white) with landing, runs,
  run detail, method, format, matrix, harness, and families pages,
  plus in-page stranger verify.
- Docs: README (gap-first, cited research), harness spec, method note,
  failure-mode matrix, SECURITY.md, CONTRIBUTING.md, CHANGELOG.md.
- CI: backend (ruff, pytest, selftest) + frontend (npm ci, build).
- Makefile for the common commands.
- Committed reproducible demo run at `runs/demo`.

### Changed

- Frontend rebuilt on Next.js (previous static build superseded).
- Positioning consolidated around the evidence layer; repository is the
  public artifact of the practice.

## [0.1.0]

### Added

- M1: the five F1 checks emitting P1 verdict events with P2 provenance
  stubs; the 7-point selftest; the deterministic sample agent.
  (Rebuild of record; see the project spec in the private record.)
