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

Behar, good, and here is what you need to reproduce it rather than take my numbers.

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

## 7. The message that answers the review, v1.2

Attachments: `DISPOSITION-2026-11-01.md` and `FINDINGS-REGISTER.md`, both as PDF, plus
`P2-DIFFERENTIAL-FIXES.patch.txt`. He does not need the zip; he can apply the patch to
`df0cf5a` and re-run his own package.

---

Behar, I have your package. Your declared sha256 is
`b2a39986c4ad238446e9d2a4928e58a35cba2ff7ceed8fda3e357ac14db90ed4` and the file that arrived
measures the same, so we are looking at the same bytes.

I ran `v2tests.py` and `v3fixes.py` unchanged, with `HFB_REPO` pointed at `df0cf5a`, before
writing a line of the patch. Your results file marks 23 of the 36 outcomes as defects; mine
came out the same 23, case for case, so the disagreement between us was never about what the
code does. On the 13 input checks I got N06, N12 and N13, and N11 is untestable here for the
same reason it was for you, `chattr +i` refused.

The three I sent you on the 9:05 message are V05, V17 and V19 in your numbering. That is
useful to know and it also means my reading of the code agreed with yours on the cases I
managed to reach, which is the first honest thing I can say about this exchange.

P2 is on top of `df0cf5a`. Against it, your package reports 9 defects and 22 outcomes behaving
as documented, and the defects that remain are the ones you said would remain. My own run,
`run.py` then `verify.py`, still reports 13 of 13 in class P and 3 of 3 in class V, two runs
still compare byte for byte, and `challenge.py` still catches every mutation it names. A fix
that quieted your cases by making the suite easier to pass would show up in those three, and
it does not.

What changed, in your terms. F-01: replay recomputes state from the record's bytes and from
the id the record is filed under, through one function that the store, the verifier and the
host all import, so a journal row's opinion of itself is not evidence and a record signed for
one action cannot resolve another. F-02: check D now refuses to report a verdict verified while
the same journal lists its action as a gap, so the verifier cannot contradict itself. F-03: the
host treats `ok: true` as permission to continue, not as acknowledgement, and requires
`stored: true` and `state: "verified"`; `D'` now withholds the effect, which changed the shipped
example run and the note says so. F-04: a failed append cuts the file back to its previous
length and the store answers that it could not persist, and a damaged tail is quarantined
before the next append rather than being written onto. F-05: B binds to the epoch the verdict
landed in, not the last boot in the file. F-09: `verify.py run run` is refused, `challenge.py`
writes nothing into the directory it was pointed at, and it ends by fingerprinting that
directory and printing that it is unchanged.

I dispute V04. In that run the replay step and the decision step are both 2, so your mutation
writes the value `decision_ts` already held and the re-signed record is byte-identical to the
WAL, signature included. I have printed that (`record_identical_to_wal=True`) and the same
mutation with the clocks five steps apart, which is caught: B fails and B.wal fails. If you
think the re-stamp is meant to move the value, the case needs a clock that does not collide,
and then I would like to see it fail against P2 before I believe the check is weak.

N13 is the one place my patch removes the thing your check reads. `challenge.py` no longer
leaves a report in the evidence directory, because that report was written by verifying the
run under test, and a failing report sitting in evidence is exactly the confusion the check was
about. Your N13 now raises on a missing file. The replacement property, that the directory is
byte-identical afterwards, is asserted in the tool and printed on every run. Rewrite it that
way and I will take the result.

Still open, and not fixed in P2: F-06 and V24, where nothing authenticates that the host died
and I have no independent kill receipt, so the survivability claim is narrowed rather than
defended; F-07 and V28 to V33, where nothing signs the sequence and a deletion inside framed
records still verifies; V22, where the failpoint still tests refusal and only your damage tests
tearing; and V36, the idle connection.

I take your release decision as written. Nothing in P2 supports a general authenticated
recovery claim, and I am not asking you to move on that. What I would like from you is the
re-run of your own package against P2, V04 either sharpened or withdrawn, and N13 rewritten.
Author order and venue still wait for finalisation.

---

## 8. Send this now, as a correction to the 9:45 message

