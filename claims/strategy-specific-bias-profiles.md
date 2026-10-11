---
type: claim
title: "Prompting strategies produce distinct directional bias profiles: Fs+CoT under-scores (bias = -1.730), RAG over-scores (bias = 1.787), and SC shows minimal directional bias (bias = -0.083)"
description: "Prompting strategies produce distinct directional bias profiles: Fs+CoT under-scores (bias = -1.730), RAG over-scores (bias = 1.787), and SC shows minimal directional bias (bias = -0.083)"
id: strategy-specific-bias-profiles
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: baicheng-lin-2026
    resource: "https://arxiv.org/abs/2608.01783"
    title: "Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783"
    author: Baicheng Lin, Lingxi Jin, and Kyung-Seok Min
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompting strategies produce distinct directional bias profiles: Fs+CoT under-scores (bias = -1.730), RAG over-scores (bias = 1.787), and SC shows minimal directional bias (bias = -0.083)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Systematic bias differed by strategy: Fs+CoT was relatively severe, RAG relatively lenient, and SC closest to teacher mean scores in overall score location with minimal directional bias. [→ Baicheng Lin 2026](#baicheng-lin-2026)

## Evidence

### Baicheng Lin 2026

Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783

`q2 · i?` · `design · r2`

Bias analysis across the 300 responses (Results section 4.4, Table 5): Fs+CoT total bias -1.730 with 77.3% under-scoring; RAG total bias 1.787 with 73.7% over-scoring; SC total bias -0.083 with bootstrap CIs including zero in all four dimensions.

> "Fs+CoT under-scored relative to teacher mean scores (bias = -1.730), RAG over-scored (bias = 1.787), and SC showed minimal directional bias (bias = -0.083)."

## Discussion


## Related Claims
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [Median aggregation across three runs produces only minor changes in agreement and does not alter the ordering of prompting strategies](median3r-aggregation-minor-effect-ordering-preserved.md) — related
- [RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)](rag-systematic-leniency-overscoring.md) — a narrower finding that bears on this claim
