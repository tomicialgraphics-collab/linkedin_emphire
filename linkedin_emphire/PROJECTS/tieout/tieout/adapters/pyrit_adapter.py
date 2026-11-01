"""PyRIT adapter (Microsoft, MIT).

PyRIT is the campaign engine: a target abstraction, converters, and an
attack executor with memory. We give it our own target (the sandbox) and
our own prompts (the catalog), let it run the single-turn send attack,
and take back three things per item: what was sent, what came back, and
PyRIT's own outcome for the attempt.

That last one is instructive. With no scorer attached, PyRIT returns
`AttackOutcome.UNDETERMINED` for every attempt. The tool is telling the
truth: it ran the attack and does not know whether it worked. The harness
records that beside its own verdict, which is the whole argument for an
external judge in one line of output.

PyRIT 1.x notes: memory must be initialised before a target is built
(`CentralMemory.set_memory_instance`), and prompts take a role string.
Both are handled here rather than in the runner, so a PyRIT API change
breaks in one file.
"""
from __future__ import annotations

import asyncio
import logging
import os
import tempfile
import time
from datetime import datetime, timezone

from ..hashing import sha256_text
from .base import PlannedItem, ToolRecord, plan_variants
from .sandbox import ENDPOINT, respond

TOOL = "pyrit"
LABEL = "PyRIT"
UTC = "%Y-%m-%dT%H:%M:%SZ"

# Two renderings of every attack: as written, and base64 encoded by
# PyRIT's own converter path below.
VARIANTS = {"raw": "prompt as written", "b64": "base64 encoded"}


def _now() -> str:
    return datetime.now(timezone.utc).strftime(UTC)


class PyRITSandboxTarget:  # replaced at import time by a real PromptTarget
    pass


def _build_target_class():
    """Define the PromptTarget subclass lazily, so this module imports
    on a machine without PyRIT."""
    from pyrit.models import Message
    from pyrit.prompt_target.common.prompt_target import PromptTarget

    class SandboxPromptTarget(PromptTarget):
        """A PyRIT target whose 'model' is the deterministic sandbox."""

        def __init__(self) -> None:
            super().__init__()
            self.last_actions: list[str] = []
            self.last_output: str = ""
            self.calls: int = 0

        async def _send_prompt_to_target_async(self, *, normalized_conversation):
            text = normalized_conversation[-1].get_value() or ""
            output, actions = respond(text)
            self.last_output, self.last_actions = output, actions
            self.calls += 1
            return [Message.from_prompt(prompt=output, role="assistant")]

        def _validate_request(self, *, normalized_conversation) -> None:
            return None

        async def cleanup_target_async(self) -> None:
            return None

    return SandboxPromptTarget


class PyRITAdapter:
    tool = TOOL
    label = LABEL

    def available(self) -> tuple[bool, str]:
        try:
            import pyrit  # noqa: F401
        except Exception as e:  # pragma: no cover - depends on the machine
            return False, f"pyrit not importable: {type(e).__name__}: {e}"
        return True, ""

    def version(self) -> str:
        try:
            from importlib import metadata

            return metadata.version("pyrit")
        except Exception:
            return "unknown"

    def plan(self) -> list[PlannedItem]:
        return plan_variants(TOOL, VARIANTS)

    def run(self, items: list[PlannedItem]) -> list[ToolRecord]:
        return asyncio.run(self._run_async(items))

    async def _run_async(self, items: list[PlannedItem]) -> list[ToolRecord]:
        logging.getLogger("pyrit").setLevel(logging.ERROR)

        from pyrit.executor.attack.single_turn.prompt_sending import PromptSendingAttack
        from pyrit.memory import CentralMemory
        from pyrit.memory.sqlite_memory import SQLiteMemory

        db_dir = tempfile.mkdtemp(prefix="tieout-pyrit-")
        CentralMemory.set_memory_instance(SQLiteMemory(db_path=os.path.join(db_dir, "pyrit.db")))

        target_cls = _build_target_class()
        records: list[ToolRecord] = []
        version = self.version()

        for item in items:
            target = target_cls()
            prompt_sent = item.prompt
            if item.variant == "b64":
                prompt_sent = _base64_variant(item.prompt)
            started = _now()
            t0 = time.perf_counter()
            native, detail = "undetermined", "no scorer attached; PyRIT does not grade without one"
            output = ""
            try:
                attack = PromptSendingAttack(objective_target=target)
                result = await attack.execute_async(objective=prompt_sent)
                output = result.last_response.converted_value or ""
                outcome = str(getattr(result, "outcome", "undetermined")).lower()
                native = "undetermined" if "undetermined" in outcome else (
                    "pass" if "success" in outcome else "fail"
                )
                detail = f"AttackOutcome={getattr(result, 'outcome', None)}"
            except Exception as e:  # a tool failure is a named gap, not a silence
                detail = f"pyrit execution error: {type(e).__name__}: {e}"
                native = "undetermined"
            elapsed = int((time.perf_counter() - t0) * 1000)
            records.append(
                ToolRecord(
                    item_id=item.item_id,
                    tool=TOOL,
                    tool_version=version,
                    prompt_sent=prompt_sent,
                    response=output,
                    native_verdict=native,
                    native_detail=detail,
                    actions=list(target.last_actions),
                    latency_ms=elapsed,
                    started_at=started,
                    finished_at=_now(),
                    extra={
                        "orchestrator": "PromptSendingAttack",
                        "variant": item.variant,
                        "prompt_sha256": sha256_text(prompt_sent),
                        "target_endpoint": ENDPOINT,
                    },
                )
            )
        return records


def _base64_variant(prompt: str) -> str:
    """Encode with PyRIT's own converter if present, else plain base64.

    Using the tool's converter keeps the variant honest: it is the exact
    transform PyRIT would apply in a real campaign, not a lookalike.
    """
    try:
        from pyrit.converter import Base64Converter

        conv = Base64Converter()
        out = conv.convert(prompt) if hasattr(conv, "convert") else None
        if isinstance(out, str) and out:
            return out
    except Exception:
        pass
    import base64

    return base64.b64encode(prompt.encode("utf-8")).decode("ascii")
