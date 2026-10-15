---
type: claim
title: "Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%"
description: "Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%"
id: egregious-capture-100-percent-after-calibration
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chris-rohlfs-2026
    resource: "https://doi.org/10.48550/arxiv.2609.28478"
    title: "Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478 [doi:10.48550/arxiv.2609.28478](https://doi.org/10.48550/arxiv.2609.28478)"
    author: "Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All 21 evaluators reached 100% capture on the 570-case synthetic egregious pool after calibration, up from a per-evaluator median of 100% with a range of 73.3–100% before. [→ Chris Rohlfs 2026](#chris-rohlfs-2026)

## Evidence

### Chris Rohlfs 2026

Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478 [doi:10.48550/arxiv.2609.28478](https://doi.org/10.48550/arxiv.2609.28478)

`q2 · i?` · `design · r2`

Per-evaluator before/after comparison on the 570-case hand-curated synthetic egregious set (denominators n=12 to n=79 per evaluator). The article reports the exact 95% Clopper–Pearson lower bound is 73.5% on the smallest denominator and 95.4% on the largest.

> "All 21 evaluators reached 100% egregious-case capture after calibration (Figure 3), up from a per-evaluator median of 100% (range 73.3–100%) before calibration."

## Discussion


## Related Claims
- [Five general instruction-following evaluators could not reach deployable activation rates (best BMK 2.23%–20.72%) because fixed rubrics cannot enumerate long per-conversation instruction sets](instruction-following-evaluators-structural-carve-out.md) — related
- [Calibrating a production LLM-as-judge suite raised per-flag precision from 0.6% to 48.9% while cutting confirmed false positives by 99%](llm-judge-calibration-precision-gain-magicschool.md) — related
- [A second LLM judge failed to corroborate 94% of 140,000 flagged failures from 2.5 million evaluations, indicating false positives dominated the pre-calibration suite](second-judge-94-percent-uncorroborated-flags.md) — related
