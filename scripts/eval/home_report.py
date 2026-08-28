"""
home_report.py — Renders eval/runs/index.html, the dashboard's actual home
page. Before this existed, "/" WAS the harness-optimizer page directly
(index_report.py used to write straight to index.html) — there was no
neutral landing spot to choose between tools, and the optimizer page had
just quietly hijacked the root URL. That page now writes to optimizer.html
instead; this is the real home, a plain link hub to it and to the scraper
page (scrape_report.py), styled to match (same :root CSS variables as
every other dashboard here, copied rather than shared per this project's
self-contained-module convention).
"""

import html


def _esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def render_html(n_optimizer_runs: int = None) -> str:
    runs_note = f"{n_optimizer_runs} run(s) recorded" if n_optimizer_runs is not None else "no runs yet"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Learning Wiki eval harness</title>
<style>
  :root {{
    color-scheme: light;
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
    --border: rgba(11,11,11,0.10);
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{
      --surface-1: #1a1a19; --page: #0d0d0d;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
      --border: rgba(255,255,255,0.10);
    }}
  }}
  :root[data-theme="dark"] {{
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
    --border: rgba(255,255,255,0.10);
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  .viz-root {{ max-width: 720px; margin: 0 auto; padding: 64px 20px; color: var(--text-primary); }}
  h1 {{ font-size: 24px; margin: 0 0 8px; }}
  .meta {{ color: var(--text-secondary); font-size: 14px; margin-bottom: 36px; }}
  .cards {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
  @media (max-width: 560px) {{ .cards {{ grid-template-columns: 1fr; }} }}
  .card {{ display: block; background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px;
           padding: 24px; text-decoration: none; color: inherit; transition: border-color 0.15s; }}
  .card:hover {{ border-color: var(--text-secondary); }}
  .card h2 {{ font-size: 17px; margin: 0 0 6px; color: var(--text-primary); }}
  .card p {{ font-size: 13px; color: var(--text-secondary); margin: 0; line-height: 1.5; }}
  .card .tag {{ display: inline-block; font-size: 11px; color: var(--text-muted); margin-top: 14px;
                text-transform: uppercase; letter-spacing: 0.04em; }}
</style>
</head>
<body>
<div class="viz-root">
  <h1>Learning Wiki eval harness</h1>
  <div class="meta">{_esc(runs_note)}</div>
  <div class="cards">
    <a class="card" href="/optimizer.html">
      <h2>Harness Optimizer</h2>
      <p>Model comparisons, prompt-version history, and auto-optimize rounds against the 10-article
      benchmark — judge scores, validator pass rates, cost and latency trends.</p>
      <span class="tag">All runs &rarr;</span>
    </a>
    <a class="card" href="/scrape.html">
      <h2>Scraper / Wiki Builder</h2>
      <p>Discover and fetch real articles (PMC/ERIC/arXiv) for a real ingest batch, then generate and
      ingest them into wiki pages.</p>
      <span class="tag">Scraper progress &rarr;</span>
    </a>
  </div>
</div>
</body>
</html>"""
