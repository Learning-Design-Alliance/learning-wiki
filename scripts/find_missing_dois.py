#!/usr/bin/env python3
"""
find_missing_dois.py — find the DOI of a Key Sources citation that has none, and add it only when the
registry record is the cited work.

Many Key Sources bullets carry an APA citation with no DOI or link (maintainer, 2026-10-14, on
patterns/case-based-learning): about 4,200 across the wiki, ~520 on the pages the main site renders.
Some are books or older journals with no DOI at all; others have one nobody looked up.

For each such bullet this asks Crossref's bibliographic search for the citation's own text and takes a
candidate only if BOTH checks the rest of the citation tooling uses pass:

- the registered title is the cited title: the title is cut out of the citation
  (check_citations._extract_title_text) and the two must agree on their main title (before any colon)
  or share at least 75% of their significant words, and check_citations.titles_align() must pass (the
  check added after a containment match put Bandura 1977 on 69 pages). The first run compared the
  registered title with the WHOLE citation line, and titles_align() is only a guard against one
  shape, so a title whose words appeared anywhere in the line passed: Stein & Valters (2012) took a
  Who's Who entry, Hunter's *Mastery teaching* took "General psychology". 257 matches, none written;
  this rule replaced it;
- citation_identity.identity_mismatch(): the registry's first author and year agree with the citation;
- the registered year is within one of the cited year (or of an "Original work published" year):
  a later edition or reissue is a different record;
- the registry's first author is the citation's first author, and an article's journal is the cited
  journal (a review of Terman & Oden carried their names and title with the reviewer first);
- the kind of work agrees: a citation written as a book (italic title, then a publisher) takes only a
  book record, one written as an article (a volume) never takes a book or a chapter. Herreid (2011),
  *Case study teaching*, NSTA Press, is a book, and the same author's 2011 journal chapter of the same
  title passed the first two checks.

Anything else is left as it is: a book with no DOI is a correct citation without one, and an absent
DOI is "not established", never a guess. Decisions go to eval/missing-dois/decisions.ndjson before any
page is written, so a run can be audited and re-applied without asking Crossref again.

    python3 scripts/find_missing_dois.py --folders principles patterns --check
    python3 scripts/find_missing_dois.py --folders principles patterns --apply
    python3 scripts/find_missing_dois.py --apply --from eval/missing-dois/decisions.ndjson
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
from pathlib import Path

import requests

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from check_citations import _extract_title_text, _norm_title, _words_from_text, titles_align  # noqa: E402
from citation_identity import identity_mismatch  # noqa: E402

OUT = WIKI_ROOT / "eval" / "missing-dois" / "decisions.ndjson"
HAS_LINK = re.compile(r"doi\.org|10\.\d{4,9}/|https?://")
MAILTO = os.environ.get("EVAL_HARNESS_CONTACT_EMAIL", "")


def bullets(folders: list) -> list:
    """(page, line) for every Key Sources bullet with no DOI or link, outside comments."""
    out = []
    for folder in folders:
        for p in sorted((WIKI_ROOT / folder).glob("*.md")):
            if p.name == "index.md":
                continue
            text = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
            if "\n## Key Sources" not in text:
                continue
            section = re.split(r"\n## ", text.split("\n## Key Sources", 1)[1])[0]
            for ln in section.split("\n"):
                if ln.startswith("- ") and len(ln) > 25 and not HAS_LINK.search(ln) and re.search(r"\(\d{4}[a-z]?\)", ln):
                    out.append((str(p.relative_to(WIKI_ROOT)), ln))
    return out


def plain(line: str) -> str:
    return re.sub(r"[*_`\[\]]", "", line[2:]).strip()


def key_of(line: str):
    m = re.match(r"-\s*\*?([^\s,(]+)", line)
    y = re.search(r"\((\d{4})[a-z]?\)", line)
    if not m or not y:
        return None
    return f"{m.group(1).strip('*').lower()}-{y.group(1)}"


def record_of(item: dict) -> dict:
    def names(people):
        return [p.get("family") or p.get("name") for p in people or [] if p.get("family") or p.get("name")]
    issued = (item.get("issued") or {}).get("date-parts") or [[None]]
    return {"resolved": True, "type": item.get("type"), "authors": names(item.get("author")),
            "editors": names(item.get("editor")), "year": issued[0][0] if issued and issued[0] else None,
            "title": (item.get("title") or [""])[0]}


def same_title(cited: str, registered: str) -> bool:
    if not cited or not registered or not titles_align(cited, registered):
        return False
    main = lambda t: _norm_title(re.split(r"[:?]", t, maxsplit=1)[0])
    if main(cited) and main(cited) == main(registered):
        return True
    a, b = _words_from_text(cited), _words_from_text(registered)
    # A citation that shortens the registered title (Vinney et al. 2019 drops "in undergraduate
    # speech-language pathology students") is a prefix of it; five significant words keep a short
    # generic title from matching a longer work that opens with it.
    if len(a) >= 5 and _norm_title(registered).startswith(_norm_title(cited).rstrip(" .")):
        return True
    return bool(a and b) and len(a & b) / len(a | b) >= 0.75


def fold(name: str) -> str:
    return unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower().replace(" ", "")


def search(line: str) -> dict:
    q = urllib.parse.quote(plain(line)[:300])
    url = (f"https://api.crossref.org/works?query.bibliographic={q}&rows=5"
           f"&select=DOI,title,author,editor,issued,published-print,published-online,type,container-title" + (f"&mailto={MAILTO}" if MAILTO else ""))
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                return r.json()
            if r.status_code in (429, 503):
                time.sleep(5 * (attempt + 1))
                continue
            return {"error": f"HTTP {r.status_code}"}
        except requests.RequestException as e:
            err = str(e)[:120]
            time.sleep(3)
    return {"error": err if 'err' in dir() else "no response"}


BOOK_TYPES = {"book", "monograph", "edited-book", "reference-book", "book-set", "book-series"}
ARTICLE_TYPES = {"journal-article", "proceedings-article", "posted-content", "report"}


def form_of(line: str):
    """'article' when an italic title or journal is followed by a volume number, 'book' when an italic
    title is followed by a publisher with no volume, else None (no constraint)."""
    if re.search(r"\*[^*]+\*\s*,?\s*\*?\d+", line) or re.search(r"\*[^*]+,\s*\d+\*", line):
        return "article"
    if re.search(r"\*[^*]+\*\.?\s*(?:\(\d+(?:st|nd|rd|th) ed\.\)\.\s*)?[A-Z][^.()]*\.?\s*$", line.strip()):
        return "book"
    return None


def decide(page: str, line: str) -> dict:
    key = key_of(line)
    y = re.search(r"\((\d{4})[a-z]?\)", line)
    cited = _extract_title_text(line, y.group(1)) if y else ""
    res = search(line)
    if "error" in res:
        # A failed lookup establishes nothing (CLAUDE.md: error is not wrong_paper).
        return {"page": page, "line": line, "doi": None, "why": "lookup failed: " + res["error"]}
    for item in (res.get("message") or {}).get("items") or []:
        rec = record_of(item)
        if not same_title(re.sub(r"[*_`]", "", cited), rec["title"]):
            continue
        if key and identity_mismatch(key, rec):
            continue
        # Same author, year and title is not enough: Herreid (2011) "Case study teaching" is an NSTA
        # Press book and also a 2011 journal chapter. The citation's form says which it is.
        form = form_of(line)
        if form == "book" and rec["type"] not in BOOK_TYPES:
            continue
        if form == "article" and rec["type"] in BOOK_TYPES | {"book-chapter"}:
            continue
        # identity_mismatch tolerates a missing or distant year, and a reissue is registered under its
        # own year: van Merrienboer & Kirschner (2007), the first edition of *Ten steps*, matched the
        # 2018 third edition. One year either way of the cited year (or of an "Original work published"
        # year) covers online-first dates and nothing else.
        years = {((item.get(k) or {}).get("date-parts") or [[None]])[0][0]
                 for k in ("published-print", "published-online", "issued")} - {None}
        cited_years = {int(y.group(1))} | {int(o) for o in re.findall(
            r"[Oo]riginal(?:ly)? (?:work )?published (?:in )?(\d{4})", line)} if y else set()
        if not any(abs(a - b) <= 1 for a in years for b in cited_years):
            continue
        # The first named person must be the citation's first author: a review of Terman & Oden (1959)
        # carries their names and title, with the reviewer first.
        first = (rec["authors"] or rec["editors"] or [""])[0]
        cited_first = fold(key.rsplit("-", 1)[0]) if key else ""
        if first and cited_first and cited_first not in fold(first):   # "van" in "vanmerrienboer"
            continue
        # An article citation names its journal; a record in another journal is either another paper or
        # a citation whose venue is wrong (Kunter & Baumert 2006 is cited in Teaching and Teacher
        # Education and registered in Learning Environments Research), and neither is fixed by a DOI.
        journal = re.search(r"\*([^*]+?),\s*\d+\*?", line)
        venue = (item.get("container-title") or [""])[0]
        if form == "article" and journal and venue and not same_title(journal.group(1), venue):
            continue
        return {"page": page, "line": line, "doi": item["DOI"].lower(), "title": rec["title"],
                "why": "title, first author and year agree with the Crossref record"}
    return {"page": page, "line": line, "doi": None, "why": "no Crossref record matched title, first author and year"}


def apply(decisions: list) -> int:
    written = 0
    by_page = {}
    for d in decisions:
        if d.get("doi"):
            by_page.setdefault(d["page"], []).append(d)
    for page, ds in by_page.items():
        path = WIKI_ROOT / page
        text = path.read_text(encoding="utf-8")
        head, sep, tail = text.partition("\n## Key Sources")
        for d in ds:
            line = d["line"]
            new = line.rstrip() + f" [doi:{d['doi']}](https://doi.org/{d['doi']})"
            if line in tail and new not in tail:
                tail = tail.replace(line, new, 1)
                written += 1
        path.write_text(head + sep + tail, encoding="utf-8")
    return written


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--folders", nargs="+", default=["principles", "patterns", "processes", "methods",
                                                       "learner-variables", "designs"])
    ap.add_argument("--from", dest="from_file")
    ap.add_argument("--workers", type=int, default=4)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if args.from_file:
        decisions = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        todo = bullets(args.folders)
        print(f"{len(todo)} Key Sources citation(s) with no DOI or link", flush=True)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        decisions = []
        with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.workers) as ex:
            for d in ex.map(lambda pl: decide(*pl), todo):
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
                decisions.append(d)
    found = [d for d in decisions if d.get("doi")]
    failed = sum(1 for d in decisions if d["why"].startswith("lookup failed"))
    print(f"{len(found)} DOI(s) found; {len(decisions) - len(found) - failed} with no matching record "
          f"(books and unregistered articles); {failed} lookups failed")
    if args.apply:
        print(f"wrote {apply(found)} DOI(s)")


if __name__ == "__main__":
    main()
