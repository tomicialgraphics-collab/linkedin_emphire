"""A real model behind a real endpoint, for people who want more than the demo.

The gate does not care where the answers come from. This folder is the
smallest honest target that puts a language model behind the gate's
contract:

    groq_target/model.py   Groq chat completions over plain urllib
    groq_target/agent.py   the claims agent: system prompt, tools, sessions
    groq_target/serve.py   POST /chat -> {"reply": ..., "actions": [...]}

Two prompt modes exist so the before/after claim survives the move from a
rule engine to a model: `vulnerable` is a sloppy claims assistant, `guarded`
is the same assistant with the rules written down. Nothing else changes
between them, so a difference in what the gate finds is a difference in the
prompt.
"""
