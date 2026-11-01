"""Adapter layer: run PyRIT, promptfoo and DeepTeam, keep one record.

The three tools answer different questions in different vocabularies and
each one grades its own work. This package holds the catalog, the
deterministic judge, the three thin adapters, the cross-tool matrix and
the tool-free re-derivation. See docs/adapters.md.
"""
from __future__ import annotations

from .catalog import ATTACKS, WEAKNESSES, catalog_hash
from .deepteam_adapter import DeepTeamAdapter
from .promptfoo_adapter import PromptfooAdapter
from .pyrit_adapter import PyRITAdapter
from .rederive import rederive_bundle
from .runner import ADAPTERS, AdapterRun, run_adapters

__all__ = [
    "ADAPTERS",
    "ATTACKS",
    "WEAKNESSES",
    "AdapterRun",
    "DeepTeamAdapter",
    "PromptfooAdapter",
    "PyRITAdapter",
    "catalog_hash",
    "rederive_bundle",
    "run_adapters",
]
