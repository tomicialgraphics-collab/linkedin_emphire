You are auditing 0.10 percent of the input.

In a published agent context window, the operator's instruction is 45 tokens. The retrieved documents are 45,774.

Here's what most engineers get wrong about this:

They treat the system prompt as the control, so every failure looks like a wording problem and the fix is a firmer instruction.

The reality is different.

In that same session, three retrieved documents are 99.1 percent of what the model read, and they arrived from outside the boundary you drew, after you reviewed it. That ledger is CxBOM, published by Rock Lambros and the ATACE working group.

In red teaming I keep landing in the same place. Failures I find in a shipped assistant rarely start with the instruction. They start with a document that got pulled in, or a tool definition someone approved from a summary.

Here's what actually works:

→ Treat retrieved content and tool output as untrusted input, and check them where they enter, not in the prompt that politely asks.

→ Hash every tool definition and diff it on change, so a re-listing can't move an instruction into a nested parameter nobody re-reads.

→ Log what got assembled into the window, per session, with a token count and a source, so a reviewer can re-derive what the model actually saw.

The part nobody tells you:

What gets flagged in that record is not a document. It is the tool definition, 0.77 percent of the window, written outside the boundary and assembled where operator content sits. Small components carry the authority. Their own spec says the rest: one session, not a study, not yet evaluated in production.

You can't audit a prompt that is one line in a context you didn't assemble.

Have you ever traced a bad answer back to what got pulled into the window instead of the instruction?

#AISecurity #AIEvaluation #RedTeaming