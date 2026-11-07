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
EMPIRE = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))


def _banned_file() -> str:
    """The canonical banned list, wherever it lives.

    It moved into DAILY CONTENT during the 2026-11-06 restructure, so the tool
    looks in the canon first and keeps the two older locations as fallbacks for
    anyone running an out-of-date checkout.
    """
    for candidate in (
        os.path.join(EMPIRE, "DAILY CONTENT", "banned_words.txt"),
        os.path.join(EMPIRE, "banned_words.txt"),
        os.path.join(REPO, "banned_words.txt"),
    ):
        if os.path.exists(candidate):
            return candidate
    return os.path.join(REPO, "banned_words.txt")


BANNED_FILE = _banned_file()

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


FENCED_BLOCK = re.compile(r"```.*?```", re.S)
TABLE_ROW = re.compile(r"^\s*\|.*$", re.M)


def strip_code_blocks(text: str) -> str:
    """Drop fenced code and table rows before judging rhythm or spacing.

    An aligned tree or a table is not prose, and a linter that reads column
    alignment as "double space mid-sentence" buries the real findings. Banned
    words are still checked against the whole file, because a banned word in a
    table is still a banned word.
    """
    return TABLE_ROW.sub(" ", FENCED_BLOCK.sub(" ", text))


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
    prose = strip_code_blocks(text)
    for m in re.finditer(rf"[a-z,;]{gap}{{2,}}[a-zA-Z]", prose):
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


# ---------------------------------------------------------------------------
# HUMAN GATE
#
# The banned-word and dash checks catch vocabulary. They do not catch rhythm,
# and rhythm is what makes writing read as machine-made: triads, uniform
# sentence length, the "not X but Y" construction used as a drumbeat, no
# contractions, and sentences that never quite end.
# ---------------------------------------------------------------------------

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")

TRIAD = re.compile(
    r"\b\w[\w'-]*,\s+\w[\w'-]*(?:,\s+\w[\w'-]*)*\s*,?\s+and\s+\w[\w'-]*"
)
NOT_X_BUT_Y = re.compile(
    r"\b(?:it'?s|it is|this is|that'?s|that is)\s+not\s+(?:just\s+|only\s+)?[^.]{3,60}?"
    r"[.,]\s+(?:it'?s|it is|this is|that'?s|that is)\b",
    re.IGNORECASE,
)
HEDGES = re.compile(
    r"\b(quite|very|really|arguably|essentially|basically|actually|simply|clearly)\b",
    re.IGNORECASE,
)
NO_TERMINAL = re.compile(r"[a-zA-Z0-9)\"']\s*$")
MISSING_SPACE_AFTER_COMMA = re.compile(r",[A-Za-z]")
DUP_WORD = re.compile(r"\b(\w+)\s+\1\b", re.IGNORECASE)


FRONT_MATTER = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)


def strip_front_matter(text: str) -> str:
    """Drop the deliverable contract block before linting the prose.

    Front matter is metadata for gate.py, not sentences, so a linter that reads
    it as paragraph one reports a false punctuation error on every gated file.
    """
    return FRONT_MATTER.sub("", text, count=1)


