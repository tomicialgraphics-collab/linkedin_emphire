import type { Provenance } from "../types";

function shortHash(h: string | undefined | null, n = 16): string {
  if (!h) return "—";
  return h.length > n ? h.slice(0, n) + "…" : h;
}

export function ProvenanceCard({ provenance: p, policyVersion }: { provenance: Provenance; policyVersion?: string }) {
  return (
    <div className="card">
      <h2>Provenance <span className="pill">P2</span></h2>
      <dl className="kv">
        <dt>harness</dt>
        <dd className="mono">
          {p.harness_version}
          {p.harness_git ? ` (${shortHash(p.harness_git, 10)})` : ""}
        </dd>
        <dt>policy</dt>
        <dd className="mono">{shortHash(policyVersion, 24)}</dd>
        <dt>agent</dt>
        <dd className="mono">{p.agent}</dd>
        <dt>model</dt>
        <dd className="mono">{p.model ?? "none (deterministic agent)"}</dd>
        <dt>dataset</dt>
        <dd className="mono">{shortHash(p.dataset_hash, 24)}</dd>
        <dt>decoding</dt>
        <dd className="mono">{JSON.stringify(p.decoding)}</dd>
        <dt>seed</dt>
        <dd className="mono">{p.seed}</dd>
        <dt>env</dt>
        <dd className="mono small">{p.env.platform} · python {p.env.python}</dd>
      </dl>
    </div>
  );
}
