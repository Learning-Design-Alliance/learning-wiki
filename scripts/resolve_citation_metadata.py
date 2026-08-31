#!/usr/bin/env python3
"""
resolve_citation_metadata.py — Settle citation defects against Crossref.

Three offline checks report defects this cannot fix on its own:

  check_citations.py --metadata    a correct DOI wearing an invented journal,
                                   volume or page range
  check_citations.py --titles      a correct DOI wearing an invented title,
                                   usually a made-up subtitle after the colon
  check_citations.py --collisions  one DOI asserted for two different papers

fix_citation_metadata.py repairs only the subset a DOI settles arithmetically
(its suffix encodes the volume and page). Everything else needs the registry,
because the alternative — believing the majority — is wrong often enough to
matter: 10.17763/haer.81.4... is cited 32 times and never once correctly.

This script asks Crossref and applies what comes back.

WHAT IT WILL DO
  * Correct a journal, volume, issue or page range to the registry's values.
  * Correct a title to the registry's, with --titles.
  * Strip a DOI whose registry title matches no citation of it in the wiki —
    that DOI is on the wrong paper, and per this project's standing rule a
    DOI that resolves to the wrong paper is worse than none, because it reads
    as verified.

WHAT IT WILL NOT DO
  * Invent or search for a replacement DOI. Removing a wrong one is safe;
    choosing a new one is the failure mode that put a Springer chapter's DOI
    on 69 pages as Bandura.
  * Touch anything when the lookup fails. An unreachable Crossref is an
    outage, not a verdict — the same reason classify_doi's "error" is not
    "wrong_paper". A run during an outage changes nothing.
  * Fill in a field Crossref left empty. Books have no volume; some records
    carry no page range. Absent means "the registry did not say", never
    "the wiki is wrong".

Usage:
    python3 scripts/resolve_citation_metadata.py --check          # report only
    python3 scripts/resolve_citation_metadata.py --check --titles
    python3 scripts/resolve_citation_metadata.py --apply
    python3 scripts/resolve_citation_metadata.py --apply --limit 20
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc

WIKI_ROOT = Path(__file__).parent.parent


def _norm_journal(s: str) -> str:
    s = (s or "").lower().strip()
    for lead in ("the ",):
        if s.startswith(lead):
            s = s[len(lead):]
    return " ".join(s.split())


def _unescape_record(record: dict) -> dict:
    """Unescape a record's text fields, whether it came fresh or from cache.

    doi_resolver unescapes at fetch time, but the cache holds entries written
    before it did — so a cached "Youth &amp; Society" survived that fix and the
    run still proposed writing the entity onto the page. Unescaping on read
    covers both, and is idempotent: journal names and paper titles do not
    legitimately contain HTML entities."""
    import html
    if not isinstance(record, dict):
        return record
    return {k: (html.unescape(v) if isinstance(v, str) else v) for k, v in record.items()}


def decide(cited: tuple, record: dict, cited_title: str = "") -> dict:
    """Compare one citation against a Crossref record. Pure — no I/O.

    `cited` is (journal, volume, issue, first_page); `record` is a
    doi_resolver.resolve_doi() result. Returns {"action", "fields", "why"}
    where action is one of:

      "none"        the registry agrees, or said nothing about these fields
      "fix_meta"    the registry disagrees on a field it actually stated
      "fix_title"   the title disagrees but journal/volume/page corroborate
                    the DOI, so the title is what was invented
      "strip_doi"   the registry's title matches nothing this page claims AND
                    the other coordinates do not corroborate it either, so the
                    DOI belongs to a different paper
      "not_found"   Crossref has no record of the DOI — reported, never acted
                    on, since Crossref does not index every registrar
      "skip"        the lookup failed; an outage tells us nothing

    Kept separate from the file walking so the decision can be tested
    without a network, which matters: this is the part that decides whether
    to rewrite hundreds of citations."""
    record = _unescape_record(record)
    if not record or record.get("status") == "error":
        return {"action": "skip", "fields": {}, "why": "lookup failed"}
    if not record.get("resolved"):
        # Crossref 404. Evidence, but not proof: Crossref only indexes DOIs
        # registered through Crossref, so a DataCite dataset DOI or an mEDRA
        # or JaLC registration is legitimately absent. Never stripped on that
        # basis alone — reported instead, and ranked by whether the prefix's
        # other DOIs resolve (see notfound_report).
        return {"action": "not_found", "fields": {},
                "why": "no Crossref record for this DOI"}

    reg_title = record.get("title") or ""
    if reg_title and cited_title:
        # The title test comes first and gates everything else. If the DOI is
        # on a different paper, "correcting" its journal to the registry's
        # would rewrite the citation into a work the page never meant.
        same = cc._same_paper(cc._words_from_text(cited_title),
                              cc._words_from_text(reg_title))
        if same and not cc.titles_align(cited_title, reg_title):
            same = False
        if not same:
            # A title mismatch alone does not tell you WHICH side is wrong.
            # strategies/student-shadowing... cites Cook-Sather (2006) "Sound,
            # presence, and silence in education", Curriculum Inquiry 36(4)
            # 359 — and the registry says the title is "Sound, Presence, and
            # Power: 'Student Voice' in Educational Research and Reform" at
            # exactly that journal, volume, issue and page. The DOI is right
            # and the TITLE is the fabrication; stripping would delete the good
            # data and keep the invented text.
            #
            # So weigh the other coordinates. Journal, volume and first page
            # are independent of the title, and two of them agreeing with the
            # registry is far better evidence of the same work than a subtitle
            # the model is known to invent.
            journal, vol, issue, page = cited
            j_ok = bool(record.get("journal")) and _norm_journal(journal) == _norm_journal(record["journal"])
            v_ok = bool(record.get("volume")) and str(vol) == str(record["volume"])
            p_ok = bool(record.get("first_page")) and str(page) == str(record["first_page"])
            # All three, and the first page is not negotiable.
            #
            # A 2-of-3 rule looked reasonable and was badly wrong in practice,
            # because the pair that satisfies it is almost always journal +
            # volume — and two articles sharing a journal and volume is the
            # normal case, not evidence. It proposed rewriting "Reading aloud
            # improves memory: A production effect" to "Why are background
            # telephone conversations distracting?" purely because both sit in
            # the same volume of the same journal.
            #
            # The first page is what identifies an article within a volume. In
            # every genuine case here it matched (Cook-Sather 3/3, Okonofua &
            # Eberhardt 3/3) and in every false one it did not.
            if j_ok and v_ok and p_ok:
                # Do not trade a fuller title for a truncated registry record.
                # Crossref gives Okonofua & Eberhardt (2015) as just "Two
                # Strikes", while the page carries "Two strikes: Race and the
                # disciplining of young students" — the real published title.
                # Rewriting there deletes a correct subtitle in the name of
                # matching the registry, which is the opposite of the point.
                #
                # A registry title that is a PREFIX of the cited one is a
                # shorter rendering of the same title, not a different one; a
                # registry title that diverges (Cook-Sather's "Sound, Presence,
                # and Power" against the page's "silence in education") is a
                # genuine correction.
                c_norm, r_norm = cc._norm_title(cited_title), cc._norm_title(reg_title)
                if c_norm.startswith(r_norm):
                    return {"action": "none", "fields": {},
                            "why": "registry title is a truncation of the fuller one "
                                   "already on the page"}
                return {"action": "fix_title", "fields": {"title": reg_title},
                        "why": f"title is wrong, not the DOI (journal, volume AND first page "
                               f"all match the registry): \"{cited_title[:45]}\" -> "
                               f"\"{reg_title[:45]}\""}
            return {"action": "strip_doi", "fields": {},
                    "why": f"DOI resolves to \"{reg_title[:70]}\", not the cited work"}

    journal, vol, issue, page = cited
    fields, why = {}, []
    for name, mine, theirs in (
        ("journal", journal, record.get("journal")),
        ("volume", vol, record.get("volume")),
        ("issue", issue, record.get("issue")),
        ("first_page", page, record.get("first_page")),
    ):
        if not theirs:
            continue                      # registry said nothing — leave it alone
        a = _norm_journal(mine) if name == "journal" else str(mine)
        b = _norm_journal(theirs) if name == "journal" else str(theirs)
        if a != b:
            fields[name] = theirs
            why.append(f"{name}: {mine!r} -> {theirs!r}")
    if fields:
        return {"action": "fix_meta", "fields": fields, "why": "; ".join(why)}
    return {"action": "none", "fields": {}, "why": "registry agrees"}


def rewrite_line(line: str, fields: dict, pages_text: str | None) -> str | None:
    """Apply `fields` to the journal/volume/issue/page span of one citation
    line. Returns the new line, or None if the span isn't parseable."""
    span = cc.source_meta_span(line)
    if not span:
        return None
    start, end, _ = span
    journal, vol, issue, page = cc.parse_source_meta(line)
    journal = fields.get("journal", journal)
    vol = fields.get("volume", vol)
    issue = fields.get("issue", issue)
    pages = pages_text or fields.get("first_page", page)
    return line[:start] + f"*{journal}, {vol}*({issue}), {pages}" + line[end:]


