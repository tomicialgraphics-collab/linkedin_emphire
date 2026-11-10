---
deliverable: doc
id: 2026-11-09_artifact-manifest-v3-v2
date: 2026-11-09
audience: reviewer
status: ready
approved: no
---

# Artifact manifest, F9b refusal pair, versions 3 and 2

Prepared 9 November 2026 by Olusanya Timothy. This page travels with the two archives and exists so that every value below
can be checked against a file in the reader's hands rather than against a message.

## What is attached

Two archives and the four result files they contain.

| File | Where it sits | Bytes | SHA-256 |
|---|---|---|---|
| F9b-refusal-pair-v3.zip | attachment | 43,489 | 3643a92c95e493923572e1908167a1e8ceca66fc41c2ba065d1fa7ec8bdd7ab6 |
| F9b-refusal-pair-v2.zip | attachment | 35,857 | 29593fbc1f57a67325430de22d9578d7402d816178a94ff8437d02ec56dac706 |
| pair3/result.json | inside v3.zip | not stated | d41a3e5546e1a4fe6683604d4bf237dad97da47e9693fead6428a64494beef81 |
| pair3-unmatched/result.json | inside v3.zip | not stated | 078b4e39f5a8a2f39f4e7b8c34de5dcd344c4faff0fe07a9a0f27df0cad1b351 |
| pair2/result.json | inside v2.zip | 13,539 | b1271532794e18dfae64340bd1061bddb263d1d0ba491b16c2d49b65cdaf4553 |
| pair2-unmatched/result.json | inside v2.zip | 13,616 | 3b7f04425d4614ecad10600ecce01210b2741fab36823c60e0ee40fe0fc30342 |

The two archives also carry an MD5 sum, which is the only digest one widely used platform will compute for us. Version 3 is
162cec51c4d2bc3af8306a351d49ed88. Version 2 is a1764c08a6df0a30573c87a936f8caca.

## Which values were computed today and which were not

Version 2, and the two result files inside it, were hashed again on 9 November and are unchanged from the values sent on 8
November. Version 3, and the two result files inside it, were hashed on 8 November from the copy now stored at Google Drive
file ID 1QZufdZ6VFJJoKyWG-Xpzrr73FfRptkRf, and were not re-hashed on 9 November because the working copy no longer exists on
this side. That is a limitation and it is stated here rather than left for the reader to discover.

Drive records its own MD5 for each upload. Version 3 is 162cec51c4d2bc3af8306a351d49ed88, created 8 November at
21:31:43 UTC, and version 2 is a1764c08a6df0a30573c87a936f8caca, created 7 November at 03:17:15 UTC. Both match the
local values above. A platform digest is still not an independent reproduction, and it is the closest thing available
without the archive being opened on another machine.

## How to check a value

On Windows PowerShell:

```powershell
Get-FileHash .\F9b-refusal-pair-v3.zip -Algorithm SHA256
```

On macOS:

```bash
shasum -a 256 F9b-refusal-pair-v3.zip
```

On Linux:

```bash
sha256sum F9b-refusal-pair-v3.zip
```

For a result file inside an archive, unpack first and hash the extracted file, not the archive. The path shown in the table
is the path inside the archive.

## What each outcome means

If every value matches, the bytes in both pairs of hands are identical and the question becomes reproducibility rather than
identity.

If the v3 archive matches but a result file inside it does not, the archive was modified after it was built, and the result
file that disagrees is the finding.

If the v3 archive does not match, the copy in the reader's hands is a different artifact. That is not a small result, it is
the whole result, and it needs recording before any comparison of the executions.

If a value cannot be computed because a file will not open, that is an unresolved result and it gets recorded as one rather
than as a mismatch.

## Two strings that separate the versions without interpretation

"25 distinct replies" appears in the version 2 result files and in neither version 3 file.

"distinct_by_exchange" appears in the version 3 result files and in neither version 2 file.

A result file carrying neither string, or both, is unresolved. It does not get sorted into a column.
