"use client";

import { useEffect, useState } from "react";
import { getRuns } from "../lib/api";
import type { RunSummary } from "../lib/types";
import { VerdictBadge } from "../components/Badge";
import { RunDetail } from "../components/RunDetail";

function useHashRoute(): string {
  const [hash, setHash] = useState("");
  useEffect(() => {
    const update = () => setHash(window.location.hash);
    update();
    window.addEventListener("hashchange", update);
    return () => window.removeEventListener("hashchange", update);
  }, []);
  return hash;
}

function RunList() {
  const [runs, setRuns] = useState<RunSummary[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getRuns().then(setRuns).catch((e) => setError(String(e)));
  }, []);

  if (error) return <div className="empty">could not load runs: {error}</div>;
  if (!runs) return <div className="empty">loading runs…</div>;
  if (runs.length === 0)
    return (
      <div className="empty">
        no runs yet
        <pre className="code">
          {`tieout demo        # keyless, deterministic sample agent
tieout verify runs/demo`}
        </pre>
      </div>
    );

  return (
    <section>
      <h1>Runs</h1>
      <p className="sub">
        each row is an evidence bundle: the verdicts, the controls, the named gaps, the judge's own
        numbers
      </p>
      <table>
        <thead>
          <tr>
            <th>run</th>
            <th>agent</th>
            <th>started (utc)</th>
            <th>verdicts</th>
            <th>controls</th>
            <th>gaps</th>
            <th />
          </tr>
        </thead>
        <tbody>
          {runs.map((r) => (
            <tr key={r.id}>
              <td className="mono">
                <a href={`#/run/${encodeURIComponent(r.id)}`}>{r.id}</a>
              </td>
              <td className="mono small">{r.agent}</td>
              <td className="mono small">{r.started_at}</td>
              <td>
                <span className="verdict-group">
                  {r.verdicts.pass != null && <VerdictBadge v="pass" />}
                  {r.verdicts.fail != null && <VerdictBadge v="fail" />}
                  {r.verdicts.undetermined != null && <VerdictBadge v="undetermined" />}
                </span>
              </td>
              <td className="mono small">
                {r.controls} / fp {r.controls_fp} / fn {r.controls_fn}
              </td>
              <td>
                {r.gaps === 0 ? (
                  <span className="ok-dot" title="no named gaps" />
                ) : (
                  <span className="gap-pill">{r.gaps}</span>
                )}
              </td>
              <td>
                <a className="btn" href={`#/run/${encodeURIComponent(r.id)}`}>
                  open
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

export default function Home() {
  const hash = useHashRoute();
  const match = hash.match(/^#\/run\/(.+)$/);

  return (
    <div className="app">
      <header className="topbar">
        <a className="brand" href="#/">
          tieout
        </a>
        <span className="tagline">
          the report is a claim. the bundle is a record a stranger can re-derive.
        </span>
      </header>
      <main>{match ? <RunDetail id={decodeURIComponent(match[1])} /> : <RunList />}</main>
      <footer className="footer">
        p1 verdict event · p2 provenance · p3 negative controls · p4 named gaps · p5 re-derivation ·
        p6 judge audit
      </footer>
    </div>
  );
}
