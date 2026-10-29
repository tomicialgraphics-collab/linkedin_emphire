import { useEffect, useState } from "react";
import RunsPage from "./pages/RunsPage";
import RunPage from "./pages/RunPage";

function useHashRoute(): string {
  const [hash, setHash] = useState(window.location.hash);
  useEffect(() => {
    const onChange = () => setHash(window.location.hash);
    window.addEventListener("hashchange", onChange);
    return () => window.removeEventListener("hashchange", onChange);
  }, []);
  return hash;
}

export default function App() {
  const hash = useHashRoute();
  const match = hash.match(/^#\/run\/(.+)$/);
  return (
    <div className="app">
      <header className="topbar">
        <a className="brand" href="#/">
          <span className="brand-mark">◈</span> tieout
        </a>
        <span className="tagline">evidence-grade agent evaluation. the report is a claim, the bundle is a record.</span>
      </header>
      <main>
        {match ? <RunPage id={decodeURIComponent(match[1])} /> : <RunsPage />}
      </main>
      <footer className="footer">
        tieout · P1 verdict event · P2 provenance · P3 negative controls · P4 named gaps · P5 re-derivation · P6 judge audit
      </footer>
    </div>
  );
}
