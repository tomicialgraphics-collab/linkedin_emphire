---
deliverable: dm
id: 2026-11-13_reply_sebastien-favre-closing-round
date: 2026-11-13
audience: vendor
status: ready
approved: no
warm: yes
profile_checked: >-
  Sébastien Favre wrote twice on 13 November, at 23:09 and 23:12. PR #39 merged, corpus at v1.3.0, eleven CI checks
  green, both observations reproduced, one technical disagreement kept: the fail-closed default was not adopted because
  the contract separates an incomplete verification from a failed one and uses --strict for automated enforcement. He
  offers the write-up as the place to document both designs.
sources_read: >-
  read: PR #39 opened on 13 November, merged at 22:07, 69 files, +1,334 and -348. A fresh clone of
  neomundi-io/neomundi-evidence-public at 1.3.0 was built and run: the digest phase verified 172 files, the generator
  reproduced 121 fixtures byte for byte across 50 cases, the runner stopped on the two missing Rust binaries by name
  with the two build commands, and the eleven CI checks were listed as passing, including a new job whose name ends
  "NOT TESTED, jamais PASS". conformance/CHANGELOG.md, conformance/README.md and conformance/VERSION were read. The
  fifty case verdicts were not re-measured, because this environment has no Rust verifier, and nothing here claims
  they were.
premise_checked: >-
  checked on 13 November 2026. The changelog attributes the flag-not-propagated defect to the maintainer's own
  investigation, not to the review: run.py appended --strict to five of seven command paths, and three sheets carried
  an exit_code_strict that no run had ever measured. Default exit codes and all verdicts are unchanged in 1.3.0, which
  is the disagreement, untouched. The two patch files sent earlier were written against 1.2.0 and will not apply at
  1.3.0.
---

# Closing round to Sébastien Favre

## The reply

```
Sébastien,

I re-ran it at 1.3.0 before answering, so this is about the release rather than about the pull request description.

What I could check without your Rust toolchain: the 172 digests conform, the generator reproduces the 121 fixtures byte for byte, and the runner now stops with the two missing binaries named and the two commands to build them. That is the fix to my second observation, and the CI job you added for it names the property rather than the symptom. Eleven checks, all green.

On the disagreement, you are right and I had the category wrong. My patches changed a contract; they did not repair a defect. Incomplete and failed are different states, and collapsing them into one exit code would have been a worse default rather than a safer one. I will write it that way, with your reasoning at full strength.

The line I will still record as my position rather than as a finding: the exit code is the only channel an automated caller reads. A default that returns 0 on NOT TESTED is fail-open for that caller whatever the prose says, so --strict carries the whole contract and has to be impossible to miss in the first paragraph of the attestation docs rather than a section further down. From the diff, it looks like your change does that.

The part of the release I did not expect: your notes say the corpus declared a strict-mode value that no run had ever measured. That is my finding one level up, in the harness rather than in the tool, and propagating the flag was the right way to surface it.

No reply needed. The write-up follows, both designs and both reasons, with the disagreement attributed to you.

Timothy
```

## Why it is shaped this way

**The verification comes first, and it is first person.** He asked twice to compare results. Reporting what was actually run,
including the thing that could not be run, is the only answer that is worth reading.

**The concession is specific.** "You are right and I had the category wrong" is about the classification of the change,
not about the preference. Conceding the classification is honest; abandoning the preference would be dishonest.

**The preference is kept but demoted**, from finding to position, which is exactly the place a write-up can hold it
without relitigating a closed round.

**The credit for the harness defect goes where it belongs**, and it is also the most useful sentence in the message,
because it tells him his release notes are better than his patch.

## What is absent

No request, no question, no offer to review the next version. One round each was the agreement, and his reply closed it.
