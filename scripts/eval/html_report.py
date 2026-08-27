"""
html_report.py — Renders a run's aggregate + per-article results as a
self-contained, offline-viewable HTML dashboard (no CDN, no build step —
open the file directly in a browser). Written by scripts/eval_harness.py's
`report` command alongside report.md/summary.csv.

Palette/marks follow the project's dataviz conventions: fixed categorical
color per model (never reassigned when the model set changes), one hue
family per chart, thin bars with rounded data-ends, a legend, and a full
data table so nothing is chart-only.
"""

import html
import json

from . import model_catalog

# Categorical palette (validated ordering — see the dataviz skill's
# references/palette.md). Assigned to models in first-seen order and never
# reshuffled within a run. Light/dark pairs per slot.
PALETTE = [
    ("#2a78d6", "#3987e5"),  # 1 blue
    ("#eb6834", "#d95926"),  # 2 orange
    ("#1baf7a", "#199e70"),  # 3 aqua
    ("#eda100", "#c98500"),  # 4 yellow
    ("#e87ba4", "#d55181"),  # 5 magenta
    ("#008300", "#008300"),  # 6 green
    ("#4a3aa7", "#9085e9"),  # 7 violet
    ("#e34948", "#e66767"),  # 8 red
]

AUTO_REFRESH_MS = 20_000  # regenerated after every completed pair — see generate_reports() in eval_harness.py

METRICS = [
    ("total_generation_cost_usd", "Total generation cost", "$", 4),
    ("avg_latency_s", "Avg latency", "s", 1),
    ("validator_pass_rate", "Validator pass rate", "%", 0, 100),
    ("avg_completeness_score", "Avg completeness", "%", 0, 100),
    ("judge_opus_avg_score", "Opus judge avg (of 5)", "", 2, 5),
    ("judge_gpt_avg_score", "GPT judge avg (of 5)", "", 2, 5),
    ("judge_gemini_avg_score", "Gemini judge avg (of 5)", "", 2, 5),
]


def _esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _fmt(value, unit: str, decimals: int, scale100: bool = False) -> str:
    if value is None:
        return "–"
    v = value * 100 if scale100 else value
    if unit == "$":
        return f"${v:.{decimals}f}"
    if unit == "%":
        return f"{v:.{decimals}f}%"
    return f"{v:.{decimals}f}{unit}"


def _model_colors(models: list) -> dict:
    return {m: PALETTE[i % len(PALETTE)] for i, m in enumerate(models)}


def _css_vars(colors: dict) -> tuple:
    light_lines, dark_lines = [], []
    for i, (model, (light, dark)) in enumerate(colors.items(), start=1):
        light_lines.append(f"  --series-{i}: {light};")
        dark_lines.append(f"  --series-{i}: {dark};")
    return "\n".join(light_lines), "\n".join(dark_lines)


def _metric_chart(key: str, label: str, unit: str, decimals: int, rows: list, colors: dict,
                   scale100: bool = False, absolute_max: float = None) -> str:
    """absolute_max fixes the bar scale to a real ceiling (5 for a /5 judge
    score, 100 for a percentage) instead of the highest value among the rows
    shown — otherwise a 3.0/5 score renders as a nearly-full bar just because
    it happens to be the best of a mediocre bunch, which reads as far better
    than it is. Cost/latency have no natural ceiling, so those stay relative."""
    pairs = [(r["model"], r.get(key)) for r in rows]
    numeric = [v * 100 if (scale100 and v is not None) else v for _, v in pairs]
    if absolute_max:
        max_val = absolute_max
    else:
        max_val = max([v for v in numeric if v is not None], default=0) or 1

    bars = []
    for i, (model, raw_val) in enumerate(pairs):
        val = raw_val * 100 if (scale100 and raw_val is not None) else raw_val
        pct = 0 if val is None else max(2, round(100 * val / max_val))
        slot = (list(colors.keys()).index(model) % len(colors)) + 1
        display = _fmt(raw_val, unit, decimals, scale100=scale100)
        desc = model_catalog.describe(model)
        title = f"{model} ({desc}): {display}" if desc else f"{model}: {display}"
        bars.append(f"""
        <div class="bar-row" title="{_esc(title)}">
          <span class="bar-label">{_esc(model)}</span>
          <div class="bar-track">
            <div class="bar-fill" style="width:{pct}%; background:var(--series-{slot});"></div>
          </div>
          <span class="bar-value">{_esc(display)}</span>
        </div>""")

    return f"""
    <div class="chart-card">
      <h3>{_esc(label)}</h3>
      <div class="bar-chart">{''.join(bars)}</div>
    </div>"""


