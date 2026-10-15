---
type: claim
title: Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87
description: Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87
id: feature-based-llm-models-outperform-direct-estimation-and-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: pooya-razavi-2025
    resource: "https://doi.org/10.1016/j.ijaied.2026.100015"
    title: "Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015"
    author: Pooya Razavi, Sonya Powers
    q: 2
    i: 3
    kind: associational
    rigour: 2
  - id: pooya-razavi-2025-2
    resource: "https://doi.org/10.1016/j.ijaied.2026.100015"
    title: "Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015"
    author: Pooya Razavi, Sonya Powers
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` For math, the feature-based random forest (RMSE = 0.83, MAE = 0.64; r = .87) beat the direct approach and all benchmarks; GBM was strongest overall, cutting RMSE 18.5% versus the dummy regressor on average. [→ Pooya Razavi 2025](#pooya-razavi-2025)
`q2 i3` For reading, the feature-based random forest (RMSE = 0.72, MAE = 0.58; r = .87) outperformed the direct approach and all benchmarks, reducing RMSE 31.6% versus the dummy regressor on average. [→ Pooya Razavi 2025 (2)](#pooya-razavi-2025-2)

## Evidence

### Pooya Razavi 2025

Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015

`q2 · i3` · `associational · r2`

Holdout evaluation of the math random forest on LLM-extracted features plus metadata; predicted estimates correlated r = .87 with true difficulties. The GBM performed similarly (RMSE = 0.81, MAE = 0.63, r = .87), and "the gradient boosting model emerges as the strongest performer".

> "produced an RMSE of 0.83 and MAE of 0.64, showing that the model’s predictions are more accurate than the ones from the previous approach (i.e., direct LLM estimation: RMSE = 0.91, MAE = 0.72)"

### Pooya Razavi 2025 (2)

Pooya Razavi, Sonya Powers. (2025). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. Edmentum. https://doi.org/10.1016/j.ijaied.2026.100015

`q2 · i3` · `design · r2`

Reading holdout results: the random forest beat the direct approach, dummy regressor, TF-IDF + RF (RMSE = 1.09), and metadata-only RF (RMSE = 0.87), with r = .87. "Compared to the dummy regressor, the random forest reduced RMSE by 31.6% on average".

> "produced an RMSE of 0.72 and MAE of 0.58, showing that the model outperforms the direct LLM estimation approach (RMSE = 0.86, MAE = 0.69), the dummy regressor benchmarks (RMSE = 1.04, MAE = 0.84)"

## Discussion


## Related Claims
- [Direct Llm Estimation Beats Dummy Regressor K5 Items](direct-llm-estimation-beats-dummy-regressor-k5-items.md)
- [Llm Features Add Value Beyond Item Metadata](llm-features-add-value-beyond-item-metadata.md)
- [Direct Llm Accuracy Varies By Grade Early Grades Worse](direct-llm-accuracy-varies-by-grade-early-grades-worse.md)
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
