#!/usr/bin/env python3
"""pipeline.py - run the emphire as a pipeline instead of a folder.

    python3 TOOLING/pipeline.py start              # boot brief: what to read, what is open
    python3 TOOLING/pipeline.py status             # open loops, recent deliveries, gate state
    python3 TOOLING/pipeline.py new post <slug>    # scaffold a post to the contract
    python3 TOOLING/pipeline.py check <path>       # the gate (same exit codes)
    python3 TOOLING/pipeline.py log <path> --to NAME --how "Drive, hash in message"
    python3 TOOLING/pipeline.py audit              # gate every live deliverable, write the report
    python3 TOOLING/pipeline.py render             # rebuild the generated docs and MAP.md
    python3 TOOLING/pipeline.py map                # inventory the whole tree
    python3 TOOLING/pipeline.py board              # what is late and what is due today
    python3 TOOLING/pipeline.py loops              # list open loops
    python3 TOOLING/pipeline.py loops done L3      # close one
    python3 TOOLING/pipeline.py loops add "text"   # open one

The point of `start` is that a new session cannot begin work without having been
shown the rules, the state and the gate. It prints and writes nothing, so it is
safe to run every session.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
EMPIRE = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(EMPIRE, ".."))
REGISTRY = os.path.join(EMPIRE, "PIPELINE", "registry")
STATE = os.path.join(EMPIRE, "STATE")
GATE = os.path.join(HERE, "gate.py")

sys.path.insert(0, HERE)
import gate as G  # noqa: E402
import board as B  # noqa: E402

TODAY = dt.date.today().isoformat()


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def load(name: str) -> dict:
    path = os.path.join(REGISTRY, name)
    return json.loads(read(path)) if os.path.exists(path) else {}


def rel(path: str) -> str:
    return os.path.relpath(path, EMPIRE)


def rule_heading(rule: dict) -> str:
    return f"{rule['id']} [{rule['severity']}] {', '.join(rule['scope'])}"


# --------------------------------------------------------------------------
# start
# --------------------------------------------------------------------------

def cmd_start(_args) -> int:
    rules = load("rules.json")
    blocks = [r for r in rules.get("rules", []) if r["severity"] == "block"]
    manual = [r for r in rules.get("rules", []) if r["severity"] == "manual"]
    loops = open_loops()

    print("=" * 72)
    print(f"EMPHIRE  stage S0  boot  {TODAY}")
    print("=" * 72)
    print(f"""
Read these before writing anything, in this order:

  1  PIPELINE/00-START.md          the boot contract, one page
  2  PIPELINE/20-RULES.md          {len(rules.get('rules', []))} rules, {len(blocks)} blocking, {len(manual)} manual
  3  PIPELINE/50-CONTRACT.md       the shape every deliverable must have
  4  PIPELINE/10-STAGES.md         where the work is and what closes it
  5  DAILY CONTENT/visual_and_hook_spec.md    if the deliverable is a post
  6  DAILY CONTENT/post_templates.txt         the fourteen templates
  7  context.md s7 and s8                     standing rules and voice
  8  STATE/OPEN-LOOPS.md                      what is unfinished
  9  STATE/BORROWED-AUDIENCE.md               who has been asked, and who is due
 10  STATE/CASE-STUDY-INDEX.md                which client page is waiting on permission
 11  PIPELINE/70-WEEKLY-REVIEW.md             the twenty minutes that kills something

Then, before it leaves the repo:

  python3 linkedin_emphire/TOOLING/pipeline.py check <path>

