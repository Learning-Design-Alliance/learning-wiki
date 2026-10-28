---
type: claim
title: "Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy"
description: "Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy"
id: cross-semester-at-risk-prediction-high-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: wei-dai-2025
    resource: "https://doi.org/10.18608/jla.2025.8735"
    title: "Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen. (2025). Learning Analytics for Early Identification of At-Risk Students and Feedback Intervention. Journal of Learning Analytics, 12(3), 102–125. https://doi.org/10.18608/jla.2025.8735"
    author: Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Random-forest models trained on trace and academic data from a prior semester achieved AUC scores above 0.8 when applied to identify at-risk students in a new cohort. [→ Wei Dai 2025](#wei-dai-2025)

## Evidence

### Wei Dai 2025

Wei Dai, Jionghao Lin, Flora Ji-Yoon Jin, Yi-Shan Tsai, Namrata Srivastava, Pierre Le Bodic, Dragan Gašević, and Guanliang Chen. (2025). Learning Analytics for Early Identification of At-Risk Students and Feedback Intervention. Journal of Learning Analytics, 12(3), 102–125. https://doi.org/10.18608/jla.2025.8735

`q2 · i?` · `design · r2`

Post-hoc evaluation of random-forest models trained on week 0–4 and week 0–7 data from the 2022 source semester and applied without retraining to the 2023 target semester of the same course. The article reports "a high prediction accuracy (with AUC scores above 0.8)" on the new cohort; no effect size is printed.

> "our predictive models demonstrated a high prediction accuracy (with AUC scores above 0.8) when applied to a new cohort of students"

## Discussion

## Related Claims

- [Attendance, behavior, and course performance (the ABC indicators) reliably predict which secondary students are at risk of dropping out](abc-early-warning-indicators-predict-dropout.md) — the general claim this finding bears on, with the studies behind it
- [Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining](cross-semester-auc-decline-without-retraining.md) — reports the opposite
- Early-semester LMS interaction data predicts AI-assisted cheating risk in the final exam, with Logistic Regression achieving AUC = 0.763 under LOOCV — related
- [Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors](college-offtrack-classified-90-percent-accuracy.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [A CatBoost classifier using only pre-enrollment achievement measures predicts dropout with an AUC of 0.774 and average precision of 0.847 on a held-out 2017 cohort.](catboost-preenrollment-dropout-prediction-auc-0774.md) — related
