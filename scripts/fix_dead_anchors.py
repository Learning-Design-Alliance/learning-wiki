#!/usr/bin/env python3
"""
fix_dead_anchors.py — Repoint subclaim links whose anchor doesn't exist.

A claim page's subclaims cite their evidence by anchor:

    `q3 i2` Children who ... [→ Van de Pol 2019](#van-de-pol-2019)

    ## Evidence
    ### Van de Pol et al. 2019

The link text and the heading are written in the same pass by the same model,
and it routinely renders the author string two different ways — "Hart &
Risley" in the link and "Hart and Risley" in the heading, "Van de Pol 2019"
against "Van de Pol et al. 2019", "Rotton & Kelly" (which slugifies to a
*double* hyphen, `rotton--kelly-1985`) against "Rotton Kelly". The anchor then
resolves to nothing and the subclaim silently stops being traceable to the
study it summarises.

Nothing caught this: `lint.check_broken_links` splits a destination at '#'
and tests only the file part, and `mkdocs build --strict` reports a missing
anchor as INFO, which --strict does not fail on. `lint.check_dead_anchors`
now reports them; this repairs the unambiguous ones.

Two repairs, both deterministic, no guessing:

1. **The fragment is a frontmatter `sources[]` id.** CLAUDE.md's claim template
   says the evidence heading's slug becomes both the anchor and the `id` of the
   matching `sources:` entry — but the id was generated with a different
   slugify than python-markdown's, so "Gabrieli, MIT McGovern Institute" became
   the id `gabrieli-mit-mcgovern` while the real anchor is
   `gabrieli-mit-mcgovern-institute`. The `sources:` list and the `###` headings
   are parsed from each other in order, so when their counts match, index N in
   one names index N in the other and the mapping is exact.

2. **The page has exactly one evidence entry.** The rewrite fires only when the
target page's `## Evidence` section contains exactly one `###` heading — then
there is only one study the subclaim can be pointing at, and no judgment is
involved. A page with two or more evidence entries and a dead anchor is left
alone and reported: guessing which study a subclaim meant is how a claim ends
up attributed to the wrong paper, which is the same failure mode as a wrong
DOI and just as invisible once written.

Usage:
    python3 scripts/fix_dead_anchors.py --check
    python3 scripts/fix_dead_anchors.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lint
import okf_lib as ok

WIKI_ROOT = Path(__file__).parent.parent

EVIDENCE_RE = re.compile(r"^##\s+Evidence\s*$", re.M)
NEXT_H2_RE = re.compile(r"^##\s+", re.M)
H3_RE = re.compile(r"^###\s+(.+?)\s*#*\s*$", re.M)


SOURCE_ID_RE = re.compile(r"^  - id:\s*(.+?)\s*$", re.M)


def _evidence_headings(text: str) -> list[str]:
    m = EVIDENCE_RE.search(text)
    if not m:
        return []
    rest = text[m.end():]
    nxt = NEXT_H2_RE.search(rest)
    return H3_RE.findall(rest[:nxt.start()] if nxt else rest)


def source_id_anchors(text: str) -> dict[str, str]:
    """{frontmatter source id -> real heading anchor}, positionally aligned.

    Only returned when the two lists are the same length; a mismatch means the
    parse drifted and pairing them by index would attribute a subclaim to the
    wrong study."""
    fm_end = text.find("\n---", 3)
    ids = SOURCE_ID_RE.findall(text[:fm_end] if fm_end != -1 else "")
    headings = _evidence_headings(text)
    if not ids or len(ids) != len(headings):
        return {}
    return {i: lint._heading_anchor(h) for i, h in zip(ids, headings)}


def sole_or_none(text: str) -> str | None:
    headings = _evidence_headings(text)
    return lint._heading_anchor(headings[0]) if len(headings) == 1 else None


def fix_page(path: Path, apply: bool) -> tuple[list, list]:
    text = path.read_text(encoding="utf-8")
    anchors = lint.page_anchors(text)
    by_id = source_id_anchors(text)
    repairs, skipped = [], []
    replacement = None
    # Rewrite right-to-left so earlier offsets stay valid.
    for start, end, dest, _ in reversed(list(ok.iter_markdown_links(text))):
        if dest.startswith(("http://", "https://", "mailto:")) or not dest.startswith("#"):
            continue
        frag = dest[1:]
        if not frag or frag in anchors:
            continue
        new = by_id.get(frag)
        if new is None:
            if replacement is None:
                replacement = sole_or_none(text) or ""
            new = replacement
        if not new or new not in anchors:
            skipped.append(frag)
            continue
        repairs.append((frag, new))
        text = text[:start] + f"](#{new})" + text[end:]
    if apply and repairs:
        path.write_text(text, encoding="utf-8")
    return repairs, skipped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    pages = lint.all_pages()
    targets = sorted({i["file"] for i in lint.check_dead_anchors(pages)})

    fixed, all_skipped = 0, []
    for rel in targets:
        repairs, skipped = fix_page(WIKI_ROOT / rel, apply=args.apply)
        for old, new in repairs:
            print(f"  {rel}: #{old} -> #{new}")
        fixed += len(repairs)
        all_skipped += [(rel, s) for s in skipped]

    print(f"\n{'Repaired' if args.apply else 'Would repair'} {fixed} anchor(s).")
    if all_skipped:
        print(f"\n{len(all_skipped)} left for a human — the target page does not have "
              f"exactly one evidence entry, so which study is meant is a judgment call:")
        for rel, frag in all_skipped:
            print(f"  {rel}: #{frag}")


if __name__ == "__main__":
    main()
