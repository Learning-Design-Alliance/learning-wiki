#!/usr/bin/env python3
"""
find_cross_folder_duplicates.py — Deterministic (no LLM) scan for the same
slug filed under more than one content-type folder.

Found by accident while enriching strategies: case-based-learning.md exists
as BOTH elements/case-based-learning.md and patterns/case-based-learning.md
— two distinct, independently-written pages for the same named concept,
filed under different OKF types (same for retrieval-practice.md and
formative-assessment.md). enrich.py's repair_misfiled_links() only catches
this opportunistically, when a freshly-generated page happens to link to
that exact slug; this script scans the whole wiki proactively instead of
waiting for one to surface one broken link at a time.

This is purely a filesystem check — no API calls, no cost, safe to run as
often as you like (e.g. before/after every enrichment batch). It's a
reporting tool, not an auto-merge: per this project's convention, content
mergers (which page stays canonical, what gets folded in) are a human call
— see find_near_duplicates.py's stage 2 for the LLM-assisted version of
that judgment call, which can be pointed at these same slugs.

Usage:
    python3 scripts/find_cross_folder_duplicates.py
"""

import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories", "claims", "learner-variables")


def find_collisions() -> dict:
    """Return {slug: [page_type, ...]} for every slug that appears in more
    than one content-type folder."""
    by_slug = defaultdict(list)
    for page_type in PAGE_TYPES:
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.stem == "index":
                continue
            by_slug[path.stem].append(page_type)
    return {slug: folders for slug, folders in sorted(by_slug.items()) if len(folders) > 1}


def main() -> None:
    collisions = find_collisions()
    if not collisions:
        print("No cross-folder slug collisions found.")
        return
    print(f"{len(collisions)} slug(s) filed under more than one folder:\n")
    for slug, folders in collisions.items():
        print(f"- {slug}: {', '.join(folders)}")
    sys.exit(1)


if __name__ == "__main__":
    main()
