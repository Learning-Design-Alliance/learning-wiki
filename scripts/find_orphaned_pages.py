#!/usr/bin/env python3
"""
find_orphaned_pages.py — List files present on the gh-pages branch that the
current mkdocs build no longer produces.

Why this exists: docs.yml deploys with `peaceiris/actions-gh-pages` and
`keep_files: true` so production deploys don't wipe out PR preview folders
under pr-preview/ (see .github/workflows/pr-preview.yml). The trade-off is
that keep_files also preserves pages for content that's since been renamed
or deleted — they just sit on gh-pages forever instead of disappearing.
This script finds those leftovers so they can be cleaned up deliberately.

Usage:
    mkdocs build                      # produces ./site
    python3 scripts/find_orphaned_pages.py [--site-dir site] [--branch gh-pages]

Exit code is 0 whether or not orphans are found — this is a reporting tool,
not a lint gate; it should never fail a deploy.
"""

import argparse
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent

# Files/prefixes that legitimately live on gh-pages outside of a normal
# mkdocs build and should never be reported as orphaned.
IGNORE_PREFIXES = ("pr-preview/",)
IGNORE_EXACT = {".nojekyll", "CNAME"}


def gh_pages_files(branch: str) -> set[str]:
    subprocess.run(
        ["git", "fetch", "origin", branch], cwd=WIKI_ROOT, check=True, capture_output=True
    )
    # -z: NUL-separated, unquoted paths. Without it, git wraps any path containing
    # non-ASCII bytes (accented letters, curly quotes, ™, etc. — common in this wiki's
    # filenames) in a quoted, backslash-escaped string, which silently breaks any
    # prefix/equality check against a plain path like "pr-preview/".
    result = subprocess.run(
        ["git", "ls-tree", "-r", "-z", "--name-only", f"origin/{branch}"],
        cwd=WIKI_ROOT, check=True, capture_output=True,
    )
    paths = {p.decode("utf-8") for p in result.stdout.split(b"\0") if p}
    return {
        p for p in paths
        if p not in IGNORE_EXACT and not any(p.startswith(pre) for pre in IGNORE_PREFIXES)
    }


def built_files(site_dir: Path) -> set[str]:
    if not site_dir.is_dir():
        sys.exit(f"ERROR: {site_dir} not found — run `mkdocs build` first")
    return {str(p.relative_to(site_dir)) for p in site_dir.rglob("*") if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="site", help="mkdocs build output dir (default: site)")
    parser.add_argument("--branch", default="gh-pages", help="deployed branch to check (default: gh-pages)")
    args = parser.parse_args()

    deployed = gh_pages_files(args.branch)
    current = built_files(WIKI_ROOT / args.site_dir)
    orphans = sorted(deployed - current)

    if not orphans:
        print(f"No orphaned files on {args.branch} — every deployed path matches the current build.")
        return

    print(f"{len(orphans)} file(s) on {args.branch} no longer produced by the current build:\n")
    for path in orphans:
        print(f"  {path}")
    print(
        f"\nThese are most likely leftovers from renamed/deleted wiki pages — "
        f"keep_files: true (see docs.yml) means they're never automatically removed. "
        f"Delete them directly from the {args.branch} branch when convenient."
    )


if __name__ == "__main__":
    main()
