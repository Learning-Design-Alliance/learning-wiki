#!/usr/bin/env python3
"""
dedupe_claim_bullets.py — one bullet per claim per section.

When two claims are merged, every link to the folded claim is re-pointed to the one kept
(merge_claims.py, update_links_for_renames.py). A page that cited both then lists the same claim
twice in one section, often under the two old titles, which reads as two claims with one link
(maintainer, 2026-10-14, on principles/retrieval-practice). 294 sections carried such a pair.

For bullets that START with a link to the same claim in the same section, outside HTML comments:

- the first bullet is kept, with its marker;
- a short note on a later bullet that the first does not already carry is appended, after "; ";
- a later bullet in the same direction (+, ~ or -) contributes its stronger strength, if stronger;
  one in a different direction keeps its reading, appended as "(also cited [~M]: its note)", since a
  marker is how that page used the claim;
- bullets carrying more than a short note (prose evidence paragraphs) are reported, not touched:
  combining two paragraphs is an edit to read, not a rule to apply.

    python3 scripts/dedupe_claim_bullets.py --check
    python3 scripts/dedupe_claim_bullets.py --apply
"""
import argparse
import collections
import re
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
FOLDERS = ("principles", "patterns", "elements", "theories", "strategies", "learner-variables", "processes",
           "methods", "designs", "products", "research-methods")
BULLET = re.compile(r"^(\s*[-*] )\[([^\]]*)\]\((\.\./claims/[^)#\s]+\.md)\)\s*((?:\[[+~\-X][SMW]?\]\s*)*)(.*)$")
SHORT = 140


def note(m) -> str:
    return m.group(5).strip().lstrip("—:-– ").strip()


def dedupe(text: str):
    """(new text, merged groups, prose groups left alone)."""
    lines = text.split("\n")
    depth, sec = 0, None
    groups = collections.defaultdict(list)
    for i, ln in enumerate(lines):
        live = depth == 0
        depth = max(depth + ln.count("<!--") - ln.count("-->"), 0)
        if not live:
            continue
        if ln.startswith("## "):
            sec = i
            continue
        m = BULLET.match(ln)
        if m:
            groups[(sec, m.group(3))].append((i, m))
    drop, merged, prose = set(), 0, 0
    for (sec, target), items in groups.items():
        if len(items) < 2:
            continue
        if any(len(note(m)) > SHORT for _, m in items):
            prose += 1
            continue
        first_i, first = items[0]
        mark = first.group(4).strip()
        extra = []
        seen = {note(first).lower()} - {""}
        for i, m in items[1:]:
            n, mk = note(m), m.group(4).strip()
            if mk and mark and mk[1] != mark[1]:
                # A different direction is a different reading of the claim: keep it.
                extra.append(f"(also cited {mk}" + (f": {n})" if n else ")"))
            else:
                # Same direction: keep the stronger strength (each was already capped at the claim's
                # evidence) and any note the first bullet lacks.
                if mk and mark and "WMS".find(mk[2:3]) > "WMS".find(mark[2:3]):
                    mark = mk
                if n and n.lower() not in seen:
                    extra.append(n)
            seen.add(n.lower())
            drop.add(i)
        line = lines[first_i].rstrip()
        if mark != first.group(4).strip():
            line = line.replace(first.group(4).strip(), mark, 1)
        if extra:
            sep = "; " if note(first) else " — "
            line += sep + "; ".join(extra)
        lines[first_i] = line
        merged += 1
    return "\n".join(l for i, l in enumerate(lines) if i not in drop), merged, prose


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    tot = pages = left = 0
    for folder in FOLDERS:
        for p in sorted((WIKI_ROOT / folder).glob("*.md")):
            text = p.read_text(encoding="utf-8")
            new, merged, prose = dedupe(text)
            if prose:
                left += prose
                print(f"  prose left for a reader: {p.relative_to(WIKI_ROOT)}")
            if merged:
                tot += merged
                pages += 1
                if args.apply:
                    p.write_text(new, encoding="utf-8")
    print(f"{tot} duplicate group(s) on {pages} page(s) {'merged' if args.apply else 'to merge'}; {left} prose group(s) left")


if __name__ == "__main__":
    main()
