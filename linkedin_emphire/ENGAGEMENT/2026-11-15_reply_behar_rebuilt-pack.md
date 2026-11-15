---
deliverable: dm
id: 2026-11-15_reply_behar_rebuilt-pack
date: 2026-11-15
time_checked: >-
  checked: 2026-11-15 09:57 WAT, read from the system clock in the sandbox immediately before delivery.
audience: collaborator
status: ready
approved: no
warm: yes
profile_checked: >-
  Behar Dalipi asked at 09:44 for the revised ZIP and hashes when they were ready, and said he would rerun both cases
  against the pinned revision. He is the reader, so every number below is one he can check himself against a file in
  the pack or against the zip hash.
premise_checked: >-
  checked: the pack was rebuilt and both cases were run on fresh checkouts before this message was written. The zip was
  built twice and hashed twice, both times e997029d, so the printed hash is reproducible. The one place the earlier
  message was wrong is corrected here in his message, not only in the pack.
sources_read: >-
  read: CLIENTS/hfb/2026-11-14_m1-pack/ (README, rebuild.sh, make_zip.sh, both probes, both two-cases logs and JSON),
  bench/store.py at the pinned revision and after the patch.
---

Pak rebuilt and uploaded. I built it twice and the hash matched both times.

```
M1-pack-host-failure-benchmark-2026-11-15.zip
36,215 bytes, 24 files
sha256 e997029d4b94701f1ce92e8d089a73b89d968ee3153097a9cd344350e44018cc
```

Download: https://drive.google.com/file/d/1dmhqD3LNvA9a9CMWwr5lYaDKPwhc3pGy/view. That is the
HFB folder you already have, and the new file replaces the 14 November one in it.

The hashes inside the pack, all repeated in the revision file under the baseline folder:

```
commit                 126f1c00dfae18b30456a8dc698ac906ca7ddb0e
bench/store.py before  99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982
bench/store.py after   b987cc49e186d9281ce86eca76a940319107002d4c5bc05d2ce362f7acc70085
patch.diff             14997eac567061e6fb53415b1c0da0ea043f0435444b4cc48477f6b849ad67d9
```

One correction to my 09:47 message, because the code says otherwise. I said the missing newline
left a record the store couldn't read, and that the gap would name a withheld sequence number.
Neither holds. The unterminated line is complete JSON with a valid digest, so the first restart
does read it and does name the conflict. Loss happens in that same start-up: the boot append
finds an unclean tail, truncates the record into a quarantine file beside the journal and
rewrites the journal, so restart 2 opens a clean file with no conflict record in it. What can be
named is the quarantined byte range, not a sequence number.

The two cases, both in the second probe in the harness folder, both run on both revisions:

**Case A, final newline removed, one journal restarted in place.** On the pinned revision restart
1 names the conflict and rewrites the file; restarts 2 to 5 report the action conflicted with
nothing to name it. With the patch, every restart reports a named gap, 328 bytes at byte 1335,
store_seq 5, kind conflict. It's withheld rather than indexed, writes are refused while it
stands, and the file stays byte-identical at `573a5554...`.

**Case B, batch write half-written and rollback refused.** You get `durable: "unknown"` with
`disk_state: "unknown"` and reason `rollback-failed`, never `durable: false`. On the pinned
revision that state can't be produced at all; its nearest answer to a refused write is
`durable: false`, which is the claim the patch stops making.

The probe exits 2 on the pinned revision and 0 with the patch. the rebuild script refuses to
write a pack if either probe answers wrongly, and the two verifier outputs are still
byte-identical.

Not in this pack: S3, S4, S5. Nothing pushed.
