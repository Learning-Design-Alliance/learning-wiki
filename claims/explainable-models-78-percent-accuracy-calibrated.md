---
type: claim
title: "Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities"
description: "Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities"
id: explainable-models-78-percent-accuracy-calibrated
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: benjamin-mawdsley-2026
    resource: "https://doi.org/10.48550/arxiv.2607.26063"
    title: "Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063 [doi:10.48550/arxiv.2607.26063](https://doi.org/10.48550/arxiv.2607.26063)"
    author: Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: benjamin-mawdsley-2026-2
    resource: "https://arxiv.org/abs/2607.26063"
    title: "Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063"
    author: Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` All model classes perform broadly similarly, with the multi-question logistic regression best on accuracy at around 78% and the constant-probability baseline far below at 51.4%. [→ Benjamin Mawdsley 2026](#benjamin-mawdsley-2026)
`q2 i?` Model output probabilities are well calibrated, lying close to the ideal 1:1 line across probability bins for each model. [→ Benjamin Mawdsley 2026 (2)](#benjamin-mawdsley-2026-2)

## Evidence

### Benjamin Mawdsley 2026

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063 [doi:10.48550/arxiv.2607.26063](https://doi.org/10.48550/arxiv.2607.26063)

`q2 · i?` · `associational · r2`

Predictive evaluation across 13 mock exams with a 90/10 train-test split and 8-fold cross-validation; Table 1 reports LogRegm accuracy 0.778±0.005, LogRegs 0.769±0.005, KNN 0.775±0.005, BMM 0.776±0.005, Flat 0.514±0.015. The multi-question logistic regression "performs best" on accuracy.

> "For accuracy, the multi question logistic regression performs best, although all approaches have an accuracy of around 78%. This is much higher than the baseline model achieves (51.4%, not shown in plots due to the large difference in scale with other model performance changes)."

### Benjamin Mawdsley 2026 (2)

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063

`q2 · i?` · `associational · r2`

Calibration analysis comparing assigned probabilities to observed pass rates in bins of the test dataset (Figure 4), with binomial confidence intervals; the authors report "all models lie very close to the ideal line".

> "Well calibrated performance can be seen, where all models lie very close to the ideal line, across all probability bins and for each model."

## Discussion


## Related Claims
- [Cluster profiles of student mathematics performance are dominated by overall ability, with most clusters being linear rescalings of average exam performance](cluster-profiles-dominated-by-overall-ability.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons](oulad-calibrated-logistic-regression-strong-prediction.md) — related
- [Bernoulli Mixture Model fits select around 10-12 clusters per question, with no runs finding high cluster counts optimal, indicating specialised skill sets do not generally exist](bmm-selects-ten-to-twelve-clusters.md) — related
- [Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline](nonlinear-models-modest-auc-gains-over-logistic-baseline.md) — related
- [k-nearest neighbours achieves the highest recall of the tested models, making it better suited when identifying which students know a topic matters](knn-highest-recall-for-identifying-students.md) — related
- [Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model](small-gain-from-question-level-features.md) — related
