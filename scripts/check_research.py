#!/usr/bin/env python3
"""
check_research.py — validate the research layer, and read it back.

    python3 scripts/check_research.py            # validate; exit 1 on any problem
    python3 scripts/check_research.py --summary  # what is in the store, by shape
    python3 scripts/check_research.py --why <claim-slug>
    python3 scripts/check_research.py --issues   # open and resolved issues

The same validation runs inside `lint.py` (`--type research`), so this script
is for working on one object with full output rather than for CI. It is safe to
run with nothing in research/ at all: an empty layer is valid, which keeps
CLAUDE.md's "a count of zero means the work is done" property intact.

`--why` is the acceptance test run as a command. The question the layer exists
to answer is *why does the wiki believe claim X*, and the answer has to reach
past the citation to the analysis, the dataset, the release and the governance
the data was collected under — from the records alone, reading no prose.
"""

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import research_lib as rl
import observation_lib as ol


def _fmt_result(result: dict) -> str:
    if not isinstance(result, dict):
        return "no result"
    mt = result.get("measure_type", "?")
    est = result.get("estimate")
    out = f"{mt}" if est is None else f"{mt} = {est}"
    if result.get("ci_lower") is not None:
        out += f" [{result['ci_lower']}, {result['ci_upper']}]"
    if result.get("k"):
        out += f", k = {result['k'].get('value')} {result['k'].get('unit')}"
    return out


def why(claim_slug: str) -> int:
    """Traverse claim <- evidence <- analysis <- dataset <- release <- protocol."""
    if not (rl.WIKI_ROOT / "claims" / f"{claim_slug}.md").is_file():
        print(f"no claims/{claim_slug}.md", file=sys.stderr)
        return 1
    obs_records, _ = ol.load_all()
    releases, _ = rl.load_releases()
    protocols, _ = rl.load_protocols()
    reviews, _ = rl.load_reviews()
    issue_recs, _ = rl.load_issues()

    print(f"claim: {claim_slug}\n")

    cited = [(k, r) for k, r in sorted(obs_records.items())
             if any((a or {}).get("claim") == claim_slug
                    for a in (r or {}).get("appears_in") or [])]
    if not cited:
        print("  No structured evidence record names this claim.")
        print("  (That is a normal state: 424 claim pages have no record. The page's")
        print("   own ## Evidence section is the argument; this store is the")
        print("   configuration that argument rests on, where anyone has written it.)")
        return 0

    for study_key, rec in cited:
        study = rec.get("study") or {}
        prov = rec.get("provenance") or {}
        edge = next(a for a in rec["appears_in"] if a.get("claim") == claim_slug)
        source_type = prov.get("source_type")
        banner = ""
        if source_type != "research":
            # Loud, because this is the field that separates a finding from a
            # simulation, a model's proposal and a platform's own telemetry. A
            # reader who misses it pools the wrong rows.
            banner = f"   << NOT A PUBLISHED FINDING: source_type = {source_type} >>"
        print(f"  [{edge.get('bearing', '?')}] {study_key}{banner}")
        if edge.get("anchor"):
            print(f"      written into the claim's argument at "
                  f"### anchor {edge['anchor']!r}")
        else:
            print("      recorded against the claim but not written into its "
                  "argument (no anchor)")
        design = (study.get("design") or {}).get("family")
        print(f"      design: {design}")

        release_ref = study.get("release")
        release = None
        if isinstance(release_ref, dict):
            pair = (release_ref.get("ref"), release_ref.get("version"))
            release = releases.get(pair)
            print(f"      release: {pair[0]}@{pair[1]}")
            if isinstance(release, dict):
                r = release.get("release") or {}
                print(f"        question: {' '.join(str(r.get('question','')).split())}")
                current = rl.latest(v for (i, v) in releases if i == pair[0])
                if current and current != pair[1]:
                    print(f"        NOTE: {pair[0]} is now at {current}; this evidence "
                          f"was produced by {pair[1]} and stays attached to it")
        elif study.get("citation"):
            print(f"      source: {' '.join(str(study['citation']).split())[:100]}")

        analyses = {a.get("id"): a for a in (release or {}).get("analyses") or []
                    if isinstance(a, dict)}
        datasets = {d.get("id"): d for d in (release or {}).get("datasets") or []
                    if isinstance(d, dict)}
        for o in rec.get("observations") or []:
            if not isinstance(o, dict):
                continue
            out = o.get("outcome") or {}
            print(f"      - {o.get('id')}: {out.get('construct')} "
                  f"-> {_fmt_result(o.get('result'))}")
            gaps = [f"{k}: {v}" for k, v in (o.get("observability") or {}).items()
                    if v != "observed"]
            if gaps:
                print(f"          not fully observed: {', '.join(sorted(gaps))}")
            a = analyses.get(o.get("analysis_ref"))
            if a:
                code = a.get("code") or {}
                print(f"          analysis: {a.get('id')} — {code.get('repo')} "
                      f"@{str(code.get('commit'))[:12]} {code.get('path')}")
                for dep in a.get("inputs") or []:
                    d = datasets.get(dep) or {}
                    loc = d.get("location") or {}
                    print(f"          dataset:  {dep} ({d.get('grain')}) "
                          f"{loc.get('kind')}:{loc.get('ref')}")
                    print(f"                    sha256 {str(d.get('sha256'))[:16]}…  "
                          f"{d.get('identifiability')} / access {d.get('access')}")

        proto = (release or {}).get("protocol")
        if isinstance(proto, dict):
            p = protocols.get((proto.get("ref"), proto.get("version"))) or {}
            consent = p.get("consent") or {}
            ext = p.get("external_review") or {}
            print(f"      protocol: {proto.get('ref')}@{proto.get('version')}")
            print(f"        consent {consent.get('mechanism')}; secondary use "
                  f"{consent.get('secondary_research_use')}; AI processing disclosed "
                  f"{consent.get('ai_processing_disclosed')}")
            print(f"        external review: {ext.get('status')}"
                  f"{' — ' + str(ext.get('approval_id')) if ext.get('approval_id') else ''}")

        # What anybody has said about any of it.
        targets = {("evidence", f"{study_key}/{o.get('id')}")
                   for o in rec.get("observations") or [] if isinstance(o, dict)}
        if isinstance(release_ref, dict):
            targets.add(("release", release_ref.get("ref")))
        targets.add(("claim", claim_slug))
        related = _reviews_for(reviews, targets) | _issues_for(issue_recs, targets)
        if related:
            print(f"      contested by: {', '.join(sorted(related))}")
        print()
    return 0


