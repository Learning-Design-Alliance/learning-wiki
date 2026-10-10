---
type: claim
title: "A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline"
description: "A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline"
id: e3sense-head-confined-engagement-prediction
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

# A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` AdaBoost on the fused 166-dimensional head-confined representation achieved 75.0%±7.0 balanced 1-off accuracy and 1.043±0.158 macro-MAE on 15 held-out forehead participants, exceeding the sensor-free mode baseline (63.0%) by 12.0 percentage points; comparisons are descriptive. [→ Sidharth Anupkrishnan 2026](#sidharth-anupkrishnan-2026)

## Evidence

### Sidharth Anupkrishnan 2026

Sidharth Anupkrishnan, Itir Sayar, Jeongah Lee, Sri Harsha Musunuri, Guan-Ming Su, Madeline Endres, Ravi Karkar, Phuc Nguyen. (2026). E3Sense: Head-Confined Multimodal Sensing of Learner Engagement. arXiv. https://arxiv.org/abs/2609.26569

`q2 · i?` · `design · r2`

Participant-independent evaluation of the E3Sense sensing study: five participant-grouped outer folds trained on both EDA sites and scored 225 segments from 15 held-out forehead participants. The study reports "75.0%± 7.0balanced 1-off accuracy" for AdaBoost against a 63.0% mode baseline; no significance test is reported.

> "AdaBoost has the strongest ordinal point estimates in Table 3, reaching 75.0%± 7.0balanced 1-off accuracy and1 .043± 0.158macro-MAE. Relative to the mode baseline, these equal-fold means differ by+12.0percentage points in balanced 1-off accuracy and −0.277in macro-MAE. These comparisons are descriptive."

## Discussion


## Related Claims
- [Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone](chest-ecg-strongest-cardiac-engagement-signal.md) — related
- [Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost](sensor-stream-performance-non-monotonic.md) — related
- [Certain multimodal data combinations improve predictive model performance, with audio plus eye-tracking data most effective in one K–8 study](mmla-k8-modality-combinations-prediction.md) — a broader claim this one bears on
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md) — related
- [Fold-local top-20 feature selection had mixed effects across model families, supporting the complete 166-dimensional representation as the primary analysis](feature-selection-effects-mixed-across-families.md) — related
- [Model-family rankings depend on the prediction target: AdaBoost leads the five-level ordinal task while LightGBM holds the highest binary macro-F1](model-family-rankings-depend-on-target.md) — related
