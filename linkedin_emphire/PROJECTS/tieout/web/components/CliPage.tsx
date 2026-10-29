const COMMANDS: { cmd: string; summary: string; flags: [string, string][]; example: string }[] = [
  {
    cmd: "tieout demo",
    summary: "run F1 against the deterministic sample agent (keyless)",
    flags: [
      ["--out", "output directory (default runs/demo)"],
      ["--suite", "suite id (default F1)"],
      ["--seed", "surface-drift seed (default 0)"],
    ],
    example: "tieout demo && tieout verify runs/demo",
  },
  {
    cmd: "tieout run",
    summary: "run a suite against an agent",
    flags: [
      ["--agent", "sample | live (default sample)"],
      ["--suite", "suite id (default F1)"],
      ["--out", "output directory (default: generated from run id)"],
      ["--model", "model name (live agent)"],
      ["--base-url", "OpenAI-compatible endpoint (live agent)"],
      ["--key", "api key (live agent; never written to the bundle)"],
      ["--system-prompt-file", "system prompt file (live agent)"],
      ["--temperature", "decoding temperature (default 0.2)"],
      ["--seed", "surface-drift seed for the sample agent (0 = documented behavior)"],
    ],
    example: "tieout run --agent live --model gpt-4o --key $KEY --suite F1",
  },
  {
    cmd: "tieout verify",
    summary: "P5 re-derivation of a bundle (stranger-safe: no model, no key, no network)",
    flags: [["run_dir", "the run directory, e.g. runs/demo"]],
    example: "tieout verify runs/demo-f2",
  },
  {
    cmd: "tieout gaps",
    summary: "the named gaps of a bundle, if any",
    flags: [["run_dir", "the run directory"]],
    example: "tieout gaps runs/demo",
  },
  {
    cmd: "tieout judge-audit",
    summary: "the judge's own numbers from a bundle (P6)",
    flags: [["run_dir", "the run directory"]],
    example: "tieout judge-audit runs/demo-f2",
  },
  {
    cmd: "tieout diff",
    summary: "cross-run stability diff (align by pre-assigned id)",
    flags: [
      ["run_a", "first run directory"],
      ["run_b", "second run directory"],
      ["--json", "machine-readable output"],
    ],
    example: "tieout diff runs/demo-stability/a runs/demo-stability/b",
  },
  {
    cmd: "tieout selftest",
    summary: "the 8-point harness selftest",
    flags: [],
    example: "tieout selftest",
  },
  {
    cmd: "tieout serve",
    summary: "bundle browser + verify over HTTP (this site's backend)",
    flags: [
      ["--port", "default 8000"],
      ["--host", "default 0.0.0.0"],
      ["--runs-dir", "default runs"],
    ],
    example: "tieout serve --runs-dir runs",
  },
];

export function CliPage() {
  return (
    <section>
      <p>
        <a className="back" href="/">
          ← home
        </a>
      </p>
      <div className="run-head">
        <h1>
          CLI <span className="pill">as the parser defines it</span>
        </h1>
      </div>
      <p className="sub">
        install with <code>pip install -e .</code> (add <code>.[dev]</code> for tests,{" "}
        <code>.[live]</code> for OpenAI-compatible live agents). every command below is exactly
        what the argparse tree accepts.
      </p>

      {COMMANDS.map((c) => (
        <div key={c.cmd} className="card">
          <h2 className="mono" style={{ fontSize: 16 }}>
            {c.cmd}
          </h2>
          <p className="sub">{c.summary}</p>
          {c.flags.length > 0 && (
            <table>
              <thead>
                <tr>
                  <th>flag</th>
                  <th>meaning</th>
                </tr>
              </thead>
              <tbody>
                {c.flags.map(([f, m]) => (
                  <tr key={f}>
                    <td className="mono small" style={{ whiteSpace: "nowrap" }}>
                      {f}
                    </td>
                    <td className="small">{m}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
          <pre className="code">{c.example}</pre>
        </div>
      ))}

      <div className="card">
        <h2>
          exit codes <span className="pill">scriptable</span>
        </h2>
        <p className="sub" style={{ marginBottom: 0 }}>
          <code>verify</code>: 0 on PASS, 1 on FAIL, 2 if there is no bundle at the path.{" "}
          <code>diff</code>: 0 once the diff is computed (the stability number is data, not a
          status), 2 on error such as a missing run. <code>selftest</code>: 0 when all 8 points
          pass, 1 otherwise. the CI workflow runs the same commands against the committed runs,
          so the site and the pipeline share one definition of pass.
        </p>
      </div>
    </section>
  );
}