def strip_doi_from_line(line: str, doi: str) -> str:
    """Remove the DOI hyperlink, leaving the citation text intact but
    unlinked — the same shape verify_page_citations leaves behind."""
    for form in (f" [doi:{doi}](https://doi.org/{doi})",
                 f" [https://doi.org/{doi}](https://doi.org/{doi})"):
        for variant in (form, form.replace(doi, doi.upper())):
            line = line.replace(variant, "")
    return line


def proven_fabrications(not_found_dois, siblings: dict, verified: set) -> dict:
    """{404'd DOI -> the sibling that proves it wrong}, for the one shape where
    a Crossref 404 is proof rather than evidence.

    Pure, so the rule that decides whether to delete a DOI can be exercised
    without a network. `siblings` comes from
    check_citations.variant_siblings(); `verified` is the set of DOIs Crossref
    resolved to the paper the page actually cites.

    The narrowness is the point. It is NOT enough that the paper has some other
    DOI that resolves — a preprint and its published version legitimately carry
    two, from two registrants, and one of them may sit outside Crossref. The
    sibling must be near-identical: the same registrant, a suffix a couple of
    characters away. No publisher issues one article under two spellings of the
    same suffix, so if one of them is the article, the other is a
    misremembering of it."""
    out = {}
    for doi in not_found_dois:
        good = sorted(siblings.get(doi, set()) & verified)
        if good:
            out[doi] = good[0]
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true", help="report only")
    g.add_argument("--apply", action="store_true", help="write the corrections")
    ap.add_argument("--titles", action="store_true",
                    help="also correct titles, not just journal/volume/pages")
    ap.add_argument("--limit", type=int, default=None,
                    help="stop after this many DOIs (each is one Crossref call, cached)")
    args = ap.parse_args()

    import doi_resolver as dr
    import resolve_doi_conflicts as rdc      # noqa: F401  (shares the cache)

    by_key = cc.load_all_citations()
    by_doi = cc.load_by_doi(by_key)
    consensus = cc.token_consensus(by_doi)
    # Which DOIs are one of several near-identical spellings offered for the
    # same paper. On its own that is only a signal — see the note in
    # check_citations.find_doi_variant_families, where two RRQ DOIs one
    # character apart are both real. It becomes actionable exactly once: a
    # member Crossref has never heard of, sitting beside a member that
    # resolves to the paper being cited. See the post-pass below.
    siblings = cc.variant_siblings(cc.find_doi_variant_families(by_key))

    # Only DOIs some check actually flagged — no point spending a lookup on
    # the thousands the wiki already agrees about.
    flagged = set()
    for r in cc.find_metadata_divergence(by_doi):
        if r["severity"] == "conflict":
            flagged.add(r["doi"])
    for r in cc.find_title_divergence(by_doi):
        if r["severity"] == "conflict":
            flagged.add(r["doi"])
    for c in cc.find_doi_collisions(by_doi):
        flagged.add(c["doi"])
    # Citation conflicts too, which the three checks above structurally cannot
    # see. All of them need two *variants* of something — two journal strings,
    # two titles, two papers — so a DOI asserted on a single page is invisible
    # to every one of them. That is exactly the bandura-1977 shape: one page
    # carries 10.1037/12256-000 and 67 carry nothing, so nothing disagrees with
    # it and nothing checks it. standardize_citations.py surfaces these as
    # "resolves to the wrong paper" and then had no way to act on them.
    for c in cc.find_conflicts(by_key):
        for e in c["entries"]:
            if e["doi"]:
                flagged.add(e["doi"])

    todo = sorted(flagged)[: args.limit] if args.limit else sorted(flagged)
    print(f"{len(flagged)} flagged DOI(s); resolving {len(todo)}.\n", file=sys.stderr)

    cache = dr.load_cache()
    fixed = stripped = skipped = agreed = 0
    edits: dict[Path, list] = {}
    # Per-prefix resolution tallies, so a 404 can be weighed against whether
    # that registrant's other DOIs resolve at all.
    prefix_ok: dict[str, int] = {}
    not_found: list[tuple[str, str]] = []
    # DOIs Crossref resolved to the paper the page actually cites.
    verified: set = set()
    # not-found DOIs kept with their citation entries, for the sibling pass.
    nf_entries: dict[str, list] = {}

    for i, doi in enumerate(todo, 1):
        cached = cache.get(doi)
        # A cache entry written before this script existed has only a title.
        # Re-fetch those rather than reading absent fields as "registry said
        # nothing", which would silently make every old entry a no-op.
        if cached and not dr._is_stale(cached) and "journal" in cached:
            record = cached
        else:
            try:
                record = dr.resolve_doi(doi)
                cache[doi] = record
                dr.save_cache(cache)
            except Exception as e:
                print(f"  [{i}/{len(todo)}] {doi}: lookup failed ({e}) — unchanged",
                      file=sys.stderr)
                skipped += 1
                continue

        for entry in by_doi[doi]:
            if not entry.get("meta"):
                continue
            year = entry["key"].rsplit("-", 1)[-1]
            cited_title = cc._extract_title_text(entry["line"], year)
            d = decide(entry["meta"], record, cited_title)
            if d["action"] == "none":
                agreed += 1
                verified.add(doi)
                prefix_ok[doi.partition("/")[0]] = prefix_ok.get(doi.partition("/")[0], 0) + 1
                continue
            if d["action"] == "not_found":
                not_found.append((doi, entry["source"]))
                nf_entries.setdefault(doi, []).append(entry)
                continue
            if d["action"] == "skip":
                skipped += 1
                continue
            path = WIKI_ROOT / entry["source"]
            edits.setdefault(path, []).append((doi, d, _unescape_record(record)))
            print(f"  [{i}/{len(todo)}] {entry['source']}: {d['action']} — {d['why']}")
            prefix_ok[doi.partition("/")[0]] = prefix_ok.get(doi.partition("/")[0], 0) + 1
            if d["action"] in ("fix_meta", "fix_title"):
                fixed += 1
            else:
                stripped += 1

    # A 404 is not proof of fabrication — except in one shape. When a paper is
    # cited with several near-identical DOIs, at most one of them can be the
    # article; so if Crossref resolves one member of the family to the paper
    # being cited and has never heard of another, the second is not "a
    # registrar Crossref does not index". Its own sibling proves the article is
    # in Crossref, under a different suffix. That is the one case where the
    # variant family upgrades a 404 from evidence to proof, and it is what
    # closes the loop on DOIs like the four 10.1080/00098655.2012.* spellings
    # of Rosenshine (2012).
    variant_stripped = 0
    proven = proven_fabrications(nf_entries, siblings, verified)
    for doi, good_sibling in proven.items():
        for entry in nf_entries[doi]:
            path = WIKI_ROOT / entry["source"]
            d = {"action": "strip_doi", "fields": {},
                 "why": (f"no Crossref record, and sibling {good_sibling} resolves to the "
                         f"paper this cites — at most one spelling can be real")}
            edits.setdefault(path, []).append((doi, d, {}))
            print(f"  [variant] {entry['source']}: strip_doi — {d['why']}")
            variant_stripped += 1
            stripped += 1
    if proven:
        not_found = [(d, s_) for d, s_ in not_found if d not in proven]

    if args.apply and edits:
        for path, items in edits.items():
            text = path.read_text(encoding="utf-8")
            out = []
            for line in text.splitlines(keepends=True):
                for doi, d, record in items:
                    if doi.lower() not in line.lower():
                        continue
                    if d["action"] == "fix_meta":
                        new = rewrite_line(line, d["fields"], record.get("pages"))
                        if new:
                            line = new
                    elif d["action"] == "fix_title":
                        year = None
                        for e in by_doi[doi]:
                            if e["source"] == str(path.relative_to(WIKI_ROOT)):
                                year = e["key"].rsplit("-", 1)[-1]
                                break
                        old_t = cc._extract_title_text(line, year) if year else ""
                        if old_t and old_t in line:
                            line = line.replace(old_t, d["fields"]["title"], 1)
                    elif d["action"] == "strip_doi":
                        line = strip_doi_from_line(line, doi)
                out.append(line)
            path.write_text("".join(out), encoding="utf-8")

    verb = "Applied" if args.apply else "Would apply"
    print(f"\n{verb}: {fixed} metadata correction(s), {stripped} DOI removal(s) "
          f"across {len(edits)} page(s).")
    print(f"{agreed} citation(s) already matched the registry.")
    print(f"{skipped} skipped because the lookup failed — an outage is not a verdict.")
    if variant_stripped:
        print(f"{variant_stripped} of the removal(s) were near-identical DOI variants "
              f"({len(proven)} DOI(s)) that Crossref has no record of while a sibling "
              f"spelling resolves to the cited paper.")
    if not_found:
        # A 404 on a prefix whose other DOIs resolve fine is the strong case:
        # that registrant IS in Crossref, so the record's absence is about this
        # DOI rather than about coverage.
        strong = [(d, s) for d, s in not_found if prefix_ok.get(d.partition("/")[0], 0) >= 3]
        weak = [(d, s) for d, s in not_found if (d, s) not in strong]
        print(f"\n{len(not_found)} DOI(s) have no Crossref record. Not stripped — Crossref "
              f"does not index DataCite, mEDRA or JaLC registrations.")
        if strong:
            print(f"  {len(strong)} are on a prefix whose other DOIs resolve fine, so that "
                  f"registrant IS in Crossref and the absence is about the DOI:")
            for d, s in strong[:15]:
                print(f"      {d}   {s}")
            if len(strong) > 15:
                print(f"      ... and {len(strong) - 15} more")
        if weak:
            print(f"  {len(weak)} on prefixes with no other resolving DOI — could simply be "
                  f"a registrar Crossref does not cover.")
    if not args.apply and edits:
        print("\nRe-run with --apply to write these.")


if __name__ == "__main__":
    main()
