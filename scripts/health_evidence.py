#!/usr/bin/env python3
"""
health_evidence.py — the evidence and graph half of the wiki's health report.

wiki_health_check.py reports what the page-level checks can see: lint, citation
and DOI conflicts, duplicates, the TODO backlog. None of it says where the wiki's
weight rests on something nobody has checked, which is what matters once most
pages are written by an unattended extractor. This adds, per run:

- **Load-bearing claims with no check behind them.** Claims three or more design
  pages cite, split by what `check_load_bearing.py` has on each at its current
  text: an open failure, judged only against abstracts it could not settle
  (`unverifiable`), never judged, or not checkable (no DOI, no abstract, no
  cached article). A claim counts as checked only if one of its entries passed.
- **Load-bearing claims resting on one study**, and the share across all claims.
- **Impact codes with no statistic**: an evidence entry coded `i1`–`i3` whose
  text carries no effect size, percentage or test statistic.
- **Claim citations with no `[±~][SMW]` marker** (`check_evidence_markers.py`).
- **The link graph**: pages with no link in or out, and the share of pages in
  the largest connected component.
- **Claims with no coded evidence**, and evidence resting on abstracts only.

Everything is computed from the files in the checkout plus the judge's record
(`eval/runs/load-bearing/judged.ndjson`, per machine) and the committed dismissals.
Nothing calls a model or the network, so it runs on every health sweep.

    python3 scripts/health_evidence.py            # the section on its own
    python3 scripts/health_evidence.py --json     # machine-readable
    python3 scripts/wiki_health_check.py          # the whole report, this included
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

LOAD_BEARING = 3          # design pages citing a claim before it counts as load-bearing
STAT_RE = re.compile(
    r"(\b[dgr]\s*[=≈]\s*[-−]?\.?\d)|η²|eta\s*squared|\bOR\s*=|odds ratio|\bβ\s*=|\bbeta\s*=|"
    r"\bSMD\b|\bES\s*=|effect size[^.]{0,20}\d|Hedges|Cohen|\d\s*%|\bpercent|\d+\s*SD\b|"
    r"standard deviation|\bF\s*\(|\bt\s*\(|χ²|chi-square[^.]{0,20}\d|correlat\w*[^.]{0,40}\.\d|"
    r"\bp\s*[<=]", re.I)
# How the corpus says an entry rests on an abstract; the phrasing varies by who wrote it.
ABSTRACT_RE = re.compile(r"abstract only|only the abstract|abstract (?:was |could be )?read|"
                         r"abstract was available|from the abstract|full text (?:is|was) paywalled", re.I)
CODES_RE = re.compile(r"^`q[^\n]*`\s*$", re.M)
# The extraction validator's own pattern, which also reads d̄, ḡ and "η2-values of", so an
# entry the pipeline accepts is not reported here as lacking a statistic.
sys.path.insert(0, str(WIKI_ROOT))
from scripts.eval.validator import EFFECT_SIZE_RE as _EFFECT_SIZE_RE  # noqa: E402


def _entries(path: Path):
    import check_load_bearing as clb
    return clb.units(path)


def load_bearing(pages: dict, ranking: list) -> dict:
    """What the judge's record says about each load-bearing claim, at its current text."""
    import check_load_bearing as clb
    heavy = [r for r in ranking if r["designs"] >= LOAD_BEARING]
    judged = clb.done_before(clb.OUT) if clb.OUT.exists() else {}
    reviewed = clb.load_reviewed()
    jobs, skipped = clb.entry_jobs(heavy, pages, offline=True) if heavy else ([], {})
    by_claim = collections.defaultdict(list)
    for j in jobs:
        by_claim[j[0]["claim"]].append(j)
    unfetched = {c for c, _ in skipped.get("_unfetched", [])}
    state = {}
    for r in heavy:
        verdicts = []
        for j in by_claim.get(r["claim"], []):
            rec = judged.get(j[-2])
            if rec is None:
                verdicts.append("never judged")
            elif rec["verdict"] in ("fail", "not-this-study") and j[-1] in reviewed:
                verdicts.append("dismissed")
            else:
                verdicts.append(rec["verdict"])
        if r["claim"] in unfetched:
            verdicts.append("never judged")
        if not verdicts:
            state[r["claim"]] = "not checkable"
        elif "fail" in verdicts or "not-this-study" in verdicts:
            state[r["claim"]] = "open failure"
        elif "pass" in verdicts:
            state[r["claim"]] = "checked"
        elif "never judged" in verdicts:
            state[r["claim"]] = "never judged"
        else:
            state[r["claim"]] = "abstract could not settle it"
    return {"claims": len(heavy), "state": state,
            "designs": {r["claim"]: r["designs"] for r in heavy},
            "judge_record_present": clb.OUT.exists()}


def graph() -> dict:
    import link_pages
    pages = link_pages.all_pages()
    adj = link_pages.link_graph(pages)
    isolated = sorted(k for k in pages if not adj[k])
    seen, largest = set(), 0
    for k in pages:
        if k in seen:
            continue
        size, stack = 0, [k]
        seen.add(k)
        while stack:
            x = stack.pop()
            size += 1
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        largest = max(largest, size)
    return {"pages": len(pages), "isolated": isolated, "main_component": largest}


