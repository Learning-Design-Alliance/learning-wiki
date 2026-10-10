---
type: claim
title: One-minute-ahead direct forecasting performs similarly to contemporaneous estimation, but performance degrades at longer horizons and a carry-forward baseline outperforms the sensor model at every future horizon
description: One-minute-ahead direct forecasting performs similarly to contemporaneous estimation, but performance degrades at longer horizons and a carry-forward baseline outperforms the sensor model at every future horizon
id: engagement-forecasting-horizon-degradation
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
    kind: associational
    rigour: 1
---

# One-minute-ahead direct forecasting performs similarly to contemporaneous estimation, but performance degrades at longer horizons and a carry-forward baseline outperforms the sensor model at every future horizon

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Class MAE changes only from 0.753 at t+0 to 0.756 at t+1, but the carry-forward baseline outperforms the directly trained sensor model at every future horizon, demonstrating substantial temporal persistence in the self-reported ratings. [→ Zikang Leng 2026](#zikang-leng-2026)

## Evidence

### Zikang Leng 2026

Zikang Leng, Edan Eyal, Yingtian Shi, Jiaman He, Yaqi Liu, and Thomas Plötz. (2026). EduGage: A Multimodal Dataset and Benchmark for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning. Proc. ACM Interact. Mob. Wearable Ubiquitous Ubiquitous Technol. https://arxiv.org/abs/2605.01238

`q2 · i?` · `associational · r1`

Temporal predictability analysis (Table 7) comparing contemporaneous estimation and direct forecasting at approximately one- to three-minute horizons against carry-forward baselines, evaluated on identical data across horizons under participant-grouped folds. Relative to t+1, Within-1 accuracy decreased by 4.13 and 8.23 percentage points at t+2 and t+3.

> "The carry-forward baseline outperforms the directly trained sensor model at every future horizon, demonstrating substantial temporal persistence in the self-reported ratings."

## Discussion


## Related Claims
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md) — related
