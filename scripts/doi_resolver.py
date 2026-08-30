#!/usr/bin/env python3
"""
doi_resolver.py — Verify every DOI cited in the wiki actually exists and
matches the paper it's cited for, by resolving it against Crossref.

check_citations.py catches DOI DISAGREEMENT across pages (two pages citing
"the same paper" with different DOIs) — a strong signal something is
wrong, but it needs a second citation of the same paper to notice anything
at all, and it can't say which of two disagreeing DOIs (if either) is
right. This resolves against ground truth instead, catching two distinct
defects manual review already found by hand this session:

  - a DOI that doesn't resolve at all (strategies/fishbowl.md's fabricated
    Webb 2009 DOI, strategies/leaderboards.md's fabricated Sailer & Homner
    2020 DOI) — confirmed fabricated, not just internally inconsistent.
  - a DOI that resolves fine but to an unrelated paper (strategies/
    teach-ok.md cited a real, live Contemporary Educational Psychology DOI
    for a completely different article than the one it named) — a live
    link to the wrong content, which passes any check that only asks
    "does this DOI exist."

Results are cached (eval/corpus/doi_resolution_cache.json, keyed by DOI)
so re-running this after every scrape/enrich batch only checks DOIs newly
cited since the last run, not the whole wiki every time — Crossref is a
shared public service, and re-verifying thousands of unchanged citations
on every run would be both slow and impolite. Entries older than
CACHE_TTL_DAYS are re-checked even if unchanged, since a DOI's Crossref
record can itself be corrected after the fact.

Usage:
    python3 scripts/doi_resolver.py                  # whole wiki, cache-backed
    python3 scripts/doi_resolver.py --type strategies
    python3 scripts/doi_resolver.py --force           # ignore cache, re-check everything
    python3 scripts/doi_resolver.py --out doi-report.md
"""

import argparse
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc

sys.path.insert(0, str(Path(__file__).parent.parent))  # for scripts.eval.compliance
from scripts.eval import compliance

WIKI_ROOT = Path(__file__).parent.parent
CACHE_PATH = WIKI_ROOT / "eval" / "corpus" / "doi_resolution_cache.json"
CACHE_TTL_DAYS = 30
CROSSREF_BASE = "https://api.crossref.org/works/"


def load_cache() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def _is_stale(entry: dict) -> bool:
    return date.today() - date.fromisoformat(entry["checked_at"]) > timedelta(days=CACHE_TTL_DAYS)


def resolve_doi(doi: str) -> dict:
    """Query Crossref for this DOI. Returns {"doi", "resolved": bool,
    "title": str|None, "checked_at": iso-date}. A 404 is a real, useful
    "this DOI does not exist" result, not an error — only a genuine
    network/transport failure raises."""
    import requests
    url = f"{CROSSREF_BASE}{doi}"
    contact = os.environ.get("EVAL_HARNESS_CONTACT_EMAIL", "")
    params = {"mailto": contact} if contact else {}
    compliance.guard(url)
    resp = requests.get(url, params=params, headers={"User-Agent": compliance.USER_AGENT}, timeout=15)
    today = date.today().isoformat()
    if resp.status_code == 404:
        return {"doi": doi, "resolved": False, "title": None, "checked_at": today}
    resp.raise_for_status()
    titles = resp.json().get("message", {}).get("title") or []
    return {"doi": doi, "resolved": True, "title": titles[0] if titles else None, "checked_at": today}


