#!/usr/bin/env python3
"""
resolve_doi_conflicts.py — Automatically resolves check_citations.py's
citation-conflict clusters (same author-year, same/similar title cited on
multiple pages with disagreeing or missing DOIs) down to one Crossref-
verified canonical DOI per cluster, then rewrites every page in the
cluster to cite it.

Never invents a DOI from model recall — a hallucinated DOI is exactly the
fabricated-citation risk this wiki's tooling already exists to catch (see
check_citations.py's module docstring, and CLAIM_TEMPLATE's anti-
fabrication rules in enrich.py). Every DOI this writes is one that was
independently confirmed, by a real Crossref lookup, to resolve to a title
matching the cluster's own citation text:

  - Most commonly: one of the DOIs some page in the cluster already
    cites (the majority-agreed one) verifies cleanly; the rest are
    typos or flatly wrong DOIs that either 404 or resolve to a
    different paper. That one clean verification becomes canonical.
  - If NONE of the already-cited DOIs verify, this falls back to a live
    Crossref bibliographic search on the cluster's own title/author
    text — still a real lookup against Crossref, never a guess — and
    verifies the top result the same way before trusting it.

A cluster is left untouched and reported for a human to look at when:
  - nothing verifies (no cited DOI checks out, and the search fallback
    found no confident match either), or
  - MORE than one candidate independently verifies to a real paper —
    meaning this was probably never one citation typo'd two different
    ways, but two genuinely different papers by the same author in the
    same year that check_citations.py's title-similarity clustering
    merged by coincidence.

Usage:
    python3 scripts/resolve_doi_conflicts.py                  # dry run, full report
    python3 scripts/resolve_doi_conflicts.py --apply           # write fixes to disk
    python3 scripts/resolve_doi_conflicts.py --key chi-2014    # just one cluster (debugging)
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc
import doi_resolver as dr

WIKI_ROOT = Path(__file__).parent.parent


def classify_doi(doi: str, cluster_title_words: set) -> dict:
    """Resolve `doi` against Crossref (cache-backed, same cache
    doi_resolver.py's own checks use) and classify it relative to this
    cluster's title: 'verified' (resolves, title matches), 'wrong_paper'
    (resolves, but to a different paper), or 'not_found' (404)."""
    cache = dr.load_cache()
    cached = cache.get(doi)
    if cached and not dr._is_stale(cached):
        result = cached
    else:
        result = dr.resolve_doi(doi)
        cache[doi] = result
        dr.save_cache(cache)

    if not result["resolved"]:
        return {"status": "not_found", "title": None}
    resolved_words = cc._words_from_text(result.get("title") or "")
    if cc._same_paper(cluster_title_words, resolved_words):
        return {"status": "verified", "title": result["title"]}
    return {"status": "wrong_paper", "title": result["title"]}


def _search_fallback(key: str, entries: list, cluster_title_words: set):
    """Try a live Crossref bibliographic search using the cluster's own
    title text, for a cluster where no already-cited DOI verified. Returns
    (doi, title) for the first search result whose title actually matches
    this cluster, or None if nothing does (including on any request
    failure — this is a best-effort fallback, not a hard requirement)."""
    author_surname, year = key.rsplit("-", 1)
    longest_entry = max(entries, key=lambda e: len(e["title_words"]))
    title_text = cc._extract_title_text(longest_entry["line"], year)
    if not title_text:
        return None
    try:
        candidates = dr.search_crossref(title_text, author_surname=author_surname)
    except Exception as e:
        print(f"  [search fallback failed for {key}: {e}]", file=sys.stderr)
        return None
    for c in candidates:
        if not c.get("doi") or not c.get("title"):
            continue
        resolved_words = cc._words_from_text(c["title"])
        if cc._same_paper(cluster_title_words, resolved_words):
            return c["doi"], c["title"]
    return None


def resolve_cluster(conflict: dict) -> dict:
    """conflict: one entry from check_citations.find_conflicts() —
    {"key", "entries", "dois"}. Returns a resolution record:
    {"key", "status": "auto_fixed"|"needs_human", ...}."""
    key = conflict["key"]
    entries = conflict["entries"]
    # The longest available title-word set is the least likely to be an
    # artifact of a truncated citation line, so use it as the reference
    # every candidate DOI's resolved title is compared against.
    cluster_title_words = max((e["title_words"] for e in entries), key=len)

    candidate_dois = sorted(d for d in conflict["dois"] if d)
    classifications = {doi: classify_doi(doi, cluster_title_words) for doi in candidate_dois}
    verified = [doi for doi, c in classifications.items() if c["status"] == "verified"]

    if len(verified) == 1:
        canonical, canonical_title = verified[0], classifications[verified[0]]["title"]
        via = "already cited"
    elif len(verified) == 0:
        found = _search_fallback(key, entries, cluster_title_words)
        if not found:
            return {"key": key, "status": "needs_human", "classifications": classifications,
                     "reason": "no already-cited DOI verified, and a Crossref bibliographic "
                               "search found no confident match either"}
        canonical, canonical_title = found
        via = "Crossref search (not previously cited by any page)"
    else:
        return {"key": key, "status": "needs_human", "classifications": classifications,
                 "reason": f"{len(verified)} different DOIs each independently verify to a real, "
                           f"matching paper — likely two distinct papers by the same author in "
                           f"the same year, not one citation typo'd differently: "
                           + "; ".join(f'{d} = "{classifications[d]["title"]}"' for d in verified)}

    changes = [{"file": e["source"], "old_doi": e["doi"]} for e in entries if e["doi"] != canonical]
    return {"key": key, "status": "auto_fixed", "canonical_doi": canonical,
             "canonical_title": canonical_title, "via": via, "changes": changes,
             "cluster_title_words": cluster_title_words}


def apply_change(rel_path: str, key: str, new_doi: str, cluster_title_words: set) -> bool:
    """Finds the specific citation line in rel_path matching `key` (author-
    year) AND this cluster's title (re-derived fresh from the file's
    current content, not from a possibly-truncated cached copy of the
    line) and rewrites just its DOI — both the `doi:X` link-text form and
    the `https://doi.org/X` URL form, independently, so a line carrying
    both isn't corrupted by a naive single string-replace. If the line
    has no DOI at all yet, appends one. Returns whether a line was found
    and changed."""
    path = WIKI_ROOT / rel_path
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    year = key.rsplit("-", 1)[-1]

    for i, raw_line in enumerate(lines):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        m = cc.CITATION_KEY_RE.search(stripped)
        if not m:
            continue
        this_key = f"{m.group(1).lower()}-{m.group(2)}"
        if this_key != key:
            continue
        this_title_words = cc._title_words(stripped, m.group(2))
        if not cc._same_paper(this_title_words, cluster_title_words):
            continue

        doi_m = cc.DOI_RE.search(stripped)
        new_line = raw_line
        if doi_m:
            old_doi = cc._normalize_doi(doi_m.group(0))
            old_doi_escaped = re.escape(old_doi)
            new_line = re.sub(r"(doi:)" + old_doi_escaped, r"\g<1>" + new_doi,
                               new_line, flags=re.IGNORECASE)
            new_line = re.sub(r"(https?://doi\.org/)" + old_doi_escaped, r"\g<1>" + new_doi,
                               new_line, flags=re.IGNORECASE)
        else:
            new_line = new_line.rstrip("\n") + f" [doi:{new_doi}](https://doi.org/{new_doi})\n"

        if new_line != raw_line:
            lines[i] = new_line
            path.write_text("".join(lines), encoding="utf-8")
            return True
        return False  # matched the line but nothing actually needed changing
    return False


def format_report(resolutions: list) -> str:
    auto_fixed = [r for r in resolutions if r["status"] == "auto_fixed"]
    needs_human = [r for r in resolutions if r["status"] == "needs_human"]
    total_changes = sum(len(r["changes"]) for r in auto_fixed)

    lines = [
        f"{len(resolutions)} conflict cluster(s) examined: "
        f"{len(auto_fixed)} auto-resolved ({total_changes} page edit(s)), "
        f"{len(needs_human)} need human judgment.\n",
    ]

    if auto_fixed:
        lines.append("## Auto-resolved\n")
        for r in auto_fixed:
            if not r["changes"]:
                continue  # every page already agreed on the canonical DOI, nothing to do
            lines.append(f"- **{r['key']}** -> `{r['canonical_doi']}` ({r['via']}) "
                          f"— \"{r['canonical_title']}\"")
            for c in r["changes"]:
                lines.append(f"  - {c['file']}: {c['old_doi'] or '(no DOI)'} -> {r['canonical_doi']}")

    if needs_human:
        lines.append("\n## Needs human judgment\n")
        for r in needs_human:
            lines.append(f"- **{r['key']}**: {r['reason']}")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="Write fixes to disk (default: dry-run report only)")
    parser.add_argument("--key", default=None, help="Only process this one conflict cluster key (e.g. chi-2014)")
    parser.add_argument("--out", default=None, help="Write the report to this path instead of stdout")
    args = parser.parse_args()

    conflicts = cc.find_conflicts(cc.load_all_citations())
    if args.key:
        conflicts = [c for c in conflicts if c["key"] == args.key]
        if not conflicts:
            print(f"No conflict cluster with key {args.key!r}.", file=sys.stderr)
            sys.exit(1)

    resolutions = []
    for i, conflict in enumerate(conflicts, 1):
        print(f"[{i}/{len(conflicts)}] resolving {conflict['key']}...", file=sys.stderr)
        resolutions.append(resolve_cluster(conflict))

    if args.apply:
        applied = failed = 0
        for r in resolutions:
            if r["status"] != "auto_fixed":
                continue
            for c in r["changes"]:
                ok = apply_change(c["file"], r["key"], r["canonical_doi"], r["cluster_title_words"])
                if ok:
                    applied += 1
                else:
                    failed += 1
                    print(f"  [WARN] could not locate/edit the citation line for {r['key']} "
                          f"in {c['file']} — left unchanged", file=sys.stderr)
        print(f"\nApplied {applied} page edit(s); {failed} could not be located and were left unchanged.",
              file=sys.stderr)

    report = format_report(resolutions)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.out}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
