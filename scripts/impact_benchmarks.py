#!/usr/bin/env python3
"""Audit observations/ effects and compute a Kraft benchmark only when verified.

This does not change the legacy ``i`` field.  A positive eligibility decision
requires source-checked, structured context for the particular effect, not a
regex guess from a paper title or a pooled effect from mixed studies.

    python3 scripts/impact_benchmarks.py --summary
    python3 scripts/impact_benchmarks.py --json > impact-context-audit.json
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
KRAFT_TIERS = json.loads((ROOT / "evidence-scales.json").read_text(encoding="utf-8"))[
    "impact_reference"]["kraft_2020"]["tiers"]
REQUIRED = (
    "verified_against_source", "unit", "population", "assignment",
    "comparator", "learner_start", "objective", "outcome_measure",
    "measure_alignment", "score_range", "effect_metric", "effect_value",
    "standardization_denominator", "horizon", "uncertainty",
)
ELIGIBLE = {
    "unit": {"single-study", "homogeneous-synthesis"},
    "population": {"pre-k-12"},
    "assignment": {"randomized", "credible-quasi-experiment"},
    "outcome_measure": {"standardized-achievement"},
    "effect_metric": {"d", "g", "smd"},
}
UNKNOWN = {"", "unknown", "unreported", "not reported", "n/a", "not assessed"}


def missing_value(value):
    return value is None or isinstance(value, str) and value.strip().lower() in UNKNOWN


def kraft_tier(context):
    """Return (tier, reason); absent fields and unreviewed sources are not eligible."""
    if context.get("verified_against_source") is not True:
        return None, "source context unverified"
    missing = [key for key in REQUIRED if missing_value(context.get(key))]
    if missing:
        return None, "missing: " + ", ".join(missing)
    for key, allowed in ELIGIBLE.items():
        if context[key] not in allowed:
            return None, f"outside Kraft scope: {key}={context[key]}"
    try:
        value = float(context["effect_value"])
    except (TypeError, ValueError):
        return None, "effect_value is not numeric"
    if not -10 <= value <= 10:
        return None, "effect_value is implausible; check the statistic"
    # These are signed effects.  A harmful effect is not a 'small benefit'.
    if value < 0:
        return None, "negative effect; report direction and magnitude separately"
    for tier in KRAFT_TIERS:
        if value >= tier["lower_inclusive"] and value < tier.get("upper_exclusive", float("inf")):
            return tier["label"], None
    return None, "effect is outside defined benchmark tiers"


METRIC = {"cohens_d": "d", "hedges_g": "g", "standardized_mean_difference": "smd"}


def derived_context(rec, obs):
    """The benchmark's inputs for one observation: the explicit `impact_context` block
    (what the record does not otherwise carry) merged with fields DERIVED from the
    record itself, so assignment, metric, value, interval, horizon, comparator and
    objective are never written twice and cannot disagree with the result they describe."""
    ctx = dict(obs.get("impact_context") or {})
    family = ((rec.get("study") or {}).get("design") or {}).get("family")
    if "assignment" not in ctx:
        ctx["assignment"] = ("randomized" if family in ("randomized-controlled-trial",
                                                       "cluster-randomized-controlled-trial") else None)
    res = obs.get("result") or {}
    ctx["effect_metric"] = METRIC.get(res.get("measure_type"))
    ctx["effect_value"] = res.get("estimate")
    ci = (res.get("ci_lower"), res.get("ci_upper"))
    ctx["uncertainty"] = (f"CI {ci[0]} to {ci[1]}" if None not in ci else
                          f"SE {res['standard_error']}" if res.get("standard_error") is not None else None)
    ctx["horizon"] = (obs.get("time") or {}).get("label")
    ctx["objective"] = (obs.get("outcome") or {}).get("construct")
    comp = {c.get("id"): c for c in rec.get("comparisons") or []}.get(obs.get("comparison_ref")) or {}
    ctx["comparator"] = comp.get("description")
    ctx["population"] = ctx.get("population_band")
    ctx["outcome_measure"] = ctx.get("outcome_class")
    return ctx


def audit(root=ROOT):
    """One row per observation reporting a standardized mean difference. Claim pages are
    not read: per-effect context belongs to the observation, which is where population,
    arms, outcome and timing already live (CLAUDE.md, 'The record is NOT in the claim's
    frontmatter'), and a claim's `sources[]` is rebuilt by sync_evidence_codes.py."""
    rows = []
    for path in sorted((root / "observations").glob("*.yaml")):
        rec = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if ((rec.get("provenance") or {}).get("source_type")) != "research":
            continue
        for obs in rec.get("observations") or []:
            if (obs.get("result") or {}).get("measure_type") not in METRIC:
                continue
            ctx = derived_context(rec, obs)
            tier, reason = kraft_tier(ctx)
            rows.append({"record": f"{path.stem}/{obs.get('id')}",
                         "claims": [a.get("claim") for a in rec.get("appears_in") or []],
                         "has_context": "impact_context" in obs,
                         "kraft_tier": tier, "reason": reason,
                         "missing": [k for k in REQUIRED if missing_value(ctx.get(k))]})
    return rows


def claims_with_numeric_i(root=ROOT):
    """How much of the corpus a benchmark could not yet read: claim evidence entries with
    a numeric `i` code. They are counted, never classified from the page."""
    n = 0
    for path in (root / "claims").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            front = yaml.safe_load(text.split("---\n", 2)[1]) or {}
            n += sum(1 for s in front.get("sources") or [] if isinstance(s, dict) and s.get("i") in (0, 1, 2, 3))
    return n


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--summary", action="store_true")
    group.add_argument("--json", action="store_true")
    args = parser.parse_args()
    rows = audit()
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        counts = Counter("Kraft " + r["kraft_tier"] if r["kraft_tier"] else r["reason"].split(":")[0]
                         for r in rows)
        print(f"Claim evidence entries with a numeric i code: {claims_with_numeric_i()} "
              "(none is classified from the page)")
        print(f"Observations reporting a standardized mean difference: {len(rows)}; "
              f"with impact_context: {sum(r['has_context'] for r in rows)}")
        for label, count in sorted(counts.items()):
            print(f"{label}: {count}")


if __name__ == "__main__":
    main()
