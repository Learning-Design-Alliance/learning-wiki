#!/usr/bin/env python3
"""
verify_citation_edits.py — did a citation tool edit only citations?

Run this after resolve_citation_metadata.py, standardize_citations.py or
apply_authorities.py writes, and before committing. It reads a diff and
reports every changed line that is not a citation line — which is the shape
every data-corruption bug in this pipeline has had:

  * strip_doi_from_line matched a DOI anywhere in the file, so a page citing
    one work rightly and another wrongly under the same DOI lost both.
  * apply_authorities stripped file-wide and did the same.
  * fix_title rewrote any line mentioning the DOI. It overwrote a frontmatter
    YAML key with a paper's title, and replaced a whole prose paragraph on
    strategies/explicit_instruction-spelling.md with a registry title, taking
    the sentence and the opening of a markdown link with it.

All three shipped. None was caught by lint.py, mkdocs or review, because the
results are valid YAML, valid markdown and plausible prose — the damage is
only visible as "this edit landed somewhere an edit had no business landing".
That is exactly what this checks, and it is a property of the *diff*, which
is why no page-level check can see it.

    python3 scripts/standardize_citations.py --apply
    python3 scripts/verify_citation_edits.py          # before you commit
    python3 scripts/verify_citation_edits.py --base origin/main

Exit status is 1 if any edit landed off a citation line. This is a guard for
tool runs, NOT a lint check: a human editing prose will and should trip it.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc

CONTENT = re.compile(r"^(" + "|".join(cc.PAGE_TYPES) + r")/")


def changed_pairs(diff: str):
    """(path, old_line, new_line) for each modified line in a content page.

    Pairs positionally within a hunk, which is how git presents a
    single-line-per-citation rewrite — the only shape these tools produce.
    A pure insertion or deletion has no counterpart and is yielded with None,
    so it is reported rather than silently skipped."""
    for f in re.split(r"^diff --git ", diff, flags=re.M)[1:]:
        path = f.split(" b/")[0][2:]
        if not CONTENT.match(path):
            continue
        for hunk in re.split(r"^@@", f, flags=re.M)[1:]:
            old = [l[1:] for l in hunk.splitlines()
                   if l.startswith("-") and not l.startswith("---")]
            new = [l[1:] for l in hunk.splitlines()
                   if l.startswith("+") and not l.startswith("+++")]
            for i in range(max(len(old), len(new))):
                yield (path,
                       old[i] if i < len(old) else None,
                       new[i] if i < len(new) else None)


def is_citation(line) -> bool:
    return bool(line) and bool(cc.CITATION_KEY_RE.search(line.strip()))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=None,
                    help="compare against this ref instead of the working tree's "
                         "uncommitted changes (e.g. origin/main)")
    args = ap.parse_args()

    cmd = ["git", "diff"] + ([f"{args.base}...HEAD"] if args.base else [])
    diff = subprocess.run(cmd, capture_output=True, text=True,
                          cwd=Path(__file__).parent.parent).stdout
    if not diff.strip():
        print("No changes to check.")
        return

    ok, bad = 0, []
    for path, old, new in changed_pairs(diff):
        # An edit is safe when it lands on a citation and leaves it one. A
        # rewrite that turns a citation into something that no longer parses
        # as one has destroyed it just as surely as one that hit prose.
        if is_citation(old) and is_citation(new):
            ok += 1
        else:
            bad.append((path, old, new))

    print(f"{ok} edit(s) landed on a citation line.")
    if not bad:
        print("Nothing landed anywhere else.")
        return

    print(f"\n{len(bad)} edit(s) did NOT — every one needs eyes before you commit:\n")
    for path, old, new in bad:
        print(f"  {path}")
        print(f"     was: {(old or '(line added)').strip()[:130]}")
        print(f"     now: {(new or '(line deleted)').strip()[:130]}\n")
    print("If you edited prose by hand, this is expected. If a script wrote these,\n"
          "it matched a DOI rather than a citation — see the module docstring.")
    sys.exit(1)


if __name__ == "__main__":
    main()
