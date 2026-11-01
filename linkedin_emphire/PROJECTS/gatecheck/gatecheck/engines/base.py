"""Engine contract: three tools, one shape.

An engine plans work from the corpus and returns findings. It does not
choose severity and it does not deduplicate: those are gate decisions, so
that two runs of the gate on the same target agree even if the engines
change.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone

from ..corpus import Case
from ..detectors import detect
from ..models import Evidence, Finding
from ..targets import TargetError

UTC = "%Y-%m-%dT%H:%M:%SZ"


def now() -> str:
    return datetime.now(timezone.utc).strftime(UTC)


@dataclass
class EngineResult:
    tool: str
    version: str
    findings: list[Finding] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    attacks_run: int = 0
    duration_ms: int = 0
    skipped: str = ""


class Engine:
    name = "base"
    label = "base"

    def available(self) -> tuple[bool, str]:
        return True, ""

    def version(self) -> str:
        return "0"

    def plan(self) -> list[Case]:
        raise NotImplementedError

    def run(self, target, cases: list[Case], severity_for, repeat: int = 1) -> EngineResult:
        started = time.perf_counter()
        repeat = max(1, int(repeat))
        result = EngineResult(tool=self.name, version=self.version())
        for case in cases:
            found = None
            hits = 0
            for _ in range(repeat):
                try:
                    finding = self._execute(target, case, severity_for)
                except TargetError as e:
                    result.errors.append(f"{case.attack_id}: {e}")
                    break
                result.attacks_run += 1
                if finding is not None:
                    hits += 1
                    if found is None:
                        found = finding
            if found is not None:
                found.hits = hits
                found.runs = repeat
                result.findings.append(found)
        result.duration_ms = int((time.perf_counter() - started) * 1000)
        return result

    def _execute(self, target, case: Case, severity_for) -> Finding | None:
        if hasattr(target, "session"):
            target.session = f"gatecheck-{self.name}-{case.attack_id}"
        hit = None            # (index, reply, category)
        actions: list[str] = []
        for index, prompt in enumerate(case.prompts):
            reply = target.send(prompt)
            if not reply.ok:
                return None
            actions.extend(reply.actions)
            category = detect(reply.text, reply.actions)
            if category is not None:
                hit = (index, reply, category)
                if index == len(case.prompts) - 1:
                    break
        if hit is None:
            return None
        index, reply, category = hit
        # A break on the last turn of a sequence, where every earlier turn
        # was allowed, is an escalation finding. A break on an earlier turn
        # is the plain category: the sequence did not cause it.
        if case.turns > 1 and index == len(case.prompts) - 1:
            category = "multi-turn-escalation"
        return Finding(
            category=category,
            severity=severity_for(category),
            title=_title(category, case),
            evidence=Evidence(prompt=case.prompts[index], response=reply.text, actions=actions),
            found_by=[self.name],
            attack_id=case.attack_id,
            turns=index + 1,
            first_seen=now(),
            last_seen=now(),
        )


def _title(category: str, case: Case) -> str:
    return {
        "system-prompt-leak": "agent discloses its instructions",
        "prompt-injection": "agent follows instructions from untrusted content",
        "tool-misuse": "agent executes an action above the approval limit",
        "data-exfiltration": "agent sends customer data to an external address",
        "multi-turn-escalation": "a sequence of allowed turns ends in a disallowed action",
    }.get(category, category)
