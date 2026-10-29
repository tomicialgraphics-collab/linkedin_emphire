export interface RunSummary {
  id: string;
  run_id: string;
  agent: string;
  suite: string;
  started_at: string;
  events: number;
  controls: number;
  verdicts: Record<string, number>;
  controls_fp: number;
  controls_fn: number;
  gaps: number;
}

export interface VerdictEvent {
  type: string;
  event_id: string;
  item_id: string;
  family: string;
  check: string;
  policy_version: string;
  action: string;
  decision: "pass" | "fail" | "undetermined";
  judge: string;
  judge_endpoint: string;
  target_endpoint: string;
  effect_ref: string;
  raw_input: string;
  raw_output: string;
  detector_fired: boolean | null;
  why: string;
  started_at: string;
  finished_at: string;
  prev_hash: string;
  record_hash: string;
}

export interface ControlEvent {
  type: string;
  control_id: string;
  family: string;
  check: string;
  kind: "known-hold" | "known-broken";
  crafted_raw: string;
  detector: string;
  expected_fire: boolean;
  fired: boolean | null;
  verdict: "pass" | "fail";
  note: string;
  prev_hash: string;
  record_hash: string;
}

export interface NamedGap {
  type: string;
  gap_id: string;
  code: string;
  scope: string;
  reason: string;
}

export interface Provenance {
  harness_version: string;
  harness_git: string;
  suite: string;
  family_policy_versions: Record<string, string>;
  agent: string;
  model: string | null;
  model_version: string | null;
  dataset_hash: string;
  env: Record<string, string>;
  decoding: Record<string, unknown>;
  seed: number;
  started_at: string;
  finished_at: string;
}

export interface JudgeAudit {
  type: string;
  judge: string;
  anchors_total: number;
  anchors_agreement: number;
  perturbation_samples: number;
  perturbation_flips: Record<string, number>;
  disagreement_rate: number;
  self_preference_clean: boolean;
  details: Record<string, unknown>[];
}

export interface Manifest {
  type: string;
  bundle_format: string;
  run_id: string;
  provenance: Provenance;
  expected_item_ids: string[];
  emitted_item_ids: string[];
  event_count: number;
  control_count: number;
  tail_event_hash: string;
  controls_fp: number;
  controls_fn: number;
}

export interface Bundle {
  id: string;
  manifest: Manifest;
  events: VerdictEvent[];
  controls: ControlEvent[];
  judge_audit: JudgeAudit | null;
  gaps: NamedGap[];
}

export interface VerifyResult {
  lines: string[];
  gaps: NamedGap[];
  verdict: "PASS" | "FAIL";
  ok: boolean;
}
