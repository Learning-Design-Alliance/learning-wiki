---
type: claim
title: Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment
description: Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment
id: rct-only-all-covariates-hurt-precision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2024
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

# Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A random forest imputation model using all covariates from the RCT sample alone produced a less precise effect estimate than adjusting for only the pretest. [→ C. Z. Mann 2024](#c-z-mann-2024)

## Evidence

### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct

`q2 · i?` · `causal · r2`

Trial-only comparison for the 44 Texas CTAI schools: the all-covariates random forest estimator had estimated variance 8.03 and relative efficiency 0.70 versus pretest-only adjustment (Tables 2-3).

> "Although including all possible covariates decreased prediction MSE in the auxiliary data, the trial data is so small that the imputation model with all covariates is noisy, and therefore hurts precision."

## Discussion


## Related Claims
- [Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation](mean-imputation-sufficient-auxiliary-model.md) — related
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
- [Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data](random-forests-outperform-neural-nets-auxiliary.md) — related
