"""Serverless deployment contract (Vercel and peers).

The repo must deploy as-is: a root ASGI entry (main.py) that serves the
same app as `tieout serve`, and a verify endpoint that stays correct
when the filesystem is ephemeral and read-only.
"""
import shutil
from pathlib import Path

from fastapi.testclient import TestClient
from test_server import make_client

from tieout.server import create_app


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


def test_explicit_root_serves_content_from_deployment_tree(tmp_path):
    """Simulates the serverless layout: tieout is installed as a wheel
    in the function's venv, so the app's __file__ points into
    site-packages. All content must then come from the explicit
    deployment root, exactly like main.py passes it."""
    root = tmp_path / "deploy"
    (root / "docs").mkdir(parents=True)
    (root / "runs").mkdir()
    repo_runs = Path(__file__).resolve().parent.parent / "runs"
    shutil.copytree(repo_runs / "demo", root / "runs" / "demo")
    (root / "docs" / "method-note.md").write_text(
        "# Method note\n\nfrom the deployment tree\n", encoding="utf-8"
    )
    (root / "docs" / "bundle-format-v1.md").write_text("# Bundle format\n", encoding="utf-8")
    (root / "docs" / "failure-mode-matrix.md").write_text("# Matrix\n", encoding="utf-8")
    (root / "docs" / "harness-spec.md").write_text("# Harness\n", encoding="utf-8")
    (root / "CHANGELOG.md").write_text("# Changelog\n\nfrom the deployment tree\n", encoding="utf-8")
    (root / "SECURITY.md").write_text("# Security\n", encoding="utf-8")
    (root / "CONTRIBUTING.md").write_text("# Contributing\n", encoding="utf-8")
    (root / "LICENSE").write_text("MIT License\n", encoding="utf-8")

    c = TestClient(create_app(root / "runs", root=root))
    docs = c.get("/api/docs").json()
    assert "deployment tree" in docs["method"]
    assert "deployment tree" in docs["changelog"]
    assert set(docs) == {
        "method", "format", "matrix", "harness",
        "changelog", "security", "contributing", "license",
    }
    runs = {r["id"] for r in c.get("/api/runs").json()}
    assert runs == {"demo"}
    assert c.post("/api/runs/demo/verify").json()["verdict"] == "PASS"


def test_static_export_serves_extensionless_routes(tmp_path):
    """The static mount must resolve Next.js export routes: a route file
    can share its name with a directory of detail pages (runs.html next
    to runs/demo.html), and neither carries the .html extension."""
    root = tmp_path / "deploy"
    (root / "runs").mkdir(parents=True)
    web = root / "web" / "out"
    (web / "runs").mkdir(parents=True)
    (web / "blog").mkdir()
    (web / "index.html").write_text("<title>home</title>", encoding="utf-8")
    (web / "runs.html").write_text("<title>runs list</title>", encoding="utf-8")
    (web / "runs" / "demo.html").write_text("<title>run demo</title>", encoding="utf-8")
    (web / "blog.html").write_text("<title>writing</title>", encoding="utf-8")
    (web / "blog" / "surface-drift.html").write_text(
        "<title>surface drift</title>", encoding="utf-8"
    )
    (web / "404.html").write_text("not found page", encoding="utf-8")
    asset = web / "_next" / "static"
    asset.mkdir(parents=True)
    (asset / "chunk.js").write_text("console.log(1)", encoding="utf-8")

    c = TestClient(create_app(root / "runs", root=root))
    assert c.get("/").status_code == 200
    r = c.get("/runs")
    assert r.status_code == 200
    assert "runs list" in r.text
    r = c.get("/runs/demo")
    assert r.status_code == 200
    assert "run demo" in r.text
    assert c.get("/blog").status_code == 200
    r = c.get("/blog/surface-drift")
    assert r.status_code == 200
    assert "surface drift" in r.text
    assert c.get("/_next/static/chunk.js").status_code == 200
    r = c.get("/blog/none")
    assert r.status_code == 404
    assert "not found page" in r.text


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
