---
deliverable: dm
id: 2026-11-14_andrey-record-fixes
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:19 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: andrey-ekhmenin
status: ready
approved: no
fix_verified: true
premise_checked: >-
  checked: every number in this message was recomputed on 14 November from a fresh clone of the
  pinned commit, at the object layer, not read from the earlier message. The console log object
  is UTF-16LE with a BOM, 5,274 bytes, digest 4889096b; the served rendering is UTF-8 with a BOM,
  2,639 bytes, digest 9828c763. The builder ordering is 459 write and 461 archive at 80fa2cf, and
  530 archive and 531 write after the patch. The verifier reports 48 passed 2 failed on the
  published code and 50 passed 0 failed on the patched code.
sources_read: >-
  none: nothing is linked. The repository, its run record and the builder were read directly from
  the clone at 80fa2cf, and every digest was recomputed rather than taken from a page.
profile_checked: >-
  Andrey Ekhmenin, independent reviewer of the pinned five-test harness. He verified the
  redteam.py and results.json digests himself before writing, so he reads numbers rather than
  taking them. He raised two findings, both accepted in writing on 4 November, and the last
  message to him promised the corrected manifest and the code change. He has not been asked to
  run anything for free, and nothing here asks him to. What the message does is give him the mechanism he
  could not see, the two artifacts, and one command that checks both without needing a reply.
---

# Andrey Ekhmenin, 14 November 2026

Two findings, both accepted on 4 November, both closed here with the numbers measured on a clean clone at `80fa2cf`.

## What was actually true, measured rather than recalled

`console.log` is stored as UTF-16LE with a byte order mark. 5,274 bytes, first bytes `ff fe`, and the blob in the run record is `e238092d`. Its own digest is `4889096b`, which is what the manifest said. A host displaying it decodes to UTF-8 with a BOM first: 2,639 bytes, digest `9828c763`, which is what Andrey got. One content, two encodings, two correct numbers.

One footnote blamed line endings. That held for `redteam.py`, which is where the Windows checkout problem came from, and it never held for `console.log`. Naming the wrong mechanism is worse than naming none, because it invites a fix that does nothing: setting `core.autocrlf=false` cannot change a stored encoding.

Only three of the seven files were covered at all. `README.md`, `check_results.py`, `provenance.txt` and `provenance-after.txt` went out with no identifier at all. A replacement gives every file a digest of its stored bytes, a byte count, an encoding, and a blob id, plus the served digest for the one file a host re-encodes. `sha256sum -c` runs clean in that directory.

## The builder, as it is and as it now reads

Under the published code at `80fa2cf`, the package is written at line 459 and the archive is called at 461 with its return value thrown away. A build that fails to archive still publishes, which is the part that cost you a second look. That is what lost the 1 November JSON, and it survived two days beside the comment saying the record travels with the package.

After the patch: archive first, result held, four refusal conditions inside `archive_run` (no results, unparseable results, no meta block, manifest that did not reach the disk). Ordering is archive 530, write 531. Any refusal means the package is not written at all.

## Verification, and what it does not cover

`03-verify_run_record.py` runs 50 checks with no network: every manifest row hashed from the object rather than a copy, encodings compared, the served digest re-derived, the harness checked at the run commit and through CRLF, the builder parsed for ordering, and the real `archive_run` run against a harness with no results to confirm it refuses and leaves the package untouched. On the published code it reports two failures. On the patched code, none. A copy of the manifest with one digest zeroed produces exactly one failure, so the script can fail.

Not claimed: the patch is not merged upstream. It does not restore the 1 November results, and a retention gap stays on the record rather than being repaired by a patch. Nothing about the five tests themselves changed.

## Delivery

Everything sits in one folder at https://drive.google.com/drive/folders/1W7a8z98zYLtVgMHKnhOdNad0nQmRn9hH, open to anyone with the link and not listed in search.

Five files are in it. Corrected manifest `dfa8a6bda65d15ae747036f222102f8a6524580aa5bc3028637934e2959174d0`, the patch is `7c504ea63c3e5fd5c95c9e9033e76ec4ec183ec2553ab37593e3080c985cc86e`, and the verifier is `8d6f77209c9ca8651b79dce22233df60fc7d9ff50f1ea6c282c49eaf46cbf074`.

## DM to paste

Andrey,

Both findings are done, and one was worse than a wrong number.

The console log is stored as UTF-16LE with a byte order mark. 5,274 bytes, first bytes ff fe, blob e238092d. Its own digest is 4889096b, which is what the manifest said. A host displaying it decodes to UTF-8 with a BOM first, so you got 2,639 bytes and 9828c763. One content, two encodings, both numbers correct. The footnote blamed line endings, which was true of the harness file and never true of this one. Naming the wrong cause is worse than naming none, because no checkout setting fixes an encoding.

Every file in that directory now carries a digest of its stored bytes, a byte count, an encoding and a blob id. The one a host re-encodes also carries its served digest. The old manifest covered three files out of seven, which I hadn't noticed. sha256sum -c runs clean there now.

On the builder, you read it right. Write at 459, archive at 461, return value discarded. My patch archives first, holds the result, and refuses on four conditions, the main one being nothing to archive. Ordering after the change is archive 530, write 531.

The verifier checks it offline in one command, 50 checks. Two failures on the published code, none on the patched one. I zeroed a digest in a copy of the manifest as well, to confirm the script can fail, and it reported that row alone.

Everything sits in one folder at https://drive.google.com/drive/folders/1W7a8z98zYLtVgMHKnhOdNad0nQmRn9hH, open to anyone with the link. Manifest hashes to dfa8a6bda65d15ae747036f222102f8a6524580aa5bc3028637934e2959174d0 and the patch to 7c504ea63c3e5fd5c95c9e9033e76ec4ec183ec2553ab37593e3080c985cc86e.

What this does not do: no merge, the 1 November results are not back, and nothing about the tests changed. The retention gap stays on the record.
