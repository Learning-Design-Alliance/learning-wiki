#!/usr/bin/env python3
"""
check_design_page.py — check a principle or pattern page in the conditional-model format.

The conversion waves (eval/page-triage/wave-*.md) checked every rewritten page with a
throwaway script and learned, wave by wave, what a page needs to help a designer. This
is that check kept, so a page an agent writes or updates outside a wave (a promoted
candidate, a page updated with attached evidence; settle_candidates.py) is held to
the same rules:

    marker_above_cap      a claim's [±~][SMW] marker is stronger than its recorded
                          evidence allows (S needs two studies and a q3, M one at q2;
                          link_pages.strength_cap)
    situation_table       no `## Fitting the design to a situation` table, or a row whose
                          Basis cell neither links a claim nor says it is untested
    unlabelled_default    a `Default design` section that does not say it is a proposal
                          or untested (wave 1: keep the concrete design, labelled)
    absence_overclaim     a sentence saying no research, study or evidence exists, or
                          that something has never been tested or compared, without
                          saying the absence is in this wiki (wave 7: answers repeated
                          "no claim here compares X" as "X has never been compared")
    missing_section       no `## Further evidence, not yet read against this model` or
                          no `## Key Sources`

Text inside HTML comments is not read: the deprecated body each page keeps is the old
page, not the model. A page not in the format (no Further evidence section) is skipped
unless named. Exit 1 if anything is found.

    python3 scripts/check_design_page.py                     # every converted page
    python3 scripts/check_design_page.py principles/sequencing.md
"""
import argparse
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import link_pages as lp  # noqa: E402

FURTHER = "## Further evidence, not yet read against this model"
CLAIM_MARK = re.compile(r"\]\(\.\./claims/([^)#\s]+)\.md(?:#[^)]*)?\)\s*\[([+~-])([SMW])\]")
ABSENCE = re.compile(r"\b(?:no|little|not any)\s+(?:published\s+|rigorous\s+|empirical\s+)?research\b"
                     r"|\bno (?:study|studies|trials?|experiments?) (?:has|have|exists?|anywhere)\b"
                     r"|\bnever been (?:tested|compared|studied|evaluated)\b"
                     r"|\b(?:has|have) not been (?:compared|studied|evaluated)\b"
                     r"|\bthe (?:field|literature) (?:has|lacks|offers no)\b", re.I)
LOCAL = re.compile(r"\bhere\b|\bthis wiki\b|\bin the wiki\b|\brecorded\b|\bcited\b|\bthis page\b|"
                   r"\bwith learners\b|\bthese rows\b|\bproposals?\b", re.I)
SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(*\[])")
_caps = {}


def cap(slug: str) -> str | None:
    if slug not in _caps:
        path = WIKI_ROOT / "claims" / f"{slug}.md"
        _caps[slug] = lp.strength_cap(lp.record(f"claims/{slug}", path)["evidence"]) if path.exists() else None
    return _caps[slug]


def sections(text: str) -> dict:
    out, cur = {}, None
    for line in text.split("\n"):
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            cur = m.group(1)
            out.setdefault(cur, [])
        elif cur:
            out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def check(path: Path) -> list:
    raw = path.read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    body = text.split("\n---\n", 1)[-1]
    probs = []
    for head in (FURTHER, "## Key Sources"):
        if head not in body:
            probs.append(("missing_section", head[3:]))
    for m in CLAIM_MARK.finditer(body):
        c = cap(m.group(1))
        if c and "WMS".index(m.group(3)) > "WMS".index(c):
            probs.append(("marker_above_cap", f"[{m.group(2)}{m.group(3)}] on {m.group(1)} (cap {c})"))
    secs = sections(body)
    fit = next((v for k, v in secs.items() if k.startswith("Fitting the design")), None)
    if fit is None:
        probs.append(("situation_table", "no `Fitting the design to a situation` section"))
    else:
        rows = [l for l in fit.split("\n") if l.startswith("|")]
        if len(rows) < 3:
            probs.append(("situation_table", "no table in the Fitting section"))
        for row in rows[2:]:
            basis = row.rstrip().rstrip("|").rsplit("|", 1)[-1]
            if "../claims/" not in basis and not re.search(r"untested|proposal|no claim", basis, re.I):
                probs.append(("situation_table", f"row with no claim and no untested label: {row[:90]}"))
    for k, v in secs.items():
        if k.lower().startswith("default design"):
            lead = (k + " " + v[:600]).lower()
            if not re.search(r"untested|proposal|not tested|while the relationship|each step says what stands behind it", lead):
                probs.append(("unlabelled_default", k))
    for k, v in secs.items():
        if k.startswith(("Key Sources", "Description", "Implications")):
            continue
        for para in v.split("\n"):
            for s in SENT.split(para):
                if ABSENCE.search(s) and not LOCAL.search(s):
                    probs.append(("absence_overclaim", f"{k}: {s.strip()[:160]}"))
    return probs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="*")
    args = ap.parse_args()
    if args.pages:
        paths = [WIKI_ROOT / p if not Path(p).is_absolute() else Path(p) for p in args.pages]
    else:
        paths = [p for f in ("principles", "patterns") for p in sorted((WIKI_ROOT / f).glob("*.md"))
                 if p.stem != "index" and FURTHER in p.read_text(encoding="utf-8")]
    total, kinds = 0, {}
    for p in paths:
        probs = check(p)
        for kind, detail in probs:
            print(f"{p.relative_to(WIKI_ROOT)}: {kind}: {detail}")
            kinds[kind] = kinds.get(kind, 0) + 1
        total += len(probs)
    print(f"\n{len(paths)} page(s) checked; {total} problem(s)" + (f": {kinds}" if kinds else ""))
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