Nothing is delivered that the gate blocks. Nothing is delivered without a line in
STATE/DELIVERY-LOG.md. Nothing is sent by the agent: the owner sends.
""")
    print("WHAT IS DUE")
    B.main(["--brief"])
    print(f"OPEN LOOPS ({len(loops)})")
    for item in loops[:12]:
        print(f"  {item['id']:>3}  {item['text']}")
    if len(loops) > 12:
        print(f"       ... {len(loops) - 12} more, run `pipeline.py loops`")
    print()
    return 0


def cmd_board(_args) -> int:
    return B.main([])


# --------------------------------------------------------------------------
# loops
# --------------------------------------------------------------------------

LOOP_RE = re.compile(r"^- \[( |x)\] (L\d+) (.*)$")


def loops_path() -> str:
    return os.path.join(STATE, "OPEN-LOOPS.md")


def open_loops() -> list[dict]:
    path = loops_path()
    if not os.path.exists(path):
        return []
    out = []
    for line in read(path).splitlines():
        m = LOOP_RE.match(line.strip())
        if m and m.group(1) == " ":
            out.append({"id": m.group(2), "text": m.group(3)})
    return out


def cmd_loops(args) -> int:
    if args.action == "done":
        target = args.item.upper()
        text = read(loops_path())
        new, hit = [], False
        for line in text.splitlines():
            m = LOOP_RE.match(line.strip())
            if m and m.group(2) == target and m.group(1) == " ":
                stamp = dt.date.today().isoformat()
                new.append(f"- [x] {target} {m.group(3)}  (closed {stamp})")
                hit = True
            else:
                new.append(line)
        if not hit:
            print(f"no open loop {target}")
            return 1
        open(loops_path(), "w", encoding="utf-8").write("\n".join(new) + "\n")
        print(f"closed {target}")
        return 0

    if args.action == "add":
        items = open_loops()
        nxt = 1
        if items:
            nxt = max(int(i["id"][1:]) for i in items) + 1
        stamp = dt.date.today().isoformat()
        with open(loops_path(), "a", encoding="utf-8") as fh:
            fh.write(f"- [ ] L{nxt} {args.item}  (opened {stamp})\n")
        print(f"opened L{nxt}")
        return 0

    items = open_loops()
    print(f"{len(items)} open loop(s)")
    for i in items:
        print(f"  {i['id']:>3}  {i['text']}")
    return 0


# --------------------------------------------------------------------------
# check
# --------------------------------------------------------------------------

def cmd_check(args) -> int:
    extra = ["--quiet"] if args.quiet else []
    if getattr(args, "profile", None):
        extra += ["--profile", args.profile]
    return G.main(args.paths + extra)


# --------------------------------------------------------------------------
# log
# --------------------------------------------------------------------------

def delivery_log() -> str:
    return os.path.join(STATE, "DELIVERY-LOG.md")


def cmd_log(args) -> int:
    path = args.path
    if not os.path.exists(path):
        print(f"no such file: {path}")
        return 2
    rep = G.gate_file(path)
    fails = len(rep.failed)
    warns = len(rep.warned)
    digest = sha256(path)
    size = os.path.getsize(path)
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    line = (
        f"| {stamp} | `{rel(os.path.abspath(path))}` | {size:,} B | `{digest}` | "
        f"{'BLOCKED' if fails else 'pass'} ({fails}F/{warns}W) | {args.to} | {args.how} |"
    )
    log = delivery_log()
    header = (
        "# Delivery log\n\n"
        "Append-only. Every file that leaves this repo gets a row: path, size, SHA-256, gate result,\n"
        "who received it, and how. A file that is not in this table has not been delivered, whatever\n"
        "the chat says. `pipeline.py log <path>` writes the row and runs the gate at the same time.\n\n"
        "| When | File | Size | SHA-256 | Gate | To | How |\n"
        "|---|---|---|---|---|---|---|\n"
    )
    if not os.path.exists(log):
        open(log, "w", encoding="utf-8").write(header)
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"{'BLOCKED' if fails else 'logged'}: {rel(os.path.abspath(path))} {digest[:16]}...")
    if fails:
        print("  the row is written with a BLOCKED verdict. Do not send until it passes.")
        return 1
    return 0


# --------------------------------------------------------------------------
# new post
# --------------------------------------------------------------------------

POST_TEMPLATE = """---
deliverable: post
id: {date}_{slug}
date: {date}
audience: public
status: draft
approved: no
template: {template}
headline:
subheadline:
headline_alt:
subheadline_alt:
headline_alt2:
subheadline_alt2:
box:
box_alt:
hashtags: []
slot:
first_comment: FIRST_COMMENT.md
---

{headline}

{subheadline}

[body: build it on {template}. Problem, the common misconception, the reality, three arrows of what
works, the part nobody tells you, one flat closer. End on a statement.]

