---
type: claim
title: In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone
description: In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone
id: rf-all-predictors-beats-pretest-auxiliary
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
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

# In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Including the full predictor set in a random forest reduced unexplained variance in 2008 TAKS passing rates by an additional 10-15% over pretest-only OLS. [→ C. Z. Mann 2024](#c-z-mann-2024)

## Evidence

### C. Z. Mann 2024

C. Z. Mann, J. Wang, A. Sales, and J. A. Gagnon-Bartsch. (2024). Using publicly available auxiliary data to improve precision of treatment effect estimation in a randomized efficacy trial. Proceedings of the 17th International Conference on Educational Data Mining. https://github.com/manncz/aeis-aux-rct

`q2 · i?` · `causal · r2`

10-fold cross-validation on auxiliary Texas schools (1,436 middle, 1,467 high): pretest OLS had R2 of 0.54 (middle) and 0.56 (high); the all-predictors random forest had R2 of 0.65 and 0.72, with lower MSE (Table 1).

> "Table 1 shows that the pretest alone explains more than 50% of the variance in the 2008 TAKS passing rates for middle and high schools, using OLS. However, including the full set of predictors in a random forest model reduces the unexplained variance by an additional 10-15%."

## Discussion


## Related Claims
- [Variable importance from the auxiliary model indicates the student cohort matters most for predicting middle school math passing rates, while demographics matter for high schools](cohort-importance-middle-school-auxiliary-model.md) — related
- [Random forest imputation of missing predictor values did not meaningfully improve auxiliary model performance over simple mean imputation](mean-imputation-sufficient-auxiliary-model.md) — related
- [Random forest models consistently outperform neural networks for predicting math TAKS passing rates in the auxiliary data](random-forests-outperform-neural-nets-auxiliary.md) — related
- [Fitting an imputation model with all covariates using only the small trial sample reduces precision relative to pretest-only adjustment](rct-only-all-covariates-hurt-precision.md) — related
- [A machine learning model using 105 predictors predicts next-year standardized math achievement with out-of-sample prediction R-squared of .70–.78](ml-model-predicts-next-year-math-achievement-r2-70-78.md) — related
