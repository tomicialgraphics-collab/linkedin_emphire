import { useState } from "react";
import { verifyRun } from "../api";
import type { VerifyResult } from "../types";

export function VerifyPanel({ id }: { id: string }) {
  const [result, setResult] = useState<VerifyResult | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function runVerify() {
    setBusy(true);
    setError(null);
    try {
      setResult(await verifyRun(id));
    } catch (e) {
      setError(String(e));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="card">
      <h2>
        Stranger verify <span className="pill">P5</span>
      </h2>
      <p className="sub">
        re-walks the hash chain, re-hashes the manifest, re-derives every verdict from the stored raw. no model,
        no key, no network.
      </p>
      <div className="verify-row">
        <button className="btn primary" onClick={runVerify} disabled={busy}>
          {busy ? "verifying…" : "run verify"}
        </button>
        {result && (
          <span className={result.ok ? "ok-text big" : "bad-text big"}>
            {result.verdict}
            {result.ok ? " (re-derivable by a stranger)" : ""}
          </span>
        )}
      </div>
      {error && <p className="bad-text">{error}</p>}
      {result && <pre className="code verify-out">{result.lines.join("\n")}</pre>}
    </div>
  );
}
