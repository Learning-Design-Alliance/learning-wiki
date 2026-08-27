"""
scrape_report.py — Self-contained HTML dashboard for the discovery+fetch
("scraper") pipeline, separate from the model-generation dashboards
(index_report.py / html_report.py / auto_optimize_report.py) — this tracks
scripts/run_scrape_batch.py's progress (discover_articles.py, then
fetch_article.py's prefetch-verify) rather than a model run.

Palette/theme follow the same conventions as the other dashboards (this
project's dataviz skill) — same :root-scoped CSS variables as
auto_optimize_report.py, copied rather than shared, since each report
module here is deliberately self-contained (see that file's own docstring)
so the dashboard server can keep serving plain static files with no shared
template engine.
"""

import html

STATUS_LABELS = {
    "discovering": ("Discovering", "var(--status-warn)"),
    "fetching": ("Fetching", "var(--status-warn)"),
    "completed": ("Completed", "var(--status-good)"),
    "error": ("Error", "var(--status-critical)"),
    "stopped_by_user": ("Stopped", "var(--status-critical)"),
}


def _esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _source_rows(discover: dict) -> str:
    by_source = (discover or {}).get("by_source") or {}
    if not by_source:
        return '<tr><td colspan="3" class="empty-note">No discovery data yet.</td></tr>'
    rows = []
    for source, counts in by_source.items():
        found, target = counts.get("found", 0), counts.get("target", 0)
        pct = min(100, round(100 * found / target)) if target else 0
        rows.append(
            f'<tr><td>{_esc(source)}</td><td class="num">{found}/{target}</td>'
            f'<td><div class="bar-track"><div class="bar-fill" style="width:{pct}%;"></div></div></td></tr>'
        )
    return "".join(rows)


def _fetch_rows(fetch: dict) -> str:
    results = (fetch or {}).get("results") or []
    if not results:
        return '<tr><td colspan="3" class="empty-note">No fetch attempts yet.</td></tr>'
    rows = []
    # Newest first, capped — this is a live tail, not a full audit log (the
    # raw console log linked below has everything).
    for r in reversed(results[-200:]):
        ok = r.get("ok")
        status_html = '<span class="ok-badge">OK</span>' if ok else '<span class="fail-badge">FAIL</span>'
        detail = _esc(r.get("chars_or_detail", ""))
        rows.append(f'<tr><td>{status_html}</td><td>{_esc(r.get("id"))}</td><td class="detail-cell">{detail}</td></tr>')
    return "".join(rows)


def _live_console_html() -> str:
    """Same pattern as index_report.py's _live_console_html() for
    auto-optimize: client-side polling of a fixed-path plain-text log
    (.scrape_console.log, written by run_scrape_batch.py's own ConsoleTee
    regardless of how it was launched) independent of this page's own
    10s full-reload cadence, so console output between state-file updates
    is still visible without SSHing in to tail a log file by hand."""
    return """
    <div class="card console-card">
      <h2 style="margin-top:0;">Live console</h2>
      <pre id="console-log-pre" class="log-box">Loading&hellip;</pre>
    </div>
    <script>
      (function () {
        var pre = document.getElementById('console-log-pre');
        var atBottom = true;
        pre.addEventListener('scroll', function () {
          atBottom = pre.scrollTop + pre.clientHeight >= pre.scrollHeight - 4;
        });
        function poll() {
          fetch('./.scrape_console.log', { cache: 'no-store' })
            .then(function (r) { if (!r.ok) throw new Error('no log yet'); return r.text(); })
            .then(function (text) {
              var lines = text.split('\\n');
              pre.textContent = lines.slice(-400).join('\\n');
              if (atBottom) { pre.scrollTop = pre.scrollHeight; }
            })
            .catch(function () { pre.textContent = '(no console output yet)'; });
        }
        poll();
        setInterval(poll, 4000);
      })();
    </script>"""


