# Changelog

## 1.0.1, 9 November 2026

Presentation release. No change to the checklist or the tooling behaviour.

- Banner and social preview card, drawn as SVG by `assets/make-banner.py` and rendered to PNG. The grid is the coverage argument as an image: a minority of squares lit, because most classes are open at the start.
- README rebuilt around the same structure as the checklist: banner, badges, table of contents with working anchors, one section per category, and the measurement argument in full.
- `assets/social-preview.png` is the file to upload as the repository social preview, which is what a LinkedIn card shows.

## 1.0.0, 9 November 2026

First release.

- 168 items across six categories: model behaviour, retrieval and knowledge, agents and tooling, output handling, measurement and evaluation, governance and practice.
- Three tiers: core 51, standard 93, extended 24.
- `checklist/checklist.json` as the single source of truth, with generated `CHECKLIST.md` and `checklist.csv`.
- `tools/validate.py`, `tools/render.py`, `tools/coverage.py`, `tools/wilson.py`, standard library only.
- Seven documents: the method, the model surface, retrieval and agents, output handling, measurement, governance, reporting, references.
- Four templates: engagement scope, finding, report, coverage argument.
- One redacted example status file.
- CI: validate, check the rendered files match, run the coverage example.
