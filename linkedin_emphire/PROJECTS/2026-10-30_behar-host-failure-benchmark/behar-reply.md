# Messages to send Behar

Three parts: the reply that has already gone (kept here as the record), the
message that carries the P0 patch, and short answers for what follows.

Attachments for LinkedIn: `P0-PATCH-NOTES.html` and
`host-failure-benchmark-p0.patch.txt`. LinkedIn takes HTML and TXT and does
not take `.patch` or `.zip`, so the patch travels as a text file with its real
extension at the end. He renames it after saving.

---

## 1. Already sent: the response to the audit

Behar, thank you. I read the audit twice and then reran the counterexamples myself rather than take them on trust.

You are right on the P0s. Six of the seven reproduce on my machine, including the two that matter most: a WAL verdict flipped from BLOCK to ALLOW with a stale signature still verifying clean, and deleting seven host journals still leaving a full pass. One is worse than reported. T14 does not just clear a named gap, it also clears it in the verifier's own recomputation, so the store and the checker agree that a forged unsigned record closed a gap.

Two claims of mine are wrong and I am withdrawing them rather than defending them. The note calls the store an independent issuer of identifiers when it accepts an id from the caller, and it says nine scenarios where the suite runs eight.

One correction on your side. T08 does not behave the way the report describes it: changing only the WAL timestamp makes B.wal fail and B hold, the reverse of the line in the report. The substance of F2 stands, but the regression test should be written against what actually happens.

I have a written response, finding by finding, and a reproduction script with one mode per finding that anyone can run against the repository. The P0 fixes are in progress. I will send the patch when the counterexamples come back failing.

Author order and venue stay where we left them until then.

---

## 2. Send now, with the two attachments

Behar, the P0 patch is attached, and it is built so you can check it rather than read my claim about it.

Apply it to a clean clone at 25cd57f, then run three commands. Before the patch, six of the seven counterexamples pass verification. After it, all seven are caught by the check that claims to catch them:

- a WAL verdict flipped to ALLOW with a stale signature now fails B
- an unsigned verdict no longer erases the C-3003 gap
- deleting the seven host journals now fails the completeness and scenario checks
- a rewritten actor or policy, and an epoch timestamp, now fail D
- a torn host journal now produces a report with an explicit unreadable state instead of a traceback

The patch also checks WAL and recovered verdicts against their signatures, compares the actor and the policy hash against the constants in common.py, and writes a versioned manifest with per-scenario event chains.

Two things will look like regressions and are not. The check count goes from 14 to 16, and example/run is regenerated, because verdict records now carry a state and the manifest is version 2. The old example fails the new checks, which is the correct outcome.

I ran the whole thing on Windows 11 with Python 3.14.5 and on Linux: 16 of 16 checks, 9 of 9 built-in mutations, 7 of 7 counterexamples, and two runs byte-identical file by file. There is still no CI matrix, so H4 is answered by a run and not by a pipeline.

What the patch does not fix is listed in the notes under the P1 and P2 headings: journal before memory, non-destructive repair, conflicts on duplicate verdicts, reply validation in the host, store-minted ids, the idle socket, and the verifier still importing the encoder it checks.

Two requests. Put the 38-case package in as audit/, next to the regression script, so the two sets live together. And let me cite your review in the note once P1 lands.

---

## 3. Now: the message that carries v1.1

Attachment: `AUDIT-RESPONSE-v1.1.html`. Nothing else, since the patch is already
on the branch and the notes travel with it.

---

Behar, both of your points are in the code and in the write-up now.

On T08 you are right, and the distinction is the part worth keeping. Changing the
WAL before the store replays makes the replayed record and the WAL carry the same
altered value, so B.wal holds and B fails. Changing it only after replay completes
makes B.wal fail. Those are two different properties and the suite now tests them
separately: f2a and f2b, each one asserting what must fail and, just as important,
what must not.

Eight counterexamples, eight caught. At 25cd57f six of the eight were accepted
or mishandled.

F2 stands exactly as you put it. Agreement between two files is convenience, not
attestation, and what the patch adds to the timestamp is a bound, not a witness.
The updated response has the two-row table at the front rather than in a footnote.

There is a second commit on the branch and it is mine to explain before you find
it. The regression runner found its run directory by parsing a printed path, which
breaks on Windows, and it then treated an existing artifact directory as proof the
suite had finished. A run that stopped early therefore died on a missing journal
instead of on its own cause, which is the same mistake as the separator one one
level up. It now requires every artifact the suite writes, retries, and prints the
run's output when none completes.

Run `python audit\regressions.py` on `p0-authenticated-recovery`. If it does not say
eight caught, tell me and I will fix that before the P1 work starts.

P1 list unchanged, and the two requests too: the 38 cases as audit/cases/, and
the review citable as REVIEW-2026-11-01.md.

---

## 4. If he asks

**"Can you demonstrate genuine host loss?"**
Not on one machine. C, C' and C'' exit with os._exit(9), so what the suite tests is a process that leaves deliberately, not a host that disappears. I will rename it everywhere, state the failure domain in the note, and list the two experiments that would cross it (an external kill at a barrier, destruction of the host-local filesystem). Both need a second failure domain: another machine, or a container with its own volume. I would rather declare that out of scope than simulate it and call it host loss.

**"Why does a substituted timestamp fail rather than being marked unverified?"**
Because a counter step is either in the host journal or it is not. If it is not, the record claims a decision the host has no evidence of, and unverified is too generous a word for that.

