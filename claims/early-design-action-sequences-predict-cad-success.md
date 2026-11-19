---
type: claim
title: "Logistic regression on the first 60% of a student's design action sequence predicts zero-net-energy design success with greater than 60% accuracy"
description: "Logistic regression on the first 60% of a student's design action sequence predicts zero-net-energy design success with greater than 60% accuracy"
id: early-design-action-sequences-predict-cad-success
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: jasmine-singh-2022
    resource: "https://doi.org/10.1002/cae.22489"
    title: "Jasmine Singh, Viranga Perera, Alejandra J. Magana, Brittany Newell, Jin Wei-Kocsis, Ying Ying Seah, Greg J. Strimel, and Charles Xie. (2022). Using Machine Learning to Predict Engineering Technology Students' Success with Computer Aided Design. Originally published 2021. [doi:10.1002/cae.22489](https://doi.org/10.1002/cae.22489)"
    author: Jasmine Singh, Viranga Perera, Alejandra J. Magana, Brittany Newell, Jin Wei-Kocsis, Ying Ying Seah, Greg J. Strimel, and Charles Xie
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Logistic regression on the first 60% of a student's design action sequence predicts zero-net-energy design success with greater than 60% accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using only the first 60% of students' design action sequences, logistic regression models achieved a 60% or greater chance of predicting whether a student would successfully design a zero net energy house. [→ Jasmine Singh 2022](#jasmine-singh-2022)

## Evidence

### Jasmine Singh 2022

Jasmine Singh, Viranga Perera, Alejandra J. Magana, Brittany Newell, Jin Wei-Kocsis, Ying Ying Seah, Greg J. Strimel, and Charles Xie. (2022). Using Machine Learning to Predict Engineering Technology Students' Success with Computer Aided Design. Originally published 2021. [doi:10.1002/cae.22489](https://doi.org/10.1002/cae.22489)

`q2 · i?` · `associational · r1`

Modeling study of JSON action logs from 128 students in the Fall 2020 ENGT 18000 energy module, using scikit-learn logistic regression with an 80-20 data split. The article reports that "If 60% of design action sequences are used, then our models have a 60% or greater chance of predicting success."

> "Our results show that even when using only the very beginning of students’ design action sequences (i.e., 10%), our models are generally better than chance at predicting if a particular student will successfully design a zero net energy house. If 60% of design action sequences are used, then our models have a 60% or greater chance of predicting success."

## Discussion


## Related Claims
- [Logistic regression on tallied design action counts predicts success with accuracy consistently above 50% and mostly above 65%](logistic-tallied-counts-above-chance.md) — related
- [A final net energy range of -10,000 to +10,000 kWh was adopted as the criterion for a successful zero net energy design](zero-net-energy-success-range-10000-kwh.md) — related
- [Linear regression on tallied design actions cannot accurately predict final net energy values](linear-regression-tallied-actions-inaccurate.md) — related
- [A logistic regression model using topic success and topic skip features predicts next-exercise success with 80% accuracy](logistic-regression-predicts-next-exercise-success-80-percent.md) — related
