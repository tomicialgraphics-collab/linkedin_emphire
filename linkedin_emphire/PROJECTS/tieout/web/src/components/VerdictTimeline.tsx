import { useState } from "react";
import type { VerdictEvent } from "../types";
import { VerdictBadge } from "./Badge";

function short(h: string, n = 10): string {
  return h.length > n ? h.slice(0, n) + "…" : h;
}

export function VerdictTimeline({ events }: { events: VerdictEvent[] }) {
  const [open, setOpen] = useState<string | null>(null);
  return (
    <div className="card">
      <h2>Verdict events <span className="pill">P1</span></h2>
      <p className="sub">
        one record per check: action, policy version, decision, effect reference, in one event, chained.
      </p>
      <ol className="chain">
        {events.map((e, i) => (
          <li key={e.event_id} className="chain-item">
            <button
              className={open === e.item_id ? "chain-row chain-open" : "chain-row"}
              onClick={() => setOpen(open === e.item_id ? null : e.item_id)}
            >
              <span className="idx mono">{String(i + 1).padStart(2, "0")}</span>
              <span className="mono item-id">{e.item_id}</span>
              <VerdictBadge v={e.decision} />
              <span className="why">{e.why}</span>
              <span className="hash mono" title={e.record_hash}>
                {short(e.record_hash)}
              </span>
            </button>
            {open === e.item_id && (
              <div className="chain-detail">
                <div className="kv">
                  <dt>action</dt>
                  <dd>{e.action}</dd>
                  <dt>judge</dt>
                  <dd className="mono small">{e.judge}</dd>
                  <dt>judge endpoint</dt>
                  <dd className="mono small">{e.judge_endpoint}</dd>
                  <dt>target endpoint</dt>
                  <dd className="mono small">{e.target_endpoint}</dd>
                  <dt>effect ref</dt>
                  <dd className="mono small">{e.effect_ref}</dd>
                  <dt>times</dt>
                  <dd className="mono small">
                    {e.started_at} → {e.finished_at}
                  </dd>
                  <dt>prev hash</dt>
                  <dd className="mono small">{short(e.prev_hash, 20)}</dd>
                </div>
                <div className="raw">
                  <div className="raw-label">input</div>
                  <pre className="code">{tryPretty(e.raw_input)}</pre>
                  <div className="raw-label">raw output</div>
                  <pre className="code">{e.raw_output}</pre>
                </div>
              </div>
            )}
          </li>
        ))}
      </ol>
    </div>
  );
}

function tryPretty(s: string): string {
  try {
    return JSON.stringify(JSON.parse(s), null, 2);
  } catch {
    return s;
  }
}
