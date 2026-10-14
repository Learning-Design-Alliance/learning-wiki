#!/usr/bin/env python3
"""
repoint_revision_cards.py — move a renamed, re-filed or merged page's revision card to the page it
became.

A card is revisions/<slug>.md, found by log_revision.py by the page's slug, with `page:` naming the
page it records. When a page is renamed, re-filed into another kind or merged, update_links_for_
renames.py re-points the link in the card's heading to the page it became, but nothing updated the
`page:` field or moved the file. On 2026-10-13, 1,877 cards named a page that no longer existed; every
one had a living successor in its heading link. Left alone, the next log_revision.py run on the
successor starts a fresh card and the page's history before the move is lost to anyone reading it.

For each such card, the successor is its heading link:

- no card exists for the successor (log_revision.card_path: revisions/<slug>.md, or
  revisions/<kind>--<slug>.md where another kind's page already holds that name): the card moves there, `page:` and the heading
  name the successor, and a line records the page it was before;
- a card exists there already: the stale card's entries are appended to it under
  "## Earlier history as <old page>", and the stale card is removed.

Nothing is deleted from the history: every entry ends up on the card of the page it describes now.

    python3 scripts/repoint_revision_cards.py --check
    python3 scripts/repoint_revision_cards.py --apply
"""
import argparse
import collections
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from log_revision import card_path  # noqa: E402  the same card a later log_revision.py run will append to
CARDS = WIKI_ROOT / "revisions"
PAGE_RE = re.compile(r"^page:\s*\.\./(\S+)\s*$", re.M)
HEAD_RE = re.compile(r"^# Revision history: \[[^\]]*\]\(\.\./([^)#\s]+)\)\s*$", re.M)


def stale_cards() -> list:
    out = []
    for card in sorted(CARDS.glob("*.md")):
        text = card.read_text(encoding="utf-8")
        m = PAGE_RE.search(text)
        if not m or (WIKI_ROOT / m.group(1)).exists():
            continue
        h = HEAD_RE.search(text)
        succ = h.group(1) if h else None
        if succ and succ != m.group(1) and (WIKI_ROOT / succ).exists():
            out.append((card, m.group(1), succ))
        else:
            out.append((card, m.group(1), None))
    return out


def entries(text: str) -> str:
    """Everything after the heading line: the revision entries."""
    h = HEAD_RE.search(text)
    return text[h.end():].strip("\n") if h else text.split("---", 2)[-1].strip("\n")


def run(apply: bool) -> None:
    stale = stale_cards()
    counts = collections.Counter()
    # Several stale cards may lead to one successor; process them one at a time so the first
    # becomes the successor's card and the rest fold into it.
    for card, old, succ in stale:
        if succ is None:
            counts["no successor (left alone)"] += 1
            continue
        kind, slug = succ[:-3].split("/", 1)
        target = card_path(kind, slug)
        text = card.read_text(encoding="utf-8")
        if target.exists() and target != card:
            counts["folded into the successor's card"] += 1
            if apply:
                kept = target.read_text(encoding="utf-8").rstrip("\n")
                kept += f"\n\n## Earlier history as {old[:-3]}\n\n{entries(text)}\n"
                target.write_text(kept, encoding="utf-8")
                subprocess.run(["git", "rm", "-q", "-f", str(card)], cwd=WIKI_ROOT, check=True)
        else:
            counts["moved to the successor"] += 1
            if apply:
                text = PAGE_RE.sub(f"page: ../{succ}", text, count=1)
                text = HEAD_RE.sub(lambda m: f"# Revision history: [{succ[:-3]}](../{succ})\n\n"
                                             f"Recorded as {old[:-3]} before it was renamed, re-filed or merged.\n\n",
                                   text, count=1)
                if target != card:
                    subprocess.run(["git", "mv", str(card), str(target)], cwd=WIKI_ROOT, check=True)
                target.write_text(text, encoding="utf-8")
    for k, v in counts.most_common():
        print(f"  {v:5}  {k}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)


if __name__ == "__main__":
    main()
