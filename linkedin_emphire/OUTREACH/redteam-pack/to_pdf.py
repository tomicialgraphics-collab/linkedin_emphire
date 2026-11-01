#!/usr/bin/env python3
"""Turn package.md into a styled HTML file you can print to PDF.

No dependencies, nothing to install. Standard library only.

    python to_pdf.py
    python to_pdf.py package.md

It writes package.html beside the markdown and tells you what to do next. Open the HTML in a
browser, print it, and choose Save as PDF. The print stylesheet already sets the margins, so
nothing needs adjusting in the dialog except the destination.
"""

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 10.5pt; line-height: 1.5; color: #111; max-width: 44em; margin: 0 auto;
}
h1 { font-size: 19pt; line-height: 1.25; margin: 0 0 .6em; }
h2 { font-size: 13pt; margin: 1.7em 0 .5em; padding-bottom: .2em; border-bottom: 1px solid #ccc; }
h3 { font-size: 11.5pt; margin: 1.2em 0 .35em; }
p { margin: .55em 0; }
ul { margin: .5em 0 .7em 1.1em; padding: 0; }
li { margin: .25em 0; }
code { font-family: Consolas, "Courier New", monospace; font-size: 9pt; background: #f2f2f2;
       padding: .05em .25em; }
pre { font-family: Consolas, "Courier New", monospace; font-size: 8.8pt; line-height: 1.35;
      background: #f7f7f7; border: 1px solid #ddd; padding: .7em .8em; white-space: pre-wrap;
      word-break: break-word; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: inherit; }
table { border-collapse: collapse; width: 100%; margin: .8em 0; font-size: 9.5pt; }
th, td { border: 1px solid #bbb; padding: .35em .5em; text-align: left; vertical-align: top; }
th { background: #eee; }
blockquote { margin: .7em 0; padding: .4em .9em; border-left: 3px solid #bbb; color: #333;
             font-size: 9.8pt; }
hr { border: 0; border-top: 1px solid #ccc; margin: 1.6em 0; }
strong { font-weight: 700; }
@media print { body { max-width: none; } a { color: #111; text-decoration: none; } }
"""

INLINE = [
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<strong>\1</strong>"),
]


def inline(text):
    out = html.escape(text, quote=False)
    for pattern, repl in INLINE:
        out = pattern.sub(repl, out)
    return out


def convert(md):
    lines = md.split("\n")
    out, i = [], 0
    para = []

    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush()
            i += 1
            block = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(block), quote=False))
            continue

        if not stripped:
            flush()
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush()
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            i += 1
            continue

        if re.fullmatch(r"[-*_]{3,}", stripped):
            flush()
            out.append("<hr>")
            i += 1
            continue

        if stripped.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip().strip("|").split("|"))
                i += 1
            cells = [[c.strip() for c in r] for r in rows]
            body = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
            if body:
                head = "".join("<th>%s</th>" % inline(c) for c in body[0])
                out.append("<table><thead><tr>%s</tr></thead><tbody>" % head)
                for r in body[1:]:
                    out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r))
                out.append("</tbody></table>")
            continue

        if re.match(r"^[-*+]\s+", stripped):
            flush()
            items = []
            while i < len(lines) and re.match(r"^[-*+]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*+]\s+", "", lines[i].strip()))
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                    items[-1] += " " + lines[i].strip()
                    i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(t) for t in items))
            continue

        if stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(quote)))
            continue

        para.append(stripped)
        i += 1

    flush()
    return "\n".join(out)


def main(argv):
    source = Path(argv[1]) if len(argv) > 1 else HERE / "package.md"
    if not source.is_absolute():
        source = (Path.cwd() / source).resolve()
    if not source.exists():
        print("no file at %s" % source)
        return 1

    md = source.read_text(encoding="utf-8")
    title = "Evidence package"
    first = re.search(r"^#\s+(.*)$", md, re.M)
    if first:
        title = first.group(1).strip()

    page = (
        "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<title>%s</title><style>%s</style></head><body>\n%s\n</body></html>\n"
        % (html.escape(title), CSS, convert(md))
    )
    target = source.with_suffix(".html")
    target.write_text(page, encoding="utf-8")

    print("wrote %s" % target)
    print("")
    print("Next:")
    print("  1. Open it:  Start-Process \"%s\"" % target)
    print("  2. Ctrl and P, choose Microsoft Print to PDF, or Save as PDF in Edge")
    print("  3. Save it as %s" % target.with_suffix(".pdf").name)
    print("")
    print("A PDF attaches to a LinkedIn message. A .md file does not.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
