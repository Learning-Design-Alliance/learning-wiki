---
type: claim
title: The end-to-end attention-estimation pipeline meets the one-second prediction stride on an NVIDIA A100 GPU, with warm latency of 50.65 ms per window and 1.02 ms for the temporal model
description: The end-to-end attention-estimation pipeline meets the one-second prediction stride on an NVIDIA A100 GPU, with warm latency of 50.65 ms per window and 1.02 ms for the temporal model
id: real-time-pipeline-latency-one-second-stride-a100
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

# The end-to-end attention-estimation pipeline meets the one-second prediction stride on an NVIDIA A100 GPU, with warm latency of 50.65 ms per window and 1.02 ms for the temporal model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On an NVIDIA A100-SXM4-40GB GPU, the warm end-to-end pipeline averaged 50.65 ms per prediction window (19.7 predictions per second), and the temporal fairness model (402,531 trainable parameters) required 1.02 ms on average for prediction. [→ Christoforos Fragkiadakis 2026](#christoforos-fragkiadakis-2026)

## Evidence

### Christoforos Fragkiadakis 2026

Christoforos Fragkiadakis, Seyed Sahand Mohammadi Ziabari, and Ali Mohammed Mansoor Alsahag. (2026). Fairness-Aware Multimodal Transformer Modeling for Real-Time Student Attention Estimation. https://arxiv.org/abs/2609.02232 [doi:10.48550/arxiv.2609.02232](https://doi.org/10.48550/arxiv.2609.02232)

`q2 · i?` · `design · r2`

Deployment feasibility benchmark on an unseen subject recording; warm latency included preprocessing, image–sensor alignment, CLIP ViT-L/14 feature extraction, window construction, and prediction, with cold-start initialization excluded.

> "the warm end-to-end pipeline achieved a mean latency of 50.65 ms per prediction window at a one-second stride on an NVIDIA A100-SXM4-40GB GPU, corresponding to a throughput of 19.7 predictions per second."

## Discussion


## Related Claims

- [A DDQN-based attention quantification model trained on multimodal EEG-fNIRS features produces predicted attention levels at one-second temporal resolution](ddqn-multimodal-attention-quantification-accurate-stable.md)
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md)
- [Densely sampled visual frames and sensor representations offered no reliable predictive advantage over the 1 FPS setting in the higher-frequency experiment](higher-frequency-sampling-no-reliable-advantage-over-1fps.md)
- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](elevate-prototype-near-real-time-consumer-hardware.md) — related
- [A multimodal EEG-fNIRS dataset was collected from 31 participants watching three instructional videos, yielding over 4.5 million data points with expert-verified attention labels](eeg-fnirs-dataset-31-participants-attention-labels.md) — related
