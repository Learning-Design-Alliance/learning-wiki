---
type: claim
title: A multimodal EEG-fNIRS dataset was collected from 31 participants watching three instructional videos, yielding over 4.5 million data points with expert-verified attention labels
description: A multimodal EEG-fNIRS dataset was collected from 31 participants watching three instructional videos, yielding over 4.5 million data points with expert-verified attention labels
id: eeg-fnirs-dataset-31-participants-attention-labels
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
  - id: shixian-zhou-2026-2
    resource: "https://arxiv.org/abs/2607.29413"
    title: "Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413"
    author: Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A multimodal EEG-fNIRS dataset was collected from 31 participants watching three instructional videos, yielding over 4.5 million data points with expert-verified attention labels

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Simultaneous EEG and fNIRS signals were collected from 31 healthy participants during videos on convolutional neural networks, matrix factorization, and neurons and synapses. [→ Shixian Zhou 2026](#shixian-zhou-2026)
`q2 i?` The dataset contains over 4.5 million data points, with experiments lasting 50.2±7.6 minutes, and labels were verified by two domain experts. [→ Shixian Zhou 2026 (2)](#shixian-zhou-2026-2)

## Evidence

### Shixian Zhou 2026

Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413 [doi:10.48550/arxiv.2607.29413](https://doi.org/10.48550/arxiv.2607.29413)

`q2 · i?` · `design · r2`

Brain data acquisition described in the Brain Dataset subsection. Participants watched videos on three topics; the authors note the sample of 31 "exceeds the sample sizes typically used in BCI experiments" and that the experiment was IRB-approved.

> "We collected a multimodal brain dataset with simultaneous EEG and fNIRS signals from 31 healthy participants (16 male, 15 female; mean age 23.6± 1.2 years) during instructional videos on convolutional neural networks, matrix factorization, and neurons and synapses."

### Shixian Zhou 2026 (2)

Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413

`q2 · i?` · `design · r2`

Dataset scale reported in the Brain Dataset subsection. Two domain experts (E3-E4) independently judged initial attention-level labels using quiz accuracy, EEG spectrograms, and fNIRS activation, with ambiguous segments discarded.

> "The dataset contains over 4.5 million data points, with each experiment lasting 50.2± 7.6 minutes."

## Discussion


## Related Claims
- [A DDQN-based attention quantification model trained on multimodal EEG-fNIRS features produces predicted attention levels at one-second temporal resolution](ddqn-multimodal-attention-quantification-accurate-stable.md) — related
- [Two case studies and expert interviews with six experts demonstrated SAVVY's effectiveness and usability for identifying attention variations and supporting video optimization](savvy-case-studies-expert-interviews-effectiveness.md) — related