def _scatter_chart(rows: list, colors: dict) -> str:
    points = []
    excluded = []
    for r in rows:
        n = r.get("n_articles") or 0
        cost = (r.get("total_generation_cost_usd") or 0) / n if n else None
        scores = [r.get("judge_opus_avg_score"), r.get("judge_gpt_avg_score"), r.get("judge_gemini_avg_score")]
        scores = [s for s in scores if s is not None]
        quality = sum(scores) / len(scores) if scores else None
        if cost is None or quality is None:
            # No judge score yet is the common case mid-batch (this model
            # hasn't completed an article yet) — say so rather than just
            # silently dropping it, so a missing dot doesn't read as a bug.
            excluded.append(r["model"])
            continue
        points.append((r["model"], cost, quality))

    excluded_note = (
        f'<p class="empty-note">Not plotted yet (no judge score): {", ".join(_esc(m) for m in excluded)} — '
        f'still running.</p>' if excluded else ""
    )

    if not points:
        return '<p class="empty-note">No points yet — need at least one model with both generation cost and a judge score.</p>' + excluded_note

    W, H, PAD, PAD_BOTTOM = 520, 340, 56, 76
    max_cost = max(p[1] for p in points) or 1
    plot_bottom = H - PAD_BOTTOM

    # First pass: compute each point's true (x, y) and preferred label anchor.
    placed = []
    for model, cost, quality in points:
        x = PAD + (cost / max_cost) * (W - 2 * PAD) if max_cost else PAD
        y = plot_bottom - (quality / 5) * (plot_bottom - PAD)
        slot = (list(colors.keys()).index(model) % len(colors)) + 1
        # Flip the label to the dot's left once it's past ~65% of the plot width,
        # so a long model name never runs off the right edge of the viewBox.
        near_right_edge = x > PAD + 0.65 * (W - 2 * PAD)
        placed.append({
            "model": model, "cost": cost, "quality": quality, "slot": slot,
            "x": x, "y": y, "anchor": "end" if near_right_edge else "start",
            "label_x": x - 12 if near_right_edge else x + 12,
        })

    # Second pass: declutter label y-positions within each anchor side — two
    # points close in score would otherwise print overlapping text (label
    # text doesn't repel like a data mark does). Push later labels down just
    # enough to keep a minimum gap; the leader stays implicit since each label
    # still starts right beside its own dot's x position.
    MIN_LABEL_GAP = 15
    for anchor in ("start", "end"):
        group = sorted([p for p in placed if p["anchor"] == anchor], key=lambda p: p["y"])
        last_y = None
        for p in group:
            label_y = p["y"] if last_y is None else max(p["y"], last_y + MIN_LABEL_GAP)
            p["label_y"] = label_y
            last_y = label_y

    svg_points = []
    for p in placed:
        svg_points.append(f"""
        <g>
          <circle cx="{p['x']:.1f}" cy="{p['y']:.1f}" r="7" fill="var(--series-{p['slot']})" stroke="var(--surface-1)" stroke-width="2">
            <title>{_esc(p['model'])}{f" ({_esc(model_catalog.describe(p['model']))})" if model_catalog.describe(p['model']) else ""}: ${p['cost']:.4f}/article, {p['quality']:.2f}/5 avg judge score</title>
          </circle>
          <text x="{p['label_x']:.1f}" y="{p['label_y'] + 4:.1f}" text-anchor="{p['anchor']}" class="scatter-label">{_esc(p['model'])}</text>
        </g>""")

    fracs = (0, 0.25, 0.5, 0.75, 1.0)
    gridlines = "".join(
        f'<line x1="{PAD}" y1="{plot_bottom - f * (plot_bottom - PAD)}" x2="{W - PAD}" '
        f'y2="{plot_bottom - f * (plot_bottom - PAD)}" class="gridline" />'
        for f in fracs
    )
    y_ticks = "".join(
        f'<text x="{PAD - 10}" y="{plot_bottom - f * (plot_bottom - PAD) + 4}" class="axis-label" text-anchor="end">{f * 5:.0f}</text>'
        for f in fracs
    )
    x_ticks = "".join(
        f'<text x="{PAD + f * (W - 2 * PAD):.1f}" y="{plot_bottom + 18}" class="axis-label" text-anchor="middle">${f * max_cost:.4f}</text>'
        for f in fracs
    )

    return f"""
    <svg viewBox="0 0 {W} {H}" class="scatter-svg" role="img" aria-label="Cost per article vs. average judge score, one point per model">
      {gridlines}
      <line x1="{PAD}" y1="{plot_bottom}" x2="{W - PAD}" y2="{plot_bottom}" class="axis-line" />
      <line x1="{PAD}" y1="{PAD}" x2="{PAD}" y2="{plot_bottom}" class="axis-line" />
      {y_ticks}
      {x_ticks}
      <text x="{W / 2}" y="{H - 12}" class="axis-title" text-anchor="middle">Cost per article ($)</text>
      <text x="16" y="{plot_bottom / 2}" class="axis-title" text-anchor="middle" transform="rotate(-90 16 {plot_bottom / 2})">Avg judge score (of 5)</text>
      {''.join(svg_points)}
    </svg>
    {excluded_note}"""


