"""Findings: the unit the gate reasons about.

A test result is not a finding. Three tools reporting the same weakness
is one finding that three tools found, and a gate that fails three times
for one bug teaches people to ignore the gate.

The identity of a finding is its fingerprint: category plus the
normalised evidence that proves it. Nothing else. Run id, timestamp,
tool, model version and latency are all excluded on purpose, because a
fingerprint that changes when the clock changes cannot be compared to a
baseline.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum

from .hashing import sha256_text


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    @property
    def rank(self) -> int:
        return {"critical": 4, "high": 3, "medium": 2, "low": 1}[self.value]

    @classmethod
    def parse(cls, value: str) -> Severity:
        try:
            return cls(value.strip().lower())
        except ValueError:
            raise ValueError(
                f"unknown severity {value!r}; use one of {[s.value for s in cls]}"
            ) from None


CATEGORIES = {
    "prompt-injection": "instructions in content the agent reads are followed",
    "system-prompt-leak": "the agent discloses its instructions",
    "tool-misuse": "the agent takes a privileged action it should route to a human",
    "data-exfiltration": "the agent sends data to a destination outside the account",
    "encoding-bypass": "an encoded payload reaches the same behaviour as plain text",
    "multi-turn-escalation": "a sequence of allowed turns ends in a disallowed action",
}


@dataclass
class Evidence:
    """What the finding is based on, in enough detail to re-check by hand."""
    prompt: str
    response: str
    actions: list[str] = field(default_factory=list)

    def excerpt(self, limit: int = 240) -> str:
        text = self.response.strip().replace("\n", " ")
        return text if len(text) <= limit else text[:limit] + "..."


@dataclass
class Finding:
    category: str
    severity: Severity
    title: str
    evidence: Evidence
    found_by: list[str] = field(default_factory=list)
    attack_id: str = ""
    turns: int = 1
    first_seen: str = ""
    last_seen: str = ""

    @property
    def fingerprint(self) -> str:
        """Stable identity: category plus the evidence signature.

        The signature is the canary-bearing part of the response with
        digits and whitespace stripped, so a different run of the same
        weakness collapses onto the same finding and a genuinely new
        behaviour does not.
        """
        signature = _signature(self.evidence.response, self.evidence.actions)
        return sha256_text(f"{self.category}\u0000{signature}")[:16]

    @property
    def id(self) -> str:
        return f"{self.category}/{self.fingerprint}"

    def merged_with(self, other: Finding) -> Finding:
        tools = sorted({*self.found_by, *other.found_by})
        return Finding(
            category=self.category,
            severity=self.severity if self.severity.rank >= other.severity.rank else other.severity,
            title=self.title if len(self.title) >= len(other.title) else other.title,
            evidence=self.evidence,
            found_by=tools,
            attack_id=self.attack_id or other.attack_id,
            turns=max(self.turns, other.turns),
            first_seen=min(filter(None, [self.first_seen, other.first_seen]), default=""),
            last_seen=max(filter(None, [self.last_seen, other.last_seen]), default=""),
        )


_CANARY = re.compile(r"[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+")


def _signature(response: str, actions: list[str] | None = None) -> str:
    """Name the behaviour, in order of how little it can drift.

    A canary is the strongest: the agent minted it. An action is next: two
    runs that both emailed the same address did the same thing, whatever the
    model said in prose that day, which matters as soon as the target is a
    model rather than a rule engine. Free text is the last resort.
    """
    canaries = _CANARY.findall(response or "")
    if canaries:
        return "|".join(sorted(set(canaries)))
    if actions:
        # subject and similar free-text arguments change with the wording;
        # the tool, the target and the shape of the call do not
        stable = {
            re.sub(r"\bsubject=[^,)]*", "subject=*", a).strip()
            for a in actions
            if a.strip()
        }
        if stable:
            joined = "|".join(sorted(stable))
            return re.sub(r"\d+", "#", joined)[:120]
    normalised = re.sub(r"\d+", "#", (response or "").lower())
    # punctuation and spacing are cosmetic: a comma added to a sentence
    # must not mint a new finding and orphan the baseline entry
    normalised = re.sub(r"[^\w\s#]", "", normalised)
    normalised = re.sub(r"\s+", " ", normalised).strip()
    return normalised[:120]


def dedupe(findings: list[Finding]) -> list[Finding]:
    """Collapse duplicates by fingerprint, keeping the union of tools."""
    merged: dict[str, Finding] = {}
    for f in findings:
        if f.id in merged:
            merged[f.id] = merged[f.id].merged_with(f)
        else:
            merged[f.id] = f
    return sorted(merged.values(), key=lambda f: (-f.severity.rank, f.category, f.id))
