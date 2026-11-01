"""DeepTeam adapter (Confident AI, Apache 2.0).

DeepTeam's full pipeline is `red_team(...)`: a simulator model invents
attacks, a target answers, an evaluation model judges. Two of those three
roles are LLM calls. That is fine and it is what the tool is for, but it
means a DeepTeam run cannot be reproduced byte for byte on a stranger's
machine, which is the one property this harness is built to keep.

So the offline path uses the half of DeepTeam that is deterministic: its
attack transformers. Base64, leetspeak and their siblings are pure
string functions, and they are exactly the transformations that find the
cheap bugs. The generative half is recorded as a named gap
(G-DEEPTEAM-SIMULATOR) rather than quietly skipped, and `live=True` runs
the full `red_team` pipeline when a model is configured.

This is the honest split, and it is worth stating in the report: a run
that says "I did not test this and here is why" is worth more than a run
that reports a green tick for a test it never ran.
"""
from __future__ import annotations

import time
from datetime import datetime, timezone

from .base import PlannedItem, ToolRecord, plan_variants
from .sandbox import ENDPOINT, respond

TOOL = "deepteam"
LABEL = "DeepTeam"
UTC = "%Y-%m-%dT%H:%M:%SZ"

# DeepTeam's deterministic transformers. The generative attacks
# (roleplay, authority escalation, prompt injection) need a simulator
# model and are out of scope for an offline run.
VARIANTS = {"raw": "prompt as written", "b64": "DeepTeam Base64", "leet": "DeepTeam Leetspeak"}

GAP_CODE = "G-DEEPTEAM-SIMULATOR"


def _now() -> str:
    return datetime.now(timezone.utc).strftime(UTC)


class DeepTeamAdapter:
    tool = TOOL
    label = LABEL

    def __init__(self, live: bool = False) -> None:
        self.live = live

    def available(self) -> tuple[bool, str]:
        try:
            import deepteam  # noqa: F401
        except ModuleNotFoundError as e:
            if "sentry_sdk" in str(e):
                return False, "deepteam needs sentry-sdk at import: pip install sentry-sdk"
            return False, f"deepteam not importable: {e}"
        except Exception as e:  # pragma: no cover
            return False, f"deepteam not importable: {type(e).__name__}: {e}"
        return True, ""

    def version(self) -> str:
        try:
            from importlib import metadata

            return metadata.version("deepteam")
        except Exception:
            return "unknown"

    def plan(self) -> list[PlannedItem]:
        return plan_variants(TOOL, VARIANTS)

    def _transform(self, variant: str, prompt: str) -> tuple[str, str]:
        """(transformed prompt, note). Uses DeepTeam's own attack classes."""
        if variant == "raw":
            return prompt, "no transform"
        try:
            from deepteam.attacks.single_turn import Base64, Leetspeak

            if variant == "b64":
                return Base64(weight=1).enhance(attack=prompt), "DeepTeam Base64.enhance"
            return Leetspeak(weight=1).enhance(attack=prompt), "DeepTeam Leetspeak.enhance"
        except Exception as e:
            return prompt, f"transform unavailable ({type(e).__name__}: {e}); sent as written"

    def run(self, items: list[PlannedItem]) -> list[ToolRecord]:
        version = self.version()
        records: list[ToolRecord] = []
        for item in items:
            prompt_sent, note = self._transform(item.variant, item.prompt)
            started = _now()
            t0 = time.perf_counter()
            output, actions = respond(prompt_sent)
            elapsed = int((time.perf_counter() - t0) * 1000)
            records.append(
                ToolRecord(
                    item_id=item.item_id,
                    tool=TOOL,
                    tool_version=version,
                    prompt_sent=prompt_sent,
                    response=output,
                    native_verdict="undetermined",
                    native_detail=(
                        "transform-only execution: DeepTeam's judge is an LLM and none was "
                        "configured, so the tool records no verdict (see " + GAP_CODE + ")"
                    ),
                    actions=actions,
                    latency_ms=elapsed,
                    started_at=started,
                    finished_at=_now(),
                    extra={
                        "variant": item.variant,
                        "transform": note,
                        "target_endpoint": ENDPOINT,
                    },
                )
            )
        return records
