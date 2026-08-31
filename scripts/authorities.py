#!/usr/bin/env python3
"""
authorities.py — the human's side of the citation record.

Everything else in this repo verifies citations against Crossref, which can
only see what Crossref indexes: journal articles with DOIs. That leaves a
large hole. 2,493 of the wiki's 12,893 citations — 1,232 distinct author-year
keys — carry no DOI and no journal metadata at all. They are books, and every
check built so far is structurally blind to them. Nothing verifies that
Ambrose et al. (2010) is *How Learning Works: Seven Research-Based Principles
for Smart Teaching*, Jossey-Bass, ISBN 978-0-470-61760-1, because there is no
registry call that would say so.

A person can say so. This file is where that goes.

`sources/authorities.ndjson` is an append-only record of citations a HUMAN has
checked against the authoritative source — a publisher's page, the book in
hand, the article's own PDF. One JSON object per line, keyed by the same
author-year key check_citations.py uses:

  {"key": "ambrose-2010",
   "title": "How Learning Works: Seven Research-Based Principles for Smart Teaching",
   "publisher": "Jossey-Bass", "isbn": "978-0-470-61760-1",
   "url": "https://www.wiley.com/...", "doi": null,
   "verified": {"by": "human:david", "at": "2026-08-31"},
   "note": "Book; no DOI is registered. Any DOI asserted for this key is invented."}

Three properties make it worth having rather than just fixing the pages:

1. `"doi": null` is a *verdict*, not an absence. It says a human established
   that no DOI exists — so any DOI a future enrichment batch invents for this
   key is provably wrong and can be stripped without a lookup. A key with no
   `doi` field at all means only "not established". Conflating those two is
   the same mistake as reading a Crossref outage as a verdict.

2. It ratchets. lint.py fails on any citation that contradicts an authority,
   so a settled decision cannot be silently undone by the next model that
   writes a page. Fixing the pages alone does not survive the next batch.

3. It is the one file in this pipeline an agent must never author. The whole
   value is that a person looked at the source, so append_authority() refuses
   any actor that is not `human:<id>` — the same reason CLAUDE.md forbids an
   agent adding a `verified:` entry to a page because the page looks complete.
"""

import json
import re
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
AUTHORITIES_PATH = WIKI_ROOT / "sources" / "authorities.ndjson"

# Fields an entry may carry. `key` and `verified` are required; the rest are
# whatever the human could establish. An absent field is never treated as a
# claim about the source — only a present one is.
FIELDS = ("key", "title", "authors", "year", "doi", "isbn", "url",
          "publisher", "journal", "verified", "note")


def normalize_isbn(isbn: str) -> str:
    """Digits (and a trailing X) only, uppercased — the comparable form."""
    return re.sub(r"[^0-9Xx]", "", isbn or "").upper()


def isbn_is_valid(isbn: str) -> bool:
    """Check the ISBN-10 or ISBN-13 checksum.

    Worth doing at the point of entry: an ISBN is a long string of digits that
    is easy to mistype and impossible to eyeball, and a wrong one on a page
    reads exactly as authoritative as a right one — the same property that
    makes a wrong DOI worse than no DOI."""
    n = normalize_isbn(isbn)
    if len(n) == 10:
        if not re.fullmatch(r"\d{9}[\dX]", n):
            return False
        total = sum((10 - i) * (10 if c == "X" else int(c)) for i, c in enumerate(n))
        return total % 11 == 0
    if len(n) == 13:
        if not n.isdigit():
            return False
        total = sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(n))
        return total % 10 == 0
    return False


def validate_entry(entry: dict) -> list[str]:
    """Return a list of problems with one authority entry ([] if it is fine)."""
    problems = []
    for f in entry:
        if f not in FIELDS:
            problems.append(f"unknown field {f!r}")
    if not entry.get("key"):
        problems.append("missing 'key'")
    elif not re.fullmatch(r"[a-z][a-z'’-]*-\d{4}[a-z]?", entry["key"]):
        problems.append(f"key {entry['key']!r} is not the author-year form "
                        f"check_citations.py uses (e.g. 'ambrose-2010')")
    v = entry.get("verified") or {}
    if not v.get("by"):
        problems.append("missing 'verified.by'")
    elif not str(v["by"]).startswith("human:"):
        # See the module docstring: the file's only value is that a person
        # looked. A machine-written 'authority' is just another unverified
        # assertion wearing a badge that says otherwise.
        problems.append(f"verified.by is {v['by']!r} — an authority must be "
                        f"established by a human:<id>, never an agent")
    if not v.get("at"):
        problems.append("missing 'verified.at'")
    if entry.get("isbn") and not isbn_is_valid(entry["isbn"]):
        problems.append(f"ISBN {entry['isbn']!r} fails its checksum")
    if "doi" in entry and entry["doi"] and not entry["doi"].lower().startswith("10."):
        problems.append(f"DOI {entry['doi']!r} does not start with '10.'")
    if not any(entry.get(f) for f in ("doi", "isbn", "url")) and "doi" not in entry:
        problems.append("no identifier and no explicit \"doi\": null verdict — "
                        "the entry establishes nothing")
    return problems


def load_authorities(path: Path = AUTHORITIES_PATH) -> dict:
    """{key: entry}, later lines winning.

    Append-only, so a correction is a new line rather than an edit: the file
    keeps the history of what was believed and when, which is the point of
    every other .ndjson in this repo."""
    out: dict[str, dict] = {}
    if not path.exists():
        return out
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        try:
            entry = json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError(f"{path.name}:{lineno}: {e}") from None
        if entry.get("key"):
            out[entry["key"]] = entry
    return out


def append_authority(entry: dict, path: Path = AUTHORITIES_PATH) -> None:
    problems = validate_entry(entry)
    if problems:
        raise ValueError("; ".join(problems))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({f: entry[f] for f in FIELDS if f in entry},
                            ensure_ascii=False) + "\n")


def contradictions(entry: dict, citation: dict) -> list[str]:
    """How one citation line disagrees with its key's authority ([] if not).

    Deliberately narrow. It reports only what the authority actually states:
    an absent field is not a claim, so a citation is never faulted for
    carrying detail the human did not record. The one exception is the
    explicit `"doi": null` verdict, which IS a statement — that no DOI exists
    — and so a DOI asserted against it is a finding."""
    out = []
    line = citation.get("line", "")
    cited_doi = citation.get("doi")
    if "doi" in entry and entry["doi"] is None and cited_doi:
        out.append(f"asserts DOI {cited_doi}, but {entry['key']} is recorded as having "
                   f"no DOI"
                   + (f" ({entry['note']})" if entry.get("note") else ""))
    elif entry.get("doi") and cited_doi and cited_doi != entry["doi"].lower():
        out.append(f"asserts DOI {cited_doi}, authority says {entry['doi']}")
    if entry.get("isbn"):
        found = re.search(r"(?:ISBN[- ]?(?:1[03])?:?\s*)?((?:97[89][-\s]?)?[\d][-\s\d]{7,}[\dXx])",
                          line)
        if found and normalize_isbn(found.group(1)) not in (
                normalize_isbn(entry["isbn"]), ""):
            out.append(f"asserts ISBN {found.group(1).strip()}, authority says "
                       f"{entry['isbn']}")
    return out
