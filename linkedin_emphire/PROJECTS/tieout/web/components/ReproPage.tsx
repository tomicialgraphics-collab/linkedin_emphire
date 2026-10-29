"use client";

import type { ReactNode } from "react";

const SETUP = `git clone https://github.com/Teamthy/Tie-out-
cd Tie-out
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"`;

const RUNS = [
  `python -m tieout verify runs/demo
python -m tieout verify runs/demo-f2
python -m tieout verify runs/demo-stability/a
python -m tieout verify runs/demo-stability/b
python -m tieout diff runs/demo-stability/a runs/demo-stability/b`,
] as const;

function Step({ n, title, children }: { n: string; title: string; children: ReactNode }) {
  return (
    <div className="card">
      <h2>
        {n} · {title}
      </h2>
      {children}
    </div>
  );
}

export function ReproPage() {
  return (
    <section>
      <p>
        <a className="back" href="/">
          ← home
        </a>
      </p>
      <div className="run-head">
        <h1>
          Reproduce <span className="pill">cold clone, no keys</span>
        </h1>
      </div>
      <p className="sub">
        everything on this site is derived from four committed bundles. this page is the
        reproduction procedure: the exact commands and the exact expected output. if any line
        differs, the claim is broken and the difference is the finding.
      </p>

      <Step n="01" title="setup">
        <p className="sub">python 3.10 or newer. no model, no api key, no network calls at verify time.</p>
        <pre className="code">{SETUP}</pre>
        <p className="sub" style={{ marginBottom: 0 }}>
          the harness selftest is 8 points; all must pass before anything else is believed.
        </p>
      </Step>

      <Step n="02" title="verify the four committed runs">
        <pre className="code">{RUNS[0]}</pre>
        <p className="sub">
          each <code>verify</code> re-walks the hash chain, re-hashes the manifest, re-runs the
          detectors on the stored raw, re-derives the statistics. expected, verbatim:
        </p>
        <pre className="code">
          {`tieout verify: runs/demo
  format : tieout-bundle/v1
  agent  : sample:deterministic-orderbot
  chain  : 22 records, intact
  items  : 14/14 pre-assigned ids present
  re-derive: 14/14 verdicts re-derived from stored raw
  controls: 8 re-derived, 0 FP / 0 FN
  gaps   : none
  VERDICT: PASS (re-derivable by a stranger)

  (demo-f2: format tieout-bundle/v1.1, 8/8 items, 8 controls 0 FP / 0 FN, VERDICT: PASS)
  (demo-stability/a and /b: 14/14 items, 8 controls 0 FP / 0 FN, VERDICT: PASS)`}
        </pre>
      </Step>

      <Step n="03" title="the stability pair">
        <p className="sub">the same F1 suite, two seeds, one record of their agreement:</p>
        <pre className="code">
          {`python -m tieout diff runs/demo-stability/a runs/demo-stability/b
  aligned    : 14 items (by pre-assigned id)
  verdicts   : 0 flipped, 14 stable  ->  stability 1.000
  transcripts: 10 drifted without a verdict flip
  rate a     : 13/14 pass (0.9286), 95% CI 0.6613..0.9982
  rate b     : 13/14 pass (0.9286), 95% CI 0.6613..0.9982`}
        </pre>
        <p className="sub" style={{ marginBottom: 0 }}>
          the interval is Clopper-Pearson, exact, computed before the bundle closed and stored in
          the manifest. see the pair side by side on the{" "}
          <a href="/compare?a=demo-stability%2Fa&b=demo-stability%2Fb">compare page</a>.
        </p>
      </Step>

      <Step n="04" title="run it yourself">
        <p className="sub">
          <code>python -m tieout demo</code> writes a fresh keyless run against the deterministic
          sample agent; <code>python -m tieout verify runs/demo</code> on the fresh bundle is the
          same stranger check against your own output.
        </p>
        <p className="sub" style={{ marginBottom: 0 }}>
          what verify does NOT check: the agent&apos;s quality. it checks the record: that the
          verdicts are bound to the raw, the chain is intact, the controls hold, and the numbers
          in the manifest re-derive. for the check semantics, read the{" "}
          <a href="/method">method note</a> and the <a href="/cli">cli</a>.
        </p>
      </Step>
    </section>
  );
}
