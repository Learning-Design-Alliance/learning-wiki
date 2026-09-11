#!/usr/bin/env python3
"""
compile_observations.py — emit `research_observation` records.

    python3 scripts/compile_observations.py                 # NDJSON to stdout
    python3 scripts/compile_observations.py --out FILE.ndjson
    python3 scripts/compile_observations.py --explain zingaretti-2026/l2-verbal-fluency-post

One line per observation, with the study-level blocks (population, context,
intervention, the named comparison) denormalised onto it — because the unit
the downstream substrate reasons over is the OBSERVATION, and a consumer
should never have to join two files to know who was in the room.

WHAT THIS DELIBERATELY DOES NOT DO
----------------------------------
**No metric is converted.** A partial η² stays a partial η²; a regression
coefficient stays one. Turning β = 17.17 words into a d would require the
pooled SD, and inventing one to make records comparable is how a store ends up
full of confident numbers nobody can trace. Comparability is an analytical
step, run explicitly and separately, downstream of this file.

**No pooling, no averaging, no universal weight.** Two observations of
"retrieval practice" are two rows, and stay two rows. The whole point of the
record is that d = .78 is a measurement of one configuration, not an edge
weight between two concepts.

**No design-hypothesis edges.** A logic model says "Goal A is intended to
contribute to Outcome B"; these records say "Study S observed relationship R
between configuration A and outcome B under population/context C". The second
can be offered as evidence for or against the first, by something that weighs
it. There is no field here that turns one into the other, and `kind` plus
`provenance.source_type` are emitted on every row so a consumer cannot lose
track of which it is holding.

**Absence is preserved, not filled.** `observability` rides on every record.
A consumer that treats an absent effect size as zero will be wrong; one that
reads `effect_size: unreported` can decline to pool the row instead.
"""

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import observation_lib as ol

RECORD_KIND = "research_observation"
COMPILER_VERSION = 2


def compile_all(directory: Path | None = None) -> tuple[list, list]:
    """([record, ...], [problem, ...]). Refuses to emit anything from a store
    that does not validate — a malformed record is worse downstream than a
    missing one, because the consumer has no way to tell it is malformed."""
    records, parse_errors = ol.load_all(directory)
    issues = list(parse_errors)
    claim_index = ol.claim_evidence_anchors()
    for key, rec in records.items():
        issues.extend(ol.validate_record(rec, key, claim_index))
    if issues:
        return [], issues

    out = []
    for key, rec in sorted(records.items()):
        study = rec.get("study") or {}
        eb = rec.get("evidence_base") or {}
        arms = {a["id"]: a for a in (eb.get("arms") or []) if isinstance(a, dict)}
        comparisons = {c["id"]: c for c in (rec.get("comparisons") or [])}
        for o in rec.get("observations") or []:
            comp = dict(comparisons.get(o.get("comparison_ref")) or {})
            # Resolve the contrast into the arms it is over. A consumer must
            # never have to join two blocks to know WHICH configuration beat
            # WHICH — that ambiguity is what v1's free-text comparison had.
            #
            # ALWAYS LISTS on the way out, whichever way the YAML was authored.
            # One arm needs no brackets in a hand-written file; a consumer
            # should never have to test whether it got a mapping or a list.
            idx_ids = ol.arms_named(comp.get("index_arm"))
            ref_ids = ol.arms_named(comp.get("reference_arm"))
            comp["index_arms"] = [arms[a] for a in idx_ids if a in arms]
            comp["reference_arms"] = [arms[a] for a in ref_ids if a in arms]
            # Derived and emitted rather than left to be counted, because it
            # changes what the estimate means: a pooled effect against two
            # different counterfactuals is a different object from one against
            # a single control, and a consumer weighting rows needs to see it.
            comp["reference_is_heterogeneous"] = len(ref_ids) > 1
            comp["index_is_heterogeneous"] = len(idx_ids) > 1
            out.append({
                "kind": RECORD_KIND,
                "compiler_version": COMPILER_VERSION,
                "schema_version": rec.get("schema_version"),
                "observation_id": f"{key}/{o['id']}",

                # --- provenance rides first, so a consumer that reads nothing
                # else still knows this is a published finding and not a
                # learner event, a simulation, or an LLM's proposal.
                "provenance": {
                    **(rec.get("provenance") or {}),
                    "study_key": key,
                    "citation": study.get("citation"),
                    "doi": study.get("doi"),
                    # Present when the source is a research release of ours
                    # rather than somebody's paper: {ref, version}, pinned to
                    # the version that produced this result and never moved to
                    # a later one. With `analysis_ref` below it closes the
                    # chain to the code and the data, so a consumer can reach
                    # the analysis without joining through prose.
                    "release": study.get("release"),
                    "analysis_ref": o.get("analysis_ref"),
                    # Each entry carries the claim AND the direction of the
                    # edge — supports / contradicts / qualifies — so a consumer
                    # weighing evidence for a proposition never has to infer a
                    # direction that the record already states.
                    "wiki_anchors": rec.get("appears_in") or [],
                },

                # --- the configuration side of the relation, kept whole.
                # Not atomised into independent variables: an arm's elements
                # are what the authors delivered TOGETHER, and separating them
                # would assert an additivity nobody measured.
                "configuration": {
                    "design": study.get("design") or {},
                    "synthesis": study.get("synthesis"),
                    # What the results are ABOUT, and in what unit it is
                    # counted. `unit` is the field that stops 23 studies and
                    # 3371 participants collapsing into one unreadable number.
                    "evidence_base": {
                        "unit": eb.get("unit"),
                        "size": eb.get("size"),
                        "additional_sizes": eb.get("additional_sizes") or [],
                        "population": eb.get("population") or {},
                        "context": eb.get("context") or {},
                        "variation": eb.get("variation") or [],
                    },
                    "arms": list(arms.values()),
                    "comparison": comp,
                    # The analysed sample for THIS result, which is routinely
                    # not the study's: a comprehension ANOVA on 62 of 67
                    # randomised, or a pooled estimate over 9 of 23 studies.
                    "sample": o.get("sample"),
                },

                # --- the observed side
                "outcome": o.get("outcome") or {},
                "time": o.get("time") or {},
                "result": o.get("result") or {},
                "moderators": o.get("moderators") or {},

                # --- what was NOT established. First-class, never dropped.
                "observability": o.get("observability") or {},
                "observability_notes": o.get("observability_notes"),

                "source_quote": o.get("source_quote"),
                "source_location": o.get("source_location"),

                # Every concept anchor the record carries, flattened for a
                # consumer that wants to index by wiki page. Source language
                # stays where it is; this is an addition, not a replacement.
                "concept_anchors": sorted({
                    a
                    for arm in arms.values()
                    for el in (arm.get("elements") or [])
                    for a in (el.get("anchors") or [])
                } | set((o.get("outcome") or {}).get("anchors") or [])),
            })
    return out, []


