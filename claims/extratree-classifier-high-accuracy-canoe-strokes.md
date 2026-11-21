---
type: claim
title: "An Extremely Randomized Tree classifier trained on consumer smartwatch and smartphone summary features distinguishes optimal from suboptimal canoe paddle strokes with high accuracy (~95%) under five-fold cross-validation."
description: "An Extremely Randomized Tree classifier trained on consumer smartwatch and smartphone summary features distinguishes optimal from suboptimal canoe paddle strokes with high accuracy (~95%) under five-fold cross-validat..."
id: extratree-classifier-high-accuracy-canoe-strokes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: shubham-parab-2025
    resource: "https://doi.org/10.48550/arXiv.2508.01511"
    title: "Shubham Parab, Anthony Lamelas, Ahmed Hassan, Pasang Bhote. (2025). Canoe Paddling Quality Assessment Using Smart Devices: Preliminary Machine Learning Study. [doi:10.48550/arXiv.2508.01511](https://doi.org/10.48550/arXiv.2508.01511)"
    author: Shubham Parab, Anthony Lamelas, Ahmed Hassan, Pasang Bhote
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An Extremely Randomized Tree classifier trained on consumer smartwatch and smartphone summary features distinguishes optimal from suboptimal canoe paddle strokes with high accuracy (~95%) under five-fold cross-validation.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Four binary classifiers were validated with 5-fold cross-validation on 66 stroke samples, and the Extratree model exhibited the best performance across stroke phases. [→ Shubham Parab 2025](#shubham-parab-2025)

## Evidence

### Shubham Parab 2025

Shubham Parab, Anthony Lamelas, Ahmed Hassan, Pasang Bhote. (2025). Canoe Paddling Quality Assessment Using Smart Devices: Preliminary Machine Learning Study. [doi:10.48550/arXiv.2508.01511](https://doi.org/10.48550/arXiv.2508.01511)

`q2 · i?` · `design · r2`

Secondary analysis of binary classification models (SVC, RF, GBF, Extratree) tested on optimal and suboptimal strokes from four participants, presented in Table 2. Across all three stroke phases, models achieved high accuracy (~95%) and F-scores between 92% and 96%, with the Extratree model exhibiting the best performance across phases.

> "Overall, the Extratree model exhibited the best performance across phases. Models generally performed best in the Recovery phase, followed by the Pull and Catch phases."

## Discussion


## Related Claims
- [Anomaly detection models (Isolation Forest, One-Class SVM) detect stroke anomalies adequately but underperform compared to traditional binary classifiers for canoe stroke quality classification.](anomaly-detection-underperforms-binary-classifiers.md) — related
- [Wrist-mounted smartwatch sensors produce better-performing stroke classification models than bicep-mounted phone sensors, with the left wrist-mounted device performing best.](wrist-sensors-better-than-bicep-canoe-strokes.md) — related
