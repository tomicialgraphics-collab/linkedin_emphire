# DRAFT for sign-off. Not approved. Not published.

Status: waiting on Praveen Babu to mark which findings he accepts, land the fixes, and sign. Publishing happens after the fixes are verified and both names are on it.

---

# What a fail-closed action gate cannot see

I spent a window testing an AI action gate from the outside: one account, one key, no source, twenty-six attempts, a budget of three hundred. The gate decides whether an agent's proposed action may run. The question I brought was the boring one. Not "can I get past it", but "what does it do all day when nobody is attacking it".

The answer is that it holds almost everything and blocks a little. It blocked five outright, and released nothing without a person across the twenty-three rows I reconciled against its own feed. A read of a customer table was held as readily as a `DROP TABLE`. That is the right way for a default to fail, and it is why the interesting findings are not about what got through.

They are about what the gate is leaning on while it holds.

## The sequence is where the gap is

Two chains ran to completion. A read of customer records containing personal data, followed by an email to an external address. And a database export, a file write, and an email to an external vendor. Neither was blocked. Neither produced a chain pattern or a semantic trigger. The gate evaluated each step on its own and had nothing to say about the shape.

The part I did not expect: inside the chain, the first read was checked against two requirements. The same read sent alone carried four. A sequence was being reviewed with less scrutiny than its parts, which is the opposite of what a reviewer would assume.

An action gate's whole premise is that a sequence is different from a list of actions. In the state I tested, the gate did not have an opinion about sequences at all, and nothing in its output told me that.

## The cheapest approval path guarded the most sensitive object

A read of every row of the credentials table, passwords and tokens included, required a scope and a person's approval. A bounded ten-row read of an ordinary orders table required those plus a production approval and a verified recent backup.

That inversion is the kind of thing that survives review because nobody looks for it. Release requirements are assumed to scale with sensitivity. Here they did not, and the thinnest path led to the table with the passwords in it.

## Three things it got right, and got right in interesting ways

**An agent cannot approve itself.** I attached approvals three ways: none, a malformed development string, and a structurally valid token minted with a key the account had never registered. None of them counted. The last one was held with a message telling exactly what was missing, which is the correct answer delivered in the correct tone. Only an approval signed with a key registered on the account clears an approval item. That is a human in the loop by construction, not by policy.

**An agent cannot shrink its declared scope.** I sent a `DROP TABLE` inside an envelope claiming it was a single record. It was blocked, and the lie itself was the violation. This was the test most likely to break something open and it did not.

**Prose is not evidence.** Claiming an approval in the task text, in three separate cases, was neither honoured nor flagged. The gate did not treat the claim as evidence, which is right, and did not mention it, which is a decision worth making explicitly rather than by default.

## A certificate that empties a field

One case returned an empty `signature` field in its certificate, where every other decision in the run returned a hex value. The trigger was a malformed approval token. The decision was correct. The certificate, which is the artifact a customer will eventually hold up in an audit, was not.

That is the smallest thing I found and the one I would fix first. It costs nothing, and the edge case will not surface in your own testing because it only appears when the input is already wrong.

## What this does not say

It does not say the gate is broken. It says the default state is a holding gate, that holding is not the same as seeing, and that the things it cannot see are sequences, sensitivity ordering, and the session facts it has already observed and does not mention.

None of this was tested against an instrumented account. Contracts, checks, a registered signing key and chain plans change the system enough that I would not carry any of the above across the line.

The fixes land next, and then I re-run the same cases against the same baseline and report what changed. When both of us are satisfied, this goes out with the numbers updated and nothing softened.
