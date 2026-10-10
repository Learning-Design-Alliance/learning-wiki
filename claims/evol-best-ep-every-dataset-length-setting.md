---
type: claim
title: Under deployment-free inference, at least one EVOL variant achieves the best test EP in every dataset–length setting across three datasets and eight baselines
description: Under deployment-free inference, at least one EVOL variant achieves the best test EP in every dataset–length setting across three datasets and eight baselines
id: evol-best-ep-every-dataset-length-setting
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

# Under deployment-free inference, at least one EVOL variant achieves the best test EP in every dataset–length setting across three datasets and eight baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across ASSIST15, Junyi, and EdNet with path lengths 5, 10, and 20, at least one EVOL variant attains the best test EP in every dataset–length cell, with the advantage clearest in longer-path and larger-concept settings. [→ Geonwoo Bang 2026](#geonwoo-bang-2026)

## Evidence

### Geonwoo Bang 2026

Geonwoo Bang, Dongho Kim, and Moohong Min. (2026). EVOL: Simulator-Guided Evolutionary Expert Synthesis for Deployment-Free Learning Path Recommendation. arXiv:2610.03273. https://arxiv.org/abs/2610.03273

`q2 · i?` · `design · r2`

Numerical evaluation results (Table 2) across three datasets (ASSIST15, Junyi, EdNet; 39–189 concepts) and L in {5,10,20}, mean±std over 3 seeds, all methods re-implemented under h0-only deployment-free inference. The article reports "the best result in every dataset–length setting" for EVOL variants.

> "At least one EVOL variant achieves the best result in every dataset–length setting, and the three EVOL variants remain tightly clustered throughout."

## Discussion


## Related Claims
- [Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10](sequencing-explains-evol-ppo-gap.md) — related
- [Final LPR performance is governed by the quality of evolutionary experts rather than by the particular imitation objective](expert-quality-over-imitation-objective.md) — related
- [Replacing evolutionary experts with random-path experts collapses performance, and greedy 1-step lookahead reaches only +0.155 EP on ASSIST15 L=10](random-experts-collapse-lpr-performance.md) — related
- [EVOL variants remain the strongest methods under stochastic response models, weakening the hypothesis that evolutionary search exploits deterministic threshold discontinuities](evol-robust-to-stochastic-response-models.md) — related
- [EVOL variants remain the strongest methods when recommended paths are executed on alternative DKT simulator instances](evol-robust-to-dkt-instance-shift.md) — related
