"use client";

import { usePathname } from "next/navigation";

const PRIMARY: { label: string; href: string }[] = [
  { label: "runs", href: "/runs" },
  { label: "compare", href: "/compare" },
  { label: "method", href: "/method" },
  { label: "families", href: "/families" },
  { label: "repro", href: "/repro" },
];

const FOOT_DOCS: { label: string; href: string }[] = [
  { label: "method note", href: "/method" },
  { label: "bundle format", href: "/format" },
  { label: "failure-mode matrix", href: "/matrix" },
  { label: "harness spec", href: "/harness" },
  { label: "owasp crosswalk", href: "/asi" },
];

const FOOT_PROJECT: { label: string; href: string }[] = [
  { label: "cli", href: "/cli" },
  { label: "changelog", href: "/changelog" },
  { label: "security", href: "/security" },
  { label: "contributing", href: "/contribute" },
  { label: "license", href: "/license" },
];

export function Shell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const active = (href: string) =>
    pathname === href || pathname.startsWith(href + "/");

  return (
    <div className="app">
      <header className="topbar">
        <a className="brand" href="/">
          tieout
        </a>
        <nav className="nav">
          {PRIMARY.map((n) => (
            <a key={n.href} className={active(n.href) ? "nav-link nav-active" : "nav-link"} href={n.href}>
              {n.label}
            </a>
          ))}
        </nav>
        <span className="tagline">the report is a claim. the bundle is a record.</span>
      </header>
      <main>{children}</main>
      <footer className="footer">
        <div className="foot-row">
          {FOOT_DOCS.map((l) => (
            <a key={l.href} className="foot-link" href={l.href}>
              {l.label}
            </a>
          ))}
        </div>
        <div className="foot-row">
          {FOOT_PROJECT.map((l) => (
            <a key={l.href} className="foot-link" href={l.href}>
              {l.label}
            </a>
          ))}
        </div>
        <div className="foot-row">
          p1 verdict event · p2 provenance · p3 negative controls · p4 named gaps · p5 re-derivation ·
          p6 judge audit
        </div>
      </footer>
    </div>
  );
}
