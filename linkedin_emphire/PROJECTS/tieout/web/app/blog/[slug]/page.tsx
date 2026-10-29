import type { Metadata } from "next";
import { ARTICLES } from "../../../lib/articles";
import { Markdown } from "../../../components/Markdown";
import { AUTHOR, LINKEDIN_URL } from "../../../lib/site";

export function generateStaticParams() {
  return ARTICLES.map((a) => ({ slug: a.slug }));
}

export const dynamicParams = false;

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const a = ARTICLES.find((x) => x.slug === params.slug);
  return { title: a ? a.title : "writing", description: a?.summary };
}

export default function ArticlePage({ params }: { params: { slug: string } }) {
  const a = ARTICLES.find((x) => x.slug === params.slug);
  if (!a) return null;

  const idx = ARTICLES.findIndex((x) => x.slug === a.slug);
  const prev = idx > 0 ? ARTICLES[idx - 1] : null;
  const next = idx < ARTICLES.length - 1 ? ARTICLES[idx + 1] : null;

  return (
    <section>
      <p>
        <a className="back" href="/blog">
          ← writing
        </a>
      </p>
      <div className="run-head">
        <h1>{a.title}</h1>
      </div>
      <p className="sub">{a.summary}</p>
      <p className="sub mono" style={{ marginBottom: 0 }}>
        {AUTHOR.toLowerCase()} ·{" "}
        <a href={LINKEDIN_URL} target="_blank" rel="noopener noreferrer">
          linkedin ↗
        </a>
      </p>

      <div className="card">
        <Markdown source={a.body} />
        <div className="raw-label">verified against</div>
        <ul className="verify-list">
          {a.verified.map((v) => (
            <li key={v} className="small">
              {v}
            </li>
          ))}
        </ul>
      </div>

      <div className="cross-links" style={{ marginTop: 18 }}>
        {prev && (
          <a className="btn" href={`/blog/${prev.slug}`}>
            ← {prev.title.length > 42 ? prev.title.slice(0, 42) + "…" : prev.title}
          </a>
        )}
        {next && (
          <a className="btn" href={`/blog/${next.slug}`}>
            {next.title.length > 42 ? next.title.slice(0, 42) + "…" : next.title} →
          </a>
        )}
      </div>
    </section>
  );
}
