# Register pin, 4 November 2026

The reviewer asked for the updated findings register to sit at an identifiable revision so the review of the S1 to S5 rows refers to fixed bytes rather than a moving file. This note is that pin.

## The revision

| Item | Value |
|---|---|
| Commit | `fbef78e752f3c6edf3a3e8dffcc1f94ae0dc0e3a` (`fbef78e`) |
| Tag | `p2-register-2026-11-04` |
| Register SHA-256 | `4413420b45d9312630b1b0e394cb8a09481a5be665135ded1ec4c693156c5c03` |
| Register size | 162 lines |
| Copies | Three, byte-identical: `host-failure-benchmark/audit/`, `PROJECTS/2026-10-30_behar-host-failure-benchmark/`, `PUBLISH/hfb-p2-reconciliation-2026-11-03/audit/` |

Every one of those three paths hashes to the value above, checked with `sha256sum` at the time of writing. Anyone reviewing the register can confirm they hold the same bytes without trusting this note.

## What changed at this revision

Five rows added, S1 to S5, each carrying the review case, the reproduction command, the log path, a status, a corrective action and a closure criterion. Nothing else in the register changed, no other row was reworded, and no status was moved toward fixed. S1, S2, S3 and S5 are `open` with a reproduction date; S4 is `open` and environment-limited.

## Integrity position, agreed 4 November

The reviewer independently compared all 42 file hashes against the original verification archive and reports that they match. That settles the content question from both sides:

- **Content: verified, both sides, by manifest.** Forty-two files, two independent comparisons, same result.
- **Container: documented, not verified.** The ZIP digest `e34c35c8…3f98` stays recorded as an unverified container hash. The reviewer has elected not to publish the original archive as a release asset at this stage, so the digest cannot be checked and is not claimed.

This supersedes the earlier wording in `p2-verification-2026-11-03/RESULTS.md`, which described the manifest route as one of two available mechanisms. It is now the mechanism in use, and the release-asset route is explicitly not taken. `RESULTS.md` is left unchanged because it is part of the delivered package and pinned by its own manifest; the correction belongs here.

## P2 closure method, agreed 4 November

A corrective action is validated by an executable regression test that fails against the affected baseline and passes after remediation, while the existing benchmark guarantees are preserved. Each acceptance criterion in the register becomes that test. Closing a row is therefore a test result rather than a judgement call, and P2 closes against the set of them.

## Not yet done

- No remediation is started. The next artefact is the remediation scope, drafted for the reviewer's comments.
- No row moves to `patched` or `closed` without the mode that fails without the fix.
- S4 still needs a filesystem that permits the immutable flag, or another way of establishing that condition recorded with the run.
