---
type: claim
title: A DDQN-based attention quantification model trained on multimodal EEG-fNIRS features produces predicted attention levels at one-second temporal resolution
description: A DDQN-based attention quantification model trained on multimodal EEG-fNIRS features produces predicted attention levels at one-second temporal resolution
id: ddqn-multimodal-attention-quantification-accurate-stable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shixian-zhou-2026
    resource: "https://doi.org/10.48550/arxiv.2607.29413"
    title: "Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413 [doi:10.48550/arxiv.2607.29413](https://doi.org/10.48550/arxiv.2607.29413)"
    author: Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A DDQN-based attention quantification model trained on multimodal EEG-fNIRS features produces predicted attention levels at one-second temporal resolution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` After training, the optimized DDQN model quantifies student attention on test data, producing a predicted attention level (high, medium, or low) at one-second resolution. [→ Shixian Zhou 2026](#shixian-zhou-2026)

## Evidence

### Shixian Zhou 2026

Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413 [doi:10.48550/arxiv.2607.29413](https://doi.org/10.48550/arxiv.2607.29413)

`q2 · i?` · `design · r2`

Attention quantification model evaluation described in the Attention Modeling subsection: a DDQN trained on 80% of the labeled dataset and tested on 20%, outputting "a predicted attention level (high, medium, or low)" per second. No effect size or test statistic is printed in the available text.

> "After training, the optimized model is used to quantify student attention on the test data, producing a predicted attention level (high, medium, or low) at a one- second temporal resolution."

## Discussion


## Related Claims

- [A multimodal EEG-fNIRS dataset was collected from 31 participants watching three instructional videos, yielding over 4.5 million data points with expert-verified attention labels](eeg-fnirs-dataset-31-participants-attention-labels.md) — related
- [A modality-aware reference model outperforms sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines for estimating minute-level attention difficulty from wearable sensing](edugage-modality-aware-model-outperforms-baselines.md) — related
- [The end-to-end attention-estimation pipeline meets the one-second prediction stride on an NVIDIA A100 GPU, with warm latency of 50.65 ms per window and 1.02 ms for the temporal model](real-time-pipeline-latency-one-second-stride-a100.md)
