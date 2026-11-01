"""Stable hashing helpers. No clock, no randomness, no machine state."""
from __future__ import annotations

import hashlib


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def short(text: str, n: int = 16) -> str:
    return sha256_text(text)[:n]
