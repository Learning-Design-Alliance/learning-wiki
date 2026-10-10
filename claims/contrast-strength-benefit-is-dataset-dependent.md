---
type: claim
title: The benefit of high- versus low-contrast sampling depends on the dataset
description: The benefit of high- versus low-contrast sampling depends on the dataset
id: contrast-strength-benefit-is-dataset-dependent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: peng-cui-2026
    resource: "https://arxiv.org/abs/2610.01627"
    title: "Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627"
    author: Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The benefit of high- versus low-contrast sampling depends on the dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` High-contrast sampling (bucket gap 7–9) is the stronger choice on GSM8K, while low-contrast sampling (gap 4–6) wins on BBH-structured; the mixed strategy is the more stable option. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `causal · r2`

Contrast-strength ablation (Figure 5) comparing high-contrast (bucket gap δ≥7), low-contrast (4≤δ≤6), and mixed sampling on GSM8K and BBH-structured. The article reports the opposite ordering across datasets and calls the mixture "a more stable option".

> "The two strategies behave in opposite ways on the two datasets: high contrast is the stronger choice on GSM8K, while low contrast wins on BBH-structured."

## Discussion


## Related Claims
- [Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone](mixing-group-and-pair-sampling-beats-either-alone.md) — related
- [Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects](hypotheses-discriminate-difficulty-effect-sizes.md) — related
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](hypothesis-guided-editing-shifts-difficulty-causally.md) — related
