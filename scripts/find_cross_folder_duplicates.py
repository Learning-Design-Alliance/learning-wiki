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

import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

# Every content folder. Derived rather than repeated: thirteen scripts each
# kept their own copy of this list, which is how learner-variables ended up
# missing from one of them for weeks. See okf_lib.CONTENT_FOLDERS.
PAGE_TYPES = tuple(ok.CONTENT_FOLDERS)


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


# A same-named cross-link is often the CORRECT, intended wiki convention —
# an element legitimately links to the principle it enacts via its own
# "Affordances" section, e.g. — so the self-link alone is not a defect
# signal. Two earlier, broader versions of this check confirmed that the
# hard way: "any self-link" flagged 54/70 collisions (including
# constructivism and anchored-instruction, which both GLM and Sonnet agreed
# were genuinely distinct); "self-link + thin page" narrowed to 35 but still
# caught creating-visual-representations, which Sonnet's own spot-check
# reasoning called out as exactly the correct thin-but-distinct
# Affordances-link pattern, not a duplicate.
#
# What actually, uniquely marks the 3 confirmed-bad cases (just-in-time-
# learning, guided-discovery, peer-teaching) is their literal boilerplate
# description text ("... is the short-form canonical {type} for ...") from
# one specific earlier bulk-ingest batch (generated.by: codex/unspecified,
# 2026-04-08) — every page carrying that exact phrase and a same-folder
# self-link is a template stub with no real content beyond the link; no
# page confirmed genuinely-distinct by either model carries that phrase.
STUB_DESCRIPTION_MARKER = "is the short-form canonical"


def find_self_referential(collisions: dict) -> dict:
    """Among the cross-folder collisions, flag the ones where a page BOTH
    (a) carries the STUB_DESCRIPTION_MARKER boilerplate, AND (b) links to
    another folder's copy of the exact same slug — the fingerprint of the
    known-defective codex/unspecified 2026-04-08 batch's thin stubs, not a
    generic "thin page" guess (see the comment above for why that failed).

    Returns {slug: [(from_folder, to_folder), ...]} — only slugs where at
    least one such link was found on a page carrying the marker.
    """
    results = {}
    for slug, folders in collisions.items():
        self_links = []
        for from_folder in folders:
            content = (WIKI_ROOT / from_folder / f"{slug}.md").read_text(encoding="utf-8")
            if STUB_DESCRIPTION_MARKER not in content:
                continue
            for to_folder in folders:
                if to_folder == from_folder:
                    continue
                if re.search(rf"\]\(\.\./{re.escape(to_folder)}/{re.escape(slug)}\.md\)", content):
                    self_links.append((from_folder, to_folder))
        if self_links:
            results[slug] = self_links
    return results


def main() -> None:
    collisions = find_collisions()
    if not collisions:
        print("No cross-folder slug collisions found.")
        return

    self_referential = find_self_referential(collisions)
    print(f"{len(collisions)} slug(s) filed under more than one folder "
          f"({len(self_referential)} with a self-referential link — see below):\n")
    for slug, folders in collisions.items():
        marker = " [SELF-REFERENTIAL]" if slug in self_referential else ""
        print(f"- {slug}: {', '.join(folders)}{marker}")

    if self_referential:
        print(f"\n{len(self_referential)} slug(s) have a page linking to another folder's copy of itself "
              f"— a strong, deterministic duplicate signal (no LLM judgment needed):\n")
        for slug, links in self_referential.items():
            link_desc = ", ".join(f"{a} -> {b}" for a, b in links)
            print(f"- {slug}: {link_desc}")

    sys.exit(1)


if __name__ == "__main__":
    main()
