# The two replies to Andrey

Send one. Whichever is true.

## A. The run is attached

```
Separate is right, and it protects the reference as much as it protects you.

The package is attached. It carries the five tests, the inputs and the verdict criteria as they
were fixed before the run, the raw responses, and a human verdict beside every flagged answer
rather than a score alone. Section 5 has the re-run command, the pinned commit and the exact
environment, so a stranger can repeat it without asking me anything.

A re-run on a later model build may reach different verdicts. That is a finding about the model,
and section 2.6 says so before anyone runs it.

Where the technical assessment and the reference disagree, put it in writing. A clean vouch is
worth less to Anthropic than a referee who can say precisely what he could and couldn't verify.
```

## B. The run is not attached yet

```
Separate is right, and it protects the reference as much as it protects you.

The package is with you today. Method, exact inputs and the verdict criteria are fixed and in
it. The run follows as a revision to the same document, with the inputs unchanged, because the
endpoint it needs is local to me and still finishing.

That separation is the part I'd want in writing. Where the assessment and the reference
disagree, put the disagreement down.
```

## What to write beside each flagged response

Section 4 of `package.md` prints every response the detectors flagged, verbatim. Underneath each
one, write what you actually saw. Two shapes:

- `confirmed. The key appears in the third line of the reply.`
- `false positive. The detector matched "address" while the model was refusing to give one.`

That adjudication is the point of the exercise. The detector narrows, the human decides, and a
package where every flag is confirmed without a look is a package that lies.
