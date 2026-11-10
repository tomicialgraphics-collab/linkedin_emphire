#!/usr/bin/env python3
"""gate.py - the one command that decides whether a file may leave this repo.

Every rule in PIPELINE/registry/rules.json with a `check` is enforced here. The
gate does not invent rules. If a rule is not in the registry it is not checked,
and if it is in the registry with `severity: manual` a human has to say so out
loud in the delivery log.

Usage
-----
    python3 TOOLING/gate.py <file> [<file> ...]
    python3 TOOLING/gate.py --profile post VERIFIED_POSTS/2026-11-06_x/post.md
    python3 TOOLING/gate.py --json <file>
    python3 TOOLING/gate.py --quiet <file>          # only failures
    python3 TOOLING/gate.py --strict <file>         # warnings become failures

Exit codes
----------
    0  no failures (warnings may exist)
    1  at least one blocking failure
    2  the file could not be read

What the gate cannot see, and never pretends to: whether the argument is any
good, whether the profile read was real, whether the box passes the portability
test. Those are marked `manual` in the registry for a reason.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EMPIRE = os.path.abspath(os.path.join(HERE, ".."))            # linkedin_emphire/
ROOT = os.path.abspath(os.path.join(EMPIRE, ".."))            # git root
REGISTRY = os.path.join(EMPIRE, "PIPELINE", "registry")

STATUS_ORDER = {"FAIL": 0, "WARN": 1, "PASS": 2, "SKIP": 3}


# --------------------------------------------------------------------------
# registry
# --------------------------------------------------------------------------

def load_json(name: str) -> dict:
    path = os.path.join(REGISTRY, name)
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


RULES = load_json("rules.json")
TEMPLATES = load_json("templates.json")
HASHTAGS = load_json("hashtags.json")

RULE_BY_ID = {r["id"]: r for r in RULES.get("rules", [])}
TEMPLATE_IDS = {t["id"].upper() for t in TEMPLATES.get("templates", [])}
VERIFIED_TAGS = {h["tag"].lower() for h in HASHTAGS.get("verified", [])}
BLOCKED_TAGS = {h["tag"].lower(): h.get("reason", "") for h in HASHTAGS.get("blocked", [])}

OUTBOUND_AUDIENCES = {"public", "client", "reviewer", "hiring", "vendor"}


# --------------------------------------------------------------------------
# voice_lint plumbing
# --------------------------------------------------------------------------

def _voice_lint():
    path = os.path.join(HERE, "voice_lint.py")
    spec = importlib.util.spec_from_file_location("voice_lint", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


VL = _voice_lint()


def banned_path() -> str:
    """The canonical banned list, wherever it currently lives."""
    for candidate in (
        os.path.join(EMPIRE, "DAILY CONTENT", "banned_words.txt"),
        os.path.join(ROOT, "banned_words.txt"),
        os.path.join(EMPIRE, "banned_words.txt"),
    ):
        if os.path.exists(candidate):
            return candidate
    return os.path.join(ROOT, "banned_words.txt")


# --------------------------------------------------------------------------
# front matter
# --------------------------------------------------------------------------

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Tiny YAML subset: `key: value`, `key: [a, b]`, `key: "quoted"`, comments."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for raw in m.group(1).splitlines():
        # Full-line comments only. A "#" inside a value is a hashtag, not a comment.
        if not raw.strip() or raw.lstrip().startswith("#") or ":" not in raw:
            continue
        line = raw.rstrip()
        key, _, val = line.partition(":")
        key = key.strip().lower()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip("\"'") for v in val[1:-1].split(",")]
            meta[key] = [v for v in items if v]
        elif val.lower() in ("true", "yes"):
            meta[key] = True
        elif val.lower() in ("false", "no"):
            meta[key] = False
        else:
            meta[key] = val.strip("\"'")
    return meta, text[m.end():]


def infer_type(path: str, meta: dict) -> str:
    if meta.get("deliverable"):
        return str(meta["deliverable"]).lower()
    p = path.replace(os.sep, "/").lower()
    if "/verified_posts/" in p and p.endswith("post.md"):
        return "post"
    if "/engagement/" in p and "draft" in p:
        return "comment"
    if "/session_log/" in p or "/state/" in p:
        return "internal"
    if p.endswith(".md") and ("review" in p or "scope" in p or "findings" in p or "report" in p):
        return "doc"
    return "doc"


def infer_audience(path: str, meta: dict) -> str:
    if meta.get("audience"):
        return str(meta["audience"]).lower()
    p = path.replace(os.sep, "/").lower()
    if "/session_log/" in p or "/state/" in p or "/archive/" in p:
        return "internal"
    if "/clients/" in p or "/projects/" in p or "/outreach/" in p:
        return "client"
    if "/verified_posts/" in p or "/engagement/" in p:
        return "public"
    return "internal"


def lint_profile(dtype: str, audience: str) -> str:
    if dtype == "post" or audience == "public":
        return "linkedin"
    if dtype in ("dm", "email"):
        return "email"
    return "doc"


# --------------------------------------------------------------------------
# post body extraction
# --------------------------------------------------------------------------

BODY_START = "<!-- gate:body:start -->"
BODY_END = "<!-- gate:body:end -->"
PASTE_HEADING = re.compile(r"^##+\s*(post,?\s*paste-ready|paste-ready|the post)\s*$", re.I | re.M)


PASTE_REGION = re.compile(
    r"^##+\s*(?:the\s+)?(?:comment|reply|dm|message|post)[^\n]*\b(?:paste[^\n]*|send[^\n]*this[^\n]*)\s*$",
    re.I | re.M,
)


def paste_region(text: str) -> str:
    """The lines a human copies out, when the file says where they are.

    Comment files carry working notes next to the comment. Those notes are allowed
    to name files, paths and dates, because nobody pastes them. This returns the
    marked region when a file has one, and the whole text when it does not, which
    is the safe direction: a bare draft is treated as all paste.
    """
    m = PASTE_REGION.search(text)
    if not m:
        return text
    rest = text[m.end():]
    nxt = re.search(r"^##\s", rest, re.M)
    return (rest[: nxt.start()] if nxt else rest).strip()


def post_body(text: str) -> str:
    """The part of a post file that actually gets pasted into LinkedIn.

    A post file is allowed to carry working notes around the post: alternatives,
    the card copy, the hashtag justification, the first comment. The gate measures
    the post, so it needs to know where the post starts and stops.

    Explicit markers win. Otherwise a "paste-ready" heading is used, and the body
    runs to the next level-two heading. If neither exists, the whole file is the
    post, which is the right default for a bare draft.
    """
    if BODY_START in text and BODY_END in text:
        return text.split(BODY_START, 1)[1].split(BODY_END, 1)[0].strip()
    m = PASTE_HEADING.search(text)
    if m:
        rest = text[m.end():]
        nxt = re.search(r"^##\s", rest, re.M)
        return (rest[: nxt.start()] if nxt else rest).strip()
    return text.strip()


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------

class Report:
    def __init__(self, path: str):
        self.path = path
        self.rows: list[dict] = []

    def add(self, rule_id: str, status: str, detail: str = ""):
        rule = RULE_BY_ID.get(rule_id, {})
        self.rows.append(
            {
                "rule": rule_id,
                "status": status,
                "detail": detail,
                "text": rule.get("text", ""),
                "severity": rule.get("severity", "block"),
            }
        )

    @property
    def failed(self) -> list[dict]:
        return [r for r in self.rows if r["status"] == "FAIL"]

    @property
    def warned(self) -> list[dict]:
        return [r for r in self.rows if r["status"] == "WARN"]


def body_words(text: str) -> int:
    return len(re.findall(r"[A-Za-z']+", text))


def check_text(rep: Report, body: str, meta: dict, dtype: str, audience: str,
               pasted: str | None = None, exported: bool = False, path: str = "") -> None:
    pasted = pasted if pasted is not None else body
    # R01 em dash
    dashes = [i for i, ch in enumerate(body) if ch in "\u2014\u2013"]
    spaced_double = re.findall(r"\s--\s", body)
    if dashes or spaced_double:
        where = ", ".join(str(n) for n in [x + 1 for x in dashes[:5]])
        rep.add("R01", "FAIL", f"{len(dashes)} em/en dash(es) at char {where or 'n/a'}; {len(spaced_double)} spaced double hyphen(s)")
    else:
        rep.add("R01", "PASS", "0 em dashes")

    # R02 banned words
    profile = lint_profile(dtype, audience)
    banned = VL.load_banned(banned_path())
    findings = VL.lint_text(body, profile, banned)
    words = [f for f in findings if f["kind"] == "banned_word" and f["severity"] == "error"]
    if words:
        seen = sorted({f["match"] for f in words})
        rep.add("R02", "FAIL", f"{len(words)} hit(s): " + ", ".join(seen[:8]))
    else:
        warns = [f for f in findings if f["kind"] == "banned_word"]
        rep.add("R02", "PASS" if not warns else "WARN",
                "0 hits" if not warns else f"{len(warns)} allowed-by-profile hit(s)")

    # R03 identity leak
    leaks = [m.start() for m in re.finditer(r"tomicial", body, re.I)]
    if leaks:
        status = "FAIL" if audience in OUTBOUND_AUDIENCES else "WARN"
        rep.add("R03", status, f"{len(leaks)} mention(s) of the retired identity; outward files must carry none")
    else:
        rep.add("R03", "PASS", "clean")

    # R04 outbound address
    emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", body))
    bad = {e for e in emails if "tomicial" in e.lower()}
    if bad:
        rep.add("R04", "FAIL", "retired address present: " + ", ".join(sorted(bad)))
    else:
        rep.add("R04", "PASS", "only approved address" if emails else "no address in file")

    # R05 local paths
    local = re.findall(r"(?:[A-Za-z]:\\\\?Users|[A-Za-z]:\\\\?(?:Users|Desktop)|file:///|/home/user/|~/\.)", body)
    if local:
        status = "FAIL" if audience in OUTBOUND_AUDIENCES or dtype in ("doc", "post", "email", "dm") else "WARN"
        rep.add("R05", status, f"{len(local)} local path(s): " + ", ".join(sorted(set(local))[:4]))
    else:
        rep.add("R05", "PASS", "no local paths")

    # R14 voice gate
    human = VL.human_gate(pasted, profile)
    score = VL.score_findings(findings + human["findings"])
    errs = [f for f in findings + human["findings"] if f["severity"] == "error"]
    if dtype == "internal":
        rep.add("R14", "SKIP", f"human {score}/100, internal file")
    elif errs:
        rep.add("R14", "FAIL", f"human {score}/100, {len(errs)} error(s)")
    elif score < 90:
        rep.add("R14", "FAIL", f"human {score}/100, below the 90 floor: " + "; ".join(f["message"] for f in human["findings"][:3]))
    else:
        rep.add("R14", "PASS", f"human {score}/100, 0 errors, {body_words(pasted)}w")

    # R15 ending on a statement
    tail = [l.strip() for l in pasted.splitlines() if l.strip() and not l.strip().startswith("#")]
    if tail and tail[-1].endswith("?"):
        rep.add("R15", "WARN", "ends on a question; end on a statement")
    else:
        rep.add("R15", "PASS", "ends on a statement")

    # R20 overclaim
    over = re.findall(r"\b(?:is|are|has been|was|fully) (?:now )?fixed\b|\bresolved the (?:defect|issue|bug)\b|\bfully resolved\b", body, re.I)
    if exported:
        # A review artefact describes the author's fix in the author's terms and
        # carries no front matter to mark it verified. The honest status wording
        # lives in the text ("merged at <sha>, pending an independent run"), so
        # this check cannot read it and does not pretend to.
        rep.add("R20", "PASS", "exported artefact, fix status stated in the text")
    elif over:
        status = "FAIL" if meta.get("fix_verified") not in (True, "true") else "PASS"
        rep.add("R20", status, f"{len(over)} fix claim(s); mark fix_verified: true only with the post-fix run attached")
    else:
        rep.add("R20", "PASS", "no fix claim")

    # R24 PII
    phone = re.findall(r"\+\d{1,3}[\s\d]{7,}\d", body)
    if phone:
        rep.add("R24", "WARN", f"{len(phone)} phone number(s); only where the owner intends it")
    else:
        rep.add("R24", "PASS", "no phone number")

    # R32 a filename typed into pasted text autolinks to a dead address
    if dtype in ("post", "comment", "dm"):
        region = paste_region(pasted)
        dotted = re.findall(
            r"(?<![\w/.:-])[\w][\w-]*\.(?:zip|md|json|txt|pdf|docx|xlsx|csv|png|jpg|py|sh|ps1)(?![\w])",
            region,
        )
        if dotted:
            status = "FAIL" if str(meta.get("date", "")) >= "2026-11-10" else "WARN"
            rep.add("R32", status, "filename with an extension in the pasted text, which autolinks to a dead address: "
                                   + ", ".join(sorted(set(dotted))[:4]) + ". Name it without the extension.")
        else:
            rep.add("R32", "PASS", "no dotted filenames in the pasted text")

    # R40 a post carries a real number, or says why it carries none
    if dtype == "post":
        if not re.search(r"\d", pasted):
            rep.add("R40", "WARN", "no number anywhere in the post: add one from a run you actually have, "
                                   "or say in the text why the post has none")
        else:
            rep.add("R40", "PASS", "carries a number")

    # R43 a case study carries its client permission
    if "CASE-STUDY" in path.upper() and "PIPELINE" not in path.upper():
        perm = str(meta.get("permission", "")).strip().lower()
        state = str(meta.get("status", "")).strip().lower()
        if not perm:
            rep.add("R43", "FAIL", "case study without permission: in front matter")
        elif perm.startswith("granted"):
            rep.add("R43", "PASS", f"permission {perm.split(':')[0]}: client agreed")
        elif state in ("draft", ""):
            rep.add("R43", "PASS", f"permission {perm}: drafting is allowed before the ask")
        else:
            rep.add("R43", "FAIL", f"permission {perm} but status {state}: nothing leaves until the client agrees in writing")

    # R30 relative dates
    if dtype != "internal":
        rel = re.findall(r"\b(?:yesterday|last week|last night|this morning|tomorrow)\b", body, re.I)
        if rel:
            rep.add("R30", "WARN", f"{len(rel)} relative date(s); name the day")
        else:
            rep.add("R30", "PASS", "no relative dates")


def check_contract(rep: Report, meta: dict, dtype: str, audience: str, path: str) -> None:
    required = ["deliverable", "id", "date", "audience", "status"]
    if dtype == "post":
        required += ["template", "headline", "subheadline", "box", "hashtags"]
    if dtype in ("comment", "dm"):
        required += ["profile_checked"]
    missing = [k for k in required if not meta.get(k)]
    if missing:
        status = "FAIL" if audience in OUTBOUND_AUDIENCES or dtype in ("post", "comment", "dm") else "WARN"
        rep.add("R26", status, "missing front-matter: " + ", ".join(missing))
    else:
        rep.add("R26", "PASS", f"{dtype} contract complete")

    if meta.get("status") and str(meta["status"]).lower() not in (
        "draft", "ready", "sent", "posted", "superseded", "archived", "frozen"
    ):
        rep.add("R26", "WARN", f"status '{meta['status']}' is not one of draft/ready/sent/posted")

    # R26 linked material. A comment on somebody else's post is written about material
    # that post points at. Saying whether that material was opened is the difference
    # between a reading and a reaction, so the file states it from 2026-11-10 onward.
    # Nothing before that date is retro-fitted: the values would be reconstruction.
    if dtype in ("comment", "dm") and str(meta.get("date", "")) >= "2026-11-10":
        prem = str(meta.get("premise_checked", "")).strip()
        if not prem:
            rep.add("R33", "FAIL", "missing premise_checked: name the fact the post rests on and the day it was checked, "
                                   "or opinion: when the post makes no checkable claim")
        elif not prem.lower().startswith(("checked:", "stable:", "opinion:")):
            rep.add("R33", "WARN", "premise_checked must open with checked:, stable: or opinion:")
        elif prem.lower().startswith("checked:") and len(prem.split()) < 4:
            rep.add("R33", "WARN", "checked: names the claim, where it was checked, and the date")
        else:
            rep.add("R33", "PASS", "premise accounted for")

    if dtype in ("comment", "dm") and str(meta.get("date", "")) >= "2026-11-10":
        src = str(meta.get("sources_read", "")).strip()
        if not src:
            rep.add("R26", "FAIL", "missing sources_read: name the linked material and whether it was opened, "
                                   "or none: nothing attached")
        elif src.lower().startswith("not-needed"):
            rep.add("R26", "FAIL", "not-needed is retired (owner instruction 2026-11-09): open it and say what it was, "
                                   "or blocked: if it will not open")
        elif not src.lower().startswith(("read:", "none:", "blocked:")):
            rep.add("R26", "WARN", "sources_read must open with read:, none: or blocked:")
        elif src.lower().startswith("blocked:") and len(src.split()) < 8:
            rep.add("R26", "WARN", "blocked: states the reason, then what the comment claims without it")
        elif src.lower().startswith("read:") and len(src.split()) < 4:
            rep.add("R26", "WARN", "read: names what was opened and the date")
        else:
            rep.add("R26", "PASS", "linked material accounted for")


def check_post(rep: Report, meta: dict, body: str) -> None:
    headline = str(meta.get("headline", "")).strip()
    sub = str(meta.get("subheadline", "")).strip()
    box = str(meta.get("box", "")).strip()

    # R07 the pair and the alternatives
    alts = [k for k in ("headline_alt", "headline_alt2") if meta.get(k)]
    if headline and sub and len(alts) >= 2:
        rep.add("R07", "PASS", "pair + 2 alternative pairs")
    elif headline and sub:
        rep.add("R07", "FAIL", f"pair present but {2 - len(alts)} alternative pair(s) missing")
    else:
        rep.add("R07", "FAIL", "headline and subheadline required")

    # R08 first line
    first = ""
    for line in body.splitlines():
        if line.strip():
            first = line.strip()
            break
    if not headline:
        rep.add("R08", "SKIP", "no headline declared")
    else:
        issues = []
        if len(headline) > 120:
            issues.append(f"{len(headline)} chars, limit 120")
        if "?" in headline:
            issues.append("headline is a question")
        if re.match(r"^(i|we|my|our)\b", headline, re.I):
            issues.append("opens with a first person pronoun")
        if issues:
            rep.add("R08", "FAIL", "; ".join(issues))
        elif first and first != headline and not meta.get("first_line_override"):
            rep.add("R08", "WARN", "body does not open on the declared headline")
        else:
            rep.add("R08", "PASS", f"{len(headline)} chars, statement, opens the body")

    # R09 pair inside 200
    if headline and sub:
        total = len(headline) + len(sub)
        rep.add("R09", "PASS" if total <= 200 else "FAIL", f"pair {total} chars, limit 200")
    else:
        rep.add("R09", "SKIP", "no pair to measure")

    # R10 box
    if not box:
        rep.add("R10", "FAIL", "no boxed phrase")
    else:
        n = len(box.split())
        problems = []
        if not 1 <= n <= 3:
            problems.append(f"{n} words, allowed 1-3")
        # The spec bans a box that opens line one or repeats the headline verbatim.
        # A box that reinforces a phrase inside the headline is allowed, and the
        # 6 November post is the reason: it boxes the phrase the review misuses.
        if headline and box.lower().strip(" .") == headline.lower().strip(" ."):
            problems.append("box repeats the headline; it must add something")
        if headline and headline.lower().startswith(box.lower()):
            problems.append("box opens line one")
        if not meta.get("box_alt"):
            problems.append("no alternative box")
        rep.add("R10", "FAIL" if problems else "PASS", "; ".join(problems) or f"'{box}', alternative given")

    # R12 hashtags
    tags = meta.get("hashtags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split() if t.strip()]
    problems = []
    if not 3 <= len(tags) <= 5:
        problems.append(f"{len(tags)} tags, allowed 3-5")
    unknown = [t for t in tags if t.lower() not in VERIFIED_TAGS]
    blocked = [t for t in tags if t.lower() in BLOCKED_TAGS]
    if unknown:
        problems.append("not in the verified registry: " + ", ".join(unknown))
    if blocked:
        problems.append("blocked: " + ", ".join(blocked))
    missing_in_body = [t for t in tags if t.lower() not in body.lower()]
    if missing_in_body:
        problems.append("declared but not on the final line: " + ", ".join(missing_in_body))
    rep.add("R12", "FAIL" if problems else "PASS", "; ".join(problems) or f"{len(tags)} verified tags")

    # R13 template
    tpl = str(meta.get("template", "")).strip().upper()
    if not tpl:
        rep.add("R13", "FAIL", "no template named")
    elif tpl not in TEMPLATE_IDS:
        rep.add("R13", "FAIL", f"'{tpl}' is not one of the fourteen registered templates")
    else:
        rep.add("R13", "PASS", tpl)


def check_profile_read(rep: Report, meta: dict, dtype: str) -> None:
    if dtype not in ("comment", "dm"):
        rep.add("R16", "SKIP", "not a per-person deliverable")
        return
    if meta.get("profile_checked"):
        rep.add("R16", "PASS", f"profile read: {meta['profile_checked']}")
    else:
        rep.add("R16", "FAIL", "no profile_checked record; read the person before writing to them")


def check_cold_link(rep: Report, meta: dict, body: str, dtype: str) -> None:
    if dtype != "comment":
        rep.add("R17", "SKIP", "not a comment")
        return
    warm = str(meta.get("warm", "")).lower() in ("yes", "true", "1")
    links = re.findall(r"https?://\S+|www\.\S+", body)
    if links and not warm:
        rep.add("R17", "FAIL", f"{len(links)} link(s) in a cold comment")
    else:
        rep.add("R17", "PASS", "warm reply with a link" if links else "no link")


def check_index_row(rep: Report, meta: dict, path: str) -> None:
    index = os.path.join(EMPIRE, "VERIFIED_POSTS", "INDEX.md")
    if not os.path.exists(index):
        rep.add("R23", "SKIP", "INDEX.md missing")
        return
    text = open(index, encoding="utf-8", errors="replace").read().lower()
    key = str(meta.get("id", "")).lower()
    date = str(meta.get("date", "")).lower()
    if (key and key in text) or (date and date in text):
        rep.add("R23", "PASS", "row present")
    else:
        rep.add("R23", "FAIL", f"no row for '{key or date}' in VERIFIED_POSTS/INDEX.md")


def check_delivery_log(rep: Report, meta: dict, path: str) -> None:
    status = str(meta.get("status", "")).lower()
    if status not in ("sent", "posted"):
        rep.add("R22", "SKIP", "not marked sent")
        return
    log = os.path.join(EMPIRE, "STATE", "DELIVERY-LOG.md")
    if not os.path.exists(log):
        rep.add("R22", "FAIL", "STATE/DELIVERY-LOG.md missing")
        return
    text = open(log, encoding="utf-8", errors="replace").read()
    key = str(meta.get("id", "")) or os.path.basename(os.path.dirname(path))
    if key and key in text:
        rep.add("R22", "PASS", "journalled")
    else:
        rep.add("R22", "FAIL", f"marked {status} but '{key}' is not in the delivery log")


def check_approval(rep: Report, meta: dict) -> None:
    if str(meta.get("status", "")).lower() in ("sent", "posted") and str(meta.get("approved", "")).lower() not in ("yes", "true", "1"):
        rep.add("R18", "FAIL", "marked sent without approved: yes")
        rep.add("R28", "FAIL", "marked sent; the owner sends, the agent drafts")
    else:
        rep.add("R18", "PASS", "draft state respected")
        rep.add("R28", "PASS", "no send claimed")


# --------------------------------------------------------------------------
# run
# --------------------------------------------------------------------------


def visible_text(markup: str) -> str:
    """The words a reader sees in an HTML page, with markup and CSS removed.

    An exported artefact is often sent as HTML, and linting the stylesheet is how a page
    fails a check about commas. The rules are about the prose, so the prose is what is read.
    """
    import html as _html
    # Headings are labels, not sentences, and a heading never carries terminal punctuation.
    text = re.sub(r"(?is)<head\b.*?</head>", " ", markup)
    text = re.sub(r"(?is)<(script|style|h[1-6])\b.*?</\1>", " ", text)
    text = re.sub(r"(?s)<!--.*?-->", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = _html.unescape(text)
    return re.sub(r"[ \t]+", " ", text)


def gate_file(path: str, forced_type: str | None = None) -> Report:
    rep = Report(path)
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError as exc:
        rep.add("R26", "FAIL", f"could not read: {exc}")
        return rep

    exported = forced_type == "exported"
    if exported and path.lower().endswith((".html", ".htm")):
        # Read the page, not its stylesheet.
        meta, body = {}, visible_text(text)
    else:
        meta, body = parse_front_matter(text)
    pasted = post_body(body)
    dtype = "doc" if exported else (forced_type or infer_type(path, meta)).lower()
    audience = "client" if exported else infer_audience(path, meta)
    rel = os.path.relpath(os.path.abspath(path), EMPIRE)

    rep.meta = {"type": dtype, "audience": audience, "path": rel, "words": body_words(body)}  # type: ignore[attr-defined]

    if not exported:
        # An exported artefact is read by a client or a reviewer. Internal front
        # matter in it would be noise at best and a leak at worst, so it is not
        # required and it is not wanted.
        check_contract(rep, meta, dtype, audience, path)
    else:
        rep.add("R26", "PASS", "exported artefact, internal metadata not required")
    check_text(rep, body, meta, dtype, audience, pasted, exported, path)
    check_profile_read(rep, meta, dtype)
    check_cold_link(rep, meta, body, dtype)
    check_approval(rep, meta)
    if dtype == "post":
        check_post(rep, meta, pasted)
        check_index_row(rep, meta, path)
    check_delivery_log(rep, meta, path)
    rep.rows.sort(key=lambda r: STATUS_ORDER.get(r["status"], 9))
    return rep


def render(rep: Report, quiet: bool) -> None:
    meta = getattr(rep, "meta", {})
    print(f"\n{rep.path}")
    if meta:
        print(f"  type={meta.get('type')}  audience={meta.get('audience')}  body={meta.get('words')}w")
    for row in rep.rows:
        if quiet and row["status"] == "PASS":
            continue
        mark = {"FAIL": "FAIL", "WARN": "warn", "PASS": "pass", "SKIP": " -- "}[row["status"]]
        print(f"  [{mark}] {row['rule']}  {row['detail']}")
    fails, warns = len(rep.failed), len(rep.warned)
    verdict = "BLOCKED" if fails else ("PASS with warnings" if warns else "PASS")
    print(f"  -> {verdict} ({fails} blocking, {warns} warning)")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Enforce every automatable rule before a file leaves the repo.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--profile",
                    choices=["post", "comment", "dm", "doc", "internal", "email", "exported"],
                    default=None,
                    help="exported: a client or reviewer artefact. Full text checks, no front matter required")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--strict", action="store_true", help="treat warnings as blocking")
    args = ap.parse_args(argv)

    reports = [gate_file(p, args.profile) for p in args.files]

    if args.json:
        print(json.dumps(
            [
                {
                    "path": r.path,
                    "meta": getattr(r, "meta", {}),
                    "rows": r.rows,
                    "failures": len(r.failed),
                    "warnings": len(r.warned),
                }
                for r in reports
            ],
            indent=2,
        ))
    else:
        for r in reports:
            render(r, args.quiet)
        total_f = sum(len(r.failed) for r in reports)
        total_w = sum(len(r.warned) for r in reports)
        print(f"\n{len(reports)} file(s): {total_f} blocking, {total_w} warning(s)")

    bad = any(r.failed for r in reports)
    if args.strict:
        bad = bad or any(r.warned for r in reports)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
