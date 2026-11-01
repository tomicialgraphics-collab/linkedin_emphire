"""The three engines, in the order the gate runs them."""
from __future__ import annotations

from .base import Engine, EngineResult
from .core_engine import CoreEngine
from .deepteam_engine import DeepTeamEngine
from .promptfoo_engine import PromptfooEngine
from .pyrit_engine import PyRITEngine

ENGINES: dict[str, type[Engine]] = {
    "gatecheck": CoreEngine,
    "deepteam": DeepTeamEngine,
    "pyrit": PyRITEngine,
    "promptfoo": PromptfooEngine,
}

__all__ = [
    "ENGINES",
    "CoreEngine",
    "DeepTeamEngine",
    "Engine",
    "EngineResult",
    "PromptfooEngine",
    "PyRITEngine",
]
