---
type: claim
title: Gradient boosted logistic regression outperforms fixed-effects and mixed-effects logistic regression in classifying introductory vs beyond-first-year E-CLASS students, though all models fall below excellent discrimination
description: Gradient boosted logistic regression outperforms fixed-effects and mixed-effects logistic regression in classifying introductory vs beyond-first-year E-CLASS students, though all models fall below excellent discrimina...
id: eclass-boosted-logistic-best-auc
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: john-m-aiken-2021
    resource: "https://doi.org/10.1103/physrevphyseducres.17.020104"
    title: "John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)"
    author: John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Gradient boosted logistic regression outperforms fixed-effects and mixed-effects logistic regression in classifying introductory vs beyond-first-year E-CLASS students, though all models fall below excellent discrimination

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The gradient boosted logistic regression model performs the best (AUC=0.798) and the mixed effects logistic regression model the worst (AUC=0.581), with the fixed effects model at AUC=0.773; all three are below the AUC>0.8 excellent-discrimination threshold. [→ John M. Aiken 2021](#john-m-aiken-2021)

## Evidence

### John M. Aiken 2021

John M. Aiken, Riccardo De Bin, H. J. Lewandowski, and Marcos D. Caballero. (2021). A Framework for Evaluating Statistical Models in Physics Education Research. [doi:10.1103/physrevphyseducres.17.020104](https://doi.org/10.1103/physrevphyseducres.17.020104)

`q2 · i?` · `associational · r2`

Binary classification study using E-CLASS data (N=10148 matched pre/post responses after reduction), predicting whether a student is in an introductory or BFY course from demographics, career-plan responses, and institution type, evaluated with 5-fold cross-validated ROC/AUC. The article reports all three models are below an "excellent discrimination" (AUC>0.8) as identified by Hosmer Jr et al.

> "Overall the gradient boosted logistic regression model performs the best (AUC=0.798), while the mixed eﬀects logistic regression model performed the worst (AUC=0.581). The ﬁxed eﬀects logistic regression model performs similar (AUC=0.773), but slightly worse, as compared to the gradient boosted model."

## Discussion


## Related Claims
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](boosting-highest-accuracy-logistic-lowest.md) — related
