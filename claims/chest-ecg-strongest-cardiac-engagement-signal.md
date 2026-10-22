---
type: claim
title: Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone
description: Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone
id: chest-ecg-strongest-cardiac-engagement-signal
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: zikang-leng-2026
    resource: "https://doi.org/10.48550/arxiv.2605.01238"
    title: "Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238 [doi:10.48550/arxiv.2605.01238](https://doi.org/10.48550/arxiv.2605.01238)"
    author: Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Chest ECG provides the strongest predictive performance across all four metrics compared with wrist HR, head PPG, and finger PPG; combining all cardiac streams does not improve upon chest ECG alone. [→ Zikang Leng 2026](#zikang-leng-2026)

## Evidence

### Zikang Leng 2026

Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238 [doi:10.48550/arxiv.2605.01238](https://doi.org/10.48550/arxiv.2605.01238)

`q2 · i?` · `design · r2`

Comparison of cardiac sensing configurations at different body locations (chest ECG, wrist HR, head PPG, finger PPG, and cardiac fusion), each trained independently under matched participant-grouped folds. Chest ECG achieved the best Class MAE of 0.847±0.092 and binary Macro-F1 of 70.54±6.64.

> "Table 6 shows that chest ECG provides the strongest predictive performance across all four metrics. Combining all cardiac streams does not improve upon chest ECG alone, suggesting that the additional cardiac measurements do not provide sufficient complementary information under this setting."

## Discussion


## Related Claims

- [Videos experienced as higher attention difficulty were associated with lower normalized quiz learning gains, providing convergent evidence that the probe captures an educationally meaningful aspect of momentary engagement](attention-difficulty-inversely-related-quiz-gains.md) — related
- [Predictive performance of sensor configurations does not change monotonically with the number of sensing streams; preferred configuration depends on target metric and sensing cost](sensor-stream-performance-non-monotonic.md) — related
- [Combining more modalities does not always improve detection of learner mental states](more-modalities-not-always-better-mental-state-detection.md) — a broader claim this one bears on
- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](e3sense-head-confined-engagement-prediction.md) — related
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md) — related
- [Facial visual dynamics provide the most informative cues for attention estimation: the Visual GRU outperforms both the train-mean baseline and the Sensor GRU](visual-gru-outperforms-sensor-gru-attention-estimation.md) — related
- [The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance](fusion-transformer-lowest-worst-group-mae-smallest-gender-gap.md) — related
- [One-minute-ahead direct forecasting performs similarly to contemporaneous estimation, but performance degrades at longer horizons and a carry-forward baseline outperforms the sensor model at every future horizon](engagement-forecasting-horizon-degradation.md) — related
- [Densely sampled visual frames and sensor representations offered no reliable predictive advantage over the 1 FPS setting in the higher-frequency experiment](higher-frequency-sampling-no-reliable-advantage-over-1fps.md) — related
- [Certain multimodal data combinations improve predictive model performance, with audio plus eye-tracking data most effective in one K–8 study](mmla-k8-modality-combinations-prediction.md) — related
- [Static HRV devices were associated with high-correlation studies, while wristband and chest belt wearables showed no significant difference in correlation levels](hrv-device-accuracy-static-vs-wearable.md)
