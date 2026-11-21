---
type: claim
title: "LLM accuracy on diagram-based thermodynamics items averages 32%, less than half the 67% text-only mean"
description: "LLM accuracy on diagram-based thermodynamics items averages 32%, less than half the 67% text-only mean"
id: llm-diagram-interpretation-thermodynamics-poor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: anna-geißler-2025
    resource: "https://doi.org/10.48550/arXiv.2508.21452"
    title: "Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)"
    author: Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM accuracy on diagram-based thermodynamics items averages 32%, less than half the 67% text-only mean

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 19 models, mean accuracy on the 17 diagram-based items was 32%, versus 67% on text-only items; the weakest model scored 6% and the strongest (gpt-o3) 76%. [→ Anna Geißler 2025](#anna-geiler-2025)

## Evidence

### Anna Geißler 2025

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `design · r2`

Cross-model comparison on the 17 diagram-based UTQA items using the same baseline prompt across platforms, reported in the Results section on diagram interpretation. The article reports the "mean accuracy was 32%" contrast and per-model extremes; no effect size is printed.

> "Across 19 models, the mean accuracy was 32%—less than half the text-only mean (67%). The weakest result (gpt-4.1) was 6% suggesting consistently chosen detractors, while the strongest (gpt-o3) reached76%"

## Discussion


## Related Claims
- [Strong models reliably solve canonical text-only thermodynamics items reducible to single state-function arguments](canonical-text-items-solved-reliably.md) — related
- [Text-only accuracy across 19 LLMs spans 0.20 to 0.88 with a grand mean of 0.67, stratified by model generation and reasoning budget](cross-model-text-only-accuracy-stratified.md) — related
- [No 2025-era LLM reaches a 95% accuracy threshold for unsupervised tutoring in undergraduate thermodynamics; the best model achieves 82%](no-llm-reaches-95-percent-thermodynamics-tutoring-threshold.md) — related