The 9:45 message said the report had not been read. It has been read and the cases have been
run, so the follow-up has to say so plainly and carry the numbers. Paste this as a message,
then send the two PDFs and the patch in a second message, because LinkedIn drops attachments
from a message this long.

---

Behar, a correction to what I sent at 9:45. The package reached me through the Drive link and
its hash matches the one in your review, so the report is read and the cases are run, not
pending delivery.

I ran `v2tests.py` and `v3fixes.py` unchanged against `df0cf5a` before touching anything. Your
results file marks 23 of the 36 outcomes as defects and I reproduced the same 23, case for
case. On the 13 input checks I got N06, N12 and N13, with N11 untestable here for the same
reason it was untestable for you.

The three defects I described at 9:05 are V05, V17 and V19 in your numbering. Your first, third
and fourth areas.

P2 sits on top of `df0cf5a`: a patch, a disposition covering all 49 cases, and the register. Run
against P2, your package reports 9 defects and 22 outcomes behaving as documented, and the
defects that remain are the ones you said would remain. Each of the six findings I answered has
a mode in `audit/regressions.py` that fires your counterexample and requires a named check to
catch it, nineteen modes in all, every one caught. The mode for the false rejection tests both
directions, since a check that fires on an ordinary restart would be as wrong as the one it
replaced. My own run still gives 13 of 13 in class P and 3 of 3 in class V, two runs byte for
byte, and every challenge mutation caught, so the patch did not quiet the suite into passing.

V04 I dispute rather than patch around. In that run the replay step and the decision step are
both 2, so your mutation writes the value `decision_ts` already held, and the re-signed record
is byte identical to the WAL. With the clocks five steps apart it is caught by both B and
B.wal. N13 needs a rewrite from you for a similar reason: the report it opens is one my fix
deliberately stopped writing, and the property is now asserted inside the tool and printed on
every run.

I take your release decision as written. Nothing in P2 supports a general authenticated
recovery claim, and I am not asking you to move on that. Author order and venue still wait for
finalisation.

---

## 9. The link he asked for, and where it should live

LinkedIn turned `FINDINGS-REGISTER.md` into a web address because the filename looks like a
domain and the dot is what it keys on. Two things follow: send the URL on its own line with
nothing after it, and put the file where a URL for it is short and stable.

The right home is the benchmark repository, in `audit/`, next to the modes the register cites.
Do not send him into `linkedin_emphire`: it is public, it carries the CV, the pipeline and the
offer material, and a reviewer following a link into that would see all of it.

---

Behar, that is the filename being read as a domain rather than a file. Here is the register
where it belongs, in the repository the code is in:

https://github.com/Teamthy/host-failure-benchmark/blob/main/audit/FINDINGS-REGISTER.md

The same directory holds `DISPOSITION-2026-11-01.md`, the case by case table for all 49 of your
checks. Both are against `006d7ee` on `main`, which is P2, so every row can be checked out
rather than taken from a patch.

Your run came out where mine did: 13 of 13 in class P, 3 of 3 in class V, all ten challenge
mutations caught with the three input checks held, and all nineteen modes caught. Class V is
three now because `D'.effect` is new: an effect committed on a record the store could not
resolve used to pass, and that was one of yours.

---

## 10. The full reply to send now

Nothing earlier has reached him except the 9:45 message, so this one carries the whole answer:
the correction, the numbers, the six findings, the dispute and the link. Codes and commits are
written without backticks, because LinkedIn does not render them and the dot in a filename is
what turned the last one into an address. Both URLs go on their own line.

---

Behar, that one is on me twice. The filename became a link because of the dot, and the message
that mentioned it said the report was unread when it had already arrived. Correcting both here,
and nothing before this should be read as an assessment.

Your package came through the Drive link. Its sha256 is b2a39986c4ad238446e9d2a4928e58a35cba2ff7ceed8fda3e357ac14db90ed4, the same as the one in your review, so the file is the file.

I ran v2tests.py and v3fixes.py unchanged against df0cf5a before changing anything. Your
results file marks 23 of the 36 outcomes as defects and I reproduced the same 23, case for case,
so we were never arguing about what the code does. On the 13 input checks I got N06, N12 and
N13. N11 is untestable here for the same reason it was for you.

The three I described earlier are V05, V17 and V19 in your numbering.

