"""
auto_optimize_report.py — Self-contained HTML dashboard for one auto-optimize
run: a single evolving lineage, one test per round (see eval_harness.py's
cmd_auto_optimize) — a diverging bar per round showing its avg judge-score
delta vs. the previous round (green = improved, red = regressed; a round
dominated by generation errors is called out instead of shown as a bar,
since there's no reliable score to plot), plus the same round-by-round data
as the markdown summary in an accessible table.

Palette/theme follow the same conventions as html_report.py (this project's
dataviz skill): status colors (not categorical hues) here because the thing
being encoded is signed magnitude/direction — diverging, not identity — see
the skill's color-formula guidance on when each applies.
"""

import html

PHASE_COLORS = ("var(--status-good)", "var(--status-critical)")  # (improved, regressed)


def _esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _round_row(r: dict, max_abs: float) -> str:
    delta = r["delta_vs_previous"]
    gen_errors = r["generation_error_count"]
    if delta is None:
        fill_html = ""
        display = f"{gen_errors} gen error(s)" if gen_errors else "unknown"
    else:
        pct = min(50, round(50 * abs(delta) / max_abs))
        color = PHASE_COLORS[0] if delta >= 0 else PHASE_COLORS[1]
        side = "right" if delta >= 0 else "left"
        fill_html = f'<div class="opt-fill opt-fill-{side}" style="width:{pct}%; background:{color};"></div>'
        display = f"{delta:+.2f}"
    link = f'<a href="./{_esc(r["run_id"])}/report.html">{_esc(r["version"])}</a>'
    return f"""
    <div class="opt-row">
      <span class="opt-label">Round {r['round']} &middot; {link}</span>
      <div class="opt-track"><div class="opt-mid"></div>{fill_html}</div>
      <span class="opt-value">{_esc(display)}</span>
    </div>"""


def _table_row(r: dict) -> str:
    delta = r["delta_vs_previous"]
    delta_str = f"{delta:+.2f}" if delta is not None else "–"
    pass_rate = f"{r['validator_pass_rate'] * 100:.0f}%" if r["validator_pass_rate"] is not None else "–"
    completeness = f"{r['avg_completeness_score'] * 100:.0f}%" if r["avg_completeness_score"] is not None else "–"
    score = f"{r['judge_score']:.2f}" if r["judge_score"] is not None else "–"
    changes = r["changes_summary"]
    return (
        f'<tr><td>{r["round"]}</td>'
        f'<td><a href="./{_esc(r["run_id"])}/report.html">{_esc(r["version"])}</a></td>'
        f'<td class="num">{r["generation_error_count"]}</td>'
        f'<td class="num">{pass_rate}</td><td class="num">{completeness}</td>'
        f'<td class="num">{score}</td><td class="num">{delta_str}</td>'
        f'<td class="changes-cell">{_esc(changes)}</td></tr>'
    )


def render_html(round_log: list, baseline_run: str, final_run_id: str, current_prompt_version: str) -> str:
    n_rounds = len(round_log)
    max_abs = max((abs(r["delta_vs_previous"]) for r in round_log if r["delta_vs_previous"] is not None),
                  default=1) or 1

    if round_log:
        chart_html = "".join(_round_row(r, max_abs) for r in round_log)
        table_rows = "".join(_table_row(r) for r in round_log)
    else:
        chart_html = ""
        table_rows = ""
    empty_note = (
        '<p class="empty-note">No round completed — stopped before the first test finished.</p>'
        if not round_log else ""
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Auto-optimize: {_esc(baseline_run)}</title>
<style>
  :root {{ color-scheme: light; }}
  .viz-root {{
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
    --gridline: #e1e0d9; --axis: #c3c2b7;
    --status-good: #0ca30c; --status-critical: #d03b3b;
    --border: rgba(11,11,11,0.10);
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) .viz-root {{
      --surface-1: #1a1a19; --page: #0d0d0d;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
      --gridline: #2c2c2a; --axis: #383835;
      --status-good: #0ca30c; --status-critical: #e66767;
      --border: rgba(255,255,255,0.10);
    }}
  }}
  :root[data-theme="dark"] .viz-root {{
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
    --gridline: #2c2c2a; --axis: #383835;
    --status-good: #0ca30c; --status-critical: #e66767;
    --border: rgba(255,255,255,0.10);
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  .viz-root {{ max-width: 900px; margin: 0 auto; padding: 32px 20px 64px; color: var(--text-primary); }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  h2 {{ font-size: 15px; margin: 28px 0 14px; }}
  .meta {{ color: var(--text-secondary); font-size: 13px; margin-bottom: 24px; }}
  .card {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 20px; }}
  .opt-row {{ display: grid; grid-template-columns: 220px 1fr 90px; align-items: center; gap: 10px; padding: 7px 0; border-bottom: 1px solid var(--gridline); }}
  .opt-row:last-child {{ border-bottom: none; }}
  .opt-label {{ font-size: 13px; color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .opt-label a {{ color: var(--text-primary); }}
  .opt-track {{ position: relative; height: 14px; background: var(--gridline); border-radius: 4px; }}
  .opt-mid {{ position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: var(--axis); }}
  .opt-fill {{ position: absolute; top: 1px; bottom: 1px; border-radius: 3px; min-width: 2px; }}
  .opt-fill-right {{ left: 50%; }}
  .opt-fill-left {{ right: 50%; }}
  .opt-value {{ font-size: 12px; text-align: right; font-variant-numeric: tabular-nums; color: var(--text-secondary); }}
  .detail-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  .detail-table th {{ text-align: left; padding: 8px 10px; color: var(--text-muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.03em; border-bottom: 1px solid var(--border); }}
  .detail-table td {{ padding: 7px 10px; border-bottom: 1px solid var(--gridline); vertical-align: top; }}
  .detail-table td.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
  .changes-cell {{ color: var(--text-secondary); font-size: 12px; max-width: 340px; }}
  .empty-note {{ color: var(--text-muted); font-size: 13px; }}
  .footer-note {{ margin-top: 12px; color: var(--text-muted); font-size: 12px; }}
</style>
</head>
<body>
<div class="viz-root">
  <h1>Auto-optimize: {_esc(baseline_run)}</h1>
  <div class="meta">
    {n_rounds} round(s) run &middot; started from <code>{_esc(baseline_run)}</code> &middot;
    final run <code>{_esc(final_run_id)}</code> &middot;
    current prompt version <code>{_esc(current_prompt_version)}</code>
  </div>
  <div class="card">
    <h2 style="margin-top:0;">Judge-score delta vs. previous round</h2>
    {chart_html}
    {empty_note}
  </div>
  <h2>Round-by-round detail</h2>
  <div class="card">
    <table class="detail-table">
      <thead><tr><th>Round</th><th>Version</th><th>Gen errors</th><th>Pass rate</th>
      <th>Completeness</th><th>Judge score</th><th>&Delta; vs previous</th><th>Changes</th></tr></thead>
      <tbody>{table_rows}</tbody>
    </table>
  </div>
  <p class="footer-note">Every round's revision becomes the new current prompt unconditionally — this is
  one evolving lineage, not a search that keeps only winners, so a regression still becomes the next
  round's starting point. Green = improved vs. the previous round, red = regressed. Click a version to
  open its own full dashboard. Raw data also at <code>auto-optimize-summary-{_esc(baseline_run)}.md</code>
  in this directory.</p>
</div>
</body>
</html>"""
