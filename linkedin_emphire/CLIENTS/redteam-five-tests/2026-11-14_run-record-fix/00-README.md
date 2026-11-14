---
deliverable: run-record-correction
id: 2026-11-14_record-fixes
date: 2026-11-14
audience: reviewer
status: ready
approved: no
fix_verified: true
---

# Two corrections to the 3 November run record

Two findings came back from the independent review of the pinned harness and the second run. Both were accepted in writing. This pack is what was promised: a corrected manifest a reader can check without asking anything, and the change to the builder that puts the record before the package.

Everything below was measured on a clean clone of the same commit, not recalled.

## Finding 1: one file, two digests, and the note that blamed the wrong cause

The claim was that `console.log` hashes to `9828c763` when read from the hosting layer and to `4889096b` in the manifest, and that no explanation was given.

Measured on the stored object at blob `e238092d`:

| what | value |
| --- | --- |
| stored bytes | 5,274 |
| encoding | UTF-16LE with a byte order mark |
| first bytes | `ff fe` |
| digest of the stored object | `4889096bc551a89116ee8e830ab6e9f896b39e4e1d8f6149800acdf1983bd81b` |
| digest of the same content served as UTF-8 with a BOM | `9828c763bf9822a40ba2186a9d027ff87c9e97bd4a7c5c610d7f5fe2844a8c1a` |
| served bytes | 2,639 |

Both numbers are true. The content is identical; the encoding is not. A host that displays a UTF-16 object decodes it to UTF-8 with a BOM first, so the response hashes differently from the object it came from. Nothing about line endings was involved, which is what the old footnote claimed, and the footnote was wrong for exactly this file.

Only three of the seven files in that directory were listed at all. `README.md`, `check_results.py`, `provenance.txt` and `provenance-after.txt` were shipped without identifiers of any kind, so nothing could be checked about them.

`01-SHA256SUMS.corrected.txt` replaces it, a drop-in swap for the manifest in the run record. Every file in the directory gets a digest of its stored bytes, its byte count, its encoding including line endings, and its blob id. The one file that a host re-encodes gets its served digest and served size printed underneath, so a reader who hashes the web page finds their number in the manifest and sees why it differs. A separate record covers the harness, with its blob id at the run commit and the digest a Windows checkout produces. A checksum row for it would send `sha256sum` looking in a directory it is not in.

## Finding 2: the record was archived after the package was written

Confirmed in the published builder at `80fa2cf`: the package is written at line 459, and `archive_run` is called at line 461 with its return value discarded. So a build that fails while archiving still leaves a published package, and a build that fails before archiving leaves one too. That is the mechanism that lost the 1 November results, and it was still in place two lines below the comment saying the record travels with the package.

`02-record-before-publish.patch` carries the change:

1. `archive_run` is called first and its result is held.
2. If archiving cannot complete, the call raises and the package is never written. Four conditions refuse: no results file, results that do not parse, results without a meta block, and a manifest that did not reach the disk.
3. The manifest it writes carries the same per-file identifiers as the corrected manifest: bytes, encoding, blob id, and the served digest where a re-encoding is possible.
4. `sha256sum -c` now runs clean in the record directory, because the harness is no longer a row and every annotation is a comment.

Ordering after the change: archive at line 530, write at line 531.

## How to check it, without asking me anything

```
python3 03-verify_run_record.py --repo /path/to/your/checkout
```

Fifty checks, no network, standard library only:

* every manifest row resolved by blob id and hashed from the object, not from a copy on disk
* byte count and encoding compared, including line endings
* the served digest re-derived and compared with the one in the manifest
* the working tree compared with the object, so a checkout that converts anything is named
* the harness digest checked at the run commit and through CRLF
* the builder parsed to confirm the archive call comes first and its result is held
* the real `archive_run` run against a throwaway harness with no results, to confirm it refuses and leaves the package untouched

`04-verify-before-and-after.log` holds the output on the published code and on the patched code, side by side, plus the control run where a digest in the manifest was altered on purpose and the script reported that row.

## What this does not claim

Nothing here is merged into the repository's default branch. It applies cleanly to `80fa2cf` and the checks above were run against a checkout with it applied.

Future builds are what the change governs. It does not restore the 1 November results, and it cannot. The run record for 2 November still lacks the raw JSON, and that stays a retention gap on the record rather than something a patch repairs.

Nothing about the design of the run is touched here. A correct manifest and an ordered archive change what a reader can verify, not what the five tests measure.

## Files

| file | what it is |
| --- | --- |
| `01-SHA256SUMS.corrected.txt` | replacement manifest for the run record, every file, blob id and encoding |
| `02-record-before-publish.patch` | the builder change, applies to `80fa2cf` |
| `03-verify_run_record.py` | one command, fifty checks, offline |
| `04-verify-before-and-after.log` | output before and after, with a control run |
| `05-SHA256SUMS.txt` | digests of the four files above |
