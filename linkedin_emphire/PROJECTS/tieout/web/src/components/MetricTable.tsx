interface Row {
  check: string;
  total: number;
  fired: number;
  undetermined: number;
}

export function MetricTable({
  metrics,
  counts,
}: {
  metrics: Row[];
  counts: { pass: number; fail: number; undetermined: number };
}) {
  return (
    <div className="card">
      <h2>The metric <span className="pill">T5</span></h2>
      <p className="sub">specific failure, sample size, rate. fired comes from heuristic detectors; the raw is in the chain.</p>
      <table className="metric">
        <thead>
          <tr>
            <th>check</th>
            <th>sample</th>
            <th>fired</th>
            <th>rate</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((m) => (
            <tr key={m.check}>
              <td className="mono">{m.check}</td>
              <td className="mono">{m.total}</td>
              <td className="mono">{m.fired}</td>
              <td className="mono">
                {m.fired} of {m.total}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <p className="sub mono">
        total: {counts.pass} pass / {counts.fail} fail / {counts.undetermined} undetermined
      </p>
    </div>
  );
}
