#!/usr/bin/env python3
"""
dedupe_preprints.py — an arXiv preprint and its published version are one study (maintainer, 2026-11-16).

The arXiv universe holds preprints of articles the wiki may already have from their published
version (through ERIC, PMC, a journal list or a curated hub), and the published version may arrive
later the same way. Reading both writes the same study twice: two sources, two sets of claim pages,
and a study counted twice in every roll-up. This finds the overlap two ways:

  by DOI    the arXiv snapshot's own published DOI for the preprint (eval/screening/<universe>.ndjson,
            `doi`), cited on a page another source wrote
  by title  a non-arXiv source in the manifest whose title is the preprint's (85% of significant words
            shared both ways, and check_citations.titles_align)

and acts on it:

  --check   report, write nothing
  --apply   a preprint not yet read whose published version is in is recorded in the manifest as
            rejected, `already-covered` (INCLUSION.md E4), so the sweep never reads it; and the
            preprints already read whose published version is in are listed, with their claim pages
            and the published version's claim pages, in eval/runs/preprint-dups.json for the
            triage to resolve (point the citations at one DOI, then judge the claim pairs with
            judge_claim_merges.py --pairs).

    python3 scripts/sweep/dedupe_preprints.py --check
    python3 scripts/sweep/dedupe_preprints.py --apply
"""
import argparse
import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402
from check_citations import titles_align  # noqa: E402

UNIVERSE = "arxiv-education-research"
CONTENT = ("claims", "principles", "patterns", "elements", "strategies", "designs", "products", "theories",
           "learner-variables", "research-methods", "methods", "processes")
DOI_RE = re.compile(r"doi\.org/(10\.\d{4,9}/[^\s)\"<>\]]+)", re.I)
OUT = WIKI_ROOT / "eval" / "runs" / "preprint-dups.json"


def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def words(s):
    return {w for w in re.findall(r"[a-z0-9]+", fold(s)) if len(w) > 3}


def cited_dois():
    out = collections.defaultdict(set)
    for d in CONTENT:
        for f in (WIKI_ROOT / d).glob("*.md"):
            for m in DOI_RE.findall(f.read_text(encoding="utf-8", errors="ignore")):
                out[m.lower().rstrip(".,;")].add(f"{d}/{f.name}")
    return out


def find():
    latest = {}
    for r in okf_lib.load_manifest():
        latest[r["id"]] = r
    own = {i: set(r.get("pages") or []) for i, r in latest.items() if r.get("status") == "ingested"}
    others = [r for r in latest.values() if not r["id"].startswith("arxiv-") and r.get("status") == "ingested"]
    index = collections.defaultdict(list)
    for r in others:
        for w in words(r["title"]):
            index[w].append(r)

    def same_title(title):
        ws = words(title)
        if len(ws) < 3:
            return None   # a two-word title matches too much to be evidence of anything
        seen = {}
        for w in ws:
            for r in index.get(w, []):
                seen[id(r)] = r
        for r in seen.values():
            b = words(r["title"])
            if b and len(ws & b) / max(len(ws), len(b)) >= 0.85 and titles_align(title, r["title"]):
                return r
        return None

    cited = cited_dois()
    lines = (WIKI_ROOT / "eval" / "screening" / f"{UNIVERSE}.ndjson").read_text(encoding="utf-8").splitlines()
    unread, read = [], []
    for m in (json.loads(l) for l in lines[1:] if l.strip()):
        r = latest.get(m["id"])
        status = r.get("status") if r else None
        if status == "rejected" and okf_lib.manifest_rejection_is_final(r):
            continue
        doi = (m.get("doi") or "").lower() or None
        mine = own.get(m["id"], set())
        by_doi = sorted(p for p in cited.get(doi, ()) if p not in mine) if doi else []
        other = same_title(m["title"])
        if not (by_doi or other):
            continue
        rec = {"id": m["id"], "title": m["title"], "published_doi": doi, "pages_citing_published_doi": by_doi,
               "published_source": other["id"] if other else None,
               "published_source_pages": sorted(other.get("pages") or []) if other else [],
               "preprint_pages": sorted(mine)}
        (read if status == "ingested" else unread).append(rec)
    return unread, read


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    unread, read = find()
    print(f"{len(unread)} preprint(s) not yet read whose published version is in the wiki")
    print(f"{len(read)} preprint(s) already read whose published version is in the wiki")
    for x in unread[:10]:
        print(f"  skip  {x['id']}  {x['title'][:70]}  <- {x['published_source'] or x['pages_citing_published_doi'][0]}")
    for x in read[:10]:
        print(f"  dup   {x['id']}  {x['title'][:70]}")
    if not a.apply:
        return
    for x in unread:
        via = (f"its published version is ingested as {x['published_source']}" if x["published_source"]
               else f"its published version (doi:{x['published_doi']}) is cited on {x['pages_citing_published_doi'][0]}")
        okf_lib.append_manifest_entry(x["id"], x["title"], "rejected", doi=x["published_doi"],
                                      reason_code="already-covered",
                                      reason=f"arXiv preprint of an article already in the wiki: {via}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(read, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"recorded {len(unread)} as already-covered; wrote {len(read)} to {OUT.relative_to(WIKI_ROOT)}")


if __name__ == "__main__":
    main()
