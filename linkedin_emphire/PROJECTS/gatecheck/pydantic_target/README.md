# pydantic_target

The claims assistant from `groq_target/` on a runtime we did not write.

PydanticAI owns the agent loop here: it calls the model, parses the tool
calls, runs them, feeds the results back, and decides when the turn is over.
Our prompt and our three tools sit inside that loop. The gate never knows the
difference, because it only sees the `actions` that come back over HTTP.

**What this proves:** the gate reads actions the way somebody else's runtime
produces them, not only the way our own loop produces them.

**What this does not prove:** independence. The prompt, the tools, the sandbox,
and the attack corpus are all still ours. If every finding this repo has ever
reported came from a target we wrote, a reviewer is right to ask what happens
against an agent we did not. That question is answered by
[`docs/THIRD_PARTY_TARGET.md`](../docs/THIRD_PARTY_TARGET.md), not by this
folder.

## Run it

```powershell
pip install "pydantic-ai-slim[openai]"
$env:GROQ_API_KEY = "gsk_..."          # your key; it never leaves your machine
python -m pydantic_target.serve --mode vulnerable      # terminal 1
python -m gatecheck run --config gatecheck.pydantic.yml  # terminal 2
```

The guarded modes work the same way as the Groq target:

```powershell
python -m pydantic_target.serve --mode guarded                 # prompt + refusing tools
python -m pydantic_target.serve --mode guarded --prompt-only   # prompt only, nothing in the tools
```

The second one is the comparison worth keeping: same words in the system
prompt, no enforcement underneath, and the run says how far the words got.

## Without a key

```powershell
python -m pydantic_target.serve --fake
```

`--fake` answers from a script, so you can point the gate at it and see the
wiring work before you spend a token. Do not quote a finding count from a
`--fake` run: the script is not a model and its answers are fixed.

## Why a second runtime at all

The shorter version is in the note. The longer one: a harness that only ever
measures its author's loop has not been tested against the thing it claims to
test. PydanticAI runs tools through `RunContext`, collects them differently,
retries differently, and gives the model a different message shape. If the
gate's findings survive that, they are findings about agent behaviour. If they
only appear inside our own loop, they were findings about our loop.

## Files

| file | what it holds |
| --- | --- |
| `agent.py` | `Policy` (the refusals), `build_agent`, `ClaimsRunner`, `groq_model` |
| `serve.py` | the `/chat` server: `--fake`, `--mode`, `--prompt-only`, `--port` |

The system prompts come from `groq_target/agent.py` on purpose. Editing them
in two places is how the two targets drift apart and stop being comparable.
