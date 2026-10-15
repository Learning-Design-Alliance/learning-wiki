---
type: claim
title: "Facial visual dynamics provide the most informative cues for attention estimation: the Visual GRU outperforms both the train-mean baseline and the Sensor GRU"
description: "Facial visual dynamics provide the most informative cues for attention estimation: the Visual GRU outperforms both the train-mean baseline and the Sensor GRU"
id: visual-gru-outperforms-sensor-gru-attention-estimation
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

# Facial visual dynamics provide the most informative cues for attention estimation: the Visual GRU outperforms both the train-mean baseline and the Sensor GRU

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The Visual GRU substantially outperformed both the train-mean baseline and the Sensor GRU on test MAE and RMSE, suggesting physiological and motion signals alone provide limited predictive information for attention estimation in DIPSER. [→ Christoforos Fragkiadakis 2026](#christoforos-fragkiadakis-2026)

## Evidence

### Christoforos Fragkiadakis 2026

Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)

`q2 · i?` · `design · r2`

Test-set comparison across 10 training seeds of the Sensor GRU (MAE 0.313, RMSE 0.398), train-mean baseline (MAE 0.312), and Visual GRU. The Visual GRU "reducing the MAE to 0.287 and the RMSE to 0.366."

> "In contrast, the Visual GRU substantially outperformed both the train-mean baseline and the Sensor GRU, reducing the MAE to 0.287 and the RMSE to 0.366."

## Discussion


## Related Claims
- [The Residual Fusion Transformer shows the lowest worst-group MAE and smallest gender gap among baselines, while the Sensor GRU shows the smallest age gap alongside the weakest overall performance](fusion-transformer-lowest-worst-group-mae-smallest-gender-gap.md) — related
- [Densely sampled visual frames and sensor representations offered no reliable predictive advantage over the 1 FPS setting in the higher-frequency experiment](higher-frequency-sampling-no-reliable-advantage-over-1fps.md) — related
- [Chest-worn ECG provides the strongest cardiac-sensing performance for attention-difficulty prediction, and fusing all cardiac streams does not improve upon chest ECG alone](chest-ecg-strongest-cardiac-engagement-signal.md) — related