P2 is on df0cf5a and is now commit 006d7ee on main. Against it your package reports 9 defects
and 22 outcomes behaving as documented. The nine are the ones you said would remain: V23 and
V24 on host loss, V28 to V33 on completeness, V22 on the failpoint, and V04, which I dispute.
My own run still gives 13 of 13 in class P and 3 of 3 in class V, two runs byte for byte, every
challenge mutation caught, and nineteen regression modes each caught, on Windows as well as
here.

What that covers: replay recomputes a record's state from its bytes and from the action id it is
filed under; check D refuses to report a verdict verified while the same journal lists it as a
gap; the host requires stored and verified in the reply before it ships; a failed append rolls
the file back and the store answers that it could not persist; B binds to the epoch the verdict
landed in rather than the last boot in the file.

V04 I would rather argue than patch around. In that run the replay step and the decision step
are both 2, so your mutation writes the value decision_ts already held, and the re-signed record
is byte identical to the WAL, signature included. With the clocks five steps apart it is caught
by B and by B.wal. If the re-stamp was meant to move the value, the case needs a clock that does
not collide, and I will take the result when it does.

N13 is the one place my fix removes what your check reads: the report it opens is one
challenge.py stopped writing into the evidence directory. The replacement property, that the
directory is byte identical afterwards, is asserted inside the tool on every run.

Nothing in P2 supports authenticated recovery, host-loss survivability or trusted timestamps,
and I am not asking you to move on your release decision.

The register:

https://github.com/Teamthy/host-failure-benchmark/blob/main/audit/FINDINGS-REGISTER.md

The case by case table for all 49 of your checks:

https://github.com/Teamthy/host-failure-benchmark/blob/main/audit/DISPOSITION-2026-11-01.md

What I would like from you is a re-run of your package against 006d7ee, V04 sharpened or
withdrawn, and N13 rewritten. Author order and venue still wait for finalisation.

---

## 11. Asking him for work, and why not in this thread

He is an independent reviewer with an open verdict on the work. The loop is not closed: he still
owes a re-run against 006d7ee, a decision on V04 and a rewritten N13. A request for paid work
inside that thread changes what his review looks like, whatever he answers, and it gives anyone
reading it later a reason to discount the assessment that currently makes the whole artifact worth
something.

Two things to keep apart:

- The review stays unpaid and unsponsored. If a commercial relationship ever starts, it goes in
  the same sentence as any published assessment of this work, either way round.
- The ask, when it comes, is about his organisation and his projects, not about whether he
  personally has money for a stranger. "Do you have funded work where this is useful" and "can I
  have a stipend" are the same request with very different framing, and only the first is
  answerable by a working engineer.

When to send it: after he has run the package against 006d7ee and the register has survived the
re-run, and after V04 and N13 are settled. Then it is a separate message, short, and it opens by
saying the review is not what it is about.

Draft, to hold until then:

---

Behar, this is separate from the review, and I am not asking you to soften a line of it. The
review stands on its own whatever your answer here.

If your group has funded work where this kind of test rig is useful, meaning durability of
records under process failure, evidence that a decision survived, verification of side effects
against what was actually stored, I would like to be considered for it, as a contract or as a
collaborator. I am not asking you to fund anything or to create a role. If the honest answer is
that there is nothing, that is useful to know and changes nothing about the review, and I will
keep sending you the register either way.

---

If he says yes, three things get agreed in writing before any code changes hands: the scope and
what counts as done, who owns the output, and how the commercial relationship is disclosed in
anything either of us publishes about this benchmark. The last one is not a formality. It is the
thing that keeps the earlier review credible.

If he says no, the better ask is a referral: which two or three people in his network make the
kind of claim this benchmark tests. A reviewer who has just spent a week in your work knows
exactly who needs it.

## 12. His reply of 10:53 PM, and the answer to send

He wrote at 10:53 PM. What his message actually settles, read carefully:

- **V04 is conceded in principle.** "V04 needs a genuine timestamp divergence to test the intended
  property" is his own phrasing of the defect in the check, not in the code. The disputed line in
  the register is now his position as well as mine, and it needs a different test rather than a
  different verdict.