def strip_markdown(text: str) -> str:
    """Keep only prose. Headings, tables, rules, bullets and code are not sentences.

    Two passes. First reflow hard-wrapped lines back onto the block they belong to,
    because a wrapped heading or bullet otherwise arrives here as a stray fragment.
    Then drop the blocks that are not prose.
    """
    # pass 1: reflow, respecting code fences and blank lines
    joined: list[str] = []
    in_fence = False
    for raw in text.split("\n"):
        line = raw.rstrip()
        if line.strip().startswith("```"):
            in_fence = not in_fence
            joined.append(line)
            continue
        if in_fence or not line.strip():
            joined.append(line)
            continue
        is_marker = bool(re.match(r"^\s*(?:#{1,6}\s|[-*+]\s|\d+[.)]\s|\|)", line))
        if not is_marker and joined and joined[-1].strip() and not joined[-1].strip().startswith(("```", "|")):
            joined[-1] = joined[-1] + " " + line.strip()
        else:
            joined.append(line)

    # pass 2: keep prose only
    out: list[str] = []
    in_fence = False
    for line in joined:
        t = line.rstrip()
        if t.strip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence or not t.strip():
            out.append("")
            continue
        if re.match(r"^#{1,6}\s", t.strip()):
            out.append("")
            continue
        if t.strip().startswith("|") or t.strip().startswith("---"):
            out.append("")
            continue
        if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", t):
            out.append("\u00b7 " + re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", t))
        else:
            out.append(t)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


def human_gate(text: str, profile: str = "linkedin") -> dict:
    """Score how machine-made a draft reads, and say which lines to fix.

    Returns {"score": 0-100, "findings": [...], "stats": {...}}. A score of 100
    means no rhythm problems found. It is a smell test, not a verdict: a human
    wrote every rule in here and a human can break every one of them on purpose.
    """
    findings: list[dict] = []
    raw = strip_code_blocks(text)
    body = strip_markdown(raw) if profile in ("doc", "markdown", "email") else raw.strip()
    words = re.findall(r"[A-Za-z']+", body)
    wc = max(len(words), 1)
    per100 = lambda n: round(n * 100.0 / wc, 2)  # noqa: E731

    sentences = [s.strip() for s in SENTENCE_SPLIT.split(body) if s.strip()]
    lengths = [len(re.findall(r"[A-Za-z']+", s)) for s in sentences] or [0]

    stats = {
        "words": len(words),
        "sentences": len(sentences),
        "mean_sentence_words": round(sum(lengths) / max(len(lengths), 1), 1),
        "sentence_length_sd": round(_sd(lengths), 1),
        "contractions": body.count("'"),
        "hedges": len(HEDGES.findall(body)),
        "triads": len([m for m in TRIAD.findall(body) if not re.search(r"\d", m)]),
        "not_x_but_y": len(NOT_X_BUT_Y.findall(body)),
    }

    # 1. Triads used as a drumbeat. One is style, three is a tic.
    triads = [m for m in TRIAD.findall(body) if not re.search(r"\d", m)]
    if len(triads) >= 3:
        findings.append({
            "severity": "warning",
            "message": f"{len(triads)} three-part lists. One reads human, three read like a template.",
        })

    # 2. The "it's not X, it's Y" construction on repeat.
    if stats["not_x_but_y"] >= 3:
        findings.append({
            "severity": "warning",
            "message": f"{stats['not_x_but_y']}x the \"not X, it's Y\" turn. Keep the best one, cut the rest.",
        })

    # 3. Uniform sentence length is the loudest tell in a paragraph of plain prose.
    if len(sentences) >= 6 and stats["sentence_length_sd"] < 3.5:
        findings.append({
            "severity": "warning",
            "message": (
                f"sentence length barely varies (sd {stats['sentence_length_sd']} words). "
                "Put a two-word sentence next to a thirty-word one."
            ),
        })

    # 4. No contractions at all reads stiff, and is easy to fix.
    if profile in ("linkedin", "email") and stats["contractions"] == 0 and wc > 40:
        findings.append({
            "severity": "warning",
            "message": "not one contraction in the whole piece. Nobody talks like that.",
        })

    # 5. Hedges dilute a claim into an opinion.
    if stats["hedges"] >= 4:
        findings.append({
            "severity": "warning",
            "message": f"{stats['hedges']} hedge words. Cut them and the claim gets stronger, not ruder.",
        })

    # 6. A paragraph that never ends in punctuation is usually a paste error.
    # A fenced block is code, and a code block with a blank line inside it used to arrive here as
    # two paragraphs of prose. Swap each block for a neutral sentence before numbering paragraphs.
    checked = re.sub(r"```.*?```", "Code block.", body, flags=re.S)
    paragraphs = [p.strip() for p in checked.split("\n\n") if p.strip()]
    for i, para in enumerate(paragraphs, 1):
        tail = para.rstrip()
        # a bold-only label such as **INTERACTIVE, 56 words** is metadata, not a sentence
        if re.fullmatch(r"\*\*.+\*\*", para):
            continue
        # a heading is a label, not a sentence
        if re.fullmatch(r"#{1,6}\s.*", para):
            continue
        # a horizontal rule is a rule
        if re.fullmatch(r"[-*_]{3,}", para):
            continue
        # a markdown table is a table, whatever the profile
        rows = [line.strip() for line in para.split("\n") if line.strip()]
        if rows and all(line.startswith("|") for line in rows):
            continue
        # an HTML comment is a build marker, not prose
        if re.fullmatch(r"(?:<!--.*?-->\s*)+", para, re.S):
            continue
        # a list item, and any paragraph containing one, is fragments, not sentences
        if "\u00b7" in para:
            continue
        # a hashtag or mention line is not a sentence and needs no full stop
        if re.fullmatch(r"[\s#@\w&,'-]+", para) and para.lstrip().startswith(("#", "@")):
            continue
        # a salutation is a greeting, not a sentence: "Evelyne-Claudia," is correct
        if re.fullmatch(r"(?:hi|hey|hello|dear)?[\s,]*[\w' .-]{1,40},", para.strip(), re.I):
            continue
        # a sign-off is a signature, not a sentence, and only the last paragraph can be one,
        # which is what stops this from excusing a fragment in the middle of a document.
        if para is paragraphs[-1]:
            if re.fullmatch(r"[A-Z][\w'.-]*(?:\s+[A-Z][\w'.-]*){0,2}", para):
                continue
            if re.fullmatch(r"(?:with\s+)?(?:my\s+)?(?:best|warm|warmest|kind)\s+regards\s*,?\s*"
                            r"[A-Z][\w'.-]*(?:\s+[A-Z][\w'.-]*){0,2}", para, re.I):
                continue
        if tail and not re.search(r"[.!?:;)\"'#`]$", tail):
            findings.append({
                "severity": "error",
                "message": f"paragraph {i} has no terminal punctuation: ...{tail[-40:]!r}",
            })

    # 7. Mechanical punctuation slips.
    for m in MISSING_SPACE_AFTER_COMMA.finditer(body):
        findings.append({
            "severity": "warning",
            "message": f"missing space after a comma near {m.group(0)!r}",
        })
    for m in DUP_WORD.finditer(body):
        if m.group(1).lower() not in ("had", "that"):
            findings.append({
                "severity": "warning",
                "message": f"doubled word: {m.group(0)!r}",
            })

    # 8. Repeated sentence openers.
    openers = [s.split()[0].lower() for s in sentences if s.split()]
    ceiling = max(3, int(wc / 120))  # a long memo legitimately leans on "The"
    for w in set(openers):
        n = openers.count(w)
        if n > ceiling and w in ("the", "this", "it", "that", "there"):
            findings.append({
                "severity": "warning",
                "message": f"{n} sentences open with {w!r}. Vary the entry.",
            })

    return {"findings": findings, "stats": stats}


def score_findings(findings: list[dict]) -> int:
    """One score across every finding, so vocabulary and rhythm cannot cancel out."""
    errors = sum(1 for f in findings if f["severity"] == "error")
    return max(0, 100 - errors * 25 - (len(findings) - errors) * 8)


def _sd(values: list[int]) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5


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
        if "offset" in f:
            where = f"line {line_of(text, f['offset'])}"
        else:
            where = "whole piece"
        print(f"  {tag}  {where:>10}  {f['message']}")
    return len(errs)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Lint text against this repo's voice rules.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--profile", choices=["linkedin", "doc", "email", "markdown"], default="linkedin")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--human", action="store_true", help="add the rhythm and punctuation gate")
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
        text = strip_front_matter(text)
        findings = lint_text(text, args.profile, banned)
        gate = None
        if args.human:
            gate = human_gate(text, args.profile)
            findings.extend(gate["findings"])
            findings.sort(key=lambda f: f.get("offset", 0))
        if args.strict:
            for f in findings:
                f["severity"] = "error"
        total_errors += report(path, text, findings)
        if gate:
            s = gate["stats"]
            score = score_findings(findings)
            print(
                f"  human gate: {score}/100 | {s['words']} words, "
                f"{s['sentences']} sentences, mean {s['mean_sentence_words']}w, "
                f"sd {s['sentence_length_sd']}, {s['contractions']} contractions, "
                f"{s['hedges']} hedges, {s['triads']} triads, {s['not_x_but_y']} not-X-but-Y"
            )
        payload.append({"file": path, "profile": args.profile, "findings": findings, "human_gate": gate})

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))

    print(f"\n{len(args.files)} file(s) checked, {len(banned)} banned phrases loaded, profile={args.profile}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
