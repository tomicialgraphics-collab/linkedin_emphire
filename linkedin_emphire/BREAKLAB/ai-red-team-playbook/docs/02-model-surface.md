# 02 The model surface

Covers `MB-01` to `MB-49`.

## Start with the instruction hierarchy

Before any injection result means anything, find out which text the system treats as instruction and which as data. Most systems have at least five channels that carry text:

1. The system prompt, written by the builder.
2. The developer or application message.
3. The user turn.
4. Retrieved content: documents, web pages, tickets, emails, files.
5. Tool output, which is usually written by something other than the user.

A sixth appears in agentic systems: messages from another agent or an MCP server.

Each needs three things stated: how it is delimited, what authority it carries, and what happens when it contains something that looks like an instruction. If those three are not declared, every result downstream is ambiguous, and a fix becomes guesswork.

The failure to look for is promotion. A summariser that concatenates retrieved text into the user turn has silently upgraded data to instruction, and no amount of prompt hardening fixes the architecture.

## Injection is a propagation question

The interesting test is not "will the model repeat this sentence". It is "does the sentence change what the system does next".

Work it as a path:

```
untrusted content  ->  model context  ->  decision  ->  tool call  ->  effect
```

At each arrow ask whether anything checks. In practice the checks that exist are input filters at the first arrow and nothing at the rest, which is why the finding is nearly always at the tool call.

Three variants worth naming:

- **Payload splitting.** The instruction is harmless in each document and complete across two.
- **Second-order injection.** The model writes text that a later process trusts: a ticket note, a commit message, a summary that becomes tomorrow's context.
- **Sanitiser ordering.** The filter runs before the encoding, so it inspects a string that is not the string the model receives.

## Language-level attacks

Keep the mechanism in mind and the catalogue becomes optional. The mechanisms are: change the surface form, change the language, change the length, change the encoding, change the shape of the output.

- Encoding: base64, ROT13, hex, leetspeak, emoji substitution.
- Character level: homoglyphs, zero-width characters, bidirectional overrides, unicode normalisation differences between the filter and the model.
- Language: a low-resource language often has weaker safety behaviour. Test three, not one.
- Length: many-shot prompts, very long contexts, and refusals that fail at turn forty.
- Shape: force the content through a structured output field and see whether the filter that inspects prose still sees it.

The mechanism framing matters because half the named attacks in circulation are the same three mechanisms wearing new names, and an adaptive attacker will invent a fourth.

## Sampling, brittleness and why one run means nothing

The same input produces different output. That is not a bug to be fixed, it is a property to be measured.

- Repeat one case ten times before quoting any single result.
- Paraphrase one request ten ways and record the spread in behaviour, not the average.
- Run at the deployed temperature. A finding at temperature zero may not exist in production, and the reverse is also true.

`tools/wilson.py` gives the interval for a small sample, which is the form most of these results take.

## The canary

Plant a unique string in the system prompt on day one, then search every output, log, trace and error message for it. It costs nothing, it detects the most valuable class of leak, and almost nobody does it. `MB-44`.

## What to write down

For the model surface, the artifact is one page:

- The five channels, ranked by authority, with the delimiter for each.
- The propagation path with the checks that exist at each arrow.
- The revision, prompt version and sampling settings in use.
- Where the canary is planted and where you searched for it.

That page is what a client can act on, and it is what makes the individual findings legible.
