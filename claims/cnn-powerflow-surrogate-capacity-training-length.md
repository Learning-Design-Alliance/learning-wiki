---
type: claim
title: In the CNN 5-bus power-flow surrogate, pairing model capacity with sufficient training length improves voltage accuracy, and line flows are the more demanding test
description: In the CNN 5-bus power-flow surrogate, pairing model capacity with sufficient training length improves voltage accuracy, and line flows are the more demanding test
id: cnn-powerflow-surrogate-capacity-training-length
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: junjie-yin-2026
    resource: "https://arxiv.org/abs/2608.02599"
    title: "Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li. (2026). Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework. arXiv preprint. https://arxiv.org/abs/2608.02599"
    author: Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: junjie-yin-2026-2
    resource: "https://arxiv.org/abs/2608.02599"
    title: "Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li. (2026). Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework. arXiv preprint. https://arxiv.org/abs/2608.02599"
    author: Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In the CNN 5-bus power-flow surrogate, pairing model capacity with sufficient training length improves voltage accuracy, and line flows are the more demanding test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The 200-epoch, 240-filter voltage model achieved test MAE below 10^-3 pu, while both 50-epoch models incurred more than an order-of-magnitude larger error. [→ Junjie Yin 2026](#junjie-yin-2026)
`q2 i?` The line-flow model reproduced active flows across all six lines with test MAE about 14 MW and reactive flows with test MAE about 2 MVAr. [→ Junjie Yin 2026 (2)](#junjie-yin-2026-2)

## Evidence

### Junjie Yin 2026

Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li. (2026). Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework. arXiv preprint. https://arxiv.org/abs/2608.02599

`q2 · i?` · `design · r2`

Numerical evaluation of three CNN voltage-model variants on held-out test operating points of a PJM 5-bus system (Monte-Carlo power-flow data, 100 samples). The 200-epoch/240-filter model reached "test MAE below10−3 pu"; lightly trained variants erred far more.

> "the model trained for 200 epochs with 240 filters reproduces this profile almost exactly (test MAE below10−3 pu), including the dip at the PQ bus, whereas the two lightly trained 50-epoch models incur more than an order- of-magnitude larger error"

### Junjie Yin 2026 (2)

Junjie Yin, Buxin She, Xinyu Feng, Fangxing (Fran) Li. (2026). Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework. arXiv preprint. https://arxiv.org/abs/2608.02599

`q2 · i?` · `design · r2`

Evaluation of the line-flow CNN variant (Model 4) on unseen test operating points. It captured active flows with "test MAE≈14MW" and reactive flows with "test MAE≈2MV Ar," with the largest residual at the most heavily loaded line.

> "with moderate per-line deviations (test MAE≈14MW on flows spanning roughly±240MW). The reactive flows are likewise captured (test MAE≈2MV Ar)"

## Discussion


## Related Claims
- [Deep learning techniques such as CNNs and RNNs better detect cheating from visual cues than traditional techniques, but each carries stated trade-offs](dl-cnn-rnn-better-visual-cheating-detection.md) — related
