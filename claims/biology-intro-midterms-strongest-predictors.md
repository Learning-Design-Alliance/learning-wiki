---
type: claim
title: Biology and Introduction to Health Sciences midterm scores are the strongest predictors of at-risk classification, with SHAP analyses showing the largest case-level impact
description: Biology and Introduction to Health Sciences midterm scores are the strongest predictors of at-risk classification, with SHAP analyses showing the largest case-level impact
id: biology-intro-midterms-strongest-predictors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: al-hashmi-reem-a-m-2025
    resource: "https://doi.org/10.1186/s12909-025-08192-6"
    title: "Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M. (2025). Early detection of at-risk health sciences students: a machine learning-based predictive study using midterm grades. BMC Medical Education. https://doi.org/10.1186/s12909-025-08192-6"
    author: Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M.
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Biology and Introduction to Health Sciences midterm scores are the strongest predictors of at-risk classification, with SHAP analyses showing the largest case-level impact

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across models, the Biology midterm emerged as the single most influential predictor, followed by Introduction to Health Sciences and English midterms, while demographic variables carried negligible weight. [→ Al Hashmi Reem A. M. 2025](#al-hashmi-reem-a-m-2025)

## Evidence

### Al Hashmi Reem A. M. 2025

Al Hashmi Reem A. M., Ozturk Ilhan, Elmehdi Hussein M. (2025). Early detection of at-risk health sciences students: a machine learning-based predictive study using midterm grades. BMC Medical Education. https://doi.org/10.1186/s12909-025-08192-6

`q2 · i?` · `associational · r1`

Post-hoc TreeSHAP analysis on the held-out test set for the trained XGBoost model, reported as interpretability analysis only and not used for model selection. Biology midterm showed mean |SHAP| ≈ 1.37, Introduction to Health Sciences ≈ 1.00, English ≈ 0.81.

> "Biology midterm exhibited the largest average absolute contribution to the model output (mean |SHAP| ≈ 1.37, log-odds scale), followed by Introduction to Health Sciences (≈ 1.00) and English (≈ 0.81). By contrast, high-school average and demographic variables had comparatively small effects (all mean |SHAP| < 0.40)."

## Discussion


## Related Claims
- [A 10-point decrease in Biology midterm score raises predicted at-risk probability by about 31 percentage points, with smaller effects for Introduction to Health Sciences (~25) and English (~18)](ten-point-biology-decline-raises-risk-31-points.md) — a narrower finding that bears on this claim
- [SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance](shap-undergrad-gpa-rank-strongest-predictor.md) — related
- [Feature importance analyses rank failed courses first for predicting academic performance, followed by institutional and academic background variables, with some regression-specific differences](feature-importance-failed-courses-institutional-background.md) — related
