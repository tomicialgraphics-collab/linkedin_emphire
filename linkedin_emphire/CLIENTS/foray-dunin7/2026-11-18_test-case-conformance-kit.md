---
deliverable: doc
id: 2026-11-18_foray-test-case-conformance-kit
date: 2026-11-18
audience: client
status: ready
approved: no
client: FORAY (Dunin7)
supersedes: >-
  The clinical trial case written earlier the same day stays valid as the product case, but this replaces it as the
  first co-build, because it serves his market entry rather than a market the owner would have to open alone.
premise: >-
  He asked for one test case and offered to review an interpretation. This is a smaller first build than the clinical
  product, it uses only what already exists, and it produces something an adopter can run without either of us.
premise_checked: >-
  checked: no claim is made about how many adopters exist or what they pay, because neither is known from this
  workspace. The one measured fact used is the review's own length, ten days, which is in his record and in the
  correction he raised himself.
sources_read: >-
  read: the register, the version 5 case study and the meeting record of 18 November. No external page opened.
---

# The first test case: a conformance kit for FORAY

## Why this one and not the product

An open protocol is adopted through one artefact: something an adopter can run against their own implementation to
find out whether it follows the specification. Without it, every new integrator needs a conversation with the
author, and the author is one person.

The review that just finished is evidence of the problem. It took ten days, one reviewer, and produced findings that
were correct. That is a good outcome and it does not scale past the second adopter.

## What gets built

1. **Checks.** Around thirty, each taken from a numbered rule in the specification, each stated as an observable
   outcome rather than an internal state. The register already contains the hard ones.
2. **A runner.** One command, standard library only, no network, pointed at a deployment. Pass or fail per check, with
   the rule it maps to printed beside the verdict.
3. **A negative control.** A deliberately broken implementation the kit must fail, so the kit proves it can fail, in
   public, every release.
4. **A report.** One page, the version of the kit and the version of the specification named at the top, and a line
   saying what the kit does not check. That last line is the part that makes it credible to an inspector.

## What it is not

Not a review of his implementation, not a conformance certification, and not a claim about security. The kit says
whether a deployment obeys stated rules. It cannot say whether the rules are sufficient, and it will say so.

## What it buys him

His first serious customer runs the kit before integration and the answer comes from the artefact rather than from
him. Every adopter after that costs him nothing to assess. And the kit is the one thing that makes an open protocol
verifiable by somebody who is not the author, which is the argument he made on the call about ten years and ten
minutes being the same question.

## What it buys the owner

A build with a public artefact, a named co-author, and a shape that recurs: every protocol that wants adopters needs
one. It also converts the register work into something that pays, without pricing the review again.

## Division of work, stated plainly

The specification and the rule numbering are his, because only he knows what each rule means. The checks, the runner,
the negative control and the report are the owner's. Both names on the published kit, and the kit is published under
the protocol rather than under either company.

## The four weeks

Two weeks for the first ten checks against the rules that carry the most weight, reviewed by him before anything else
is built. Two weeks for the runner, the control and the report. If the first ten checks find a rule that cannot be
stated as an observable outcome, that is the finding, and it goes back into the specification.
