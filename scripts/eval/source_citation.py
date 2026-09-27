"""Deterministic repair of the source article's own citation, after generation.

Every evidence entry's `citation` names the article being extracted (v133's L0b:
"third-party works never appear in citation"). The model can copy that line from
the article header, but it cannot know a link the header does not print, and an
ERIC report, a conference paper or a preprint usually prints none. The validator
then failed it for "citation should include a year and a DOI/URL", and every
correction retry asked it to supply one, which is a request to invent a DOI.
In the 2026-09-24 pre-extractor test that was 23 of v133's 25 citation errors.

The pipeline already knows a stable link for the article: the catalogue URL it
was fetched from (the ERIC record, the arXiv abstract, the PMC page). So a
citation that names the source and carries no link gets that URL appended here,
before validation, and the record lists each repair. Nothing is appended to a
citation that does not name the source, and nothing is removed or
rewritten, except a bare site homepage standing in for a link (see fix()) and
an author list the model inverted (see swapped_authors()); a wrong DOI stays for
the citation gate, which checks it against the registry.
"""
import re
from urllib.parse import urlparse

from . import validator

_URL = re.compile(r"https?://[^\s)\]>]+", re.I)
_WORD = re.compile(r"[a-z0-9]+")
_STOP = {"a", "an", "the", "of", "and", "in", "on", "for", "to", "with", "by", "at", "from", "as", "is", "vs"}


def _words(text: str) -> list:
    return [w for w in _WORD.findall((text or "").lower()) if w not in _STOP]


def names_source(citation: str, entry: dict) -> bool:
    """True when the citation carries the source's title (its first 10 content
    words, 80% of them) and its year, give or take one. Titles are the identity
    test because the authors field in a catalogue record is formatted three
    different ways, and a year of one either way is allowed because catalogues
    date a conference paper by its submission (ERIC gives ED491961 as 2005; the
    paper was presented at AERA 2006)."""
    if not isinstance(citation, str):
        return False
    title = _words(entry.get("title"))[:10]
    if len(title) < 2:
        return False
    have = set(_words(citation))
    if sum(w in have for w in title) / len(title) < 0.8:
        return False
    try:
        year = int(entry.get("year"))
    except (TypeError, ValueError):
        return True
    return any(str(y) in citation for y in (year - 1, year, year + 1))


# PubMed's author format, "Husain W, Ammar A, Pandi-Perumal SR": surname, then initials.
_PUBMED_AUTHOR = re.compile(r"^(?P<family>[^\W\d_][\w'’‐-]*(?: [^\W\d_][\w'’‐-]*)*) (?P<initials>[A-Z]{1,3})$")
_FOLD = re.compile(r"[‐-]")


def _fold(name: str) -> str:
    return _FOLD.sub("-", (name or "").strip().lower())


def swapped_authors(citation: str, entry: dict):
    """The APA author list from the catalogue record, when the citation's authors
    are the record's with given name and surname exchanged; otherwise None.

    PMC's article text prints each author surname first ("Husain Waqar"), and GLM
    read the first word as a given name, writing "Waqar, Husain; Achraf, Ammar; ..."
    (batch 9, 2026-09-27). The citation gate then stripped the correct DOI from all
    eight pages, because the cited first author appears nowhere in the registry
    record. Only a PubMed-format record is used, and only when most of the
    citation's first authors carry the record's surname in the given-name place."""
    if not isinstance(citation, str) or not isinstance(entry.get("authors"), str):
        return None
    record = [_PUBMED_AUTHOR.match(a.strip()) for a in entry["authors"].split(",")]
    if not record or not all(record):
        return None
    head = citation.split("(", 1)[0]
    cited = [a.strip() for a in head.split(";") if a.strip()]
    pairs = [[x.strip() for x in a.split(",", 1)] for a in cited]
    pairs = [p for p in pairs if len(p) == 2]
    n = min(len(pairs), len(record), 5)
    if n < 2:
        return None
    swapped = sum(_fold(pairs[i][1]) == _fold(record[i]["family"]) and
                  _fold(pairs[i][0]) != _fold(record[i]["family"]) for i in range(n))
    if swapped < max(2, n - 1):
        return None
    names = [f"{m['family']}, {'. '.join(m['initials'])}." for m in record]
    return (", ".join(names[:-1]) + ", & " + names[-1]) if len(names) > 1 else names[0]


def _norm(link: str) -> str:
    u = urlparse(link)
    return (u.netloc.lower().removeprefix("www."), u.path.rstrip("/").lower(), u.query.lower())


def _same_catalogue(link: str, url: str) -> bool:
    """Same host and the same first path segment as the catalogue URL, so a link
    to the same catalogue's record page: eric.ed.gov/?id=..., a PMC article page,
    an arXiv abstract. A DOI or publisher link is never one."""
    a, b = urlparse(link), urlparse(url)
    if a.netloc.lower().removeprefix("www.") != b.netloc.lower().removeprefix("www."):
        return False
    first = lambda u: (u.path.strip("/").split("/") or [""])[0].lower()
    return first(a) == first(b) and (bool(a.query) == bool(b.query))


def repair(parsed: dict, entry: dict) -> list:
    """Append the catalogue URL to every source citation that carries no link.
    Edits `parsed` in place and returns [{field, added}] for the record."""
    url = (entry or {}).get("url")
    if not isinstance(parsed, dict) or not url:
        return []
    repairs = []

    def fix(value, field):
        if not (isinstance(value, str) and names_source(value, entry)):
            return value
        authors = swapped_authors(value, entry)
        if authors:
            head, sep, rest = value.partition("(")
            value = authors + " " + sep + rest
            repairs.append({"field": field, "replaced": head.strip(), "authors": authors})
        # A bare site homepage is not a link to the article: GLM wrote
        # "https://www.aera.net" for an AERA paper to satisfy "needs a DOI/URL"
        # (bench, 2026-09-26). It is replaced by the catalogue URL, and that is
        # the only rewrite this module makes.
        for m in _URL.finditer(value):
            link = m.group(0).rstrip(".,;")
            if urlparse(link).path.strip("/") == "" and not urlparse(link).query:
                repairs.append({"field": field, "replaced": link, "added": url})
                return value.replace(link, url)
            # A link into the catalogue the article was fetched from, naming another
            # record: GLM gave Armbruster & Anderson (1982), fetched as ED218595, the
            # link eric.ed.gov/?id=ED185595, which the article never prints (batch 9,
            # 2026-09-27). The catalogue URL is known, so it replaces the guess.
            if _same_catalogue(link, url) and _norm(link) != _norm(url):
                repairs.append({"field": field, "replaced": link, "added": url})
                return value.replace(link, url)
        if not validator.CITATION_LINK_RE.search(value):
            repairs.append({"field": field, "added": url})
            return value.rstrip().rstrip(".") + ". " + url
        return value

    for i, c in enumerate(parsed.get("contributions") or []):
        if not isinstance(c, dict):
            continue
        for j, ev in enumerate(c.get("evidence") or []):
            if isinstance(ev, dict) and "citation" in ev:
                ev["citation"] = fix(ev["citation"], f"contributions[{i}].evidence[{j}].citation")
        ks = c.get("key_sources")
        if isinstance(ks, list):
            c["key_sources"] = [fix(s, f"contributions[{i}].key_sources[{j}]") for j, s in enumerate(ks)]
    return repairs
