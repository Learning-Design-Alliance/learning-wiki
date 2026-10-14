#!/usr/bin/env python3
"""
upgrade_worklist.py — the order in which principle and pattern pages are brought to the conditional
format, and what each one needs first.

Principles and patterns are what a course design names (`Realizes:`, `pattern:`), so a thin or
evidence-less one is a weak link in every design that names it (maintainer, 2026-10-14). The loop
for each page, run in waves:

1. **search**: a canonical page resting on two studies or fewer gets one evidence search first:
   unlinked claims already in the wiki (`link_pages.py --pages ... --claims-only --verify`) and the
   named syntheses on its topic, ingested by name.
2. **fold**: a page still on two studies or fewer after its search is folded into its parent
   (`merge_pages.py`). The maintainer, 2026-10-14: "Old pages with nothing in them were placeholders
   that haven't really held up to the research", and most such topics are anecdotal rather than
   research-based. A page with no parent is reported, not folded.
3. **convert**: a canonical page on three or more studies is rewritten in the conditional format
   (`principle-pattern-authoring.md`), checked by `check_design_page.py` and brief tests.
4. **fragment**: a page that is not canonical folds into the canonical page triage named for it
   (`eval/page-triage/triage.tsv`), or is re-filed; it is never converted on its own.

A page already converted (it has `## Fitting the design to a situation`) is done; a re-read is due
when its `## Further evidence, not yet read against this model` grows past ten bullets.

Rows are ordered by inbound links from other pages, most first: the pages most of the wiki points at
are the ones a design is most likely to name.

    python3 scripts/upgrade_worklist.py                  # summary and the next rows per step
    python3 scripts/upgrade_worklist.py --step search    # one step, every row
    python3 scripts/upgrade_worklist.py --tsv            # the whole table
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import build_reverse_index  # noqa: E402
import evidence_rollup  # noqa: E402

KINDS = {"principles": "principle", "patterns": "pattern"}
THIN = 2          # studies at or below which a page is searched, then folded
REREAD = 10       # unread further-evidence bullets that call for a re-read


def live(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def triage() -> dict:
    path = WIKI_ROOT / "eval" / "page-triage" / "triage.tsv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as fh:
        return {r["key"]: r for r in csv.DictReader(fh, delimiter="\t")}


def rows() -> list:
    reverse = build_reverse_index.build()
    claims = evidence_rollup.load_claims()
    cites = evidence_rollup.citations_by_page(reverse)
    tri = triage()
    out = []
    for folder, kind in KINDS.items():
        inbound = reverse["edges"].get(folder, {})
        for path in sorted((WIKI_ROOT / folder).glob("*.md")):
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            body = live(text)
            fm = text.split("\n---", 1)[0]
            canonical = bool(re.search(r"^canonical:\s*true\s*$", fm, re.M))
            converted = "## Fitting the design to a situation" in body
            prof = evidence_rollup.page_profile(cites.get((folder, path.stem), []), claims)
            n_in = sum(len(v) for v in inbound.get(path.stem, {}).values())
            further = re.search(r"\n## Further evidence, not yet read against this model\n(.*?)(?=\n## |\Z)", body, re.S)
            unread = len(re.findall(r"^- ", further.group(1), re.M)) if further else 0
            t = tri.get(f"{folder}/{path.stem}", {})
            parent = t.get("verdict_canonical") or ""
            if converted:
                step = "reread" if unread > REREAD else "done"
            elif not canonical:
                step = "fragment"
            elif prof["studies"] <= THIN:
                step = "search"
            else:
                step = "convert"
            out.append({"page": f"{folder}/{path.stem}", "kind": kind, "step": step, "inbound": n_in,
                        "claims": prof["claims"], "studies": prof["studies"], "q3_plus": prof["q3_plus"],
                        "unread": unread, "triage": t.get("verdict", ""), "parent": parent})
    out.sort(key=lambda r: (-r["inbound"], r["page"]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--step", choices=["search", "convert", "fragment", "reread", "done"])
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--tsv", action="store_true")
    args = ap.parse_args()
    table = rows()
    cols = ["page", "step", "inbound", "claims", "studies", "q3_plus", "unread", "triage", "parent"]
    if args.tsv:
        print("\t".join(cols))
        for r in table:
            print("\t".join(str(r[c]) for c in cols))
        return
    counts = Counter((r["kind"], r["step"]) for r in table)
    print("step      principles  patterns")
    for step in ("search", "convert", "fragment", "reread", "done"):
        print(f"{step:9} {counts[('principle', step)]:10}  {counts[('pattern', step)]:8}")
    for step in ([args.step] if args.step else ("search", "convert", "fragment", "reread")):
        sel = [r for r in table if r["step"] == step]
        if not sel:
            continue
        print(f"\n{step} ({len(sel)}):")
        for r in sel[: (None if args.step else args.limit)]:
            extra = f" -> {r['parent']}" if r["parent"] else ""
            print(f"  {r['inbound']:4} in · {r['studies']:3} studies · {r['claims']:3} claims  {r['page']}"
                  f"  [{r['triage'] or 'untriaged'}{extra}]")


if __name__ == "__main__":
    main()
