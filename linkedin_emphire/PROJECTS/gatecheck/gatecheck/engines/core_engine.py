"""The first-party engine: no dependency, always available.

A gate that needs three third-party tools before it can say anything is
a gate that reports "nothing found" on a clean machine, which is worse
than reporting nothing at all. This engine runs the same corpus with no
extras installed, so `pip install -e .` and one command produce a real
result on the first try. The three tools then add breadth (DeepTeam's
encodings), sequences (PyRIT's campaigns) and CI assertions (promptfoo),
on top of a result the gate could already stand behind.
"""
from __future__ import annotations

from ..corpus import SEQUENCES, SINGLE_TURN, Case
from .base import Engine


class CoreEngine(Engine):
    name = "gatecheck"
    label = "gatecheck core"

    def available(self) -> tuple[bool, str]:
        return True, ""

    def version(self) -> str:
        from .. import __version__

        return __version__

    def plan(self) -> list[Case]:
        return list(SINGLE_TURN) + list(SEQUENCES)