def search_crossref(title_text: str, author_surname: str = None) -> list:
    """Live Crossref bibliographic search (query.bibliographic + optional
    query.author) — NOT a direct DOI lookup, and not cached the way
    resolve_doi() is (a free-text query isn't a stable cache key the way
    a DOI is). Used only as a fallback by resolve_doi_conflicts.py, for a
    conflict cluster where none of the DOIs already cited on any page
    verify — i.e. only when there's a real, specific reason to make one
    more live call, not on every citation. Returns up to 3 candidates:
    [{"doi", "title", "score"}], ranked by Crossref's own relevance score.
    Never a source of a DOI value on its own — the caller still has to
    independently verify a candidate's title actually matches before
    treating it as real (same bar as resolve_doi())."""
    import requests
    params = {"query.bibliographic": title_text, "rows": 3}
    if author_surname:
        params["query.author"] = author_surname
    contact = os.environ.get("EVAL_HARNESS_CONTACT_EMAIL", "")
    if contact:
        params["mailto"] = contact
    url = "https://api.crossref.org/works"
    compliance.guard(url)
    resp = requests.get(url, params=params, headers={"User-Agent": compliance.USER_AGENT}, timeout=15)
    resp.raise_for_status()
    items = resp.json().get("message", {}).get("items", [])
    results = []
    for item in items:
        titles = item.get("title") or []
        results.append({
            "doi": item.get("DOI"),
            "title": titles[0] if titles else None,
            "score": item.get("score", 0),
        })
    return results


def check_all(page_types=None, force: bool = False) -> list:
    """Returns flagged issues: [{"doi", "file", "line", "issue": "not_found"
    or "title_mismatch", "resolved_title"}]. Uses/updates the on-disk cache."""
    page_types = page_types or cc.PAGE_TYPES
    by_key = cc.load_all_citations(page_types)

    # One representative entry per unique DOI is enough to check against
    # Crossref — cross-page disagreement on the SAME DOI is check_citations.py's
    # job, not this one's.
    by_doi = {}
    for entries in by_key.values():
        for e in entries:
            if e["doi"] and e["doi"] not in by_doi:
                by_doi[e["doi"]] = e

    cache = load_cache()
    issues = []
    checked = 0
    for doi, entry in sorted(by_doi.items()):
        cached = cache.get(doi)
        if cached and not force and not _is_stale(cached):
            result = cached
        else:
            print(f"Resolving {doi} ({entry['source']})...", file=sys.stderr)
            try:
                result = resolve_doi(doi)
            except Exception as e:
                print(f"  [ERROR] {doi}: {e}", file=sys.stderr)
                continue
            cache[doi] = result
            checked += 1

        if not result["resolved"]:
            issues.append({"doi": doi, "file": entry["source"], "line": entry["line"],
                            "issue": "not_found", "resolved_title": None})
        elif result["title"]:
            year = entry["key"].rsplit("-", 1)[-1]
            cited_words = cc._title_words(entry["line"], year)
            resolved_words = cc._words_from_text(result["title"])
            if not cc._same_paper(cited_words, resolved_words):
                issues.append({"doi": doi, "file": entry["source"], "line": entry["line"],
                                "issue": "title_mismatch", "resolved_title": result["title"]})

    save_cache(cache)
    print(f"Checked {checked} DOI(s) against Crossref ({len(by_doi) - checked} served from cache).", file=sys.stderr)
    return issues


def format_report(issues: list) -> str:
    if not issues:
        return "No DOI resolution problems found."
    lines = [f"{len(issues)} DOI resolution problem(s):\n"]
    for i in issues:
        if i["issue"] == "not_found":
            lines.append(f"- **{i['doi']}** ({i['file']}): does not exist on Crossref — likely fabricated")
        else:
            lines.append(f"- **{i['doi']}** ({i['file']}): resolves, but to a different paper "
                          f"— \"{i['resolved_title']}\" — likely misattributed")
        lines.append(f"  cited as: {i['line']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--type", choices=cc.PAGE_TYPES, default=None,
                        help="Restrict to one page type (default: whole wiki)")
    parser.add_argument("--force", action="store_true", help="Ignore the cache, re-check every DOI")
    parser.add_argument("--out", default=None, help="Write the report to this path instead of stdout")
    args = parser.parse_args()

    page_types = (args.type,) if args.type else None
    issues = check_all(page_types, force=args.force)
    report = format_report(issues)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.out}", file=sys.stderr)
    else:
        print(report)
    sys.exit(0 if not issues else 1)


if __name__ == "__main__":
    main()
