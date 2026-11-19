---
type: claim
title: "A U.S.-trained ridge regression model explains 60.8% of variance in U.S. science achievement and outperforms a forward-selected OLS model"
description: "A U.S.-trained ridge regression model explains 60.8% of variance in U.S."
id: ridge-model-60-8-variance-outperforms-ols
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: xingyu-li-2021
    resource: "https://doi.org/10.48550/arXiv.2103.15212"
    title: "Xingyu Li, Difan Song, Miaozhe Han, Yu Zhang, and René F. Kizilcec. (2021). On the limits of algorithmic prediction across the globe. Originally published 2020. [doi:10.48550/arXiv.2103.15212](https://doi.org/10.48550/arXiv.2103.15212)"
    author: Xingyu Li, Difan Song, Miaozhe Han, Yu Zhang, and René F. Kizilcec
    q: 2
    i: "?"
    kind: associational
    rigour: 3
---

# A U.S.-trained ridge regression model explains 60.8% of variance in U.S. science achievement and outperforms a forward-selected OLS model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The U.S.-trained ridge model achieved R2 = 0.608 on the U.S. test set, versus R2 = 0.497 for an OLS model with up to 20 forward-selected predictors. [→ Xingyu Li 2021](#xingyu-li-2021)

## Evidence

### Xingyu Li 2021

Xingyu Li, Difan Song, Miaozhe Han, Yu Zhang, and René F. Kizilcec. (2021). On the limits of algorithmic prediction across the globe. Originally published 2020. [doi:10.48550/arXiv.2103.15212](https://doi.org/10.48550/arXiv.2103.15212)

`q2 · i?` · `associational · r3`

Numerical evaluation of the ridge model on the held-out U.S. test set (Ntest = 1,140), using PV 1 in Science as the continuous outcome. The article prints RMSE = 60.53, RRSE = 0.63, MAE = 47.84, RAE = 0.60, R2 = 0.608. R2 is variance explained, not a standardized effect size, so impact is coded i? (no magnitude reported; not a null effect).

> "The U.S.-trained model performed well on the test set, RMSE = 60.53 (RRSE = 0.63), MAE = 47.84 (RAE = 0.60), and R2 = 0.608."

## Discussion


## Related Claims
- [A machine learning model using 105 predictors predicts next-year standardized math achievement with out-of-sample prediction R-squared of .70–.78](ml-model-predicts-next-year-math-achievement-r2-70-78.md) — related
- [In forward-selection regression, Reading is the most significant TEAS predictor of Fundamentals scores, and the four areas together account for approximately 19% of variance](reading-strongest-teas-regression-predictor-19-percent-variance.md) — related
- [Regression models explain 23.7% of overall achievement variance in primary school and 17.1% in secondary school](regression-variance-primary-secondary-achievement.md) — related
- [An ML ensemble model predicts MCAT scores with limited accuracy, explaining 36% of variance](ml-mcat-prediction-limited-accuracy.md) — related
- [In auxiliary Texas school data, a random forest with all predictors predicts math TAKS passing rates better than OLS with the pretest alone](rf-all-predictors-beats-pretest-auxiliary.md) — related
