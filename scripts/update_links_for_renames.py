#!/usr/bin/env python3
"""
update_links_for_renames.py — After pages are renamed, re-point every inbound
cross-link at the new filename.

Why this exists: renaming a page is two jobs, and `git mv` only does the first.
Nothing else in the wiki updates the pages that link to the one you moved.

This is not hypothetical. Two independent slug-normalisation efforts ran against
this wiki at once. One (a984820f on the scraper branch) renamed 192 files and did
update the links in its own tree. The other (162 renames on
claude/ecstatic-mclaren-43fb6c) did not, and looked clean anyway — lint there
reports zero broken links, because that tree sits 101 commits behind and indexes
2035 pages against this tree's 3599, so most of the pages that link to the old
names do not exist there yet.

The failure mode is a rename that is correct in its own tree and breaks links
only once merged forward. It happened here: merging the scraper branch orphaned
17 links to `a_finder's_guide_to_facts.md`, which that branch had renamed to
`a_finders_guide_to_facts.md` — links this branch had itself repaired one commit
earlier. This script re-pointed all 17 from a one-line rename map.

So: whoever renames chooses the names, and this closes the gap they leave. It
does not rename anything and has no opinion about what a good slug is.

Link forms handled, for each renamed page:

    ](old.md)                     same-folder link
    ](../folder/old.md)           cross-folder link (the wiki's normal form)
    ](/folder/old.md)             bundle-root-absolute (OKF permits it)
    ](%27old%27.md)               percent-encoded punctuation, which models emit
                                  for slugs containing ' " ? , ( ) & +

Rewrites are anchored on `](...)` so a bare filename mentioned in prose is left
alone, and every rewrite is verified to resolve on disk before being kept — a
pass can never turn a working link into a broken one.

Usage:
    # take the rename map from renames already staged in git (git mv / git add)
    python3 scripts/update_links_for_renames.py --from-git --dry-run
    python3 scripts/update_links_for_renames.py --from-git --apply

    # or from an explicit map: one "old<TAB>new" pair per line, bundle-relative
    python3 scripts/update_links_for_renames.py --map renames.tsv --apply

Run `python3 scripts/lint.py --type broken_links` afterwards to confirm.
"""

import argparse
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib

WIKI_ROOT = Path(__file__).parent.parent

# Punctuation that appears literally in this wiki's filenames and that models
# percent-encode on the way out. Kept as an explicit table rather than calling
# urllib.parse.quote so the set stays visible and reviewable.
ENCODABLE = "'\"?,()&+ "


def rename_map_from_git() -> dict:
    """Read staged renames out of `git status --porcelain -z`.

    With -z a rename is emitted as "R  <new>\\0<old>\\0", so the pair has to be
    read two entries at a time; the non-z form quotes and arrow-joins paths,
    which is unparseable for filenames that themselves contain quotes and
    spaces — and many of these do.
    """
    out = subprocess.run(
        ["git", "-C", str(WIKI_ROOT), "status", "--porcelain", "-z"],
        capture_output=True, text=True, check=True).stdout
    parts = out.split("\0")
    renames = {}
    i = 0
    while i < len(parts):
        entry = parts[i]
        if not entry:
            i += 1
            continue
        if entry[:1] in ("R", "C") or entry[1:2] in ("R", "C"):
            new, old = entry[3:], parts[i + 1]
            renames[old] = new
            i += 2
        else:
            i += 1
    return renames


def rename_map_from_file(path: Path) -> dict:
    renames = {}
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if "\t" not in line:
            sys.exit(f"{path}:{n}: expected 'old<TAB>new', got: {line!r}")
        old, new = line.split("\t", 1)
        renames[old.strip()] = new.strip()
    return renames


def link_variants(old_path: str, from_folder: str) -> list:
    """Every way a page in `from_folder` might spell a link to `old_path`.

    `from_folder` is "" for a page at the bundle root (index.md, log.md), where
    the correct form is "folder/slug.md" with no "../" prefix — log.md's own
    entries were left broken by an earlier version of this that always prefixed.
    """
    folder, _, basename = old_path.partition("/")
    forms = [f"/{folder}/{basename}"]
    if from_folder:
        forms.append(f"../{folder}/{basename}")
        if folder == from_folder:
            forms.append(basename)
    else:
        forms.append(f"{folder}/{basename}")
    # percent-encoded spellings of each form
    encoded = []
    for f in forms:
        e = "".join(
            f"%{ord(c):02X}" if c in ENCODABLE else c for c in f)
        if e != f:
            encoded.append(e)
        lower = "".join(
            f"%{ord(c):02x}" if c in ENCODABLE else c for c in f)
        if lower != f and lower != e:
            encoded.append(lower)
    return forms + encoded


def new_link_for(new_path: str, from_folder: str) -> str:
    folder, _, basename = new_path.partition("/")
    if not from_folder:                 # page at the bundle root
        return f"{folder}/{basename}"
    return basename if folder == from_folder else f"../{folder}/{basename}"


def all_pages() -> list:
    pages = []
    for folder in okf_lib.CONTENT_FOLDERS + ["revisions", "sources", "."]:
        d = WIKI_ROOT / folder
        if not d.is_dir():
            continue
        pages.extend(sorted(p for p in d.glob("*.md")))
    return pages


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--from-git", action="store_true",
                     help="derive the rename map from renames staged in git")
    src.add_argument("--map", type=Path, help="file of 'old<TAB>new' bundle-relative pairs")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="report without writing (default)")
    mode.add_argument("--apply", action="store_true", help="write the rewrites")
    args = ap.parse_args()

    renames = rename_map_from_git() if args.from_git else rename_map_from_file(args.map)
    renames = {o: n for o, n in renames.items() if o.endswith(".md") and o != n}
    if not renames:
        print("No renames found — nothing to re-point.")
        return 0
    print(f"Rename map: {len(renames)} page(s)\n")

    rewritten, skipped, touched = 0, [], {}
    for page in all_pages():
        try:
            text = original = page.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        from_folder = page.parent.name if page.parent != WIKI_ROOT else ""
        for old_path, new_path in renames.items():
            replacement = new_link_for(new_path, from_folder)
            # Never keep a rewrite that does not resolve: guarantees this pass
            # cannot convert a working link into a broken one.
            if not (page.parent / replacement).resolve().is_file():
                continue
            for variant in link_variants(old_path, from_folder):
                # Both spellings: bare, and the <...> form lint requires for a
                # target containing parentheses. Old names here routinely have
                # them ("academic_choice_(planning,_working,_reflecting).md").
                for needle in (f"]({variant})", f"](<{variant}>)"):
                    if needle not in text:
                        continue
                    n = text.count(needle)
                    text = text.replace(needle, f"]({replacement})")
                    rewritten += n
                    touched.setdefault(str(page.relative_to(WIKI_ROOT)), 0)
                    touched[str(page.relative_to(WIKI_ROOT))] += n
        if text != original and args.apply:
            page.write_text(text, encoding="utf-8")

    for f, n in sorted(touched.items()):
        print(f"  {f}  ({n})")
    verb = "Rewrote" if args.apply else "Would rewrite"
    print(f"\n{verb} {rewritten} link(s) across {len(touched)} page(s).")
    if not args.apply:
        print("Dry run — nothing written. Re-run with --apply.")
    else:
        print("Now run: python3 scripts/lint.py --type broken_links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
