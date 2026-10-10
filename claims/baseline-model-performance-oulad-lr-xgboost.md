---
type: claim
title: Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC
description: Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC
id: baseline-model-performance-oulad-lr-xgboost
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: raymond-a-opoku-2025
    resource: "https://doi.org/10.18608/jla.2025.8543"
    title: "Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543"
    author: Raymond A. Opoku, Bo Pei and Wanli Xing
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` LR achieved 75% accuracy (AUC-ROC 0.8328) and XGBoost 74% accuracy (AUC-ROC 0.8433) on the binary pass/fail prediction task. [→ Raymond A. Opoku 2025](#raymond-a-opoku-2025)

## Evidence

### Raymond A. Opoku 2025

Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

`q2 · i?` · `design · r2`

Baseline evaluation of LR and XGBoost on OULAD using 10-fold nested cross-validation (Tables 2-3, Figure 5). The article reports LR accuracy of 75% with AUC-ROC 0.8328 and XGBoost accuracy of 74% with AUC-ROC 0.8433. AUC/accuracy values are not standardized effect sizes.

> "The AUC-ROC score for the XGBoost model is 0.8433, which is slightly higher than that of the LR model, indicating marginally better performance in distinguishing between the pass and fail classes."

## Discussion


## Related Claims
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](baseline-ml-models-biased-tpr-oulad.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96](gradient-boosting-best-enrollment-predictor-aid-optimization.md) — related
- [Percentile heuristics transferred from health behavior systematically overpredict weekly K-12 engagement and underperform XGBoost by 20-30%](percentile-heuristics-overpredict-weekly-engagement.md) — related
