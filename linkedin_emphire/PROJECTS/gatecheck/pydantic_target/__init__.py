"""The same claims agent, run by somebody else's agent loop.

`groq_target/` writes its own tool-calling loop: it calls the model, reads
the tool calls, runs them, feeds the results back, and stops after a few
steps. Every one of those decisions is ours, which is fine for a
demonstration and weak for evidence.

This package keeps the claim tools and the prompts, throws the loop away,
and hands the turn to PydanticAI, a third-party agent framework. The agent
loop, the message handling, the tool schema derivation and the retry
behaviour are theirs. What stays ours is the part a gate is allowed to own:
the tools, the policy, and the attacks.

That is the honest middle of the independence ladder described in
docs/THIRD_PARTY_TARGET.md. It is not somebody else's agent. It is somebody
else's runtime, which is the cheapest way to check that the findings were
not an artefact of how our own loop was written.
"""
