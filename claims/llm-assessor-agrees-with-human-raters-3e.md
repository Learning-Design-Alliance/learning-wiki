---
type: claim
title: An automated LLM assessor rates 3E clinical communication skills with agreement comparable to individual human raters
description: An automated LLM assessor rates 3E clinical communication skills with agreement comparable to individual human raters
id: llm-assessor-agrees-with-human-raters-3e
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: masum-hasan-2026
    resource: "https://doi.org/10.48550/arxiv.2609.22517"
    title: "Masum Hasan, Ron Epstein, Thomas Carroll, Ehsan Hoque. (2026). Scalable AI-based clinical communication training and automated assessment. https://arxiv.org/abs/2609.22517 [doi:10.48550/arxiv.2609.22517](https://doi.org/10.48550/arxiv.2609.22517)"
    author: Masum Hasan, Ron Epstein, Thomas Carroll, Ehsan Hoque
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An automated LLM assessor rates 3E clinical communication skills with agreement comparable to individual human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The selected LLM judge achieved a Pearson correlation of 0.759 and an ICC(A,1) of 0.746 with the consensus of human raters, ranking within the upper range of the six human rating sources. [→ Masum Hasan 2026](#masum-hasan-2026)

## Evidence

### Masum Hasan 2026

Masum Hasan, Ron Epstein, Thomas Carroll, Ehsan Hoque. (2026). Scalable AI-based clinical communication training and automated assessment. https://arxiv.org/abs/2609.22517 [doi:10.48550/arxiv.2609.22517](https://doi.org/10.48550/arxiv.2609.22517)

`q2 · i?` · `design · r2`

Leave-one-rater-out validation analysis comparing the selected LLM judge (GPT-5.4 low reasoning) against human rating sources. The judge "achieved a Pearson correlation of 0.759" and ICC(A,1) of 0.746; it ranked third of six sources for correlations and had the lowest MAE (0.106).

> "Relative to the consensus of all human rating sources, the LLM achieved a Pearson correlation of 0.759, a Spearman correlation of 0.720, an MAE of 0.106, and an ICC(A,1) of 0.746 (95% CI, 0.640–0.830)."

## Discussion


## Related Claims
- [HAL's text-based human-likeness advantage did not transfer to embodied audiovisual interaction, and measured 3E performance was virtually identical between models](hal-human-likeness-did-not-transfer-embodied.md) — related
- [Participants with prior communication-training experience achieved higher overall 3E scores than those without](prior-training-higher-3e-scores.md) — related
- [AI assessors show emerging reliability: acceptable AI-human rater agreement (Cohen's 0.78) in a 12-educator case study and human-comparable feedback helpfulness ratings with 45 learners](agentic-assessment-rater-agreement-and-helpfulness.md) — related
