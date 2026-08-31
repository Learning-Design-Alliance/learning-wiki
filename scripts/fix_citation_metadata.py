#!/usr/bin/env python3
"""
fix_citation_metadata.py — Repair fabricated journal/volume/page metadata.

The enrichment pipeline reliably copies a paper's *title* and *DOI* and then
invents the journal around them. Graham & Perin (2007) is cited 101 times in
this wiki under one DOI with seven different journal/volume/page strings:
92 as Journal of Educational Psychology 99(3) 445-476, and single pages as
Psychological Bulletin, Psychological Science, Reading Research Quarterly and
three more.

Every one of those pages passes every other check. The DOI resolves, so
nothing downstream questions the volume and page numbers wrapped around it —
which makes this worse than a wrong DOI. A wrong DOI at least resolves to
something a reader can check; a correct DOI wearing an invented journal name
validates cleanly and reads as precision. Anyone citing this wiki would
propagate a reference that does not exist.

**The repair is arithmetic, not a vote.** A minority variant is rewritten
only when the DOI's own suffix spells out the majority's volume, issue and
first page — 10.1037/0022-0663.99.3.445 *is* ISSN 0022-0663, volume 99,
issue 3, page 445 — and does not spell out the minority's. Where the DOI is
opaque about it (10.1207/s1532690xci0201_3 packs the volume into a publisher
token), nothing is touched and the case is reported for a Crossref pass.
That is 32 citations repairable here and 317 left for the network, and the
split is deliberate: guessing which of two journals is right is the same
error as guessing a DOI, and just as invisible afterwards.

Naming variants ("PNAS" vs "Proceedings of the National Academy of
Sciences", same volume and page) are left alone — that is house style, not a
defect.

Usage:
    python3 scripts/fix_citation_metadata.py --check
    python3 scripts/fix_citation_metadata.py --apply
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc

WIKI_ROOT = Path(__file__).parent.parent


def canonical_span(doi: str, entries: list) -> str | None:
    """The majority's exact journal/volume/page text, read off a real page."""
    for e in entries:
        path = WIKI_ROOT / e["source"]
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if doi.lower() in line.lower():
                span = cc.source_meta_span(line)
                if span and cc.parse_source_meta(line) == e["meta"]:
                    return span[2]
    return None


def plan(results: list[dict], consensus: dict | None = None) -> tuple[list, list]:
    """(repairs, deferred) — repairs are DOI-proven, deferred need Crossref."""
    repairs, deferred = [], []
    for r in results:
        if r["severity"] != "conflict":
            continue
        # Never repair toward a leader the DOI itself contradicts. This is the
        # inversion the whole check exists to catch: 32 pages cite
        # 10.17763/haer.81.4... as Journal of Educational Research 104(6), and
        # the DOI plainly says Harvard Educational Review volume 81 issue 4.
        # Rewriting the minority to match that majority would convert the last
        # correct citations into copies of the fabrication.
        if consensus is not None and cc.leading_contradicted(r, consensus):
            deferred.append(r)
            continue
        if not r["majority_corroborated"]:
            deferred.append(r)
            continue
        canon = canonical_span(r["doi"], r["variants"][0][1])
        if canon is None:
            deferred.append(r)
            continue
        for meta, es in r["variants"][1:]:
            # Never rewrite a variant the DOI also vouches for — if both sides
            # are corroborated the DOI is on two real papers, which is
            # find_doi_collisions' problem and not something to paper over.
            if cc.doi_corroborates(r["doi"], *meta[1:]):
                deferred.append(r)
                continue
            for e in es:
                # The title decides whether this is one paper described two
                # ways, or two papers sharing a DOI. Same title -> the journal
                # around it was invented and the DOI is the reliable part, so
                # repair. Different title -> the DOI itself is on the wrong
                # paper, and rewriting the journal would turn a correct
                # citation with a bad DOI into a wholly wrong citation. That
                # case belongs to find_doi_collisions and a human.
                if not any(cc._same_paper(e["title_words"], m["title_words"])
                           for m in r["variants"][0][1]):
                    deferred.append(r)
                    continue
                repairs.append({"doi": r["doi"], "file": e["source"],
                                "was": meta, "canonical": canon})
    return repairs, deferred


def apply_repair(rep: dict) -> bool:
    path = WIKI_ROOT / rep["file"]
    text = path.read_text(encoding="utf-8")
    out, changed = [], False
    for line in text.splitlines(keepends=True):
        if rep["doi"].lower() in line.lower() and cc.parse_source_meta(line) == rep["was"]:
            s, e, _ = cc.source_meta_span(line)
            line = line[:s] + rep["canonical"] + line[e:]
            changed = True
        out.append(line)
    if changed:
        new = "".join(out)
        # The DOI is the anchor the repair is keyed on; if a rewrite ever
        # dropped it the page would silently lose its only verifiable link.
        assert rep["doi"].lower() in new.lower(), f"repair dropped the DOI in {rep['file']}"
        path.write_text(new, encoding="utf-8")
    return changed


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    by_doi = cc.load_by_doi(cc.load_all_citations())
    results = cc.find_metadata_divergence(by_doi)
    repairs, deferred = plan(results, consensus=cc.token_consensus(by_doi))

    for rep in repairs:
        j, v, i, pg = rep["was"]
        print(f"  {rep['file']}")
        print(f"      {j} {v}({i}), {pg}  ->  {rep['canonical']}")
        if args.apply:
            apply_repair(rep)

    print(f"\n{'Repaired' if args.apply else 'Would repair'} {len(repairs)} citation(s) "
          f"across {len({r['file'] for r in repairs})} page(s).")
    print(f"{sum(sum(len(e) for _, e in r['variants'][1:]) for r in deferred)} citation(s) "
          f"across {len(deferred)} DOI(s) need Crossref — the DOI does not encode its own "
          f"volume/issue/page, so which journal is right cannot be settled offline.\n"
          f"Run `check_citations.py --metadata` for the list.")


if __name__ == "__main__":
    main()