#AISecurity #AIRedTeam #AIEvaluation #AIGovernance
"""


def cmd_new(args) -> int:
    date = args.date or TODAY
    folder = os.path.join(EMPIRE, "VERIFIED_POSTS", f"{date}_{args.slug}")
    os.makedirs(folder, exist_ok=True)
    post = os.path.join(folder, "post.md")
    if os.path.exists(post) and not args.force:
        print(f"exists: {rel(post)} (use --force to overwrite)")
        return 1
    open(post, "w", encoding="utf-8").write(
        POST_TEMPLATE.format(date=date, slug=args.slug, template=args.template)
    )
    meta = os.path.join(folder, "metadata.json")
    if not os.path.exists(meta):
        open(meta, "w", encoding="utf-8").write(json.dumps(
            {
                "post_number": None,
                "date": date,
                "slug": args.slug,
                "template": args.template,
                "status": "DRAFT",
                "hashtags": [],
            },
            indent=2,
        ) + "\n")
    print(f"scaffolded {rel(post)}")
    print("  fill the front matter and the body, then: pipeline.py check " + rel(post))
    return 0


# --------------------------------------------------------------------------
# status
# --------------------------------------------------------------------------

def cmd_status(_args) -> int:
    items = open_loops()
    print(f"\nOPEN LOOPS  {len(items)}")
    for i in items:
        print(f"  {i['id']:>3}  {i['text']}")

    log = delivery_log()
    print("\nRECENT DELIVERIES")
    if os.path.exists(log):
        rows = [l for l in read(log).splitlines() if l.startswith("| 20")]
        for r in rows[-8:]:
            print("  " + r)
        if not rows:
            print("  none journalled yet")
    else:
        print("  no delivery log")

    print("\nGATE")
    posts = sorted(p for p in os.listdir(os.path.join(EMPIRE, "VERIFIED_POSTS"))
                   if re.match(r"\d{4}-\d{2}-\d{2}_", p))
    contract = legacy = 0
    for p in posts:
        f = os.path.join(EMPIRE, "VERIFIED_POSTS", p, "post.md")
        if os.path.exists(f):
            meta, _ = G.parse_front_matter(read(f))
            if meta:
                contract += 1
            else:
                legacy += 1
    tag_count = len(G.VERIFIED_TAGS)
    no_post = len(posts) - contract - legacy
    print(f"  posts on file: {contract + legacy} ({contract} under contract, {legacy} legacy)"
          + (f", {no_post} folder(s) with no post.md" if no_post else ""))
    print(f"  rules: {len(G.RULE_BY_ID)}  templates: {len(G.TEMPLATE_IDS)}  verified hashtags: {tag_count}")
    print(f"  run `pipeline.py audit` for the full scoreboard\n")
    return 0


# --------------------------------------------------------------------------
# growth
# --------------------------------------------------------------------------

GROWTH_TARGET = 5000
GROWTH_DEADLINE = "2026-12-25"
GROWTH_CHECKPOINTS = [("2026-11-15", 1600), ("2026-11-29", 2600), ("2026-12-13", 3300)]


def _follower_rows():
    path = os.path.join(EMPIRE, "analytics", "follower-log.md")
    rows = []
    if not os.path.exists(path):
        return rows
    for line in open(path).read().splitlines():
        m = re.match(r"\|\s*(\d{4}-\d{2}-\d{2})[^|]*\|\s*([\d,]+)\s*\|", line)
        if m:
            rows.append((m.group(1), int(m.group(2).replace(",", ""))))
    return sorted(rows)



VIEWER_DIR = os.path.join(EMPIRE, "analytics", "profile-viewers")

_VIEWER_BUCKETS = [
    ("founder or owner", ("founder", "business owner")),
    ("university or student", ("university", "college", "student", "institute of technology",
                               "universita", "epfl", "icfo")),
    ("research fellow or professor", ("research fellow", "professor")),
    ("security industry or vendor", ("network security", "security and investigations", "infragard",
                                     "cymulate", "gray swan", "sonatype", "palo alto", "advai",
                                     "tenet security", "nimble")),
    ("named engineering role", ("software developer at", "engineer at", "developer at",
                                "chief technology officer", "technology manager")),
]


def _viewer_file(args):
    name = getattr(args, "file", None)
    if name:
        return name
    if not os.path.isdir(VIEWER_DIR):
        return None
    files = sorted(f for f in os.listdir(VIEWER_DIR) if f.endswith(".txt"))
    return os.path.join(VIEWER_DIR, files[-1]) if files else None


def cmd_viewers(args) -> int:
    """Segment a pasted profile viewer list. One descriptor per line."""
    path = _viewer_file(args)
    if not path or not os.path.exists(path):
        print("\n  viewers: no list found. Save the pasted page to analytics/profile-viewers/YYYY-MM-DD_visible.txt\n")
        return 1
    lines = [l.strip() for l in open(path, encoding="utf-8").read().splitlines() if l.strip()]
    if not lines:
        print("  viewers: the file is empty.")
        return 1
    total = len(lines)
    print(f"\n  {os.path.basename(path)}: {total} visible entries")
    print("  a share, not a census. LinkedIn shows part of the ninety day total.\n")
    for label, words in _VIEWER_BUCKETS:
        hits = [l for l in lines if any(w in l.lower() for w in words)]
        print(f"    {len(hits):>4}  {len(hits) / total:>5.0%}  {label}")
    industries = {}
    for line in lines:
        m = re.search(r"in the ([A-Za-z ,&]+) industry", line)
        if m:
            k = m.group(1).strip()
            industries[k] = industries.get(k, 0) + 1
    print("\n  industries named in the descriptors")
    for label, count in sorted(industries.items(), key=lambda kv: -kv[1])[:6]:
        print(f"    {count:>4}  {label}")
    founders = [l for l in lines if "founder" in l.lower() or "business owner" in l.lower()]
    soft = [l for l in founders if re.search(r"software|it services|technology, information|security", l.lower())]
    print(f"\n  founders in a software, IT or security industry: {len(soft)} of {len(founders)}")
    print("  that last number is the one that names buyers.\n")
    return 0


def cmd_growth(_args) -> int:
    rows = _follower_rows()
    if not rows:
        print("growth: analytics/follower-log.md has no dated rows yet. One line a day, or this command cannot speak.")
        return 1
    last_date, last = rows[-1]
    first_date, first = rows[0]
    d_last = dt.date.fromisoformat(last_date)
    d_dead = dt.date.fromisoformat(GROWTH_DEADLINE)
    days_left = (d_dead - d_last).days
    need = GROWTH_TARGET - last
    per_day = need / days_left if days_left > 0 else float("inf")
    span = (d_last - dt.date.fromisoformat(first_date)).days
    observed = (last - first) / span if span > 0 else 0.0
    projected = int(last + observed * days_left)

    print(f"\n  followers {last:,} on {last_date}   target {GROWTH_TARGET:,} by {GROWTH_DEADLINE}")
    print(f"  net new needed {need:,} over {days_left} day(s)  =  {per_day:.1f} a day")
    print(f"  observed since {first_date}: {observed:.1f} a day  ->  {projected:,} on the deadline")
    verdict = "on track" if observed >= per_day else "behind the rate the target needs"
    print(f"  verdict: {verdict}")
    print("\n  checkpoints from STRATEGY/2026-11-06_follower-plan_1007-to-5000.md")
    for day, floor in GROWTH_CHECKPOINTS:
        d = dt.date.fromisoformat(day)
        if d <= d_last:
            state = "met" if last >= floor else "MISSED"
        else:
            gap_days = (d - d_last).days
            pace = (floor - last) / gap_days
            state = f"due in {gap_days} day(s), needs {pace:.1f} a day to reach {floor:,}"
        print(f"    {day}  floor {floor:,}   {state}")
    print("\n  the one line to fill tonight: analytics/follower-log.md\n")
    return 0


# --------------------------------------------------------------------------
# revenue
# --------------------------------------------------------------------------

REVENUE_TARGET = 5000
REVENUE_DEADLINE = "2026-12-25"


def _revenue_rows():
    path = os.path.join(EMPIRE, "STATE", "REVENUE-LOG.md")
    rows = []
    if not os.path.exists(path):
        return rows
    for line in open(path).read().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.match(r"\d{4}-\d{2}-\d{2}$", cells[0]):
            continue
        try:
            amount = float(re.sub(r"[^0-9.]", "", cells[3]) or 0)
        except ValueError:
            amount = 0.0
        rows.append({"date": cells[0], "deal": cells[1], "client": cells[2],
                     "amount": amount, "state": cells[4].lower()})
    # The log is append only: a deal that moves state gets a new row, never an edit.
    # So a client and an amount can appear more than once, and the arithmetic has to
    # take the last word rather than add every word. Without this, a proposal that was
    # declined still counts as proposed, and the gap to the target is a fiction.
    latest = {}
    for row in rows:
        key = (row["client"].lower(), row["amount"])
        if key not in latest or row["date"] >= latest[key]["date"]:
            latest[key] = row
    return list(latest.values())


def cmd_revenue(_args) -> int:
    rows = _revenue_rows()
    if not rows:
        print("revenue: STATE/REVENUE-LOG.md has no deals. A deal that is not a row does not exist for the maths.")
        return 1
    paid = sum(r["amount"] for r in rows if r["state"] == "paid")
    won = sum(r["amount"] for r in rows if r["state"] == "won")
    proposed = sum(r["amount"] for r in rows if r["state"] == "proposed")
    free = [r for r in rows if r["state"] == "free"]
    open_deals = [r for r in rows if r["state"] in ("prospect", "proposed", "won")]
    d_last = dt.date.today()
    days_left = (dt.date.fromisoformat(REVENUE_DEADLINE) - d_last).days
    gap = max(0.0, REVENUE_TARGET - paid - won)
    avg = (sum(r["amount"] for r in rows if r["state"] in ("paid", "won")) / max(1, len([r for r in rows if r["state"] in ("paid", "won")])))
    print(f"\n  revenue to {REVENUE_DEADLINE}: paid {paid:,.0f}  agreed {won:,.0f}  proposed {proposed:,.0f}  of {REVENUE_TARGET:,}")
    print(f"  days left {days_left}   gap to target {gap:,.0f}")
    if days_left > 0:
        print(f"  gap per day {gap / days_left:,.0f}")
    print(f"  deals at 0 USD recorded as free: {len(free)} of {len(rows)}")
    print(f"  open conversations: {len(open_deals)}")
    for r in open_deals:
        print(f"    {r['state']:<9} {r['amount']:>8,.0f}  {r['client']}  ({r['deal']})")
    if avg:
        print(f"  average closed deal {avg:,.0f}, so the gap is about {gap / avg:.1f} more deals at that size")
    print()
    return 0


# --------------------------------------------------------------------------
# upwork: the volume channel, measured rather than intended
# --------------------------------------------------------------------------

UPWORK_DIR = os.path.join(EMPIRE, "UPWORK")
CONNECTS_FILE = os.path.join(UPWORK_DIR, "connects.txt")
PROPOSAL_QUOTA = 8  # two a day, Monday to Thursday


def _field(text: str, meta: dict, key: str) -> str:
    """A front-matter value, or the older `Key: value` line inside the file.

    The proposals folder predates front matter, so the first entries record
    connects and dates as a plain line. Read both rather than rewriting history.
    """
    value = str(meta.get(key, "")).strip()
    if value:
        return value
    m = re.search(r"^%s:\s*(.+)$" % re.escape(key), text, re.M | re.I)
    return m.group(1).strip() if m else ""


def _proposal_rows() -> list[dict]:
    folder = os.path.join(UPWORK_DIR, "PROPOSALS")
    rows = []
    if not os.path.isdir(folder):
        return rows
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name.upper() == "README.MD":
            continue
        text = read(os.path.join(folder, name))
        meta, _ = G.parse_front_matter(text)
        raw_date = _field(text, meta, "date")
        m = re.search(r"\d{4}-\d{2}-\d{2}", raw_date)
        connects = _field(text, meta, "connects")
        m2 = re.search(r"\d+", connects)
        quoted = _field(text, meta, "quoted")
        m3 = re.search(r"[\d,]+", quoted)
        rows.append({
            "file": name,
            "date": m.group(0) if m else "",
            "connects": int(m2.group(0)) if m2 else 0,
            "quoted": float(m3.group(0).replace(",", "")) if m3 else 0.0,
            "status": (_field(text, meta, "status") or "unknown").split(".")[0].strip().lower(),
        })
    return rows


def cmd_upwork(_args) -> int:
    rows = _proposal_rows()
    today = dt.date.today()
    week_ago = today - dt.timedelta(days=7)

    def in_week(r):
        try:
            return dt.date.fromisoformat(r["date"]) >= week_ago
        except ValueError:
            return False

    sent = [r for r in rows if r["status"].startswith(("sent", "reply", "interview", "won", "hired"))]
    recent = [r for r in rows if in_week(r) and r["status"] != "draft"]
    spent = int(round(sum(r["connects"] for r in sent)))
    quoted = sum(r["quoted"] for r in rows if r["quoted"])

    balance = None
    if os.path.exists(CONNECTS_FILE):
        m = re.search(r"\d+", read(CONNECTS_FILE))
        balance = int(m.group(0)) if m else None

    print()
    if balance is None:
        print("  connects: unknown. Put the number Upwork shows in UPWORK/connects.txt and it stops being a guess.")
    else:
        print(f"  connects: {balance:,} on hand")
    print(f"  proposals sent: {len(sent)} of {len(rows)} files   quoted total {quoted:,.0f}")
    print(f"  last 7 days: {len(recent)} of {PROPOSAL_QUOTA} quota ({PROPOSAL_QUOTA / 7:.1f} a day)")
    print(f"  connects spent on sent proposals: {spent:,}")
    if balance is not None:
        typical = 12
        print(f"  at about {typical} connects a proposal, {balance:,} connects buys {balance // typical} proposals, "
              f"under the {PROPOSAL_QUOTA} a week the plan asks for")
    won = [r for r in rows if r["status"].startswith(("won", "hired"))]
    print(f"  won through this folder: {len(won)}")
    if not sent:
        print()
        print("  Nothing has been sent. A proposal that stays a draft costs nothing and earns nothing;")
        print("  the first send is the only event in this file that can turn into money.")
    print()
    print("  An agreed job becomes a row in STATE/REVENUE-LOG.md. ./emphire revenue is the only place")
    print("  that counts, so a win that is not a row is not money yet.")
    print()
    return 0


# --------------------------------------------------------------------------
# audit
# --------------------------------------------------------------------------

def cmd_audit(args) -> int:
    rows = []
    for folder in sorted(os.listdir(os.path.join(EMPIRE, "VERIFIED_POSTS"))):
        if not re.match(r"\d{4}-\d{2}-\d{2}_", folder):
            continue
        post = os.path.join(EMPIRE, "VERIFIED_POSTS", folder, "post.md")
        if not os.path.exists(post):
            continue
        meta, _ = G.parse_front_matter(read(post))
        rep = G.gate_file(post)
        rows.append((folder, bool(meta), len(rep.failed), len(rep.warned), rep))

    recent = dt.date.today() - dt.timedelta(days=14)
    engagement = os.path.join(EMPIRE, "ENGAGEMENT")
    if os.path.isdir(engagement):
        for name in sorted(os.listdir(engagement)):
            full = os.path.join(engagement, name)
            if not (os.path.isfile(full) and name.endswith(".md")):
                continue
            mtime = dt.date.fromtimestamp(os.path.getmtime(full))
            if mtime < recent:
                continue
            meta, _ = G.parse_front_matter(read(full))
            rep = G.gate_file(full)
            rows.append((f"ENGAGEMENT/{name}", bool(meta), len(rep.failed), len(rep.warned), rep))

    lines = [
        "# Gate report",
        "",
        f"Generated {dt.datetime.now().strftime('%Y-%m-%d %H:%M')} by `TOOLING/pipeline.py audit`.",
        "Legacy rows are posts written before the contract existed. They are frozen: they are not",
        "re-gated, and they cannot be reposted without being brought under the contract first.",
        "",
        "| File | Contract | Blocking | Warnings | Verdict |",
        "|---|---|---|---|---|",
    ]
    blocked = 0
    for name, under, f, w, _rep in rows:
        verdict = "BLOCKED" if f and under else ("pass" if under and not w else ("pass, warnings" if under else "legacy"))
        if f and under:
            blocked += 1
        lines.append(f"| `{name}` | {'yes' if under else 'legacy'} | {f} | {w} | {verdict} |")
    report = os.path.join(STATE, "GATE-REPORT.md")
    open(report, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{len(rows)} deliverable(s) checked, {blocked} blocked under contract")
    print(f"report: {rel(report)}")
    if blocked and not args.tolerant:
        for name, under, f, _w, rep in rows:
            if under and f:
                print(f"\n{name}")
                for row in rep.failed:
                    print(f"  {row['rule']}  {row['detail']}")
        return 1
    return 0


# --------------------------------------------------------------------------
# adopt: bring a legacy file under the contract without touching its prose
# --------------------------------------------------------------------------

ADOPT_KEYS = ["deliverable", "id", "date", "audience", "status"]


def cmd_adopt(args) -> int:
    path = args.path
    text = read(path)
    if text.lstrip().startswith("---"):
        print(f"{rel(os.path.abspath(path))} already has front matter")
        return 0
    dtype = args.type
    if dtype == "post":
        print("posts are scaffolded, not adopted: use `new post <slug>` and move the body in")
        return 1
    folder = os.path.basename(os.path.dirname(os.path.abspath(path)))
    guess_id = folder if re.match(r"\d{4}-\d{2}-\d{2}", folder) else os.path.splitext(os.path.basename(path))[0]
    date = args.date or (guess_id[:10] if re.match(r"\d{4}-\d{2}-\d{2}", guess_id) else TODAY)
    block = ["---", f"deliverable: {dtype}", f"id: {guess_id}", f"date: {date}",
             f"audience: {args.audience}", "status: draft", "approved: no", "---", "", ""]
    open(path, "w", encoding="utf-8").write("\n".join(block) + text)
    print(f"adopted {rel(os.path.abspath(path))} as {dtype}/{args.audience} on {date}")
    print("  fill any type-specific keys the gate asks for, then re-run check")
    return 0


# --------------------------------------------------------------------------
# promote: settle a two-lineage file without deleting either side
# --------------------------------------------------------------------------

def cmd_promote(args) -> int:
    variant = args.variant
    canon = args.over
    for path in (variant, canon):
        if not os.path.exists(path):
            print(f"missing: {path}")
            return 2
    if G.sha256(variant) == G.sha256(canon):
        print("the two files are already identical, nothing to do")
        return 0

    stem, ext = os.path.splitext(os.path.basename(canon))
    parked = os.path.join(os.path.dirname(canon), "_variants", f"{stem}.superseded{ext}")
    n = 2
    while os.path.exists(parked):
        parked = os.path.join(os.path.dirname(canon), "_variants", f"{stem}.superseded-{n}{ext}")
        n += 1
    os.makedirs(os.path.dirname(parked), exist_ok=True)

    old_digest = G.sha256(canon)[:16]
    shutil.move(canon, parked)
    shutil.copy2(variant, canon)
    os.remove(variant)
    print(f"promoted   {variant}")
    print(f"     over  {canon} (old copy at {parked}, sha {old_digest})")
    print("now: run  pipeline.py render  and check anything that reads this file")
    return 0


# --------------------------------------------------------------------------
# verify-moves: prove a restructure deleted nothing unique
# --------------------------------------------------------------------------

def cmd_verify_moves(args) -> int:
    """Every path deleted by a commit must still have a byte-identical file in HEAD.

    This is the check that answers "where did that file go". A deletion whose
    blob is still in the tree is a duplicate, by definition: same bytes. A
    deletion whose blob is nowhere is either a real loss or a file that was
    rewritten, and it gets reported so a human can say which.
    """
    since = args.since
    # -z and a NUL split: paths with spaces in them are common here ("DAILY CONTENT"),
    # and git quotes them otherwise, which turns one path into three fake ones.
    deleted = [p for p in subprocess.run(
        ["git", "-c", "core.quotepath=false", "diff", "--diff-filter=D", "--name-only", "-z",
         f"{since}^", since],
        capture_output=True, text=True, cwd=ROOT,
    ).stdout.split("\0") if p]
    if not deleted:
        print(f"{since}: no deletions")
        return 0

    parents = {}
    for path in deleted:
        out = subprocess.run(["git", "-c", "core.quotepath=false", "rev-parse", f"{since}^:{path}"],
                             capture_output=True, text=True, cwd=ROOT).stdout.strip()
        if out:
            parents[path] = out

    live = {}
    tree = subprocess.run(["git", "-c", "core.quotepath=false", "ls-tree", "-r", "-z", "HEAD"],
                          capture_output=True, text=True, cwd=ROOT).stdout.split("\0")
    for line in tree:
        if not line:
            continue
        meta, path = line.split("\t", 1)
        sha = meta.split()[2]
        if path.startswith(".history/"):
            continue
        live.setdefault(sha, []).append(path)

    found, lost = [], []
    for path, blob in parents.items():
        (found if blob in live else lost).append((path, live.get(blob, [""])[0]))

    print(f"{since}: {len(deleted)} deletions")
    print(f"  byte-identical survivor in the live tree: {len(found)}")
    print(f"  no survivor, needs a human: {len(lost)}")
    for path, where in found[: args.show]:
        print(f"    {path}\n      == {where}")
    if len(found) > args.show:
        print(f"    ... {len(found) - args.show} more, same result")
    for path, _ in lost:
        print(f"    UNMATCHED  {path}")
    return 1 if lost else 0


# --------------------------------------------------------------------------
# map + render
# --------------------------------------------------------------------------

SKIP_DIRS = {".git", ".history", "node_modules", "__pycache__", ".venv", "dist", "build"}


def walk_area(path: str) -> tuple[int, int, str]:
    count = size = 0
    newest = ""
    for base, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            full = os.path.join(base, f)
            try:
                st = os.stat(full)
            except OSError:
                continue
            count += 1
            size += st.st_size
            stamp = dt.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d")
            newest = max(newest, stamp)
    return count, size, newest


def cmd_map(args) -> int:
    areas = load("areas.json")
    declared = {a["area"]: a for a in areas.get("areas", [])}
    present = sorted(
        d for d in os.listdir(EMPIRE)
        if os.path.isdir(os.path.join(EMPIRE, d)) and d not in SKIP_DIRS
    )
    lines = [
        "# MAP",
        "",
        f"Generated {TODAY} by `TOOLING/pipeline.py map`. Do not edit by hand: the tree is the source",
        "and this file is its index. If an area is undeclared, declare it in",
        "`PIPELINE/registry/areas.json` with a purpose, an owner role and a stage.",
        "",
        f"| Area | Files | Size | Purpose | Role | Stage |",
        "|---|---|---|---|---|---|",
    ]
    undeclared = []
    for d in present:
        count, size, newest = walk_area(os.path.join(EMPIRE, d))
        meta = declared.get(d)
        if not meta:
            undeclared.append(d)
            lines.append(f"| `{d}` | {count} | {size / 1024:.0f} KB | **UNDECLARED** | | |")
        else:
            lines.append(f"| `{d}` | {count} | {size / 1024:.0f} KB | {meta['purpose']} | {meta['role']} | {meta['stage']} |")

    lines += ["", "## Root files", "", "| File | Purpose |", "|---|---|"]
    for f in sorted(os.listdir(EMPIRE)):
        full = os.path.join(EMPIRE, f)
        if os.path.isdir(full) or f.startswith("."):
            continue
        purpose = next((r["purpose"] for r in areas.get("root_files", []) if r["file"] == f), "**UNDECLARED**")
        lines.append(f"| `{f}` | {purpose} |")

    lines += ["", "## Rules, templates, tags", "",
              f"- rules: {len(G.RULE_BY_ID)} in `PIPELINE/registry/rules.json`",
              f"- templates: {len(G.TEMPLATE_IDS)} in `PIPELINE/registry/templates.json`",
              f"- verified hashtags: {len(G.VERIFIED_TAGS)} in `PIPELINE/registry/hashtags.json`",
              ""]

    # The root, so a session also sees what is deliberately outside the pipeline.
    root_lines = ["", "## Repository root, outside the working tree", "",
                  "| Path | Purpose |", "|---|---|"]
    for entry in areas.get("root_dirs", []):
        # No file counts here on purpose: some of these folders are gitignored, so
        # a count would differ between a working copy and a clean checkout and the
        # render check in CI would fail for no reason.
        root_lines.append(f"| `{entry['dir']}/` | {entry['purpose']} |")
    root_lines += [
        "| `AGENTS.md` | the contract for any session |",
        "| `README.md` | the map for a human in a hurry |",
        "| `context.md` | the session handoff |",
        "| `emphire`, `emphire.ps1` | the pipeline commands, bash and PowerShell 5.1 |",
        "",
    ]
    lines += root_lines

    out = os.path.join(EMPIRE, "MAP.md")
    open(out, "w", encoding="utf-8").write("\n".join(lines))
    print(f"{rel(out)}: {len(present)} areas, {len(undeclared)} undeclared")
    for d in undeclared:
        print(f"  UNDECLARED  {d}")
    return 0


def cmd_visual(args) -> int:
    """Render the card that ships with a post. One implementation, in VISUAL."""
    sys.path.insert(0, os.path.join(EMPIRE, "VISUAL"))
    import post_visual

    post = Path(args.post)
    if not post.is_absolute():
        post = Path(EMPIRE) / post if (Path(EMPIRE) / post).exists() else Path(post).resolve()
    if not post.exists():
        print(f"no such post: {args.post}")
        return 2
    result = post_visual.build(post, args.pages)
    print(f"card    {rel(result['cover'])}")
    for page in sorted(result["out"].glob("page*.png")):
        print(f"page    {rel(page)}")
    if result["pdf"]:
        print(f"pdf     {rel(result['pdf'])}  ({result['pages']} pages)")
    print("\nUpload it, then put the Drive link in the post's front matter as visual_link.")
    return 0


def cmd_render(_args) -> int:
    rules = load("rules.json")["rules"]
    by_sev = {}
    for r in rules:
        by_sev.setdefault(r["severity"], []).append(r)

    out = [
        "# 20 RULES",
        "",
        "Generated from `PIPELINE/registry/rules.json` by `TOOLING/pipeline.py render`.",
        "**Do not edit this file.** Edit the registry, render, then run the gate on a known-good file",
        "so you know the check still fires and does not misfire.",
        "",
        f"{len(rules)} rules: {len(by_sev.get('block', []))} blocking, "
        f"{len(by_sev.get('warn', []))} warning, {len(by_sev.get('manual', []))} manual.",
        "",
        "## Blocking",
        "",
        "| ID | Rule | Scope | Check | Source |",
        "|---|---|---|---|---|",
    ]
    for r in by_sev.get("block", []):
        out.append(f"| {r['id']} | {r['text']} | {', '.join(r['scope'])} | `{r['check']}` | {r['source']} |")

    out += ["", "## Warning", "", "| ID | Rule | Scope | Check | Source |", "|---|---|---|---|---|"]
    for r in by_sev.get("warn", []):
        out.append(f"| {r['id']} | {r['text']} | {', '.join(r['scope'])} | `{r['check']}` | {r['source']} |")

    out += ["", "## Manual, no check exists", "",
            "These cannot be automated. Say out loud that you did them, in the delivery log, or the",
            "deliverable is not done.", "", "| ID | Rule | How to verify |", "|---|---|---|"]
    for r in by_sev.get("manual", []):
        out.append(f"| {r['id']} | {r['text']} | {r.get('verify_with', '')} |")

    out += ["", "## Where the gate gets its teeth", "",
            "```", "python3 linkedin_emphire/TOOLING/pipeline.py check <path>", "```", "",
            "Exit 0 means no blocking rule fired. It does not mean the argument is good. A rule marked",
            "manual is exactly the part a person still has to be honest about.", ""]
    open(os.path.join(EMPIRE, "PIPELINE", "20-RULES.md"), "w", encoding="utf-8").write("\n".join(out))

    tpls = load("templates.json")
    out = ["# 30 TEMPLATES", "",
           "Generated from `PIPELINE/registry/templates.json`. Source: `DAILY CONTENT/post_templates.txt`.",
           "Every post names one ID in its front matter. R13 blocks anything that is not here.", "",
           "## Rotation", ""]
    out += [f"- {r}" for r in tpls.get("rotation_rules", [])]
    out += ["", "| ID | Template | Family | Lane fit | Use when | Shape |", "|---|---|---|---|---|---|"]
    for t in tpls["templates"]:
        out.append(f"| {t['id']} | {t['name']} | {t['family']} | {t['lane_fit']} | {t['use_when']} | {' -> '.join(t['shape'])} |")
    out += ["", "## Notes", ""]
    out += [f"- **{t['id']} {t['name']}**: {t['note']}" for t in tpls["templates"]]
    out.append("")
    open(os.path.join(EMPIRE, "PIPELINE", "30-TEMPLATES.md"), "w", encoding="utf-8").write("\n".join(out))

    tags = load("hashtags.json")
    out = ["# 40 HASHTAGS", "",
           "Generated from `PIPELINE/registry/hashtags.json`. A tag that is not in the verified table",
           "cannot ship: R12 blocks it. No follower counts are claimed anywhere, because LinkedIn",
           "serves hashtag pages only to signed-in sessions and a number that cannot be checked is a",
           "fabricated number.", "", "## Verified", "",
           "| Tag | Lane | Verified | Evidence |", "|---|---|---|---|"]
    for h in tags.get("verified", []):
        out.append(f"| {h['tag']} | {h['lane']} | {h['verified']} | {h['evidence']} |")
    out += ["", "## Blocked", "", "| Tag | Why |", "|---|---|"]
    for h in tags.get("blocked", []):
        out.append(f"| {h['tag']} | {h['reason']} |")
    out += ["", "## Rules", ""] + [f"- {r}" for r in tags.get("rules", [])] + [""]
    open(os.path.join(EMPIRE, "PIPELINE", "40-HASHTAGS.md"), "w", encoding="utf-8").write("\n".join(out))

    cmd_map(argparse.Namespace())
    print("rendered 20-RULES.md, 30-TEMPLATES.md, 40-HASHTAGS.md")
    return 0


# --------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="pipeline", description="Run the emphire as a pipeline.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("start").set_defaults(fn=cmd_start)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("board").set_defaults(fn=cmd_board)

    p = sub.add_parser("check")
    p.add_argument("paths", nargs="+")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--profile", default=None,
                   choices=["post", "comment", "dm", "doc", "internal", "email", "exported"],
                   help="exported: a client or reviewer artefact, no front matter required")
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("new")
    p.add_argument("kind", choices=["post"])
    p.add_argument("slug")
    p.add_argument("--date")
    p.add_argument("--template", default="T1")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_new)

    p = sub.add_parser("log")
    p.add_argument("path")
    p.add_argument("--to", required=True)
    p.add_argument("--how", default="file plus hash")
    p.set_defaults(fn=cmd_log)

    p = sub.add_parser("promote")
    p.add_argument("variant", help="the parked file you want to become the canon")
    p.add_argument("--over", required=True, dest="over", help="the current canon it replaces")
    p.set_defaults(fn=cmd_promote)

    p = sub.add_parser("verify-moves")
    p.add_argument("--since", required=True, help="commit that performed the restructure")
    p.add_argument("--show", type=int, default=5, help="how many matches to print")
    p.set_defaults(fn=cmd_verify_moves)

    p = sub.add_parser("adopt")
    p.add_argument("path")
    p.add_argument("--type", choices=["comment", "dm", "doc", "email", "internal"], required=True)
    p.add_argument("--audience", choices=["public", "client", "reviewer", "hiring", "vendor", "internal"],
                   default="internal")
    p.add_argument("--date")
    p.set_defaults(fn=cmd_adopt)

    p = sub.add_parser("audit")
    p.add_argument("--tolerant", action="store_true")
    p.set_defaults(fn=cmd_audit)

    pv = sub.add_parser("viewers")
    pv.add_argument("file", nargs="?")
    pv.set_defaults(fn=cmd_viewers)
    sub.add_parser("growth").set_defaults(fn=cmd_growth)
    sub.add_parser("revenue").set_defaults(fn=cmd_revenue)

    sub.add_parser("upwork").set_defaults(fn=cmd_upwork)

    p = sub.add_parser("visual")
    p.add_argument("post", help="path to a post.md")
    p.add_argument("--pages", type=int, default=None, help="how many cards counting the cover")
    p.set_defaults(fn=cmd_visual)

    sub.add_parser("render").set_defaults(fn=cmd_render)
    sub.add_parser("map").set_defaults(fn=cmd_map)

    p = sub.add_parser("loops")
    p.add_argument("action", nargs="?", default="list", choices=["list", "done", "add"])
    p.add_argument("item", nargs="?")
    p.set_defaults(fn=cmd_loops)

    args = ap.parse_args(argv)
    if args.cmd == "loops" and args.action in ("done", "add") and not args.item:
        ap.error("loops done/add needs an id or a sentence")
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
