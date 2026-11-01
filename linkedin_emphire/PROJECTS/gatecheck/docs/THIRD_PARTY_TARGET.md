# Pointing the gate at an agent we did not write

This is a plan with a runbook, not a result. The result arrives when one of
the options below has been run and the numbers are in `PRECISION.md` with a
run id next to them.

The reason it matters: `groq_target/` and the attack corpus were both
written here. A reviewer will discount that, correctly. The single
strongest follow-up is the same three runs against an agent somebody else
designed, with our role reduced to adapters.

## What has to be independent

Four things can be ours or theirs, and the evidence is only as good as the
weakest one that is still ours:

| piece | current | what independence looks like |
| --- | --- | --- |
| agent code | ours | their repo, their loop |
| system prompt | ours | theirs, unchanged |
| tools | ours | theirs, unchanged |
| corpus | ours | ours, and that is fine |

The corpus staying ours is not a flaw. A gate has to own its attacks. What
has to change hands is the thing being attacked.

## The contract a target has to meet

The gate sends `POST {"message": ...}` and reads `{"reply": ...,
"actions": [...]}`. `X-Session` carries the conversation so a multi-turn
sequence stays one conversation.

The `actions` field is the part that decides how good the measurement can
be. Findings backed by a tool call do not depend on the model describing
itself honestly. A target that only returns prose limits the gate to
canary matching in text, which is weaker and noisier.

So the first question about any candidate is: **can the adapter see the
tool calls?** If the answer is no, the measurement is text-only and should
be labelled that way.

## Candidates, with the tradeoff stated

### A. An open-source agent, run locally  (recommended)

Take a real agent from a public repository, run it on this machine with
your own model key, and write a thin adapter that exposes `/chat` and maps
its tool calls to `actions`.

- Independence: high. The agent loop, the prompt and the tools are theirs.
- Work: read their entry point, write an adapter, usually 50 to 100 lines.
- Cost: whatever their agent costs per call, on your key.
- Risk: their setup may be heavy. Choose something with one file and a
  clear "run this" instruction, not a platform.
- Licence: if it permits redistribution, the adapter can live here and note
  the version. If it does not, keep it a dependency and never vendor the
  code.

This is the option to take first.

### B. A framework's own agent loop

Build the agent with a third-party framework, for example a prebuilt ReAct
agent, and keep only the prompt and the tools ours.

- Independence: medium. The loop is theirs, the instructions are ours.
- Work: an afternoon, and it runs on the same Groq key.
- Honest label: "a framework agent with our prompt", not "their agent".

**Built.** `pydantic_target/` is this option, on PydanticAI: their runtime
calls the model, parses the tool calls, executes them, and decides when the
turn ends; our prompt and our three tools sit inside it. Nine tests drive it
through a scripted model, so it runs with no key and no network, and the wire
contract is the same `/chat` plus `X-Session` that `groq_target/` speaks.
[`pydantic_target/README.md`](../pydantic_target/README.md) opens by saying
what it does not prove, because the temptation with a working adapter is to
call it the independent target and stop.

It is worth doing as a warm-up and as a second data point next to A. It is not
a substitute for A, and nothing measured on it should be described as a result
against an agent we did not write.

The first live run on it is recorded in
[`RUNTIME_COMPARISON.md`](RUNTIME_COMPARISON.md): the same corpus on both
loops, two findings that reproduced identically, one that did not reproduce
at all, and the guarded modes on that runtime still unmeasured.

### C. A public sandbox built for testing

Some vendors publish a demo endpoint with terms that allow testing.

- Independence: high, if the terms allow it.
- Risk: rate limits, downtime, and a terms-of-service question that has to
  be read rather than assumed. Read it first and keep the link.

### D. Not this

Pointing the corpus at a live product we do not own. No permission, no
measurement, and a legal problem instead of a page.

## Runbook

1. Pick the agent. One file to start it, tool calls visible, a licence you
   have read.
2. Write the adapter. It must print the tool calls it saw, or the first run
   will silently measure nothing.
3. Point `gatecheck.<name>.yml` at it with its own baseline file, because a
   new target cannot be diffed against the old one's record.
4. Run `--repeat 3` three times, unguarded, and keep every run record.
5. Read the findings by hand. Mark each true or false, with a reason.
6. Fill the table in `PRECISION.md`: attacks, findings, reproduction rate,
   hand-verified precision, coverage against what the agent actually did.
7. Commit the adapter and the run records, and write one paragraph about
   what surprised you. That paragraph is the thing a reviewer reads.

## What a publishable result looks like

- Three runs, same commit, same model, same corpus, with the reproduction
  rate for every finding.
- Every finding hand-marked, including the false positives. A page with a
  false-positive column that is not zero is more credible than one without
  the column.
- One finding that the agent's own authors would agree is real, quoted from
  their code or their prompt.
- The word "independent" used precisely, and the parts that were still ours
  named in the same paragraph.

## What I need from you to start

One thing: which candidate, or a link to an agent you already have running.
The key stays on your machine and never in this chat. I build and unit-test
the adapter here against a scripted model, which is how `groq_target/` was
tested, and you run the live pass and paste the output.

If you have no preference: send me a link to an open-source agent you have
actually used, and I will read its entry point and tell you in one message
whether it is a cheap adapter or a week of work. That is a shorter
conversation than picking from a list.
