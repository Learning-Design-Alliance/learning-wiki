---
type: claim
title: A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing
description: A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing
id: edugage-modality-aware-model-outperforms-baselines
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

# A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across participant-based cross-validation, the modality-aware reference model achieves an MAE of 0.80, 83.18% within-1 accuracy, 70.96% binary accuracy, and 62.90% binary Macro-F1, outperforming the listed baseline families. [→ Zikang Leng 2026](#zikang-leng-2026)

## Evidence

### Zikang Leng 2026

Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238

`q2 · i?` · `design · r2`

Benchmark evaluation of the EduGage dataset under a participant-grouped four-fold cross-validation protocol (Table 4). The modality-aware model achieved the lowest MAE of 0.80, versus an MAE of 1.05 for the task-informed Peer Window Mean baseline. The authors note the remaining error demonstrates the difficulty of the task.

> "Across participant-based cross-validation, the modality-aware reference model achieves an MAE of 0.80, 83.18% within-1 accuracy, 70.96% binary accuracy, and 62.90% binary Macro-F1, outperforming sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines."

## Discussion


## Related Claims
- [Videos experienced as higher attention difficulty were associated with lower normalized quiz learning gains, providing convergent evidence that the probe captures an educationally meaningful aspect of momentary engagement](attention-difficulty-inversely-related-quiz-gains.md) — related
- [One-minute-ahead direct forecasting performs similarly to contemporaneous estimation, but performance degrades at longer horizons and a carry-forward baseline outperforms the sensor model at every future horizon](engagement-forecasting-horizon-degradation.md) — related
- [Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone](chest-ecg-strongest-cardiac-engagement-signal.md) — related
- [Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost](sensor-stream-performance-non-monotonic.md) — related
- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](e3sense-head-confined-engagement-prediction.md) — related
