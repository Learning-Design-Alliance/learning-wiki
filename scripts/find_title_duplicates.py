#!/usr/bin/env python3
"""
find_title_duplicates.py — Deterministic same-folder near-duplicate detection.
No API calls.

The wiki had two dedup checks and a hole between them:

  find_cross_folder_duplicates.py catches the SAME SLUG in different type
  folders. It cannot see two differently-named pages in one folder.

  find_near_duplicates.py catches same-folder near-duplicates properly, but
  even its Stage 1 (just proposing candidates) is an LLM call, so
  wiki_health_check.py deliberately never runs it — "costs real API calls
  and needs a human or Sonnet-level judgment call per candidate, not
  something to fire unattended on a schedule."

The consequence: principles/competency-based-assessment.md and
principles/competency-based-learning-assessment.md sat side by side, both
status: review, and no automated check could ever have reported them.

Proposing candidates does not need a model. Two titles sharing most of
their significant words is a deterministic string fact. This script
computes it for free, so the LLM stage (find_near_duplicates.py) is spent
only on the judgment call it is actually needed for: are these the same
practice, and which page should survive?

Deliberately a reporting tool, not a lint failure and not an auto-merge.
It finds 943 candidate pairs across the wiki as written — mostly
hyphen-vs-underscore variants of one page from two ingest conventions —
which is a backlog to work through, not a reason to block CI. Merging
content stays a human call, per this project's convention.

Usage:
    python3 scripts/find_title_duplicates.py
    python3 scripts/find_title_duplicates.py --type principles
    python3 scripts/find_title_duplicates.py --threshold 0.8
    python3 scripts/find_title_duplicates.py --out report.md
"""

import argparse
import itertools
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
PAGE_TYPES = ("principles", "elements", "patterns", "strategies", "theories",
              "learner-variables", "claims", "processes", "methods")

_STOP = {"the", "and", "of", "in", "a", "an", "for", "on", "to", "with", "from",
         "how", "what", "when", "does", "by", "as", "at"}

# A word this common carries no signal about whether two pages are the same
# page; comparing every pair that shares it would be quadratic for nothing.
_UBIQUITOUS_MIN = 60


def _tokens(text: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower())
            if w not in _STOP and len(w) > 2}


def _title(path: Path) -> str:
    m = re.search(r"^title:\s*\"?(.+?)\"?\s*$", path.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else path.stem.replace("_", " ").replace("-", " ")


def find_pairs(folder: str, threshold: float = 0.6) -> list:
    """[(score, path_a, path_b)] for same-folder pages whose titles overlap by
    at least `threshold` (Jaccard over significant words), highest first."""
    d = WIKI_ROOT / folder
    if not d.exists():
        return []
    pages = [(p, _tokens(_title(p))) for p in sorted(d.glob("*.md")) if p.stem != "index"]

    # Invert to token -> page ids so only pages sharing a word are compared.
    index = defaultdict(list)
    for i, (_, toks) in enumerate(pages):
        for w in toks:
            index[w].append(i)

    seen, pairs = set(), []
    for w, ids in index.items():
        if len(ids) > _UBIQUITOUS_MIN:
            continue
        for a, b in itertools.combinations(ids, 2):
            if (a, b) in seen:
                continue
            seen.add((a, b))
            ta, tb = pages[a][1], pages[b][1]
            if not ta or not tb:
                continue
            score = len(ta & tb) / len(ta | tb)
            if score >= threshold:
                pairs.append((score, pages[a][0], pages[b][0]))
    pairs.sort(key=lambda x: -x[0])
    return pairs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--type", choices=PAGE_TYPES, default=None)
    ap.add_argument("--threshold", type=float, default=0.6,
                    help="Minimum title-word overlap, 0-1 (default 0.6)")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    folders = (args.type,) if args.type else PAGE_TYPES
    lines, total = [], 0
    for folder in folders:
        pairs = find_pairs(folder, args.threshold)
        total += len(pairs)
        lines.append(f"\n## {folder} — {len(pairs)} candidate pair(s)\n")
        for score, a, b in pairs:
            lines.append(f"- `{score:.2f}` {a.name} ⇄ {b.name}")
    header = (f"# Near-duplicate title candidates\n\n{total} pair(s) at overlap "
              f">= {args.threshold}. Deterministic title comparison only — confirm with "
              f"`find_near_duplicates.py` or by reading the pages before merging anything.\n")
    report = header + "\n".join(lines)

    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Wrote {total} candidate pair(s) to {args.out}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
