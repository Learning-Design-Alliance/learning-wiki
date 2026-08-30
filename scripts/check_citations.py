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
# Excludes bare ')'/']' so a DOI embedded in a markdown link — [doi:X](url) —
# doesn't swallow the link's own closing punctuation, but still allows a
# BALANCED (...) pair as part of the DOI itself: several publishers'
# DOIs legitimately contain parens (Wiley SICI-style, ASCE, ASHA, and
# Academic Press's older series all do — e.g. 10.1061/(ASCE)0733-9445
# (2002)128:9(1119), 10.1044/0161-1461(2004/018)). The plain-exclusion
# version truncated these mid-DOI at the first paren (confirmed against
# real citations via resolve_doi_conflicts.py: chi-1996, nelson-1990, and
# several others all had a real, resolvable DOI reported as "not_found"
# only because the truncated fragment sent to Crossref wasn't a real DOI
# at all — the wiki content was fine, this regex was the actual bug).
DOI_RE = re.compile(r"10\.\d{4,9}/(?:\([^\s()]*\)|[^\s()\]])+")

# Same first-author-surname + year is not enough to call two citations "the
# same paper" — e.g. Ericsson, Krampe & Tesch-Romer (1993) vs. Ericsson &
# Simon (1993) are different works by an overlapping author list in the same
# year. Require the title text (the part of the line after the year) to
# actually overlap before treating two same-key entries as one citation.
#
# Deliberately grammatical function words ONLY — no domain topic words (no
# "learning", "research", "science", "instruction", "practice", ...). An
# earlier version included those, tuned only against the two same-author-
# year false positives this file was built to fix (Ericsson 1993 x2, Clark
# 2016 x2) — those still separate fine on their other, more distinctive
# words either way. But doi_resolver.py reuses this same word-set logic to
# compare a citation's title against Crossref's title directly, with no
# author-year prefilter, and education-research titles routinely consist
# ALMOST ENTIRELY of exactly those "topic" words (e.g. "E-Learning and the
# Science of Instruction") — stripping them collapsed both sides to an
# empty set and reported an automatic false "different paper" on a title
# that was actually identical. Confirmed by hand against two real
# doi_resolver.py false positives before narrowing this list.
_TITLE_STOPWORDS = {
    "the", "and", "of", "in", "a", "an", "for", "on", "to", "with", "from",
    "how", "what", "when", "does",
}


def _words_from_text(text: str) -> set:
    """Significant (lowercase, len>=4, stopword-filtered) words from any text
    — shared by _title_words below and doi_resolver.py's title-match check,
    so both use the exact same notion of "same paper"."""
    return {w for w in re.findall(r"[a-zA-Z]{4,}", text.lower()) if w not in _TITLE_STOPWORDS}


def _extract_title_text(line: str, year: str) -> str:
    """The raw title substring of a citation line (everything between the
    "(Year)." clause and the venue/DOI that follows) — used both to build
    the word-set _title_words compares with, and, as actual text (word
    order preserved), as a Crossref bibliographic search query when no
    already-cited DOI verifies (see resolve_doi_conflicts.py)."""
    idx = line.find(f"({year})")
    tail = line[idx + len(year) + 2:] if idx != -1 else line
    # The slice above still starts with the ". " ending the "(Year)."
    # clause, immediately before the title itself — strip that first, or
    # the title-end search below matches THAT period (since it's often
    # also immediately followed by an italic "*", when the title itself is
    # italicized) and cuts the tail down to nothing before the title text
    # is ever reached.
    tail = tail.lstrip(". ")
    # Cut at the title's actual end, not just before the DOI/URL — otherwise
    # venue text (an italicized journal/book name, "In *Conference
    # Proceedings*", a publisher name after ". ") gets pulled in as if it
    # were part of the title, diluting a genuine match below threshold (a
    # second confirmed doi_resolver.py false positive: matching venue noise
    # like "ASEE Annual Conference & Exposition Proceedings" swamped the two
    # words that actually matched).
    end_marker = re.search(r"\.\s+(?=\*|In\s)", tail)
    if end_marker:
        tail = tail[:end_marker.start() + 1]
    else:
        tail = re.split(r"doi:|https?://", tail, maxsplit=1)[0]
    return tail.strip()


def _title_words(line: str, year: str) -> set:
    return _words_from_text(_extract_title_text(line, year))


def _same_paper(a: set, b: set) -> bool:
    if not a or not b:
        return False
    union = len(a | b)
    return union > 0 and len(a & b) / union >= 0.35


def _normalize_doi(doi: str) -> str:
    doi = doi.strip().rstrip(".,;")
    # Only strip a trailing ')' if it's unbalanced (more ')' than '(' seen
    # so far) — several publishers' DOIs legitimately end in a closing
    # paren (e.g. 10.1061/(ASCE)0733-9445(2002)128:9(1119)), so an
    # unconditional rstrip(")") would corrupt those right back to the
    # truncated form DOI_RE was just fixed to stop producing. In the
    # normal case (DOI_RE's match is already balanced) this loop never
    # runs at all.
    while doi.endswith(")") and doi.count("(") < doi.count(")"):
        doi = doi[:-1]
    return doi.lower()


def extract_citations(text: str, source_label: str) -> list[dict]:
    """Return one entry per citation-looking line found in this page's
    Key Sources or Evidence section(s): {"key", "doi" (or None), "line",
    "source", "title_words"}."""
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
            year = key_m.group(2)
            key = f"{key_m.group(1).lower()}-{year}"
            doi_m = DOI_RE.search(line)
            results.append({
                "key": key,
                "doi": _normalize_doi(doi_m.group(0)) if doi_m else None,
                "line": line[:160],
                "source": source_label,
                "title_words": _title_words(line, year),
            })
    return results


def _cluster_by_title(entries: list) -> list:
    """Split same author-year entries into groups that are actually the same
    paper by title-word overlap (see _same_paper)."""
    clusters: list[list[dict]] = []
    for e in entries:
        for cluster in clusters:
            if any(_same_paper(e["title_words"], m["title_words"]) for m in cluster):
                cluster.append(e)
                break
        else:
            clusters.append([e])
    return clusters


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
    """Return (author-year, title-cluster) groups where >1 distinct non-null
    DOI is cited, or where some entries carry a DOI and others (for what
    title-clustering judged the same paper) don't. If touched_files is
    given, only report conflicts involving at least one of those files —
    used for a targeted post-enrichment-batch check."""
    conflicts = []
    for key, entries in by_key.items():
        if len(entries) < 2:
            continue
        for cluster in _cluster_by_title(entries):
            if len(cluster) < 2:
                continue
            if touched_files and not any(e["source"] in touched_files for e in cluster):
                continue
            dois = {e["doi"] for e in cluster if e["doi"]}
            has_missing = any(e["doi"] is None for e in cluster)
            if len(dois) > 1 or (dois and has_missing):
                conflicts.append({"key": key, "entries": cluster, "dois": dois})
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
