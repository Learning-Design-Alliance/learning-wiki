---
type: claim
title: Xgboost more accurately predicts graduating semesters for female students, under-represented minority students, and students with missing high school GPA than logistic regression
description: Xgboost more accurately predicts graduating semesters for female students, under-represented minority students, and students with missing high school GPA than logistic regression
id: xgboost-subgroup-recall-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: aiken-2020
    resource: "https://doi.org/10.1371/journal.pone.0242334"
    title: "Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)"
    author: Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: aiken-2020-2
    resource: "https://doi.org/10.1371/journal.pone.0242334"
    title: "Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)"
    author: Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: aiken-2020-3
    resource: "https://doi.org/10.1371/journal.pone.0242334"
    title: "Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)"
    author: Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Xgboost more accurately predicts graduating semesters for female students, under-represented minority students, and students with missing high school GPA than logistic regression

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` By out-of-sample recall, xgboost better predicts graduating semesters for women (all semesters except 16), under-represented minority students (all semesters), and students with missing high school GPA. [→ Aiken 2020](#aiken-2020)

## Evidence

### Aiken 2020

Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)

`q2 · i?` · `associational · r2`

Sub-population recall comparison of the two models (Fig. 6). The article reports xgboost is more effective for female students "for all semesters except for semester 16"; no effect size is printed.

> "Xgboost is more effective at correctly predicting the graduating semester of female students as assessed by the out-of-sample recall for all semesters except for semester 16 (Fig. 6)."

### Aiken 2020 (2)

Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)

`q2 · i?` · `associational · r2`

Sub-population recall comparison (Fig. 6): xgboost is more effective for under-represented minority students "for all semesters"; no effect size is printed.

> "Xgboost is also more effective at correctly predicting the graduating semester of under represented minority students for all semesters (Fig. 6)."

### Aiken 2020 (3)

Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)

`q2 · i?` · `associational · r2`

Sub-population recall comparison (Fig. 6): xgboost handles missing-data cases "better than the logistic regression model for all semesters"; no effect size is printed.

> "Additionally, Xgboost is able to handle missing data cases better than the logistic regression model for all semesters (Fig. 6)."

## Discussion


## Related Claims
- [Gradient boosted trees (xgboost) outperform maximum-likelihood logistic regression at predicting graduating semester by out-of-sample F1-score, except in semesters 15-16](xgboost-outperforms-mle-time-to-graduation.md) — a broader claim this one bears on
- [XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set](xgboost-comparable-to-logistic-regression.md) — reports the opposite
- [Models exhibit a recall–precision trade-off: Logistic Regression and Naïve Bayes maximize recall (0.94) with more false positives, while XGBoost balances recall with stronger precision](recall-precision-tradeoff-early-warning-models.md) — related
- [Enrollment factors predict time-to-graduation about twice as strongly as preparation factors](enrollment-factors-outweigh-preparation-graduation-timing.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
