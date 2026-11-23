#!/usr/bin/env python3
"""
arxiv_dois.py — give each evidence entry read from an arXiv preprint a verified DOI, preferring the
published version's (maintainer, 2026-11-16: a preprint and its published version are one study).

Extraction cites an arXiv source by whatever link its text offers (a lab homepage, Google Scholar,
"https://arxiv.org"), and often with the year of a conference or journal version rather than the
preprint's, so nearly every claim an arXiv batch writes fails the DOI rule. Done by hand on the first
two batches, a page-level shortcut put one paper's DOI on another paper's entry where a page cited
two. This works entry by entry:

  1. which source: the entry's citation title is matched to the batch's own arXiv sources in the
     manifest (check_citations.titles_align and 80% of significant words); no match, no change;
  2. the published version, when the arXiv snapshot names one or Crossref finds it by title and first
     author: accepted only with the title aligned, the first author's family name present in the
     citation, and the year within one of the cited year. The same study then carries one DOI
     wherever it is cited, which is what lets a duplicate claim be found and a study counted once;
  3. else the preprint's own DataCite DOI (10.48550/arXiv.<id>), with the title aligned, or for a
     translated title the first author and year (the arXiv id from the manifest is the coordinate).
  A cited year that is not the chosen record's becomes the record's year (even one year off). An
  earlier one is kept in the citation as "Originally published YYYY" only when the article's own cached
  text puts that year beside a publication word (proceedings, conference, journal, presented, ...):
  most earlier years a model writes are a data-collection or conference year it guessed, and a note
  saying so reads as verified (maintainer, 2026-11-22).

    --years   for entries already citing a preprint's arXiv DOI on the batch's pages, align the cited
              year with the DataCite record's, the same way (a published DOI's Crossref year is left
              alone: a proceedings volume is often issued the year after the one it is cited by)

The body citation line is rewritten (the DOI link takes the place of the line's other URLs) along
with the entry's heading and the anchors that point at it; sync_evidence_codes.py rebuilds sources[]
from the body afterwards. Decisions go to eval/runs/arxiv-dois.ndjson.

    python3 scripts/sweep/arxiv_dois.py --label j-scrarxiv-3 --check
    python3 scripts/sweep/arxiv_dois.py --label j-scrarxiv-3 --apply [--pages claims/a.md ...]
    python3 scripts/sweep/arxiv_dois.py --label j-scrarxiv-1 --apply --upgrade   # earlier batches
"""
import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
from pathlib import Path

import requests

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402
from check_citations import titles_align  # noqa: E402

UA = {"User-Agent": "learning-wiki/1.0 (mailto:contact@learningdesignalliance.org)"}
LOG = WIKI_ROOT / "eval" / "runs" / "arxiv-dois.ndjson"
ENTRY = re.compile(r"(?m)^(### )([^\n]+?) (\d{4})((?: \(\d+\))?)\n\n([^\n`>][^\n]*)$")


def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def words(s):
    return {w for w in re.findall(r"[a-z0-9]+", fold(s)) if len(w) > 3}


def overlap(a, b):
    x, y = words(a), words(b)
    return len(x & y) / max(1, min(len(x), len(y))) if x and y else 0


def get(url, params=None):
    for t in range(4):
        try:
            r = requests.get(url, params=params, headers=UA, timeout=40)
            if r.status_code == 429:
                time.sleep(2 ** t)
                continue
            return r
        except requests.RequestException:
            time.sleep(2 ** t)
    return None


def crossref(doi):
    r = get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/()"))
    if r is None or r.status_code != 200:
        return None
    m = r.json()["message"]
    return {"doi": m["DOI"], "title": (m.get("title") or [""])[0],
            "first": fold((m.get("author") or [{}])[0].get("family", "")),
            "year": ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0]}


def crossref_search(title, first):
    r = get("https://api.crossref.org/works", {"rows": 5, "query.bibliographic": f"{title} {first}"})
    if r is None or r.status_code != 200:
        return []
    out = []
    for m in r.json()["message"]["items"]:
        out.append({"doi": m["DOI"], "title": (m.get("title") or [""])[0],
                    "first": fold((m.get("author") or [{}])[0].get("family", "")),
                    "year": ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0]})
    return out


