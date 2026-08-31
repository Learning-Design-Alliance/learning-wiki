#!/usr/bin/env python3
"""
apply_authorities.py — enforce human-verified authorities on the pages.

Reads sources/authorities.ndjson and reports (or repairs) every citation that
contradicts a verdict a person recorded. Today that means one repair the
authority makes safe and nothing else can:

  strip a DOI from a key recorded as having none.

That is deliberately the only automatic edit. `"doi": null` is a positive
statement by a human that no DOI is registered for the source, so a DOI on
the page is invented and removing it loses nothing. Every other disagreement
— a wrong ISBN, a DOI that differs from the recorded one, a title that does
not match — is *reported* rather than rewritten, because the page might be
citing a different edition, a chapter rather than the book, or the reprint
rather than the original, and only the person who checked the source can say
which. The tooling has been wrong about exactly this kind of "obvious"
correction before: see the Cook-Sather title case in CLAUDE.md.

    python3 scripts/apply_authorities.py --check
    python3 scripts/apply_authorities.py --apply
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import authorities as au
import check_citations as cc
from resolve_citation_metadata import strip_doi_from_line

WIKI_ROOT = Path(__file__).parent.parent


def _is_target(line: str, finding: dict) -> bool:
    """Whether this file line is the citation the finding is about.

    Matching on the DOI alone is not enough, and getting that wrong is how
    this script first stripped a *correct* DOI:
    strategies/positive_behavior_interventions_and_supports.md cites both
    Horner (2005) and Sugai & Horner (2009) with the same
    10.1007/978-0-387-09632-2_13, one wrongly and one rightly. A file-wide
    replace on the DOI removed both. The finding is about one citation, so the
    edit has to be too — anchor on the citation text as well.

    check_citations truncates its stored line at 160 characters, so this
    compares a prefix; that is still specific enough to separate two citations
    that differ in their first words, which is every real case."""
    stem = finding["line"][:120]
    return bool(stem) and line.strip().startswith(stem) \
        and finding["doi"].lower() in line.lower()


def out_of_scope(auth: dict, by_key: dict) -> list[dict]:
    """Citations sharing an authority's key but citing a different work.

    Reported, never acted on. An author-year key is not unique — see
    authorities.covers() — and the fact that one exists is worth saying out
    loud, because APA's own answer (a 2009a / 2009b year suffix) is a page
    edit only a person should make."""
    out = []
    for key, entry in auth.items():
        if not entry.get("title"):
            continue
        for c in by_key.get(key, []):
            if not au.covers(entry, c):
                out.append({"key": key, "source": c["source"], "doi": c["doi"]})
    return out


def findings(auth: dict, by_key: dict) -> list[dict]:
    """One record per citation that disagrees with its key's authority."""
    out = []
    for key, entry in auth.items():
        for c in by_key.get(key, []):
            for why in au.contradictions(entry, c):
                out.append({"key": key, "source": c["source"], "doi": c["doi"],
                            "why": why, "line": c["line"],
                            # Only the no-DOI verdict is auto-repairable; see
                            # the module docstring.
                            "fixable": bool(c["doi"]) and "doi" in entry
                                       and entry["doi"] is None})
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    auth = au.load_authorities()
    if not auth:
        print(f"No authorities recorded yet ({au.AUTHORITIES_PATH.relative_to(WIKI_ROOT)} "
              f"is absent or empty).\nRecord one with scripts/log_authority.py.")
        return
    by_key = cc.load_all_citations()
    results = findings(auth, by_key)
    other = out_of_scope(auth, by_key)
    covered = sum(len(by_key.get(k, [])) for k in auth) - len(other)
    print(f"{len(auth)} authorit(y/ies) recorded, covering {covered} citation(s).")
    if other:
        print(f"\n{len(other)} citation(s) share an authority's author-year key but cite a "
              f"different work, so no authority applies to them. An author-year key is not "
              f"unique; APA's answer is a 2009a/2009b suffix, which is a page edit only you "
              f"should make:")
        for r in other:
            print(f"      {r['key']}  {r['source']}  ({r['doi'] or 'no DOI'})")
    if not results:
        print("\nEvery citation covered by an authority agrees with what was verified.")
        return

    fixable = [r for r in results if r["fixable"]]
    manual = [r for r in results if not r["fixable"]]
    written = set()
    if args.apply and fixable:
        for r in fixable:
            path = WIKI_ROOT / r["source"]
            text = path.read_text(encoding="utf-8")
            new = "".join(strip_doi_from_line(line, r["doi"]) if _is_target(line, r) else line
                          for line in text.splitlines(keepends=True))
            if new != text:
                path.write_text(new, encoding="utf-8")
                written.add(r["source"])

    verb = "Stripped" if args.apply else "Would strip"
    if fixable:
        print(f"\n{verb} {len(fixable)} invented DOI(s) from keys recorded as having none"
              + (f" ({len(written)} page(s) written)." if args.apply else "."))
        for r in fixable:
            print(f"      {r['source']}: {r['doi']}")
        if args.apply and len(written) < len({r["source"] for r in fixable}):
            print("      (pages not listed as written already had nothing to remove)")
    if manual:
        print(f"\n{len(manual)} disagreement(s) a person has to settle — the page may be "
              f"citing a different edition, a chapter, or a reprint, and only you know:")
        for r in manual:
            print(f"      {r['source']}\n          {r['why']}")
    if args.check and fixable:
        print("\nRe-run with --apply to write these.")


if __name__ == "__main__":
    main()
