
from fastapi.testclient import TestClient

from tieout.harness import get_family
from tieout.harness.agents import SampleOrderBot
from tieout.harness.runner import run_suite
from tieout.server import create_app


def make_client(tmp_path):
    runs = tmp_path / "runs"
    run_suite(get_family("F1"), SampleOrderBot(), out_dir=runs / "demo")
    return TestClient(create_app(runs))


def test_health(tmp_path):
    c = make_client(tmp_path)
    r = c.get("/api/health")
    assert r.status_code == 200
    assert r.json()["ok"] is True


def test_runs_list_and_detail(tmp_path):
    c = make_client(tmp_path)
    runs = c.get("/api/runs").json()
    assert len(runs) == 1
    assert runs[0]["events"] == 14
    assert runs[0]["verdicts"]["pass"] == 13
    assert runs[0]["verdicts"]["fail"] == 1

    detail = c.get("/api/runs/demo").json()
    assert detail["manifest"]["bundle_format"] == "tieout-bundle/v1"
    assert len(detail["events"]) == 14
    assert len(detail["controls"]) == 8
    assert detail["judge_audit"]["anchors_total"] >= 12
    assert detail["gaps"] == []


def test_verify_endpoint(tmp_path):
    c = make_client(tmp_path)
    r = c.post("/api/runs/demo/verify")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["verdict"] == "PASS"
    assert any(line.startswith("VERDICT: PASS") for line in body["lines"])


def test_families_and_asi(tmp_path):
    c = make_client(tmp_path)
    fams = c.get("/api/families").json()
    assert fams[0]["family_id"] == "F1"
    assert fams[0]["items"] == 14
    assert fams[0]["controls"] == 8
    asi = c.get("/api/asi").json()
    assert {row["asi"] for row in asi["crosswalk"]} == {"ASI01", "ASI02", "ASI03", "ASI06", "ASI09", "ASI10"}
