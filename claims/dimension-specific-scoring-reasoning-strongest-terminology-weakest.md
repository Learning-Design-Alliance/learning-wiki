---
type: claim
title: "LLM scoring performance is dimension-specific: Reasoning shows the strongest agreement and Terminology the weakest across all three strategies"
description: "LLM scoring performance is dimension-specific: Reasoning shows the strongest agreement and Terminology the weakest across all three strategies"
id: dimension-specific-scoring-reasoning-strongest-terminology-weakest
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

# LLM scoring performance is dimension-specific: Reasoning shows the strongest agreement and Terminology the weakest across all three strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across all three prompting strategies, Reasoning generally showed the strongest agreement with teacher mean scores while Terminology showed the lowest agreement. [→ Baicheng Lin 2026](#baicheng-lin-2026)

## Evidence

### Baicheng Lin 2026

Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783

`q2 · i?` · `design · r2`

Dimension-level analysis in Results Table 2 for the 300 responses: e.g., Fs+CoT Reasoning ICC (2,1) = 0.802 versus Terminology ICC (2,1) = 0.661; SC Terminology ICC (2,1) = 0.458. The article concludes scoring performance "was dimension-specific rather than uniform across the rubric."

> "Across all three prompting strategies, Reasoning generally showed the strongest agreement with teacher mean scores. Terminology showed the lowest agreement for all three strategies."

## Discussion


## Related Claims
- [The automated scoring system's agreement with human raters varied widely by dimension, with information fidelity showing a weak, non-significant correlation](yunyi-human-agreement-varies-by-dimension.md) — a broader claim this one bears on
- [LLM-human agreement is highest for identifying whether students listed a concept and lowest for judging definition correctness](coding-dimension-listing-easier-than-correct-defining.md) — a broader claim this one bears on
- [Across rubric dimensions, content scored highest (A = 4.03) while production scored lowest (D = 3.41), driven by synthetic voice quality (D1 = 3.16)](bespoke-content-strongest-production-weakest-voice.md) — related
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [Median aggregation across three runs produces only minor changes in agreement and does not alter the ordering of prompting strategies](median3r-aggregation-minor-effect-ordering-preserved.md) — related
