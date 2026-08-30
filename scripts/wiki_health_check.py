#!/usr/bin/env python3
"""
wiki_health_check.py — One consolidated pass across everything this session
built piecemeal in response to real problems found in enrichment output:
lint.py's checks (broken links, missing descriptions, claim evidence,
principle-claim links, trust/verification, source manifest integrity),
cross-page citation disagreement (check_citations.py), DOIs that don't
actually resolve or resolve to the wrong paper (doi_resolver.py — cached,
so cheap to re-run), same-slug duplicates across type folders — both the
deterministic self-referential-stub pattern and the remainder needing real
judgment (find_cross_folder_duplicates.py), and the size of the
still-unenriched stub/TODO backlog per type.

Meant to run two ways:
  1. Automatically after every scrape/enrich batch (run_scrape_batch.py
     calls this at the end) — cheap, since DOI resolution is cached and
     dedupe detection here is filesystem-only, no LLM calls.
  2. On a nightly schedule independent of scraper activity (see
     deploy/wiki-health-check.service/.timer), so drift gets caught even
     during quiet periods — a wrong-folder link or fabricated DOI
     introduced by a human edit, not just an enrichment batch, still shows
     up in the next scheduled run.

Every run appends one row to eval/health/history.ndjson, so trends are
visible over time (is the TODO backlog shrinking? are new citation
conflicts appearing faster than they're fixed?) instead of each run being
a disconnected snapshot with nothing to compare against.

This does NOT run find_near_duplicates.py's LLM-based near-duplicate scan
(similar titles within one folder, or the cross-folder collisions that
need real judgment) — that costs real API calls and, per this session's
GLM-vs-Sonnet spot check (40% disagreement on a 10-item sample), needs a
human or Sonnet-level judgment call per candidate, not something to fire
unattended on a schedule. Run find_near_duplicates.py directly for that.

Usage:
    python3 scripts/wiki_health_check.py                  # full check, DOIs cache-backed
    python3 scripts/wiki_health_check.py --skip-doi        # skip Crossref calls entirely (fast, offline)
    python3 scripts/wiki_health_check.py --out report.md
    python3 scripts/wiki_health_check.py --no-history      # don't append to history.ndjson (e.g. for testing)
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lint
import check_citations as cc
import find_cross_folder_duplicates as fcfd

WIKI_ROOT = Path(__file__).parent.parent
HISTORY_PATH = WIKI_ROOT / "eval" / "health" / "history.ndjson"
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories", "claims", "learner-variables")


def count_incomplete_pages() -> dict:
    """{page_type: {"total", "draft", "todo"}} — a plain filesystem scan, no
    CSV dependency (unlike enrich.py's find_pages_to_enrich, which needs the
    CSVs to match rows against and isn't meant as a standalone health metric)."""
    counts = {}
    for page_type in PAGE_TYPES:
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            continue
        draft = todo = total = 0
        for path in folder.glob("*.md"):
            if path.stem == "index":
                continue
            total += 1
            text = path.read_text(encoding="utf-8")
            if "status: draft" in text:
                draft += 1
            if "<!-- TODO -->" in text:
                todo += 1
        counts[page_type] = {"total": total, "draft": draft, "todo": todo}
    return counts


def count_total_incomplete_pages() -> int:
    """True union count of pages needing enrichment (status:draft OR
    carrying an unfilled TODO marker). count_incomplete_pages() tracks
    "draft" and "todo" as two separate per-type counts that can both be
    true of the same page, so summing them (as enrich.py's post-batch
    summary used to) double-counts and overstates the real backlog — this
    is the exact figure, used for deciding whether a repeated enrichment
    sweep is still making progress."""
    total = 0
    for page_type in PAGE_TYPES:
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            continue
        for path in folder.glob("*.md"):
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            if "status: draft" in text or "<!-- TODO -->" in text:
                total += 1
    return total


def run(skip_doi: bool = False) -> dict:
    pages = lint.all_pages()
    lint_checks = {
        "broken_links": lint.check_broken_links,
        "drafts": lint.check_draft_no_description,
        "claims": lint.check_claims_missing_evidence,
        "principles": lint.check_principles_missing_claims,
        "competing": lint.check_unfilled_competing_claims,
        "conflicts": lint.check_open_conflicts,
        "trust": lint.check_stable_unverified,
        "manifest": lint.check_manifest_integrity,
    }
    lint_results = {name: fn(pages) for name, fn in lint_checks.items()}

    citation_conflicts = cc.find_conflicts(cc.load_all_citations())
    collisions = fcfd.find_collisions()
    self_referential = fcfd.find_self_referential(collisions)
    incomplete = count_incomplete_pages()

    doi_issues = []
    if not skip_doi:
        import doi_resolver
        doi_issues = doi_resolver.check_all()

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "lint": {name: len(issues) for name, issues in lint_results.items()},
        "citation_conflicts": len(citation_conflicts),
        "doi_issues": len(doi_issues),
        "cross_folder_collisions": len(collisions),
        "cross_folder_self_referential": len(self_referential),
        "cross_folder_needs_judgment": len(collisions) - len(self_referential),
        "incomplete_pages": incomplete,
        "_detail": {
            "lint": lint_results,
            "citation_conflicts": citation_conflicts,
            "doi_issues": doi_issues,
            "self_referential": self_referential,
        },
    }


