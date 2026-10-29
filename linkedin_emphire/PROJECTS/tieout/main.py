"""Vercel serverless entrypoint (ASGI).

The same app as `tieout serve`, minus uvicorn: Vercel's Python runtime
invokes this ASGI app directly. The runs directory is read from the
deployed function bundle (the committed demo runs).

Two properties of the serverless environment, handled explicitly:

- the filesystem is ephemeral, so the verify endpoint's
  `verify_report.json` write is best-effort (see server.py); the
  report is always returned in the HTTP response, which is what the
  UI consumes
- there are no background workers or websockets: tieout has neither
"""
from pathlib import Path

from tieout.server import create_app

ROOT = Path(__file__).resolve().parent

app = create_app(ROOT / "runs")
