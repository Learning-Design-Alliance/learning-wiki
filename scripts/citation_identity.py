"""
citation_identity.py — Does a registry record name the work a citation names?

Every DOI check in this repo compared the cited TITLE with the registry's, and
sometimes the journal, volume and first page. None asked who wrote it or when.
That gap let three kinds of wrong DOI through, all found in the 2026-09-26
citation pass:

  * a different paper with a similar title. Pronovost et al. (2006), "An
    intervention to decrease catheter-related bloodstream infections in the
    ICU", was about to receive 10.1016/j.ajic.2008.10.008, a 2008 paper in
    another journal whose title overlaps almost word for word;
  * a journal review of the cited book. 10.2307/2804509 carries exactly the
    title of Lave & Wenger (1991), *Situated learning*, because it is Bloch's
    1994 review of it. The reviewer is the first author;
  * a record of the wrong kind. 10.1037/e502412013-155 is a PsycEXTRA dataset
    record of Mueller & Oppenheimer's conference talk, cited on seven pages as
    their 2014 *Psychological Science* article.

`identity_mismatch()` answers the one question the title checks cannot: given
the citation's author-year key (check_citations' key, e.g. "pronovost-2006")
and the registry record, is this the same work? It is pure and offline, so
every caller (the ingest gate, standardize_citations, resolve_citation_metadata)
applies the same rule and it can be tested without a network.

It returns None when the record is consistent with the key, or a short reason
when it is not. It errs toward None: a record with no authors, or a key whose
year cannot be read, decides nothing, because "the registry did not say" is not
evidence that the wiki is wrong.
"""

import re
import unicodedata

# Registry types that are never the thing a wiki citation means. A dataset
# record is how PsycEXTRA registers conference abstracts; a peer-review record is
# a referee report. Preprints (posted-content) are legitimately cited and are
# NOT in this set.
UNCITABLE_TYPES = {"dataset", "peer-review", "component"}

# Types whose registry year routinely differs from the cited year, because the
# DOI belongs to a reprint, a new edition or an online re-issue of the same text
# (Collins, Brown & Newman 1989 is registered as a 2018 Routledge chapter). A
# year mismatch alone is not treated as a different work for these.
BOOK_TYPES = {"book", "monograph", "edited-book", "book-chapter", "reference-entry",
              "book-section", "book-part", "reference-book", "report"}

# Types for which authorship can legitimately be carried by editors, so the
# cited "author" may appear anywhere in the list rather than first.
EDITED_TYPES = {"book", "monograph", "edited-book", "reference-book"}


def fold(name: str) -> str:
    """Lowercase ASCII letters only: 'Rimm‐Kaufman' -> 'rimmkaufman',
    'van Merriënboer' -> 'vanmerrienboer'."""
    s = unicodedata.normalize("NFKD", name or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.lower())


def _lev(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def same_surname(cited: str, registry: str) -> bool:
    """Tolerant surname match. Crossref spells 'Palincsar' as 'Palinscar' and
    'Rowe' as 'Row', puts whole names in the family field ('Brandi Simonsen'),
    and drops or keeps particles ('Merriënboer' vs 'van Merrienboer')."""
    c, r = fold(cited), fold(registry)
    if not c or not r:
        return False
    if r.startswith(c[:6]) or (len(r) >= 3 and c.startswith(r)):
        return True
    if (len(c) >= 4 and c in r) or (len(r) >= 4 and r in c):
        return True
    if len(c) >= 3 and r.endswith(c):          # 'Gog' read off 'van Gog, T.'
        return True
    return len(c) >= 5 and _lev(c, r[:len(c) + 1]) <= 2


def parse_key(key: str):
    """'rimm-kaufman-2007' -> ('rimm-kaufman', 2007). The year may carry a
    letter suffix ('2007a'); a key with no readable year returns None for it."""
    surname, _, yr = (key or "").rpartition("-")
    m = re.match(r"(\d{4})", yr)
    return (surname or yr), (int(m.group(1)) if m else None)


def cited_surnames(line: str, year) -> list:
    """Surnames of the authors a citation line lists before its '(Year)'."""
    head = line.split(f"({year}")[0] if year else line
    return re.findall(r"([A-Z][A-Za-z'\u2019\-]+(?: [A-Z][a-z]+)?), [A-Z]\.", head)


def identity_mismatch(key: str, record: dict):
    """None if the registry record is consistent with the citation's
    author-year key; otherwise a one-line reason it names a different work.

    This is strong enough to act on: callers treat a mismatch as the DOI
    belonging to another work. The co-author check below is not, and is kept
    separate for that reason."""
    if not record or not record.get("resolved"):
        return None
    rtype = record.get("type")
    if rtype in UNCITABLE_TYPES:
        return f"the registry record is a {rtype}, not the cited work"
    surname, year = parse_key(key)
    authors = [a for a in (record.get("authors") or []) if a]
    editors = [a for a in (record.get("editors") or []) if a]
    names = authors or editors
    ryear = record.get("year")
    if surname and names and not same_surname(surname, names[0]):
        anywhere = any(same_surname(surname, n) for n in authors + editors)
        # The cited author further down the list, in the same year, is the page
        # getting the author ORDER wrong on the right paper (Dweck 1998 for
        # Mueller & Dweck 1998). A review of a book comes years after it.
        same_year = bool(year and ryear and abs(int(ryear) - year) <= 1)
        if not (anywhere and (rtype in EDITED_TYPES or same_year)):
            where = "later in the author list" if anywhere else "nowhere in it"
            return (f"the registry's first author is {names[0]}; the cited "
                    f"author {surname} appears {where}")
    if year and ryear and abs(int(ryear) - year) > 1 and rtype not in BOOK_TYPES:
        return f"the registry dates it {ryear}, the citation {year}"
    return None


def coauthor_mismatch(record: dict, cited_authors: list):
    """None, or a reason the citation's SECOND author is not among the
    registry's authors.

    Report-only, never grounds for removing a DOI. It catches a citation built
    from two works, where the first author matches and the rest belongs to
    someone else (Mayer & Fiorella cited under a DOI that is Mayer's
    single-author chapter). But in a corpus check most hits were the right DOI
    with invented co-authors, which removing the DOI would not fix. So callers
    use it only to refuse an automatic TITLE rewrite. It applies only when the
    registry lists two or more authors, because Crossref sometimes records the
    first author alone (Harkins et al. 2021: one author there, six on the
    article)."""
    authors = [a for a in ((record or {}).get("authors") or []) if a]
    if not cited_authors or len(cited_authors) < 2 or len(authors) < 2:
        return None
    second = cited_authors[1]
    tokens = [t for t in re.split(r"[\s\-]+", second) if len(t) >= 3] or [second]
    if any(same_surname(t, n) for t in tokens for n in authors):
        return None
    return (f"the citation's second author {second} is not among the "
            f"registry's authors ({', '.join(authors[:4])})")
