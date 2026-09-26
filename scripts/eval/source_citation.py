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
rewritten, except a bare site homepage standing in for a link (see fix());
a wrong DOI stays for the citation gate, which checks it against the registry.
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
        # A bare site homepage is not a link to the article: GLM wrote
        # "https://www.aera.net" for an AERA paper to satisfy "needs a DOI/URL"
        # (bench, 2026-09-26). It is replaced by the catalogue URL, and that is
        # the only rewrite this module makes.
        for m in _URL.finditer(value):
            link = m.group(0).rstrip(".,;")
            if urlparse(link).path.strip("/") == "" and not urlparse(link).query:
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
