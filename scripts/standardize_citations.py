#!/usr/bin/env python3
"""
standardize_citations.py — Give every citation of one paper the same DOI.

Two thirds of the wiki's citation conflicts are the same simple shape: many
pages cite a paper with one agreed DOI, and a few cite it with none.
collins-1989 is the clean example — 22 pages carry
10.4324/9781315044408-14 and strategies/on-the-job-training-ojt.md carries
nothing, so the checker reports a conflict that is really just an omission.

**Consensus is not the test, and must not be.** In this corpus the same shape
also covers bandura-1977: 68 citations, of which exactly ONE asserts
10.1037/12256-000 and 67 assert nothing. Filling in the blanks by copying the
majority would be right for collins and would, for bandura, propagate a single
unverified DOI onto 67 pages — which is precisely how a Springer chapter's DOI
came to sit on 69 pages as Bandura (1977) in the first place. The direction of
the majority is the only difference between the two, and it is not a
difference in evidence.

So the DOI is written only where Crossref confirms it resolves to the paper
being cited. That makes the 1-vs-67 case as safe as the 22-vs-1 case: both are
decided by the registry rather than by a vote, and a run during an outage
changes nothing.

Usage:
    python3 scripts/standardize_citations.py --check
    python3 scripts/standardize_citations.py --apply
    python3 scripts/standardize_citations.py --apply --key collins-1989
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc

WIKI_ROOT = Path(__file__).parent.parent

# End of an APA citation line, before any trailing DOI link. The DOI goes
# after the final period of the reference itself.
_TRAILING_WS = re.compile(r"\s*$")


def add_doi_to_line(line: str, doi: str) -> str | None:
    """Append a DOI hyperlink to a citation line, or None if it already has one."""
    if "doi.org" in line.lower() or re.search(r"10\.\d{4,9}/", line):
        return None
    body = _TRAILING_WS.sub("", line)
    if not body:
        return None
    if not body.endswith("."):
        body += "."
    return f"{body} [doi:{doi}](https://doi.org/{doi})\n"


def consensus_sample(have: list[dict]) -> dict:
    """The citation whose title the most pages agree on.

    This used to be have[0] — whichever page sorted first — and the whole
    cluster's verification rode on it. patall-2008 is cited on 22 pages: 21
    give the title as "...A meta-analysis of research findings" and three give
    invented subtitles ("...of research on choice", "...of research on giving
    choices"). classify_doi compares that one sample against Crossref and
    rejects a subtitle that diverges, so had the arbitrary first page been one
    of the three, all 22 citations would have been classified wrong_paper, the
    fill would have been refused, and the report would have told the reader
    that a correct DOI "resolves to the wrong paper".

    Voting on the *title* is safe in a way voting on the DOI is not, and the
    difference matters. The DOI still has to resolve, and the registry still
    has to confirm it names this paper — the vote only picks which of several
    spellings of the paper's name is put to Crossref. A majority cannot
    promote an unverified DOI here; it can only avoid handing the check a
    known-corrupted sample."""
    by_title = {}
    for e in have:
        year = e["key"].rsplit("-", 1)[-1]
        by_title.setdefault(_norm(cc._extract_title_text(e["line"], year)), []).append(e)
    return max(by_title.values(), key=len)[0]


def _norm(t: str) -> str:
    return re.sub(r"\s+", " ", (t or "").lower().strip(" .")) 


def candidates(by_key: dict) -> list[dict]:
    """Conflicts that are one agreed DOI plus citations omitting it."""
    out = []
    for c in cc.find_conflicts(by_key):
        dois = {e["doi"] for e in c["entries"] if e["doi"]}
        missing = [e for e in c["entries"] if not e["doi"]]
        if len(dois) == 1 and missing:
            have = [e for e in c["entries"] if e["doi"]]
            out.append({"key": c["key"], "doi": dois.pop(),
                        "missing": missing, "have": have})
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    ap.add_argument("--key", default=None, help="only this author-year key")
    args = ap.parse_args()

    import resolve_doi_conflicts as rdc

    by_key = cc.load_all_citations()
    cands = candidates(by_key)
    if args.key:
        cands = [c for c in cands if c["key"] == args.key]

    print(f"{len(cands)} paper(s) with one agreed DOI and citation(s) omitting it "
          f"({sum(len(c['missing']) for c in cands)} to fill in).\n", file=sys.stderr)

    added = wrong = skipped = 0
    edits: dict[Path, list] = {}

    for c in sorted(cands, key=lambda c: -len(c["missing"])):
        sample = consensus_sample(c["have"])
        year = sample["key"].rsplit("-", 1)[-1]
        cited_title = cc._extract_title_text(sample["line"], year)
        res = rdc.classify_doi(c["doi"], sample["title_words"], cited_title)

        ratio = f"{len(c['have'])} assert / {len(c['missing'])} omit"
        if res["status"] == "verified":
            # Verify each PAGE, not just the cluster. Checking one sample and
            # then writing its DOI onto every page that omits it assumes the
            # omitting pages cite the same work, and in this corpus they very
            # often do not: 30 pages omitting wineburg-2019's DOI give titles
            # like "Lateral reading and the nature of expertise: The studies
            # of civic online reasoning" and "...: Reading rates and college
            # students' use of multiple sources" — one stem, several different
            # papers or several invented subtitles.
            #
            # Filling those wrote a DOI onto a citation of a different work,
            # and resolve_citation_metadata — which checks each page's own
            # title — then stripped every one of them straight back off. A run
            # of both reported 73 fills and 72 removals and changed six lines.
            # Beyond the churn, the order of the two scripts decided the
            # outcome, which is not a property a verification pass may have.
            #
            # classify_doi is the same call, cache-backed, so this costs no
            # extra lookups; it just asks it about the citation being edited.
            filled, mismatched = 0, []
            for e in c["missing"]:
                e_year = e["key"].rsplit("-", 1)[-1]
                e_title = cc._extract_title_text(e["line"], e_year)
                e_res = rdc.classify_doi(c["doi"], e["title_words"], e_title)
                if e_res["status"] != "verified":
                    mismatched.append((e, e_title, e_res["status"]))
                    continue
                edits.setdefault(WIKI_ROOT / e["source"], []).append((e["line"], c["doi"]))
                added += 1
                filled += 1
            print(f"  [verify] {c['key']:22} {ratio:22} {c['doi']}")
            if mismatched:
                skipped += len(mismatched)
                print(f"           {filled} filled; {len(mismatched)} NOT filled — those "
                      f"pages cite a different title under this key:")
                for e, t, st in mismatched[:4]:
                    print(f"             {st:11} {e['source']}")
                    print(f"                         \"{(t or '')[:72]}\"")
                if len(mismatched) > 4:
                    print(f"             ... and {len(mismatched) - 4} more")
        elif res["status"] == "wrong_paper":
            wrong += 1
            print(f"  [WRONG ] {c['key']:22} {ratio:22} {c['doi']}\n"
                  f"           resolves to \"{(res.get('title') or '')[:70]}\" — not written "
                  f"anywhere, and the {len(c['have'])} page(s) asserting it need review")
        else:
            skipped += 1
            print(f"  [skip  ] {c['key']:22} {ratio:22} {c['doi']} ({res['status']})")

    if args.apply and edits:
        for path, items in edits.items():
            text = path.read_text(encoding="utf-8")
            out = []
            for line in text.splitlines(keepends=True):
                for excerpt, doi in items:
                    # entries carry a 160-char excerpt; match on it rather than
                    # on equality so the real (longer) line is the one edited.
                    if line.startswith(excerpt[:80]):
                        new = add_doi_to_line(line, doi)
                        if new:
                            line = new
                        break
                out.append(line)
            path.write_text("".join(out), encoding="utf-8")

    verb = "Added" if args.apply else "Would add"
    print(f"\n{verb} {added} DOI(s) across {len(edits)} page(s).")
    print(f"{wrong} DOI(s) resolve to the wrong paper — nothing written for those; the pages "
          f"already asserting them need review.")
    print(f"{skipped} skipped (lookup failed or not found — an outage is not a verdict).")


if __name__ == "__main__":
    main()
