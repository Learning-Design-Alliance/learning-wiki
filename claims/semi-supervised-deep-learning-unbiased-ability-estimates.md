---
type: claim
title: A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness
description: A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness
id: semi-supervised-deep-learning-unbiased-ability-estimates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: xue-2020
    resource: "https://educationaldatamining.org/EDM2020/"
    title: "Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/"
    author: "Xue, K., Huggins-Manley, A. C., & Leite, W."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A semi-supervised deep learning architecture recovers the ability distribution of anchor students more accurately than direct 2PL-IRT fitting under simulated nonignorable missingness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In simulation, the ability estimates from the semi-supervised deep learning architecture matched the true ability distribution more closely than estimates from directly fitting 2PL-IRT to anchor students' responses. [→ Xue 2020](#xue-2020)

## Evidence

### Xue 2020

Xue, K., Huggins-Manley, A. C., & Leite, W. (2020). Semi-supervised Learning Method for Adjusting Biased Item Difficulty Estimates Caused by Nonignorable Missingness under 2PL-IRT Model. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), pp. 715-719. https://educationaldatamining.org/EDM2020/

`q1 · i?` · `design · r2`

Simulation study under 2PL-IRT using known pretest mathematical ability as true student ability and biased anchor-student item parameters; Table 1 prints, for example, domain 1 true mean 0.090 (σ 0.93), direct fit -0.001 (σ 0.99), and DFN estimate 0.095 (σ 0.90) across the 10 domains. No test statistics are reported for this comparison.

> "Comparison of the distribution of ability estimates between directly 2PL-IRT model ﬁtting (ˆθ) and the proposed semi-supervised deep learning architecture ( ˜Θ)."

## Discussion


## Related Claims
- Both proposed adjustment methods (IEA and BA) reduce RMSE of item difficulty estimates from direct 2PL-IRT fitting, with BA yielding more consistent (lower-variance) estimates in simulation — related
- In a statewide VLE algebra dataset, item missingness is nonignorable: skipping is related to student ability and item difficulty as measured in 2PL-IRT — related
- [MCAR item and response missingness in linear tests shows no differential effect on model fit across Designs 1 to 4](mcar-missingness-linear-tests-no-fit-effect.md) — related
- [Achievement gap estimates are widely used to measure the effectiveness and fairness of the education system, so their accuracy and unbiasedness are necessary for appropriate conclusions](gap-estimates-accuracy-necessary-for-conclusions.md) — related
- [Latent singing ability varies widely across learners, with sequence-level theta estimates spanning −3.79 to 3.36 logits](wide-latent-ability-spread-singing-learners.md) — related