def _issue_list_html(issues: list, render) -> str:
    if not issues:
        return '<li class="none">None</li>'
    return "".join(f"<li>{render(i)}</li>" for i in issues)


def _detail_table(by_model: dict, colors: dict) -> str:
    rows_html = []
    detail_id = 0
    for model, records in by_model.items():
        slot = (list(colors.keys()).index(model) % len(colors)) + 1
        for rec in sorted(records, key=lambda r: r["article_id"]):
            detail_id += 1
            row_id = f"detail-{detail_id}"
            gen = rec.get("generation") or {}
            val = rec.get("validation") or {}
            judges = rec.get("judges") or {}
            opus = judges.get("opus", {}).get("average_score")
            gpt = judges.get("gpt", {}).get("average_score")
            gemini = judges.get("gemini", {}).get("average_score")

            if "error" in gen:
                status_html = '<span class="status-dot" style="background:var(--status-critical)"></span> Gen error'
            elif val.get("passed"):
                status_html = '<span class="status-dot" style="background:var(--status-good)"></span> Passed'
            else:
                status_html = '<span class="status-dot" style="background:var(--status-critical)"></span> Failed'

            rows_html.append(f"""
        <tr class="detail-toggle" data-target="{row_id}">
          <td><span class="disclosure">&#9656;</span></td>
          <td><span class="swatch" style="background:var(--series-{slot})"></span>{_esc(model)}</td>
          <td>{_esc(rec.get('article_title', rec['article_id']))[:50]}</td>
          <td>{status_html}</td>
          <td class="num">{_fmt(val.get('completeness_score'), '%', 0, scale100=True)}</td>
          <td class="num">{_fmt(gen.get('cost_usd'), '$', 5)}</td>
          <td class="num">{_fmt(gen.get('latency_s'), 's', 1)}</td>
          <td class="num">{_fmt(opus, '', 2)}</td>
          <td class="num">{_fmt(gpt, '', 2)}</td>
          <td class="num">{_fmt(gemini, '', 2)}</td>
        </tr>
        <tr class="detail-row" id="{row_id}">
          <td colspan="10">{_detail_panel(rec, val, judges)}</td>
        </tr>""")

    return f"""
    <table class="detail-table article-detail-table">
      <colgroup>
        <col style="width:3%"><col style="width:13%"><col style="width:24%">
        <col style="width:10%"><col style="width:10%"><col style="width:8%">
        <col style="width:7%"><col style="width:7%"><col style="width:7%"><col style="width:7%">
      </colgroup>
      <thead>
        <tr><th></th><th>Model</th><th>Article</th><th>Status</th><th>Completeness</th>
            <th>Cost</th><th>Latency</th><th>Opus</th><th>GPT</th><th>Gemini</th></tr>
      </thead>
      <tbody>{''.join(rows_html)}</tbody>
    </table>"""


def _detail_panel(rec: dict, val: dict, judges: dict) -> str:
    parsed = rec.get("parsed")
    gen = rec.get("generation") or {}

    if parsed:
        contributions_html = _esc(json.dumps(parsed, indent=2))
        output_block = f'<pre class="detail-json">{contributions_html}</pre>'
    else:
        reason = gen.get("error") or rec.get("parse_error") or "no output captured"
        output_block = f'<p class="detail-empty">No parsed output — {_esc(reason)}</p>'

    validator_html = _issue_list_html(
        val.get("issues", []),
        lambda i: f'<span class="badge badge-{i["severity"]}">{i["severity"]}</span> <code>{_esc(i["field"])}</code> — {_esc(i["message"])}',
    )

    judge_blocks = []
    for jname, jdata in judges.items():
        scores = jdata.get("scores", {})
        score_str = ", ".join(f"{k}: {v}" for k, v in scores.items())
        issues_html = _issue_list_html(jdata.get("issues", []), lambda x: _esc(x))
        judge_blocks.append(f"""
          <p class="subhead">{_esc(jname)} judge — verdict: {_esc(jdata.get('verdict', '–'))} ({_esc(score_str)})</p>
          <ul class="issue-list">{issues_html}</ul>""")

    return f"""
      <div class="detail-panel">
        <p class="subhead">Full extraction output</p>
        {output_block}
        <p class="subhead">Validator issues</p>
        <ul class="issue-list">{validator_html}</ul>
        {"".join(judge_blocks)}
      </div>"""


