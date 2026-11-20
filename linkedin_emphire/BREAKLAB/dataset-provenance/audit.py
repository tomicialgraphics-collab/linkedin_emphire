#!/usr/bin/env python3
"""Provenance audit for a Hugging Face dataset, run against its file tree.

The point of this tool is to answer five questions about a dataset without
downloading it:

  1. Does the repository agree with the card about how big it is?
  2. How many files are actually usable, and what are the rest?
  3. Where did the content come from, and does that source allow redistribution?
  4. Does the repository carry artefacts that execute on load?
  5. Does it contain material that doubles as an evaluation set?

Everything here works from the tree listing, which the Hugging Face API serves
for a gated dataset to an account that has been granted access. Nothing is
downloaded, nothing is imported, nothing is executed.

Usage
    python audit.py --tree tree.json --dataset Vyber07/cyber-security
    python audit.py --tree tree.json --claim "16 GB" --claim "95 GB" --claim "under 1K"
    python audit.py --tree tree.json --unsafe files.txt --json out.json

The tree is the JSON from
    https://huggingface.co/api/datasets/<id>/tree/main?recursive=true

Exit codes
    0  every check ran, no blocking finding
    1  at least one blocking finding
    2  the input was not usable
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

# Artefacts that can execute or unpack on load. Hugging Face's own scanner
# flags some of these, which is what the "scanned as unsafe" banner counts.
EXECUTABLE_EXT = {
    ".pkl", ".pickle", ".pt", ".pth", ".ckpt", ".bin", ".h5", ".joblib",
    ".py", ".sh", ".ps1", ".bat", ".exe", ".dll", ".so", ".jar", ".ipynb",
}
ARCHIVE_EXT = {".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z"}

# Upstream sources named by a card, mapped to the licence standing verified on
# 14 November 2026. "blocked" means the terms prohibit redistribution of the
# material as it stands; "conditional" means redistribution is allowed only if
# a stated condition is met; "open" means the material is redistributable.
UPSTREAM = {
    "portswigger": {
        "standing": "blocked",
        "why": "Website Terms 7.4 and 7.7: downloads are for personal use only and "
               "no part may be used or shared for commercial purposes without a licence. "
               "7.8 ends the right to use on breach.",
        "source": "portswigger.net/web-security/certification/terms-and-conditions/website-terms-of-use",
    },
    "hackthebox": {
        "standing": "blocked",
        "why": "User Agreement 11.2 grants a limited personal licence for upskilling within "
               "the Services, and 11.4(a) forbids copying, reproducing or distributing any "
               "portion of HTB Content. Academy terms 4 forbids reproduction for any purpose.",
        "source": "resources.hackthebox.com/hubfs/Legal/UA.pdf, academy.hackthebox.com/tos",
    },
    "tryhackme": {
        "standing": "blocked",
        "why": "Terms of Use 3.1: content is for personal use only, and no part may be copied, "
               "aggregated or republished for any commercial purpose without written permission. "
               "Business terms 8(b) forbids reproducing Content to deliver training outside the service.",
        "source": "tryhackme.com/terms, tryhackme.com/legal/business-terms-of-use",
    },
    "mitre": {
        "standing": "conditional",
        "why": "ATT&CK is licensed for research, development and commercial use provided every copy "
               "reproduces the copyright designation and the licence text.",
        "source": "attack.mitre.org/resources/terms-of-use",
        "condition": "© 2026 The MITRE Corporation. This work is reproduced and distributed with "
                     "the permission of The MITRE Corporation.",
    },
    "sans": {
        "standing": "unknown",
        "why": "SANS papers are copyrighted to SANS Institute and the authors. No redistribution "
               "terms were verified, so treat as blocked until read.",
        "source": "not verified",
    },
    "vulnhub": {
        "standing": "unknown",
        "why": "VMs are distributed by their authors under their own terms, which vary per machine.",
        "source": "not verified",
    },
    "owasp": {
        "standing": "conditional",
        "why": "OWASP written material is generally CC BY-SA, which requires attribution and "
               "share-alike. Not verified for this dataset.",
        "source": "not verified",
    },
    "nvd": {
        "standing": "open",
        "why": "NVD data is a US government work and redistributable. Not verified for this dataset.",
        "source": "not verified",
    },
    "cisa": {"standing": "open", "why": "US government work.", "source": "not verified"},
}

# Names that mark a file as evaluation material. Content that sits in a training
# corpus and also on a leaderboard makes the leaderboard meaningless for anyone
# who trains on it.
EVAL_MARKERS = [
    "swe-bench", "swebench", "gpqa", "mmlu", "humaneval", "cybench", "cyberseceval",
    "nyu-ctf", "picoctf", "htb-ctf", "portswigger-lab", "benchmark", "leaderboard",
]

BYTES = {"kb": 1024, "mb": 1024 ** 2, "gb": 1024 ** 3, "tb": 1024 ** 4}


def human(n: int) -> str:
    for unit, scale in (("TB", BYTES["tb"]), ("GB", BYTES["gb"]), ("MB", BYTES["mb"]), ("KB", BYTES["kb"])):
        if abs(n) >= scale:
            return f"{n / scale:,.1f} {unit}"
    return f"{n:,} B"


def parse_size(text: str) -> int | None:
    """Turn '16 GB', '~95 GB', '< 1K' into a byte figure, or None."""
    t = text.lower().replace(",", "").strip()
    t = t.replace("~", "").replace("approximately", "").strip()
    lt = t.startswith("<")
    t = t.lstrip("< ").strip()
    m = re.match(r"([\d.]+)\s*([kmgt]?)(i?b|b)?$", t.replace(" ", ""))
    if not m:
        return None
    value = float(m.group(1))
    unit = m.group(2)
    scale = 1 if unit == "" else BYTES[{"k": "kb", "m": "mb", "g": "gb", "t": "tb"}[unit]]
    size = int(value * scale)
    if lt:
        size = min(size, 999)
    return size


def load_tree(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict) and "tree" in data:
        data = data["tree"]
    if not isinstance(data, list):
        raise ValueError("tree file must be a list of file objects, or an object with a tree key")
    rows = []
    for item in data:
        if not isinstance(item, dict):
            continue
        if item.get("type") not in (None, "file"):
            continue
        path = item.get("path") or item.get("rfilename") or ""
        if not path:
            continue
        size = item.get("size")
        if size is None and isinstance(item.get("lfs"), dict):
            size = item["lfs"].get("size")
        rows.append({"path": path, "size": int(size or 0), "oid": item.get("oid") or ""})
    return rows


def check_inventory(rows: list[dict]) -> dict:
    total = sum(r["size"] for r in rows)
    ext = Counter(os.path.splitext(r["path"])[1].lower() or "<none>" for r in rows)
    top = defaultdict(int)
    for r in rows:
        parts = r["path"].split("/")
        top[parts[0] if len(parts) > 1 else "<root>"] += 1
    empty = [r["path"] for r in rows if r["size"] == 0]
    return {
        "files": len(rows),
        "bytes": total,
        "size": human(total),
        "extensions": dict(ext.most_common()),
        "top_level": dict(sorted(top.items(), key=lambda kv: -kv[1])),
        "empty_files": empty,
        "largest": sorted(rows, key=lambda r: -r["size"])[:10],
    }


def check_claims(rows: list[dict], claims: list[str]) -> dict:
    total = sum(r["size"] for r in rows)
    out = []
    for claim in claims:
        parsed = parse_size(claim)
        out.append({
            "claim": claim,
            "bytes": parsed,
            "agrees": None if parsed is None else abs(parsed - total) <= max(parsed * 0.05, 1),
            "ratio": None if not parsed else round(total / parsed, 2),
        })
    distinct = {c["bytes"] for c in out if c["bytes"]}
    return {
        "claims": out,
        "distinct_figures": len(distinct),
        "worst_ratio": max((c["ratio"] or 1) for c in out) if out else None,
        "consistent": (len(distinct) <= 1) if len(out) > 1 else None,
    }


def check_licence(rows: list[dict], card: str) -> dict:
    text = (card or "").lower()
    hits = {}
    for key, info in UPSTREAM.items():
        if key in text or key.replace("hackthebox", "hackthebox") in text.replace("hack the box", "hackthebox"):
            hits[key] = info
    if "hack the box" in text and "hackthebox" not in hits:
        hits["hackthebox"] = UPSTREAM["hackthebox"]
    blocked = [k for k, v in hits.items() if v["standing"] == "blocked"]
    conditional = [k for k, v in hits.items() if v["standing"] == "conditional"]
    unmet = []
    for k in conditional:
        cond = UPSTREAM[k].get("condition")
        if cond and cond.lower()[:40] not in (card or "").lower():
            unmet.append(k)
    return {
        "sources_found": hits,
        "blocked": blocked,
        "conditional": conditional,
        "conditions_unmet": unmet,
        "verdict": "blocked" if blocked else ("conditional" if conditional else "unknown"),
    }


def check_artefacts(rows: list[dict], unsafe_paths: list[str]) -> dict:
    executables = [r["path"] for r in rows if os.path.splitext(r["path"])[1].lower() in EXECUTABLE_EXT]
    archives = [r["path"] for r in rows if os.path.splitext(r["path"])[1].lower() in ARCHIVE_EXT]
    return {
        "executable_count": len(executables),
        "executable_sample": executables[:25],
        "archive_count": len(archives),
        "archive_sample": archives[:10],
        "platform_flagged": unsafe_paths,
        "platform_flagged_count": len(unsafe_paths),
    }


def check_contamination(rows: list[dict]) -> dict:
    hits = defaultdict(list)
    for r in rows:
        p = r["path"].lower()
        for marker in EVAL_MARKERS:
            if marker in p:
                hits[marker].append(r["path"])
                break
    return {"markers": {k: v[:10] for k, v in hits.items()}, "total": sum(len(v) for v in hits.values())}


def check_json_validity(rows: list[dict], local_dir: str | None) -> dict | None:
    if not local_dir:
        return None
    good = bad = 0
    failures = []
    for r in rows:
        if os.path.splitext(r["path"])[1].lower() not in (".json", ".jsonl"):
            continue
        full = os.path.join(local_dir, r["path"])
        if not os.path.exists(full):
            continue
        try:
            with open(full, encoding="utf-8") as fh:
                if full.endswith(".jsonl"):
                    for line in fh:
                        if line.strip():
                            json.loads(line)
                else:
                    json.load(fh)
            good += 1
        except Exception as exc:  # noqa: BLE001 - the failure is the finding
            bad += 1
            failures.append({"path": r["path"], "error": type(exc).__name__, "detail": str(exc)[:120]})
    return {"valid": good, "invalid": bad, "failures": failures[:40]}


def render(report: dict) -> str:
    inv, claims, lic, art = report["inventory"], report["claims"], report["licence"], report["artefacts"]
    lines = []
    lines.append(f"# Provenance audit: {report['dataset']}")
    lines.append("")
    lines.append(f"Run {report['ran_at']} against the file tree only. Nothing was downloaded.")
    lines.append("")
    lines.append("## 1. Inventory")
    lines.append("")
    lines.append(f"- {inv['files']} files, {inv['size']} in total.")
    lines.append(f"- Extensions: " + ", ".join(f"{k} {v}" for k, v in list(inv["extensions"].items())[:8]))
    if inv["empty_files"]:
        lines.append(f"- {len(inv['empty_files'])} zero-byte files.")
    lines.append("")
    lines.append("## 2. What the card claims")
    lines.append("")
    for c in claims["claims"]:
        mark = "agrees" if c["agrees"] else "does not agree"
        detail = ""
        if c["ratio"] and not c["agrees"]:
            detail = ", off by more than 1,000x" if c["ratio"] > 1000 else f", actual is {c['ratio']}x"
        lines.append(f"- {c['claim']}: {mark}{detail}")
    lines.append("")
    if claims["consistent"] is None:
        lines.append("One figure given, so there is nothing to reconcile.")
    elif claims["consistent"]:
        lines.append("The stated sizes agree with each other.")
    else:
        lines.append(f"**{claims['distinct_figures']} different figures for one quantity.** "
                     "Whichever is right, the card has not been checked by the person who wrote it.")
    lines.append("")
    lines.append("## 3. Licence standing")
    lines.append("")
    for key, info in lic["sources_found"].items():
        lines.append(f"- **{key}**: {info['standing']}. {info['why']}")
        lines.append(f"  - {info['source']}")
    if lic["conditions_unmet"]:
        lines.append("")
        lines.append(f"Conditions not met in the card: {', '.join(lic['conditions_unmet'])}")
    lines.append("")
    lines.append(f"Verdict on redistribution: **{lic['verdict']}**.")
    lines.append("")
    lines.append("## 4. Artefacts that run or unpack")
    lines.append("")
    lines.append(f"- {art['executable_count']} files with an executable or serialising extension.")
    lines.append(f"- {art['archive_count']} archives.")
    lines.append(f"- {art['platform_flagged_count']} files flagged by the platform's own scanner"
                 + (f": {', '.join(art['platform_flagged'])}" if art["platform_flagged"] else "."))
    lines.append("")
    lines.append("## 5. Evaluation overlap")
    lines.append("")
    if report["contamination"]["total"]:
        for marker, paths in report["contamination"]["markers"].items():
            lines.append(f"- {marker}: {len(paths)} path(s), for example {paths[0]}")
    else:
        lines.append("No file paths matched the evaluation markers this tool knows about. "
                     "That is not the same as no overlap: the check is on names, not content.")
    if report.get("json_validity"):
        jv = report["json_validity"]
        lines.append("")
        lines.append(f"JSON validity, read locally: {jv['valid']} valid, {jv['invalid']} invalid.")
    lines.append("")
    lines.append("## What this does not establish")
    lines.append("")
    lines.append("It says nothing about whether the content is accurate, useful or safe. It checks "
                 "what a page says about itself, which is enough to stop a pipeline before it starts "
                 "and not enough to bless one that has.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit a dataset from its file tree, without downloading it.")
    ap.add_argument("--tree", required=True, help="tree.json from the HF API, or a directory listing")
    ap.add_argument("--dataset", default="unknown dataset")
    ap.add_argument("--claim", action="append", default=[], help="a size the card states, repeatable")
    ap.add_argument("--card", default="", help="path to the card text, used for the licence check")
    ap.add_argument("--unsafe", default="", help="file with one platform-flagged path per line")
    ap.add_argument("--local", default=None, help="optional local directory, to test JSON validity")
    ap.add_argument("--json", default=None, help="write the machine-readable report here")
    ap.add_argument("--out", default=None, help="write the markdown report here")
    args = ap.parse_args()

    try:
        rows = load_tree(args.tree)
    except Exception as exc:  # noqa: BLE001
        print(f"could not read the tree: {exc}", file=sys.stderr)
        return 2
    if not rows:
        print("the tree parsed but held no files", file=sys.stderr)
        return 2

    card = ""
    if args.card and os.path.exists(args.card):
        with open(args.card, encoding="utf-8") as fh:
            card = fh.read()

    unsafe = []
    if args.unsafe and os.path.exists(args.unsafe):
        with open(args.unsafe, encoding="utf-8") as fh:
            unsafe = [line.strip() for line in fh if line.strip()]

    report = {
        "dataset": args.dataset,
        "ran_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "inventory": check_inventory(rows),
        "claims": check_claims(rows, args.claim),
        "licence": check_licence(rows, card),
        "artefacts": check_artefacts(rows, unsafe),
        "contamination": check_contamination(rows),
        "json_validity": check_json_validity(rows, args.local),
    }
    report["inventory"]["largest"] = [
        {"path": r["path"], "size": human(r["size"])} for r in report["inventory"]["largest"]
    ]

    text = render(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        print(text)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, default=str)

    blocking = (
        not report["claims"]["consistent"]
        or report["licence"]["verdict"] == "blocked"
        or report["artefacts"]["platform_flagged_count"] > 0
    )
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