def explain(records: list, observation_id: str) -> int:
    """The success criterion, run as a command.

    'What exactly was done, to whom, compared with what, in what context,
    measured how, at what time, with what result and uncertainty, and what
    important information was not reported?' — answered from the record alone,
    with no narrative prose read."""
    rec = next((r for r in records if r["observation_id"] == observation_id), None)
    if rec is None:
        print(f"no observation {observation_id!r}. Available:", file=sys.stderr)
        for r in records:
            print(f"  {r['observation_id']}", file=sys.stderr)
        return 1

    cfg, res, obsv = rec["configuration"], rec["result"], rec["observability"]

    def block(label, text):
        print(f"\n{label}\n  {text or '—'}")

    print(f"=== {rec['observation_id']} ===")
    # A release of ours carries no hand-written citation — the release IS the
    # source, and copying its title and authors into the record would be the
    # second copy this schema exists to avoid. Name it instead.
    prov = rec["provenance"]
    release = prov.get("release")
    if prov.get("citation"):
        print(f"    {prov['citation']}")
    elif isinstance(release, dict):
        print(f"    research release {release.get('ref')}@{release.get('version')}"
              f"{'  analysis: ' + prov['analysis_ref'] if prov.get('analysis_ref') else ''}")
    else:
        print("    source not recorded")
    idx_arms = cfg["comparison"].get("index_arms") or []
    block("WHAT WAS DONE", "" if idx_arms else "(no index arm — see the comparison below)")
    for idx in idx_arms:
        if len(idx_arms) > 1:
            print(f"    [{idx.get('id')}] {idx.get('description')}")
        else:
            print(f"    {idx.get('description')}")
        for el in idx.get("elements") or []:
            anchors = ", ".join(el.get("anchors") or []) or "no wiki anchor"
            print(f"      - {el['term']}  [{anchors}]")
        if idx.get("dose"):
            d = idx["dose"]
            print(f"      dose: {d.get('amount')} {d.get('unit')} — {d.get('detail', '')}")

    ebase = cfg["evidence_base"]
    size = ebase.get("size") or {}
    block("TO WHOM", (ebase.get("population") or {}).get("description"))
    print(f"    evidence base: {size.get('value')} {size.get('unit')}")
    for s in ebase.get("additional_sizes") or []:
        print(f"      also {s.get('value')} {s.get('unit')} — {s.get('note')}")
    if cfg.get("sample"):
        print(f"    analysed for THIS result: {cfg['sample'].get('value')} "
              f"{cfg['sample'].get('unit')}")
    for f in ("age_or_stage", "prior_knowledge", "language_background"):
        if (ebase.get("population") or {}).get(f):
            print(f"    {f}: {ebase['population'][f]}")
    for v in ebase.get("variation") or []:
        print(f"    varies by {v.get('dimension')}: {v.get('distribution')}")

    refs = cfg["comparison"].get("reference_arms") or []
    block("COMPARED WITH", f"[{cfg['comparison'].get('kind')}] "
                           f"{cfg['comparison'].get('description')}")
    if cfg["comparison"].get("reference_is_heterogeneous"):
        print(f"    ** HETEROGENEOUS COMPARATOR — {len(refs)} different configurations "
              f"pooled into one estimate **")
    for ref in refs:
        print(f"    reference arm [{ref.get('id')}]: {ref.get('description')}")
    block("IN WHAT CONTEXT", "; ".join(
        f"{k}: {v}" for k, v in (ebase.get("context") or {}).items() if v))
    block("MEASURED HOW", f"{rec['outcome'].get('construct')} "
                          f"— {rec['outcome'].get('measure')} "
                          f"({rec['outcome'].get('scale')}, {rec['outcome'].get('direction')})")
    print(f"    source language: {rec['outcome'].get('source_language')!r}")
    print(f"    outcome role: {rec['outcome'].get('role')} ({rec['outcome'].get('role_basis')})")
    for v in rec["outcome"].get("valued_by") or []:
        print(f"    valued by {v.get('actor')}: {v.get('basis')}")
    block("AT WHAT TIME", f"{rec['time'].get('label')} "
                          f"{rec['time'].get('offset') or ''}")
    block("WITH WHAT RESULT", f"{res.get('measure_type')} = {res.get('estimate')} "
                              f"{res.get('unit') or ''}".strip())
    for f in ("standard_error", "ci_lower", "ci_upper", "p_value", "statistic",
              "model", "finding", "interpretation", "descriptives", "note"):
        if res.get(f) is not None:
            print(f"    {f}: {res[f]}")
    if res.get("k"):
        print(f"    pooled over: {res['k'].get('value')} {res['k'].get('unit')}")
    if res.get("heterogeneity"):
        h = res["heterogeneity"]
        unit = {"percent": "%"}.get(h.get("unit"), f" {h['unit']}" if h.get("unit") else "")
        note = f" — {h['interpretation']}" if h.get("interpretation") else ""
        print(f"    heterogeneity: {h.get('statistic')} = {h.get('value')}{unit}{note}")
    if res.get("prediction_interval"):
        pi = res["prediction_interval"]
        print(f"    prediction interval: {pi.get('lower')} to {pi.get('upper')}")
    if res.get("certainty"):
        c = res["certainty"]
        print(f"    certainty: {c.get('rating')} ({c.get('framework')})")
    synth = cfg.get("synthesis") or {}
    for a in synth.get("attempted_but_precluded") or []:
        print(f"    ATTEMPTED AND PRECLUDED: {a.get('analysis')} — {a.get('reason')}")
    mods = rec["moderators"].get("reported") or []
    block("REPORTED MODERATORS", "none reported" if not mods else "")
    for m in mods:
        print(f"    - {m['variable']}: {m['relationship']}")
    block("WHAT WAS NOT REPORTED", "; ".join(
        f"{k} = {v}" for k, v in obsv.items() if v != "observed") or "nothing — every field observed")
    if rec.get("observability_notes"):
        print(f"    {rec['observability_notes'].strip()}")
    print(f"\nSOURCE\n  \"{rec['source_quote']}\"\n  — {rec['source_location']}")
    print(f"\nPROVENANCE\n  source_type={rec['provenance'].get('source_type')} "
          f"method={rec['provenance'].get('extraction_method')} "
          f"verification={rec['provenance'].get('verification')}")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, help="write NDJSON here instead of stdout")
    ap.add_argument("--explain", metavar="OBSERVATION_ID",
                    help="print one record as prose — the success-criterion check")
    args = ap.parse_args()

    records, issues = compile_all()
    if issues:
        print(f"refusing to compile: {len(issues)} schema issue(s)", file=sys.stderr)
        for i in issues:
            print(f"  {i}", file=sys.stderr)
        sys.exit(1)

    if args.explain:
        sys.exit(explain(records, args.explain))

    # YAML resolves an unquoted 2026-09-07 to a date object, which json
    # cannot encode. Normalise at the boundary rather than forcing every
    # author to quote a date correctly — the same call okf_lib's doi_resolver
    # makes about unescaping Crossref's HTML entities once, on the way in.
    def _iso(o):
        if isinstance(o, (date, datetime)):
            return o.isoformat()
        raise TypeError(f"{type(o).__name__} is not JSON serializable")

    lines = "".join(json.dumps(r, ensure_ascii=False, sort_keys=True, default=_iso) + "\n"
                    for r in records)
    if args.out:
        args.out.write_text(lines, encoding="utf-8")
        print(f"Wrote {args.out}: {len(records)} {RECORD_KIND} record(s).")
    else:
        sys.stdout.write(lines)


if __name__ == "__main__":
    main()
