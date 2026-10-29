"""FastAPI server: bundle browser + stranger verify over HTTP.

The UI is a viewer for tieout's own evidence bundles, not an LLM
observability dashboard: it renders the record and runs the P5
re-derivation. Bind to 0.0.0.0 when the port is published.
"""
from __future__ import annotations

import json
import stat
from pathlib import Path

import anyio
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from . import __version__
from .bundle.verify import verify_bundle
from .diff import DiffError, diff_bundles
from .harness import get_family, list_families
from .mappings import ASI_CROSSWALK, F1_PROPOSED_MAPPING, F2_PROPOSED_MAPPING


def create_app(runs_dir: str | Path, root: str | Path | None = None) -> FastAPI:
    runs_dir = Path(runs_dir)
    # Explicit deployment root for serverless bundles: the app may be
    # imported from an installed wheel (site-packages), where __file__
    # no longer points at the deployed tree. Local use and the CLI keep
    # the __file__ default.
    root = Path(root) if root else Path(__file__).resolve().parent.parent
    app = FastAPI(title="tieout", version=__version__)

    def _load(run_id: str):
        d = runs_dir / run_id
        if not d.is_dir() or not (d / "bundle.jsonl").exists():
            raise HTTPException(status_code=404, detail=f"run {run_id!r} not found")
        lines = [
            json.loads(line)
            for line in (d / "bundle.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        manifest = lines[0]
        rest = lines[1:]
        return (
            d,
            manifest,
            [ln for ln in rest if ln.get("type") == "event"],
            [ln for ln in rest if ln.get("type") == "control"],
            next((ln for ln in rest if ln.get("type") == "judge_audit"), None),
            [ln for ln in rest if ln.get("type") == "gap"],
        )

    @app.get("/api/health")
    def health() -> dict:
        return {"ok": True, "version": __version__}

    @app.get("/api/runs")
    def runs() -> list[dict]:
        out = []
        if runs_dir.exists():
            # runs may be nested (e.g. runs/demo-stability/a): enumerate
            # every directory that carries a bundle, at any depth
            for b in sorted(runs_dir.rglob("bundle.jsonl")):
                name = b.parent.relative_to(runs_dir).as_posix()
                _, manifest, events, controls, _audit, gaps = _load(name)
                verdicts: dict[str, int] = {}
                for e in events:
                    verdicts[e["decision"]] = verdicts.get(e["decision"], 0) + 1
                stats = manifest.get("statistics") or []
                out.append(
                    {
                        "id": name,
                        "run_id": manifest.get("run_id"),
                        "agent": manifest.get("provenance", {}).get("agent"),
                        "suite": manifest.get("provenance", {}).get("suite"),
                        "started_at": manifest.get("provenance", {}).get("started_at"),
                        "bundle_format": manifest.get("bundle_format"),
                        "seed": manifest.get("provenance", {}).get("seed", 0),
                        "events": len(events),
                        "controls": len(controls),
                        "verdicts": verdicts,
                        "controls_fp": manifest.get("controls_fp", 0),
                        "controls_fn": manifest.get("controls_fn", 0),
                        "gaps": len(gaps),
                        "statistics": stats,
                    }
                )
        return out

    # `{run_id:path}`: run ids may be nested (e.g. `demo-stability/a`);
    # the default parameter converter stops at a slash and would 404
    @app.get("/api/runs/{run_id:path}")
    def run_detail(run_id: str) -> dict:
        d, manifest, events, controls, audit, gaps = _load(run_id)
        return {
            "id": d.name,
            "manifest": manifest,
            "events": events,
            "controls": controls,
            "judge_audit": audit,
            "gaps": gaps,
        }

    @app.post("/api/runs/{run_id:path}/verify")
    def verify_run(run_id: str) -> dict:
        d, manifest, events, controls, _audit, _gaps = _load(run_id)
        fam_id = events[0].get("family") if events else None
        family = get_family(fam_id) if fam_id else None
        res = verify_bundle(d, family=family)
        report = {
            "lines": res.lines,
            "gaps": [g.model_dump() for g in res.gaps],
            "verdict": res.verdict,
            "ok": res.ok,
        }
        # Best-effort: on serverless deploys (Vercel) the filesystem is
        # ephemeral and read-only, so the persisted report may not
        # survive. The report is always returned in the response, which
        # is what the UI consumes; the write exists for the local and
        # container deployments where the runs directory is real.
        try:
            (d / "verify_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        except OSError:
            pass
        return report

    @app.get("/api/families")
    def families() -> list[dict]:
        return [
            {
                "family_id": f.family_id,
                "name": f.name,
                "policy_label": f.policy_label,
                "policy_version": f.policy_version,
                "items": len(f.items),
                "controls": len(f.controls),
                "item_ids": f.item_ids(),
                "items_detail": [
                    {"id": i.item_id, "check": i.check, "action": i.action} for i in f.items
                ],
            }
            for f in list_families()
        ]

    @app.get("/api/docs")
    def docs() -> dict:
        base = root / "docs"
        return {
            key: path.read_text(encoding="utf-8") if path.exists() else ""
            for key, path in {
                "method": base / "method-note.md",
                "format": base / "bundle-format-v1.md",
                "matrix": base / "failure-mode-matrix.md",
                "harness": base / "harness-spec.md",
                "changelog": root / "CHANGELOG.md",
                "security": root / "SECURITY.md",
                "contributing": root / "CONTRIBUTING.md",
                "license": root / "LICENSE",
            }.items()
        }

    @app.get("/api/asi")
    def asi() -> dict:
        return {
            "crosswalk": ASI_CROSSWALK,
            "f1_proposed": F1_PROPOSED_MAPPING,
            "f2_proposed": F2_PROPOSED_MAPPING,
        }

    @app.get("/api/diff")
    def diff(a: str, b: str) -> dict:
        for rid in (a, b):
            d = runs_dir / rid
            if not d.is_dir() or not (d / "bundle.jsonl").exists():
                raise HTTPException(status_code=404, detail=f"run {rid!r} not found")
        try:
            return diff_bundles(runs_dir / a, runs_dir / b)
        except DiffError as e:
            raise HTTPException(status_code=400, detail=str(e)) from None

    dist = root / "web" / "out"
    if dist.exists():
        app.mount("/", StaticExport(directory=dist, html=True), name="ui")
    return app


class StaticExport(StaticFiles):
    """StaticFiles with Next.js static-export route resolution.

    A Next export writes `/runs` to `out/runs.html` and `/runs/demo`
    to `out/runs/demo.html`: extensionless, and a route file can share
    its name with a directory of detail pages. Plain StaticFiles only
    resolves exact files and directory indexes, so those routes would
    404. This adds the resolution order static hosts use: the exact
    file, then `<path>.html`, then `<path>/index.html`, then the
    404 page.
    """

    async def get_response(self, path: str, scope: dict) -> object:
        full_path, stat_result = await anyio.to_thread.run_sync(self.lookup_path, path)
        already_resolved = (
            stat_result is not None
            and stat.S_ISREG(stat_result.st_mode)
        ) or (
            self.html
            and stat_result is not None
            and stat.S_ISDIR(stat_result.st_mode)
            and await anyio.to_thread.run_sync(self._has_index, path)
        )
        if (
            not already_resolved
            and self.html
            and scope["method"] in ("GET", "HEAD")
            and "." not in path.rsplit("/", 1)[-1]
        ):
            for candidate in (path + ".html", path.rstrip("/") + "/index.html"):
                cand_path, cand_stat = await anyio.to_thread.run_sync(
                    self.lookup_path, candidate
                )
                if cand_stat is not None and stat.S_ISREG(cand_stat.st_mode):
                    return self.file_response(cand_path, cand_stat, scope)
        return await super().get_response(path, scope)

    def _has_index(self, path: str) -> bool:
        _full, stat_result = self.lookup_path(path.rstrip("/") + "/index.html")
        return stat_result is not None and stat.S_ISREG(stat_result.st_mode)
