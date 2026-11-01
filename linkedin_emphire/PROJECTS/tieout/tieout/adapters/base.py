"""Adapter protocol: what a red-team tool has to give the harness.

Three rules make the three tools comparable:

1. tieout plans before anything runs. Every item id exists before the
   tool starts, so a tool that silently drops an attack leaves a nameable
   absence (P4) instead of a smaller number.
2. The tool reports what it sent and what came back. The harness does not
   accept a score alone.
3. The harness owns the judge. Each tool's own verdict is recorded beside
   ours as `native_verdict`, and the gap between the two is measured
   rather than hidden. A tool's opinion is evidence about the tool.

Nothing here imports PyRIT, promptfoo or DeepTeam. The adapters do that
lazily, so a machine with none of them installed can still verify a
bundle produced by all three.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from ..harness.base import Control, Family, Item
from .catalog import ATTACKS, CONTROLS, WEAKNESSES, attack
from .detectors import DETECTORS


@dataclass(frozen=True)
class PlannedItem:
    """One pre-assigned unit of work, before any tool touches it."""
    item_id: str       # "<TOOL>-<ATTACK>-<variant>", e.g. PYRIT-A01-raw
    tool: str
    attack_id: str
    weakness: str
    variant: str
    prompt: str
    action: str


@dataclass
class ToolRecord:
    """What one tool reports for one planned item."""
    item_id: str
    tool: str
    tool_version: str
    prompt_sent: str
    response: str
    native_verdict: str        # "pass" | "fail" | "undetermined"
    native_detail: str
    actions: list[str] = field(default_factory=list)
    latency_ms: int = 0
    started_at: str = ""
    finished_at: str = ""
    extra: dict = field(default_factory=dict)


class Adapter(Protocol):
    tool: str          # short id used in item ids and the matrix
    label: str         # human name for the report

    def available(self) -> tuple[bool, str]:
        """(installed?, reason if not)."""
        ...

    def version(self) -> str:
        ...

    def plan(self) -> list[PlannedItem]:
        ...

    def run(self, items: list[PlannedItem]) -> list[ToolRecord]:
        ...


def item_id(tool: str, attack_id: str, variant: str) -> str:
    return f"{tool.upper()}-{attack_id}-{variant}"


def plan_variants(tool: str, variants: dict[str, str]) -> list[PlannedItem]:
    """Plan every attack once per variant.

    `variants` maps a variant name to a note about how the text changes;
    the prompt itself is produced by the adapter, because the point of
    the variant is the tool's own transform.
    """
    items: list[PlannedItem] = []
    for a in ATTACKS:
        for variant in variants:
            items.append(
                PlannedItem(
                    item_id=item_id(tool, a.attack_id, variant),
                    tool=tool,
                    attack_id=a.attack_id,
                    weakness=a.weakness,
                    variant=variant,
                    prompt=a.prompt,
                    action=a.action,
                )
            )
    return items


def build_family(items: list[PlannedItem], label: str) -> Family:
    """A Family the existing verify() can re-derive, built from adapter items."""
    fam_items = [
        Item(
            item_id=i.item_id,
            check=i.weakness,
            action=i.action,
            input_spec={
                "tool": i.tool,
                "attack": i.attack_id,
                "variant": i.variant,
                "prompt": i.prompt,
            },
        )
        for i in items
    ]
    fam_controls = [
        Control(
            control_id=cid,
            check=check,
            kind=kind,
            crafted_raw=raw,
            expected_fire=expected,
            note=note,
        )
        for cid, check, kind, raw, expected, note in CONTROLS
    ]
    return Family(
        family_id="A0_ADAPTERS",
        name=label,
        policy_label="adapter-catalog/v1",
        items=fam_items,
        controls=fam_controls,
        # keyed by weakness code, which is what the event's `check` holds
        detectors={w.code: DETECTORS[w.detector] for w in WEAKNESSES.values()},
    )


def detector_name(weakness: str) -> str:
    return WEAKNESSES[weakness].detector


def attack_of(planned: PlannedItem):
    return attack(planned.attack_id)
