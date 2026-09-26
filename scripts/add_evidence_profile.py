#!/usr/bin/env python3
"""
add_evidence_profile.py — what a principle, strategy, theory or other page rests on.

A claim page states its own weight (add_evidence_summary.py). The pages that
cite claims did not: a strategy citing twelve claims said nothing about how
many studies stood behind them, how strong those were, or how many of its
claims hang on a single paper. So each page that cites claims gets a second
banner line, in the claim header's style:

    # Contrasting Cases

    > **Strategy** · [All strategies](index.md)
    > **Evidence** · 12 claims (9 for, 2 mixed, 1 against) · 19 studies, `q2`–`q4` · 9 of 19 report an effect size · 3 claims rest on one study

Every number comes from evidence_rollup.py, which counts distinct studies
rather than claims and never turns the codes into a verdict (see its
docstring). "for / mixed / against" are the page's own `[+]`, `[~]`, `[-]`
markers on its claim links; "unmarked" counts links carrying none.

Only a line in this script's own grammar is replaced (GENERATED_RE), so a
hand-written `> **Evidence** ·` line is kept and reported, as in
add_evidence_summary.py. Idempotent: a second run changes nothing.

    python3 scripts/add_evidence_profile.py --check
    python3 scripts/add_evidence_profile.py --apply
"""
import argparse
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import evidence_rollup as er  # noqa: E402
import okf_lib  # noqa: E402

SUMMARY_RE = re.compile(r"^>\s*\*\*Evidence\*\*\s*·.*$")
BANNER_RE = re.compile(r"^>\s*\*\*[^*]+\*\*\s*·\s*\[[^\]]*\]\(index\.md\)\s*$")
_POL = r"\d+ (?:for|mixed|against|unmarked)"
GENERATED_RE = re.compile(
    r"^> \*\*Evidence\*\* · (?:no claims cited|\d+ claims? \(" + _POL + r"(?:, " + _POL + r")*\)"
    r"(?: · no studies recorded yet| · \d+ stud(?:y|ies)(?:, `q\d`(?:–`q\d`)?)?"
    r" · \d+ of \d+ report an effect size(?: · (?:1 claim rests|\d+ claims rest) on one study)?))$")


def process(path: Path, want: str, apply: bool):
    text = path.read_text(encoding="utf-8")
    fm_match = okf_lib.FRONTMATTER_RE.match(text)
    fm_prefix = text[:fm_match.end()] if fm_match else ""
    _, body = okf_lib.split_frontmatter(text)
    lines = body.split("\n")
    h1 = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1 is None:
        return "skipped", "no H1"
    scan = h1 + 1
    while scan < len(lines) and not lines[scan].strip():
        scan += 1
    if scan >= len(lines) or not BANNER_RE.match(lines[scan].strip()):
        return "skipped", "no type banner — run add_type_banner.py first"
    after = scan + 1
    if after < len(lines) and SUMMARY_RE.match(lines[after].strip()):
        have = lines[after].strip()
        if have == want:
            return None, None
        if not GENERATED_RE.match(have):
            return "kept", have
        action = "updated"
        lines[after] = want
    else:
        action = "inserted"
        lines[after:after] = [want]
    if apply:
        path.write_text(fm_prefix + "\n".join(lines), encoding="utf-8")
    return action, want


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    claims = er.load_claims()
    cites = er.citations_by_page()
    bad = 0
    for kind in er.PROFILE_KINDS:
        counts, notes = {}, []
        for path in sorted((WIKI_ROOT / kind).glob("*.md")):
            if path.stem == "index":
                continue
            want = er.profile_line(er.page_profile(cites.get((kind, path.stem), []), claims))
            if not GENERATED_RE.match(want):   # the grammar and the writer must agree
                raise SystemExit(f"profile_line produced a line outside GENERATED_RE: {want}")
            action, detail = process(path, want, args.apply)
            key = action or "unchanged"
            counts[key] = counts.get(key, 0) + 1
            if action in ("skipped", "kept"):
                notes.append(f"{action.upper()} {path.name}: {detail}")
        bad += counts.get("inserted", 0) + counts.get("updated", 0)
        verb = "" if args.apply else " (dry run)"
        print(f"{kind}/{verb}: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
        for n in notes[:5]:
            print(f"      {n}")
    if args.check and bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
