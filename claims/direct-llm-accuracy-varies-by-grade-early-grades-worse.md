---
type: claim
title: Direct LLM estimation accuracy varies by grade, performing worse for early grades; math grade K was worse than the dummy regressor and math grade 1 showed no significant prediction
description: Direct LLM estimation accuracy varies by grade, performing worse for early grades; math grade K was worse than the dummy regressor and math grade 1 showed no significant prediction
id: direct-llm-accuracy-varies-by-grade-early-grades-worse
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: pooya-razavi-2026
    resource: "https://doi.org/10.1016/j.ijaied.2026.100015"
    title: "Pooya Razavi, Sonya Powers. (2026). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. *International Journal of Artificial Intelligence in Education, 36*, 100015. https://doi.org/10.1016/j.ijaied.2026.100015"
    author: Pooya Razavi, Sonya Powers
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: pooya-razavi-2026-2
    resource: "https://doi.org/10.1016/j.ijaied.2026.100015"
    title: "Pooya Razavi, Sonya Powers. (2026). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. *International Journal of Artificial Intelligence in Education, 36*, 100015. https://doi.org/10.1016/j.ijaied.2026.100015"
    author: Pooya Razavi, Sonya Powers
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Direct LLM estimation accuracy varies by grade, performing worse for early grades; math grade K was worse than the dummy regressor and math grade 1 showed no significant prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For math grade K, both error indices exceeded the dummy regressor benchmarks, and grade 1 errors were only minimally better than benchmarks. [→ Pooya Razavi 2026](#pooya-razavi-2026)
`q2 i?` In the per-grade training regressions, GPT estimates did not significantly predict true difficulty for math grade 1 (p = 0.369), and reading R2 ranged from .02 (grade 1) to .45 (grade 3). [→ Pooya Razavi 2026 (2)](#pooya-razavi-2026-2)

## Evidence

### Pooya Razavi 2026

Pooya Razavi, Sonya Powers. (2026). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. *International Journal of Artificial Intelligence in Education, 36*, 100015. https://doi.org/10.1016/j.ijaied.2026.100015

`q2 · i?` · `associational · r2`

By-grade holdout analysis of the direct approach for math. "both error indices for grade K were higher than the benchmarks"; grade 1 errors were minimally better, while grades 2-5 improved on the dummy regressor by at least 0.08 points.

> "Importantly, both error indices for grade K were higher than the benchmarks, showing that even though this grade has the lowest RMSE and MAE, the prediction accuracy is worse than a model predicting item difficulties based on grade averages."

### Pooya Razavi 2026 (2)

Pooya Razavi, Sonya Powers. (2026). Estimating Item Difficulty Using Large Language Models and Tree-Based Machine Learning Algorithms. *International Journal of Artificial Intelligence in Education, 36*, 100015. https://doi.org/10.1016/j.ijaied.2026.100015

`q2 · i?` · `associational · r2`

Training-set regressions predicting true difficulty from rescaled GPT estimates per subject and grade (Table 4). Math grade 1 was the exception: F(1,261) = 0.81, p = 0.369, so GPT estimates did not significantly predict true estimates there.

> "For math, the adjusted R2 values of the significant models ranged from .11 for grade 5 to .23 for grade 4. For reading, the R2 varied between .02 (grade 1) to .45 (grade 3)."

## Discussion


## Related Claims
- [Direct Llm Estimation Beats Dummy Regressor K5 Items](direct-llm-estimation-beats-dummy-regressor-k5-items.md)
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
