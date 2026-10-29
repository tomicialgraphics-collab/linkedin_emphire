# Contributing

## Setup

```bash
make install     # or: pip install -e ".[dev]"
make test        # pytest
make selftest    # the 7-point harness selftest
make lint        # ruff
```

Frontend:

```bash
cd web
npm install
npm run build    # next build, static export to web/out
```

Run everything:

```bash
make ui && make serve
# then open http://localhost:8000
```

## The evidence doctrine (read before touching the harness)

1. **Nothing is silent.** A code path that cannot decide must emit an
   `undetermined` event plus a named gap. "Skip" is not a verdict.
2. **The check does not grade itself.** New checks must ship with
   crafted negative controls (known-hold and known-broken) written
   outside the check.
3. **Verdicts are re-derivable.** A detector must be a pure function of
   the stored raw. If your feature needs the network or a model to
   re-derive, it does not belong in `verify`.
4. **Ids are pre-assigned.** New items get their ids from the family
   declaration, before the run. The manifest's `expected_item_ids` is
   the contract that makes absence nameable.
5. **The policy version moves.** Any change to items, controls, or
   detector code changes the policy hash; that is intended, and old
   bundles remain bound to the old version.

## Adding a check family

1. Create `tieout/harness/f<n>_<name>/` with `prompts.py` (inputs),
   `detectors.py` (pure functions + a NAIVE variant), `family.py`
   (items, controls, `Family` instance).
2. Register it in `tieout/harness/__init__.py` (`FAMILIES`).
3. Add the test: a deterministic agent behavior expectation, the metric
   contract, controls clean, tamper caught.
4. Extend `tests/` and, if the family is deterministic, the selftest.
5. Update `docs/` (bundle format only if the record schema changed) and
   the README families section.

## Adding a page

Pages are hash routes in `web/app/page.tsx` (`#/runs`, `#/run/<id>`,
`#/method`, `#/format`, `#/matrix`, `#/harness`, `#/families`). New
pages: add a component in `web/components/`, a route in `page.tsx`,
and a nav entry if it belongs in the top bar. Keep the monochrome
system: black, white, gray levels, no color; verdicts read as
typography.

## Style

- Python: ruff (line length 100), no new runtime dependencies without a
  note in the PR/commit (the keyless core must stay keyless).
- TypeScript: strict mode; the build typechecks.
- Docs: the docs double as the site's content (rendered by
  `web/components/Markdown.tsx`); keep to the supported markdown subset
  (headings, paragraphs, lists, tables, fenced code, inline code, bold,
  links).
- Commits: imperative, one fact per line, state what changed and how it
  was verified.
