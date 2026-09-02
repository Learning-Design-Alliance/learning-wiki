#!/usr/bin/env python3
"""
page_identity.py — stable `id:` and `aliases:` for the pages design docs point at.

The learning-design-spec pipeline resolves a design document against this wiki:
a pattern plan names `element: <slug>`, a principle names `Realizes: <slug>`, a
design section cites `research:<claim-slug>`, and `spec/learners.md` requires
every learner dimension to be a `learner-variables/` slug. Its contract
(findings/0008) opens with: *every page's id is stable and unique within its
kind* — a rename breaks a course.

Measured before this existed:

    elements    325 pages, 0 with an id
    principles  198 pages, 0 with an id
    patterns    130 pages, 0 with an id
    claims      422 pages, id: present on all of them and useless as identity —
                56 blank, only 183 of the 366 non-empty equal to the slug, and
                six values used by more than one page (we-4, se-1,
                redundancy-effect, ...). enrich.py stamps an empty `id: ` into
                every new claim, which is where the blanks come from.

So a page's identity really is its filename, and nothing says so or checks it.
`id:` is therefore set to the slug on every kind a design document can point
at, which also repurposes the claims field from the short programmatic code
CLAUDE.md documented ("we-4", "fi-2"). That code is safe to drop: it is not
unique, not always present, and referenced nowhere in the 12,893 citations —
while the design spec addresses claims by slug throughout.

`aliases:` is what makes a rename non-breaking, and it is deliberately NOT
stamped empty onto 1,076 pages. It appears when a page is actually renamed:
update_links_for_renames.py records the old slug there, so a design document
written against the old name still resolves. Empty fields on a thousand pages
are noise that trains a reader to skip the block.

    python3 scripts/page_identity.py --check     # report only
    python3 scripts/page_identity.py --apply     # write ids
    python3 scripts/page_identity.py --add-alias elements/foo.md old-slug
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent

# The kinds a design document can name.
#
# Strategies are in the list, and were nearly left out. findings/0008's
# contract names only claim, pattern, element and principle slugs, and the
# reverse index reaches strategies without naming them — so the first cut of
# this excluded them. spec/patterns.md then adds a phase field that is a
# strategy slug outright:
#
#     phases:
#       - phase: Read the case
#         element: case-based-learning
#         strategy: chunked-reading-with-embedded-questions
#
# whose `### Instructions` become the phase's brief. A strategy rename
# therefore breaks a shipped course exactly the way an element rename does,
# and 2,557 pages had no id at all.
#
# Theories stay out: nothing in the spec addresses one. A page type gains an
# id when something outside the wiki depends on pointing at it.
IDENTIFIED_TYPES = ("elements", "principles", "patterns", "claims", "learner-variables",
                    "strategies")

ID_RE = re.compile(r"^id:[ \t]*([^\n]*)$", re.M)
ALIASES_RE = re.compile(r"^aliases:[ \t]*(\[[^\]]*\])[ \t]*$", re.M)


def split_fm(text: str):
    """(frontmatter_text, rest) or (None, text) when there is no frontmatter."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[4:end + 1], text[end + 1:]


ALIASES_BLOCK_RE = re.compile(r"^aliases:[ \t]*\n((?:[ \t]+-[ \t]*[^\n]*\n?)+)", re.M)


def read_aliases(fm: str) -> list:
    """Both YAML list spellings, because both are written here.

    page_identity writes the inline form (`aliases: [a, b]`) — it edits raw
    frontmatter text and inline keeps the edit to one line. okf_lib's
    dump_frontmatter writes the block form, and ingest_extractions builds pages
    through that. A reader that understood only one would silently see no
    aliases on half the pages that have them, which is worse than not
    supporting aliases at all: the rename would look recorded and still not
    resolve."""
    fm = fm or ""
    m = ALIASES_RE.search(fm)
    if m:
        inner = m.group(1)[1:-1].strip()
        return [a.strip().strip('"\'') for a in inner.split(",") if a.strip()]
    m = ALIASES_BLOCK_RE.search(fm)
    if m:
        return [ln.strip().lstrip("-").strip().strip('"\'')
                for ln in m.group(1).splitlines() if ln.strip()]
    return []


