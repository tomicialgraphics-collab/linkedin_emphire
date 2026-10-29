"use client";

import { useEffect, useState } from "react";
import { getFamiliesDetail } from "../lib/api";
import type { FamilyDetail as FamilyDetailType } from "../lib/types";

const DESCRIPTION: Record<string, React.ReactNode> = {
  F1: (
    <>
      the legacy line of the public five-tests repo (d95a57e), ported unchanged into the evidence
      model: same inputs, same detectors, now emitting chained verdict events.
    </>
  ),
  F2: (
    <>
      the failure-mode matrix, <a href="/matrix">docs/failure-mode-matrix.md</a>, made executable:
      rows E (evidence at decision time), P (persistence), R (recovery), V (independent
      verification) as checks. each check carries one scenario where the sample fixture makes the
      designed break and one where it makes the documented hold; for a live agent the same prompts
      are sent and the verdict is the measurement, not the label.
    </>
  ),
};

export function FamilyDetail({ id }: { id: string }) {
  const [families, setFamilies] = useState<FamilyDetailType[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getFamiliesDetail().then(setFamilies).catch((e) => setError(String(e)));
  }, []);

  if (error) return <div className="empty">could not load families: {error}</div>;
  if (!families) return <div className="empty">loading family…</div>;

  const f = families.find((x) => x.family_id === id);
  if (!f)
    return (
      <div className="empty">
        family {id} is not live yet. F3-F6 are planned against the{" "}
        <a href="/asi">OWASP Agentic crosswalk</a>.
      </div>
    );

  return (
    <section>
      <p>
        <a className="back" href="/families">
          ← families
        </a>
      </p>
      <div className="run-head">
        <h1>
          {f.family_id} · {f.name} <span className="pill">policy {f.policy_label}</span>
        </h1>
      </div>
      <p className="sub mono">
        {f.items} items · {f.controls} negative controls · policy version{" "}
        {f.policy_version.slice(0, 40)}…
      </p>
      <p className="sub">{DESCRIPTION[f.family_id]}</p>

      <div className="card">
        <h2>items</h2>
        <table>
          <thead>
            <tr>
              <th>item id</th>
              <th>check</th>
              <th>action</th>
            </tr>
          </thead>
          <tbody>
            {f.items_detail.map((i) => (
              <tr key={i.id}>
                <td className="mono small">{i.id}</td>
                <td className="mono small">{i.check}</td>
                <td className="small">{i.action}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="sub" style={{ marginTop: 12, marginBottom: 0 }}>
          see it in the record: <a href="/runs/demo-f2">runs/demo-f2</a> is an F2 run;{" "}
          <a href="/runs/demo">runs/demo</a> is the F1 line.
        </p>
      </div>
    </section>
  );
}
