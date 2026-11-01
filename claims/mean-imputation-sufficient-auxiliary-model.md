---
type: claim
title: Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation
description: Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation
id: mean-imputation-sufficient-auxiliary-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: c-z-mann-2024
    resource: "https://github.com/manncz/aeis-aux-rct"
    title: "C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct"
    author: C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Random forest missing value imputation did not improve model performance meaningfully over simple mean imputation while costing substantially more computing time. [→ C. Z. Mann 2024](#c-z-mann-2024)

## Evidence

### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct

`q2 · i?` · `causal · r2`

Missing-data handling comparison during auxiliary model development, evaluating mean imputation and missForest random forest imputation by the MSE and R2 of random forest and neural net predictions for middle and high schools. Missing values were ultimately replaced with 0 after centering and scaling.

> "using random forest missing value imputation did not improve model performance meaningfully over sim- ple mean imputation, while taking substantially more com- puting power and time."

## Discussion


## Related Claims
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](rct-only-all-covariates-hurt-precision.md) — related
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
- [Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data](random-forests-outperform-neural-nets-auxiliary.md) — related
