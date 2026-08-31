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

from . import model_catalog

STATUS_LABELS = {
    "discovering": ("Discovering", "var(--status-warn)"),
    "fetching": ("Fetching", "var(--status-warn)"),
    "generating": ("Generating", "var(--status-warn)"),
    "ingesting": ("Ingesting", "var(--status-warn)"),
    "completed": ("Completed", "var(--status-good)"),
    "error": ("Error", "var(--status-critical)"),
    "stopped_by_user": ("Stopped", "var(--status-critical)"),
}
ACTIVE_STATUSES = ("discovering", "fetching", "generating", "ingesting")


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


def _model_options_html(selected: str = None) -> str:
    options = ['<option value="">(discover + fetch only, no generation)</option>']
    for slug, desc in model_catalog.MODEL_DESCRIPTIONS.items():
        sel = " selected" if slug == selected else ""
        options.append(f'<option value="{_esc(slug)}"{sel}>{_esc(slug)} — {_esc(desc)}</option>')
    return "".join(options)


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


def _history_rows(history: list) -> str:
    if not history:
        return '<tr><td colspan="6" class="empty-note">No previous runs yet.</td></tr>'
    rows = []
    for h in reversed(history):  # newest first — archived in chronological (oldest-first) order
        status = h.get("status", "unknown")
        label, color = STATUS_LABELS.get(status, (status, "var(--text-secondary)"))
        config = h.get("config") or {}
        fetch = h.get("fetch") or {}
        cfg_bits = [f"pmc={config.get('pmc', 0)}", f"eric={config.get('eric', 0)}", f"arxiv={config.get('arxiv', 0)}"]
        if config.get("model"):
            cfg_bits.append(_esc(config["model"]))
        rows.append(
            f'<tr><td>{_esc(h.get("label", "–"))}</td>'
            f'<td><span class="status-pill" style="background:{color};">{_esc(label)}</span></td>'
            f'<td>{" &middot; ".join(cfg_bits)}</td>'
            f'<td class="num">{fetch.get("ok", 0)}/{fetch.get("total", 0)}</td>'
            f'<td>{_esc((h.get("started_at") or "–")[:19].replace("T", " "))}</td>'
            f'<td>{_esc((h.get("finished_at") or "–")[:19].replace("T", " ") if h.get("finished_at") else "–")}</td></tr>'
        )
    return "".join(rows)


def _live_console_html() -> str:
    """Same pattern as index_report.py's _live_console_html() for
    auto-optimize: client-side polling of a plain-text log, independent of
    this page's own 5s state-poll cadence, so console output is visible
    without SSHing in to tail a log file by hand.

    Which log: run_scrape_batch.py's own singleton (.scrape_console.log)
    covers the discover/fetch phases it runs in-process — but generation
    (chained by run_scrape_batch.py, OR run by hand later to resume a
    crashed/interrupted batch, e.g. `eval_harness.py run --run-id <the
    batch's label>`) is a separate process that eval_harness.py's cmd_run
    tees into eval/runs/<run_id>/.console.log instead (see its own
    docstring). Rather than requiring an explicit signal for which one is
    live right now, this just tries the per-run-id log first (keyed off
    .scrape_state.json's own label, so it doesn't matter whether that
    generation step is the orchestrated chain or a manual resume — same
    run-id either way) and falls back to the singleton if that 404s."""
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
        function fetchLog(url) {
          return fetch(url, { cache: 'no-store' }).then(function (r) { return r.ok ? r : null; });
        }
        function poll() {
          fetch('./.scrape_state.json', { cache: 'no-store' })
            .then(function (r) { return r.ok ? r.json() : {}; })
            .catch(function () { return {}; })
            .then(function (state) {
              var label = (state && state.label) || '';
              var perRun = label ? './' + encodeURIComponent(label) + '/.console.log' : null;
              if (!perRun) { return fetchLog('./.scrape_console.log'); }
              return fetchLog(perRun).then(function (r) { return r || fetchLog('./.scrape_console.log'); });
            })
            .then(function (r) { if (!r) throw new Error('no log yet'); return r.text(); })
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


def render_html(state: dict, history: list = None) -> str:
    status = state.get("status", "unknown")
    label, color = STATUS_LABELS.get(status, (status, "var(--text-secondary)"))
    config = state.get("config") or {}
    discover = state.get("discover") or {}
    fetch = state.get("fetch") or {}
    is_active = status in ACTIVE_STATUSES

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
  .launch-form {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px;
                   align-items: end; margin-top: 10px; }}
  .launch-form label {{ display: flex; flex-direction: column; gap: 4px; font-size: 12px; color: var(--text-secondary); }}
  .launch-form label.checkbox-label {{ flex-direction: row; align-items: center; gap: 6px; }}
  .launch-form label.checkbox-label input {{ width: auto; }}
  .launch-form input, .launch-form select {{ font: inherit; padding: 6px 8px; border-radius: 6px; border: 1px solid var(--border);
                         background: var(--page); color: var(--text-primary); }}
  .log-box {{ background: #0d0d0d; color: #d7d7d2; font-family: ui-monospace, monospace; font-size: 12px;
              padding: 14px; border-radius: 8px; max-height: 320px; overflow-y: auto; white-space: pre-wrap;
              overflow-wrap: anywhere; }}
  .footer-note {{ margin-top: 12px; color: var(--text-muted); font-size: 12px; }}
  .table-scroll {{ max-height: 520px; overflow-y: auto; border: 1px solid var(--border); border-radius: 10px; }}
  .table-scroll .idx-table {{ border: none; border-radius: 0; }}
  .table-scroll thead th {{ position: sticky; top: 0; background: var(--surface-1); z-index: 1; }}
