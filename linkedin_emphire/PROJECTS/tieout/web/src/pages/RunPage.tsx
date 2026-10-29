import { useEffect, useMemo, useState } from "react";
import { getBundle } from "../api";
import type { Bundle, VerdictEvent } from "../types";
import { VerdictBadge } from "../components/Badge";
import { ProvenanceCard } from "../components/ProvenanceCard";
import { MetricTable } from "../components/MetricTable";
import { VerdictTimeline } from "../components/VerdictTimeline";
import { ControlsCard } from "../components/ControlsCard";
import { GapsCard } from "../components/GapsCard";
import { JudgeAuditCard } from "../components/JudgeAuditCard";
import { VerifyPanel } from "../components/VerifyPanel";

export default function RunPage({ id }: { id: string }) {
  const [bundle, setBundle] = useState<Bundle | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setBundle(null);
    getBundle(id).then(setBundle).catch((e) => setError(String(e)));
  }, [id]);

  const metrics = useMemo(() => {
    if (!bundle) return [];
    const groups = new Map<string, VerdictEvent[]>();
    for (const e of bundle.events) {
      const key = e.check.split("-")[0];
      groups.set(key, [...(groups.get(key) ?? []), e]);
    }
    return [...groups.entries()].map(([check, evs]) => ({
      check,
      total: evs.length,
      fired: evs.filter((e) => e.detector_fired === true).length,
      undetermined: evs.filter((e) => e.decision === "undetermined").length,
    }));
  }, [bundle]);

  if (error) return <div className="empty">could not load run: {error}</div>;
  if (!bundle) return <div className="empty">loading bundle…</div>;

  const p = bundle.manifest.provenance;
  const counts = { pass: 0, fail: 0, undetermined: 0 };
  for (const e of bundle.events) counts[e.decision] += 1;

  return (
    <section>
      <p>
        <a className="back" href="#/">
          ← all runs
        </a>
      </p>
      <div className="run-head">
        <h1 className="mono">{bundle.id}</h1>
        <div className="verdict-group">
          <VerdictBadge v="pass" />
          <VerdictBadge v="fail" />
          <VerdictBadge v="undetermined" />
        </div>
      </div>
      <p className="sub mono">
        {p.agent} · suite {p.suite} · {p.started_at} → {p.finished_at} · {bundle.events.length} events, {bundle.controls.length} controls
      </p>

      <VerifyPanel id={id} />
      <MetricTable metrics={metrics} counts={counts} />
      <VerdictTimeline events={bundle.events} />
      <ControlsCard controls={bundle.controls} fp={bundle.manifest.controls_fp} fn={bundle.manifest.controls_fn} />
      <GapsCard gaps={bundle.gaps} />
      {bundle.judge_audit && <JudgeAuditCard audit={bundle.judge_audit} />}
      <ProvenanceCard provenance={p} policyVersion={p.family_policy_versions[bundle.events[0]?.family ?? ""]} />
    </section>
  );
}
