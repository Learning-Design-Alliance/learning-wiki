---
type: claim
title: "Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy"
description: "Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy"
id: cross-semester-at-risk-prediction-high-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
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
- [Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining](cross-semester-auc-decline-without-retraining.md) — reports the opposite