**"Is the suite still worth publishing?"**
As a demonstration of the named-gap result, yes, and your Appendix B is close to the sentence I would use. Not as authenticated recovery or host-loss survival. Those stay blocked until P0 and P1 are done and the claims matrix shows a test behind every guarantee sentence.

**"What about authorship?"**
Unchanged and settled the same way we agreed: at finalisation, against CONTRIBUTION.md, after the patch cycle.

---

## 5. The message that carries P1

Attachment: `AUDIT-RESPONSE-v1.2.html` and `P1-PATCH-NOTES.html`. Nothing else.

---

Behar, the four P1 items are done, in two commits on top of the branch: the
code, and the regenerated example.

To your list, in your numbering. F11: the store journals before it indexes, and a
journal that refuses a write answers that it could not persist instead of
answering from memory. F7: a repair copies the bytes it removes into a
quarantine file and records its length and digest in the repair record. F9: two
verdicts that disagree become a named conflict carrying both sequence numbers,
and the action stays unresolved. F10: a reply counts only if it names the action
that was asked about, and a store that confirms the wrong one gets a rejection
and no effect.

Two of those are orderings inside a process, so their counterexamples restore the
old code rather than damaging an artifact. f7 and f9 damage evidence, f10 and f11
damage the program. Twelve counterexamples now, ten mutations, twenty checks,
twelve of them class P.

F6 I have not changed, and I want to ask rather than decide. If the store mints
every id, then C'' and A' stop being possible for any action the host can name,
because naming it is registering it. Those two rows are the silence cases, and
they are the strongest thing in the table. Do you want strict minting with both
recast, or registration kept and the claim kept as narrow as it is now?

Everything above was run on Linux from a clean checkout. Windows has run P0 and
this patch has not been on Windows yet; the notes say that where it belongs
rather than in this message.

---

## 6. The message for his reproduction (send this one)

Attachment: `P1-PATCH-NOTES.html`. Nothing else.

---

Behar, good, and here is what you need in order to reproduce it rather than take
my numbers.

`main` at `df0cf5a`, three commits past your 25cd57f. From the root of the
checkout: `python verify.py example\run` and `python audit\regressions.py`.
Expected 20 of 20 and 12 of 12. `python run.py` then `python challenge.py` on the
directory it prints gives you 10 mutations caught and 2 input checks held.

One thing you should find before you find it yourself. The first Windows run of
this patch broke my own verifier twice. Pointed at a directory that does not
exist, it printed a failed check and then raised FileNotFoundError while writing
its report, after the P0 notes had promised it no longer raises. Worse: given two
directories that were both absent, it reported determinism holds. Absent compared
to absent is a match, so two runs that were not there were called identical,
which is the same defect as a missing artifact passing a completeness check, in
the program that exists to catch that.

Both are fixed in the third commit and both are tests now. A path that is not a
run is refused with exit 2 and no traceback, and a comparison fails when either
side is missing an artifact. Neither changed a result in the response, because
every number in it came from a run that existed. But you should have the version
that refuses them rather than the version that quietly agreed with nothing.

Windows now shows the same 20, 10 and 12 as Linux, at the commit above.

---

## 7. The message for the 9:05 PM review

Attachment: `FINDINGS-REGISTER.md` as a PDF or paste the table, since LinkedIn takes
neither Markdown nor a folder. Ask for the report and the package to be readable here
before any assessment of the eleven is written.

---

Behar, this is the right next step and the register is the right instrument for it.
I have started one rather than promising one: `FINDINGS-REGISTER.md`, one row per
finding, with the status words defined so that "fixed" can only mean a reproduction
that fails without the commit.

I have not yet read your report or opened the package. The attachment came through
LinkedIn, which shows me the filename and not the file, and the Drive link is not
reachable from where I work, so both need to reach me another way before I assess
the eleven cases. Rather than wait, I went through the five areas in your message
against `df0cf5a` and found three defects of my own in them.

One. Recovery authenticates by trust. On replay the store takes a record's `state`
from the journal instead of recomputing it, so an unsigned verdict whose journal line
says `verified` closes its gap after a restart. The verifier catches it, because it
recomputes independently, but the component that reports gaps does not.

Two. An effect is committed on a qualified acknowledgement. The host reads `ok` and
the action id and stops there, so the unsigned D' verdict, which the store replies to
with `state: unverified`, still logs `effect_committed`. That is in the shipped
example run now, which means one of my own rows was passing while contradicting
itself.

Three. An I/O failure has no answer. If the journal cannot be written, the store
raises inside the handler, prints a traceback, and closes the connection with no
reply, instead of saying it could not persist. The effect is still withheld at the
host, but by accident rather than by design.

All three are in the register with the commands that reproduce them, as open. I have
not fixed them yet: your report may describe the same three in a sharper form, and I
would rather fix once.

On the register's shape, this is what I would add to your proposal. Each row carries
the reproduction as a runnable command, the commit that closes it, and the regression
mode that fails without that commit, so the third column can be checked by running
the second. Rows that test something outside the stated threat model go to
`disputed` with the reasoning in the row, not deleted, so the disagreement stays
visible.

Author order and venue still wait for finalisation, as we agreed.

---

## For you, not for him

- The patch is delivered as two text attachments. Do not paste a repository link that carries the workspace name.
- If he pushes on severity, the line to hold is: the limitation was disclosed, the verdict line contradicted the disclosure. That is the defect, and it is fixable without a new external witness.
- The audit's own section 2 says 37/38 is not a reliability percentage. Do not restate it as one either way.
- Keep his review and your patch runs together. The exchange is now a review, a response and a patch, and that sequence is the thing worth showing anyone later.
