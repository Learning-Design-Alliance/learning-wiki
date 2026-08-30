"""
health_report.py — Renders eval/runs/health.html, the wiki-content health
dashboard: the same :root CSS variables as every other dashboard here
(copied rather than shared per this project's self-contained-module
convention — see home_report.py's docstring). Fed by wiki_health_check.py's
run() result; written by wiki_health_check.write_dashboard_page(), called
after every enrichment batch, every scraper ingest batch, the nightly
systemd timer, and once at dashboard_server.py startup.

Deliberately self-contained (stdlib `html` only, no relative imports) so
it can be imported two different ways without conflict: as
`scripts.eval.health_report` (package-style, if anything ever needs that)
and as a bare `import health_report` from wiki_health_check.py, which adds
scripts/eval/ directly to sys.path rather than importing the scripts.eval
package (see wiki_health_check.py's sys.path setup) — a relative import
here would break the second form.
"""

import html
import urllib.parse

AUTO_REFRESH_MS = 60_000  # this page's data only changes once per batch/nightly
                          # run, not every few seconds like an active eval run —
                          # a slower refresh than html_report.py's 20s is plenty.


def _esc(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _file_link(rel_path: str) -> str:
    """A wiki-relative path like 'claims/foo.md' as a clickable link to
    dashboard_server.py's /edit page (a simple textarea editor with a Save
    button, path-validated there — see _resolve_editable_path)."""
    return f'<a href="/edit?path={urllib.parse.quote(rel_path)}"><code>{_esc(rel_path)}</code></a>'


def _fmt_ts(iso_ts: str) -> str:
    # Keep it simple/robust: just trim the sub-second + timezone-offset noise
    # rather than pulling in a full parse — "2026-08-30T12:34:56.789012+00:00"
    # -> "2026-08-30 12:34:56 UTC". Falls back to the raw string on anything
    # unexpected rather than erroring the whole page over a display nicety.
    try:
        date_part, time_part = iso_ts.split("T")
        time_part = time_part.split("+")[0].split(".")[0]
        return f"{date_part} {time_part} UTC"
    except (ValueError, IndexError):
        return iso_ts


LINT_LABELS = {
    "broken_links": "Broken links",
    "drafts": "Draft pages missing a description",
    "claims": "Claims missing evidence / DOI",
    "principles": "Principles with no linked claims",
    "competing": "Unfilled competing-claims sections",
    "conflicts": "Open discussion conflicts",
    "trust": "Stable pages never human-verified",
    "manifest": "Source manifest integrity",
}


def _stat_tile(label: str, value, sub: str = "", warn: bool = False) -> str:
    cls = "tile warn" if warn else "tile"
    sub_html = f'<div class="tile-sub">{_esc(sub)}</div>' if sub else ""
    return f"""
    <div class="{cls}">
      <div class="tile-value">{_esc(value)}</div>
      <div class="tile-label">{_esc(label)}</div>
      {sub_html}
    </div>"""


def _type_bar(page_type: str, counts: dict) -> str:
    total = counts["total"]
    draft = counts["draft"]
    todo = counts["todo"]
    # "needs work" here is an upper-bound estimate (draft + todo can
    # double-count the same page) — good enough for a bar's visual
    # proportion, unlike count_total_incomplete_pages()'s exact union count.
    needs_work = min(total, draft + todo)
    clean = max(0, total - needs_work)
    pct_clean = round(100 * clean / total) if total else 100
    return f"""
    <div class="bar-row" title="{_esc(page_type)}: {clean}/{total} clean, {draft} draft, {todo} with unfilled TODOs">
      <span class="bar-label">{_esc(page_type)}</span>
      <div class="bar-track">
        <div class="bar-fill" style="width:{pct_clean}%;"></div>
      </div>
      <span class="bar-value">{clean}/{total}</span>
    </div>"""


def _lint_section(lint_detail: dict) -> str:
    blocks = []
    for name, issues in lint_detail.items():
        if not issues:
            continue
        label = LINT_LABELS.get(name, name)
        by_type: dict[str, list] = {}
        for issue in issues:
            by_type.setdefault(issue.get("type", name), []).append(issue)
        type_blocks = []
        for itype, group in sorted(by_type.items(), key=lambda kv: -len(kv[1])):
            rows = "".join(
                f'<li>{_file_link(i["file"])} — {_esc(i["detail"])}</li>'
                for i in group[:15]
            )
            more = f'<li class="muted">... and {len(group) - 15} more</li>' if len(group) > 15 else ""
            type_blocks.append(f"""
            <details>
              <summary>{_esc(itype)} <span class="count-badge">{len(group)}</span></summary>
              <ul class="issue-list">{rows}{more}</ul>
            </details>""")
        blocks.append(f"""
        <div class="issue-group">
          <h3>{_esc(label)} <span class="count-badge">{len(issues)}</span></h3>
          {"".join(type_blocks)}
        </div>""")
    if not blocks:
        return '<p class="muted">No lint issues found.</p>'
    return "".join(blocks)


def _judgment_section(result: dict) -> str:
    detail = result["_detail"]
    parts = []

    needs_judgment = detail.get("needs_judgment", {})
    if needs_judgment:
        rows = "".join(
            f'<li><strong>{_esc(slug)}</strong> — appears in: '
            f'{", ".join(_file_link(f"{folder}/{slug}.md") for folder in folders)}</li>'
            for slug, folders in list(needs_judgment.items())[:25]
        )
        more = (f'<li class="muted">... and {len(needs_judgment) - 25} more</li>'
                if len(needs_judgment) > 25 else "")
        parts.append(f"""
        <div class="issue-group">
          <h3>Cross-folder duplicate candidates <span class="count-badge">{len(needs_judgment)}</span></h3>
          <p class="muted">Same slug in more than one folder, not resolved by the deterministic
          self-referential-stub check — run <code>find_near_duplicates.py --cross-folder</code>
          or review by hand.</p>
          <ul class="issue-list">{rows}{more}</ul>
        </div>""")

    conflicts = detail.get("citation_conflicts", [])
    if conflicts:
        rows = []
        for c in conflicts[:20]:
            entries = "".join(
                f'<li>{_file_link(e["source"])}: {_esc(e["doi"] or "(no DOI)")} — {_esc(e["line"][:100])}</li>'
                for e in c["entries"]
            )
            rows.append(f'<li><strong>{_esc(c["key"])}</strong><ul class="issue-list">{entries}</ul></li>')
        more = f'<li class="muted">... and {len(conflicts) - 20} more</li>' if len(conflicts) > 20 else ""
        parts.append(f"""
        <div class="issue-group">
          <h3>Citation conflicts <span class="count-badge">{len(conflicts)}</span></h3>
          <p class="muted">The same author-year citation with disagreeing DOIs, or a DOI given on
          one page and missing on another for what looks like the same paper.</p>
          <ul class="issue-list">{"".join(rows)}{more}</ul>
        </div>""")

    doi_issues = detail.get("doi_issues", [])
    if result.get("doi_skipped"):
        parts.append("""
        <div class="issue-group">
          <p class="muted">DOI resolution against Crossref was skipped this pass (every automatic
          run uses --skip-doi so it stays fast — only the nightly systemd timer, or the button
          below, does real DOI validation).</p>
          <form method="post" action="/refresh-health">
            <button type="submit">Run full check now (with DOI resolution)</button>
          </form>
        </div>""")
    elif doi_issues:
        rows = "".join(
            f'<li>{_file_link(i["file"])}: <code>{_esc(i.get("doi"))}</code> — '
            f'{_esc(i.get("issue", i.get("reason", "")))} {_esc(i.get("title", ""))}</li>'
            for i in doi_issues[:20]
        )
        more = f'<li class="muted">... and {len(doi_issues) - 20} more</li>' if len(doi_issues) > 20 else ""
        parts.append(f"""
        <div class="issue-group">
          <h3>DOI resolution problems <span class="count-badge">{len(doi_issues)}</span></h3>
          <ul class="issue-list">{rows}{more}</ul>
        </div>""")

    if not parts:
        return '<p class="muted">Nothing currently needs human judgment.</p>'
    return "".join(parts)


def render_html(result: dict) -> str:
    lint_total = sum(result["lint"].values())
    doi_display = "skipped" if result.get("doi_skipped") else str(result["doi_issues"])
    total_incomplete = sum(min(c["total"], c["draft"] + c["todo"]) for c in result["incomplete_pages"].values())

    tiles = "".join([
        _stat_tile("Lint issues", lint_total, warn=lint_total > 0),
        _stat_tile("Citation conflicts", result["citation_conflicts"], warn=result["citation_conflicts"] > 0),
        _stat_tile("DOI problems", doi_display, warn=(not result.get("doi_skipped")) and result["doi_issues"] > 0),
        _stat_tile("Needs judgment", result["cross_folder_needs_judgment"],
                   sub=f"{result['cross_folder_self_referential']} auto-resolved",
                   warn=result["cross_folder_needs_judgment"] > 0),
        _stat_tile("Incomplete pages", total_incomplete, sub="draft or unfilled TODO", warn=total_incomplete > 0),
    ])

    type_bars = "".join(_type_bar(t, c) for t, c in result["incomplete_pages"].items())

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Wiki Health</title>
<style>
  :root {{
    color-scheme: light;
    --surface-1: #fcfcfb; --page: #f9f9f7;
    --text-primary: #0b0b0b; --text-secondary: #52514e; --text-muted: #898781;
    --border: rgba(11,11,11,0.10);
    --good: #1baf7a; --warn: #eb6834;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{
      --surface-1: #1a1a19; --page: #0d0d0d;
      --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
      --border: rgba(255,255,255,0.10);
      --good: #199e70; --warn: #d95926;
    }}
  }}
  :root[data-theme="dark"] {{
    --surface-1: #1a1a19; --page: #0d0d0d;
    --text-primary: #ffffff; --text-secondary: #c3c2b7; --text-muted: #898781;
    --border: rgba(255,255,255,0.10);
    --good: #199e70; --warn: #d95926;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  .viz-root {{ max-width: 960px; margin: 0 auto; padding: 48px 20px 96px; color: var(--text-primary); }}
  h1 {{ font-size: 24px; margin: 0 0 4px; }}
  h3 {{ font-size: 14px; margin: 0 0 8px; display: flex; align-items: center; gap: 8px; }}
  .meta {{ color: var(--text-secondary); font-size: 13px; margin-bottom: 8px; }}
  .back-link {{ font-size: 13px; color: var(--text-secondary); text-decoration: none; }}
  .back-link:hover {{ color: var(--text-primary); }}
  .tiles {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin: 28px 0 36px; }}
  @media (max-width: 760px) {{ .tiles {{ grid-template-columns: repeat(2, 1fr); }} }}
  .tile {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px; padding: 16px; }}
  .tile.warn .tile-value {{ color: var(--warn); }}
  .tile-value {{ font-size: 26px; font-weight: 600; color: var(--good); }}
  .tile-label {{ font-size: 12px; color: var(--text-secondary); margin-top: 4px; }}
  .tile-sub {{ font-size: 11px; color: var(--text-muted); margin-top: 2px; }}
  section {{ margin-bottom: 36px; }}
  section > h2 {{ font-size: 16px; margin: 0 0 14px; }}
  .bar-row {{ display: grid; grid-template-columns: 140px 1fr 64px; align-items: center; gap: 10px;
              font-size: 13px; margin-bottom: 8px; }}
  .bar-label {{ color: var(--text-secondary); }}
  .bar-track {{ height: 8px; background: var(--border); border-radius: 4px; overflow: hidden; }}
  .bar-fill {{ height: 100%; background: var(--good); border-radius: 4px; }}
  .bar-value {{ text-align: right; color: var(--text-muted); font-size: 12px; }}
  .issue-group {{ background: var(--surface-1); border: 1px solid var(--border); border-radius: 12px;
                  padding: 16px 20px; margin-bottom: 14px; }}
  .count-badge {{ display: inline-block; background: var(--border); color: var(--text-secondary);
                  font-size: 11px; padding: 1px 7px; border-radius: 10px; }}
  details {{ margin: 6px 0; }}
  summary {{ cursor: pointer; font-size: 13px; color: var(--text-secondary); }}
  .issue-list {{ font-size: 12px; color: var(--text-secondary); margin: 8px 0 0; padding-left: 18px; }}
  .issue-list li {{ margin-bottom: 4px; }}
  .issue-list code {{ color: var(--text-primary); }}
  .muted {{ color: var(--text-muted); font-size: 12px; }}
  p.muted {{ font-size: 13px; }}
  button {{ margin-top: 10px; padding: 7px 16px; font-size: 13px; border-radius: 8px;
            border: 1px solid var(--border); background: var(--good); color: #fff; cursor: pointer; }}
</style>
</head>
<body>
<div class="viz-root">
  <a class="back-link" href="/index.html">&larr; Dashboard home</a>
  <h1>Wiki Health</h1>
  <div class="meta">Last scanned {_esc(_fmt_ts(result["timestamp"]))} &middot; auto-refreshes every
  {AUTO_REFRESH_MS // 1000}s</div>

  <div class="tiles">{tiles}</div>

  <section>
    <h2>Pages by type</h2>
    {type_bars}
  </section>

  <section>
    <h2>Needs human judgment</h2>
    {_judgment_section(result)}
  </section>

  <section>
    <h2>Lint findings</h2>
    {_lint_section(result["_detail"]["lint"])}
  </section>
</div>
<script>
  setTimeout(function () {{ location.reload(); }}, {AUTO_REFRESH_MS});
</script>
</body>
</html>"""
