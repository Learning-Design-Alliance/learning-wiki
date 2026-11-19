---
type: claim
title: Mean-field agent-based model reproduces group-level achievement but underestimates students with low prior knowledge and very low motivation
description: Mean-field agent-based model reproduces group-level achievement but underestimates students with low prior knowledge and very low motivation
id: abm0-mean-field-reproduces-group-achievement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: velásquez-rojas-2021
    resource: "https://doi.org/10.48550/arXiv.2103.06926"
    title: "Velásquez-Rojas, F., & Laguna, M. F. (2021). The knowledge acquisition process from a complex system perspective: observations and models. Originally published 2019. [doi:10.48550/arXiv.2103.06926](https://doi.org/10.48550/arXiv.2103.06926)"
    author: "Velásquez-Rojas, F., & Laguna, M. F."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
  - id: velásquez-rojas-2021-2
    resource: "https://doi.org/10.48550/arXiv.2103.06926"
    title: "Velásquez-Rojas, F., & Laguna, M. F. (2021). The knowledge acquisition process from a complex system perspective: observations and models. Originally published 2019. [doi:10.48550/arXiv.2103.06926](https://doi.org/10.48550/arXiv.2103.06926)"
    author: "Velásquez-Rojas, F., & Laguna, M. F."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Mean-field agent-based model reproduces group-level achievement but underestimates students with low prior knowledge and very low motivation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` ABM0 stochastic simulations reproduce the average final knowledge and dispersion of each real achievement group. [→ Velásquez-Rojas 2021](#velasquez-rojas-2021)
`q1 i?` For students whose surveys showed low prior knowledge and very low motivation, ABM0 underestimated the final result. [→ Velásquez-Rojas 2021 (2)](#velasquez-rojas-2021-2)

## Evidence

### Velásquez-Rojas 2021

Velásquez-Rojas, F., & Laguna, M. F. (2021). The knowledge acquisition process from a complex system perspective: observations and models. Originally published 2019. [doi:10.48550/arXiv.2103.06926](https://doi.org/10.48550/arXiv.2103.06926)

`q1 · i?` · `theoretical · r2`

Stochastic agent-based simulations with the same group proportions as the real course (numerical results shown in Fig. 3); the article reports the model "fits very well to the real data of each group of agents" over many independent realizations.

> "This figure shows that the model fits very well to the real data of each group of agents, which seems to be a quite robust behavior for this model and serves as a validation of the chosen methodology."

### Velásquez-Rojas 2021 (2)

Velásquez-Rojas, F., & Laguna, M. F. (2021). The knowledge acquisition process from a complex system perspective: observations and models. Originally published 2019. [doi:10.48550/arXiv.2103.06926](https://doi.org/10.48550/arXiv.2103.06926)

`q1 · i?` · `design · r2`

Individual-trajectory comparison for agents whose outcomes did not match their student's; the article reports the ABM0 "underestimated the final result", attributing this to successful strategies not contemplated in the model. It notes these students' surveys showed low prior knowledge and very low motivation.

> "Furthermore, in such cases the ABM0 model underestimated the final result, indicating that some successful strategies used by students are not contemplated in this model and reveals the variability in knowledge acquisition of some agents."

## Discussion


## Related Claims
- [A computational model of learning reproduced the direction of two tutor A/B experiments without human training data, but not students' absolute performance](computational-learner-model-predicts-tutor-experiment-direction.md) — a broader claim this one bears on
- [Simulations predict higher final knowledge when students form clusters than when working individually, with low-achieving students most favored](cluster-formation-improves-simulated-achievement.md) — related
- [Sensitivity analyses restricting to students assessed in all 15 terms reproduced the full-sample between-group comparisons](sensitivity-15-term-subsample-same-comparisons.md) — related
