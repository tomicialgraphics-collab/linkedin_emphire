import type { ControlEvent } from "../types";
import { VerdictBadge } from "./Badge";

export function ControlsCard({
  controls,
  fp,
  fn,
}: {
  controls: ControlEvent[];
  fp: number;
  fn: number;
}) {
  return (
    <div className="card">
      <h2>
        Negative controls <span className="pill">P3</span>{" "}
        <span className={fp + fn === 0 ? "ok-text" : "bad-text"}>
          {fp} FP / {fn} FN
        </span>
      </h2>
      <p className="sub">
        the check cannot write its own grade: these crafted items are graded by the same detectors, and the
        harness's false-positive / false-negative rate for this run is in the manifest.
      </p>
      <table className="metric">
        <thead>
          <tr>
            <th>control</th>
            <th>check</th>
            <th>kind</th>
            <th>expected</th>
            <th>fired</th>
            <th>verdict</th>
          </tr>
        </thead>
        <tbody>
          {controls.map((c) => (
            <tr key={c.control_id} title={c.note}>
              <td className="mono small">{c.control_id}</td>
              <td className="mono">{c.check}</td>
              <td>{c.kind}</td>
              <td className="mono">{String(c.expected_fire)}</td>
              <td className="mono">{String(c.fired)}</td>
              <td>
                <VerdictBadge v={c.verdict} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
