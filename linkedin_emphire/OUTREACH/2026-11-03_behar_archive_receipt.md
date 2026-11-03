# Behar, 3:23 PM: archive digest and reproduction guide

He confirms he has verified the original supplemental archive, has built the S1 to S5 reproduction guide
with commands, fixtures, expected observations and environment-dependent limits, and asks for an email
address because LinkedIn will not carry a zip.

**The digest he supplies:** `e34c35c8a9269dddfd0ec9452b5a3b3e5894246362ce031c36be3d5b26b33f98`

Recorded, not confirmed. Nothing in the local tree matches it, because the file has not arrived. It
becomes a verified digest only when received bytes hash to it. Do not cite it as verified before then.

## The reply, 291 words, lint clean

Behar,

Digest recorded: e34c35c8a9269dddfd0ec9452b5a3b3e5894246362ce031c36be3d5b26b33f98.

I will hash the received bytes before opening anything and report what I get, so the number in this
thread and the number I compute are checked against each other. If they differ, we compare files rather
than opinions.

On delivery, one route is better than email: attach the archive to a commit or a release asset in your own
repository and send the URL. Then the bytes a reader fetches are the bytes the digest describes, and a
third party can check that without asking either of us. A link whose contents are pinned by a digest is
the one version of a link that stops moving.

If you would rather not publish it, send it to olusanyatimothy54@gmail.com and I will confirm on receipt.
Reception only. The conversation stays here.

Before I run the guide: which environment does it assume, and which revision do the fixtures expect? I am
pinned to 006d7ee71aa6599521d6675c32f496c5427a846b. If your commands assume another revision, tell me
which, because I would rather reproduce your setup than a near copy of it.

I will report S1 to S5 as reproduced, not reproduced, or partial, each with the command and the observed
output rather than a verdict alone, and partial stays unreconciled in the register.

On closure: the reconciliation is two commits, 1780208 and 7598349, on main. The first carries the
corrected counts, the attributed register and disposition, and the eight evidence logs. The second removes
an internal file from the manifest, so it lists exactly twelve files, each hashing at 7598349. That is the
revision to review.

One request: send me the shape you want the results returned in and I will answer in that shape, so the
comparison is line by line.

Olusanya

## Why each part is there

- **The digest is repeated back verbatim.** It gives him a string to check his own copy against before he
  sends, and it puts the number in the thread twice, so there is no ambiguity about which file is under
  discussion.
- **Hash before opening.** The digest is the acceptance test for the file, not a formality attached to it.
- **A URL beats an email.** His own DOC-4 objection is that a link can be edited later. A link whose
  contents are pinned by a published digest is not that, and it lets him keep the archive private or
  public as he prefers. The email is offered second, as a fallback, and framed as reception only, which
  keeps the exchange on LinkedIn.
- **The environment question is asked before the run, not after.** Running his fixtures against an
  environment he did not assume produces a difference that proves nothing, and then we spend a week
  arguing about whose container was wrong.
- **The pin is stated.** `006d7ee` is the revision under review. If the guide assumes another, that has to
  surface before the results do.
- **No date is promised.** The commitment is the shape of the report and the honesty of the three states,
  not a deadline.
- **Closure is answered with the two commits and the manifest count.** This also restates the sha in
  context, after the 12:30 PM message that went out with the placeholder still in it.

## After sending

1. Hash the file before opening it. Record both the claimed and computed digests in the evidence folder.
2. Run S1 to S5 against `006d7ee` in the environment he names, one at a time, keeping stdout per run.
3. Report in his shape, using only reproduced, not reproduced, or partial. Update the register per row in
   the same commit.
4. Do not describe any of the five as accepted or rejected. Unreconciled until reproduced.
