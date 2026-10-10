---
type: claim
title: Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone
description: Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone
id: mixing-group-and-pair-sampling-beats-either-alone
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

# Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Interpolating between group-only and pair-only prompting under the same question budget yields better results in most cases, scales better, and reaches a higher upper bound on GSM8K and BBH-structured. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `causal · r2`

Sampling-strategy ablation (Figure 4) comparing group-only, pair-only, and mixed prompting at fixed question budgets on GSM8K and BBH-structured. The article reports that the mixture "yields better results in most cases" and reaches a higher upper bound.

> "On both datasets, however, interpolating between them under the same budget yields better results in most cases (shadow area), scales better as the budget grows, and reaches a higher upper bound (orange line)."

## Discussion


## Related Claims
- [The benefit of high- versus low-contrast sampling depends on the dataset](contrast-strength-benefit-is-dataset-dependent.md) — related
- [Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects](hypotheses-discriminate-difficulty-effect-sizes.md) — related
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](hypothesis-guided-editing-shifts-difficulty-causally.md) — related
- [A small question budget of about 200 suffices for strong hypothesis quality, with room to scale](small-budget-suffices-for-hypothesis-quality.md) — related
- [Baseline hypothesis generators saturate after 5–10 effective hypotheses while the proposed method keeps improving](baseline-generators-saturate-proposed-method-keeps-improving.md) — related
