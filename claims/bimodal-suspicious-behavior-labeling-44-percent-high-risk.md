---
type: claim
title: "A 20% suspicious-question labeling threshold partitions 52 students into 23 high-risk (44.2%) and 29 low-risk, robustly across nearby cut-offs"
description: "A 20% suspicious-question labeling threshold partitions 52 students into 23 high-risk (44.2%) and 29 low-risk, robustly across nearby cut-offs"
id: bimodal-suspicious-behavior-labeling-44-percent-high-risk
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

# A 20% suspicious-question labeling threshold partitions 52 students into 23 high-risk (44.2%) and 29 low-risk, robustly across nearby cut-offs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Labeling students high-risk when suspicious events (copy, focus-loss, right-click) occurred in at least 5 of 25 exam questions produced 23 high-risk and 29 low-risk students, and any cut-off between 9% and 20% produces the same partition. [→ Akçapınar 2026](#akcapnar-2026)

## Evidence

### Akçapınar 2026

Akçapınar, G. (2026). Early Prediction of AI-Assisted Cheating Risk in Online Exams Through Learning Analytics. https://scholar.google.com/scholar?q=Early+Prediction+of+AI-Assisted+Cheating+Risk+in+Online+Exams+Through+Learning+Analytics

`q2 · i?` · `associational · r1`

Question-level labeling of exam-log events for 52 students in a proctored face-to-face final. The suspicious-question distribution was "strongly bimodal" with an empty region between three and four suspicious questions; a sensitivity check at 10%, 20%, and 30% preserved the group pattern.

> "This rule produced 23 high -risk and 29 low-risk students. Because the cut -off sits above an empty region, the labels are not highly sensitive to a small change in the threshold. Any cut-off between 9% and 20% produces the same partition, while thresholds up to 48% affect only the four observations closest to the boundary."

## Discussion


## Related Claims
- [High-risk students disproportionately scored 80 or above on the final exam (13 of 23), while no low-risk student did](high-risk-students-high-final-scores.md) — related
- [Classification threshold trades sensitivity against specificity: 0.30 yields 91.3% sensitivity, 0.60 yields 89.7% specificity](cheating-risk-threshold-sensitivity-tradeoff.md) — related
- [Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV](lms-traces-predict-ai-assisted-cheating-risk.md) — related
