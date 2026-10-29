# Changelog

All notable changes to this project are documented here. The format is
based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
