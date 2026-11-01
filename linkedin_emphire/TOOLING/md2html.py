#!/usr/bin/env python3
"""Turn one of our markdown briefs into a self-contained, printable HTML page.

No external fonts, no CDN, no JavaScript. SAY blocks and NOTE blocks are rendered as
distinct cards because the documents are meant to be read aloud, with the spoken parts
legible at arm's length and the notes quieter beside them.

    python3 TOOLING/md2html.py SRC.md DEST.html --title "The Aithos script"

Handles the subset of markdown these documents actually use: h1 to h3, bold, italic,
inline code, bullet and numbered lists, blockquotes, pipe tables, rules, and the
**SAY** / **NOTE** markers as block starts.
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys

CSS = """
:root{
  --ink:#14181f; --muted:#5b6472; --line:#dfe3ea; --paper:#ffffff;
  --say:#0f3d33; --say-bg:#f2f8f5; --say-line:#2f7a63;
  --note:#4a5262; --note-bg:#f6f7f9;
  --accent:#1a4f8b;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:#eef0f4; color:var(--ink);
  font-family:Charter, "Bitstream Charter", "Iowan Old Style", Georgia, "Times New Roman", serif;
  font-size:18px; line-height:1.62;
}
main{
  max-width:44rem; margin:0 auto; background:var(--paper);
  padding:3.2rem 2.4rem 4rem; box-shadow:0 1px 2px rgba(16,24,40,.06), 0 12px 40px rgba(16,24,40,.07);
}
h1{
  font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
  font-size:1.9rem; line-height:1.2; letter-spacing:-.02em; margin:0 0 .4rem;
}
h2{
  font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
  font-size:1.16rem; letter-spacing:-.01em; margin:2.6rem 0 .9rem;
  padding-top:1.1rem; border-top:1px solid var(--line);
}
h2:first-of-type{border-top:0; padding-top:0}
h3{
  font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
  font-size:1rem; margin:1.8rem 0 .5rem; color:var(--accent);
}
p{margin:0 0 1rem}
strong{font-weight:650}
em{font-style:italic}
hr{border:0; border-top:1px solid var(--line); margin:2rem 0}
ul,ol{margin:0 0 1rem; padding-left:1.3rem}
li{margin:.3rem 0}
code{
  font-family:ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size:.86em; background:#eef1f5; padding:.1em .35em; border-radius:3px;
}
blockquote{
  margin:1.1rem 0; padding:.9rem 1.1rem; background:#f7f9fc;
  border-left:3px solid #b9c6d8; color:#24303f;
}
blockquote p:last-child{margin-bottom:0}
.say{
  margin:1.1rem 0 1.4rem; padding:1.1rem 1.2rem; background:var(--say-bg);
  border-left:4px solid var(--say-line); border-radius:0 6px 6px 0;
  font-size:1.06rem; line-height:1.66;
}
.say p{margin:0 0 .85rem}
.say p:last-child{margin:0}
.note{
  margin:1rem 0 1.6rem; padding:.85rem 1.1rem; background:var(--note-bg);
  border-left:3px solid #c6ccd6; border-radius:0 6px 6px 0;
  font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
  font-size:.88rem; line-height:1.55; color:var(--note);
}
.note p{margin:0 0 .6rem}
.note p:last-child{margin:0}
.note .tag{display:block; font-weight:700; letter-spacing:.08em; font-size:.7rem; text-transform:uppercase; color:#8a93a1; margin-bottom:.35rem}
.say .tag{display:block; font-weight:700; letter-spacing:.14em; font-size:.66rem; text-transform:uppercase; color:#4f8b76; margin-bottom:.45rem; font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif}
table{border-collapse:collapse; width:100%; margin:1rem 0 1.4rem; font-size:.92rem;
  font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif}
th,td{text-align:left; padding:.5rem .6rem; border-bottom:1px solid var(--line); vertical-align:top}
th{font-size:.78rem; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); border-bottom:1px solid #c8ced9}
footer{margin-top:3rem; padding-top:1rem; border-top:1px solid var(--line);
  font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, sans-serif;
  font-size:.78rem; color:var(--muted)}
a{color:var(--accent)}
@media (max-width:600px){
  body{font-size:17px}
  main{padding:1.6rem 1.1rem 3rem; box-shadow:none}
  h1{font-size:1.55rem}
}
@media print{
  body{background:#fff; font-size:11.2pt}
  main{max-width:none; box-shadow:none; padding:0}
  h2{break-after:avoid; page-break-after:avoid}
  .say,.note,blockquote,table,li{break-inside:avoid; page-break-inside:avoid}
  .say{background:#f3f7f5}
  footer{border-top:1px solid #ccc}
}
"""

TITLE_FALLBACK = "Document"


def inline(text: str) -> str:
    out = html.escape(text)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|") and s.count("|") >= 2


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(md: str) -> tuple[str, list[str]]:
    lines = md.splitlines()
    body: list[str] = []
    title = None
    block = None          # None | "say" | "note"
    buf: list[str] = []   # paragraphs inside a say/note block
    i = 0

    paras: list[str] = []   # finished paragraphs inside the current say/note block

    def flush_block() -> None:
        nonlocal block, buf, paras
        if block:
            if buf:
                paras.append(" ".join(buf))
            if paras:
                cls = block
                tag = "SAY, read this out loud" if cls == "say" else "Notes, not spoken"
                body.append('<div class="%s"><span class="tag">%s</span>%s</div>'
                            % (cls, tag, "".join("<p>%s</p>" % inline(p) for p in paras)))
        block, buf, paras = None, [], []

    def flush_para() -> None:
        nonlocal buf
        if buf:
            body.append("<p>%s</p>" % inline(" ".join(buf)))
            buf = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            if block:
                if buf:
                    paras.append(" ".join(buf))
                    buf = []
            else:
                flush_para()
            i += 1
            continue

        if stripped in ("**SAY**", "**NOTE**"):
            if block:
                flush_block()
            else:
                flush_para()
            block = "say" if stripped == "**SAY**" else "note"
            i += 1
            continue

        if stripped.startswith("# "):
            flush_block() if block else flush_para()
            if title is None:
                title = stripped[2:].strip()
            else:
                body.append("<h1>%s</h1>" % inline(stripped[2:].strip()))
            i += 1
            continue

        if stripped.startswith("## "):
            flush_block() if block else flush_para()
            body.append("<h2>%s</h2>" % inline(stripped[3:].strip()))
            i += 1
            continue

        if stripped.startswith("### "):
            flush_block() if block else flush_para()
            body.append("<h3>%s</h3>" % inline(stripped[4:].strip()))
            i += 1
            continue

        if set(stripped) <= {"-", "*", "_"} and len(stripped) >= 3:
            flush_block() if block else flush_para()
            body.append("<hr>")
            i += 1
            continue

        if is_table_row(stripped):
            flush_block() if block else flush_para()
            rows = []
            while i < len(lines) and is_table_row(lines[i].strip()):
                rows.append(cells(lines[i]))
                i += 1
            rows = [r for r in rows if not all(set(c) <= set("-: ") for c in r)]
            if rows:
                head = "".join("<th>%s</th>" % inline(c) for c in rows[0])
                rest = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r)
                               for r in rows[1:])
                body.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>"
                            % (head, rest))
            continue

        if stripped.startswith("> "):
            flush_block() if block else flush_para()
            quoted = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quoted.append(lines[i].strip().lstrip(">").strip())
                i += 1
            inner = "".join("<p>%s</p>" % inline(q) for q in quoted if q)
            body.append("<blockquote>%s</blockquote>" % inner)
            continue

        if stripped.startswith(("- ", "* ")):
            flush_block() if block else flush_para()
            items = []
            while i < len(lines) and lines[i].strip().startswith(("- ", "* ")):
                items.append(lines[i].strip()[2:].strip())
                i += 1
            body.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        if re.match(r"^\d+\.\s", stripped):
            flush_block() if block else flush_para()
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s", "", lines[i].strip()))
                i += 1
            body.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        if block:
            buf.append(stripped)
        else:
            buf.append(stripped)
        i += 1

    if block:
        flush_block()
    else:
        flush_para()
    return (title or TITLE_FALLBACK), body


def build(src: str, dest: str, title_override: str | None, subtitle: str | None) -> None:
    with open(src, encoding="utf-8") as fh:
        md = fh.read()
    title, body = convert(md)
    if title_override:
        title = title_override
    stamp = subtitle or ""
    doc = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>%s</title>
<style>%s</style>
</head>
<body>
<main>
<h1>%s</h1>
%s
<footer>%s</footer>
</main>
</body>
</html>
""" % (html.escape(title), CSS, html.escape(title), "\n".join(body), html.escape(stamp))
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("%s -> %s (%d KB)" % (os.path.basename(src), os.path.basename(dest),
                                len(doc.encode("utf-8")) // 1024))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Markdown brief to self-contained HTML.")
    parser.add_argument("src")
    parser.add_argument("dest", nargs="?")
    parser.add_argument("--title", default=None)
    parser.add_argument("--subtitle", default=None)
    args = parser.parse_args(argv)
    dest = args.dest or os.path.splitext(args.src)[0] + ".html"
    build(args.src, dest, args.title, args.subtitle)
    return 0


if __name__ == "__main__":
    sys.exit(main())
