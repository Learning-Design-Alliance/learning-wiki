---
type: claim
title: RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)
description: RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)
id: rag-systematic-leniency-overscoring
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

# RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` RAG exhibited positive bias in all four dimensions with all 95% bootstrap confidence intervals above zero, over-scoring 44.7% to 46.0% of responses across dimensions. [→ Baicheng Lin 2026](#baicheng-lin-2026)

## Evidence

### Baicheng Lin 2026

Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783

`q2 · i?` · `design · r2`

Bias analysis of RAG scores against teacher mean scores for the 300 responses, reported in Results section 4.4 and Table 5; total-score bias was 1.787 with over-scoring in "44.7% to 46.0% of responses across dimensions".

> "RAG showed a consistent positive bias in all four dimensions. All 95% bootstrap confidence intervals were above zero. This indicates systematic leniency relative to the teacher mean scores. Over-scoring occurred in 44.7% to 46.0% of responses across dimensions."

## Discussion


## Related Claims
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [Prompting strategies produce distinct directional bias profiles: Fs+CoT under-scores (bias = -1.730), RAG over-scores (bias = 1.787), and SC shows minimal directional bias (bias = -0.083)](strategy-specific-bias-profiles.md) — a broader claim this one bears on
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — related
