---
type: claim
title: "An Algorithm-Induced Test controls FPR at 5% but greatly reduces Power to 17%"
description: "An Algorithm-Induced Test controls FPR at 5% but greatly reduces Power to 17%"
id: algorithm-induced-test-controls-fpr-reduces-power
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

# An Algorithm-Induced Test controls FPR at 5% but greatly reduces Power to 17%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The Algorithm-Induced Test, which constructs a non-parametric distribution by simulating TS data collection, controls FPR at 5% but reduces Power to 17%. [→ Williams 2021](#williams-2021)

## Evidence

### Williams 2021

Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)

`q2 · i?` · `causal · r2`

Evaluation of the Algorithm-Induced Test, the second of two methods for incorporating bandit-algorithm knowledge into statistical testing, using the simulation environment with n=785 simulated participants.

> "This allows control of the FPR at 5% but greatly reduces Power (to 17%)."

## Discussion


## Related Claims
- [The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses](bandit-inference-issues-persist-across-tests.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
