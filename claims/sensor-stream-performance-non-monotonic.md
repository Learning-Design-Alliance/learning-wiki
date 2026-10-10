---
type: claim
title: Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost
description: Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost
id: sensor-stream-performance-non-monotonic
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: zikang-leng-2026
    resource: "https://arxiv.org/abs/2605.01238"
    title: "Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238"
    author: Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Smaller sensor configurations sometimes achieve similar or better observed results than larger ones; the five-stream EEG+EDA+eSense IMU+HR+Ring Temperature configuration achieved the highest Within-1 accuracy (85.86%) and binary accuracy (74.44%), while ECG alone achieved the highest binary Macro-F1 (70.54%). [→ Zikang Leng 2026](#zikang-leng-2026)

## Evidence

### Zikang Leng 2026

Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238

`q2 · i?` · `design · r2`

Modality configuration tradeoff study screening all 2,047 nonempty combinations of the 11 sensing streams under the same participant-grouped folds (Table 5). Reduced configurations such as the five-stream EEG, EDA, eSense IMU, HR, and Ring Temperature setup reached the highest Within-1 accuracy (85.86±4.72%).

> "Performance does not change monotonically with the number of streams: smaller configurations sometimes achieve similar or better observed results than larger ones."

## Discussion


## Related Claims
- [Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone](chest-ecg-strongest-cardiac-engagement-signal.md) — related
- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](e3sense-head-confined-engagement-prediction.md) — related
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md) — related
- [Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1](llama-guard-scaling-trend-education-classification.md) — reports the opposite
- [A tool's effectiveness results from the whole configuration of events, activities, and contexts in which it is used](tool-effectiveness-depends-on-context-configuration.md) — related
