# Evidence: reproduction steps for two failure-path defects

Sent by Timothy Olusanya, 13 November 2026. Independent review, not a contribution to the project.

## What this document is

Two defects I found running the public repository, with the exact commands and the exact output. Each step is
copy-pasteable and each expected result is stated before the observed one, so you can tell disagreement from a typo.

## Environment

| Item | Value |
|---|---|
| Repository | `neomundi-io/neomundi-evidence-public` |
| Commit | `439d15499a57746904abd561e0f2edc35f925daf` (shallow clone, 13 November 2026) |
| Conformance corpus | 1.2.0 |
| Python | 3.11.2 |
| `cryptography` | absent in the first run, 50.0.2 in the second |

The commands below are written from the repository root.

## Baseline, before anything is called a defect

```
cd conformance && python3 runners/run.py --verifier python
```

Expected: the corpus passes against the reference implementation.

Observed with `cryptography` installed:

```
BILAN : AMBIGUOUS=10  PASS=40
```

Forty pass, ten are declared ambiguous, none fail. `sha256sum --check SHA256SUMS` also passes on all 172 files. That
is the state I am comparing against, so neither defect below is a general claim about the corpus.

## Defect one: an attestation that was never checked exits 0

```
python3 verify_attestation.py \
  conformance/fixtures/D-tampered/D-06-attestation-signature-invalid/attestation.jws; echo "exit=$?"
```

Observed:

```
[NOT TESTED] signature cryptographique - aucun magasin de confiance fourni : la cle nm-ev-demo-v1 n est pas resoluble.
[NOT TESTED] identite de confiance - sans magasin, aucune confiance n est etablie
BILAN : 5 PASS, 0 FAIL, 6 NOT TESTED
Niveau atteint : AUCUN au-dela de l integrite.
exit=0
```

Five PASS, six NOT TESTED, no level reached, and the process reports success. This is the D-06 tampered-attestation
fixture, so the file under examination is one that should not be presented as verified.

Adding `--strict` gives the intended answer:

```
python3 verify_attestation.py <same path> --strict; echo "exit=$?"
exit=2
```

with the three required guarantees named in the summary. So the correct behaviour exists and is one flag away. The
problem is the plain call, which is the shape a CI step takes. A pipeline that runs the verifier as documented cannot
distinguish this file from one whose signature was checked and confirmed.

## Defect two: the missing dependency is silent in the binary result

On an interpreter without `cryptography`:

```
python3 -m venv /tmp/nc
/tmp/nc/bin/python verify_attestation.py \
  conformance/fixtures/D-tampered/D-06-attestation-signature-invalid/attestation.jws; echo "exit=$?"
```

Observed: the same `exit=0`, the signature line NOT TESTED, no level reached. The prose is honest and the exit code is
not, so the two disagree and only one of them reaches an automated caller.

The corpus under that interpreter does report it:

```
/tmp/nc/bin/python conformance/runners/run.py --verifier python
BILAN : AMBIGUOUS=10  FAIL=5  PASS=35
```

Five failures, and three of them are attestation verdicts:

```
python  D-06-attestation-signature-invalid   FAIL   verdict attendu REJETE, observe ACCEPTE
python  D-07-attestation-payload-tampered    FAIL   verdict attendu REJETE, observe ACCEPTE
python  D-08-attestation-wrong-key           FAIL   verdict attendu REJETE, observe ACCEPTE
```

A tampered attestation is logged as accepted because a package was never installed. The runner catches it; the
verifier, called on its own, does not, and the runner is the thing a reader is less likely to have run.

## What I did not test

- The Rust verifiers. No toolchain here, and `--verifier all` refuses without both binaries. I make no claim about
  them.
- The four open normative questions in the specification. I read them and did not arbitrate any of them.
- The private dossiers referenced in the README. Not available, not requested.
- Anything about whether the attested executions took place. No signature establishes that.

## One correction to my first message

I wrote that six PASS sat above the NOT TESTED lines. It is five. The rest of that message stands, and the error is
mine rather than a difference in build.
