---
deliverable: dm
id: 2026-11-14_dm_behar-m1-pack
date: 2026-11-14
time_checked: >-
  checked: 2026-11-14 18:19 WAT, read from the system clock in the sandbox before this file was sent for gate.
audience: collaborator
status: ready
approved: no
warm: yes
profile_checked: >-
  Behar Dalipi said on the morning of 14 November that he will review the M1 evidence when the
  pack arrives, and ruled V04 inside F-08 as scope in the same message. The pack is S1 only.
sources_read: >-
  read: the public benchmark at commit 126f1c0, cloned and run rather than described. The runner
  and the verifier were executed on both revisions, and the probe was written against the store's
  own socket protocol. No part of this pack is quoted from the earlier thread.
premise_checked: >-
  checked: on 14 November 2026, in this environment. Baseline probe exits 2 with two named
  failing cuts. Patched probe exits 0 at all five. The verifier exits 0 on both revisions with
  byte-identical output. The patch applies cleanly to a fresh clone of 126f1c0 and produces
  ead1b552be700468168a784533750941fbc83fe23f938709a972c7f1d2867df7. The delivery zip is
  23196 bytes, sha256 fe074db79f0c139ec7b3fe992fddc41d3f66d7665f8f22f84f69fd4bbfcb7d24 and md5
  314cebedbc1caab95be6180bb47f774a, reproducible with make_zip.sh. Drive folder 1xAvOeWh1KMv9XPJyoA3QhsvvntDe-fRo, public as reader,
  not discoverable by search.
---

# The M1 pack: the link, the hashes, and why both

The thread agreed "two hashes and a revision, no links". The pack has outgrown that: sixteen
files plus a hash list is not a thing to attach to a message. So it goes as one folder plus one
zip, and the hashes stay in the message so the link is not load-bearing. That is a deviation
from the shape agreed with him, and the message says so in the sentence where it happens rather
than leaving him to notice it.

**Drive folder** (viewer for anyone holding the link, not discoverable by search):
`https://drive.google.com/drive/folders/1xAvOeWh1KMv9XPJyoA3QhsvvntDe-fRo`

Contents: the zip, plus the pack's readme and its classification log as separate files so the
argument can be read without downloading anything.

**The zip:** 18 files, 23,196 bytes, sha256 `fe074db79f0c139ec7b3fe992fddc41d3f66d7665f8f22f84f69fd4bbfcb7d24`,
md5 `314cebedbc1caab95be6180bb47f774a`. Deterministic: two builds from the same folder produce
the same hash, which is the only reason a hash of a zip means anything. The md5 is the number
Drive itself displays, so the download can be checked without a command line.

**Why Drive and not the repository.** The repository holding this pack is the owner's own, and a
finding about somebody else's benchmark does not get published by us before he has read it. The
pack also carries his rulings from a private exchange. Drive gives a link with a viewer role and
no search visibility, which is the same rail used for the Favre exchange, and it can be closed
when the round ends.

## What was actually run

Not described. Run. The public tree at `126f1c0` was cloned, the runner and the verifier
executed, and a probe written against the store's own socket protocol: issue, verdict ALLOW,
verdict BLOCK. Then the journal that conflict produced was cut at every line boundary, and each
cut image handed to a fresh store process.

Baseline, `line-4` at byte 1277, which is the boundary between the two writes:

```
conflicted=True, conflict record=False, verdict seqs=[3, 4]
```

That is the defect, and it is not an edit: it is a place a crash can stop the file.

Patched tree, all five cuts:

```
Every cut either reports no conflict or reports one it can name with both sequence numbers.
```

## What moved and what did not

- The twenty-two suite checks: all hold, before and after, and the two verifier outputs are
  byte-identical, both `b3f990f4...` in the hash list.
- Twenty-four artifacts: twenty-three byte-identical. `store.jsonl` differs on two of its
  eighteen lines, by one added field each, `batch`. No field removed, no sequence moved.
- The `conflict` check still passes without being edited, because the conflict record still
  carries `first_seq` and `second_seq`.

## What the pack does not claim

**The cut is a model, not a measurement.** Truncating the journal at a line boundary is a
deterministic stand-in for a crash between two fsyncs. It says nothing about device behaviour
under power loss, and no claim in the pack rests on hardware.

**S1 is not the milestone.** S3, S4 and S5 are absent, and S4 keeps its own schedule.

**The patch is not pushed.** It is a diff against a hash. Whether it goes in is his call in his
repository, and the register is his to move. V04 is recorded here as scope on his ruling, with
his reasoning attached, and the published text still reads disputed.

## The message

```
Behar,

The pack is ready: one folder, one zip inside it, and the hashes in this message.

https://drive.google.com/drive/folders/1xAvOeWh1KMv9XPJyoA3QhsvvntDe-fRo

We agreed two hashes and no links. Sixteen files is too many to attach, so the files are in a folder instead, and the hashes stay here so the link is not the thing you have to trust. The zip is 23196 bytes. Its sha256 is fe074db79f0c139ec7b3fe992fddc41d3f66d7665f8f22f84f69fd4bbfcb7d24 and its md5 is 314cebedbc1caab95be6180bb47f774a, which is the number Drive shows next to the file, so you can check what you downloaded before you open it. Every file inside carries its own hash in the manifest the zip contains. The folder is viewer access for anyone holding the link and is not searchable.

What the pack tests, by cutting rather than by describing: a real conflict goes through a real store, the journal that conflict leaves is cut at every line boundary, and each cut image is handed to a fresh store that is asked two questions. Is this action conflicted, and can you name the conflict. On the pinned revision, two of the five cuts answer yes and no. One is the boundary between the two writes you narrowed, the other is inside the conflict record's own write.

With the change, all five either report no conflict or report one they can name with both sequence numbers. The incomplete batch is withheld from the index and the store says so on start-up, so half a claim is not a claim.

All twenty-two checks hold at both revisions and the verifier output is byte-identical between them. Twenty-three of twenty-four artifacts are byte-identical, and the store journal differs on two of its eighteen lines by one added field each. No field removed, no sequence number moved, and the conflict check still passes without being edited.

Three limits, stated rather than left to be found. The cut is a model of a crash between writes, not a measurement of a device under power loss. S3, S4 and S5 are not in this pack, and S4 keeps its own schedule. The patch is a diff against a hash and stays a diff; whether it goes in is yours.

One question. If your S1 narrowing meant something narrower than one write and one fsync for the pair, say which of the two records you expected to carry the pairing, and I will rebuild the pack against that instead.

Olusanya
```
