---
type: claim
title: "Model-family rankings depend on the prediction target: AdaBoost leads the five-level ordinal task while LightGBM holds the highest binary macro-F1"
description: "Model-family rankings depend on the prediction target: AdaBoost leads the five-level ordinal task while LightGBM holds the highest binary macro-F1"
id: model-family-rankings-depend-on-target
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: sidharth-anupkrishnan-2026
    resource: "https://arxiv.org/abs/2609.26569"
    title: "Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen. (2026). E3Sense: Head-Confined Multimodal Sensing of Learner Engagement. arXiv. https://arxiv.org/abs/2609.26569"
    author: Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model-family rankings depend on the prediction target: AdaBoost leads the five-level ordinal task while LightGBM holds the highest binary macro-F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the secondary binary target, LightGBM achieved the highest macro-F1 point estimate (58.9%±7.9), ahead of XGBoost (56.7%±5.1) and AdaBoost (54.3%±3.0), reversing the ordinal-task ordering. [→ Sidharth Anupkrishnan 2026](#sidharth-anupkrishnan-2026)

## Evidence

### Sidharth Anupkrishnan 2026

Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen. (2026). E3Sense: Head-Confined Multimodal Sensing of Learner Engagement. arXiv. https://arxiv.org/abs/2609.26569

`q2 · i?` · `design · r2`

Binary sensitivity analysis within the same five-fold participant-grouped RQ1 evaluation, using the fixed 166-dimensional representation. The study reports the LightGBM "macro-F1 point estimate at 58.9%±7.9", above the 49.0%±1.1 random-distribution binary baseline; values are descriptive fold means.

> "LightGBM has the highest macro-F1 point estimate at 58.9%±7.9, followed by XGBoost at56.7%±5.1and AdaBoost at54.3%±3.0."

## Discussion


## Related Claims
- [Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis](feature-selection-effects-mixed-across-families.md) — related
- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](e3sense-head-confined-engagement-prediction.md) — related
