---
type: claim
title: The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance
description: The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance
id: fusion-transformer-lowest-worst-group-mae-smallest-gender-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: christoforos-fragkiadakis-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02232"
    title: "Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)"
    author: Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 10 seeds, the Residual Fusion Transformer achieved the lowest worst-group MAE for both age (0.328) and gender (0.289) and the lowest gender gap (0.015); the Sensor GRU achieved the smallest age gap (0.096) but with substantially lower predictive performance. [→ Christoforos Fragkiadakis 2026](#christoforos-fragkiadakis-2026)

## Evidence

### Christoforos Fragkiadakis 2026

Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)

`q2 · i?` · `design · r2`

Demographic subgroup evaluation across 10 seeds (Table 4): the fusion model also exhibited the lowest gender gap (0.015), while the Sensor GRU achieved the smallest age gap (0.096) and the Visual GRU the largest age gap (0.147).

> "The Residual Fusion Transformer achieved the lowest worst-group MAE for both age (0.328) and gender (0.289), providing the most favorable balance between overall performance and worst-group error among the evaluated baselines."

## Discussion


## Related Claims

- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md) — related
- [Facial visual dynamics provide the most informative cues for attention estimation: the Visual GRU outperforms both the train-mean baseline and the Sensor GRU](visual-gru-outperforms-sensor-gru-attention-estimation.md) — related
- [Demographic MAE-gap regularization reduces targeted subgroup gaps on validation data, but these fairness gains do not consistently transfer to held-out test subjects](mae-gap-regularization-validation-gains-do-not-generalize.md) — related
- [GRU is the lowest-performing model across both single-task and multi-task competency modeling, likely due to its two gating units versus LSTMs' three](gru-lowest-performing-competency-model.md)
- [Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone](chest-ecg-strongest-cardiac-engagement-signal.md) — related
- [Densely sampled visual frames and sensor representations offered no reliable predictive advantage over the 1 FPS setting in the higher-frequency experiment](higher-frequency-sampling-no-reliable-advantage-over-1fps.md) — related
- [Repeated subject-level split experiments confirm that validation-level fairness improvements from MAE-gap regularization do not correspond to consistent generalization to unseen subjects](repeated-subject-splits-confirm-fairness-non-generalization.md) — related