</style>
</head>
<body>
<div class="viz-root">
  <div class="meta"><a href="/">&larr; Home</a> &middot; <a href="/optimizer.html">Harness optimizer →</a></div>
  <h1>Scraper progress</h1>
  <div class="meta">Discovery (PMC/ERIC/arXiv) + prefetch-verify for a real ingest batch — updates live
  every 5s while active, no page reload.</div>

  <div class="card">
    <div class="status-row">
      <span class="status-pill" id="status-pill" style="background:{color};">{_esc(label)}</span>
      <strong id="batch-label">{_esc(state.get('label', '(no batch run yet)'))}</strong>
      <span id="stop-button-container">{stop_button}</span>
    </div>
    <div class="config-line" id="config-line">
      pmc={config.get('pmc', '–')} &middot; eric={config.get('eric', '–')} &middot; arxiv={config.get('arxiv', '–')}
      &middot; out=<code>{_esc(config.get('out', '–'))}</code>
      {f" &middot; arxiv_snapshot=<code>{_esc(config.get('arxiv_snapshot'))}</code>" if config.get('arxiv_snapshot') else ""}
      {f" &middot; model=<code>{_esc(config.get('model'))}</code>" if config.get('model') else ""}
      {f" &middot; prompt={_esc(config.get('prompt_version'))}" if config.get('prompt_version') else ""}
      {f" &middot; correction_attempts={_esc(config.get('max_correction_attempts'))}" if config.get('model') else ""}
      {f" &middot; error: {_esc(state.get('error_detail'))}" if state.get('error_detail') else ""}
    </div>
  </div>

  <h2>Start a new batch</h2>
  <div class="card" id="launch-card">
    <form method="POST" action="/launch-scrape" class="launch-form" id="launch-form"
          onsubmit="return !{str(is_active).lower()};">
      <label>PMC target<input type="number" name="pmc" value="200" min="0" max="5000"></label>
      <label>ERIC target<input type="number" name="eric" value="700" min="0" max="5000"></label>
      <label>arXiv target<input type="number" name="arxiv" value="0" min="0" max="500"></label>
      <label>arXiv snapshot path (optional)<input type="text" name="arxiv_snapshot"
             placeholder="blank = auto-download via kagglehub"
             value="{_esc(config.get('arxiv_snapshot') or '')}"></label>
      <label>Output manifest<input type="text" name="out" value="eval/corpus/manifest_real.json"></label>
      <label>Model<select name="model">{_model_options_html(config.get('model'))}</select></label>
      <label>Prompt version<input type="text" name="prompt_version" placeholder="blank = CURRENT"
             value="{_esc(config.get('prompt_version') or '')}"></label>
      <label>Correction attempts<input type="number" name="max_correction_attempts" min="0" max="5"
             value="{_esc(config.get('max_correction_attempts', 2))}"></label>
      <label class="checkbox-label"><input type="checkbox" name="refresh_cache" value="1"> Refresh discovery cache
        (ignore cached PMC/ERIC search results from a prior batch)</label>
      <button type="submit" class="btn btn-primary" id="launch-submit-btn" {"disabled" if is_active else ""}>Launch batch</button>
    </form>
    <p class="footer-note" id="launch-note" style="{'display:block;' if is_active else 'display:none;'}">A batch is already running — stop it before launching another.</p>
  </div>

  <h2>Discovery — candidates found per source</h2>
  <div class="card">
    <table class="idx-table">
      <thead><tr><th>Source</th><th>Found / target</th><th>Progress</th></tr></thead>
      <tbody id="discover-body">{_source_rows(discover)}</tbody>
    </table>
  </div>

  <h2 id="fetch-header">Prefetch-verify — {fetch_done_count}/{fetch_total} attempted ({fetch_ok} OK, {fetch_fail} failed)</h2>
  <div class="card">
    <div class="table-scroll">
      <table class="idx-table">
        <thead><tr><th>Status</th><th>Article</th><th>Detail</th></tr></thead>
        <tbody id="fetch-body">{_fetch_rows(fetch)}</tbody>
      </table>
    </div>
  </div>

  <h2>Previous runs</h2>
  <div class="card">
    <div class="table-scroll">
      <table class="idx-table">
        <thead><tr><th>Label</th><th>Status</th><th>Config</th><th>Fetched</th><th>Started</th><th>Finished</th></tr></thead>
        <tbody>{_history_rows(history or [])}</tbody>
      </table>
    </div>
  </div>

  {_live_console_html()}