- **N13 is conceded.** "N13 should be updated to reflect the revised evidence-preservation
  mechanism" moves the argument from whether the property holds to how the check should be written.
- **Nothing else is settled.** He has not ruled on V23, V24 or V28 to V33, and he has not accepted
  any disposition. He is going to read the register and rerun against 006d7ee first.
- **He has not asked for anything.** No document, no call, no introduction. The temptation here is
  to fill the silence. Do not.

That leaves eight cases open by my count: V23, V24 and V28 through V33. V04 comes off the list as
settled, with the test to be re-specified rather than the finding withdrawn.

**The reply. Send as is.**

Hi Behar,

Thank you, and I agree with both of your rulings.

On V04, the entry stands on the ground you name. The mutation writes the value the field already
holds, so the property it is meant to test never gets exercised. If it is useful for the rerun, I
can supply a variant with an injected clock skew and a real divergence between the two steps,
marked as synthetic so nobody later mistakes it for a case that occurred naturally. Tell me if you
want it and it goes in with the next push.

On N13, the entry will be rewritten to test the evidence-preservation path as it is now
implemented, rather than the file the earlier version left in the directory. I will send you the
replacement wording before it goes into the register, so your copy and the upstream copy cannot
drift apart.

Until your rerun lands I am not changing anything. 006d7ee is the right target, the audit files are
at 20e3ebf, and the cases still open are V23, V24 and V28 to V33. When your results arrive I will
fold them into a single reconciliation against the register rather than answering case by case, so
the record stays readable.

Best regards,
Olusanya

Why this and not more. It accepts both rulings in one line each, offers him the one artefact that
would make his V04 rerun meaningful without asking him to design it, and commits to a single
consolidated response so he is not answering messages while he works. It also ends without a
question, which leaves him free to go and do the rerun.

**What not to send.** No mention of the stipend, the funded work or referrals, which stay in
section 11 and stay held until after this review closes. No further defence of V04 beyond the
sentence he has already accepted. No summary of the patch, which he has. No deadline.

### 12.1 The register wording, held until his rerun confirms

Not applied. Send it to him only if he asks who writes the entries, and do not push it upstream
until his results are in, since a register that moves under a reviewer is worse than one that is a
week late.

**V04, replacement for the current line. Tested, not proposed.**

> V04 | Replay re-stamps decision_ts with its own clock step and re-signs. In the natural fixture
> the mutation is inert: the replay step and the decision step are both 2, so it writes back the
> value the field already held and re-signing produces identical bytes
> (evidence/2026-11-01/v04-inert-proof.log, `record_identical_to_wal=True`). The property is tested
> by the synthetic variant V04-SKEW in `audit/v04_synthetic_skew.py`
> (evidence/2026-11-01/v04-synthetic-skew.log). Five replay steps are injected before the re-stamp,
> so the two timestamps differ (wal_ts 2, stored_ts 7), the record is not the WAL record, and both
> B and B.wal fail with exit 1. The control run with no skew reproduces the inert case and every
> check holds, which shows the difference comes from the divergence and not from a change in the
> checker. The variant is labelled synthetic and tests the binding property only; it does not
> attest independent timestamp provenance, which this design does not provide.

**N13, replacement for the current line. Verified, and the verification corrected my own wording.**

> N13 | The earlier check required challenge.py to leave a passing report in the directory it was
> pointed at. That behaviour was removed. challenge.py now copies what it needs, verifies against
> the copies and writes nothing into the evidence directory, and among its held assertions it
> prints "the run you pointed me at is unchanged, no file added, removed or rewritten"
> (column spacing normalised in this quote). Its
> closing line is the summary that every mutation was caught, not the fingerprint line, which is
> the detail I had wrong in my first draft of this entry. The check therefore raises on the absent
> file rather than testing the property. Under the current implementation the property is asserted
> by the tool on every run (evidence/2026-11-01/n13-preservation-check.log: exit 0, eighteen files
> before and after, no verify-report.json, directory fingerprint unchanged). A rewritten N13 should
> confirm the absence of new files and that assertion line, not the presence of a report.

## 13. His message of 11:08 PM, and the answer that carries the work

