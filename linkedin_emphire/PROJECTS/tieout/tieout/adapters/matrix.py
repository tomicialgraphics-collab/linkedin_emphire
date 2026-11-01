"""Cross-tool coverage and consensus.

Two tools that both miss a bug is not twice the evidence, it is the same
blind spot twice. Two tools where one misses and one catches is the
interesting case, and no single tool can report it because no single tool
knows what the others asked.

The matrix answers three questions per weakness:
  tested    did the tool actually run items for this weakness
  hit       how many of those items broke
  unique    did this tool catch something the others missed
"""
from __future__ import annotations

import json
from pathlib import Path

from .catalog import WEAKNESSES


def _load(run_dir: str | Path) -> tuple[dict, list[dict], list[dict]]:
    run_dir = Path(run_dir)
    lines = [
        json.loads(ln)
        for ln in (run_dir / "bundle.jsonl").read_text(encoding="utf-8").splitlines()
        if ln.strip()
    ]
    manifest = lines[0]
    events = [ln for ln in lines[1:] if ln.get("type") == "event"]
    audit = [ln for ln in lines[1:] if ln.get("type") == "tool_audit"]
    return manifest, events, audit


def coverage(run_dir: str | Path) -> dict:
    manifest, events, audit = _load(run_dir)
    tools = []
    for e in events:
        tool = e["item_id"].split("-")[0].lower()
        if tool not in tools:
            tools.append(tool)
    tools.sort()

    rows = []
    for code, w in WEAKNESSES.items():
        row = {
            "weakness": code,
            "name": w.name,
            "asi": w.asi,
            "cells": {},
            "tools_hit": [],
            "tools_tested": [],
        }
        for tool in tools:
            evs = [e for e in events if e["check"] == code and e["item_id"].lower().startswith(tool)]
            if not evs:
                row["cells"][tool] = {"tested": 0, "hit": 0, "state": "not tested"}
                continue
            hit = sum(1 for e in evs if e.get("detector_fired"))
            row["tools_tested"].append(tool)
            if hit:
                row["tools_hit"].append(tool)
            row["cells"][tool] = {
                "tested": len(evs),
                "hit": hit,
                "state": "hit" if hit else "held",
            }
        rows.append(row)

    tested_rows = [r for r in rows if r["tools_tested"]]
    both = [r["weakness"] for r in tested_rows if len(r["tools_hit"]) >= 2]
    unique = [
        {"weakness": r["weakness"], "caught_by": r["tools_hit"]}
        for r in tested_rows
        if len(r["tools_hit"]) == 1 and len(r["tools_tested"]) >= 2
    ]
    missed_by_all = [
        r["weakness"] for r in tested_rows if not r["tools_hit"]
    ]
    return {
        "run_id": manifest.get("run_id"),
        "tools": tools,
        "rows": rows,
        "found_by_two_or_more": both,
        "unique_catches": unique,
        "missed_by_every_tool": missed_by_all,
        "tool_audit": audit[0] if audit else None,
    }


def render_matrix(cov: dict) -> str:
    tools = cov["tools"]
    head = ["weakness", "asi"] + tools
    widths = [max(len(head[0]), 13), 5] + [max(10, len(t)) for t in tools]
    out = ["  ".join(h.ljust(w) for h, w in zip(head, widths, strict=False)), "  ".join("-" * w for w in widths)]
    for r in cov["rows"]:
        cells = [r["weakness"].ljust(widths[0]), r["asi"].ljust(widths[1])]
        for i, tool in enumerate(tools):
            c = r["cells"].get(tool, {"state": "not tested"})
            label = (
                f"{c['hit']}/{c['tested']} hit" if c.get("tested") else "not tested"
            )
            cells.append(label.ljust(widths[2 + i]))
        out.append("  ".join(cells))
    out.append("")
    out.append(f"found by two or more tools : {', '.join(cov['found_by_two_or_more']) or 'none'}")
    out.append(f"caught by exactly one tool : {len(cov['unique_catches'])}")
    out.append(f"missed by every tool       : {', '.join(cov['missed_by_every_tool']) or 'none'}")
    audit = cov.get("tool_audit")
    if audit:
        out.append(
            f"tool vs harness agreement  : {audit.get('agreed_total')} agreed, "
            f"{audit.get('disagreed_total')} disagreed, "
            f"rate {audit.get('agreement_rate')}"
        )
        for t in audit.get("tools", []):
            out.append(
                f"  {t['tool']:<10} items {t['items']:>2}  native pass {t['native_pass']:>2}  "
                f"native fail {t['native_fail']:>2}  undetermined {t['native_undetermined']:>2}  "
                f"agreed {t['agreed']:>2}  disagreed {t['disagreed']:>2}"
            )
    return "\n".join(out)
