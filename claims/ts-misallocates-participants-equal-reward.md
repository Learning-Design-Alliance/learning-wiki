---
type: claim
title: Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm
description: Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm
id: ts-misallocates-participants-equal-reward
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: williams-2021
    resource: "https://doi.org/10.48550/arXiv.2103.12198"
    title: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)"
    author: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When two arms have equal reward, TS responds to sampling variability and converges on one arm, producing biased estimates of the other arm. [→ Williams 2021](#williams-2021)

## Evidence

### Williams 2021

Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)

`q2 · i?` · `causal · r2`

Empirical illustration from simulation (Figure 1) of why TS inflates FPR: sampling variability makes one arm look 'lower', TS stops assigning it, leading to biased estimation of that arm and high confidence in the other arm's mean.

> "Since TS is adaptive to the posterior probability (which is sensitive to the sample mean), when (by chance) an arm's sample mean is lower than its true mean, TS will assign fewer participants to it and assign them to the other 'higher' arm"

## Discussion


## Related Claims
- [The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses](bandit-inference-issues-persist-across-tests.md) — related
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](classroom-ts-deployment-uneven-allocation.md) — a narrower finding that bears on this claim
- [Instructors valued adaptive experiments using Thompson Sampling for rapidly directing students to better interventions but were concerned about generalizable conclusions](instructors-value-adaptive-experiments-but-worry-about-inference.md) — related
- [The adaptive trial design reallocates more study subjects to more promising treatment arms as evidence accumulates](adaptive-allocation-to-promising-arms.md) — related
- [Bayesian adaptive design benefits study subjects by allocating them to more effective treatment arms](bayesian-adaptive-benefits-study-subjects.md) — related