PHASE_LABELS = {
    "done": "Done",
    "done-with-errors": "Done (errors)",
    "running": "Running",
    "queued": "Queued",
}


def _queue_section(queue_status: list, colors: dict) -> str:
    """Which models are tested vs. still in the queue, at a glance — without
    this, a model that hasn't produced a result file yet is indistinguishable
    from one that was never configured, which is exactly what made "why does
    the dashboard only show 2 of 5 models" confusing mid-batch."""
    if not queue_status:
        return ""
    rows_html = []
    for s in queue_status:
        model = s["model"]
        slot = (list(colors.keys()).index(model) % len(colors)) + 1 if model in colors else 1
        pct = round(100 * s["done"] / s["total"]) if s["total"] else 0
        count_str = f"{s['done']}/{s['total']}" + (f" ({s['errors']} err)" if s["errors"] else "")
        desc = model_catalog.describe(model)
        desc_html = f'<span class="queue-model-desc">{_esc(desc)}</span>' if desc else ""
        rows_html.append(f"""
        <div class="queue-row">
          <span class="swatch" style="background:var(--series-{slot})"></span>
          <span class="queue-model">
            <span class="queue-model-name">{_esc(model)}</span>
            {desc_html}
          </span>
          <span class="queue-badge queue-badge-{s['phase']}">{_esc(PHASE_LABELS.get(s['phase'], s['phase']))}</span>
          <div class="bar-track queue-track"><div class="bar-fill" style="width:{max(2, pct)}%; background:var(--series-{slot});"></div></div>
          <span class="queue-count">{_esc(count_str)}</span>
        </div>""")

    n_done = sum(1 for s in queue_status if s["phase"] in ("done", "done-with-errors"))
    return f"""
    <div class="card queue-card">
      <h3>Model queue &mdash; {n_done}/{len(queue_status)} model(s) complete</h3>
      {''.join(rows_html)}
    </div>"""


def _legend(colors: dict) -> str:
    items = []
    for i, model in enumerate(colors, start=1):
        desc = model_catalog.describe(model)
        title = f' title="{_esc(desc)}"' if desc else ""
        items.append(f'<span class="legend-item"{title}><span class="swatch" style="background:var(--series-{i})"></span>{_esc(model)}</span>')
    return f'<div class="legend">{"".join(items)}</div>'


def _failure_section(failure_summary: dict, colors: dict) -> str:
    if not failure_summary:
        return ""
    blocks = []
    for model, data in failure_summary.items():
        slot = (list(colors.keys()).index(model) % len(colors)) + 1 if model in colors else 1
        parts = [f'<h3><span class="swatch" style="background:var(--series-{slot})"></span>{_esc(model)}</h3>']

        if data.get("validator_top_issues"):
            items = "".join(
                f'<li><span class="badge badge-{i["severity"]}">{i["severity"]}</span> '
                f'<code>{_esc(i["field"])}</code> — {_esc(i["message"])} '
                f'<span class="count-tag">&times;{i["count"]}</span></li>'
                for i in data["validator_top_issues"]
            )
            parts.append(f'<p class="subhead">Most common validator issues</p><ul class="issue-list">{items}</ul>')

        if data.get("judge_keyword_tally"):
            chips = "".join(
                f'<span class="chip">{_esc(bucket)}: {count}</span>'
                for bucket, count in data["judge_keyword_tally"].items()
            )
            parts.append(f'<p class="subhead">Judge complaint categories (failed verdicts)</p><div class="chip-row">{chips}</div>')

        if data.get("worst_articles"):
            items = "".join(
                f'<li>{_esc(a["article_id"])} — {a["avg_judge_score"]}/5 avg judge score</li>'
                for a in data["worst_articles"]
            )
            parts.append(f'<p class="subhead">Lowest-scoring articles</p><ul class="issue-list">{items}</ul>')

        if data.get("subclaim_unsupported_samples"):
            items = "".join(
                f'<li>({_esc(s["article_id"])}, {_esc(s["judge"])} judge, {_esc(s["contribution_slug"])}): '
                f'&ldquo;{_esc(s["subclaim_text"])}&rdquo; — {_esc(s["reasoning"])}</li>'
                for s in data["subclaim_unsupported_samples"]
            )
            parts.append(f'<p class="subhead">Subclaim-level judging (FActScore avg: '
                         f'{_esc(data.get("subclaim_factscore_avg"))}) — unsupported subclaims</p>'
                         f'<ul class="issue-list">{items}</ul>')

        blocks.append(f'<div class="failure-block">{"".join(parts)}</div>')

    return f'<div class="card failure-grid">{"".join(blocks)}</div>'