</div>
<script>
  (function () {{
    var STATUS_LABELS = {{
      discovering: ['Discovering', 'var(--status-warn)'],
      fetching: ['Fetching', 'var(--status-warn)'],
      generating: ['Generating', 'var(--status-warn)'],
      ingesting: ['Ingesting', 'var(--status-warn)'],
      completed: ['Completed', 'var(--status-good)'],
      error: ['Error', 'var(--status-critical)'],
      stopped_by_user: ['Stopped', 'var(--status-critical)']
    }};

    function esc(s) {{
      var d = document.createElement('div');
      d.textContent = (s === null || s === undefined) ? '' : String(s);
      return d.innerHTML;
    }}

    function sourceRows(discover) {{
      var bySource = (discover && discover.by_source) || {{}};
      var keys = Object.keys(bySource);
      if (!keys.length) return '<tr><td colspan="3" class="empty-note">No discovery data yet.</td></tr>';
      return keys.map(function (source) {{
        var c = bySource[source] || {{}};
        var found = c.found || 0, target = c.target || 0;
        var pct = target ? Math.min(100, Math.round(100 * found / target)) : 0;
        return '<tr><td>' + esc(source) + '</td><td class="num">' + found + '/' + target + '</td>' +
               '<td><div class="bar-track"><div class="bar-fill" style="width:' + pct + '%;"></div></div></td></tr>';
      }}).join('');
    }}

    function fetchRows(fetchState) {{
      var results = (fetchState && fetchState.results) || [];
      if (!results.length) return '<tr><td colspan="3" class="empty-note">No fetch attempts yet.</td></tr>';
      var shown = results.slice(-200).slice().reverse();
      return shown.map(function (r) {{
        var badge = r.ok ? '<span class="ok-badge">OK</span>' : '<span class="fail-badge">FAIL</span>';
        return '<tr><td>' + badge + '</td><td>' + esc(r.id) + '</td><td class="detail-cell">' +
               esc(r.chars_or_detail || '') + '</td></tr>';
      }}).join('');
    }}

    function applyState(state) {{
      var status = state.status || 'unknown';
      var labelColor = STATUS_LABELS[status] || [status, 'var(--text-secondary)'];
      var isActive = ['discovering', 'fetching', 'generating', 'ingesting'].indexOf(status) !== -1;
      var config = state.config || {{}};
      var discover = state.discover || {{}};
      var fetchState = state.fetch || {{}};
      var fetchTotal = fetchState.total || 0, fetchOk = fetchState.ok || 0, fetchFail = fetchState.fail || 0;
      var fetchDone = fetchOk + fetchFail;

      var pill = document.getElementById('status-pill');
      pill.textContent = labelColor[0];
      pill.style.background = labelColor[1];
      document.getElementById('batch-label').textContent = state.label || '(no batch run yet)';
      document.getElementById('stop-button-container').innerHTML = isActive
        ? '<form method="POST" action="/stop-scrape" class="inline-form"><button type="submit" class="btn btn-danger">Stop</button></form>'
        : '';
      document.getElementById('config-line').innerHTML =
        'pmc=' + esc(config.pmc != null ? config.pmc : '–') + ' &middot; eric=' + esc(config.eric != null ? config.eric : '–') +
        ' &middot; arxiv=' + esc(config.arxiv != null ? config.arxiv : '–') +
        ' &middot; out=<code>' + esc(config.out || '–') + '</code>' +
        (config.arxiv_snapshot ? ' &middot; arxiv_snapshot=<code>' + esc(config.arxiv_snapshot) + '</code>' : '') +
        (config.model ? ' &middot; model=<code>' + esc(config.model) + '</code>' : '') +
        (config.prompt_version ? ' &middot; prompt=' + esc(config.prompt_version) : '') +
        (config.model ? ' &middot; correction_attempts=' + esc(config.max_correction_attempts) : '') +
        (state.error_detail ? ' &middot; error: ' + esc(state.error_detail) : '');
      document.getElementById('discover-body').innerHTML = sourceRows(discover);
      document.getElementById('fetch-header').textContent =
        'Prefetch-verify — ' + fetchDone + '/' + fetchTotal + ' attempted (' + fetchOk + ' OK, ' + fetchFail + ' failed)';
      document.getElementById('fetch-body').innerHTML = fetchRows(fetchState);
      document.getElementById('launch-submit-btn').disabled = isActive;
      document.getElementById('launch-note').style.display = isActive ? 'block' : 'none';
      document.getElementById('launch-form').setAttribute('onsubmit', 'return ' + (!isActive) + ';');
    }}

    function poll() {{
      fetch('./.scrape_state.json', {{ cache: 'no-store' }})
        .then(function (r) {{ if (!r.ok) throw new Error('no state yet'); return r.json(); }})
        .then(applyState)
        .catch(function () {{ /* keep last-rendered state on a transient fetch error */ }});
    }}
    poll();
    setInterval(poll, 5000);
  }})();
</script>
</body>
</html>"""
