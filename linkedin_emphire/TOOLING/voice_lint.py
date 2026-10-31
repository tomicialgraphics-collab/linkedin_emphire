#!/usr/bin/env python3
"""voice_lint.py - check any draft against this repo's own voice rules.

The rules are already written down in the repo, they were just never enforced
by anything but a careful read:

  * banned_words.txt  -> the "WORDS I NEVER USE" list (84 entries)
  * context.md s7     -> no em dashes in any owner-facing content
  * context.md s8     -> signature lines, plain tone

Usage
-----
    python3 voice_lint.py <file> [<file> ...]
    python3 voice_lint.py linkedin_emphire/APPLICATIONS/.../letter.txt
    python3 voice_lint.py --profile doc RESUME/x.txt
    python3 voice_lint.py --strict draft.md      # banned words become errors
    python3 voice_lint.py --json draft.md        # machine readable

Profiles
--------
    linkedin  default. The banned list is taken literally: every hit is an error.
    doc       resumes, letters, technical docs. Same list, but the technical
              exceptions below are allowed, because the word is the correct
              name for the thing and a recruiter expects it.
    email     like doc, plus a few email conventions.

Exit codes
----------
    0  clean (or warnings only, unless --strict)
    1  at least one error
    2  could not read input
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
BANNED_FILE = os.path.join(REPO, "banned_words.txt")

# Words that exist in banned_words.txt because they are AI slop on LinkedIn, but
# which are the correct technical term inside a resume or an email to a research
# org. Allowed under --profile doc/email, flagged under linkedin.
TECHNICAL_EXCEPTIONS = {
    "harness",
    "comprehensive",
    "robust",
    "navigate",
    "streamline",
}

# Extra tells that are not in banned_words.txt but read as machine-written.
EXTRA_TELLS = [
    (r"in today[\u2019']s fast[- ]paced", "stock AI opener"),
    (r"it(?:[\u2019']s| is) important to note", "filler hedge"),
    (r"\bmoreover\b", "essay connective"),
    (r"\bit is worth noting\b", "filler hedge"),
    (r"\bi hope this (email |message )?finds you well\b", "stock email opener"),
    (r"\bplease do not hesitate\b", "stock email closer"),
    (r"\bthank you for your time and consideration\b", "stock email closer"),
    (r"\bas an ai language model\b", "self-reference"),
]

# Hard rule from context.md s7: no em dashes, no en dashes.
DASH_PATTERNS = [
    ("\u2014", "em dash (banned by standing rule)"),
    ("\u2013", "en dash (banned by standing rule)"),
    ("\u2015", "horizontal bar (banned by standing rule)"),
]


def load_banned(path: str = BANNED_FILE) -> list[tuple[str, str]]:
    """Return [(regex, display_phrase)] from the ❌ lines in banned_words.txt."""
    if not os.path.exists(path):
        return []
    raw = open(path, encoding="utf-8", errors="replace").read()
    phrases = re.findall(r'\u274c\s*"([^"]+)"', raw)

    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for phrase in phrases:
        p = phrase.strip().strip('"').strip()
        p = p.rstrip(".").rstrip(":").strip()
        if not p:
            continue
        variants = [v.strip() for v in p.split("/") if v.strip()]
        for v in variants:
            v = re.sub(r"\[[^\]]+\]", r"\\w+", v)
            low = v.lower()
            if low in seen:
                continue
            seen.add(low)
            parts = v.split()
            if len(parts) == 1 and re.fullmatch(r"[\w\\+]+", v):
                pattern = r"\b" + re.escape(v).replace("\\\\w", r"\w+") + r"\b"
            else:
                escaped = re.escape(v).replace(r"\\w\+", r"\w+")
                pattern = r"\b" + escaped + r"\b"
            out.append((pattern, phrase.strip()))
    return out


def lint_text(text: str, profile: str, banned: list[tuple[str, str]]) -> list[dict]:
    findings: list[dict] = []
    strict_banned = profile == "linkedin"
    allow = set() if profile == "linkedin" else TECHNICAL_EXCEPTIONS

    for pattern, display in banned:
        if display.lower().strip() in allow:
            continue
        for m in re.finditer(pattern, text, re.IGNORECASE):
            low = m.group(0).lower()
            if low in allow:
                continue
            findings.append(
                {
                    "kind": "banned_word",
                    "severity": "error" if strict_banned else "warning",
                    "message": f'banned phrase: "{display}"',
                    "match": m.group(0),
                    "offset": m.start(),
                }
            )

    for tell, why in EXTRA_TELLS:
        for m in re.finditer(tell, text, re.IGNORECASE):
            findings.append(
                {
                    "kind": "ai_tell",
                    "severity": "warning",
                    "message": f"{why}: \"{m.group(0)}\"",
                    "match": m.group(0),
                    "offset": m.start(),
                }
            )

    for ch, why in DASH_PATTERNS:
        if ch in text:
            for m in re.finditer(re.escape(ch), text):
                findings.append(
                    {
                        "kind": "dash",
                        "severity": "error",
                        "message": why,
                        "match": ch,
                        "offset": m.start(),
                    }
                )

    # Straight quotes are fine; curly quotes inside a plain-text .eml will render
    # as mojibake in some clients, so surface them for email drafts only.
    if profile == "email":
        for ch, why in [("\u2019", "curly apostrophe"), ("\u201c", "curly quote")]:
            n = text.count(ch)
            if n:
                findings.append(
                    {
                        "kind": "encoding",
                        "severity": "warning",
                        "message": f"{n}x {why} (renders as mojibake in plain-text email)",
                        "match": ch,
                        "offset": text.find(ch),
                    }
                )

    # double space mid-sentence, a small copy-editing tell
    gap = r"[^\S\n]"  # spaces and tabs, never a newline
    for m in re.finditer(rf"[a-z,;]{gap}{{2,}}[a-zA-Z]", text):
        findings.append(
            {
                "kind": "spacing",
                "severity": "warning",
                "message": "double space mid-sentence",
                "match": m.group(0),
                "offset": m.start(),
            }
        )

    findings.sort(key=lambda f: (f["offset"], f["kind"]))
    return findings


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def report(path: str, text: str, findings: list[dict]) -> int:
    errs = [f for f in findings if f["severity"] == "error"]
    warns = [f for f in findings if f["severity"] != "error"]
    print(f"\n{path}")
    print(f"  {len(text.split())} words, {len(errs)} error(s), {len(warns)} warning(s)")
    if not findings:
        print("  clean")
        return 0
    for f in findings:
        tag = "ERROR" if f["severity"] == "error" else " warn"
        where = f"line {line_of(text, f['offset'])}"
        print(f"  {tag}  {where:>10}  {f['message']}")
    return len(errs)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Lint text against this repo's voice rules.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--profile", choices=["linkedin", "doc", "email"], default="linkedin")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--json", action="store_true", help="machine readable output")
    ap.add_argument("--banned-file", default=BANNED_FILE)
    args = ap.parse_args(argv)

    banned = load_banned(args.banned_file)
    if not banned:
        print(f"voice_lint: warning: no banned phrases loaded from {args.banned_file}", file=sys.stderr)

    total_errors = 0
    payload = []
    for path in args.files:
        try:
            text = open(path, encoding="utf-8").read()
        except OSError as exc:
            print(f"voice_lint: cannot read {path}: {exc}", file=sys.stderr)
            return 2
        findings = lint_text(text, args.profile, banned)
        if args.strict:
            for f in findings:
                f["severity"] = "error"
        total_errors += report(path, text, findings)
        payload.append({"file": path, "profile": args.profile, "findings": findings})

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))

    print(f"\n{len(args.files)} file(s) checked, {len(banned)} banned phrases loaded, profile={args.profile}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
