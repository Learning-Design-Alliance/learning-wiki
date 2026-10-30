---
type: claim
title: "Calibrating a production LLM-as-judge suite raised per-flag precision from 0.6% to 48.9% while cutting confirmed false positives by 99%"
description: "Calibrating a production LLM-as-judge suite raised per-flag precision from 0.6% to 48.9% while cutting confirmed false positives by 99%"
id: llm-judge-calibration-precision-gain-magicschool
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
    rigour: 3
---

# Calibrating a production LLM-as-judge suite raised per-flag precision from 0.6% to 48.9% while cutting confirmed false positives by 99%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After calibration, per-flag precision rose from 0.6% (24 true positives among 4,002 flags) to 48.9% (43 among 88), a 99% reduction in confirmed false-positive flags. [→ Chris Rohlfs 2026](#chris-rohlfs-2026)

## Evidence

### Chris Rohlfs 2026

Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478 [doi:10.48550/arxiv.2609.28478](https://doi.org/10.48550/arxiv.2609.28478)

`q2 · i?` · `design · r3`

Ground-truthing audit of the two flag streams on the 2,482-case benchmark: 4,002 pre-calibration flags were audited with fixed rules plus human assessment, and the 88 post-calibration flags were fully manually ground-truthed. The article reports "precision rose from 0.6%" to 48.9% while true-positive flags rose from 24 to 43.

> "precision rose from 0.6% (24 true positives among 4,002 flags) to 48.9% (43 among 88), so the calibrated suite surfaces more confirmed failures from a primary stream roughly one-fiftieth the size."

## Discussion


## Related Claims

- [Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%](egregious-capture-100-percent-after-calibration.md) — related
- [A second LLM judge failed to corroborate 94% of 140,000 flagged failures from 2.5 million evaluations, indicating false positives dominated the pre-calibration suite](second-judge-94-percent-uncorroborated-flags.md) — related
- [Grader errors dominate audited rejections on benchmarks using rule-based evaluators (PHYBench and PRISM-Physics)](grader-errors-dominate-rule-based-evaluator-benchmarks.md)
