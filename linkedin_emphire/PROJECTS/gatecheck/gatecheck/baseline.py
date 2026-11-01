"""The baseline: the only reason a gate can be trusted on a Tuesday.

Without a stored baseline every run reports everything and the gate is
noise, which is how security gates die. With one, a pull request is
judged against the last accepted state of the same target, and the only
thing that fails the build is a change.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .models import Finding, Severity

UTC = "%Y-%m-%dT%H:%M:%SZ"

NEW = "new"
FIXED = "fixed"
UNCHANGED = "unchanged"
WORSE = "worse"


def _now() -> str:
    return datetime.now(timezone.utc).strftime(UTC)


@dataclass
class Baseline:
    path: Path
    findings: dict[str, dict] = field(default_factory=dict)
    updated_at: str = ""

    @classmethod
    def load(cls, path: str | Path) -> Baseline:
        path = Path(path)
        if not path.exists():
            return cls(path=path)
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            path=path,
            findings={f["id"]: f for f in data.get("findings", [])},
            updated_at=data.get("updated_at", ""),
        )

    def save(self, run_findings: list[Finding]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        entries = []
        for f in run_findings:
            previous = self.findings.get(f.id, {})
            entries.append(
                {
                    "id": f.id,
                    "category": f.category,
                    "severity": f.severity.value,
                    "title": f.title,
                    "found_by": f.found_by,
                    "attack_id": f.attack_id,
                    "first_seen": previous.get("first_seen") or _now(),
                    "last_seen": _now(),
                    "accepted": previous.get("accepted", False),
                }
            )
        self.path.write_text(
            json.dumps(
                {"version": 1, "updated_at": _now(), "findings": sorted(entries, key=lambda e: e["id"])},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        self.findings = {e["id"]: e for e in entries}
        self.updated_at = _now()

    def accept(self, finding_id: str, reason: str = "") -> bool:
        """Record a decision that this finding is accepted, with a reason."""
        if finding_id not in self.findings:
            return False
        entry = self.findings[finding_id]
        entry["accepted"] = True
        entry["accepted_reason"] = reason
        entry["accepted_at"] = _now()
        data = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {"findings": []}
        for f in data["findings"]:
            if f["id"] == finding_id:
                f.update({k: entry[k] for k in ("accepted", "accepted_reason", "accepted_at")})
        data["updated_at"] = self.updated_at or _now()
        self.path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        return True

    def compare(self, findings: list[Finding]) -> dict:
        """Classify this run against the baseline."""
        new, worse, unchanged, fixed = [], [], [], []
        seen = set()
        for f in findings:
            seen.add(f.id)
            previous = self.findings.get(f.id)
            if previous is None:
                new.append(f)
                continue
            previous_severity = Severity.parse(previous["severity"])
            if f.severity.rank > previous_severity.rank:
                worse.append({"finding": f, "was": previous_severity})
            else:
                unchanged.append(f)
        for fid, entry in self.findings.items():
            if fid not in seen and not entry.get("accepted"):
                fixed.append(entry)
        return {
            "new": new,
            "worse": worse,
            "unchanged": unchanged,
            "fixed": fixed,
        }

    def accepted_ids(self) -> set[str]:
        return {fid for fid, e in self.findings.items() if e.get("accepted")}
