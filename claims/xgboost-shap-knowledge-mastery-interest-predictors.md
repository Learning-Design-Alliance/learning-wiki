---
type: claim
title: An XGBoost model predicted post-class test performance well, with knowledge mastery and learning interest the strongest SHAP contributors
description: An XGBoost model predicted post-class test performance well, with knowledge mastery and learning interest the strongest SHAP contributors
id: xgboost-shap-knowledge-mastery-interest-predictors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: li-jialan-2025
    resource: "https://doi.org/10.1186/s12909-025-08440-9"
    title: "Li Jialan, Wu Ningling, Lu Jianyun, Tong Xiaoliang, Gao Lihua, Zeng Jinrong. (2025). Implementation and evaluation of a Sim + LBL hybrid teaching model in dermatology and venereology: a prospective study. BMC Medical Education. https://doi.org/10.1186/s12909-025-08440-9"
    author: Li Jialan, Wu Ningling, Lu Jianyun, Tong Xiaoliang, Gao Lihua, Zeng Jinrong
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# An XGBoost model predicted post-class test performance well, with knowledge mastery and learning interest the strongest SHAP contributors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The XGBoost regression model achieved R² = 0.82 on the independent test set, and SHAP analysis identified Q6 (knowledge mastery; mean SHAP = 4.60) and Q7 (learning interest; mean SHAP = 1.04) as the most influential predictors, with teaching modality contributing less (mean SHAP = 0.57). [→ Li Jialan 2025](#li-jialan-2025)

## Evidence

### Li Jialan 2025

Li Jialan, Wu Ningling, Lu Jianyun, Tong Xiaoliang, Gao Lihua, Zeng Jinrong. (2025). Implementation and evaluation of a Sim + LBL hybrid teaching model in dermatology and venereology: a prospective study. BMC Medical Education. https://doi.org/10.1186/s12909-025-08440-9

`q1 · i?` · `causal · r1`

Predictive modeling of PostScore using pre-test score, teaching modality, and Q3/Q4/Q6–Q8, with hyperparameters tuned by ten-fold cross-validated grid search; test-set RMSE = 3.99, MAE = 2.99, R² = 0.82 (Fig. 3a). SHAP values are model-derived contributions, not experimental effects.

> "SHAP analysis showed that Q6 (facilitation of knowledge mastery; mean SHAP = 4.60) and Q7 (stimulation of learning interest; mean SHAP = 1.04) were the most influential predictors of post-class performance."

## Discussion


## Related Claims
- [The effect of teaching modality on academic performance was fully mediated by perceived knowledge mastery and learning interest](mediation-knowledge-mastery-interest-full-mediation.md) — related
- [Sim + LBL students reported greater satisfaction, perceived learning outcomes, and core-competency gains than LBL students](sim-lbl-greater-satisfaction-engagement-competency.md) — related
- [Undergraduate students taught with the Sim + LBL hybrid model achieved higher total post-class test scores than students taught with traditional LBL in dermatology and venereology](sim-lbl-higher-total-post-class-scores.md) — related
- [SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance](shap-undergrad-gpa-rank-strongest-predictor.md) — related
- [SHAP modality attributions aligned with each BARS dimension's behavioral focus, supporting interpretable feedback](shap-modality-contributions-align-with-bars-dimensions.md) — related