def render_html(state: dict) -> str:
    status = state.get("status", "unknown")
    label, color = STATUS_LABELS.get(status, (status, "var(--text-secondary)"))
    config = state.get("config") or {}
    discover = state.get("discover") or {}
    fetch = state.get("fetch") or {}
    is_active = status in ("discovering", "fetching")

    fetch_total, fetch_ok, fetch_fail = fetch.get("total", 0), fetch.get("ok", 0), fetch.get("fail", 0)
    fetch_done_count = fetch_ok + fetch_fail

    stop_button = (
        '<form method="POST" action="/stop-scrape" class="inline-form">'
        '<button type="submit" class="btn btn-danger">Stop</button></form>'
        if is_active else ""
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="10">
<title>Scraper progress — {_esc(state.get('label', 'scrape batch'))}</title>
<style>
  :root {{
    color-scheme: light;
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
    --gridline: #e1e0d9; --axis: #c3c2b7;
    --status-good: #0ca30c; --status-critical: #d03b3b; --status-warn: #b8860b;
    --border: rgba(11,11,11,0.10);
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{
      --surface-1: #1a1a19; --page: #0d0d0d;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
      --gridline: #2c2c2a; --axis: #383835;
      --status-good: #0ca30c; --status-critical: #e66767; --status-warn: #d4a72c;
      --border: rgba(255,255,255,0.10);
    }}
  }}
  :root[data-theme="dark"] {{
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
    --gridline: #2c2c2a; --axis: #383835;
    --status-good: #0ca30c; --status-critical: #e66767; --status-warn: #d4a72c;
    --border: rgba(255,255,255,0.10);
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  .viz-root {{ max-width: 900px; margin: 0 auto; padding: 32px 20px 64px; color: var(--text-primary); }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  h2 {{ font-size: 15px; margin: 28px 0 14px; }}
  .meta {{ color: var(--text-secondary); font-size: 13px; margin-bottom: 20px; }}
  .meta a {{ color: var(--text-primary); }}
  .card {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 20px; }}
  .status-row {{ display: flex; align-items: center; gap: 10px; margin-bottom: 4px; }}
  .status-pill {{ display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: 12px; font-weight: 600;
                  color: white; background: {color}; }}
  .config-line {{ color: var(--text-secondary); font-size: 13px; }}
  .idx-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  .idx-table th {{ text-align: left; padding: 8px 10px; color: var(--text-muted); font-weight: 600; font-size: 11px;
                    text-transform: uppercase; letter-spacing: 0.03em; border-bottom: 1px solid var(--border); }}
  .idx-table td {{ padding: 7px 10px; border-bottom: 1px solid var(--gridline); vertical-align: top; }}
  .idx-table td.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
  .detail-cell {{ color: var(--text-secondary); font-size: 12px; max-width: 480px; overflow-wrap: anywhere; }}
  .bar-track {{ position: relative; height: 10px; background: var(--gridline); border-radius: 4px; min-width: 120px; }}
  .bar-fill {{ position: absolute; top: 0; bottom: 0; left: 0; border-radius: 4px; background: var(--status-good); min-width: 2px; }}
  .ok-badge {{ color: var(--status-good); font-weight: 600; }}
  .fail-badge {{ color: var(--status-critical); font-weight: 600; }}
  .empty-note {{ color: var(--text-muted); font-size: 13px; text-align: center; padding: 12px; }}
  .btn {{ font: inherit; padding: 7px 16px; border-radius: 7px; border: 1px solid var(--border); background: var(--surface-1);
          color: var(--text-primary); cursor: pointer; }}
  .btn-primary {{ background: var(--text-primary); color: var(--page); border-color: var(--text-primary); }}
  .btn-danger {{ border-color: var(--status-critical); color: var(--status-critical); }}
  .inline-form {{ display: inline; }}
  .launch-form {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; align-items: end; margin-top: 10px; }}
  .launch-form label {{ display: flex; flex-direction: column; gap: 4px; font-size: 12px; color: var(--text-secondary); }}
  .launch-form input {{ font: inherit; padding: 6px 8px; border-radius: 6px; border: 1px solid var(--border);
                         background: var(--page); color: var(--text-primary); }}
  .log-box {{ background: #0d0d0d; color: #d7d7d2; font-family: ui-monospace, monospace; font-size: 12px;
              padding: 14px; border-radius: 8px; max-height: 320px; overflow-y: auto; white-space: pre-wrap;
              overflow-wrap: anywhere; }}
  .footer-note {{ margin-top: 12px; color: var(--text-muted); font-size: 12px; }}
</style>
</head>
<body>
<div class="viz-root">
  <h1>Scraper progress</h1>
  <div class="meta">Discovery (PMC/ERIC/arXiv) + prefetch-verify for a real ingest batch — auto-refreshes
  every 10s while active. <a href="/">&larr; Back to eval runs</a></div>

  <div class="card">
    <div class="status-row">
      <span class="status-pill">{_esc(label)}</span>
      <strong>{_esc(state.get('label', '(no batch run yet)'))}</strong>
      {stop_button}
    </div>
    <div class="config-line">
      pmc={config.get('pmc', '–')} &middot; eric={config.get('eric', '–')} &middot; arxiv={config.get('arxiv', '–')}
      &middot; out=<code>{_esc(config.get('out', '–'))}</code>
      {f" &middot; error: {_esc(state.get('error_detail'))}" if state.get('error_detail') else ""}
    </div>
  </div>

  <h2>Discovery — candidates found per source</h2>
  <div class="card">
    <table class="idx-table">
      <thead><tr><th>Source</th><th>Found / target</th><th>Progress</th></tr></thead>
      <tbody>{_source_rows(discover)}</tbody>
    </table>
  </div>

  <h2>Prefetch-verify — {fetch_done_count}/{fetch_total} attempted ({fetch_ok} OK, {fetch_fail} failed)</h2>
  <div class="card">
    <table class="idx-table">
      <thead><tr><th>Status</th><th>Article</th><th>Detail</th></tr></thead>
      <tbody>{_fetch_rows(fetch)}</tbody>
    </table>
  </div>

  <h2>Start a new batch</h2>
  <div class="card">
    <form method="POST" action="/launch-scrape" class="launch-form" onsubmit="return !{str(is_active).lower()};">
      <label>PMC target<input type="number" name="pmc" value="200" min="0" max="5000"></label>
      <label>ERIC target<input type="number" name="eric" value="700" min="0" max="5000"></label>
      <label>arXiv target<input type="number" name="arxiv" value="0" min="0" max="500"></label>
      <label>Output manifest<input type="text" name="out" value="eval/corpus/manifest_real.json"></label>
      <button type="submit" class="btn btn-primary" {"disabled" if is_active else ""}>Launch batch</button>
    </form>
    {f'<p class="footer-note">A batch is already running — stop it before launching another.</p>' if is_active else ''}
  </div>

  {_live_console_html()}
</div>
</body>
</html>"""