He accepted the synthetic skew, asked for preconditions, expected results and a reproducible
assertion that the two values differ, asked to verify the N13 wording before it enters the shared
register, fixed 006d7ee as the evaluation target, and thanked me for consolidating. That is a
green light on the two things he asked for in the previous message, so this one is a delivery
message rather than an argument.

What was built, in the tree, so he can run it:

- `audit/v04_synthetic_skew.py` applies his mutation to the replay path only, injects five
  synthetic steps before the re-stamp, and runs the control and the variant in the same
  invocation. Result: control wal_ts 2, stored_ts 2, every check holds, exit 0; variant wal_ts 2,
  stored_ts 7, B and B.wal fail, exit 1. Every assertion is printed by the script.
- `audit/n13_preservation_check.py` points challenge.py at a completed run and checks the
  fingerprint before and after. Result: exit 0, eighteen files before and after, no
  verify-report.json, fingerprint unchanged.
- Logs: `evidence/2026-11-01/v04-synthetic-skew.log` and
  `evidence/2026-11-01/n13-preservation-check.log`.

What the verification changed: challenge.py does not close on the fingerprint line, as my first
draft of the N13 wording claimed. It prints "the run you pointed me at is unchanged,
no file added, removed or rewritten" among its held assertions and closes on the summary. Being corrected
by my own tool before he reads it is better than being corrected by him afterwards, and the reply
says so rather than quietly fixing it.

**The reply. Send as is.**

Hi Behar,

Both are done, and both are reproducible on your side.

V04. I built the variant as a separate, labelled test rather than bending the natural fixture.
audit/v04_synthetic_skew.py applies your mutation to the replay path only, injects five synthetic
steps before the re-stamp, and asserts three things: the two timestamps differ, the record is not
the WAL record, and B and B.wal both fail with exit 1. The control run with no skew reproduces the
inert case and every check holds, which shows the difference comes from the divergence and not
from a change in the checker. Observed numbers are wal_ts 2 and stored_ts 7 in the variant, both 2
in the control. The preconditions, the expected results and the assertions are printed by the
script itself, so you are not relying on my summary, and the log is
evidence/2026-11-01/v04-synthetic-skew.log. The variant is marked synthetic everywhere and claims
the binding property only. It does not attest independent timestamp provenance, and I would rather
say that plainly than let it read as though it does.

N13. I verified the replacement wording against the current implementation before sending it, and
the verification corrected one detail in my own draft. challenge.py does not close on the
fingerprint line. It prints "the run you pointed me at is unchanged, no file added, removed
or rewritten" among its held assertions, and closes on the summary that every mutation was caught.
The check itself: exit 0, eighteen files before and after, no verify-report.json, directory
fingerprint unchanged. audit/n13_preservation_check.py reproduces this and the log is
evidence/2026-11-01/n13-preservation-check.log. A rewritten N13 should confirm the absence of new
files and that assertion line, not the presence of a report.

The shared register is untouched. Both replacement entries are ready, and I will send them once
you have seen this, so your copy and the upstream copy move together.

006d7ee stays fixed on my side until your rerun is in. If it turns anything up that disagrees with
what I have written, tell me and I will correct it in the register rather than in a message.

Best regards,
Olusanya

**What not to add.** No apology for the earlier N13 sentence, since the correction is in the
message and an apology would make a small thing large. No explanation of how the script works
internally. No second offer of work, and nothing from section 11. No question at the end, because
the next move is his rerun.

## 14. His message of 11:15 PM: attribution

A reasonable and easy request, and one worth getting exactly right because it lands in a permanent
record. He asks for three things: his full name in the reviewer attribution and in the relevant
headings, "the reviewer" retained where it reads naturally, and his role described as a research
collaborator conducting independent technical verification rather than an unrelated external
reviewer. He explicitly does not ask for any change to the technical findings.

What was done, in both documents:

- An **Attribution** section at the top of each. Reviewer and author are named and separated. The
  findings are his; the fixes, the verdicts and the reasoning behind a dispute are mine. His
  contribution is stated as verification and adversarial testing and expressly not an endorsement
  of the benchmark, which matters later, when someone reads the register as a review that passed.
- Headings now name him: "Findings raised by Behar Dalipi, as F-numbered in his review", "the one
  case the reviewer's test rig can no longer run", "threat-model notes, in the reviewer's terms".
