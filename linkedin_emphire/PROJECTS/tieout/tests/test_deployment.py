"""Serverless deployment contract (Vercel and peers).

The repo must deploy as-is: a root ASGI entry (main.py) that serves the
same app as `tieout serve`, and a verify endpoint that stays correct
when the filesystem is ephemeral and read-only.
"""
from pathlib import Path

from fastapi.testclient import TestClient
from test_server import make_client


def test_vercel_entry_serves_the_app():
    import main

    c = TestClient(main.app)
    assert c.get("/api/health").status_code == 200
    assert c.get("/api/health").json()["ok"] is True
    ids = {r["id"] for r in c.get("/api/runs").json()}
    # the committed evidence runs must be readable from the deployed tree
    assert {"demo", "demo-f2", "demo-stability/a", "demo-stability/b"} <= ids
    assert c.get("/api/docs").status_code == 200
    assert c.get("/api/families").status_code == 200
    # nested run ids must be routable on detail, verify and diff
    by_id = {r["id"]: r for r in c.get("/api/runs").json()}
    det = c.get("/api/runs/demo-stability/a")
    assert det.status_code == 200
    assert det.json()["manifest"]["run_id"] == by_id["demo-stability/a"]["run_id"]
    assert len(det.json()["events"]) == by_id["demo-stability/a"]["events"]
    ver = c.post("/api/runs/demo-stability/a/verify")
    assert ver.status_code == 200
    assert ver.json()["ok"] is True
    d = c.get("/api/diff", params={"a": "demo-stability/a", "b": "demo-stability/b"})
    assert d.status_code == 200
    assert d.json()["stability"] == 1.0
    assert d.json()["verdict_flips"] == 0


def test_verify_report_persisted_when_writable(tmp_path):
    c = make_client(tmp_path)
    r = c.post("/api/runs/demo/verify")
    assert r.status_code == 200
    assert (tmp_path / "runs/demo/verify_report.json").exists()


def test_verify_stays_correct_on_readonly_filesystem(tmp_path, monkeypatch):
    """Simulates the serverless filesystem: the write fails, the report
    must still be complete in the response (the UI consumes the
    response, not the file)."""
    c = make_client(tmp_path)
    orig = Path.write_text

    def boom(self, *args, **kwargs):
        if self.name == "verify_report.json":
            raise PermissionError("read-only filesystem (simulated serverless)")
        return orig(self, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", boom)
    r = c.post("/api/runs/demo/verify")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["verdict"] == "PASS"
    assert body["lines"]
    assert not (tmp_path / "runs/demo/verify_report.json").exists()
