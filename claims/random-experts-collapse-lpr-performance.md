---
type: claim
title: Replacing evolutionary experts with random-path experts collapses performance, and greedy 1-step lookahead reaches only +0.155 EP on ASSIST15 L=10
description: Replacing evolutionary experts with random-path experts collapses performance, and greedy 1-step lookahead reaches only +0.155 EP on ASSIST15 L=10
id: random-experts-collapse-lpr-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: geonwoo-bang-2026
    resource: "https://arxiv.org/abs/2610.03273"
    title: "Geonwoo Bang, Dongho Kim, and Moohong Min. (2026). EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation. arXiv:2610.03273. https://arxiv.org/abs/2610.03273"
    author: Geonwoo Bang, Dongho Kim, and Moohong Min
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Replacing evolutionary experts with random-path experts collapses performance, and greedy 1-step lookahead reaches only +0.155 EP on ASSIST15 L=10

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` BC on random-path experts reaches +0.354 EP, well below PPO-vanilla (+0.543), while evolutionary search reaches +0.614, showing bad demonstrations actively bias the policy and joint sequence optimization matters. [→ Geonwoo Bang 2026](#geonwoo-bang-2026)

## Evidence

### Geonwoo Bang 2026

Geonwoo Bang, Dongho Kim, and Moohong Min. (2026). EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation. arXiv:2610.03273. https://arxiv.org/abs/2610.03273

`q2 · i?` · `causal · r2`

Controlled Stage-1 ablation on ASSIST15 L=10 (3 seeds, Table 3) comparing greedy 1-step lookahead (+0.155), random-path experts (+0.354), and evolutionary search (+0.614) under identical candidate sets and budgets.

> "(ii) Random-path experts discard search entirely; BC on them reaches+0.354, well below PPO-vanilla (+0.543), so any source of demonstrations is not enough—bad demonstrations actively bias the policy."

## Discussion


## Related Claims
- [Under deployment-free inference, at least one EVOL variant achieves the best test EP in every dataset–length setting across three datasets and eight baselines](evol-best-ep-every-dataset-length-setting.md) — related
- [Final LPR performance is governed by the quality of evolutionary experts rather than by the particular imitation objective](expert-quality-over-imitation-objective.md) — related
- [Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10](sequencing-explains-evol-ppo-gap.md) — related
