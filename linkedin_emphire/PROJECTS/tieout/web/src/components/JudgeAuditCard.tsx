import type { JudgeAudit } from "../types";

function pct(x: number): string {
  return (100 * x).toFixed(1) + "%";
}

export function JudgeAuditCard({ audit }: { audit: JudgeAudit }) {
  return (
    <div className="card">
      <h2>
        Judge audit <span className="pill">P6</span>{" "}
        <span className={audit.self_preference_clean ? "ok-text" : "bad-text"}>
          self-preference {audit.self_preference_clean ? "clean" : "DIRTY"}
        </span>
      </h2>
      <p className="sub">who checks the checker: the judge's own numbers, measured offline on crafted, versioned anchors.</p>
      <dl className="kv">
        <dt>judge</dt>
        <dd className="mono small">{audit.judge}</dd>
        <dt>anchors</dt>
        <dd className="mono">{audit.anchors_total}</dd>
        <dt>anchor agreement</dt>
        <dd className="mono">{pct(audit.anchors_agreement)}</dd>
        <dt>perturbation flips</dt>
        <dd className="mono">
          {Object.entries(audit.perturbation_flips)
            .map(([k, v]) => `${k}=${v}`)
            .join("  ")}
        </dd>
        <dt>disagreement rate (primary vs naive)</dt>
        <dd className="mono">{pct(audit.disagreement_rate)}</dd>
      </dl>
      {audit.details.length > 0 && (
        <div>
          <div className="raw-label">audit details</div>
          <pre className="code">{JSON.stringify(audit.details, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
