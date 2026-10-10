---
type: claim
title: Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10
description: Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10
id: sequencing-explains-evol-ppo-gap
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
    kind: design
    rigour: 2
---

# Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` After uniformly shuffling each recommended path, EVOL-BC and PPO-vanilla obtain nearly indistinguishable EP, while the original ordered paths retain a clear advantage for EVOL, indicating transfer of an order-sensitive policy. [→ Geonwoo Bang 2026](#geonwoo-bang-2026)

## Evidence

### Geonwoo Bang 2026

Geonwoo Bang, Dongho Kim, and Moohong Min. (2026). EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation. arXiv:2610.03273. https://arxiv.org/abs/2610.03273

`q2 · i?` · `design · r2`

Pedagogical decomposition (Table 5, ASSIST15 L=10, 3 seeds, 200 test learners) measuring target coverage and EP drop after shuffling (SeqDrop). EVOL-BC: EP +0.627, SeqDrop +0.297; PPO-vanilla: EP +0.561, SeqDrop +0.227.

> "After uniformly shuffling each recommended path, EVOL-BC and PPO-vanilla obtain nearly indistinguishable EP. This suggests that the two methods select concept sets of comparable quality, but differ in how those concepts are ordered."

## Discussion


## Related Claims
- [Under deployment-free inference, at least one EVOL variant achieves the best test EP in every dataset–length setting across three datasets and eight baselines](evol-best-ep-every-dataset-length-setting.md) — related
- [EVOL variants remain the strongest methods when recommended paths are executed on alternative DKT simulator instances](evol-robust-to-dkt-instance-shift.md) — related
- [EVOL variants remain the strongest methods under stochastic response models, weakening the hypothesis that evolutionary search exploits deterministic threshold discontinuities](evol-robust-to-stochastic-response-models.md) — related
- [Replacing evolutionary experts with random-path experts collapses performance, and greedy 1-step lookahead reaches only +0.155 EP on ASSIST15 L=10](random-experts-collapse-lpr-performance.md) — related
- [Final LPR performance is governed by the quality of evolutionary experts rather than by the particular imitation objective](expert-quality-over-imitation-objective.md) — related
