---
type: claim
title: Anomaly detection models (Isolation Forest, One-Class SVM) detect stroke anomalies adequately but underperform compared to traditional binary classifiers for canoe stroke quality classification.
description: Anomaly detection models (Isolation Forest, One-Class SVM) detect stroke anomalies adequately but underperform compared to traditional binary classifiers for canoe stroke quality classification.
id: anomaly-detection-underperforms-binary-classifiers
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

# Anomaly detection models (Isolation Forest, One-Class SVM) detect stroke anomalies adequately but underperform compared to traditional binary classifiers for canoe stroke quality classification.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Anomaly detection models showed performance on the catch and recovery phases better than the pull phase, but generally underperformed compared to binary classifiers. [→ Shubham Parab 2025](#shubham-parab-2025)

## Evidence

### Shubham Parab 2025

Shubham Parab, Anthony Lamelas, Ahmed Hassan, Pasang Bhote. (2025). Canoe Paddling Quality Assessment Using Smart Devices: Preliminary Machine Learning Study. [doi:10.48550/arXiv.2508.01511](https://doi.org/10.48550/arXiv.2508.01511)

`q2 · i?` · `design · r2`

Secondary analysis evaluated Isolation Forest and One-Class SVM anomaly detection models on stroke data, presented in Table 4. Anomaly detection models showed adequate performance but did not surpass the binary classifiers, suggesting the latter captured broader stroke data patterns.

> "Overall, anomaly detection models underperformed relative to traditional binary classifiers, as summarized in Table 4 and Figure 15."

## Discussion


## Related Claims
- [An Extremely Randomized Tree classifier trained on consumer smartwatch and smartphone summary features distinguishes optimal from suboptimal canoe paddle strokes with high accuracy (~95%) under five-fold cross-validation.](extratree-classifier-high-accuracy-canoe-strokes.md) — related
- [Wrist-mounted smartwatch sensors produce better-performing stroke classification models than bicep-mounted phone sensors, with the left wrist-mounted device performing best.](wrist-sensors-better-than-bicep-canoe-strokes.md) — related
