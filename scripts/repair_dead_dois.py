#!/usr/bin/env python3
"""
repair_dead_dois.py — a DOI on a page that no registry knows: find the real one, or take it off.

check_source_validity.py --retractions found 2026-10-25 that a few hundred of the DOIs the wiki
cites are registered at neither Crossref nor DataCite, and doi.org returns 404 for them: the
model that wrote the page invented them (10.3102/0034654316685135 on universal-design-for-
learning, 10.1037/0033-295x.106.1.60 on transfer-tasks). An invented DOI is worse than none,
because it reads as verified (CLAUDE.md).

For each line carrying a dead DOI, the DOI is taken out and find_missing_dois.decide() asks
Crossref's bibliographic search for the citation; a candidate is accepted only when its title,
first author, year, kind of work and journal agree with the citation, the same rule that tool
uses everywhere. Otherwise the citation stays without a DOI, which says "not established" and
nothing more. A link whose only target was the dead DOI keeps its text and loses the link.

Every decision is written to eval/source-validity/dead-dois.ndjson before any page changes.

    python3 scripts/repair_dead_dois.py --check     # decide, print, write nothing to pages
    python3 scripts/repair_dead_dois.py --apply
"""
import argparse
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import check_source_validity as csv_  # noqa: E402
import find_missing_dois as fmd  # noqa: E402

LOG = WIKI_ROOT / "eval" / "source-validity" / "dead-dois.ndjson"
# A dead DOI can be the prefix of a live one (10.1001/jama.2013.2820 and ...282057, or
# ...2010.01564 and ...01564.x): every match must end where the DOI ends.
END = r"(?![A-Za-z0-9_\-/:;<>(]|\.[A-Za-z0-9])"


def has(line: str, doi: str) -> bool:
    return re.search(re.escape(doi) + END, line, re.I) is not None


def dead_dois() -> dict:
    """dead doi -> pages, from the last --retractions run's lookups (registry 404 both places)."""
    cache = csv_._lookups()
    return {d: p for d, p in csv_.cited_dois().items() if (cache.get(d) or {}).get("status") == "not-found"}


def strip(line: str, doi: str) -> str:
    e = re.escape(doi) + END
    url = rf"https?://(?:dx\.)?doi\.org/{e}"
    s = line
    s = re.sub(rf"\s*\[(?:doi:\s*)?{e}\]\({url}\)", "", s, flags=re.I)          # [doi:X](url)
    s = re.sub(rf"\s*\[{url}\]\({url}\)", "", s, flags=re.I)                     # [url](url)
    s = re.sub(rf"\[([^\]]+)\]\({url}\)", r"\1", s, flags=re.I)                  # [text](url) -> text
    s = re.sub(rf"\s*<?{url}>?", "", s, flags=re.I)                              # bare url
    s = re.sub(rf"\s*\bdoi:\s*{e}", "", s, flags=re.I)                           # doi:X
    return s.rstrip()


def repair_text(text: str, doi: str, new: "str | None") -> str:
    """Replace or remove one dead DOI everywhere in a page."""
    out = []
    for line in text.split("\n"):
        if not has(line, doi):
            out.append(line)
            continue
        m = re.match(r'^(\s*resource:\s*)"?https?://(?:dx\.)?doi\.org/', line, re.I)
        if m:
            if new:
                out.append(f'{m.group(1)}"https://doi.org/{new}"')
            continue                                   # no resource is "not established"
        if new:
            out.append(re.sub(re.escape(doi) + END, new, line, flags=re.I))
        else:
            out.append(strip(line, doi))
    return "\n".join(out)


def arxiv_doi(pages, line: str):
    """An arXiv source's own DataCite DOI (10.48550/arXiv.<id>), when the manifest says the
    page came from arXiv and DataCite's title is the cited one. Found 2026-10-25: a 2026
    conference paper cited with an ACM DOI not yet registered is on DataCite under arXiv's."""
    ids = set()
    for r in csv_.manifest_sources():
        if r["id"].startswith("arxiv-") and set(r.get("pages") or []) & set(pages):
            ids.add(r["id"][len("arxiv-"):])
    for aid in sorted(ids):
        rec = csv_.lookup(f"10.48550/arxiv.{aid}", csv_._lookups())
        if rec.get("status") == "datacite" and rec.get("title") and csv_.ref_matches(line, rec["title"]):
            return rec["doi"]
    return None


def citation_line(text: str, doi: str) -> "str | None":
    """The citation the DOI is attached to: a line with an author-year and the DOI."""
    for line in text.split("\n"):
        if has(line, doi) and re.search(r"\((1[89]\d\d|20\d\d)[a-z]?\)", line) and "resource:" not in line:
            return line
    for line in text.split("\n"):
        if has(line, doi) and re.search(r"title:\s*\"", line):
            return re.sub(r'^\s*title:\s*"|"\s*$', "", line)
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    dead = dead_dois()
    print(f"{len(dead)} dead DOIs on {len({p for ps in dead.values() for p in ps})} pages", file=sys.stderr)
    decisions = []
    for doi, pages in sorted(dead.items()):
        new, why, line = None, "no citation line with an author-year found", None
        for page in sorted(pages):
            line = citation_line((WIKI_ROOT / page).read_text(encoding="utf-8"), doi)
            if line:
                d = fmd.decide(page, strip(line, doi))
                new, why = d.get("doi"), d["why"]
                if not new:
                    a = arxiv_doi(pages, line)
                    if a:
                        new, why = a, "the source's arXiv DOI on DataCite, whose title the citation carries"
                break
        if new == doi:
            new, why = None, "search returned the same unregistered DOI"
        decisions.append({"doi": doi, "new": new, "why": why, "citation": (line or "")[:300], "pages": sorted(pages)})
        print(f"{doi} -> {new or '(removed)'}  {why}")
    if a.apply:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a", encoding="utf-8") as fh:
            for d in decisions:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        for d in decisions:
            for page in d["pages"]:
                p = WIKI_ROOT / page
                t = p.read_text(encoding="utf-8")
                n = repair_text(t, d["doi"], d["new"])
                if n != t:
                    p.write_text(n, encoding="utf-8")
    found = sum(1 for d in decisions if d["new"])
    print(f"{found} replaced with a verified DOI, {len(decisions) - found} removed", file=sys.stderr)


if __name__ == "__main__":
    main()
