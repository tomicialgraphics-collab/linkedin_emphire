---
deliverable: dm
id: 2026-11-16_dm_behar-m1f-the-scope-of-the-guarantee
date: 2026-11-16
audience: direct
status: ready
approved: no
warm: yes
time_checked: >-
  checked: 2026-11-16 22:02 WAT, read from the system clock before this file was written.
profile_checked: >-
  Behar Dalipi confirmed M1e at 21:42 on 16 November with signed verdicts, two retries and five restarts: the journal
  byte-identical, the gap still visible, writes refused, f23 and f24 both caught, 22 verifier checks and 21 audit modes
  passing. He scoped the documented guarantee to the complete record missing its final newline and recorded the limit
  himself: recovery can quarantine a genuinely torn line before the retry's append open fails, and the reply still says
  unchanged. He is content to merge with that limit recorded.
premise: >-
  The limitation reproduced exactly, 44 torn bytes quarantined by recovery, the file going from 341 to 297, and the
  retry answering unchanged without touching it. No behaviour changed in this revision: the guarantee is now written at
  its real size and pinned by a mode, so it cannot widen without a check failing.
sources_read: >-
  read: his 21:42 message, the M1e tree, and the run of the new mode on both trees. Every number here comes from a run
  made on this machine on 16 November.
fix_verified: true
fix_evidence: >-
  CLIENTS/hfb/2026-11-16_m1f-pack/03-this-change/f25.log and regressions.log, produced on 2026-11-16 on this tree; the
  same mode against M1e is 02-previous-change/f25.log, which passes there too because the behaviour was never broken.
premise_checked: >-
  checked: the before side is M1e, the tree he cleared, identified by file hash in its revision file. f25 passing on both
  trees is stated in the message rather than left to be discovered, because a mode that passes before and after is
  either honest scoping or a mode that tests nothing.
---

## DM, paste this

<!-- gate:body:start -->
Your limit reproduces exactly, and you've scoped it the right way round.

A torn line is damage rather than a gap, so recovery quarantines it before any append is attempted. On a replay with 44 torn bytes: the file goes from 341 bytes to 297, the quarantine file holds those 44 with their sha256, no journal gap is claimed, and then the retry fails at open and answers unchanged. That is true of the retry and says nothing about the 44 bytes recovery removed a moment earlier.

What changed, and it is documentation rather than behaviour. The module docstring now carries the scope in four sentences. The audit readme has a section on it, so a reviewer meets the limit before the modes. And f25 pins both halves: recovery quarantines exactly those bytes and calls it damage, the retry changes nothing itself, and the reply is unchanged.

f25 passes on M1e as well, which is the honest result rather than a weak one. The behaviour was never broken. The claim was too broad, and the mode exists so the scope is tested where it is stated.

No code that decides anything changed. bench/store.py differs from M1e only in its docstring.

bench/store.py 0989c8db, audit/regressions.py 490de706, audit/README.md ae147a28, patch 27b0c47b, zip 52f2d5bf, 17 files. Twenty-two modes, 22 caught, 0 missed. run and verify both clean.
Folder: https://drive.google.com/drive/folders/16WHG81Vij9N5CI1rx_HcYLA-gCCNgG_Q
That folder is the one to use from here.

There is one thing in the readme you may want to overrule. I recorded why the limit is recorded rather than fixed: recovery has to remove a torn line to produce a readable journal, a refusal has to leave the file alone, and only one of them can own the file at that instant. The alternative is a reply that distinguishes my append from what recovery did before it, which changes the reply shape and would need its own review. It's written down as the next thing to do if you want it, not folded into a documentation revision.
<!-- gate:body:end -->

## Why the limit is agreed with, not argued around

He found it, he scoped it correctly, and he set the condition for merging. The message reproduces his case with numbers so the agreement is checkable rather than polite, and then does exactly what he asked.

The one thing the message will not do is imply the reply was right. It says plainly that `unchanged` is true of the retry and says nothing about the bytes recovery removed, which is his sentence, restated.

## Why f25 passing on both trees is said out loud

A mode that passes before and after looks like a mode that tests nothing. Stating the reason in the message, and in the mode's own docstring, keeps it honest: the behaviour was never broken, the claim about it was too broad.

Leaving that for him to discover would be the kind of thing that costs a reviewer's trust in the whole set.

## The offer at the end

The reply-shape change is real and it is his call. Naming it, with the reason it was not folded in, is the difference between a documentation revision and a quiet behaviour change smuggled into one.

If he says do it, it becomes its own change with its own mode, and f25 changes to assert the new field rather than the old silence.

## If he merges

Nothing further from this side. The merge condition was his, it is met, and the next message should be about the thing after it rather than about this.
