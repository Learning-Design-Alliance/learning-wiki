#!/usr/bin/env python3
"""
check_citations.py — Cross-page citation consistency checker.

Finds the same citation (same first author + year) appearing in ## Key
Sources / ## Evidence sections across multiple wiki pages, and flags any
case where they disagree — most importantly, two different DOIs given for
what should be the identical source. Built after an enrich.py batch (GLM-5.3
via --provider openrouter) cited Sailer & Homner (2020) with two different
DOIs across gamification.md and leaderboards.md, and cited Hamari, Koivisto
& Sarsa (2014) with a DOI on one page but not the other — a real,
citable-looking fabrication risk that a per-page read can't catch, since
no single page looks wrong in isolation.

This is a self-consistency check only — it does not verify a DOI against a
real registry (e.g. Crossref); it just catches disagreement across the
wiki's own pages, which is a strong signal that at least one instance was
invented or misremembered.

Usage:
    python3 scripts/check_citations.py                       # whole wiki
    python3 scripts/check_citations.py --type strategies      # one folder
    python3 scripts/check_citations.py --files strategies/games.md strategies/simulations.md
                                                                # only report conflicts touching these
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories", "claims", "learner-variables")

# Matches a citation line's leading "Author, A. ... (Year)." — single author
# ("Smith, J. (2020)") or first-of-several ("Smith, J., & Jones, K. (2020)").
CITATION_KEY_RE = re.compile(r"^[-*]?\s*([A-Z][A-Za-z'’-]+),.*?\((\d{4}[a-z]?)\)")
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s)\]]+")


def _normalize_doi(doi: str) -> str:
    return doi.strip().rstrip(".,;)").lower()


def extract_citations(text: str, source_label: str) -> list[dict]:
    """Return one entry per citation-looking line found in this page's
    Key Sources or Evidence section(s): {"key", "doi" (or None), "line", "source"}."""
    results = []
    for section_name in ("Key Sources", "Evidence"):
        m = re.search(rf"##\s*{re.escape(section_name)}\s*\n(.+?)(?=\n##\s|\Z)", text, re.DOTALL)
        if not m:
            continue
        for line in m.group(1).splitlines():
            line = line.strip()
            if not line or line.startswith("<!--"):
                continue
            key_m = CITATION_KEY_RE.search(line)
            if not key_m:
                continue
            key = f"{key_m.group(1).lower()}-{key_m.group(2)}"
            doi_m = DOI_RE.search(line)
            results.append({
                "key": key,
                "doi": _normalize_doi(doi_m.group(0)) if doi_m else None,
                "line": line[:160],
                "source": source_label,
            })
    return results


def load_all_citations(page_types=PAGE_TYPES) -> dict:
    """Return {key: [citation, ...]} across every page of the given types."""
    by_key = defaultdict(list)
    for page_type in page_types:
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            rel = str(path.relative_to(WIKI_ROOT))
            for c in extract_citations(text, rel):
                by_key[c["key"]].append(c)
    return by_key


def find_conflicts(by_key: dict, touched_files: set = None) -> list[dict]:
    """Return citation keys where >1 distinct non-null DOI is cited, or where
    some entries carry a DOI and others (same key) don't. If touched_files is
    given, only report conflicts involving at least one of those files —
    used for a targeted post-enrichment-batch check."""
    conflicts = []
    for key, entries in by_key.items():
        if len(entries) < 2:
            continue
        if touched_files and not any(e["source"] in touched_files for e in entries):
            continue
        dois = {e["doi"] for e in entries if e["doi"]}
        has_missing = any(e["doi"] is None for e in entries)
        if len(dois) > 1 or (dois and has_missing):
            conflicts.append({"key": key, "entries": entries, "dois": dois})
    return conflicts


def format_report(conflicts: list[dict]) -> str:
    if not conflicts:
        return "No citation conflicts found."
    lines = [f"{len(conflicts)} citation conflict(s):\n"]
    for c in conflicts:
        lines.append(f"## {c['key']}")
        for e in c["entries"]:
            lines.append(f"  - {e['source']}: {e['doi'] or '(no DOI)'} — {e['line']}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--type", choices=PAGE_TYPES, default=None,
                        help="Restrict the corpus scanned to one page type (default: whole wiki)")
    parser.add_argument("--files", nargs="+", default=None,
                        help="Only report conflicts touching these bundle-relative files "
                             "(the corpus scanned is still the whole wiki, so a conflict "
                             "against an older unrelated page is still caught)")
    args = parser.parse_args()

    page_types = PAGE_TYPES if args.files else ((args.type,) if args.type else PAGE_TYPES)
    by_key = load_all_citations(page_types)
    touched = set(args.files) if args.files else None
    conflicts = find_conflicts(by_key, touched)
    print(format_report(conflicts))
    sys.exit(0 if not conflicts else 1)


if __name__ == "__main__":
    main()
