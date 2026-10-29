"use client";

import { useEffect, useState } from "react";
import { getAsi } from "../lib/api";
import type { AsiData } from "../lib/types";

export function AsiPage() {
  const [asi, setAsi] = useState<AsiData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getAsi().then(setAsi).catch((e) => setError(String(e)));
  }, []);

  if (error) return <div className="empty">could not load the crosswalk: {error}</div>;
  if (!asi) return <div className="empty">loading crosswalk…</div>;

  return (
    <section>
      <p>
        <a className="back" href="/">
          ← home
        </a>
      </p>
      <div className="run-head">
        <h1>
          OWASP Agentic crosswalk <span className="pill">ASI01-ASI10</span>
        </h1>
      </div>
      <p className="sub">
        record-derived: which threat each family covers today, and which are planned. the sub-check
        mapping below is marked proposed, per the project&apos;s own P4 doctrine: a proposed
        mapping is data, not a claim.
      </p>

      <div className="card">
        <h2>threat → families</h2>
        <table>
          <thead>
            <tr>
              <th>asi</th>
              <th>title</th>
              <th>families</th>
              <th>status</th>
            </tr>
          </thead>
          <tbody>
            {asi.crosswalk.map((r) => (
              <tr key={r.asi}>
                <td className="mono">{r.asi}</td>
                <td className="small">{r.title}</td>
                <td className="small">{r.families.join(", ") || "—"}</td>
                <td className="small">{r.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="card">
        <h2>
          sub-check mapping <span className="pill">proposed</span>
        </h2>
        <div className="raw-label">F1 (five checks)</div>
        <table>
          <thead>
            <tr>
              <th>check</th>
              <th>name</th>
              <th>proposed asi</th>
              <th>status</th>
            </tr>
          </thead>
          <tbody>
            {asi.f1_proposed.map((r) => (
              <tr key={r.check}>
                <td className="mono">{r.check}</td>
                <td className="small">{r.name}</td>
                <td className="small">{r.proposed_asi}</td>
                <td className="small">{r.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <div className="raw-label">F2 (state and recovery)</div>
        <table>
          <thead>
            <tr>
              <th>check</th>
              <th>name</th>
              <th>proposed asi</th>
              <th>status</th>
            </tr>
          </thead>
          <tbody>
            {asi.f2_proposed.map((r) => (
              <tr key={r.check}>
                <td className="mono">{r.check}</td>
                <td className="small">{r.name}</td>
                <td className="small">{r.proposed_asi}</td>
                <td className="small">{r.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="sub" style={{ marginTop: 12, marginBottom: 0 }}>
          <a href="/families">open the families →</a>
        </p>
      </div>
    </section>
  );
}
