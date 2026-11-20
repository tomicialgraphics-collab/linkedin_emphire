# Two patches, and the measurements behind them

Sent by Timothy Olusanya, 13 November 2026. Companion to the reproduction steps and to the diff in the same folder.

Both patches were written against commit `439d15499a57746904abd561e0f2edc35f925daf`, applied, and run. Every number
below is from that run, not from reasoning about the code.

## What each patch changes, in one line

1. The exit code fails closed when a pillar of the verdict is not demonstrated, instead of only when the caller asks
   for `--strict`.
2. The verifier refuses to run when it cannot verify a signature, instead of printing NOT TESTED under an exit code
   that reads as success.

Neither patch changes a single verdict line. PASS, FAIL and NOT TESTED are produced by exactly the same code as
before. What changes is what an automated caller can conclude from the process.

## Patch one: the exit code follows the verdict

```python
def piliers_non_demontres(self):
    return [i for e, i, _ in self.lignes if i in PILIERS and e != PASS]

def code_de_sortie(self, strict=False, allow_untested=False):
    if self.compte(FAIL):
        return 1
    if self.piliers_non_demontres() and not allow_untested:
        return 2
    if strict and self.requises_non_demontrees():
        return 2
    return 0
```

`--allow-untested` restores today's 0 for callers that only read 0 and 1, so the change is reversible from the command
line rather than from a patch revert.

### Why pillars, and not every NOT TESTED line

The store-digest line is hardening. It makes the trust store harder to swap, and it does not decide whether the
verdict holds, because the verdict is already established by the five pillars. If that line blocked too, every normal
run without `--store-digest` would exit 2, and a check that is always red is a check people switch off. The five
pillars are the contingent ones: each can be PASS in the right conditions, so each one failing to reach PASS means the
verdict was not established.

### Measured, before and after

| Case | Before | After |
|---|---|---|
| D-06, no trust store | 0 | 2 |
| D-06, its own store and archive | 1 | 1 |
| D-06, `--strict` | 2 | 2 |
| D-06, `--allow-untested` | 0 | 0 |
| Corpus with `cryptography` | 40 PASS, 10 AMBIGUOUS, 0 FAIL | unchanged |

## Patch two: refuse rather than degrade

```python
if not CRYPTO and not arguments.allow_no_crypto:
    print("REFUS : `cryptography` est absent de cet environnement ...", file=sys.stderr)
    return 4
```

Exit 4, not 1 and not 2. A missing capability is not a finding about the evidence, and collapsing it into 1 would
report a tampered attestation where the truth is an unverified one. `--allow-no-crypto` asks for the partial report
explicitly.

| Case | Before | After |
|---|---|---|
| No `cryptography`, plain call | 0 | 4 |
| No `cryptography`, `--allow-no-crypto` | 0 | 2 |
| Corpus, no `cryptography` | 35 PASS, 10 AMBIGUOUS, 5 FAIL | 33 PASS, 8 AMBIGUOUS, 9 ERROR |

## One line needed outside the verifier

The conformance runner derives the verdict from the exit code:

```python
verdict = "REJETE" if sortie["code"] == 1 else "ACCEPTE"
```

Under that rule an exit 4 becomes ACCEPTE. It now maps 1 to REJETE, 0 to ACCEPTE, and anything else to NON VERIFIE.
That is a third reading of the same three codes, and it is the reason patch two is not just a `sys.exit`.

## The two assertions I have changed, and why that is the honest version of this

`tests/test_attestation.py` case 4 and case 15 both require `code == 0` when a pillar is NOT TESTED. So the current
behaviour is a decision the suite enforces, not an accident, and I would rather say so than file it as a bug. In the
patch, case 4 expects 2, and case 15 checks both the refusal (4) and the partial report under `--allow-no-crypto` (2).
The suite is 24/24 before and after.

If you read those two cases as the contract, the argument is worth having on its merits. My position is that "no FAIL"
and "verified" are different statements, and only one of them belongs in an exit code.

## How to apply

```
git checkout -b review/fail-closed
git apply 03-neomundi-fail-closed.diff
```

Three files, 95 insertions, 16 deletions.

## What the patch does not do

- It does not touch the Rust verifiers, which I never built.
- It does not arbitrate any of the four open normative questions.
- It does not make a refusal distinguishable from a crash in the runner's table. ERROR is the existing state for a
  technical condition that prevents a conclusion, and a refusal lands there. A fourth state would be better and I did
  not invent one for you.
- It does not change the JSON report schema, the four levels, or any wording of any control line. The only field whose
  value moves is `exit_code`, which is the point.
