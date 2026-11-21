---
type: claim
title: Wrist-mounted smartwatch sensors produce better-performing stroke classification models than bicep-mounted phone sensors, with the left wrist-mounted device performing best.
description: Wrist-mounted smartwatch sensors produce better-performing stroke classification models than bicep-mounted phone sensors, with the left wrist-mounted device performing best.
id: wrist-sensors-better-than-bicep-canoe-strokes
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

# Wrist-mounted smartwatch sensors produce better-performing stroke classification models than bicep-mounted phone sensors, with the left wrist-mounted device performing best.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models trained on wrist-mounted device data outperformed those trained on bicep-mounted phone data, with the left wrist-mounted device producing the best-performing model. [→ Shubham Parab 2025](#shubham-parab-2025)

## Evidence

### Shubham Parab 2025

Shubham Parab, Anthony Lamelas, Ahmed Hassan, Pasang Bhote. (2025). Canoe Paddling Quality Assessment Using Smart Devices: Preliminary Machine Learning Study. [doi:10.48550/arXiv.2508.01511](https://doi.org/10.48550/arXiv.2508.01511)

`q2 · i?` · `design · r2`

Secondary analysis evaluated Extratree classifiers trained independently on data from different body locations (left wrist, right wrist, bicep), presented in Table 3. The left wrist-mounted device produced the best model performance, closely followed by the right wrist-mounted device, with wrist devices outperforming bicep-mounted ones.

> "Overall, the left wrist-mounted device produced the best model performance, closely followed by the right wrist-mounted device. Detailed results are presented in Table 3 and Figure 13."

## Discussion


## Related Claims
- [An Extremely Randomized Tree classifier trained on consumer smartwatch and smartphone summary features distinguishes optimal from suboptimal canoe paddle strokes with high accuracy (~95%) under five-fold cross-validation.](extratree-classifier-high-accuracy-canoe-strokes.md) — related
- [Anomaly detection models (Isolation Forest, One-Class SVM) detect stroke anomalies adequately but underperform compared to traditional binary classifiers for canoe stroke quality classification.](anomaly-detection-underperforms-binary-classifiers.md) — related
