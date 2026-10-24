---
type: claim
title: Curriculum strategies in AI training often yield faster convergence and better generalization, but difficulty in ML reflects optimization rather than learner readiness
description: Curriculum strategies in AI training often yield faster convergence and better generalization, but difficulty in ML reflects optimization rather than learner readiness
id: curriculum-learning-sequencing-gains-and-limits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: peng-wang-2026
    resource: "https://doi.org/10.1007/s10648-026-10195-8"
    title: "Peng Wang, Fred Paas. (2026). Five Educational-Psychology Lenses for Training and Evaluating AI Models. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10195-8"
    author: Peng Wang, Fred Paas
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: peng-wang-2026-2
    resource: "https://doi.org/10.1007/s10648-026-10195-8"
    title: "Peng Wang, Fred Paas. (2026). Five Educational-Psychology Lenses for Training and Evaluating AI Models. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10195-8"
    author: Peng Wang, Fred Paas
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Curriculum strategies in AI training often yield faster convergence and better generalization, but difficulty in ML reflects optimization rather than learner readiness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Curriculum strategies in machine learning often lead to faster convergence and better generalization, echoing the educational principle that sequencing instruction matters. [→ Peng Wang 2026](#peng-wang-2026)
`q2 i?` In some AI training regimes, especially for very large models, developers front-load difficult examples via hard example mining, where difficulty reflects optimization and distributional coverage rather than learner readiness. [→ Peng Wang 2026 (2)](#peng-wang-2026-2)

## Evidence

### Peng Wang 2026

Peng Wang, Fred Paas. (2026). Five Educational-Psychology Lenses for Training and Evaluating AI Models. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10195-8

`q2 · i?` · `theoretical · r3`

The article's narrative review of curriculum learning reports that sequencing training data from simpler to more difficult often improves convergence and generalization. It frames this as empirical support for the educational analogy, citing the seminal work on Curriculum Learning.

> "Empirically, curriculum strategies often lead to faster convergence and better generalization, echoing long-standing educational wisdom that sequencing instruction matters"

### Peng Wang 2026 (2)

Peng Wang, Fred Paas. (2026). Five Educational-Psychology Lenses for Training and Evaluating AI Models. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10195-8

`q2 · i?` · `theoretical · r3`

The article describes hard example mining as a divergence from human pedagogy, noting that ML difficulty is operationalized via loss, gradient magnitude, or rarity rather than conceptual complexity. It recommends transfer and robustness tests under distribution shift rather than inference from sequencing alone.

> "Yet in some AI training regimes, especially for very large models, developers sometimes do front-load difficult examples, a tactic known as "hard example mining" (Shrivastava et al., 2016)."

## Discussion


## Related Claims
- [Reinforcement learning in adaptive educational systems faces sample inefficiency and reward-design instability, motivating hybrid RL-ML approaches](rl-sample-inefficiency-reward-design-limits.md) — related
- [Reinforcement learning operationalizes motivational constructs by representing motivation in the reward function](rl-reward-function-operationalizes-motivation.md) — related
