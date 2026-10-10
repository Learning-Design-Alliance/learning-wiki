---
type: claim
title: "Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity"
description: "Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity"
id: cheating-risk-threshold-sensitivity-tradeoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: akçapınar-2026
    resource: "https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics"
    title: "Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics"
    author: Akçapınar, G.
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` At threshold 0.30 the Logistic Regression model identified 21 of 23 high-risk students (Sensitivity = 91.3%, Specificity = 51.7%), while at 0.60 it identified 12 (Sensitivity = 52.2%, Specificity = 89.7%). [→ Akçapınar 2026](#akcapnar-2026)

## Evidence

### Akçapınar 2026

Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics

`q2 · i?` · `associational · r1`

Threshold analysis of the Logistic Regression LOOCV held-out predictions (Fig. 3 confusion matrix and ROC). At the default 0.50 threshold, "Sensitivity = 60.9%" and "Specificity = 82.8%" with Precision = 73.7%.

> "At 0.30, the model identified 21 of 23 high -risk students (Sensitivity = 91.3%, Specificity = 51.7%, Precision = 60.0%). At 0.60, it identified 12 high -risk students (Sensitivity = 52.2%, Specificity = 89.7%, Precision = 80.0%)."

## Discussion


## Related Claims
- [A 20% suspicious-question labeling threshold partitions 52 students into 23 high-risk (44.2%) and 29 low-risk, robustly across nearby cut-offs](bimodal-suspicious-behavior-labeling-44-percent-high-risk.md) — related
- [Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV](lms-traces-predict-ai-assisted-cheating-risk.md) — related
- [Recommended MAP Growth screening cut scores yield sensitivity, specificity, and lower-bound AUC of at least 0.8 for most grades and terms](map-growth-screening-accuracy-08-criteria.md) — related
