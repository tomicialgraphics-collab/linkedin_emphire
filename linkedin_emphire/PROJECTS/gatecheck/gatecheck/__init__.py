"""gatecheck: a security gate for AI agents that runs in CI.

The unit of output is a finding, not a test result. A finding has an
identity that survives runs, so the gate can answer the only question a
pull request actually asks: is this worse than it was yesterday.
"""
from __future__ import annotations

__version__ = "0.3.1"
