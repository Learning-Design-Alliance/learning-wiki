---
type: claim
title: "In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms"
description: "In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms"
id: classroom-ts-deployment-uneven-allocation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: williams-2021
    resource: "https://doi.org/10.48550/arXiv.2103.12198"
    title: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)"
    author: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A."
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In Experiment 2 (three arms: Answer Only, Hint, Worked Solution), TS placed over 88% of students in one arm, and hypothesis tests did not support the apparent differences. [→ Williams 2021](#williams-2021)

## Evidence

### Williams 2021

Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)

`q1 · i?` · `causal · r2`

Real classroom deployment of TS in a university course with three arms (Answer Only, Hint, Worked Solution). Wald tests yielded p-values of 0.364 and 0.083, not supporting the apparent differences suggested by assignment probabilities.

> "the adaption in Experiment 2 led to over 88% of students being placed in a single arm, and the small numbers of students in the other arms led to high uncertainty about the true effectiveness of these alternative arms"

## Discussion


## Related Claims
- [The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses](bandit-inference-issues-persist-across-tests.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — a broader claim this one bears on
- [The multi-step grading recipe with calibration examples achieves the highest scoring accuracy and receives the majority of bandit arm pulls](multi-step-examples-highest-aes-accuracy.md) — related
- [Instructors valued adaptive experiments using Thompson Sampling for rapidly directing students to better interventions but were concerned about generalizable conclusions](instructors-value-adaptive-experiments-but-worry-about-inference.md) — related
