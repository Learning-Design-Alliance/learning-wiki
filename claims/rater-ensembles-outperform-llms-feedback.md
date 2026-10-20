---
type: claim
title: "Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects"
description: "Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects"
id: rater-ensembles-outperform-llms-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: stefano-bannò-2026
    resource: "https://doi.org/10.48550/arxiv.2605.04298"
    title: "Stefano Bannò, Kate Knill, Mark Gales. (2026). Towards Self-Referential Analytic Assessment: A Profile-Based Approach to L2 Writing Evaluation with LLMs. https://arxiv.org/abs/2605.04298 [doi:10.48550/arxiv.2605.04298](https://doi.org/10.48550/arxiv.2605.04298)"
    author: Stefano Bannò, Kate Knill, Mark Gales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When averaging performance across aspects, an ensemble of two operational raters is sufficient to outperform the LLMs; for individual aspects such as Logicality, an ensemble of three raters is needed. [→ Stefano Bannò 2026](#stefano-banno-2026)

## Evidence

### Stefano Bannò 2026

Stefano Bannò, Kate Knill, Mark Gales. (2026). Towards Self-Referential Analytic Assessment: A Profile-Based Approach to L2 Writing Evaluation with LLMs. https://arxiv.org/abs/2605.04298 [doi:10.48550/arxiv.2605.04298](https://doi.org/10.48550/arxiv.2605.04298)

`q2 · i?` · `design · r2`

Ensemble analysis in the Experimental results section (Tables 11 and 12, Figure 2 errorbars for Logicality): OR2 averages 37.19 (negative) and 38.56 (positive) F0.5, exceeding all LLM averages; OR3 averages 46.48 and 47.84.

> "When averaging performance across aspects, an ensemble of two operational raters is sufficient to outperform the LLMs. However, considering individual aspects, as in Figure 2, larger ensembles are required."

## Discussion


## Related Claims
- [Human operational raters remain stronger than LLMs at identifying relative strengths (positive feedback) within learner profiles](human-raters-stronger-positive-feedback.md) — reports the opposite
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — related
- [Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning](ensembling-worsens-llm-alignment-with-learning.md) — related
- [In a self-referential framework, LLMs, particularly GPT-4.1, tend to outperform a single operational human rater at identifying relative weaknesses (negative feedback) across several Language and Content aspects](llms-outperform-single-rater-negative-feedback.md) — related
- Majority-vote ensembling across three runs produced only modest accuracy gains (1% to 5%) with no model showing degradation — related
- [Model self-confidence, weighted probabilistic scoring, and ensemble modeling each significantly improve LLM-based divergent thinking scoring, raising correlation with human judges from r = 0.781 to r = 0.823](llm-scoring-three-techniques-raise-human-judge-correlation.md) — related
- [Rank-based metrics can be misleading for analytic assessment: systems prompted for holistic scoring achieve strong, sometimes stronger, correlations with analytic scores than when prompted for those aspects](rank-based-metrics-misleading-analytic-assessment.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