def _exec_summary_section(summary: dict, colors: dict) -> str:
    if not summary:
        return ""
    parts = [f'<p class="exec-headline">{summary["n_models"]} model(s) &middot; '
             f'{summary["total_articles"]} article results &middot; ${summary["total_cost_usd"]} spent so far</p>']

    rec = summary.get("recommendation")
    if rec:
        slot = (list(colors.keys()).index(rec["model"]) % len(colors)) + 1 if rec["model"] in colors else 1
        cost_str = f", ${rec['cost_per_article']:.4f}/article" if rec.get("cost_per_article") else ""
        parts.append(f"""
        <div class="rec-card">
          <span class="swatch" style="background:var(--series-{slot})"></span>
          <div>
            <div class="rec-model">Recommended so far: <code>{_esc(rec['model'])}</code></div>
            <div class="rec-detail">{rec['quality']:.2f}/5 avg judge score{cost_str}</div>
          </div>
        </div>""")
    else:
        parts.append('<p class="empty-note">No model has a judge score yet.</p>')

    if summary.get("ranked_models"):
        rows_html = "".join(
            f'<tr><td><span class="swatch" style="background:var(--series-'
            f'{(list(colors.keys()).index(m["model"]) % len(colors)) + 1 if m["model"] in colors else 1}"></span>{_esc(m["model"])}</td>'
            f'<td class="num">{m["quality"]:.2f}/5</td>'
            f'<td class="num">{_fmt(m["cost_per_article"], "$", 5)}</td>'
            f'<td class="num">{_fmt(m["validator_pass_rate"], "%", 0, scale100=True)}</td>'
            f'<td class="num">{m["n_articles"]}{" (partial)" if m["partial_sample"] else ""}</td></tr>'
            for m in summary["ranked_models"]
        )
        parts.append(f"""
        <table class="detail-table exec-rank-table">
          <thead><tr><th>Model</th><th>Judge score</th><th>Cost/article</th><th>Validator pass rate</th><th>Articles</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>""")

    if summary.get("caveats"):
        items = "".join(f"<li>{_esc(c)}</li>" for c in summary["caveats"])
        parts.append(f'<p class="subhead">Caveats</p><ul class="issue-list">{items}</ul>')

    if summary.get("process_fixes"):
        items = "".join(
            f'<li><span class="chip">{_esc(f["issue"])} &times;{f["count"]}</span> {_esc(f["recommendation"])}</li>'
            for f in summary["process_fixes"]
        )
        parts.append(f'<p class="subhead">Recommended fixes to the extraction prompt / validator</p>'
                     f'<ul class="issue-list fix-list">{items}</ul>')
    else:
        parts.append('<p class="empty-note">No systematic process issues detected yet.</p>')

    return f'<div class="card">{"".join(parts)}</div>'


