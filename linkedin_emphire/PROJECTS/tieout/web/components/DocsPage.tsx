"use client";

import { useEffect, useState } from "react";
import { getDocs } from "../lib/api";
import type { DocKey } from "../lib/types";
import { Markdown } from "./Markdown";

const TITLES: Record<DocKey, { title: string; sub: string; cross: { label: string; href: string }[] }> = {
  method: {
    title: "Method note",
    sub: "the gap, the pillars as doctrine, how to read a bundle, reproducibility stated precisely",
    cross: [
      { label: "bundle format v1", href: "/format" },
      { label: "failure-mode matrix", href: "/matrix" },
      { label: "harness spec", href: "/harness" },
    ],
  },
  format: {
    title: "Bundle format, v1",
    sub: "the record schema, the chain, the gap codes, the verify procedure",
    cross: [
      { label: "method note", href: "/method" },
      { label: "harness spec", href: "/harness" },
    ],
  },
  matrix: {
    title: "Failure-mode matrix",
    sub: "four failure modes of decision-time evidence, five columns, two test classes",
    cross: [
      { label: "harness spec", href: "/harness" },
      { label: "method note", href: "/method" },
    ],
  },
  harness: {
    title: "Harness spec",
    sub: "the T0-T6 phases as implemented, tests A-D, the binding field map, the standing named gaps",
    cross: [
      { label: "failure-mode matrix", href: "/matrix" },
      { label: "bundle format v1", href: "/format" },
    ],
  },
  changelog: {
    title: "Changelog",
    sub: "all notable changes, newest first",
    cross: [
      { label: "method note", href: "/method" },
      { label: "cli", href: "/cli" },
    ],
  },
  security: {
    title: "Security",
    sub: "scope, verify-don't-trust, disclosure",
    cross: [
      { label: "method note", href: "/method" },
      { label: "reproduce", href: "/repro" },
    ],
  },
  contributing: {
    title: "Contributing",
    sub: "how to add a family, a run, or a check, with the rules the code enforces",
    cross: [
      { label: "cli", href: "/cli" },
      { label: "changelog", href: "/changelog" },
    ],
  },
  license: {
    title: "License",
    sub: "MIT",
    cross: [
      { label: "contributing", href: "/contribute" },
      { label: "changelog", href: "/changelog" },
    ],
  },
};

export function DocsPage({ docKey }: { docKey: DocKey }) {
  const [source, setSource] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setSource(null);
    setError(null);
    getDocs()
      .then((d) => setSource(d[docKey] ?? ""))
      .catch((e) => setError(String(e)));
  }, [docKey]);

  const meta = TITLES[docKey];

  return (
    <section>
      <p>
        <a className="back" href="/">
          ← home
        </a>
      </p>
      <div className="run-head">
        <h1>{meta.title}</h1>
      </div>
      <p className="sub">{meta.sub}</p>
      <div className="cross-links">
        {meta.cross.map((c) => (
          <a key={c.href} className="btn" href={c.href}>
            {c.label}
          </a>
        ))}
      </div>
      <div className="card">
        {error && <p className="bad-text">{error}</p>}
        {!source && !error && <p className="sub">loading document…</p>}
        {source && <Markdown source={source} />}
      </div>
    </section>
  );
}
