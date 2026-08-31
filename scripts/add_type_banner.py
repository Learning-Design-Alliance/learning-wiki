#!/usr/bin/env python3
"""
add_type_banner.py — Put a visible page-type banner directly under every
content page's H1, so a reader can tell at a glance which section of the
wiki they're in.

Why this is needed: 73 slugs exist in more than one type folder, and some
(cooperative-learning, direct-instruction) exist in ALL FOUR of
principles/elements/patterns/strategies. The pages are near-identically
titled, so on the rendered docs site, in GitHub's file view, in the
dashboard's edit box, and in whatever the LLM reads during an ingest, the
only thing distinguishing "the cooperative-learning PRINCIPLE" from "the
cooperative-learning STRATEGY" was the folder in the URL. Frontmatter
carries `type`, but mkdocs strips frontmatter out of the rendered page
entirely, so it's invisible exactly where it's most needed.

The banner is a blockquote, which renders as a visible callout in both
GitHub and mkdocs-material, and doubles as a link back to the section
index:

    # Cooperative Learning

    > **Principle** · [All principles](index.md)

The banner text is derived from the page's FOLDER, not its frontmatter
`type` — the banner's whole job is to answer "which section am I in",
and the folder is what actually determines that. Where the two disagree,
that's a real data bug: --check reports it, and lint.py's
check_type_banner covers it on every health run.

This duplicates `type:` from frontmatter into the body, which is the same
tradeoff CLAUDE.md already accepts for `sources:` mirroring the citations
in `## Key Sources` — a structured field and a human-readable body
rendering of the same fact, kept in sync by a lint check rather than by
one being dropped.

Idempotent: re-running updates an existing banner in place rather than
stacking a second one, so it's safe to run after any batch that created
new pages.

Usage:
    python3 scripts/add_type_banner.py --check     # report only, write nothing
    python3 scripts/add_type_banner.py --apply     # insert/update banners
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib

WIKI_ROOT = Path(__file__).parent.parent

# folder -> (singular display label, frontmatter `type` value)
TYPE_LABELS = {
    "principles": ("Principle", "principle"),
    "elements": ("Element", "element"),
    "patterns": ("Pattern", "pattern"),
    "strategies": ("Strategy", "strategy"),
    "theories": ("Theory", "theory"),
    "learner-variables": ("Learner Variable", "learner-variable"),
    "claims": ("Claim", "claim"),
}

# Matches a banner this script wrote, so a re-run updates rather than
# duplicates. Deliberately loose about the label and link text (so a
# page that moved folders, or an older banner wording, is still
# recognised and corrected) but anchored on the blockquote + bold +
# index.md link shape.
BANNER_RE = re.compile(r"^>\s*\*\*[^*]+\*\*\s*·\s*\[[^\]]*\]\(index\.md\)\s*$")


def banner_for(folder: str) -> str:
    label, _ = TYPE_LABELS[folder]
    # "All principles", "All learner variables" — lowercase the label for
    # the link text so it reads as prose, not a second heading.
    plural = folder.replace("-", " ")
    return f"> **{label}** · [All {plural}](index.md)"


def process_page(path: Path, folder: str, apply: bool) -> dict | None:
    """Insert or update the banner. Returns a record describing what
    changed (or would change), or None if the page was already correct."""
    text = path.read_text(encoding="utf-8")
    # Keep the frontmatter block VERBATIM (comments, quoting, key order and
    # all) and re-attach it on write. okf_lib.split_frontmatter's first
    # return value is a filtered list of scalar lines meant for reading,
    # not a faithful copy for round-tripping — rebuilding the page from it
    # would silently drop anything it filters. Writing back just the body
    # is worse still: it strips the frontmatter outright, which is exactly
    # what an earlier version of this script did to 3,424 pages in one run.
    fm_match = okf_lib.FRONTMATTER_RE.match(text)
    fm_prefix = text[:fm_match.end()] if fm_match else ""
    fm_lines, body = okf_lib.split_frontmatter(text)
    fm = okf_lib.parse_frontmatter_scalars(fm_lines)

    lines = body.split("\n")
    h1_idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1_idx is None:
        return {"file": f"{folder}/{path.name}", "action": "skipped",
                "detail": "no H1 heading found — left alone"}

    want = banner_for(folder)
    rel = f"{folder}/{path.name}"

    # Frontmatter `type` disagreeing with the folder the page actually
    # lives in is worth surfacing either way — the banner follows the
    # folder, so a mismatch means the frontmatter is lying about what
    # this page is.
    declared = (fm.get("type") or "").strip()
    _, expected_type = TYPE_LABELS[folder]
    type_mismatch = declared != expected_type

    # Find an existing banner: the first non-blank line after the H1.
    scan = h1_idx + 1
    while scan < len(lines) and not lines[scan].strip():
        scan += 1

    if scan < len(lines) and BANNER_RE.match(lines[scan].strip()):
        # "unchanged" rather than "updated" when the banner is already
        # right: a frontmatter/folder mismatch is worth reporting every
        # run, but it is not a change this script makes (the banner
        # follows the folder and is already correct), and calling it one
        # would make repeat runs look like they keep editing a page they
        # actually leave alone.
        action = "unchanged" if lines[scan].strip() == want else "updated"
        lines[scan] = want
    else:
        action = "inserted"
        lines[h1_idx + 1:h1_idx + 1] = ["", want]

    if action == "unchanged" and not type_mismatch:
        return None

    if apply and action != "unchanged":
        path.write_text(fm_prefix + "\n".join(lines), encoding="utf-8")

    record = {"file": rel, "action": action, "detail": want}
    if type_mismatch:
        record["detail"] += (f"  [frontmatter says type: {declared or '(missing)'}, "
                             f"but the page is in {folder}/ — expected {expected_type}]")
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Report what would change; write nothing")
    group.add_argument("--apply", action="store_true", help="Insert/update banners on disk")
    args = parser.parse_args()

    changes = []
    for folder in TYPE_LABELS:
        folder_dir = WIKI_ROOT / folder
        if not folder_dir.exists():
            continue
        for path in sorted(folder_dir.glob("*.md")):
            if path.stem == "index":
                continue
            rec = process_page(path, folder, apply=args.apply)
            if rec:
                changes.append(rec)

    inserted = sum(1 for c in changes if c["action"] == "inserted")
    updated = sum(1 for c in changes if c["action"] == "updated")
    skipped = [c for c in changes if c["action"] == "skipped"]
    mismatches = [c for c in changes if "frontmatter says type:" in c["detail"]]

    verb = "Applied" if args.apply else "Would apply"
    print(f"{verb}: {inserted} banner(s) inserted, {updated} updated, {len(skipped)} page(s) skipped.")
    if mismatches:
        print(f"\n{len(mismatches)} page(s) whose frontmatter `type` disagrees with their folder:")
        for c in mismatches[:20]:
            print(f"  - {c['file']}: {c['detail'].split('  [', 1)[1].rstrip(']')}")
        if len(mismatches) > 20:
            print(f"  ... and {len(mismatches) - 20} more")
    if skipped:
        print(f"\n{len(skipped)} page(s) skipped:")
        for c in skipped[:20]:
            print(f"  - {c['file']}: {c['detail']}")
        if len(skipped) > 20:
            print(f"  ... and {len(skipped) - 20} more")


if __name__ == "__main__":
    main()
