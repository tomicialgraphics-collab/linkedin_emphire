# The Behar audit: what is in this folder

One folder per review exchange item, latest version first. Everything here is
either a document the reviewer has been sent, a patch he can apply, or a copy of
a file he pulls individually.

Start with `EXCHANGE-LOG.md`. It is the record of the review: what he found, what
reproduced, what was withdrawn, what each patch changed, what has been run on
which machine, and what is still open. The documents below are the artefacts that
record refers to.

## Documents sent to the reviewer

| file | version | content |
| --- | --- | --- |
| `AUDIT-RESPONSE-v1.2.html` | current | the response to the audit, including the T08 settlement table, the P0 and P1 summaries, the claims boundary and the F6 question |
| `AUDIT-RESPONSE-v1.2.md` | current | the same, as source. Markdown is not attachable to LinkedIn, which is why the HTML exists |
| `P1-PATCH-NOTES.html` | current | the four P1 fixes, the three probes, the two verifier defects found on Windows, and the Windows results |
| `P0-PATCH-NOTES.html` | current | the P0 fixes, the two runner portability bugs, and the eight counterexamples |
| `AUDIT-RESPONSE-v1.0.md`, `AUDIT-RESPONSE-v1.1.*`, `P0-PATCH-NOTES.md` | superseded | kept because the reviewer has copies and a claim that changed should be traceable |

## Code he can apply

| file | base | state |
| --- | --- | --- |
| `host-failure-benchmark-p11.patch` | `41013f0` | current. P1.1, the verifier input fixes |
| `host-failure-benchmark-p11.patch.txt` | same | same bytes, for LinkedIn, which does not accept `.patch` |
| `host-failure-benchmark-p1.patch` | `9194c61` | P1 |
| `host-failure-benchmark-p1-cumulative.patch` | `25cd57f` | P0 and P1 in one patch |
| `host-failure-benchmark-p0.patch` | `25cd57f` | P0 |
| `regressions.py` | current | standalone copy of `audit/regressions.py`, for a one-file refresh without applying a patch |
| `repro_audit.py` | current | the seven original reproduction modes, kept for the record |

Runnable snapshots, outside this folder, one level up in `PROJECTS/`:
`host-failure-benchmark-p0.zip`, `-p1.zip`, `-p11.zip`.

## State of the code the patches produce

`Teamthy/host-failure-benchmark`, `main` at `df0cf5a`, public.

```
python verify.py example\run      -> 20 of 20 checks hold (12 P, 2 V, 6 meta)
python challenge.py <run>         -> 10 of 10 mutations caught, 2 of 2 input checks held
python audit\regressions.py       -> 12 of 12 counterexamples caught
python verify.py does-not-exist   -> exit 2, no traceback, nothing verified
```

Windows 11 with Python 3.14.5 and Linux with 3.11.2 both produce the first, second
and third lines. The byte-identical two-run comparison exists on Linux only.

## Messages

`behar-reply.md` holds every message sent to him, the drafts for the ones pending,
and short answers for the questions most likely next. `behar-reply.md` is the
source of truth for what he has actually read.

## Open

- F6, store-minted identifiers: a design question, asked and not assumed.
- F15, an idle connection can hold the store.
- The verifier still imports the encoder it checks.
- No CI matrix.
- `audit/cases/`, his 38-case package, requested and not yet received.
- Author order and venue, deferred to finalisation by agreement.
