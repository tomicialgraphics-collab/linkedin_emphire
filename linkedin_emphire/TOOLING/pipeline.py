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
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EMPIRE = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(EMPIRE, ".."))
REGISTRY = os.path.join(EMPIRE, "PIPELINE", "registry")
STATE = os.path.join(EMPIRE, "STATE")
GATE = os.path.join(HERE, "gate.py")

sys.path.insert(0, HERE)
import gate as G  # noqa: E402

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

Then, before it leaves the repo:

  python3 linkedin_emphire/TOOLING/pipeline.py check <path>

Nothing is delivered that the gate blocks. Nothing is delivered without a line in
STATE/DELIVERY-LOG.md. Nothing is sent by the agent: the owner sends.
""")
    print(f"OPEN LOOPS ({len(loops)})")
    for item in loops[:12]:
        print(f"  {item['id']:>3}  {item['text']}")
    if len(loops) > 12:
        print(f"       ... {len(loops) - 12} more, run `pipeline.py loops`")
    print()
    return 0


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
    rc = G.main(args.paths + (["--quiet"] if args.quiet else []))
    return rc


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
        path = os.path.join(ROOT, entry["dir"])
        count, size, newest = walk_area(path) if os.path.isdir(path) else (0, 0, "")
        root_lines.append(f"| `{entry['dir']}/` | {entry['purpose']} ({count} files) |")
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

    p = sub.add_parser("check")
    p.add_argument("paths", nargs="+")
    p.add_argument("--quiet", action="store_true")
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