def render_html(run_id: str, generated: str, rows: list, by_model: dict, failure_summary: dict = None,
                 exec_summary: dict = None, queue_status: list = None) -> str:
    models = [r["model"] for r in rows]
    for s in (queue_status or []):
        if s["model"] not in models:
            # A queued/not-yet-started model has no row yet (compute_rows only
            # sees completed pairs) — append it so it still gets a stable,
            # non-colliding color slot in the queue section below.
            models.append(s["model"])
    colors = _model_colors(models)
    light_vars, dark_vars = _css_vars(colors)

    charts = "".join(
        _metric_chart(key, label, unit, decimals, rows, colors, scale100=(unit == "%"),
                      absolute_max=(spec[0] if spec else None))
        for key, label, unit, decimals, *spec in METRICS
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Eval run: {_esc(run_id)}</title>
<style>
  :root {{
    color-scheme: light;
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
    --gridline: #e1e0d9; --axis: #c3c2b7;
    --status-good: #0ca30c; --status-critical: #d03b3b; --status-warning: #fab219;
    --border: rgba(11,11,11,0.10);
{light_vars}
  }}
  /* Variables live on :root (not .viz-root) so body's `background: var(--page)`
     below — an ANCESTOR of .viz-root in the DOM — can actually see them.
     Custom properties cascade to descendants only; declaring these one level
     too low left dark-mode text color (white) flipping correctly while the
     page background silently fell back to the browser default (white),
     making most of the page's text invisible against it. */
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{
      --surface-1: #1a1a19; --page: #0d0d0d;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
      --gridline: #2c2c2a; --axis: #383835;
      --status-good: #0ca30c; --status-critical: #e66767; --status-warning: #fab219;
      --border: rgba(255,255,255,0.10);
{dark_vars}
    }}
  }}
  :root[data-theme="dark"] {{
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
    --gridline: #2c2c2a; --axis: #383835;
    --status-good: #0ca30c; --status-critical: #e66767; --status-warning: #fab219;
    --border: rgba(255,255,255,0.10);
{dark_vars}
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  .viz-root {{ max-width: 1040px; margin: 0 auto; padding: 32px 20px 64px; color: var(--text-primary); }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  .meta {{ color: var(--text-secondary); font-size: 13px; margin-bottom: 24px; }}
  h2 {{ font-size: 16px; margin: 36px 0 12px; }}
  h3 {{ font-size: 13px; color: var(--text-secondary); margin: 0 0 12px; font-weight: 600; }}
  .card {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 20px; }}
  .chart-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }}
  .chart-card {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; padding: 16px 20px; }}
  .bar-row {{ display: grid; grid-template-columns: 130px 1fr 70px; align-items: center; gap: 10px; padding: 5px 0; }}
  .bar-label {{ font-size: 12px; color: var(--text-secondary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .bar-track {{ height: 16px; background: var(--gridline); border-radius: 4px; }}
  .bar-fill {{ height: 16px; border-radius: 4px; min-width: 4px; }}
  .bar-value {{ font-size: 12px; color: var(--text-primary); font-variant-numeric: tabular-nums; text-align: right; }}
  .legend {{ display: flex; flex-wrap: wrap; gap: 14px; margin: 8px 0 20px; font-size: 12px; color: var(--text-secondary); }}
  .legend-item {{ display: inline-flex; align-items: center; gap: 6px; }}
  .swatch {{ display: inline-block; width: 10px; height: 10px; border-radius: 3px; }}
  .scatter-svg {{ width: 100%; height: auto; }}
  .gridline {{ stroke: var(--gridline); stroke-width: 1; }}
  .axis-line {{ stroke: var(--axis); stroke-width: 1; }}
  .axis-label, .axis-title {{ fill: var(--text-muted); font-size: 10px; }}
  .axis-title {{ font-size: 11px; }}
  .scatter-label {{ fill: var(--text-secondary); font-size: 11px; }}
  .detail-table {{ width: 100%; border-collapse: collapse; font-size: 13px; background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }}
  .detail-table th {{ text-align: left; padding: 10px 12px; color: var(--text-muted); font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.03em; border-bottom: 1px solid var(--border); }}
  .detail-table td {{ padding: 9px 12px; border-bottom: 1px solid var(--gridline); }}
  .detail-table td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .detail-table tr:last-child td {{ border-bottom: none; }}
  .article-detail-table {{ table-layout: fixed; }}
  .article-detail-table th, .article-detail-table .detail-toggle td {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .breadcrumb {{ margin-bottom: 10px; }}
  .breadcrumb a {{ color: var(--text-secondary); font-size: 13px; text-decoration: none; }}
  .breadcrumb a:hover {{ color: var(--text-primary); text-decoration: underline; }}
  .detail-toggle {{ cursor: pointer; }}
  .detail-toggle:hover td {{ background: var(--gridline); }}
  .disclosure {{ display: inline-block; color: var(--text-muted); transition: transform 0.15s; }}
  .detail-toggle.expanded .disclosure {{ transform: rotate(90deg); }}
  .detail-row {{ display: none; }}
  .detail-row.expanded {{ display: table-row; }}
  .detail-row td {{ padding: 16px; background: var(--page); }}
  .detail-panel {{ font-size: 12px; }}
  .detail-json {{ background: var(--gridline); border-radius: 8px; padding: 12px; overflow-x: auto; max-height: 360px; white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11px; line-height: 1.5; margin: 0 0 12px; }}
  .detail-empty {{ color: var(--text-muted); margin: 0 0 12px; }}
  .issue-list .none {{ color: var(--text-muted); }}
  .status-dot {{ display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 6px; }}
  .empty-note {{ color: var(--text-muted); font-size: 13px; }}
  .footer-note {{ margin-top: 28px; color: var(--text-muted); font-size: 12px; }}
  .failure-grid {{ display: flex; flex-direction: column; gap: 24px; }}
  .failure-block h3 {{ font-size: 14px; color: var(--text-primary); display: flex; align-items: center; gap: 8px; margin: 0 0 10px; }}
  .subhead {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.03em; color: var(--text-muted); margin: 14px 0 6px; }}
  .issue-list {{ margin: 0; padding-left: 0; list-style: none; font-size: 13px; }}
  .issue-list li {{ padding: 4px 0; border-bottom: 1px solid var(--gridline); }}
  .issue-list li:last-child {{ border-bottom: none; }}
  .issue-list code {{ background: var(--gridline); padding: 1px 5px; border-radius: 4px; font-size: 12px; }}
  .badge {{ display: inline-block; font-size: 10px; text-transform: uppercase; padding: 1px 6px; border-radius: 4px; margin-right: 4px; }}
  .badge-error {{ background: var(--status-critical); color: #fff; }}
  .badge-warning {{ background: var(--status-warning); color: #0b0b0b; }}
  .count-tag {{ color: var(--text-muted); font-size: 12px; float: right; }}
  .chip-row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .chip {{ background: var(--gridline); color: var(--text-secondary); font-size: 12px; padding: 4px 10px; border-radius: 999px; }}
  .exec-headline {{ font-size: 14px; color: var(--text-secondary); margin: 0 0 16px; }}
  .rec-card {{ display: flex; align-items: flex-start; gap: 10px; background: var(--gridline); border-radius: 10px; padding: 14px 16px; margin-bottom: 20px; }}
  .rec-card .swatch {{ width: 14px; height: 14px; margin-top: 3px; }}
  .rec-model {{ font-size: 15px; font-weight: 600; color: var(--text-primary); }}
  .rec-model code {{ background: var(--surface-1); padding: 1px 6px; border-radius: 4px; }}
  .rec-detail {{ font-size: 13px; color: var(--text-secondary); margin-top: 2px; }}
  .exec-rank-table {{ margin-bottom: 20px; }}
  .fix-list li {{ padding: 8px 0; }}
  .queue-card {{ margin-bottom: 20px; }}
  .queue-row {{ display: grid; grid-template-columns: 12px 1fr 120px 140px 110px; align-items: center; gap: 10px; padding: 6px 0; border-bottom: 1px solid var(--gridline); }}
  .queue-row:last-child {{ border-bottom: none; }}
  .queue-model {{ display: flex; flex-direction: column; overflow: hidden; min-width: 0; }}
  .queue-model-name {{ font-size: 13px; color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .queue-model-desc {{ font-size: 11px; color: var(--text-muted); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .queue-track {{ height: 10px; }}
  .queue-count {{ font-size: 12px; color: var(--text-secondary); text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
  .queue-badge {{ font-size: 10px; text-transform: uppercase; letter-spacing: 0.02em; padding: 2px 8px; border-radius: 999px; text-align: center; background: var(--gridline); color: var(--text-muted); }}
  .queue-badge-done {{ background: var(--status-good); color: #fff; }}
  .queue-badge-done-with-errors {{ background: var(--status-warning); color: #0b0b0b; }}
  .queue-badge-running {{ background: var(--status-warning); color: #0b0b0b; }}
  .tabs {{ display: flex; gap: 4px; border-bottom: 1px solid var(--border); margin-bottom: 20px; }}
  .tab-btn {{
    font: inherit; font-size: 13px; font-weight: 600; color: var(--text-secondary);
    background: none; border: none; border-bottom: 2px solid transparent;
    padding: 10px 14px; cursor: pointer; margin-bottom: -1px;
  }}
  .tab-btn:hover {{ color: var(--text-primary); }}
  .tab-btn.active {{ color: var(--text-primary); border-bottom-color: var(--series-1); }}
  .tab-panel {{ display: none; }}
  .tab-panel.active {{ display: block; }}
</style>
</head>
<body>
<div class="viz-root">
  <div class="breadcrumb"><a href="../index.html">&larr; All runs</a></div>
  <h1>Eval run: {_esc(run_id)}</h1>
  <div class="meta">Generated {_esc(generated)} &middot; {len(models)} model(s) &middot; {sum(r.get('n_articles', 0) for r in rows)} article results &middot; auto-refreshes every {AUTO_REFRESH_MS // 1000}s</div>

  {_queue_section(queue_status or [], colors)}

  <div class="tabs" role="tablist">
    <button class="tab-btn active" data-target="tab-summary" role="tab" aria-selected="true">Summary</button>
    <button class="tab-btn" data-target="tab-cost-quality" role="tab" aria-selected="false">Cost vs. quality</button>
    <button class="tab-btn" data-target="tab-metrics" role="tab" aria-selected="false">Per-model metrics</button>
    <button class="tab-btn" data-target="tab-failures" role="tab" aria-selected="false">Failure patterns</button>
    <button class="tab-btn" data-target="tab-detail" role="tab" aria-selected="false">Per-article detail</button>
  </div>

  <div id="tab-summary" class="tab-panel active">
    {_exec_summary_section(exec_summary or {}, colors)}
  </div>

  <div id="tab-cost-quality" class="tab-panel">
    <div class="card">
      {_scatter_chart(rows, colors)}
      {_legend(colors)}
    </div>
  </div>

  <div id="tab-metrics" class="tab-panel">
    <div class="chart-grid">{charts}</div>
  </div>

  <div id="tab-failures" class="tab-panel">
    {_failure_section(failure_summary or {}, colors)}
  </div>

  <div id="tab-detail" class="tab-panel">
    {_detail_table(by_model, colors)}
  </div>

  <p class="footer-note">Raw per-article JSON, report.md, and summary.csv live alongside this file in the same run directory.</p>
</div>
<script>
  function activateTab(target) {{
    var btn = document.querySelector('.tab-btn[data-target="' + target + '"]');
    if (!btn) return;
    document.querySelectorAll('.tab-btn').forEach(function (b) {{ b.classList.remove('active'); b.setAttribute('aria-selected', 'false'); }});
    document.querySelectorAll('.tab-panel').forEach(function (p) {{ p.classList.remove('active'); }});
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');
    document.getElementById(target).classList.add('active');
  }}

  function expandedSet() {{
    try {{ return new Set(JSON.parse(localStorage.getItem('eval-report-expanded') || '[]')); }}
    catch (e) {{ return new Set(); }}
  }}
  function saveExpanded(set) {{
    try {{ localStorage.setItem('eval-report-expanded', JSON.stringify(Array.from(set))); }} catch (e) {{}}
  }}

  // Binds every interactive behavior against whatever's currently in the
  // DOM — called once on initial load, and again after every in-place
  // refresh (see refreshInPlace below) since replacing .viz-root's
  // innerHTML also discards its old event listeners along with the old
  // nodes they were bound to.
  function initPage() {{
    document.querySelectorAll('.tab-btn').forEach(function (btn) {{
      btn.addEventListener('click', function () {{
        activateTab(btn.dataset.target);
        try {{ localStorage.setItem('eval-report-tab', btn.dataset.target); }} catch (e) {{}}
      }});
    }});
    try {{
      var savedTab = localStorage.getItem('eval-report-tab');
      if (savedTab) activateTab(savedTab);
    }} catch (e) {{}}

    // Expandable per-article rows — state persisted the same way as the tab
    // choice, so drilling into one survives the periodic auto-refresh.
    var expanded = expandedSet();
    document.querySelectorAll('.detail-toggle').forEach(function (row) {{
      var target = document.getElementById(row.dataset.target);
      if (expanded.has(row.dataset.target)) {{
        row.classList.add('expanded');
        target.classList.add('expanded');
      }}
      row.addEventListener('click', function () {{
        row.classList.toggle('expanded');
        target.classList.toggle('expanded');
        var set = expandedSet();
        if (row.classList.contains('expanded')) {{ set.add(row.dataset.target); }} else {{ set.delete(row.dataset.target); }}
        saveExpanded(set);
      }});
    }});
  }}

  // Auto-refresh (this file is regenerated after every completed article/model
  // pair — see generate_reports() in eval_harness.py), fetched and swapped
  // into the current page instead of a full location.reload(): a real
  // navigation reloads the browser tab from scratch — blanking it, then
  // repainting everything — which reads as a jarring flash every cycle on
  // a page that refreshes every {AUTO_REFRESH_MS // 1000}s. Re-fetching the same URL and
  // replacing just .viz-root's contents updates the numbers in place with
  // no navigation, no flash, and no lost scroll position.
  function refreshInPlace() {{
    fetch(location.href, {{ cache: 'no-store' }})
      .then(function (resp) {{ return resp.text(); }})
      .then(function (text) {{
        var newRoot = new DOMParser().parseFromString(text, 'text/html').querySelector('.viz-root');
        var oldRoot = document.querySelector('.viz-root');
        if (newRoot && oldRoot) {{
          oldRoot.innerHTML = newRoot.innerHTML;
          initPage();
        }}
      }})
      .catch(function () {{}})  // a network hiccup just tries again next cycle
      .then(function () {{ setTimeout(refreshInPlace, {AUTO_REFRESH_MS}); }});
  }}

  initPage();
  setTimeout(refreshInPlace, {AUTO_REFRESH_MS});
</script>
</body>
</html>"""