- Table columns that said "his case" and "his outcome" now read "the reviewer's case" and "the
  reviewer's outcome", which keeps the columns readable and the name in the prose where it belongs.
- The state of his rerun is recorded in both documents: in progress at the time of writing, and no
  result from it reported. That sentence is there so the record cannot later be read as claiming a
  clean independent pass.
- Provenance of the section itself is noted, so a future reader knows why the attribution changed
  between versions.

**One edit outside attribution, disclosed rather than slipped in.** The N13 note said challenge.py
"ends by fingerprinting the evidence directory and printing that it is unchanged". It does not end
there, as the 11:08 message said after running it. The note now reads that it writes nothing into
the directory and prints the unchanged line among its held assertions. That is a correction to a
description of my own tool, not a change to a finding, and he should hear it from me rather than
find it in a diff.

**Nothing technical moved.** Every status is as it was, V04 remains disputed on the record, V23, V24
and V28 to V33 are untouched, and the replacement N13 entry stays held until his rerun lands.

**The reply. Send as is.**

Hi Behar,

Agreed on all three, and it is a better record for it.

Both documents now carry an Attribution section: you as research collaborator conducting the
independent technical verification, failure-model analysis and adversarial testing, and me as author
of the implementation and the remediation, which includes every fix and every verdict recorded
there. The headings that were carrying "his" now name you, the tables read "the reviewer's case" and
"the reviewer's outcome", and "the reviewer" stays where it reads naturally. I also recorded that
your contribution is verification and adversarial testing and is not an endorsement of the
benchmark, because a register can be misread later as a review that passed, and I would rather the
document say plainly that it is not that.

Both documents also state that your independent rerun against 006d7ee was in progress and that no
result from it is reported. That keeps the record honest about what is established and what is still
being checked.

One edit outside attribution, which I would rather flag than let you find in a diff. The N13 note
described challenge.py as ending on the fingerprint line. It does not, as I said in my last message.
The wording now matches what the tool actually prints. No finding changed.

No status moved. V04 remains disputed on the record until you tell me the synthetic variant settles
it, the eight remaining cases are untouched, and the replacement N13 entry is still held.

If you would rather review the two files before they go into the shared register, say so and I will
send them as they now stand.

Best regards,
Olusanya

**Why disclose the N13 edit.** He is asking for precision in a permanent record. Correcting a
sentence and not mentioning it is the one thing that would undermine the reason he asked.

## 15. His message of 11:18 PM: send the two replacement entries

He accepts the synthetic skew as methodologically appropriate, because it separates timestamp
consistency from independent attestation, accepts the revised N13 as addressing the property more
directly, and asks for the two replacement entries so he can review the wording against the evidence
before the shared register is synchronised. That is a delivery message, and the entries are the
content. Two decisions inside it are mine to propose and his to settle.

**The status word for V04.** Under this register's own rule a row is closed only when a mode in
`audit/regressions.py` fails without the fix. There is no fix to fail without here: the binding
already held, and what V04 identified was a defect in the test rather than in the code. So "closed"
would be the wrong word, and "disputed" is now wrong too, since he has accepted the reasoning. The
honest word is **scope**: nothing to patch, the claim is narrowed, and the narrowing is written in
the row with the variant named. I propose that and offer the alternative, because it is his finding
and he may prefer the row to read as settled in a stronger sense. If he does, the variant becomes a
mode in the regression file and the row moves under the existing rule.

**The N13 status stays as it is.** "Fixed, the reviewer's check needs updating" is accurate and
becomes testable once his check is rewritten, so the entry's wording carries the instruction rather
than the disposition changing.

**The message. Send as is.**

Hi Behar,

Here are both entries, with the evidence each one cites so you can check the wording against the
numbers rather than against my summary.

V04, proposed for the disputed table:

