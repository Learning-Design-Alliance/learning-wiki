#!/usr/bin/env python3
"""
check_evidence_markers.py — claim citations with nothing to weigh them by.

The `[±~][SMW]` marker beside a claim link is the wiki's evidence layer, and
the design-spec pipeline reads it and nothing else for evidence quality
(findings/0008, requirement 3). It is better than the frontmatter
`evidence_strength:` field in a way worth naming: strength attaches to the
*citation*, not the claim, so a claim cited `[+S]` on one page and `[~W]` on
another records a disagreement that one number per claim would flatten. And
polarity carries as much as strength — a principle citing `[-S]` is citing
strong evidence *against*, a constraint rather than support.

So a citation without a marker is a citation nothing can weigh.

    python3 scripts/check_evidence_markers.py           # ranked report
    python3 scripts/check_evidence_markers.py --full    # every occurrence

## Why this is a script and not a lint check

Measured: 11,453 of 11,697 citations outside `claims/` already carry one
(97.9%). The 244 that do not are a real backlog, and adding them to `lint.py`
would take it from 0 to permanently red — which is the property CLAUDE.md
leans on when it says a count of zero means the work is done rather than the
check being broken. `find_title_duplicates.py` sets the precedent: a known
backlog is reported, not lint-failing.

And the backlog cannot be cleared mechanically. A marker asserts a polarity
and a strength about how *this page* uses *this claim*; deriving one from the
claim's own frontmatter, or copying the majority marker other pages used,
would manufacture exactly the kind of plausible unverified detail this repo
already lost weeks to on DOIs. Each one needs somebody to read the sentence.

Links from `claims/` pages are excluded: a claim linking a claim is a
`## Related Claims` relation, not a citation, and 247 of the 491 raw
unmarked links are that.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
CITING_KINDS = ("principles", "elements", "patterns", "strategies", "theories",
                "learner-variables", "processes", "methods")

CLAIM_LINK_RE = re.compile(r"\]\(<?(?:\.\./)?(?:/)?claims/([^)>#]+?)\.md(?:#[^)>]*)?>?\)")
# [+S] [~M] [-W] — and [X] for "contradicted / discredited", which CLAUDE.md's
# evidence-tag table defines and which is a rating, not a missing one.
MARKER_RE = re.compile(r"\A[ \t]*(?:\[[+~-][SMW]\]|\[X\])")


def scan() -> list:
    """[(page, claim_slug, line_number, line_excerpt)] for unmarked citations."""
    known = {p.stem for p in (WIKI_ROOT / "claims").glob("*.md")}
    out = []
    for kind in CITING_KINDS:
        folder = WIKI_ROOT / kind
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            for m in CLAIM_LINK_RE.finditer(text):
                if m.group(1).split("/")[-1] not in known:
                    continue
                if MARKER_RE.match(text[m.end():]):
                    continue
                line_no = text.count("\n", 0, m.start()) + 1
                start = text.rfind("\n", 0, m.start()) + 1
                end = text.find("\n", m.end())
                excerpt = text[start:end if end != -1 else len(text)].strip()
                out.append((f"{kind}/{path.name}", m.group(1), line_no, excerpt))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--full", action="store_true", help="list every occurrence")
    args = ap.parse_args()

    rows = scan()
    if not rows:
        print("Every claim citation outside claims/ carries an evidence marker.")
        return

    by_page = defaultdict(list)
    for page, slug, line, excerpt in rows:
        by_page[page].append((slug, line, excerpt))

    print(f"{len(rows)} claim citation(s) across {len(by_page)} page(s) carry no "
          f"[±~][SMW] marker.\n")
    print("Each needs a person or an agent to read the sentence and say how this page "
          "uses\nthis claim — supports, qualifies or contradicts, and how strongly. It "
          "cannot be\nderived from the claim's own rating, and copying the marker other "
          "pages used for\nthe same claim would assert something nobody checked.\n")
    ranked = sorted(by_page.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    for page, items in (ranked if args.full else ranked[:20]):
        print(f"  {len(items):3}  {page}")
        for slug, line, excerpt in (items if args.full else items[:2]):
            print(f"       :{line}  {slug}")
            print(f"              {excerpt[:110]}")
    if not args.full and len(ranked) > 20:
        print(f"\n  ... and {len(ranked) - 20} more page(s). --full for every occurrence.")


if __name__ == "__main__":
    main()
