---
deliverable: doc
id: 2026-11-09_hash-recomputation-v2
date: 2026-11-09
audience: reviewer
status: ready
approved: no
---

# Hash recomputation record, version 2 archive

Prepared on 9 November 2026 by Olusanya Timothy, against the seven items listed in Evelyne-Claudia's message of the same
morning. This record covers the version 2 archive only. Version 3 is not on this machine and is therefore not covered, which
is stated here rather than left to be inferred from an absence.

## 1. The archive

| Field | Value |
|---|---|
| Filename | F9b-refusal-pair-v2.zip |
| Byte length | 35,857 |
| SHA-256 | 29593fbc1f57a67325430de22d9578d7402d816178a94ff8437d02ec56dac706 |
| MD5 | a1764c08a6df0a30573c87a936f8caca |
| Google Drive record | MD5 a1764c08a6df0a30573c87a936f8caca, uploaded 7 November 2026 at 03:17:15 UTC, file ID 1TT1vkxbZOwcLf9Nq7_DuKqxtgblgMcTV |
| Read at | 9 November 2026, 11:10 UTC |

## 2. Method and conditions

Opening was done with Python 3.11.2 and the standard library `zipfile` module. Each member was read
with `ZipFile.read()`, which returns the decompressed bytes of that member from the archive stream. Nothing was ever
written to disk, never opened in an editor, and never passed through any text conversion, so no encoding or line ending
transformation could occur between the archive and the digest.

Digests were computed with the standard library `hashlib` on those bytes in the same process. The operating system was
Linux 6.1.158+, x86_64, glibc 2.36, running in a container. No other tool computed or
rewrote any of these values.

The CRC-32 column below is not one of ours. It is the checksum recorded in the archive's own central directory at build time,
so it is a second, independent control on the member bytes.

## 3. Members, paths, lengths and digests

Paths below are the paths inside the archive, exactly as stored. One root directory, `F9b-pair-v2/`, prefixes every member,
which matters when an extracted tree is compared against the archive listing.

| Member path inside the archive | Bytes | CRC-32 in the archive | SHA-256 of the member bytes |
|---|---|---|---|
| F9b-pair-v2/bench/common.py | 3,223 | d7c97edd | c4039b867b287388e7f90126ea78db2489836bf78a815c7805b64f1473cead45 |
| F9b-pair-v2/bench/host.py | 15,652 | 6d4de2d2 | 97aa10fc8dca799db7f089d782376e782bde8e7c1fdb8fe4ff3568bd62f8b32f |
| F9b-pair-v2/bench/store.py | 21,077 | 27ac4cc2 | 99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982 |
| F9b-pair-v2/pair2/result.json | 13,539 | 4bb88584 | b1271532794e18dfae64340bd1061bddb263d1d0ba491b16c2d49b65cdaf4553 |
| F9b-pair-v2/pair2-unmatched/result.json | 13,616 | 873bdab7 | 3b7f04425d4614ecad10600ecce01210b2741fab36823c60e0ee40fe0fc30342 |
| F9b-pair-v2/F9b-CORRECTION-04.md | 5,628 | dc7aaafe | 09ad209a94343f3cc3c0ac376d7d82a9dd8535c5ea4fabd45fd5b76e6b4f5a24 |
| F9b-pair-v2/F9b-refusal-pair-v2.py | 16,494 | 5d52e096 | f87ef861362ebe04cd10acf827d7d2664714805039c0327b753465b3d44bf412 |
| F9b-pair-v2/F9b-conflict-write.py | 17,594 | 590cbbc5 | 991e9eec09c291bf0179b6677577c5929b688df0b2b2c10fea2cc163d669e891 |
| F9b-pair-v2/RUN-v2.txt | 1,958 | 5fb51e63 | 0e00725b5e8820e6fa4b21cf2ab0c0885b2d0bc887788388a6f2d6a241d81680 |
| F9b-pair-v2/RESULT-refusal-pair-v2.txt | 1,548 | 05ccf83b | 14d8f32850371c5becf1b71e131eb20b779c2b471deadd0c3ec8f5afb4c4e542 |
| F9b-pair-v2/RESULT-refusal-pair-v2-unmatched.txt | 1,559 | 4b4cd7e7 | 5da82d7126b557d8ded9027db5dd1e1d8680fdb4d2a0f5aa216250e028b2d891 |
| F9b-pair-v2/F9b-refusal-pair-EXPECTATION.md | 3,045 | b1a2abb9 | 5994c0329bca4f6ba83abeff9c4b654231fd8381598e3d81e34dbcdc2fd61938 |
| F9b-pair-v2/LICENSE | 1,090 | aca4e440 | 414363e3ff1e09058cc7635bab0f5585c212f9e8281e788f7b6128fa9cf79f89 |
## 4. Comparison against the values reported on 8 November

| Reported item | Reported value | Value recomputed from the archive | Result |
|---|---|---|---|
| pair2/result.json | b1271532794e18dfae64340bd1061bddb263d1d0ba491b16c2d49b65cdaf4553 | b1271532794e18dfae64340bd1061bddb263d1d0ba491b16c2d49b65cdaf4553 | Match |
| pair2-unmatched/result.json | 3b7f04425d4614ecad10600ecce01210b2741fab36823c60e0ee40fe0fc30342 | 3b7f04425d4614ecad10600ecce01210b2741fab36823c60e0ee40fe0fc30342 | Match |
| Archive | 29593fbc1f57a67325430de22d9578d7402d816178a94ff8437d02ec56dac706 | 29593fbc1f57a67325430de22d9578d7402d816178a94ff8437d02ec56dac706 | Match |

Both members hash, from inside the archive, to the values published on 8 November. That answers the first of the three
questions, which is computational correspondence for this archive, and it answers nothing else.

## 5. What this record does not establish

Nothing here explains the two values reported from the other examination, and no cause is assigned to them. A match
establishes that the bytes inside this archive are the bytes hashed on 8 November. Silence follows on how any other value was
produced, on which file, with which tool, or at which point in that process.

Nor does this establish that the earlier examination was wrong. What it establishes is the content of this archive.

## 6. Version 3

Not performed. The version 3 archive is not present on this machine, which is the same gap recorded as loop L65: the working
copy was lost and the only surviving copy is the Drive upload at file ID 1QZufdZ6VFJJoKyWG-Xpzrr73FfRptkRf, 43,489 bytes,
MD5 162cec51c4d2bc3af8306a351d49ed88. Running the same procedure against it, and appending the result here as section 7, waits on the archive coming back into
hand. Until then the version 3 members are covered only by the 8 November digests, which is the limitation
already stated in the manifest.

## 7. Version 3, appended when available

Pending.
