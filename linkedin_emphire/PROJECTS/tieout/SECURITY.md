# Security

## Scope

tieout is an evaluation harness. Its security properties concern the
**integrity of the record**, not the protection of the target:

- the bundle is the artifact: hash chain, manifest, file hash
- `verify` is the integrity check: no model, no key, no network
- the detectors are heuristic judges; the P6 judge audit measures them
  every run and reports the numbers, including the flips

## Verify, don't trust

Anyone reviewing this repository should verify its claims from a cold
clone:

```bash
pip install -e ".[dev]"
python -m tieout selftest
python -m tieout demo
python -m tieout verify runs/demo
pytest
```

All four must pass. The committed demo run at `runs/demo` is a real
artifact: its `verify` output is in `runs/demo/verify_report.json`.

## Reporting issues

Open an issue on the repository. If a report involves a live endpoint
or an active engagement, keep the details out of the public issue and
open a security advisory (GitHub: Security -> Advisories -> New draft)
or share via direct message first; the issue can link the advisory once
it is public.

## Safe use

- Live runs send the prompts in `tieout/harness/f1_five_checks/prompts.py`
  and the system prompt you supply to the endpoint you configure.
  Treat any live endpoint as receiving that content; do not point the
  harness at an endpoint with credentials you would not accept being
  quoted back to you.
- The `MY_SYSTEM_PROMPT_FILE` / `--system-prompt-file` contract sends the
  file's full content as the system prompt. Use a file you are willing
  to have transmitted verbatim.
- Result bundles contain raw inputs and outputs. Share bundles
  deliberately: the raw is the point, but it is also the privacy
  surface.

## Heuristic disclaimer

Detectors flag likely failures; they do not prove them. A `fail` in a
bundle is a detector firing on a stored raw, re-derivable by a stranger.
Confirmation is a human act, in the raw, by design.
