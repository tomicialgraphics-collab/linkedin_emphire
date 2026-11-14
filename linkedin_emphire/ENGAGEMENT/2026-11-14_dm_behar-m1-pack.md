---
deliverable: dm
id: 2026-11-14_dm_behar-m1-pack
date: 2026-11-14
audience: collaborator
status: ready
approved: no
warm: yes
profile_checked: >-
  Behar Dalipi said on the morning of 14 November that he will review the M1 evidence when the
  pack arrives, and ruled V04 inside F-08 as scope in the same message. The pack is S1 only.
sources_read: >-
  read: the public benchmark at commit 126f1c0, cloned and run rather than described. The runner
  and the verifier were executed on both revisions, and the probe was written against the store's own
  socket protocol. No part of this pack is quoted from the earlier thread.
premise_checked: >-
  checked: on 14 November 2026, in this environment. Baseline probe exits 2 with two named
  failing cuts. Patched probe exits 0 at all five. verify.py exits 0 on both revisions with
  byte-identical output. The forty-line patch applies to bench/store.py at
  99f25cab23b3dea0f6f739a96fae23bc25bbc3d0a0db96e801ac7d701ae1f982 and produces
  ead1b552be700468168a784533750941fbc83fe23f938709a972c7f1d2867df7.
---

# The M1 pack: one property, two revisions, and the edges of the claim

Pack: `CLIENTS/hfb/2026-11-14_m1-pack/`, sixteen files plus a hash list. Two hashes, one
revision, no links, which was the shape agreed.

## What was actually run

Not described. Run. The public tree at `126f1c0` was cloned, the runner and the verifier executed,
and a probe written against the store's own socket protocol: issue, verdict ALLOW, verdict
BLOCK. Then the journal that conflict produced was cut at every line boundary, and each cut
image handed to a fresh store process.

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
  byte-identical, all thirty lines.
- Twenty-four artifacts: twenty-three byte-identical. `store.jsonl` differs on two of its
  eighteen lines, by one added field each, `batch`. No field removed, no sequence moved.
- The `conflict` check still passes without being edited, because the conflict record still
  carries `first_seq` and `second_seq`.

## What the pack does not claim

**The cut is a model, not a measurement.** Truncating the journal at a line boundary is a
deterministic stand-in for a crash between two fsyncs. It says nothing about device behaviour
under power loss, and no claim in the pack rests on hardware.

**S1 is not the milestone.** S3, S4 and S5 are absent, and S4 stays open on its own schedule.

**The patch is not pushed.** It is a diff against a hash. Whether it goes in is his call in his
repository, and the register is his to move. V04 is recorded here as scope on his ruling, with
his reasoning attached, and the published text still reads disputed.

## The message

```
Behar,

The pack is with this message: sixteen files plus a hash list, two file hashes, one revision.

What it contains is one property, tested by cutting the journal rather than by describing it. A real conflict goes through a real store, the journal that conflict leaves is cut at every line boundary, and each cut image is handed to a fresh store that is then asked two questions: is this action conflicted, and can you name the conflict. On the pinned revision, two of the five cuts answer yes and no. One is the boundary between the two writes you narrowed, the other is inside the conflict record's own write.

With the change, all five either report no conflict or report one they can name with both sequence numbers. The incomplete batch is withheld from the index and the store says so on start-up, so half a claim is not a claim.

The rest of the pack is the part I would want if I were reading it: all twenty-two checks hold at both revisions and the verifier output is byte-identical between them, twenty-three of twenty-four artifacts are byte-identical, and store.jsonl differs on two of eighteen lines by one added field each. No field removed, no sequence number moved, and the conflict check still passes without being edited.

Three limits, stated rather than left to be found. The cut is a model of a crash between writes, not a measurement of a device under power loss. S3, S4 and S5 are not in this pack, and S4 keeps its own schedule. The patch is a diff against a hash and stays a diff; whether it goes in is yours.

One question. If your S1 narrowing meant something narrower than one write and one fsync for the pair, say which of the two records you expected to carry the pairing, and I will rebuild the pack against that instead.

Olusanya
```
