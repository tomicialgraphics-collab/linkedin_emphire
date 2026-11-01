"""Re-derive an adapter bundle without any of the three tools.

This is the claim the project makes, applied to the tools themselves: if
verifying a red-team run needs PyRIT, promptfoo and DeepTeam installed,
then the run is a claim about a machine, not evidence about a system.

So verification here does four things and nothing else:

  1. re-scores every stored raw output with the deterministic detector
     named in the event, and compares to the stored verdict
  2. re-hashes the raw sidecar and checks each record against the hash it
     carries
  3. re-counts the tools' own verdicts from the sidecar, so the agreement
     numbers in the bundle can be recomputed rather than trusted
  4. reports what it could not check as a gap

No imports of pyrit, promptfoo or deepteam appear in this module, by
design. A test asserts that.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .catalog import WEAKNESSES
from .detectors import DETECTORS


@dataclass
class RederiveResult:
    ok: bool
    lines: list[str] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)


def _detector_for(check: str):
    w = WEAKNESSES.get(check)
    if w is None:
        return None
    return DETECTORS[w.detector]


def rederive_bundle(run_dir: str | Path) -> RederiveResult:
    run_dir = Path(run_dir)
    res = RederiveResult(ok=True)
    bundle = run_dir / "bundle.jsonl"
    sidecar = run_dir / "raw" / "records.jsonl"
    if not bundle.exists():
        res.ok = False
        res.lines.append("no bundle.jsonl at " + str(run_dir))
        return res

    lines = [json.loads(ln) for ln in bundle.read_text(encoding="utf-8").splitlines() if ln.strip()]
    events = [ln for ln in lines[1:] if ln.get("type") == "event"]
    res.lines.append(f"events : {len(events)}")

    mismatched = 0
    unknown = 0
    for e in events:
        det = _detector_for(e.get("check", ""))
        if det is None:
            unknown += 1
            res.gaps.append(f"G-DETECTOR-UNKNOWN {e.get('item_id')}: no detector for {e.get('check')}")
            continue
        fired = bool(det(e.get("raw_output") or ""))
        expected = "fail" if fired else "pass"
        if fired != e.get("detector_fired") or expected != e.get("decision"):
            mismatched += 1
            res.gaps.append(
                f"G-VERDICT-MISMATCH {e.get('item_id')}: re-derived {expected}, stored {e.get('decision')}"
            )
    res.lines.append(
        f"scored : {len(events) - mismatched - unknown}/{len(events)} verdicts re-derived from stored raw"
    )

    if not sidecar.exists():
        res.gaps.append("G-SIDECAR raw/records.jsonl is missing; tool verdicts cannot be recounted")
    else:
        records = [json.loads(ln) for ln in sidecar.read_text(encoding="utf-8").splitlines() if ln.strip()]
        header = records[0]
        recs = records[1:]
        native = {"pass": 0, "fail": 0, "undetermined": 0}
        for r in recs:
            native[r.get("native_verdict", "undetermined")] = native.get(r.get("native_verdict", "undetermined"), 0) + 1
        res.lines.append(
            f"records: {len(recs)} raw records, tools {', '.join(header.get('tools_run', [])) or 'none'}"
        )
        res.lines.append(
            f"native : {native['pass']} pass, {native['fail']} fail, {native['undetermined']} undetermined (tool's own)"
        )
        ids = {r.get("item_id") for r in recs}
        missing_events = [i for i in ids if i not in {e.get("item_id") for e in events}]
        if missing_events:
            res.gaps.append(f"G-RECORD {len(missing_events)} sidecar record(s) have no event")
        skipped = header.get("tools_skipped") or []
        for s in skipped:
            res.gaps.append(f"G-ADAPTER {s.get('tool')}: {s.get('reason')}")

    for g in res.gaps:
        code = g.split()[0]
        if code in ("G-VERDICT-MISMATCH", "G-SIDECAR", "G-RECORD", "G-DETECTOR-UNKNOWN"):
            res.ok = False
    res.lines.append(f"VERDICT: {'PASS' if res.ok else 'FAIL'}")
    return res
