# P1: the four recovery and authority items

Olusanya Timothy. 1 November 2026.

This is the second patch in the exchange. The first (P0) made the verifier reject
the counterexamples the review supplied. This one fixes the four items the
review listed as P1, and it is a single commit on top of the P0 branch.

Base: `9194c61` (`p0-authenticated-recovery`), which is `3b6b781` on `25cd57f`.
The patch applies clean to a fresh checkout of `9194c61` and, as the cumulative
variant, to `25cd57f` directly.

## The four, one at a time

| finding | what was wrong | what changed | the check that fails without it |
| --- | --- | --- | --- |
| F11 | the store indexed a record in memory before appending it to its journal, so for the length of one write it reported a decision a restart would not have | the journal append happens first and the sequence number is only consumed once the bytes are on disk; a journal that refuses a write returns `ok: false, durable: false` and memory is untouched | `journal-first` |
| F7 | a repair truncated a torn journal and reported how many bytes it dropped, then dropped them | the discarded tail is copied to `store.jsonl.quarantine-N.bin` before the truncation, and the repair record carries that file's name, byte count and sha256 | `repair-quarantine` |
| F9 (state half) | two verdicts for one action resolved to whichever record a component read first | a second verdict that differs from the first is recorded as a conflict naming both sequence numbers, the state becomes `conflicted`, and neither record closes the gap. The verifier recomputes the same rule from the journal | `conflict` |
| F10 | the host logged an effect whether or not the store's reply answered the request it had made | a reply counts only if it is well formed, reports success, and names the action that was asked about. Anything else produces `reply_rejected` with the reasons, and the effect is withheld | `reply-checked` |

Two of these are orderings inside a process and two are defects in what the
artifacts contain. That distinction is carried into the regression suite: F7 and
F9 are counterexamples that damage the evidence, F10 and F11 are counterexamples
that restore the old code. Mutating an artifact cannot demonstrate a bug that
lives in the order of two writes, and a suite that pretended otherwise would be
testing its own mutation.

## Three probes

None of these four can be shown inside the main run without damaging the record
the rest of the suite depends on. So `run.py` runs three short probes at the end,
each in its own directory, each with its own journal where it needs one:

- `probe-durability` starts a store with `HFB_FAILPOINT=verdict`, which makes the
  journal refuse a verdict write before any bytes are produced. It asks for a
  verdict, then asks the same process what it knows, then restarts the store and
  asks again. The expected answers are: `ok: false`, nothing, nothing.
- `probe-repair` writes a two-record journal with a third record cut mid-line,
  starts the store on it, and lets the repair happen. The verifier then requires
  the repair record's quarantine file to exist with the byte count and digest the
  repair claims.
- `probe-reply` starts `bench/stub_store.py`, a fixture that answers every
  request, succeeds at every request, and names `S-0000` in every verdict reply.
  Host scenario E ships a verdict to it. The expected answer is a named rejection
  and no effect.

The failpoint is a test hook inside the store, not a simulated disk failure. It
refuses the write at the one moment the ordering matters, which is what makes the
result checkable; it does not stand in for a full disk, a dying device, or an
interrupted fsync. That limit is the same one the note states about the whole
suite.

## What the numbers are now

```
python verify.py example/run        -> 20 of 20 checks hold (12 P, 2 V, 6 meta)
python challenge.py <run>           -> 10 of 10 mutations caught
python audit/regressions.py         -> 12 of 12 counterexamples caught
two consecutive runs compared       -> identical, file by file
```

Check count 16 to 20. Four new checks, all in class P, because all four are about
whether evidence outlives the process that made it. The class V count is
unchanged at 2, and so is the sentence attached to it: a signature over a record
still proves integrity and provenance and nothing about authorisation.

The regression suite went from 8 modes to 12:

| mode | kind | caught by |
| --- | --- | --- |
| f7 | the quarantine file deleted | repair-quarantine |
| f9 | the conflict record removed | conflict |
| f10 | the host's reply check disabled | reply-checked |
| f11 | memory indexed before the journal | journal-first |

## Three things that will look like regressions

`example/run` is regenerated again, because the artifact set changed: the three
probe directories are now part of a run, and the manifest lists them. The old
example fails the new completeness check, which is the correct outcome.

The check count moves from 16 to 20.

Two fields in the store journal changed name and meaning. `replayed_seq` was
`journal.seq - 1`, which was wrong by one and read as though it were a sequence
number. It is now `replayed_records`, and it is the count of records the replay
recovered: 2 for a two-record journal, 0 for a fresh one. Any reader that was
parsing the old field should read the new one, and the repair record now also
carries the quarantine fields.

## What is still open

Identifiers are still chosen by the caller. The store records the registration
and, since the P0 patch, the note says "registered" rather than "issued". Making
the store mint the id is a five-line change to the protocol and a large change to
the scenarios: A' exists to show silence when no prior expectation was registered,
and under strict minting any action the host can name is one the store already
knows about. That row would have to be recast, and recasting it changes the
scenario table rather than fixing a defect. I would rather put that to you as a
design question than ship it inside a bug-fix patch.

Also unchanged: an idle connection can still hold the store (F15); the verifier
still imports the encoder it checks, so the correlated-oracle problem stays until
there is a second encoder; and there is no CI matrix, so the cross-platform claim
is still two runs compared by hand.

## Applying it

On top of the P0 branch:

```
git checkout p0-authenticated-recovery
git apply host-failure-benchmark-p1.patch
git add -A
git commit -m "P1: journal before memory, repair that keeps its bytes, named conflicts, checked replies"
git push -u origin p0-authenticated-recovery
```

Cumulative, from `25cd57f`:

```
git checkout -B p1-recovery-and-authority 25cd57f
git apply host-failure-benchmark-p1-cumulative.patch
git add -A && git commit -m "P0 and P1"
```

On Windows, in PowerShell, from the root of the checkout:

```powershell
python verify.py example\run
python challenge.py example\run
python audit\regressions.py
```

## Platform note, stated plainly

Everything above was run on Linux, Python 3.11.2, from a fresh checkout with the
patch applied and from the zip. Windows 11 with Python 3.14.5 has run the suite at
P0: 16 of 16 checks and 9 of 9 mutations. This patch has not been run on Windows
yet. The two additions that touch the platform are the probes, which use the same
process announcement and the same newline handling as the rest of the suite, and
nested artifact paths in the manifest, which are written with forward slashes so
that a Windows run and a Linux run produce the same manifest bytes. Both are
stated as expected, not as observed, until you run it.
