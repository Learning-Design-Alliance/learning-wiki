#!/usr/bin/env python3
"""Audit coded claim sources and compute a Kraft benchmark only when verified.

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


def kraft_tier(context):
    """Return (tier, reason); absent fields and unreviewed sources are not eligible."""
    if context.get("verified_against_source") is not True:
        return None, "source context unverified"
    missing = [key for key in REQUIRED if context.get(key) in (None, "", "unknown")]
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
    return ("small" if value < .05 else "medium" if value < .20 else "large"), None


def audit(root=ROOT):
    rows = []
    for path in sorted((root / "claims").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        front = yaml.safe_load(text.split("---\n", 2)[1]) or {}
        for source in front.get("sources") or []:
            if not isinstance(source, dict) or source.get("i") not in (0, 1, 2, 3):
                continue
            context = source.get("impact_context") or {}
            tier, reason = kraft_tier(context)
            rows.append({"page": str(path.relative_to(root)), "source": source.get("id"),
                         "legacy_i": source["i"], "kraft_tier": tier, "reason": reason,
                         "missing": [k for k in REQUIRED if context.get(k) in (None, "", "unknown")]})
    return rows


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
        print(f"Coded source records: {len(rows)}")
        for label, count in sorted(counts.items()):
            print(f"{label}: {count}")


if __name__ == "__main__":
    main()
