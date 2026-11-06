# Reply to Behar, 6 November 2026

LinkedIn message. Attach `REMEDIATION-SCOPE-2026-11-06.md` (or the HTML).

---

Behar,

Thank you for reading it that closely, and for agreeing the structure. All five refinements are in the scope, and each one changed something concrete rather than being noted.

S1 now distinguishes four states rather than two: persisted, nothing written, partial, and indeterminate. The partial state is the one your S1 describes, and it carries the sequence numbers of the records that are on disk, because a caller cannot act on `durable: false` alone. The mode checks the journal immediately after the failed append and again after a restart, as two separate assertions, since those can disagree. The reply may only say nothing was written when the rollback has been truncated, re-read, and fsynced.

S2 writes the repair record on the runtime cut path with the fields the start-up path already writes, plus the byte range and a source field. If writing that record fails, the request reports `repair_record: "not_written"` and state keeps saying so. Failure to record the repair is now an observable condition rather than a silent success, which is the part your note made sharper than my first draft.

S3 is four modes rather than one, one per behaviour: classification, bounded execution with timeout reporting, progress before completion, and a preflight for missing optional utilities including `bc`. They are ports of the scenarios in the verification folder, so you can run them from the repository. Your constraint is the acceptance test: a fifth mode compares the full table of mode to caught or MISSED and every mode's failed-check set before and after, and fails on any difference beyond the four intended ones.

S4 has no code proposed, only a precondition. I have defined equivalence by the failure condition rather than by the flag: both environments count as equivalent only if the verifier is asked to write or replace the report, cannot, and is then asked to present it as current. If the read-only mount refuses at a different point, it is recorded as a narrower condition and the row stays open.

S5 fixes the actual leak. The custom modes lose their work directory because `fresh_copy` returns the tree and drops the parent, which is the two copies in the row. Retention becomes opt-in and every retained path is printed.

On closure discipline: each row will carry the baseline failure, the post-fix pass, the revision and the execution log, and a classification log showing the other rows did not move. A milestone finishing is not a row closing, and S4 is not closed on any schedule but its own.

Four decisions I would rather have from you than make for you, all in section 9: the partial-state shape, the exit code for an unclassifiable run, whether you can supply a host where `chattr +i` succeeds, and whether retention should be a runner flag or an environment variable.

The register itself is untouched, still at SHA-256 `4413420b...5c03`. The scope is a separate file: 2,088 words, SHA-256 `0d40270a36e717a9dd7275a47fb756ffccf3741ab07d0ffecda5a5347d32da1c`. The HTML rendering is the same document with its own hash if you prefer to read it formatted.

Olusanya
