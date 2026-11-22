---
type: claim
title: An XGBoost model on spatial metrics fails to predict burst pressure, indicating spatial metrics alone are insufficient standalone indicators of suture quality
description: An XGBoost model on spatial metrics fails to predict burst pressure, indicating spatial metrics alone are insufficient standalone indicators of suture quality
id: xgboost-spatial-metrics-poor-burst-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: spagnulo-r-2025
    resource: "https://doi.org/10.1007/s00464-025-12441-6"
    title: "Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A. (2025). From precision to strength: computer vision for suture quality assessment—an ex vivo pilot study. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12441-6"
    author: Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# An XGBoost model on spatial metrics fails to predict burst pressure, indicating spatial metrics alone are insufficient standalone indicators of suture quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Spagnulo R 2025: no comparison group (read from the study by two models, 2026-11-22)

## Subclaims
`q2 i?` The regression model performed poorly (R2 = −0.42, MSE = 93.7) with high multicollinearity (VIF > 10) among predictors. [→ Spagnulo R 2025](#spagnulo-r-2025)

## Evidence

### Spagnulo R 2025

Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A. (2025). From precision to strength: computer vision for suture quality assessment—an ex vivo pilot study. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12441-6

`q2 · i?` · `causal · r1`

XGBoost regression with repeated 5-fold cross-validation (10 repeats, 80/20 splits) on the significant spatial features from the 45-procedure dataset. Overall performance was poor (R2 = −0.42, MSE = 93.7, fold MSE range 26.8–232.3); SHAP identified P all max error and PM mean error as most influential (mean |SHAP| 1.86 and 1.85).

> "only 10 out of 50 folds yielding a positive coefficient of determination (R2 > 0.1), while the overall model performance was poor (R2 = -0.42 and MSE = 93.7), suggesting that it fails to explain variance in the target"

## Discussion


## Related Claims
- [Operator experience level is not associated with suture burst pressure differences](experience-no-burst-pressure-difference.md) — related
- [Objective performance indicators alone poorly predict robotic ventral hernia case complexity compared with clinical factors (F1 0.58 vs 0.87)](opi-alone-poor-predictor-hernia-case-complexity.md) — a broader claim this one bears on
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
- [Logistic regression performs poorly (mean accuracy 0.4243) and SVM moderately (0.7374) on physiological exam-outcome prediction](logistic-regression-poor-svm-moderate-physiological-exam-prediction.md) — related
