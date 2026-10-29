import type { Metadata } from "next";
import { ARTICLES, THEMES } from "../../lib/articles";
import { AUTHOR, LINKEDIN_URL } from "../../lib/site";

export const metadata: Metadata = {
  title: "writing",
  description:
    "twelve articles on ai red teaming, security, research engineering, evaluation and software engineering. every number in them traces to a committed record in this repository.",
};

export default function BlogIndex() {
  return (
    <section>
      <div className="run-head">
        <h1>writing</h1>
      </div>
      <p className="sub">
        twelve articles, five disciplines. every number in them is verified against a committed
        record in this repository: a bundle, a manifest field, a test, or a cited artifact. each
        article ends with its sources. written by {AUTHOR.toLowerCase()},{" "}
        <a href={LINKEDIN_URL} target="_blank" rel="noopener noreferrer">
          linkedin ↗
        </a>
      </p>

      {THEMES.map((t) => {
        const arts = ARTICLES.filter((a) => a.theme === t.id);
        if (arts.length === 0) return null;
        return (
          <div key={t.id} className="card">
            <h2>
              {t.label} <span className="pill">{t.line}</span>
            </h2>
            {arts.map((a, i) => (
              <div key={a.slug} style={{ marginTop: i === 0 ? 0 : 18 }}>
                <a className="art-title" href={`/blog/${a.slug}`}>
                  {String(i + 1).padStart(2, "0")} · {a.title}
                </a>
                <p className="sub" style={{ marginBottom: 0 }}>
                  {a.summary}
                </p>
              </div>
            ))}
          </div>
        );
      })}
    </section>
  );
}
