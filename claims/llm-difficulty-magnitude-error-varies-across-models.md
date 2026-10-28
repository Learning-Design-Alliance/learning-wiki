---
type: claim
title: Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)
description: Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)
id: llm-difficulty-magnitude-error-varies-across-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

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
- [GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error](turn-level-convergence-gpt-4o-mini.md) — related
- [Rank orderings of teachers do not change radically under mild scale transformations](teacher-rank-orderings-robust-to-mild-transformations.md) — related
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
- [Zero-shot GPT-4o difficulty ratings, rescaled and entered in grade-specific regressions, beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related
