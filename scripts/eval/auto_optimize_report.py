"""
auto_optimize_report.py — Self-contained HTML dashboard for one auto-optimize
run: a per-round diverging bar chart of every candidate's avg judge-score
delta (green = improved, red = regressed, adopted candidate starred), plus
the same round-by-round data as the markdown summary in an accessible table.
Written by eval_harness.py's cmd_auto_optimize() alongside the .md summary.

Palette/theme follow the same conventions as html_report.py (this project's
dataviz skill): status colors (not categorical hues) here because the thing
being encoded is signed magnitude/direction — diverging, not identity — see
the skill's color-formula guidance on when each applies.
"""

import html

PHASE_COLORS = ("var(--status-good)", "var(--status-critical)")  # (improved, regressed)


def _esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _round_section(round_entry: dict) -> str:
    candidates = round_entry["candidates"]
    max_abs = max((abs(c["delta"]) for c in candidates if c["delta"] is not None), default=1) or 1

    rows_html = []
    for c in candidates:
        adopted = c["version"] == round_entry["adopted"]
        delta = c["delta"]
        gen_errors = c.get("gen_errors", 0)
        if delta is None:
            fill_html = ""
            display = f"{gen_errors} gen error(s)" if gen_errors else "unknown"
        else:
            pct = min(50, round(50 * abs(delta) / max_abs))
            color = PHASE_COLORS[0] if delta >= 0 else PHASE_COLORS[1]
            side = "right" if delta >= 0 else "left"
            fill_html = f'<div class="opt-fill opt-fill-{side}" style="width:{pct}%; background:{color};"></div>'
            display = f"{delta:+.2f}"
        star = " &#9733;" if adopted else ""
        link = f'<a href="./{_esc(c["run_id"])}/report.html">{_esc(c["version"])}</a>'
        rows_html.append(f"""
        <div class="opt-row{' opt-row-adopted' if adopted else ''}">
          <span class="opt-label">{link} <span class="opt-lens">({_esc(c['lens'])})</span>{star}</span>
          <div class="opt-track"><div class="opt-mid"></div>{fill_html}</div>
          <span class="opt-value">{_esc(display)}</span>
        </div>""")

    table_row_parts = []
    for c in candidates:
        gen_errors = c.get("gen_errors", 0)
        if c["delta"] is not None:
            delta_str = f"{c['delta']:+.2f}"
        else:
            delta_str = f"{gen_errors} gen error(s)" if gen_errors else "unknown"
        adopted_str = "Yes" if c["version"] == round_entry["adopted"] else ""
        table_row_parts.append(
            f'<tr><td>{_esc(c["version"])}</td><td>{_esc(c["lens"])}</td>'
            f'<td class="num">{_esc(delta_str)}</td><td>{adopted_str}</td></tr>'
        )
    table_rows = "".join(table_row_parts)

    stop_note = (
        '<p class="empty-note">No candidate cleared the improvement threshold this round — search stopped here.</p>'
        if round_entry["adopted"] is None else ""
    )

    return f"""
    <div class="card round-card">
      <h3>Round {round_entry['round']} &mdash; baseline <code>{_esc(round_entry['baseline'])}</code></h3>
      <div class="opt-chart">{''.join(rows_html)}</div>
      {stop_note}
      <table class="detail-table round-table">
        <thead><tr><th>Candidate</th><th>Lens</th><th>Avg judge-score delta</th><th>Adopted?</th></tr></thead>
        <tbody>{table_rows}</tbody>
      </table>
    </div>"""


def render_html(round_log: list, baseline_run: str, final_run_id: str, current_prompt_version: str) -> str:
    n_rounds = len(round_log)
    n_adopted = sum(1 for r in round_log if r["adopted"] is not None)
    sections = "".join(_round_section(r) for r in round_log) if round_log else (
        '<p class="empty-note">No round completed — stopped before any candidate finished.</p>')

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
  .viz-root {{ max-width: 860px; margin: 0 auto; padding: 32px 20px 64px; color: var(--text-primary); }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  h3 {{ font-size: 14px; margin: 0 0 14px; }}
  .meta {{ color: var(--text-secondary); font-size: 13px; margin-bottom: 24px; }}
  .card {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px; margin-bottom: 20px; }}
  .round-card h3 code {{ background: var(--gridline); padding: 1px 6px; border-radius: 4px; font-size: 13px; }}
  .opt-row {{ display: grid; grid-template-columns: 220px 1fr 70px; align-items: center; gap: 10px; padding: 7px 0; border-bottom: 1px solid var(--gridline); }}
  .opt-row:last-child {{ border-bottom: none; }}
  .opt-row-adopted {{ background: color-mix(in srgb, var(--status-good) 8%, transparent); border-radius: 6px; }}
  .opt-label {{ font-size: 13px; color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .opt-label a {{ color: var(--text-primary); }}
  .opt-lens {{ color: var(--text-muted); font-size: 11px; }}
  .opt-track {{ position: relative; height: 14px; background: var(--gridline); border-radius: 4px; }}
  .opt-mid {{ position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: var(--axis); }}
  .opt-fill {{ position: absolute; top: 1px; bottom: 1px; border-radius: 3px; min-width: 2px; }}
  .opt-fill-right {{ left: 50%; }}
  .opt-fill-left {{ right: 50%; }}
  .opt-value {{ font-size: 12px; text-align: right; font-variant-numeric: tabular-nums; color: var(--text-secondary); }}
  .detail-table {{ width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 16px; }}
  .detail-table th {{ text-align: left; padding: 8px 10px; color: var(--text-muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.03em; border-bottom: 1px solid var(--border); }}
  .detail-table td {{ padding: 7px 10px; border-bottom: 1px solid var(--gridline); }}
  .detail-table td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .empty-note {{ color: var(--text-muted); font-size: 13px; }}
  .footer-note {{ margin-top: 12px; color: var(--text-muted); font-size: 12px; }}
</style>
</head>
<body>
<div class="viz-root">
  <h1>Auto-optimize: {_esc(baseline_run)}</h1>
  <div class="meta">
    {n_rounds} round(s) run &middot; {n_adopted} adopted &middot;
    final run <code>{_esc(final_run_id)}</code> &middot;
    current prompt version <code>{_esc(current_prompt_version)}</code>
  </div>
  {sections}
  <p class="footer-note">Green = improved vs. that round's baseline, red = regressed, &#9733; = adopted.
  Click a candidate's version to open its own full dashboard. Raw data also at
  <code>auto-optimize-summary-{_esc(baseline_run)}.md</code> in this directory.</p>
</div>
</body>
</html>"""
