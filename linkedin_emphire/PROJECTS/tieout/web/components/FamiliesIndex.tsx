"use client";

import { useEffect, useState } from "react";
import { getFamiliesDetail } from "../lib/api";
import type { FamilyDetail } from "../lib/types";

const BLURB: Record<string, string> = {
  F1: "the legacy line of the public five-tests repo, ported unchanged into the evidence model",
  F2: "the failure-mode matrix made executable: rows E, P, R, V as checks with their own controls",
};

export function FamiliesIndex() {
  const [families, setFamilies] = useState<FamilyDetail[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getFamiliesDetail().then(setFamilies).catch((e) => setError(String(e)));
  }, []);

  if (error) return <div className="empty">could not load families: {error}</div>;
  if (!families) return <div className="empty">loading families…</div>;

  return (
    <section>
      <p>
        <a className="back" href="/">
          ← home
        </a>
      </p>
      <div className="run-head">
        <h1>Check families</h1>
      </div>
      <p className="sub">
        a family is content: items + policy version + verdict emitter + negative controls. F1 and
        F2 are live; F3-F6 are planned against the{" "}
        <a href="/asi">OWASP Agentic crosswalk</a>.
      </p>

      {families.map((f) => (
        <div key={f.family_id} className="card">
          <h2>
            <a href={`/families/${f.family_id.toLowerCase()}`}>
              {f.family_id} · {f.name}
            </a>{" "}
            <span className="pill">policy {f.policy_label}</span>
          </h2>
          <p className="sub mono">
            {f.items} items · {f.controls} negative controls
          </p>
          <p className="sub" style={{ marginBottom: 0 }}>
            {BLURB[f.family_id] ?? ""}
          </p>
        </div>
      ))}

      <div className="card">
        <h2>
          where they sit <span className="pill">crosswalk</span>
        </h2>
        <p className="sub" style={{ marginBottom: 0 }}>
          every check maps to OWASP Agentic AI Threats; the sub-check mapping is marked proposed,
          per the project&apos;s own P4 doctrine. <a href="/asi">open the crosswalk →</a>
        </p>
      </div>
    </section>
  );
}
