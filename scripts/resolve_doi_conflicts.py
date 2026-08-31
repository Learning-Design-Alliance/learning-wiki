#!/usr/bin/env python3
"""
resolve_doi_conflicts.py — Automatically fixes two kinds of bad DOI, using
only real Crossref lookups, never a model's own recall (a hallucinated
DOI is exactly the fabricated-citation risk this wiki's tooling already
exists to catch — see check_citations.py's module docstring and
CLAIM_TEMPLATE's anti-fabrication rules in enrich.py):

1. Multi-page conflicts (check_citations.py's clusters — same author-year,
   same/similar title cited on more than one page with disagreeing or
   missing DOIs). Resolves every already-cited DOI against Crossref; if
   exactly one verifies (its real title matches the citation), every page
   in the cluster gets rewritten to it.

2. Single-citation DOI problems — a DOI that's simply wrong (doesn't
   resolve at all, or resolves to a different paper) even though every
   page citing this author-year-title agrees on it, so check_citations.py
   never flagged it as a cross-page disagreement (there's nothing to
   disagree with — everyone's wrong the same way). Confirmed in
   production: a citation gave 10.1001/jama.2013.2820 for Cook et al.,
   which doesn't exist — the real DOI, 10.1001/jama.2011.1234, has a
   different year AND registration number, not just a typo'd digit.

Both cases use the same fallback when nothing already cited verifies: a
live Crossref bibliographic search on the citation's own title/author
text (still a real lookup, never a guess), verified the same way before
being trusted.

A cluster or citation is left untouched and reported for a human to look
at when:
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
    python3 scripts/resolve_doi_conflicts.py --skip-standalone # conflict clusters only, skip
                                                                # the single-citation DOI pass
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc
import doi_resolver as dr

WIKI_ROOT = Path(__file__).parent.parent
NEEDS_HUMAN_SNAPSHOT_PATH = WIKI_ROOT / "eval" / "health" / "doi_needs_human.json"


def classify_doi(doi: str, cluster_title_words: set, cited_title_text: str = None) -> dict:
    """Resolve `doi` against Crossref (cache-backed, same cache
    doi_resolver.py's own checks use) and classify it relative to this
    cluster's title: 'verified' (resolves, title matches), 'wrong_paper'
    (resolves, but to a different paper), 'not_found' (404), or 'error'
    (the Crossref request itself failed even after retrying — treated the
    same as not_found by every caller: not verified, so the cluster falls
    through to the search fallback or gets reported, but a transient
    network failure on one DOI never crashes the whole run)."""
    cache = dr.load_cache()
    cached = cache.get(doi)
    if cached and not dr._is_stale(cached):
        result = cached
    else:
        try:
            result = dr.resolve_doi(doi)
        except Exception as e:
            print(f"  [resolve failed for {doi}: {e}]", file=sys.stderr)
            return {"status": "error", "title": None}
        cache[doi] = result
        dr.save_cache(cache)

    if not result["resolved"]:
        return {"status": "not_found", "title": None}
    resolved_title = result.get("title") or ""
    resolved_words = cc._words_from_text(resolved_title)
    if cc._same_paper(cluster_title_words, resolved_words):
        # Word overlap says yes — but a short, generic cited title is fully
        # contained in plenty of longer, unrelated works. cc.titles_align
        # rejects the containment case unless one title actually begins with
        # the other (a real subtitle expansion). Without it, Bandura's
        # "Social learning theory" verified against a Springer chapter called
        # "Model of Causality in Social Learning Theory" at 0.60 overlap, and
        # that DOI was written onto 69 pages.
        if cited_title_text and not cc.titles_align(cited_title_text, resolved_title):
            return {"status": "wrong_paper", "title": resolved_title}
        return {"status": "verified", "title": resolved_title}
    return {"status": "wrong_paper", "title": resolved_title}


def _cited_title_text(key: str, entries: list, cluster_title_words: set) -> str:
    """The cluster's own title as TEXT (word order intact), for the positional
    check in cc.titles_align. Read fresh from disk via _locate_citation_line
    for the same reason _search_fallback does: entries[...]["line"] is
    truncated to 160 chars and cuts into the title on long author lists."""
    _, year = key.rsplit("-", 1)
    longest = max(entries, key=lambda e: len(e["title_words"]))
    located = _locate_citation_line(longest["source"], key, cluster_title_words)
    return cc._extract_title_text(located[1].strip() if located else longest["line"], year)


def _search_fallback(key: str, entries: list, cluster_title_words: set, debug: bool = False):
    """Try a live Crossref bibliographic search using the cluster's own
    title text, for a cluster where no already-cited DOI verified. Returns
    (doi, title) for the first search result whose title actually matches
    this cluster, or None if nothing does (including on any request
    failure — this is a best-effort fallback, not a hard requirement).
    debug=True prints the exact query sent and every raw candidate
    Crossref returned (matched or not) with its word-overlap fraction, to
    diagnose a specific 'needs_human' case (see --key --debug)."""
    author_surname, year = key.rsplit("-", 1)
    longest_entry = max(entries, key=lambda e: len(e["title_words"]))
    # Re-read the full line from disk rather than trusting
    # longest_entry["line"] — extract_citations() truncates that to 160
    # chars, which cuts into the title itself for any citation with a
    # long author list (confirmed in production on a real 8-author
    # citation), producing a garbled, incomplete search query.
    located = _locate_citation_line(longest_entry["source"], key, cluster_title_words)
    full_line = located[1].strip() if located else longest_entry["line"]
    title_text = cc._extract_title_text(full_line, year)
    if debug:
        print(f"  [debug] cluster_title_words: {sorted(cluster_title_words)}", file=sys.stderr)
        print(f"  [debug] search query: title={title_text!r} author={author_surname!r}", file=sys.stderr)
    if not title_text:
        return None
    try:
        candidates = dr.search_crossref(title_text, author_surname=author_surname)
    except Exception as e:
        print(f"  [search fallback failed for {key}: {e}]", file=sys.stderr)
        return None
    if debug:
        if not candidates:
            print("  [debug] Crossref returned zero candidates", file=sys.stderr)
        for c in candidates:
            resolved_words = cc._words_from_text(c.get("title") or "")
            union = cluster_title_words | resolved_words
            overlap = len(cluster_title_words & resolved_words) / len(union) if union else 0.0
            print(f"  [debug] candidate: {c.get('doi')!r} title={c.get('title')!r} "
                  f"overlap={overlap:.2f} (need >= 0.35)", file=sys.stderr)
    for c in candidates:
        if not c.get("doi") or not c.get("title"):
            continue
        resolved_words = cc._words_from_text(c["title"])
        if cc._same_paper(cluster_title_words, resolved_words) and \
                cc.titles_align(title_text, c["title"]):
            return c["doi"], c["title"]
    return None


def resolve_cluster(conflict: dict, debug: bool = False) -> dict:
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
    cited_title = _cited_title_text(key, entries, cluster_title_words)
    classifications = {doi: classify_doi(doi, cluster_title_words, cited_title)
                       for doi in candidate_dois}
    verified = [doi for doi, c in classifications.items() if c["status"] == "verified"]

    if len(verified) == 1:
        canonical, canonical_title = verified[0], classifications[verified[0]]["title"]
        via = "already cited"
    elif len(verified) == 0:
        found = _search_fallback(key, entries, cluster_title_words, debug=debug)
        if not found:
            return {"key": key, "status": "needs_human", "classifications": classifications,
                     "files": sorted({e["source"] for e in entries}),
                     "reason": "no already-cited DOI verified, and a Crossref bibliographic "
                               "search found no confident match either"}
        canonical, canonical_title = found
        via = "Crossref search (not previously cited by any page)"
    else:
        return {"key": key, "status": "needs_human", "classifications": classifications,
                 "files": sorted({e["source"] for e in entries}),
                 "reason": f"{len(verified)} different DOIs each independently verify to a real, "
                           f"matching paper — likely two distinct papers by the same author in "
                           f"the same year, not one citation typo'd differently: "
                           + "; ".join(f'{d} = "{classifications[d]["title"]}"' for d in verified)}

    changes = [{"file": e["source"], "old_doi": e["doi"]} for e in entries if e["doi"] != canonical]

    # Verify every change is actually locatable BEFORE reporting success —
    # a page that cites this same author-year key more than once, with
    # titles too similar to disambiguate (e.g. Gentner et al.'s two related
    # 2003 papers, or Cook et al.'s two related 2013 systematic reviews —
    # genuinely different real papers by an overlapping author team,
    # clustered together here only because their titles cross the 0.35
    # same-paper threshold), can't be safely rewritten: guessing which line
    # is "the" outdated one risks silently retargeting a correct citation
    # at the wrong paper. Confirmed in production: locke-2002, gentner-2003,
    # and cook-2013 were reported "auto_fixed" on every single run, then
    # silently failed to locate at apply time and no-op'd — every run,
    # forever, with nothing to show a human this needs their attention.
    # Catching it here instead surfaces it once, honestly, as needs_human.
    unlocatable = [c for c in changes if _locate_citation_line(c["file"], key, cluster_title_words) is None]
    if unlocatable:
        return {"key": key, "status": "needs_human", "classifications": classifications,
                 "files": sorted({e["source"] for e in entries}),
                 "reason": f"identified {canonical} as the canonical DOI ({via}), but "
                           f"{len(unlocatable)} page(s) cite this author-year key more than once "
                           f"with titles too similar to safely tell which line to rewrite — likely "
                           f"two distinct papers by the same author(s) in the same year, not one "
                           f"citation typo'd differently"}

    return {"key": key, "status": "auto_fixed", "canonical_doi": canonical,
             "canonical_title": canonical_title, "via": via, "changes": changes,
             "cluster_title_words": cluster_title_words}


def resolve_standalone_issues(by_key: dict, conflict_keys: set, debug_key: str = None) -> list:
    """Handles the OTHER way a DOI can be wrong: every page citing this
    author-year-title agrees on the same DOI, so check_citations.py never
    flagged a cross-page disagreement — but the DOI itself is simply
    wrong (doesn't resolve, or resolves to a different paper). Confirmed
    in production: a citation gave a DOI for Cook et al. that doesn't
    exist at all; the real one has a different year AND registration
    number, not a typo'd digit — no amount of comparing pages against
    each other would have caught it, since nothing disagreed.

    conflict_keys: author-year keys already handled by resolve_cluster()
    in this same run — skipped here so a DOI already fixed isn't
    reprocessed against a stale (pre-fix) snapshot of by_key. Call this
    with a FRESH by_key (re-read from disk) if conflicts were applied
    first — see main().

    debug_key: print full search diagnostics (see _search_fallback), but
    only for this one author-year key — running with debug on for all of
    them would spam hundreds of lines."""
    by_doi: dict[str, list] = {}
    for key, entries in by_key.items():
        if key in conflict_keys:
            continue
        for e in entries:
            if e["doi"]:
                by_doi.setdefault(e["doi"], []).append(e)

    resolutions = []
    unique_dois = sorted(by_doi.items())
    print(f"Checking {len(unique_dois)} unique DOI(s) not already handled as a conflict "
          f"(cache-backed where possible; anything unverified falls through to a live, "
          f"uncached Crossref search, so this can take a while with no output in between)...",
          file=sys.stderr)
    for i, (doi, affected) in enumerate(unique_dois, 1):
        print(f"  [{i}/{len(unique_dois)}] checking {doi} ({affected[0]['key']})...", file=sys.stderr)
        cluster_title_words = max((e["title_words"] for e in affected), key=len)
        classification = classify_doi(doi, cluster_title_words,
                                      _cited_title_text(affected[0]["key"], affected, cluster_title_words))
        if classification["status"] == "verified":
            continue  # already correct, nothing to do

        key = affected[0]["key"]
        found = _search_fallback(key, affected, cluster_title_words, debug=(key == debug_key))
        if not found:
            resolutions.append({
                "key": key, "status": "needs_human",
                "files": sorted({e["source"] for e in affected}),
                "reason": f"cited DOI {doi} {classification['status']} against Crossref, and a "
                          f"bibliographic search on this citation's own title/author found no "
                          f"confident replacement",
            })
            continue

        new_doi, new_title = found
        resolutions.append({
            "key": key, "status": "auto_fixed", "canonical_doi": new_doi,
            "canonical_title": new_title,
            "via": f"Crossref search (every page agreed on {doi}, which {classification['status']})",
            "changes": [{"file": e["source"], "old_doi": doi} for e in affected],
            "cluster_title_words": cluster_title_words,
        })
    return resolutions


def _locate_citation_line(rel_path: str, key: str, cluster_title_words: set):
    """Finds the specific citation line in rel_path matching `key` (author-
    year), re-derived fresh from the file's actual current content — never
    from entries[...]["line"], which extract_citations() truncates to 160
    chars, cutting straight into the title for anything with a long author
    list (confirmed on a real 8-author citation: the stored line ran out
    mid-word, inside the title itself, before the DOI/URL was even
    reached). Returns (line_index, full_untruncated_line) or None if no
    matching line is found.

    Only checks this cluster's title-word overlap when MORE THAN ONE line
    on this page shares the same author-year key — that's the only case
    with anything to disambiguate (e.g. two different papers by the same
    author in the same year both cited on one page). When there's exactly
    one candidate line, using it is unambiguous regardless of how its
    wording compares to cluster_title_words, which is picked from some
    OTHER page in the cluster and can legitimately differ (a different
    subtitle, an abbreviated vs. full title, different punctuation).
    Requiring the overlap check even in the unambiguous case was a real,
    confirmed production bug: a resolve run correctly identified the
    canonical DOI for wineburg-2019 and graham-2011 (each cited on ~25
    pages) but the overlap check rejected the match on every single page,
    because cluster_title_words came from whichever page happened to have
    the most distinct title words, and other pages' shorter/differently
    worded citations of the exact same book didn't clear 0.35 overlap
    against it — 63 correct, unambiguous edits silently skipped as
    'could not locate' in one run alone."""
    path = WIKI_ROOT / rel_path
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    candidates = []
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
        candidates.append((i, raw_line, stripped, m.group(2)))

    if not candidates:
        return None
    if len(candidates) == 1:
        i, raw_line, _, _ = candidates[0]
        return i, raw_line

    matches = [(i, raw_line) for i, raw_line, stripped, year in candidates
               if cc._same_paper(cc._title_words(stripped, year), cluster_title_words)]
    if len(matches) == 1:
        return matches[0]
    return None


def apply_change(rel_path: str, key: str, new_doi: str, cluster_title_words: set) -> bool:
    """Rewrites just the DOI on the matching citation line — both the
    `doi:X` link-text form and the `https://doi.org/X` URL form,
    independently, so a line carrying both isn't corrupted by a naive
    single string-replace. If the line has no DOI at all yet, appends
    one. Returns whether a line was found and changed."""
    path = WIKI_ROOT / rel_path
    located = _locate_citation_line(rel_path, key, cluster_title_words)
    if located is None:
        return False
    i, raw_line = located
    stripped = raw_line.strip()

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

    if new_line == raw_line:
        return False  # matched the line but nothing actually needed changing
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    lines[i] = new_line
    path.write_text("".join(lines), encoding="utf-8")
    return True


def _format_section(resolutions: list, heading: str) -> list:
    auto_fixed = [r for r in resolutions if r["status"] == "auto_fixed"]
    needs_human = [r for r in resolutions if r["status"] == "needs_human"]
    total_changes = sum(len(r["changes"]) for r in auto_fixed)

    lines = [
        f"## {heading}", "",
        f"{len(resolutions)} examined: {len(auto_fixed)} auto-resolved "
        f"({total_changes} page edit(s)), {len(needs_human)} need human judgment.\n",
    ]

    if auto_fixed:
        lines.append("### Auto-resolved\n")
        for r in auto_fixed:
            if not r["changes"]:
                continue  # every page already agreed on the canonical DOI, nothing to do
            lines.append(f"- **{r['key']}** -> `{r['canonical_doi']}` ({r['via']}) "
                          f"— \"{r['canonical_title']}\"")
            for c in r["changes"]:
                lines.append(f"  - {c['file']}: {c['old_doi'] or '(no DOI)'} -> {r['canonical_doi']}")

    if needs_human:
        lines.append("\n### Needs human judgment\n")
        for r in needs_human:
            lines.append(f"- **{r['key']}**: {r['reason']}")

    return lines


def format_report(conflict_resolutions: list, standalone_resolutions: list = ()) -> str:
    lines = _format_section(conflict_resolutions, "Multi-page conflicts")
    if standalone_resolutions:
        lines.append("")
        lines.extend(_format_section(standalone_resolutions, "Single-citation DOI problems "
                                                              "(every page agreed, but the DOI was wrong)"))
    return "\n".join(lines)


def write_needs_human_snapshot(conflict_resolutions: list, standalone_resolutions: list) -> None:
    """Persists the needs_human entries from both categories as JSON, so
    the Wiki Health dashboard (health_report.py, via
    wiki_health_check.py's write_dashboard_page) can display and link to
    them without re-running this whole (slow — hundreds of live,
    uncached Crossref search calls) analysis on every page load or after
    every enrichment batch. Only meaningful for a full, unscoped run —
    main() skips this when --key or --debug-key narrowed the analysis to
    one cluster, since a partial snapshot would silently hide everything
    not covered by that run."""
    entries = []
    for r in list(conflict_resolutions) + list(standalone_resolutions):
        if r["status"] != "needs_human":
            continue
        entries.append({"key": r["key"], "reason": r["reason"], "files": r.get("files", [])})
    snapshot = {"generated_at": datetime.now(timezone.utc).isoformat(), "entries": entries}
    NEEDS_HUMAN_SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    NEEDS_HUMAN_SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")


def _apply_resolutions(resolutions: list) -> None:
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
    print(f"Applied {applied} page edit(s); {failed} could not be located and were left unchanged.",
          file=sys.stderr)


def debug_key(key: str) -> None:
    """Fast, read-only diagnostic for one author-year key's single-citation
    DOI status: classifies every DOI it's cited with, and — for anything
    not verified — runs the search fallback with full diagnostics (the
    exact query sent, every raw Crossref candidate, and its word-overlap
    fraction against the 0.35 threshold). Bypasses scanning the rest of
    the wiki entirely, so this stays fast regardless of wiki size —
    re-running the FULL standalone pass just to reach one key would mean
    waiting through however many live, uncached search calls sort before
    it alphabetically."""
    by_key = cc.load_all_citations()
    entries = by_key.get(key)
    if not entries:
        print(f"No citations found with key {key!r}.", file=sys.stderr)
        sys.exit(1)

    by_doi: dict[str, list] = {}
    no_doi = []
    for e in entries:
        if e["doi"]:
            by_doi.setdefault(e["doi"], []).append(e)
        else:
            no_doi.append(e)

    print(f"{key}: {len(entries)} citation(s) across {len({e['source'] for e in entries})} page(s), "
          f"{len(by_doi)} distinct DOI(s), {len(no_doi)} with no DOI at all.\n")

    for doi, affected in sorted(by_doi.items()):
        cluster_title_words = max((e["title_words"] for e in affected), key=len)
        classification = classify_doi(doi, cluster_title_words,
                                      _cited_title_text(key, affected, cluster_title_words))
        title_note = f' — Crossref title: "{classification["title"]}"' if classification.get("title") else ""
        print(f"DOI {doi}: {classification['status']}{title_note}")
        print(f"  cited on: {', '.join(e['source'] for e in affected)}")
        if classification["status"] != "verified":
            found = _search_fallback(key, affected, cluster_title_words, debug=True)
            if found:
                print(f"  [debug] VERDICT: would fix to {found[0]!r} (\"{found[1]}\")")
            else:
                print("  [debug] VERDICT: no candidate cleared the threshold — needs human judgment")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="Write fixes to disk (default: dry-run report only)")
    parser.add_argument("--key", default=None, help="Only process this one conflict cluster key (e.g. chi-2014) "
                                                      "— skips the single-citation DOI pass entirely")
    parser.add_argument("--debug", action="store_true",
                         help="With --key, print full search-fallback diagnostics for that one cluster")
    parser.add_argument("--debug-key", default=None,
                         help="Fast, read-only diagnostic for one author-year key's single-citation DOI "
                              "status (the exact search query, every raw Crossref candidate, and its "
                              "word-overlap score) — bypasses the full conflict/standalone scan entirely, "
                              "so it's quick regardless of wiki size. Ignores every other flag.")
    parser.add_argument("--out", default=None, help="Write the report to this path instead of stdout")
    parser.add_argument("--skip-standalone", action="store_true",
                         help="Only process multi-page conflict clusters; skip the single-citation DOI pass "
                              "(every page agrees on a DOI, but the DOI itself is wrong)")
    args = parser.parse_args()

    if args.debug_key:
        debug_key(args.debug_key)
        return

    conflicts = cc.find_conflicts(cc.load_all_citations())
    if args.key:
        conflicts = [c for c in conflicts if c["key"] == args.key]
        if not conflicts:
            print(f"No conflict cluster with key {args.key!r}.", file=sys.stderr)
            sys.exit(1)

    conflict_resolutions = []
    for i, conflict in enumerate(conflicts, 1):
        print(f"[{i}/{len(conflicts)}] resolving conflict {conflict['key']}...", file=sys.stderr)
        conflict_resolutions.append(resolve_cluster(conflict, debug=args.debug and conflict["key"] == args.key))

    if args.apply:
        _apply_resolutions(conflict_resolutions)

    standalone_resolutions = []
    if not args.skip_standalone and not args.key:
        # Re-read from disk so this reflects any conflict fixes just
        # applied above, rather than resolving against a stale, pre-fix
        # snapshot that would still show the old (already-fixed) DOI.
        by_key = cc.load_all_citations()
        conflict_keys = {c["key"] for c in conflicts}
        print("Checking single-citation DOI problems (every page agrees, but the DOI is wrong)...",
              file=sys.stderr)
        standalone_resolutions = resolve_standalone_issues(by_key, conflict_keys)
        if args.apply:
            _apply_resolutions(standalone_resolutions)

    if not args.key:
        write_needs_human_snapshot(conflict_resolutions, standalone_resolutions)

    report = format_report(conflict_resolutions, standalone_resolutions)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote report to {args.out}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
