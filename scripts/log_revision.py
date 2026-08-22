#!/usr/bin/env python3
"""
log_revision.py — Append a revision card to revisions/{slug}.md and update
                  the page's frontmatter (last_edited, edited_by).

Usage:
    python3 scripts/log_revision.py <page-path> \
        --by "David Porcaro" \
        --type "content" \
        --desc "Added claims we-1 through we-5 with evidence tags"

    python3 scripts/log_revision.py principles/worked-examples.md \
        --by "Claude" \
        --type "ingest" \
        --desc "Initial ingest from research_briefs CSV"

Change types:
    ingest      Initial import from a source (CSV, paper, etc.)
    content     Added or rewrote substantive content
    claim       Added, updated, or linked a claim
    source      Added or corrected a source citation
    structure   Changed section headers or page schema
    status      Changed page status (draft → review → stable)
    correction  Fixed an error
    deprecate   Marked content as deprecated
"""

import re
import sys
import argparse
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

WIKI_ROOT = Path(__file__).parent.parent
TODAY = date.today().isoformat()


def get_slug_and_type(page_path: Path) -> tuple[str, str]:
    """Return (slug, page_type) from a path relative to wiki root."""
    rel = page_path.relative_to(WIKI_ROOT)
    parts = rel.parts
    if len(parts) == 2:
        return parts[1].replace(".md", ""), parts[0]
    return rel.stem, "unknown"


def update_frontmatter(page_path: Path, editor: str):
    """Update the page's OKF `generated: {by, at}` field to record this edit."""
    text = page_path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return  # no frontmatter

    fm = parts[1]
    body = parts[2]
    actor = ok.actor_for(editor)

    if re.search(r"^generated:\s*$", fm, re.MULTILINE):
        fm = re.sub(r"generated:\s*\n(\s+by:.*\n\s+at:.*\n)",
                     f"generated:\n  by: {ok.yaml_escape(actor)}\n  at: {TODAY}\n", fm)
    else:
        fm = fm.rstrip() + f"\ngenerated:\n  by: {ok.yaml_escape(actor)}\n  at: {TODAY}\n"

    page_path.write_text(f"---{fm}---{body}", encoding="utf-8")


def add_verified(page_path: Path, editor: str):
    """Append a `verified: {by, at}` confirmation event to the page's frontmatter.
    Only call this for a substantive human (or agent) review of the page's accuracy —
    never automatically, and never just because a page looks complete."""
    text = page_path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        return
    fm, body = parts[1], parts[2]
    actor = ok.actor_for(editor)
    fm = ok.add_verified_entry(fm, actor, TODAY)
    page_path.write_text(f"---{fm}---{body}", encoding="utf-8")


def append_revision_card(slug: str, page_type: str, editor: str, change_type: str, description: str):
    """Create or append to revisions/{slug}.md."""
    revisions_dir = WIKI_ROOT / "revisions"
    revisions_dir.mkdir(exist_ok=True)

    rev_path = revisions_dir / f"{slug}.md"
    rel_link = ok.to_relative(f"/{page_type}/{slug}.md", "revisions")  # ../<page_type>/<slug>.md

    card = f"""
### {TODAY} · {change_type} · {editor}
{description}
"""

    if not rev_path.exists():
        header = f"""---
type: revisions
page: {rel_link}
---

# Revision history: [{page_type}/{slug}]({rel_link})

"""
        rev_path.write_text(header + card.lstrip(), encoding="utf-8")
    else:
        existing = rev_path.read_text(encoding="utf-8")
        rev_path.write_text(existing + card, encoding="utf-8")


def append_wiki_log(page_type: str, slug: str, change_type: str, description: str):
    """Append a bullet to log.md under today's OKF date-grouped '## YYYY-MM-DD' section."""
    rel_link = ok.to_relative(f"/{page_type}/{slug}.md", None)  # log.md lives at the wiki root
    bullet = f"* **{change_type.capitalize()}**: [{page_type}/{slug}]({rel_link}) — {description}"
    ok.append_log_entries([bullet])


def main():
    parser = argparse.ArgumentParser(description="Log a revision card for a wiki page")
    parser.add_argument("page", help="Path to page (e.g. principles/worked-examples.md)")
    parser.add_argument("--by", default="unknown", help="Editor name or 'Claude'")
    parser.add_argument(
        "--type",
        choices=["ingest", "content", "claim", "source", "structure", "status", "correction", "deprecate"],
        default="content",
        help="Type of change",
    )
    parser.add_argument("--desc", required=True, help="One-line change description")
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Also append a verified: {by, at} entry — use only for a substantive review "
             "of the page's accuracy, e.g. by a human reviewer approving a PR, never just "
             "because the page looks complete",
    )
    args = parser.parse_args()

    page_path = WIKI_ROOT / args.page
    if not page_path.exists():
        print(f"ERROR: {page_path} not found")
        sys.exit(1)

    slug, page_type = get_slug_and_type(page_path)

    update_frontmatter(page_path, args.by)
    if args.verify:
        add_verified(page_path, args.by)
    append_revision_card(slug, page_type, args.by, args.type, args.desc)
    append_wiki_log(page_type, slug, args.type, args.desc)

    print(f"Logged revision: {page_type}/{slug}")
    print(f"  Revision card: revisions/{slug}.md")
    print(f"  Frontmatter updated: generated.by={ok.actor_for(args.by)}, generated.at={TODAY}")
    if args.verify:
        print(f"  verified entry added: by={ok.actor_for(args.by)}, at={TODAY}")
    print(f"  log.md updated: {TODAY}")


if __name__ == "__main__":
    main()
