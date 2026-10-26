---
type: claim
title: The scheduling model fit the experimental data well, correlating strongly with actual final-test performance (r = 0.775) with AUC = 0.871
description: The scheduling model fit the experimental data well, correlating strongly with actual final-test performance (r = 0.775) with AUC = 0.871
id: model-fit-recall-prediction-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: luke-g-eglington-and-philip-i-pavlik-jr-2020
    resource: "https://doi.org/10.1038/s41539-020-00074-4"
    title: "Luke G. Eglington and Philip I. Pavlik Jr. (2020). Optimizing practice scheduling requires quantitative tracking of individual item performance. npj Science of Learning 5:15. https://doi.org/10.1038/s41539-020-00074-4"
    author: Luke G. Eglington and Philip I. Pavlik Jr
    q: 3
    i: 3
    kind: causal
    rigour: "?"
---

# The scheduling model fit the experimental data well, correlating strongly with actual final-test performance (r = 0.775) with AUC = 0.871

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q3` · `i3` large
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i3` Predicted and actual average final-test performance correlated at r = 0.775, and the model achieved AUC = 0.871. [→ Luke G. Eglington and Philip I. Pavlik Jr 2020](#luke-g-eglington-and-philip-i-pavlik-jr-2020)

## Evidence

### Luke G. Eglington and Philip I. Pavlik Jr 2020

Luke G. Eglington and Philip I. Pavlik Jr. (2020). Optimizing practice scheduling requires quantitative tracking of individual item performance. npj Science of Learning 5:15. https://doi.org/10.1038/s41539-020-00074-4

`q3 · i3` · `causal · r?`

Model-fit analysis of Experiment 2 data: "a strong correlation between predicted and actual average performance on the ﬁnal test, r = 0.775"; McFadden's pseudo-R² was 0.37, within the range considered evidence of good fit.

> "There was a strong correlation between predicted and actual average performance on the ﬁnal test, r = 0.775, p < 0.001. An analysis of the sensitivity and speci ﬁcity of the model also indicated a good ﬁt, AUC = 0.871, 95% con ﬁdence interval = 0.868–0.874."

## Discussion


## Related Claims
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons](oulad-calibrated-logistic-regression-strong-prediction.md) — related