def format_report(result: dict) -> str:
    lint_total = sum(result["lint"].values())
    lint_breakdown = ", ".join(f"{k}={v}" for k, v in result["lint"].items() if v)
    lint_line = f"- Lint issues: {lint_total}" + (f" ({lint_breakdown})" if lint_breakdown else "")

    lines = [
        f"# Wiki health check — {result['timestamp']}",
        "",
        "## Summary",
        lint_line,
        f"- Citation conflicts: {result['citation_conflicts']}",
        f"- DOI resolution problems: {result['doi_issues']}",
        f"- Cross-folder slug collisions: {result['cross_folder_collisions']} "
        f"({result['cross_folder_self_referential']} resolved deterministically, "
        f"{result['cross_folder_needs_judgment']} need judgment — run "
        f"`find_near_duplicates.py --cross-folder`)",
        "",
        "## Incomplete pages by type",
    ]
    for page_type, c in result["incomplete_pages"].items():
        lines.append(f"- {page_type}: {c['total']} total, {c['draft']} draft, {c['todo']} with unfilled TODOs")

    for name, issues in result["_detail"]["lint"].items():
        if not issues:
            continue
        lines.append(f"\n## Lint: {name} ({len(issues)})")
        for i in issues[:20]:
            lines.append(f"- {i['file']}: {i['detail']}")
        if len(issues) > 20:
            lines.append(f"- ... and {len(issues) - 20} more")

    if result["_detail"]["citation_conflicts"]:
        lines.append("\n## Citation conflicts")
        lines.append(cc.format_report(result["_detail"]["citation_conflicts"]))

    if result["_detail"]["doi_issues"]:
        lines.append("\n## DOI resolution problems")
        import doi_resolver
        lines.append(doi_resolver.format_report(result["_detail"]["doi_issues"]))

    if result["_detail"]["self_referential"]:
        lines.append("\n## Cross-folder duplicates (deterministic — self-referential stub)")
        for slug, links in result["_detail"]["self_referential"].items():
            link_desc = ", ".join(f"{a} -> {b}" for a, b in links)
            lines.append(f"- {slug}: {link_desc}")

    return "\n".join(lines)


def append_history(result: dict) -> None:
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary = {k: v for k, v in result.items() if k != "_detail"}
    with open(HISTORY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(summary) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skip-doi", action="store_true", help="Skip Crossref DOI resolution (fast, fully offline)")
    parser.add_argument("--out", default=None, help="Write the report to this path instead of stdout")
    parser.add_argument("--no-history", action="store_true", help="Don't append to eval/health/history.ndjson")
    parser.add_argument("--incomplete-count", action="store_true",
                         help="Print just the exact total-incomplete-pages count (fast, no lint/citation/DOI "
                              "checks) and exit — for scripting a convergence check across repeated "
                              "enrichment sweeps")
    args = parser.parse_args()

    if args.incomplete_count:
        print(count_total_incomplete_pages())
        return

    result = run(skip_doi=args.skip_doi)
    report = format_report(result)

    if not args.no_history:
        append_history(result)

    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.out}", file=sys.stderr)
    else:
        print(report)

    total_issues = (sum(result["lint"].values()) + result["citation_conflicts"]
                     + result["doi_issues"] + result["cross_folder_needs_judgment"])
    sys.exit(0 if not total_issues else 1)


if __name__ == "__main__":
    main()
