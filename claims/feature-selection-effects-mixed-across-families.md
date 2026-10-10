---
type: claim
title: Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis
description: Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis
id: feature-selection-effects-mixed-across-families
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
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

# Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Retaining the top 20 features improved both ordinal metrics for the linear and Random Forest models but worsened both for XGBoost and LightGBM; for AdaBoost, accuracy rose 0.9 points while macro-MAE and binary macro-F1 worsened slightly. [→ Sidharth Anupkrishnan 2026](#sidharth-anupkrishnan-2026)

## Evidence

### Sidharth Anupkrishnan 2026

Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen. (2026). E3Sense: Head-Confined Multimodal Sensing of Learner Engagement. arXiv. https://arxiv.org/abs/2609.26569

`q2 · i?` · `design · r2`

Secondary sensitivity analysis refitting each fixed family with fold-local top-20 feature selection learned only from training participants (Table 4). The study reports a "family-dependent pattern" and describes the effects as mixed; all values are descriptive fold means.

> "Feature-selection effects are therefore mixed rather than uniformly beneficial, supporting the complete 166-dimensional representation as the primary analysis."

## Discussion


## Related Claims
- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](e3sense-head-confined-engagement-prediction.md) — related
- [Model-family rankings depend on the prediction target: AdaBoost leads the five-level ordinal task while LightGBM holds the highest binary macro-F1](model-family-rankings-depend-on-target.md) — related