def read_id(fm: str):
    m = ID_RE.search(fm or "")
    return m.group(1).strip().strip('"\'') if m else None


def set_id(fm: str, slug: str) -> str:
    """Set `id:` to slug, replacing whatever was there, or inserting after `type:`.

    Placed after `type:` rather than appended, so the two fields that together
    say what this page IS sit next to each other in every file."""
    if ID_RE.search(fm):
        return ID_RE.sub(f"id: {slug}", fm, count=1)
    m = re.search(r"^type:[^\n]*\n", fm, re.M)
    if m:
        return fm[:m.end()] + f"id: {slug}\n" + fm[m.end():]
    return f"id: {slug}\n" + fm


def add_alias(fm: str, alias: str) -> str:
    """Append `alias` to the page's aliases list, creating the field if absent.

    Idempotent: re-recording a rename that was already recorded is a no-op, so
    running the rename tool twice cannot produce a duplicated alias."""
    existing = read_aliases(fm)
    if alias in existing:
        return fm
    merged = "[" + ", ".join(existing + [alias]) + "]"
    if ALIASES_RE.search(fm):
        return ALIASES_RE.sub(f"aliases: {merged}", fm, count=1)
    if ALIASES_BLOCK_RE.search(fm):
        return ALIASES_BLOCK_RE.sub(f"aliases: {merged}\n", fm, count=1)
    m = ID_RE.search(fm)
    if m:
        return fm[:m.end()] + f"\naliases: {merged}" + fm[m.end():]
    return fm.rstrip("\n") + f"\naliases: {merged}\n"


def scan(types=IDENTIFIED_TYPES) -> dict:
    """{kind: [(path, slug, current_id, aliases), ...]}"""
    out = {}
    for kind in types:
        folder = WIKI_ROOT / kind
        if not folder.exists():
            continue
        rows = []
        for path in sorted(folder.glob("*.md")):
            if path.stem == "index":
                continue
            fm, _ = split_fm(path.read_text(encoding="utf-8"))
            rows.append((path, path.stem, read_id(fm), read_aliases(fm)))
        out[kind] = rows
    return out


def collisions(rows: list) -> list:
    """Every name (id or alias) claimed by more than one page in this kind.

    Aliases share the namespace with ids on purpose: a design document that
    says `element: foo` cannot tell whether foo is a current slug or a retired
    one, so if two pages answer to it the reference is ambiguous however it
    got that way."""
    owners = defaultdict(list)
    for path, slug, page_id, aliases in rows:
        for name in {page_id or slug, *aliases}:
            owners[name].append(path.name)
    return [(name, files) for name, files in sorted(owners.items()) if len(files) > 1]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    g.add_argument("--add-alias", nargs=2, metavar=("PAGE", "OLD_SLUG"),
                   help="record a retired slug on one page (what the rename tool calls)")
    args = ap.parse_args()

    if args.add_alias:
        page, old = args.add_alias
        path = WIKI_ROOT / page
        text = path.read_text(encoding="utf-8")
        fm, rest = split_fm(text)
        if fm is None:
            sys.exit(f"{page} has no frontmatter to record an alias in.")
        path.write_text("---\n" + add_alias(fm, old) + rest, encoding="utf-8")
        print(f"{page}: aliases now {read_aliases(add_alias(fm, old))}")
        return

    data = scan()
    total_written = 0
    problems = 0
    for kind, rows in data.items():
        needs = [(p, s) for p, s, i, _ in rows if i != s]
        dupes = collisions(rows)
        print(f"{kind:18} {len(rows):5} pages | {len(rows) - len(needs):5} already identified "
              f"| {len(needs):5} to set | {len(dupes)} name collision(s)")
        for name, files in dupes[:5]:
            print(f"      {name!r} claimed by {', '.join(files)}")
            problems += 1
        if args.apply:
            for path, slug in needs:
                text = path.read_text(encoding="utf-8")
                fm, rest = split_fm(text)
                if fm is None:
                    print(f"      SKIP (no frontmatter): {path.name}")
                    continue
                path.write_text("---\n" + set_id(fm, slug) + rest, encoding="utf-8")
                total_written += 1

    if args.apply:
        print(f"\nWrote id: on {total_written} page(s).")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
