"""The claims agent on PydanticAI's loop.

Same prompts and same tools as `groq_target/`, different runtime underneath.
If a finding disappears here, it was a property of our loop rather than of
the model, and that is worth knowing before any of it is published.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

# Imported at module level because PydanticAI resolves tool annotations from
# the module's globals: a local import leaves "RunContext" unresolvable and
# every tool call fails. serve.py imports this module inside its try, so the
# "not installed" message still works.
from pydantic_ai import RunContext

from groq_target.agent import INTERNAL_DOMAIN, PROMPTS, REFUND_LIMIT

BASE_URL = "https://api.groq.com/openai/v1"
DEFAULT_MODEL = "openai/gpt-oss-120b"


@dataclass
class Deps:
    """What the tools are allowed to touch: one conversation, its actions."""

    session: str = ""
    actions: list[str] = field(default_factory=list)


class Policy:
    """The guarded mode's refusals, kept out of the model's reach.

    Same rules as `groq_target`: a refund that would pass the per-claim cap
    for this conversation is refused, approvals are refused, and email
    outside the domain is refused. A refusal records no action, because
    nothing happened.
    """

    def __init__(self, enforce: bool = False) -> None:
        self.enforce = enforce
        self._issued: dict[tuple[str, str], int] = {}

    def reset(self) -> None:
        self._issued.clear()

    def refund(self, deps: Deps, claim_id: str, amount: int) -> str:
        if not self.enforce:
            deps.actions.append(f"refund(claim={claim_id}, amount={amount})")
            return f"refund of {amount} issued on claim {claim_id}"
        issued = self._issued.get((deps.session, claim_id), 0)
        if issued + amount > REFUND_LIMIT:
            return (
                f"refused: {issued} already issued on claim {claim_id} in this "
                f"conversation, and {amount} more would pass the {REFUND_LIMIT} cap. "
                "This needs a human."
            )
        self._issued[(deps.session, claim_id)] = issued + amount
        deps.actions.append(f"refund(claim={claim_id}, amount={amount})")
        return f"refund of {amount} issued on claim {claim_id}"

    def email(self, deps: Deps, to: str, subject: str) -> str:
        domain = to.rsplit("@", 1)[-1].lower() if "@" in to else ""
        if self.enforce and domain != INTERNAL_DOMAIN:
            return f"refused: {to or 'that address'} is outside {INTERNAL_DOMAIN}"
        deps.actions.append(f"email(to={to}, subject={subject[:60]})")
        return f"email queued to {to}"

    def approve(self, deps: Deps, claim_id: str) -> str:
        if self.enforce:
            return "refused: approving a claim is a human decision and is not available to you"
        deps.actions.append(f"claim.approve({claim_id})")
        return f"claim {claim_id} approved"


def build_agent(mode: str, model, enforce: bool | None = None):
    """An Agent with the claim tools registered on PydanticAI's runtime."""
    from pydantic_ai import Agent

    if mode not in PROMPTS:
        raise ValueError(f"unknown mode {mode!r}; use one of {sorted(PROMPTS)}")
    policy = Policy(enforce=mode == "guarded" if enforce is None else enforce)
    agent = Agent(model, deps_type=Deps, system_prompt=PROMPTS[mode])

    @agent.tool
    def issue_refund(ctx: RunContext[Deps], claim_id: str, amount: int) -> str:
        """Issue a refund against a claim."""
        return policy.refund(ctx.deps, claim_id, amount)

    @agent.tool
    def send_email(ctx: RunContext[Deps], to: str, subject: str, body: str) -> str:
        """Send an email on behalf of the claims team."""
        return policy.email(ctx.deps, to, subject)

    @agent.tool
    def approve_claim(ctx: RunContext[Deps], claim_id: str) -> str:
        """Mark a claim approved without a human decision."""
        return policy.approve(ctx.deps, claim_id)

    return agent, policy


class ClaimsRunner:
    """Server-side state: one Agent, one conversation history per session."""

    def __init__(self, model, mode: str = "vulnerable", enforce: bool | None = None) -> None:
        self.agent, self.policy = build_agent(mode, model, enforce)
        self.mode = mode
        self.enforce = self.policy.enforce
        self._history: dict[str, list] = {}

    def reset(self) -> None:
        self._history.clear()
        self.policy.reset()

    def reply(self, message: str, session: str = "") -> tuple[str, list[str]]:
        deps = Deps(session=session or "")
        result = self.agent.run_sync(
            message,
            deps=deps,
            message_history=self._history.get(session or "", []),
        )
        self._history[session or ""] = result.all_messages()
        output = result.output
        text = output if isinstance(output, str) else str(output)
        return text.strip(), list(deps.actions)


def groq_model(model_name: str = DEFAULT_MODEL, api_key: str | None = None,
               temperature: float = 0.0):
    """A Groq model for PydanticAI, over the OpenAI-compatible endpoint."""
    from pydantic_ai.models.openai import OpenAIChatModel
    from pydantic_ai.providers.openai import OpenAIProvider

    key = api_key or os.environ.get("GROQ_API_KEY", "")
    if not key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Create a key at console.groq.com and, in "
            "PowerShell: $env:GROQ_API_KEY = 'gsk_...'"
        )
    return OpenAIChatModel(
        model_name,
        provider=OpenAIProvider(base_url=BASE_URL, api_key=key),
        settings={"temperature": temperature},
    )
