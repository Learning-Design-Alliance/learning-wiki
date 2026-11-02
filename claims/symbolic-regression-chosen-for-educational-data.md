---
type: claim
title: Symbolic regression was chosen over other machine-learning algorithms because it yields explicit human-interpretable models without assuming a model form, suiting small, missing-value-prone educational datasets
description: Symbolic regression was chosen over other machine-learning algorithms because it yields explicit human-interpretable models without assuming a model form, suiting small, missing-value-prone educational datasets
id: symbolic-regression-chosen-for-educational-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-02
evidence_strength: weak
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: fedor-duzhin-and-anders-gustafsson-2018
    resource: "https://doi.org/10.3390/educsci8010007"
    title: "Fedor Duzhin and Anders Gustafsson. (2018). Machine Learning-Based App for Self-Evaluation of Teacher-Specific Instructional Style and Tools. Educ. Sci. 2018, 8, 7. https://doi.org/10.3390/educsci8010007"
    author: Fedor Duzhin and Anders Gustafsson
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Symbolic regression was chosen over other machine-learning algorithms because it yields explicit human-interpretable models without assuming a model form, suiting small, missing-value-prone educational datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors argue that small datasets rule out neural networks, missing entries rule out support vector machines, overfitting risk rules out random forests, unknown model form rules out classical regression, and the need for feature selection rules out k-nearest neighbours, leaving symbolic regression. [→ Fedor Duzhin and Anders Gustafsson 2018](#fedor-duzhin-and-anders-gustafsson-2018)

## Evidence

### Fedor Duzhin and Anders Gustafsson 2018

Fedor Duzhin and Anders Gustafsson. (2018). Machine Learning-Based App for Self-Evaluation of Teacher-Specific Instructional Style and Tools. Educ. Sci. 2018, 8, 7. https://doi.org/10.3390/educsci8010007

`q1 · i?` · `design · r2`

Methodological argument (type d/e) in Section 2, weighing the constraints of educational quasi-experiment data: small datasets, missing entries, overfitting risk, unknown model form, and desired feature selection. Symbolic regression models are explicit equations in terms of predictors.

> "We have chosen a machine learning algorithm that produces explicit human-interpretable models and yet does not assume any speciﬁc form in advance— symbolic regression"

## Discussion


## Related Claims
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
