#!/usr/bin/env python3
"""
fix_links.py — Repair local markdown links that don't actually work.

Two defects, both invisible to the old regex-based link check and both
producing links that render as dead literal text on the docs site:

1. **Parens in the destination.** A page whose filename contains parentheses
   — strategies/project-based_learning_(pbl).md, academic_choice_(planning,
   _working,_reflecting).md — cannot be linked with a bare destination: the
   markdown parser closes the destination at the first ')'. mkdocs reports
   these as "unrecognized relative link ... left as is" (an INFO, so
   `--strict` does not catch them) and emits no working link. Fixed by
   wrapping the destination in <...>, CommonMark's form for exactly this.

2. **Missing .md extension.** "../principles/chunking" instead of
   "../principles/chunking.md". mkdocs says "Did you mean ...chunking.md?"
   and leaves the link inert. Fixed by appending .md when that makes the
   target resolve.

Anything still unresolved after both repairs is reported for a human — a
link to a page that genuinely doesn't exist is a content decision (create
the page, repoint the link, or drop it), not something to guess at.

Usage:
    python3 scripts/fix_links.py --check     # report only
    python3 scripts/fix_links.py --apply     # rewrite
"""

import argparse
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

WIKI_ROOT = Path(__file__).parent.parent
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories",
              "learner-variables", "claims", "processes", "methods")


def _resolves(page: Path, dest: str) -> bool:
    target = urllib.parse.unquote(dest.split("#")[0])
    if not target:
        return True          # pure anchor link
    return (page.parent / target).exists()


def fix_page(path: Path, apply: bool) -> tuple[list, list]:
    """Returns (repairs, unresolved) for one page."""
    text = path.read_text(encoding="utf-8")
    repairs, unresolved = [], []
    # Rewrite right-to-left so earlier offsets stay valid.
    for start, end, dest, is_angle in reversed(list(ok.iter_markdown_links(text))):
        if dest.startswith(("http://", "https://", "#", "mailto:")):
            continue
        new = None
        if _resolves(path, dest):
            # Works on disk — but if it carries parens un-angled, markdown
            # still can't parse it.
            if ok.link_needs_angle_brackets(dest) and not is_angle:
                new = f"<{dest}>"
        elif not dest.endswith(".md") and _resolves(path, dest + ".md"):
            new = f"<{dest}.md>" if ok.link_needs_angle_brackets(dest) else f"{dest}.md"
        else:
            unresolved.append(dest)
            continue
        if new is None:
            continue
        repairs.append((dest, new))
        text = text[:start] + f"]({new})" + text[end:]
    if apply and repairs:
        path.write_text(text, encoding="utf-8")
    return repairs, unresolved


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    total_repairs, all_unresolved = 0, []
    for folder in PAGE_TYPES:
        d = WIKI_ROOT / folder
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            if p.stem == "index":
                continue
            repairs, unresolved = fix_page(p, apply=args.apply)
            total_repairs += len(repairs)
            all_unresolved += [(str(p.relative_to(WIKI_ROOT)), u) for u in unresolved]

    verb = "Repaired" if args.apply else "Would repair"
    print(f"{verb} {total_repairs} link(s).")
    if all_unresolved:
        print(f"\n{len(all_unresolved)} link(s) point at a target that does not exist "
              f"— these need a human decision:")
        for f, u in all_unresolved:
            print(f"  {f}: {u}")


if __name__ == "__main__":
    main()
