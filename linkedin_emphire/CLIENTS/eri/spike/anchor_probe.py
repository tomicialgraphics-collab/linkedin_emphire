#!/usr/bin/env python3
"""Probe the FORAY anchoring service and record exactly what comes back.

Monday's first job is not to build anything. It is to find out whether a batch of fingerprints returns
something a stranger can open: a transaction id, a block time, and a link that resolves on a public
explorer. This script does that and nothing else.

The point is the record, not the answer. Every run appends one JSON line to anchor-probe.jsonl with the
moment, the endpoint, the request, the status, the headers, the raw body and the sha256 of that body. If
FORAY returns a transaction id, the line proves it. If FORAY returns an error, the line proves that too,
with the exact text, which is what makes a Monday morning conversation useful instead of memorable.

    python3 anchor_probe.py --url https://example.invalid/anchor --dry-run
    python3 anchor_probe.py --url https://example.invalid/anchor
    python3 anchor_probe.py --url ... --explorer https://example.invalid/tx/{tx}

Nothing here guesses FORAY's schema. If the documented shape differs, edit build_request() to match the
documentation and keep the rest. Standard library only, on purpose: it has to run on any machine either
of us picks up on Monday.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta

WAT = timezone(timedelta(hours=1))
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "anchor-probe.jsonl")

# Three fingerprints of known inputs, so the same probe can be run again and compared. These are the
# sha256 of the strings "eri-probe-1", "eri-probe-2" and "eri-probe-3".
KNOWN_INPUTS = ["eri-probe-1", "eri-probe-2", "eri-probe-3"]

# Keys that would count as a transaction id or a block time if they appear in the response. Nothing here
# is asserted; the script reports what it found and what it did not.
TX_KEYS = ("tx", "txid", "tx_id", "transaction", "transaction_id", "hash", "anchor", "reference", "id")
TIME_KEYS = ("block_time", "blocktime", "timestamp", "time", "anchored_at", "confirmed_at")


def fingerprints(inputs=KNOWN_INPUTS):
    return [hashlib.sha256(s.encode()).hexdigest() for s in inputs]


def build_request(fps):
    """The body sent to FORAY. Replace with the documented shape when the documentation is to hand."""
    return {"fingerprints": fps}


def post(url, payload, timeout=20):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "eri-anchor-probe/1"})
    started = datetime.now(timezone.utc)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            status, headers = r.status, dict(r.headers)
    except urllib.error.HTTPError as e:
        raw = e.read()
        status, headers = e.code, dict(e.headers or {})
    except Exception as e:  # noqa: BLE001 - the failure is the finding
        return {"status": None, "headers": {}, "raw": b"", "error": f"{type(e).__name__}: {e}",
                "started": started.isoformat(), "elapsed_ms": None}
    elapsed = int((datetime.now(timezone.utc) - started).total_seconds() * 1000)
    return {"status": status, "headers": headers, "raw": raw, "error": None,
            "started": started.isoformat(), "elapsed_ms": elapsed}


def walk_keys(obj, wanted):
    """Find candidate keys anywhere in a nested response, case insensitive."""
    found = []

    def rec(node, path=""):
        if isinstance(node, dict):
            for k, v in node.items():
                here = f"{path}.{k}" if path else k
                if k.lower() in wanted and not isinstance(v, (dict, list)):
                    found.append((here, v))
                rec(v, here)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                rec(v, f"{path}[{i}]")

    rec(obj)
    return found


def record(line):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True, help="the FORAY anchoring endpoint")
    ap.add_argument("--explorer", default=None,
                    help="explorer URL template containing {tx}, used to test whether a stranger can open it")
    ap.add_argument("--dry-run", action="store_true", help="print the request and write nothing")
    ap.add_argument("--timeout", type=float, default=20)
    args = ap.parse_args()

    fps = fingerprints()
    payload = build_request(fps)
    now = datetime.now(WAT).strftime("%Y-%m-%d %H:%M WAT")

    if args.dry_run:
        print(f"dry run, {now}")
        print(f"endpoint : {args.url}")
        print(f"body     : {json.dumps(payload)}")
        print("nothing sent, nothing written")
        for f in fps:
            print(f"  fingerprint {f}")
        return 0

    res = post(args.url, payload, timeout=args.timeout)
    text = res["raw"].decode("utf-8", "replace")
    parsed, parse_error = None, None
    try:
        parsed = json.loads(text) if text else None
    except json.JSONDecodeError as e:
        parse_error = str(e)

    tx_hits = walk_keys(parsed, set(TX_KEYS)) if parsed is not None else []
    time_hits = walk_keys(parsed, set(TIME_KEYS)) if parsed is not None else []
    explorer_url, explorer_status = None, None
    if args.explorer and tx_hits:
        candidate = str(tx_hits[0][1])
        explorer_url = args.explorer.replace("{tx}", candidate)
        try:
            with urllib.request.urlopen(explorer_url, timeout=args.timeout) as r:
                explorer_status = r.status
        except urllib.error.HTTPError as e:
            explorer_status = e.code
        except Exception as e:  # noqa: BLE001
            explorer_status = f"{type(e).__name__}"

    line = {
        "probed_at": now,
        "endpoint": args.url,
        "request": payload,
        "status": res["status"],
        "error": res["error"],
        "elapsed_ms": res["elapsed_ms"],
        "response_body_sha256": hashlib.sha256(res["raw"]).hexdigest(),
        "response_headers": res["headers"],
        "response_body": text[:4000],
        "parse_error": parse_error,
        "tx_candidates": tx_hits,
        "time_candidates": time_hits,
        "explorer_url": explorer_url,
        "explorer_status": explorer_status,
    }
    record(line)

    print(f"probed {now}")
    print(f"status  : {res['status']}   error: {res['error']}")
    print(f"elapsed : {res['elapsed_ms']} ms")
    print(f"body    : {text[:400] or '(empty)'}")
    print(f"tx keys : {tx_hits or 'none found'}")
    print(f"time keys: {time_hits or 'none found'}")
    if explorer_url:
        print(f"explorer: {explorer_url} -> {explorer_status}")
    print(f"recorded in {LOG}")

    # Exit code is the verdict, so it can be read at a glance on Monday morning.
    verdict = bool(tx_hits) and bool(time_hits) and (explorer_status in (200, None))
    print("VERDICT : " + ("anchoring returns an openable reference" if verdict
                          else "not yet: see the record before promising anything downstream"))
    return 0 if verdict else 2


if __name__ == "__main__":
    sys.exit(main())
