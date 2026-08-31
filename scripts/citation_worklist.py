#!/usr/bin/env python3
"""
citation_worklist.py — what a person should look at next, ranked.

The four checks each report their own defect in its own flat list, which is
fine for a machine and useless for a human deciding where an hour goes: 81
conflicts, 10 collisions, 9 metadata divergences, 98 invented titles, 15
variant families, and no way to see that several of those lines are the same
source. This collapses all of them onto the author-year key, ranks by how
many citations ride on it, and says what is already known — so the top of the
list is the source whose resolution fixes the most pages.

It also surfaces the corpus's largest blind spot, which none of the checks
can see at all. 2,493 citations across 1,232 keys carry no DOI and no journal
metadata: they are books, Crossref has nothing to say about them, and nothing
verifies that the title, publisher or edition on the page is real. Those are
ranked separately, because the work is different — a book needs a person and
a publisher page, not a lookup.

Keys already settled in sources/authorities.ndjson drop out, so the list
shrinks as you work.

    python3 scripts/citation_worklist.py                # top of both lists
    python3 scripts/citation_worklist.py --books        # only the book backlog
    python3 scripts/citation_worklist.py --limit 40
    python3 scripts/citation_worklist.py --key dweck-2006   # everything on one source
"""

import argparse
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import authorities as au
import check_citations as cc

WIKI_ROOT = Path(__file__).parent.parent


def build(by_key: dict) -> tuple[dict, dict]:
    """({key: {"cites", "pages", "flags"}} for flagged keys, same for books)."""
    by_doi = cc.load_by_doi(by_key)
    doi_key = {}
    for k, entries in by_key.items():
        for e in entries:
            if e["doi"]:
                doi_key.setdefault(e["doi"], k)

    flags = defaultdict(set)
    for c in cc.find_conflicts(by_key):
        if len(c["dois"]) > 1:
            flags[c["key"]].add(f"{len(c['dois'])} different DOIs for one paper")
        else:
            # find_conflicts also fires when ONE DOI is agreed and other pages
            # simply omit it. Saying "1 DOIs for one paper" reads as a defect
            # in the DOI; the actual work is filling the gaps — and only after
            # Crossref confirms it, since bandura-1977 has exactly this shape
            # with one unverified assertion and 67 omissions.
            missing = sum(1 for e in c["entries"] if not e["doi"])
            flags[c["key"]].add(f"one asserted DOI, {missing} citation(s) omit it")
    for f in cc.find_doi_variant_families(by_key):
        flags[f["key"]].add(f"{len(f['members'])} near-identical DOI variants "
                            f"(at least {len(f['members']) - 1} invented)")
    for c in cc.find_doi_collisions(by_doi):
        k = doi_key.get(c["doi"])
        if k:
            flags[k].add("one DOI shared with a different paper")
    for r in cc.find_metadata_divergence(by_doi):
        if r["severity"] == "conflict" and doi_key.get(r["doi"]):
            flags[doi_key[r["doi"]]].add("citations disagree on journal/volume/pages")
    for r in cc.find_title_divergence(by_doi):
        if r["severity"] == "conflict" and doi_key.get(r["doi"]):
            flags[doi_key[r["doi"]]].add("citations disagree on the title")

    flagged, books = {}, {}
    for k, entries in by_key.items():
        rec = {"cites": len(entries),
               "pages": sorted({e["source"] for e in entries}),
               "flags": sorted(flags.get(k, ()))}
        if rec["flags"]:
            flagged[k] = rec
        elif not any(e["doi"] for e in entries) and not any(e.get("meta") for e in entries):
            # No DOI and no journal string anywhere: a book, and invisible to
            # every check in check_citations.py — all five need two variants
            # of something to compare, and there is nothing here to compare.
            books[k] = rec
    return flagged, books


def show(title: str, items: dict, limit: int, note: str = "") -> None:
    if not items:
        print(f"{title}: nothing outstanding.\n")
        return
    total = sum(v["cites"] for v in items.values())
    print(f"{title}: {len(items)} source(s), {total} citation(s).")
    if note:
        print(f"  {note}")
    print()
    for k, v in sorted(items.items(), key=lambda kv: (-kv[1]["cites"], kv[0]))[:limit]:
        print(f"  {v['cites']:4} cites  {len(v['pages']):3} pages   {k}")
        for f in v["flags"]:
            print(f"                          - {f}")
    if len(items) > limit:
        print(f"\n  ... and {len(items) - limit} more (--limit to see further).")
    print()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--books", action="store_true", help="only the unverifiable-book backlog")
    ap.add_argument("--flagged", action="store_true", help="only the machine-flagged sources")
    ap.add_argument("--key", help="show every page citing one source, and how it is cited")
    args = ap.parse_args()

    by_key = cc.load_all_citations()
    settled = au.load_authorities()

    if args.key:
        entries = by_key.get(args.key)
        if not entries:
            print(f"No citations found for {args.key!r}.")
            return
        if args.key in settled:
            print(f"Already recorded as an authority by "
                  f"{settled[args.key]['verified']['by']} on "
                  f"{settled[args.key]['verified']['at']}.\n")
        for e in sorted(entries, key=lambda e: (e["doi"] or "", e["source"])):
            print(f"  {e['source']}")
            print(f"      {e['line'][:150]}")
        print(f"\n{len(entries)} citation(s) across "
              f"{len({e['source'] for e in entries})} page(s).")
        return

    flagged, books = build(by_key)
    for k in settled:
        flagged.pop(k, None)
        books.pop(k, None)
    if settled:
        print(f"{len(settled)} source(s) already settled in "
              f"sources/authorities.ndjson and excluded below.\n")

    if not args.books:
        show("Machine-flagged — a registry lookup or a judgement call", flagged, args.limit,
             "Resolve with scripts/resolve_citation_metadata.py where Crossref can settle "
             "it;\n  record what you establish by hand with scripts/log_authority.py.")
    if not args.flagged:
        show("Unverifiable by any check — no DOI, no journal metadata (books)", books,
             args.limit,
             "Nothing has ever checked these. Each needs a person and a publisher page.\n"
             "  Record each verdict with scripts/log_authority.py so it sticks.")


if __name__ == "__main__":
    main()
