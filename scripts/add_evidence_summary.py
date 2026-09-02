#!/usr/bin/env python3
"""
add_evidence_summary.py — put a claim's evidence weight in its header.

A claim page states its weight twice, and both are below the fold: `q3 i2`
prefixes under `## Subclaims`, and a codes line under each `## Evidence`
entry. To learn what a claim rests on you had to scroll and parse. An agent
resolving `research:<claim-slug>` wants that in one look, and so does a reader.

So a second banner line goes directly under the type banner:

    # Example–problem sequences reduce cognitive load…

    > **Claim** · [All claims](index.md)
    > **Evidence** · 1 study · `q3` peer-reviewed experiment · `i2` medium · n=48

Body content rather than a rendered-only hook, deliberately: an agent reading
the repository file sees exactly what a reader on the docs site sees. That is
the same tradeoff the type banner already accepts — derived data duplicated
into the body, kept honest by a script and a lint check rather than by
dropping one copy.

## What it does NOT do

It never collapses the evidence into a single verdict. `evidence_strength:`
already tried that and produced nineteen spellings across 422 pages, and
findings/0008 is explicit that a per-claim number flattens exactly what the
per-citation codes preserve. So a claim resting on studies coded q2 and q4
reports `q2–q4`, not "moderate". The range is derived; a verdict would be
invented.

## Absence is stated, not implied

A claim with no coded evidence gets `> **Evidence** · none recorded yet`
rather than no line at all. 313 of the 422 claim pages are stubs with an
empty `## Evidence`, and "no line" cannot be told apart from "the script
never ran here" — the same distinction this repo keeps between a Crossref
outage and a Crossref verdict.

    python3 scripts/add_evidence_summary.py --check
    python3 scripts/add_evidence_summary.py --apply
"""

import argparse
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib

SCALES_PATH = WIKI_ROOT / "evidence-scales.json"
SUMMARY_RE = re.compile(r"^>\s*\*\*Evidence\*\*\s*·.*$")
BANNER_RE = re.compile(r"^>\s*\*\*[^*]+\*\*\s*·\s*\[[^\]]*\]\(index\.md\)\s*$")


def _labels():
    d = json.loads(SCALES_PATH.read_text(encoding="utf-8"))
    return ({t["code"]: t["label"] for t in d["quality"]["tiers"]},
            {t["code"]: t["label"] for t in d["impact"]["tiers"]})


def summary_line(sources: list) -> str:
    """The `> **Evidence** · …` line for one claim's evidence entries.

    Reads the same `sources[]` q/i/n that sync_evidence_codes.py mirrors out
    of the body, so the header cannot disagree with the entries it summarises
    — there is one parse, not two."""
    q_lab, i_lab = _labels()
    coded = [s for s in sources if isinstance(s, dict) and ("q" in s or "i" in s)]
    if not coded:
        return "> **Evidence** · none recorded yet"

    parts = [f"{len(coded)} stud{'y' if len(coded) == 1 else 'ies'}"]

    def rng(field, labels):
        vals = [s[field] for s in coded if isinstance(s.get(field), int)]
        if not vals:
            return None
        lo, hi = min(vals), max(vals)
        if lo == hi:
            # One tier across the evidence: name it, since the label is the
            # part a reader actually wants and there is no ambiguity to hide.
            return f"`{field}{lo}` {labels.get(lo, '')}".strip()
        # A spread is reported as a spread. Averaging two studies coded q2 and
        # q4 into "q3" would assert a tier neither study has.
        return f"`{field}{lo}`–`{field}{hi}`"

    for field, labels in (("q", q_lab), ("i", i_lab)):
        r = rng(field, labels)
        if r:
            parts.append(r)

    ns = [str(s["n"]) for s in coded if s.get("n")]
    if len(ns) == 1:
        parts.append(f"n={ns[0]}")
    return "> **Evidence** · " + " · ".join(parts)


def process(path: Path, apply: bool):
    text = path.read_text(encoding="utf-8")
    # Frontmatter kept VERBATIM and re-attached — see the long note in
    # add_type_banner.process_page for what happens when it is not.
    fm_match = okf_lib.FRONTMATTER_RE.match(text)
    fm_prefix = text[:fm_match.end()] if fm_match else ""
    fm_lines, body = okf_lib.split_frontmatter(text)

    section = okf_lib.get_section(body, "Evidence")
    sources = okf_lib.parse_evidence_sources(section) if section else []
    want = summary_line(sources)

    lines = body.split("\n")
    h1 = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1 is None:
        return {"file": path.name, "action": "skipped", "detail": "no H1"}

    # Anchor to the type banner: the summary belongs directly under it, and
    # placing it by counting blank lines from the H1 would put it above the
    # banner on a page whose banner is missing.
    scan = h1 + 1
    while scan < len(lines) and not lines[scan].strip():
        scan += 1
    if scan >= len(lines) or not BANNER_RE.match(lines[scan].strip()):
        return {"file": path.name, "action": "skipped",
                "detail": "no type banner — run add_type_banner.py first"}

    after = scan + 1
    if after < len(lines) and SUMMARY_RE.match(lines[after].strip()):
        if lines[after].strip() == want:
            return None
        action = "updated"
        lines[after] = want
    else:
        action = "inserted"
        lines[after:after] = [want]

    if apply:
        path.write_text(fm_prefix + "\n".join(lines), encoding="utf-8")
    return {"file": path.name, "action": action, "detail": want}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    counts, skipped = {}, []
    for path in sorted((WIKI_ROOT / "claims").glob("*.md")):
        if path.stem == "index":
            continue
        rec = process(path, args.apply)
        if rec is None:
            counts["unchanged"] = counts.get("unchanged", 0) + 1
            continue
        counts[rec["action"]] = counts.get(rec["action"], 0) + 1
        if rec["action"] == "skipped":
            skipped.append(f"{rec['file']}: {rec['detail']}")

    verb = "" if args.apply else " (dry run)"
    print(f"claims/{verb}: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
    for s in skipped[:10]:
        print(f"      SKIPPED {s}")


if __name__ == "__main__":
    main()
