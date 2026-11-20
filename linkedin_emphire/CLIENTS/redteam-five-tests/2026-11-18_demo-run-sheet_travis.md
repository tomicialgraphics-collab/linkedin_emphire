---
deliverable: doc
id: 2026-11-18_travis-demo-run-sheet
date: 2026-11-18
audience: internal
status: ready
approved: no
time_checked: >-
  checked: 2026-11-18 22:29 WAT, read from the system clock before this file was written.
premise_checked: >-
  checked: every command and every line of expected output below was run or read in this workspace before the sheet was
  written. The self-test takes 0.13 seconds and prints exactly the failure quoted here. The three log excerpts come
  from 04-prefix-collision.log at the line ranges given, and they are quoted verbatim.
sources_read: >-
  read: the version 2 correction pack of 14 November, its readme, its log and its verifier. No page opened.
---

# What I show Travis, and how

Five minutes. One terminal, one shared window, font at 20pt or larger, nothing else on screen. No slides, no repo
explorer, no idling - every command is run fresh so the output appears while he is watching.

## 0:00 to 0:30, the frame

Say this before typing anything:

> A verifier was published, and it passed its own suite fifty checks to zero. It could not fail. I am going to show you
> the exact input it passed, then the same input against the fixed version.

## 0:30 to 2:00, the failure, from the recorded run

```
cd CLIENTS/redteam-five-tests/2026-11-14_run-record-fix-v2
sed -n 24,29p 04-prefix-collision.log
sed -n 67,69p 04-prefix-collision.log
```

On screen: the row `pass  console.log digest of the stored object   4889096bc551a891`, then `50 passed, 0 failed`.

What to say over it: that digest is sixteen characters and the true one is sixty-four. The manifest disagrees with
the object in every character after the sixteenth, and the check calls it a pass. The number on the right is the whole
suite agreeing.

## 2:00 to 3:00, the same input, fixed

```
sed -n 212,215p 04-prefix-collision.log
sed -n 257,260p 04-prefix-collision.log
```

On screen: `FAIL  console.log digest of the stored object    got 4889096bc551a89116ee8e83..., manifest says
4889096bc551a891ffffffff...` and then `53 passed, 1 failed`.

Say: same input, same machine, one row. The fix is a comparison on all sixty-four characters, in all five places it
appears.

## 3:00 to 4:00, the live proof that the checker can fail

```
python3 03-verify_run_record.py --self-test
```

On screen, in about a tenth of a second:

```
FAIL  prefix collision is a difference               got e41eba7f89729c8300000000..., manifest says e41eba7f89729c8358da8b98...

self-test: 0 passed, 1 failed (1 failed means the checker compares all 64)
```

This is the moment of the demo and it looks like the wrong result. Say the sentence plainly: a check that cannot fail
is not a check, so the self-test is designed to fail, and it exits zero only when it does. A future edit that puts
prefix comparison back turns this red.

## 4:00 to 5:00, the limit

Say what the verifier is not. It checks that the objects named in a manifest are the objects on disk and in git at the
commit named, and that the record and the package are bound to each other. It cannot tell whether a run should have
been performed at all, and it does not claim to. That sentence is the difference between a tool he can rely on and a
tool he has to trust.

## If anything goes wrong on screen

Do not debug in front of him and do not narrate it. Open the same three log ranges, which carry the same evidence, and
say the live run is the same thing he is reading. Then move to the ten minutes on his number.

## What is not shown

No repository checkout is available in this sandbox, so the `--repo` run at fifty-four checks against a live checkout
is described rather than performed. Say so if he asks for it, and offer it as a follow-up with the checkout.

## The three sentences to leave him with

1. A suite that passes everything is telling you about the author's confidence, not the coverage of the instrument.
2. If the checker cannot fail, nothing downstream of it means anything, and the failure has to be a fixture in the
   test set rather than a memory in somebody's head.
3. Any number you publish should ship with the command that reproduces it, and the line saying what it cannot see.
