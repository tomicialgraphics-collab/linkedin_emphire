"""PyRIT engine: sequences.

PyRIT is the campaign tool: a target abstraction, memory, and an attack
executor that can hold a conversation. In a gate its job is the case a
single-turn scanner cannot reach, where every individual turn is allowed
and the last one is not.

PyRIT 1.x needs a memory instance before a target is constructed, so the
engine owns that setup and tears it down. If PyRIT is absent the engine
reports itself unavailable and the gate keeps going with the other two.
"""
from __future__ import annotations

import asyncio
import logging
import os
import tempfile

from ..corpus import SEQUENCES, SINGLE_TURN, Case
from .base import Engine


class PyRITEngine(Engine):
    name = "pyrit"
    label = "PyRIT"

    def available(self) -> tuple[bool, str]:
        try:
            import pyrit  # noqa: F401
        except Exception as e:
            return False, f"pyrit not installed: {e}"
        return True, ""

    def version(self) -> str:
        try:
            from importlib import metadata

            return metadata.version("pyrit")
        except Exception:
            return "unknown"

    def plan(self) -> list[Case]:
        # Sequences first: they are the reason this engine is in the gate.
        return list(SEQUENCES) + list(SINGLE_TURN[:4])

    def run(self, target, cases, severity_for):
        logging.getLogger("pyrit").setLevel(logging.ERROR)
        return asyncio.run(self._run_async(target, cases, severity_for))

    async def _run_async(self, target, cases, severity_for):
        import time

        from ..detectors import detect
        from ..models import Evidence, Finding
        from ..targets import TargetError
        from .base import EngineResult, _title, now

        _setup_memory()

        started = time.perf_counter()
        result = EngineResult(tool=self.name, version=self.version())

        for case in cases:
            try:
                hit = await self._run_case(case, target, detect)
            except TargetError as e:
                result.errors.append(f"{case.attack_id}: {e}")
                continue
            result.attacks_run += 1
            if hit is None:
                continue
            index, reply, category = hit
            if case.turns > 1 and index == len(case.prompts) - 1:
                category = "multi-turn-escalation"
            result.findings.append(
                Finding(
                    category=category,
                    severity=severity_for(category),
                    title=_title(category, case),
                    evidence=Evidence(prompt=case.prompts[index], response=reply.text,
                                      actions=reply.actions),
                    found_by=[self.name],
                    attack_id=case.attack_id,
                    turns=index + 1,
                    first_seen=now(),
                    last_seen=now(),
                )
            )
        result.duration_ms = int((time.perf_counter() - started) * 1000)
        return result

    async def _run_case(self, case: Case, target, detect):
        """Drive the case through PyRIT's executor against an HTTP target.

        PyRIT keeps memory for the conversation and applies its own
        normalisation to every message, which is the point: the gate is
        testing what PyRIT would actually send, not what we would.
        """
        from pyrit.executor.attack.single_turn.prompt_sending import PromptSendingAttack
        from pyrit.models import Message
        from pyrit.prompt_target.common.prompt_target import PromptTarget

        class HttpPromptTarget(PromptTarget):
            def __init__(self):
                super().__init__()
                self.last_reply = None

            async def _send_prompt_to_target_async(self, *, normalized_conversation):
                text = normalized_conversation[-1].get_value() or ""
                reply = target.send(text)
                self.last_reply = reply
                return [Message.from_prompt(prompt=reply.text, role="assistant")]

            def _validate_request(self, *, normalized_conversation) -> None:
                return None

            async def cleanup_target_async(self) -> None:
                return None

        hit = None
        for index, prompt in enumerate(case.prompts):
            if hasattr(target, "session"):
                target.session = f"gatecheck-pyrit-{case.attack_id}"
            prompt_target = HttpPromptTarget()
            attack = PromptSendingAttack(objective_target=prompt_target)
            await attack.execute_async(objective=prompt)
            reply = prompt_target.last_reply
            if reply is None:
                continue
            category = detect(reply.text, reply.actions)
            if category is not None:
                hit = (index, reply, category)
        return hit


def _setup_memory() -> None:
    from pyrit.memory.central_memory import CentralMemory
    from pyrit.memory.sqlite_memory import SQLiteMemory

    db = os.path.join(tempfile.mkdtemp(prefix="gatecheck-pyrit-"), "memory.db")
    try:
        CentralMemory.get_memory_instance()
    except Exception:
        CentralMemory.set_memory_instance(SQLiteMemory(db_path=db))
