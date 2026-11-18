---
type: claim
title: Enrollment factors predict time-to-graduation about twice as strongly as preparation factors
description: Enrollment factors predict time-to-graduation about twice as strongly as preparation factors
id: enrollment-factors-outweigh-preparation-graduation-timing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: aiken-2020
    resource: "https://doi.org/10.1371/journal.pone.0242334"
    title: "Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)"
    author: Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Enrollment factors predict time-to-graduation about twice as strongly as preparation factors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the xgboost model's F1-weighted feature importances, enrollment features contribute roughly half again more than preparation features to predicting graduating semester. [→ Aiken 2020](#aiken-2020)

## Evidence

### Aiken 2020

Aiken, J. M., De Bin, R., Hjorth-Jensen, M., Caballero, M. D. (2020). Predicting time to graduation at a large enrollment American university. arXiv. [doi:10.1371/journal.pone.0242334](https://doi.org/10.1371/journal.pone.0242334)

`q2 · i?` · `associational · r2`

Feature-importance analysis of the xgboost discrete-time hazard model, with per-semester importances weighted by out-of-sample F1-score and averaged over 11 semesters. The article states preparation is "about half as important in predicting when a student graduates in comparison to enrollment factors"; no effect size is printed.

> "Preparation is about half as important in predicting when a student graduates in comparison to enrollment factors (Fig. 7)."

## Discussion


## Related Claims
- [Math placement score and high school GPA predict early graduation, while AP credits do not strongly predict graduating early](preparation-predicts-early-graduation-not-ap-credits.md) — related
- [Cumulative credit hours near 120 are the strongest predictor of on-time graduation (semesters 8-10)](cumulative-credit-hours-predict-on-time-graduation.md) — related
- [Changing a major becomes more important for predicting graduation in later graduating semesters](major-change-predicts-later-graduation.md) — related
- [Gradient boosted trees (xgboost) outperform maximum-likelihood logistic regression at predicting graduating semester by out-of-sample F1-score, except in semesters 15-16](xgboost-outperforms-mle-time-to-graduation.md) — related
- [Xgboost more accurately predicts graduating semesters for female students, under-represented minority students, and students with missing high school GPA than logistic regression](xgboost-subgroup-recall-advantage.md) — related