def datacite(aid):
    r = get("https://api.datacite.org/dois/" + urllib.parse.quote(f"10.48550/arxiv.{aid}", safe="/"))
    if r is None or r.status_code != 200:
        return None
    a = r.json()["data"]["attributes"]
    cr = a.get("creators") or [{}]
    return {"doi": f"10.48550/arXiv.{aid}", "title": (a.get("titles") or [{}])[0].get("title", ""),
            "first": fold(cr[0].get("familyName") or cr[0].get("name") or ""), "year": a.get("publicationYear")}


CACHE = WIKI_ROOT / "eval" / "corpus" / "cache"
PUB_WORDS = re.compile(r"published in|proceedings of|presented at|accepted (?:for|to|in|at|by)|appeared in|"
                       r"to appear in|copyright|©|journal of|conference on|symposium on", re.I)


def earlier_year_supported(aid, year):
    """Does the article's own front matter tie `year` to a publication? Only the first 4,000 characters
    are read: a year in the reference list is some other paper's, and says nothing about this one."""
    f = CACHE / f"arxiv-{aid}.txt"
    if not f.exists():
        return False
    head = f.read_text(encoding="utf-8", errors="ignore")[:4000]
    # a year that ends or starts a range ("between 2001 and 2018", "2012-2018") is the data's span,
    # not a publication of this article (Odden et al. 2020, split batch 5)
    in_range = re.compile(rf"(?:\d{{4}}\s*(?:-|–|to|and)\s*{year}(?!\d))|(?:(?<!\d){year}\s*(?:-|–|to)\s*\d{{4}})")
    # nor is a year in a template stub ("Journal xx (xx)"), in a submission or forthcoming notice, in a
    # meeting's dates ("11-16 July 2021") or in a study's name ("Snowmass 2021") (split batch 6)
    not_publication = re.compile(r"\bxx\b|submitted to|to appear|\d{1,2}\s*[-–]\s*\d{1,2}\s+[A-Z][a-z]+\s*$|"
                                 r"Snowmass\s*$", re.I)
    return any(PUB_WORDS.search(head[max(0, m.start() - 120):m.end() + 120])
               and not in_range.search(head[max(0, m.start() - 12):m.end() + 8])
               and not not_publication.search(head[max(0, m.start() - 120):m.start()])
               for m in re.finditer(rf"(?<!\d){year}(?!\d)", head))


def cited_title(line, year):
    # a ". " after a lone capital is an initial inside the title ("A.V. Usova's Contribution"), not its end
    m = re.search(rf"\({year}\)\.\s*(.+?)(?:(?<!\b[A-Z])\.\s|\?\s|$)", line)
    return (m.group(1) if m else line).strip(" .*")


def published_ok(rec, title, citation, year):
    return bool(rec and rec["title"] and overlap(title, rec["title"]) >= 0.75 and titles_align(title, rec["title"])
                and rec["first"] and rec["first"].split()[-1] in fold(citation) and rec["year"]
                and abs(int(rec["year"]) - year) <= 1)