def evidence(pages: dict) -> dict:
    """Per-entry evidence problems across every claim."""
    import evidence_rollup as er
    claims = er.load_claims()
    one_study, no_evidence, abstract_only_claims = [], [], []
    impact_no_stat, entries, abstract_entries = [], 0, 0
    for slug, c in claims.items():
        studies = {er.study_key(s) for s in c["sources"]}
        if not studies:
            no_evidence.append(slug)
        elif len(studies) == 1:
            one_study.append(slug)
        path = pages[slug]
        _, units = _entries(path)
        abstract_here = 0
        for anchor, block, _subs in units:
            entries += 1
            codes = CODES_RE.search(block)
            if ABSTRACT_RE.search(block):
                abstract_entries += 1
                abstract_here += 1
            m = re.search(r"\bi([1-3])\b", codes.group(0)) if codes else None
            if m and not STAT_RE.search(block) and not _EFFECT_SIZE_RE.search(block):
                impact_no_stat.append(f"{slug}#{anchor}")
        if units and abstract_here == len(units):
            abstract_only_claims.append(slug)
    return {"claims": len(claims), "entries": entries, "one_study": one_study,
            "no_evidence": no_evidence, "impact_no_statistic": impact_no_stat,
            "abstract_entries": abstract_entries, "abstract_only_claims": abstract_only_claims}


def run() -> dict:
    import check_load_bearing as clb
    import check_evidence_markers as cem
    pages = clb.claim_pages()
    ranking = clb.ranking(pages)
    lb = load_bearing(pages, ranking)
    ev = evidence(pages)
    g = graph()
    unmarked = cem.scan()
    one = set(ev["one_study"])
    lb_counts = collections.Counter(lb["state"].values())
    return {
        "load_bearing_claims": lb["claims"],
        "load_bearing": dict(lb_counts),
        "load_bearing_one_study": sum(1 for c in lb["state"] if c in one),
        "claims_one_study": len(ev["one_study"]),
        "claims_no_evidence": len(ev["no_evidence"]),
        "claims": ev["claims"],
        "evidence_entries": ev["entries"],
        "abstract_only_entries": ev["abstract_entries"],
        "impact_no_statistic": len(ev["impact_no_statistic"]),
        "unmarked_claim_citations": len(unmarked),
        "isolated_pages": len(g["isolated"]),
        "main_component_share": round(g["main_component"] / g["pages"], 3),
        "_detail": {
            "load_bearing_state": lb["state"], "designs": lb["designs"],
            "judge_record_present": lb["judge_record_present"],
            "one_study": ev["one_study"], "no_evidence": ev["no_evidence"],
            "impact_no_statistic": ev["impact_no_statistic"],
            "abstract_only_claims": ev["abstract_only_claims"],
            "isolated": g["isolated"],
            "unmarked": [f"{p}:{n} -> {c}" for p, c, n, _ in unmarked],
        },
    }


def format_section(r: dict, limit: int = 15) -> str:
    d = r["_detail"]
    lb = r["load_bearing"]
    pct = lambda a, b: f"{a / b:.0%}" if b else "n/a"
    lines = [
        "## Evidence and links",
        f"- Load-bearing claims (cited by {LOAD_BEARING}+ design pages): {r['load_bearing_claims']} — "
        + ", ".join(f"{v} {k}" for k, v in sorted(lb.items(), key=lambda kv: -kv[1]))
        + " — `check_load_bearing.py --report`, procedure in `eval/load-bearing/README.md`",
        f"- Load-bearing claims resting on one study: {r['load_bearing_one_study']} of {r['load_bearing_claims']}",
        f"- Claims resting on one study: {r['claims_one_study']} of {r['claims']} "
        f"({pct(r['claims_one_study'], r['claims'])}); with no coded evidence: {r['claims_no_evidence']}",
        f"- Evidence entries read from an abstract only: {r['abstract_only_entries']} of {r['evidence_entries']} "
        f"({pct(r['abstract_only_entries'], r['evidence_entries'])})",
        f"- Evidence entries coded `i1`–`i3` with no effect size or test statistic in the entry: "
        f"{r['impact_no_statistic']} (an `i` code needs a printed magnitude; CLAUDE.md, impact table)",
        f"- Claim citations with no `[±~][SMW]` marker: {r['unmarked_claim_citations']} — `check_evidence_markers.py`",
        f"- Pages with no link in or out: {r['isolated_pages']}; pages in the main component: "
        f"{r['main_component_share']:.0%} — `link_pages.py --unlinked`",
    ]
    if not d["judge_record_present"]:
        lines.append("- (No judge record on this machine: every load-bearing claim reads as never judged. "
                     "Run `check_load_bearing.py` here, or read the report where the batches run.)")
    order = ["open failure", "never judged", "not checkable", "abstract could not settle it"]
    for state in order:
        claims = sorted((c for c, s in d["load_bearing_state"].items() if s == state),
                        key=lambda c: -d["designs"][c])
        if not claims:
            continue
        lines.append(f"\n### Load-bearing, {state} ({len(claims)})")
        for c in claims[:limit]:
            one = " · one study" if c in set(d["one_study"]) else ""
            lines.append(f"- claims/{c}.md — {d['designs'][c]} design pages{one}")
        if len(claims) > limit:
            lines.append(f"- ... and {len(claims) - limit} more")
    if d["impact_no_statistic"]:
        lines.append(f"\n### Impact coded with no statistic ({len(d['impact_no_statistic'])}, first {limit})")
        lines += [f"- claims/{e.replace('#', '.md#', 1)}" for e in d["impact_no_statistic"][:limit]]
    if d["isolated"]:
        by = collections.Counter(k.split("/")[0] for k in d["isolated"])
        lines.append(f"\n### Pages with no link in or out ({len(d['isolated'])}: "
                     + ", ".join(f"{v} {k}" for k, v in by.most_common()) + ")")
        lines += [f"- {k}.md" for k in d["isolated"][:limit]]
        if len(d["isolated"]) > limit:
            lines.append(f"- ... and {len(d['isolated']) - limit} more")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--limit", type=int, default=15, help="rows per list")
    args = ap.parse_args()
    r = run()
    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print(format_section(r, args.limit))


if __name__ == "__main__":
    main()
