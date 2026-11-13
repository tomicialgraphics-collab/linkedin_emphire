---
deliverable: post
id: 2026-11-13_exit-zero-never-checked
date: 2026-11-13
audience: public
status: ready
approved: no
template: T1
headline: The verifier printed NOT TESTED and exited 0.
subheadline: Three states, two codes, and the one that could not be demonstrated inherited the same exit as success.
headline_alt: A check that could not run reported that everything was fine.
subheadline_alt: The tool's own test suite required that behaviour, which makes it a contract and not a bug.
headline_alt2: Two codes for three states is how a verifier lies by accident.
subheadline_alt2: NOT TESTED is not PASS, but both of them were 0.
box: EXIT ZERO
box_alt: THE INTERFACE
hashtags: [#AISecurity, #AIEvaluation, #AIRedTeam, #AIGovernance]
slot: 09:00 WAT, Saturday 14 November 2026
first_comment: FIRST_COMMENT.md, playbook link only
visual_link: https://drive.google.com/file/d/1qRxHwUOxG8UCPZGDau1RlIX2faSWQuYs/view
carousel_link: https://drive.google.com/file/d/1XjjzuwsA2wNXxtjiH-exGlxt3xi28nIo/view
---

# Post 34: the exit code that reports success for a check that never ran

Slot **09:00 WAT, Saturday 14 November 2026**. Written on the evening of Friday 13 November, when the question of
publishing tonight came up: the Nvidia post took 09:00 that morning, so tonight would be twelve hours behind it and the
second of two posts inside a day is the one that dies. The text is ready to paste tonight if the Nvidia post did not go
out, and the slot above is the recommendation if it did.

The subject is a review finding from this week's external read of a public signature verifier: the tool exits 0 when it
never checked the signature, and two of its own test cases assert that it should. Nothing in the post names the tool, the
author or the repository, and none of the counts come from a private document.

## Verification: what is established here

- **Established by running it.** With no trust store configured against a tampered attestation, the verifier prints NOT
  TESTED for the signature and for trust, reaches no level, and exits 0. With its strict flag it exits 2 and names the
  guarantees it could not demonstrate.
- **Established by reading the suite.** Two cases in that tool's own test file assert exit 0 for a pillar left NOT
  TESTED. This is a requirement the author wrote, not an accident.
- **Established by writing the patch.** Failing closed on the parts of the verdict that decide the level moves nothing
  else: the verdict lines, the levels and the JSON schema are unchanged, and the tool's suite still passes after the two
  assertions are updated.
- **Not claimed.** Nothing here is asserted about that tool's users, its accuracy on valid attestations, or its Rust
  verifier, which was not built. No figure in the post comes from a source outside that run.

## Rules this was built against

- Template T1, technical, proof of work with the finding in the open.
- First line under 120 characters, a statement, and identical to the declared headline.
- Headline plus subheadline inside 200 characters.
- Exactly one boxed phrase, two words, not opening line one.
- Four tags from the verified registry on the final line.
- No em dashes, no bold, no invented number, no relative date, no client named.
- Human gate 90 or above with zero errors.

## Recommended headline pair

**HEADLINE:** The verifier printed NOT TESTED and exited 0.

**SUBHEADLINE:** Three states, two codes, and the one that could not be demonstrated inherited the same exit as success.

45 characters and 105 characters, 150 together.

## Card copy

```
HEADLINE   THE VERIFIER PRINTED NOT
           TESTED AND EXITED 0.    [EXIT ZERO]

SUB        THREE STATES, TWO CODES,
           AND SUCCESS WAS THE DEFAULT
           FOR THE ONE IT SKIPPED.
```

## Post, paste-ready

<!-- gate:body:start -->
The verifier printed NOT TESTED and exited 0.
Three states, two codes, and the one that could not be demonstrated inherited the same exit as success.

Here is the mechanic. A signature check has three outcomes: passed, failed, and not tested. Two of those map cleanly onto
0 and 1. Not tested is the one with no code of its own, so it inherits 0, and every automated caller downstream reads 0
as fine.

I ran one of these tools against a tampered file with no trust store configured. No key, no verification, no level
reached. It printed NOT TESTED twice, then 5 PASS, 0 FAIL, 6 NOT TESTED, then exit 0. Add one flag and it exits 2 and
names the three guarantees it could not demonstrate. So the correct behaviour existed the whole time, one flag from the
place where a pipeline meets the tool.

Then the part worth writing about. Two of that tool's own test cases assert exit 0 for exactly this state, with names
attached. That suite is not missing the point, it is defending it. Which means this was never a bug report. It is a
disagreement about what a word means, and it has a smaller blast radius than a bug because the fix is a decision rather
than a repair.

My patch is deliberately small. Fail closed on the parts that decide whether a level was reached, and leave the hardening
lines alone. A check that fails on every unproven detail is always red, and a check that is always red is a check people
switch off, which returns you to the original problem with extra steps.

Worth doing in your own stack. Find every check that can return "unknown", look at its exit code, and ask whether anyone
downstream can tell the difference between that and a pass. Most of the ones I open cannot.

#AISecurity #AIEvaluation #AIRedTeam #AIGovernance
<!-- gate:body:end -->