def _reviews_for(reviews, targets) -> set:
    out = set()
    for rid, rec in reviews.items():
        t = ((rec or {}).get("review") or {}).get("target") or {}
        if (t.get("kind"), t.get("ref")) in targets:
            out.add(f"review {rid}")
    return out


def _issues_for(issue_recs, targets) -> set:
    out = set()
    for iid, rec in issue_recs.items():
        block = (rec or {}).get("issue") or {}
        t = block.get("target") or {}
        if (t.get("kind"), t.get("ref")) in targets:
            out.add(f"issue {iid} ({block.get('state')})")
    return out


def issues_report() -> None:
    issue_recs, _ = rl.load_issues()
    reviews, _ = rl.load_reviews()
    if not issue_recs:
        print("No issues recorded.")
        return
    for iid, rec in sorted(issue_recs.items()):
        b = (rec or {}).get("issue") or {}
        t = b.get("target") or {}
        print(f"{b.get('state','?'):<11} {iid}")
        print(f"            {t.get('kind')} {t.get('ref')}"
              f"{'@' + t.get('version') if t.get('version') else ''} "
              f"[{b.get('category')}]")
        print(f"            {' '.join(str(b.get('summary','')).split())}")
        counts = {f: len(b.get(f) or []) for f in
                  ("raised_by", "supporting", "disputing", "response")}
        # The whole point of the object, printed: N people, one problem.
        print(f"            {counts['raised_by']} independent identification(s), "
              f"{counts['supporting']} supporting, {counts['disputing']} disputing, "
              f"{counts['response']} response(s)")
        first = (b.get("raised_by") or [None])[0]
        if first:
            when = ((reviews.get(first) or {}).get("review") or {}).get("created_at")
            print(f"            first identified by {first} ({when})")
        res = b.get("resolution") or {}
        if res:
            rr = res.get("resulting_release") or {}
            print(f"            resolution: {res.get('outcome')} "
                  f"(asserted by {res.get('decided_by')})"
                  f"{' -> ' + rr.get('ref') + '@' + rr.get('version') if rr else ''}")
        print()


