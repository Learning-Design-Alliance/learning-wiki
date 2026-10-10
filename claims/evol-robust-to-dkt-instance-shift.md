---
type: claim
title: EVOL variants remain the strongest methods when recommended paths are executed on alternative DKT simulator instances
description: EVOL variants remain the strongest methods when recommended paths are executed on alternative DKT simulator instances
id: evol-robust-to-dkt-instance-shift
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

# EVOL variants remain the strongest methods when recommended paths are executed on alternative DKT simulator instances

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Policies trained against the original DKT (seed 42) and executed on four alternative DKT instances keep EVOL variants strongest, with graph-conditioned baselines degrading more sharply. [→ Geonwoo Bang 2026](#geonwoo-bang-2026)

## Evidence

### Geonwoo Bang 2026

Geonwoo Bang, Dongho Kim, and Moohong Min. (2026). EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation. arXiv:2610.03273. https://arxiv.org/abs/2610.03273

`q2 · i?` · `design · r2`

Simulator-instance shift stress test (Table 6, ASSIST15 L=10): policies trained on the seed-42 DKT executed on four alternative DKTs (seeds 7, 100, 200, 333; validation AUC 0.700–0.708 vs 0.704). EVOL-BC cross-instance mean +0.341 vs PPO-vanilla +0.250.

> "First, all three EVOL variants remain the strongest methods across the alternative DKT instances, and their differences are much smaller than the gap to the strongest baseline."

## Discussion


## Related Claims
- [Under deployment-free inference, at least one EVOL variant achieves the best test EP in every dataset–length setting across three datasets and eight baselines](evol-best-ep-every-dataset-length-setting.md) — related
- [EVOL variants remain the strongest methods under stochastic response models, weakening the hypothesis that evolutionary search exploits deterministic threshold discontinuities](evol-robust-to-stochastic-response-models.md) — related
- [Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10](sequencing-explains-evol-ppo-gap.md) — related