def decide(title, citation, year, aid, snapshot_doi):
    if snapshot_doi:
        rec = crossref(snapshot_doi)
        if published_ok(rec, title, citation, year):
            return rec, "published (arXiv snapshot DOI, Crossref-verified)"
    for rec in crossref_search(title, (re.split(r"[ ,.]", citation.strip()) or [""])[0]):
        if published_ok(rec, title, citation, year):
            return rec, "published (Crossref title search)"
    rec = datacite(aid)
    if not rec:
        return None, "no DataCite record"
    author = rec["first"] and rec["first"].split()[-1] in fold(citation)
    aligned = overlap(title, rec["title"]) >= 0.75 and titles_align(title, rec["title"])
    if aligned or (author and abs(int(rec["year"]) - year) <= 1):
        return rec, "preprint (DataCite)" + ("" if aligned else ", translated title: author, year and arXiv id")
    return None, "DataCite title and author do not match the citation"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--label", required=True, help="the batch, e.g. j-scrarxiv-3")
    ap.add_argument("--pages", nargs="*", help="only these pages (default: every page the batch's arXiv sources wrote)")
    ap.add_argument("--upgrade", action="store_true",
                    help="also move entries that cite a preprint's arXiv DOI to its published version's")
    ap.add_argument("--years", action="store_true",
                    help="only align the cited year of entries that already give a DOI with that DOI's record")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    batch = json.loads((WIKI_ROOT / f"eval/corpus/manifest_{a.label}.json").read_text(encoding="utf-8"))
    ids = {str(x.get("id")) for x in (batch.get("articles") if isinstance(batch, dict) else batch) or []}
    latest = {}
    for r in okf_lib.load_manifest():
        latest[r["id"]] = r
    sources = {i: r for i, r in latest.items() if i.startswith("arxiv-") and r.get("status") == "ingested"
               and (not ids or i in ids)}
    snap = {}
    for l in (WIKI_ROOT / "eval/screening/arxiv-education-research.ndjson").read_text(encoding="utf-8").splitlines()[1:]:
        m = json.loads(l)
        snap[m["id"]] = (m.get("doi") or "").lower() or None
    pages = a.pages
    if not pages:
        # the pages the batch's sources wrote, and the older claims it changed in the working tree: a
        # claim merge folds an arXiv entry into an existing page the manifest does not list
        import subprocess
        changed = subprocess.run(["git", "diff", "--name-only", "--", "claims"], cwd=WIKI_ROOT,
                                 capture_output=True, text=True).stdout.split()
        pages = sorted({p for r in sources.values() for p in r.get("pages") or [] if p.startswith("claims/")}
                       | {p for p in changed if p.endswith(".md") and not p.endswith("index.md")})
    log = LOG.open("a", encoding="utf-8") if a.apply else None
    done = changed = 0
    for page in pages:
        path = WIKI_ROOT / page
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        renames = {}

        def fix(mo):
            nonlocal done
            head, who, year, n, line = mo.groups()
            year = int(year)
            if "doi.org/10." in line and a.years:
                # --years: the cited year follows the record of the DOI the entry already gives
                dm = re.search(r"\[doi:(10\.[^\]]+)\]", line)
                if not dm:
                    return mo.group(0)
                doi = dm.group(1)
                arx = re.match(r"10\.48550/arxiv\.(.+)$", doi, re.I)
                if not arx:
                    # only a preprint's posting year is unambiguous: Crossref's issued year for a
                    # proceedings volume (PERC 2013 issued 2014) is not the year it is cited by
                    return mo.group(0)
                rec = datacite(arx.group(1))
                title = cited_title(line, year)
                if not (rec and rec["year"] and int(rec["year"]) != year and overlap(title, rec["title"]) >= 0.75
                        and titles_align(title, rec["title"])):
                    return mo.group(0)
                new_year = int(rec["year"])
                note = (f" Originally published {year}."
                        if year < new_year and earlier_year_supported(arx.group(1), year) else "")
                renames[f"{who} {year}{n}"] = f"{who} {new_year}{n}"
                done += 1
                if log:
                    log.write(json.dumps({"page": page, "entry": f"{who} {new_year}{n}", "doi": doi,
                                          "why": f"cited year {year} aligned with the record's {new_year}"}) + "\n")
                print(f"  {page.split('/')[-1][:44]:44} {who[:24]:24} {year} -> {new_year}  {doi}")
                line = re.sub(rf"\({year}\)", f"({new_year})", line, count=1)
                if note and "Originally published" not in line:
                    line = line.replace(f" [doi:{doi}]", f"{note} [doi:{doi}]", 1)
                return f"{head}{who} {new_year}{n}\n\n{line}"
            if "doi.org/10." in line:
                arx = re.search(r"\[doi:(10\.48550/arxiv\.([^\]]+))\]\([^)]+\)", line, re.I)
                if not (a.upgrade and arx):
                    return mo.group(0)
                # --upgrade: an entry citing the preprint's own DOI takes the published version's,
                # by the same test, and nothing else about it changes
                title = cited_title(line, year)
                aid = arx.group(2)
                rec = None
                snap_doi = snap.get(f"arxiv-{aid}")
                for cand in ([crossref(snap_doi)] if snap_doi else []) + crossref_search(
                        title, (re.split(r"[ ,.]", line.strip()) or [""])[0]):
                    if published_ok(cand, title, line, year):
                        rec = cand
                        break
                if not rec:
                    return mo.group(0)
                done += 1
                entry = {"page": page, "entry": f"{who} {year}{n}", "arxiv": aid, "doi": rec["doi"],
                         "why": "upgraded from the preprint's DOI to the published version's"}
                if log:
                    log.write(json.dumps(entry, ensure_ascii=False) + "\n")
                print(f"  {page.split('/')[-1][:44]:44} {who[:24]:24} {year} -> {rec['doi']:34} upgraded")
                return mo.group(0).replace(arx.group(0), f"[doi:{rec['doi']}](https://doi.org/{rec['doi']})")
            title = cited_title(line, year)
            match = [(overlap(title, r["title"]), i) for i, r in sources.items()
                     if overlap(title, r["title"]) >= 0.8 and titles_align(title, r["title"])]
            if not match:
                # a citation in the article's own language, against a manifest title in English: the
                # page's one source, when the manifest names exactly one, still has to pass the
                # translated-title check (first author and year) on DataCite
                wrote = [i for i, r in sources.items() if page in (r.get("pages") or [])]
                if len(wrote) != 1:
                    return mo.group(0)
                match = [(0, wrote[0])]
            aid = max(match)[1].removeprefix("arxiv-")
            rec, why = decide(title, line, year, aid, snap.get(f"arxiv-{aid}"))
            done += 1
            entry = {"page": page, "entry": f"{who} {year}{n}", "arxiv": aid, "doi": rec and rec["doi"], "why": why}
            if log:
                log.write(json.dumps(entry, ensure_ascii=False) + "\n")
            print(f"  {page.split('/')[-1][:44]:44} {who[:24]:24} {year} -> {entry['doi'] or '-':34} {why}")
            if not rec:
                return mo.group(0)
            new_year = year
            note = ""
            # the citation carries the year of the record whose DOI it gives: a year one off (a preprint
            # posted the year after the conference, or the data-collection year) is still the wrong year,
            # and the load-bearing judge fails it
            if int(rec["year"]) != year:
                new_year = int(rec["year"])
                if year < new_year and earlier_year_supported(aid, year):
                    note = f" Originally published {year}."
                line = re.sub(rf"\({year}\)", f"({new_year})", line, count=1)
                renames[f"{who} {year}{n}"] = f"{who} {new_year}{n}"
            line = re.sub(r"\s*<?https?://(?!doi\.org)[^\s>]+>?", "", line).rstrip(" .")
            link = f"[doi:{rec['doi']}](https://doi.org/{rec['doi']})"
            return f"{head}{who} {new_year}{n}\n\n{line}.{note} {link}"

        new = ENTRY.sub(fix, text)
        for old, nw in renames.items():
            # python-markdown's heading id: punctuation dropped ("J.O." -> "jo"), spaces to hyphens
            o_anchor = re.sub(r"[-\s]+", "-", re.sub(r"[^\w\s-]", "", fold(old))).strip("-")
            n_anchor = re.sub(r"[-\s]+", "-", re.sub(r"[^\w\s-]", "", fold(nw))).strip("-")
            new = new.replace(f"(#{o_anchor})", f"(#{n_anchor})").replace(f"→ {old}]", f"→ {nw}]")
        if new != text:
            changed += 1
            if a.apply:
                path.write_text(new, encoding="utf-8")
    print(f"{done} arXiv entr(ies) decided; {changed} page(s) {'changed' if a.apply else 'would change'}")


if __name__ == "__main__":
    main()