def summary() -> None:
    protocols, _ = rl.load_protocols()
    releases, _ = rl.load_releases()
    reviews, _ = rl.load_reviews()
    issue_recs, _ = rl.load_issues()
    obs_records, _ = ol.load_all()

    by_obj = defaultdict(list)
    for (oid, v) in protocols:
        by_obj[("protocol", oid)].append(v)
    for (oid, v) in releases:
        by_obj[("release", oid)].append(v)
    print(f"{len({k for k, _ in protocols})} protocol(s), "
          f"{len({k for k, _ in releases})} release(s), "
          f"{len(reviews)} review(s), {len(issue_recs)} issue(s).\n")

    for (kind, oid), versions in sorted(by_obj.items()):
        print(f"  {kind} {oid}: {', '.join(sorted(versions, key=rl.semver))} "
              f"(current: {rl.latest(versions)})")
    print()

    linked = [k for k, r in obs_records.items()
              if isinstance((r or {}).get("study", {}).get("release"), dict)]
    print(f"  {len(linked)} observation record(s) produced by a release of ours; "
          f"{len(obs_records) - len(linked)} from sources we read.")

    bearings = Counter(a.get("bearing") for r in obs_records.values()
                       for a in (r or {}).get("appears_in") or [])
    anchored = sum(1 for r in obs_records.values()
                   for a in (r or {}).get("appears_in") or [] if a.get("anchor"))
    total_edges = sum(bearings.values())
    print(f"  {total_edges} evidence->claim edge(s): "
          f"{', '.join(f'{v} {k}' for k, v in bearings.most_common())}")
    print(f"  {anchored} of them written into a claim's argument; "
          f"{total_edges - anchored} recorded but not promoted.\n")

    types = Counter(((r or {}).get("review") or {}).get("review_type")
                    for r in reviews.values())
    bases = Counter(b for r in reviews.values()
                    for b in (((r or {}).get("review") or {}).get("author") or {}).get("basis") or [])
    moderated = [rid for rid, r in reviews.items()
                 if any(m.get("state") != "visible"
                        for m in ((r or {}).get("review") or {}).get("moderation") or [])]
    for label, counter in (("review type", types), ("contribution basis", bases)):
        print(f"  {label}")
        for k, v in counter.most_common():
            print(f"    {v:>4}  {k}")
        print()
    print(f"  {len(moderated)} review(s) carry a moderation action "
          f"{'(' + ', '.join(sorted(moderated)) + ')' if moderated else ''}")

    states = Counter(((r or {}).get("issue") or {}).get("state") for r in issue_recs.values())
    print(f"  issue state: " + ", ".join(f"{v} {k}" for k, v in states.most_common()))

    # Synthetic and model-proposed records, named. The store must never make a
    # simulation indistinguishable from a finding at a glance.
    synthetic = sorted(k for k, r in obs_records.items()
                       if ((r or {}).get("provenance") or {}).get("source_type") != "research")
    if synthetic:
        print(f"\n  NOT PUBLISHED FINDINGS ({len(synthetic)}): {', '.join(synthetic)}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", action="store_true",
                    help="describe the layer rather than validating it")
    ap.add_argument("--issues", action="store_true", help="list issues and their state")
    ap.add_argument("--why", metavar="CLAIM_SLUG",
                    help="traverse claim <- evidence <- analysis <- dataset <- "
                         "release <- protocol")
    args = ap.parse_args()

    if args.why:
        sys.exit(why(args.why))
    if args.issues:
        issues_report()
        return
    if args.summary:
        summary()
        return

    problems = rl.validate_all()
    if not problems:
        protocols, _ = rl.load_protocols()
        releases, _ = rl.load_releases()
        reviews, _ = rl.load_reviews()
        issue_recs, _ = rl.load_issues()
        print(f"research/: {len(protocols)} protocol version(s), {len(releases)} release "
              f"version(s), {len(reviews)} review(s), {len(issue_recs)} issue(s), "
              f"0 issues.")
        return
    print(f"{len(problems)} problem(s):", file=sys.stderr)
    for p in problems:
        print(f"  {p}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
