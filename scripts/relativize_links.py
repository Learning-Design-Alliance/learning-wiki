#!/usr/bin/env python3
"""
relativize_links.py — One-time pass converting every bundle-root-absolute cross-link
(`/folder/slug.md`) in the wiki to a relative path (`slug.md` / `../folder/slug.md`).

Why: OKF allows either absolute-bundle-relative or relative markdown links. Absolute
form works fine on GitHub and in plain markdown viewers, but plain mkdocs (without a
link-rewriting plugin) renders `/folder/slug.md` as a literal domain-root path, which
404s once the site is hosted under a subpath. Relative links work everywhere with no
extra plugin, so migrate_to_okf.py's initial conversion is followed by this pass.

Every content folder is exactly one level deep, so the relative form is mechanical:
see okf_lib.to_relative().

Usage:
    python3 scripts/relativize_links.py [--dry-run]
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok


def process(path: Path, from_folder, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    new_text = ok.relativize_links(text, from_folder)
    if new_text == text:
        return False
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    changed = 0
    total = 0

    for folder in ok.CONTENT_FOLDERS + ["sources"]:
        d = ok.WIKI_ROOT / folder
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            total += 1
            from_folder = folder  # index.md counts as living in its own folder too
            if process(p, from_folder, args.dry_run):
                changed += 1

    for name in ("index.md", "log.md", "CLAUDE.md", "README.md"):
        p = ok.WIKI_ROOT / name
        if p.exists():
            total += 1
            if process(p, None, args.dry_run):
                changed += 1

    print(f"{'Would change' if args.dry_run else 'Changed'} {changed}/{total} files.")


if __name__ == "__main__":
    main()
