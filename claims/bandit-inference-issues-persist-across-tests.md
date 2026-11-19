---
type: claim
title: "The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses"
description: "The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses"
id: bandit-inference-issues-persist-across-tests
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
  - id: williams-2021-2
    resource: "https://doi.org/10.48550/arXiv.2103.12198"
    title: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)"
    author: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Welch's t-test shows FPR of 11.9% for TS vs 5.0% for UR, and Power of 52.4% for TS vs 81.2% for UR. [→ Williams 2021](#williams-2021)
`q2 i?` Bayes factor analysis (cutoff 3.0) shows FPR of 4.2% for TS vs 0.5% for UR, and Power of 19.3% for TS vs 49.8% for UR. [→ Williams 2021 (2)](#williams-2021-2)

## Evidence

### Williams 2021

Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)

`q2 · i?` · `causal · r2`

Table 2 simulation results for Welch's t-test across TS, UR, and EG data collection strategies with n=785 simulated participants. TS FPR is 11.9% vs UR 5.0%; TS Power is 52.4% vs UR 81.2%.

> "2. Welch's t-test 11.9 % (0.5) 52. 4% (0.7) 5.0 % (0.3) 81.2 % (0.6) 5.4 % (0.3) 36. 8% (0.7)"

### Williams 2021 (2)

Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)

`q2 · i?` · `causal · r2`

Table 2 simulation results for Bayes factor analysis (cutoff 3.0) across TS, UR, and EG. TS FPR is 4.2% vs UR 0.5%; TS Power is 19.3% vs UR 49.8%.

> "3. Bayes factor (Cutoff 3.0) 4.2 % (0.3) 19.3 % (0.6) 0.5 % (0.1) 49.8 % (0.7) 1.2 % (0.2) 17.5 % (0.5)"

## Discussion


## Related Claims
- [An Algorithm-Induced Test controls FPR at 5% but greatly reduces Power to 17%](algorithm-induced-test-controls-fpr-reduces-power.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — related
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](classroom-ts-deployment-uneven-allocation.md) — related
- [Thompson Sampling and TS† exploit a single arm even when no significant difference exists among arm means](bandit-exploitation-without-significant-arm-difference.md) — related
