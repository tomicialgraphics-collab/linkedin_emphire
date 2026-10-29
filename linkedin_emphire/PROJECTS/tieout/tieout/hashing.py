"""Canonical hashing and the verdict-event hash chain (P1 / P5).

The chain is the unit of re-derivation. Each record line carries the
sha256 of its canonical payload, including the previous line's hash.
A stranger with the bundle file and the check definition can re-walk
the chain, re-hash the manifest, and re-run the detectors on the
stored raw outputs: no model, no key, no network.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

GENESIS = "0" * 64


def canonical(obj: object) -> str:
    """Canonical JSON: sorted keys, compact separators, no key reordering."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def record_hash(payload: dict) -> str:
    """Hash of one record line.

    The caller passes the record dict with its own hash field removed
    and prev_hash already set. verify() recomputes exactly this.
    """
    h = {k: v for k, v in payload.items() if k != "record_hash"}
    return sha256_text(canonical(h))
