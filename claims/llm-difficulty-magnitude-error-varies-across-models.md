---
type: claim
title: Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)
description: Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)
id: llm-difficulty-magnitude-error-varies-across-models
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: la-hadi-2025
    resource: "https://doi.org/10.48550/arxiv.2607.26067"
    title: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)"
    author: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` RMSE and MAE values vary notably across LLM models, so correlation alone overstates practical predictive accuracy of difficulty magnitude. [→ La Hadi 2025](#la-hadi-2025)

## Evidence

### La Hadi 2025

La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2025). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)

`q2 · i?` · `associational · r2`

Analysis of the same four-model comparison against empirical IRT difficulty reports that "RMSE and MAE values vary notably across models"; Table 1 shows RMSE (IRT) from 0.809 to 0.974 and MAE from 0.638 to 0.727.

> "RMSE and MAE values vary notably across models (Table 1), showing that models with similar correlations differ in their ability to estimate difficulty magnitude."

## Discussion


## Related Claims
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
- [CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation](irt-validates-ctt-quiz-difficulty-ranking.md) — related
- CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations — related
- [GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts](gpt-4o-mini-lowest-act-balance-mae.md) — related
- [Teacher value-added estimates are highly correlated across model specifications that differ in student and peer control variables](vam-estimates-highly-correlated-across-specifications.md) — related
- [Exploratory analysis found item difficulty differed across sources, driven by the Google Gemini versus NLE contrast](item-difficulty-differs-across-sources-gemini-nle.md) — related
