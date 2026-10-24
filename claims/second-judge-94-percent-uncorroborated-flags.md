---
type: claim
title: "A second LLM judge failed to corroborate 94% of 140,000 flagged failures from 2.5 million evaluations, indicating false positives dominated the pre-calibration suite"
description: "A second LLM judge failed to corroborate 94% of 140,000 flagged failures from 2.5 million evaluations, indicating false positives dominated the pre-calibration suite"
id: second-judge-94-percent-uncorroborated-flags
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# A second LLM judge failed to corroborate 94% of 140,000 flagged failures from 2.5 million evaluations, indicating false positives dominated the pre-calibration suite

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Re-examining every failure from 2.5 million evaluations over a six-month window with a second LLM judge showed 94% of the 140,000 failures were not corroborated. [→ Chris Rohlfs 2026](#chris-rohlfs-2026)

## Evidence

### Chris Rohlfs 2026

Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478 [doi:10.48550/arxiv.2609.28478](https://doi.org/10.48550/arxiv.2609.28478)

`q2 · i?` · `design · r2`

Production log analysis over a six-month window in which a second LLM judge re-examined all 140,000 failures from 2.5 million evaluations; the article reports "In 94% of the 140,000 failures, the second model failed to corroborate the issue."

> "We applied a second LLM judge to re-examine every failure from 2.5 million evaluations over a six-month window. In 94% of the 140,000 failures, the second model failed to corroborate the issue."

## Discussion


## Related Claims
- [Calibrating a production LLM-as-judge suite raised per-flag precision from 0.6% to 48.9% while cutting confirmed false positives by 99%](llm-judge-calibration-precision-gain-magicschool.md) — related
- [Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%](egregious-capture-100-percent-after-calibration.md) — related
