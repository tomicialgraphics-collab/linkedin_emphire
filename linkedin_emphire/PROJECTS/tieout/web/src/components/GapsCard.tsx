import type { NamedGap } from "../types";

export function GapsCard({ gaps }: { gaps: NamedGap[] }) {
  return (
    <div className="card">
      <h2>
        Named gaps <span className="pill">P4</span>
      </h2>
      <p className="sub">anything that could not be verified is recorded with reason and scope, never dropped silently.</p>
      {gaps.length === 0 ? (
        <p className="ok-text">no named gaps in this bundle. a bundle with a named gap is more honest than a green bundle; this one simply has none.</p>
      ) : (
        <ul className="gap-list">
          {gaps.map((g) => (
            <li key={g.gap_id}>
              <span className="gap-code mono">[{g.code}]</span>{" "}
              <span className="mono small">{g.scope}</span>: {g.reason}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