> V04 | Replay re-stamps decision_ts with its own clock step and re-signs (old T09). The mutation is
> inert in the natural fixture: the replay step and the decision step are both 2, so the write puts
> back the value the field already held and re-signing produces identical bytes
> (evidence/2026-11-01/v04-inert-proof.log, record_identical_to_wal=True). The property is tested by
> a synthetic variant with a genuine divergence, V04-SKEW in audit/v04_synthetic_skew.py. Five
> replay steps are injected before the re-stamp: wal_ts 2, stored_ts 7, the stored record is not the
> WAL record, and B and B.wal both fail with exit 1. The control run with no skew reproduces the
> inert case, every check holds and verify exits 0, so the difference comes from the divergence and
> not from a change in the checker (evidence/2026-11-01/v04-synthetic-skew.log). Scope: a record
> whose timestamp changed between the decision and the ship must not be accepted. Independent
> timestamp provenance is not claimed and this design does not provide it.

N13, proposed for the input-check table:

> N13 | The original check required challenge.py to leave a passing verify-report.json in the
> directory it was pointed at. That behaviour was removed. challenge.py now copies what it needs,
> verifies against the copies, writes nothing into the evidence directory, and prints among its held
> assertions that the run it was pointed at is unchanged, no file added, removed or rewritten; its
> closing line is the summary that every mutation was caught. The check therefore raises on the
> absent file rather than testing the property. Under the current implementation the property is
> asserted on every run: exit 0, eighteen files before and after, no verify-report.json, directory
> fingerprint unchanged (evidence/2026-11-01/n13-preservation-check.log, reproduced by
> audit/n13_preservation_check.py). A rewritten N13 should confirm the absence of new files and that
> assertion line, not the presence of a report.

One question on V04's status word, and it is yours to settle. Under the register's rule a row closes
only when a mode fails without the fix. There is no fix here to fail without, because the binding
already held and what V04 found was a defect in the test rather than in the code. So "closed" would
overstate it and "disputed" now understates it. I have written "scope", meaning nothing to patch and
the claim narrowed with the variant named. If you would rather the row read as settled, say so and I
will add the variant as a mode in audit/regressions.py so it moves under the existing rule.

N13's status I have left alone, because "fixed, the reviewer's check needs updating" is accurate
until your check is rewritten.

Nothing in the shared register has moved. These two entries go in together, with your agreement, in
one commit, so your copy and the upstream copy stay identical.

Best regards,
Olusanya

**What not to do.** Do not send the entries as an attachment, which turns a two minute read into a
download. Do not pre-empt his choice on the status word by picking one and defending it. And do not
add a fourth document describing the two entries, since the entries are the document.

## 16. His message of 11:31 PM: attribution accepted, and the one thing still open

A close. He accepts the attribution as the foundation of the shared record, accepts that verification
is not endorsement, notes the N13 correction and the decision to leave dispositions unchanged, and
says he looks forward to completing the P2 reconciliation on that basis. No question, no request,
nothing to correct.

Note what this message does not do. It does not acknowledge the two replacement entries he asked for
at 11:18. Either they were sent after it and he has not read them yet, or they have not gone. Check
before replying: if they have not been sent, section 15 is the message that is owed, and this close
does not replace it.

**If the entries have gone, send this and nothing more.**

Thank you, Behar. The two replacement entries are ready for when you sit down with the reconciliation,
and nothing in the register moves until you have read them. No hurry from my side.

**Why so little.** He is closing a long evening's exchange. The relationship is now in the state it
needs to be in, which is a reviewer who trusts the record and a record that has not moved under him.
Anything longer reopens a conversation he has just finished, and anything with a question in it
gives him work at midnight for no reason.

**What is actually left, in order.**

1. His independent rerun against `006d7ee`, which is his to do and cannot be hurried.
2. His read of the two replacement entries, and his word on how V04 should be recorded: scope as
   proposed, or a regression mode so the row closes.
3. The register commit, both entries together, only after (1) and (2).
4. Section 11 stays parked until the review closes. Nothing about work or money has been raised in
   twenty minutes of warm exchange, which is the reason the review is still worth something.

## For you, not for him

- The patch is delivered as two text attachments. Do not paste a repository link that carries the workspace name.
- If he pushes on severity, the line to hold is: the limitation was disclosed, the verdict line contradicted the disclosure. That is the defect, and it is fixable without a new external witness.
- The audit's own section 2 says 37/38 is not a reliability percentage. Do not restate it as one either way.
- Keep his review and your patch runs together. The exchange is now a review, a response and a patch, and that sequence is the thing worth showing anyone later.
