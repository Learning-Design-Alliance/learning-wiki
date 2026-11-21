---
type: claim
title: Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm
description: Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm
id: ts-misallocates-participants-equal-reward
aliases: [ts-random-favouring-problematic-for-inference]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
source_checked: 2026-11-20
sources:
  - id: williams-2021
    resource: "https://doi.org/10.48550/arXiv.2103.12198"
    title: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)"
    author: "Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: zavaleta-bernuy-2021
    resource: "https://doi.org/10.1007/978-3-030-78270-2_75"
    title: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2021). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. [doi:10.1007/978-3-030-78270-2_75](https://doi.org/10.1007/978-3-030-78270-2_75)"
    author: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J."
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q1`–`q2`
> **Currency** · newest study 2021 · checked against its sources 2026-11-20 (automated, 2 of 2 entries) · not reviewed by a person

## Subclaims

`q2 i?` When two arms have equal reward, TS responds to sampling variability and converges on one arm, producing biased estimates of the other arm. [→ Williams 2021](#williams-2021)

`q1 i?` The authors interpret that TS may randomly favour an arm even when giving this arm more frequently has no consequences for participants, which can be problematic for scientific inference and statistical analysis. [→ Zavaleta-Bernuy 2021](#zavaleta-bernuy-2021)

## Evidence

### Williams 2021

Williams, J. J., Nogas, J., Deliu, N., Shaikh, H., Villar, S., Durand, A., & Rafferty, A. (2021). Challenges in Statistical Analysis of Data Collected by a Bandit Algorithm: An Empirical Exploration in Applications to Adaptively Randomized Experiments. Originally published 2020. [doi:10.48550/arXiv.2103.12198](https://doi.org/10.48550/arXiv.2103.12198)

`q2 · i?` · `causal · r2`

Empirical illustration from simulation (Figure 1) of why TS inflates FPR: sampling variability makes one arm look 'lower', TS stops assigning it, leading to biased estimation of that arm and high confidence in the other arm's mean.

> "Since TS is adaptive to the posterior probability (which is sensitive to the sample mean), when (by chance) an arm's sample mean is lower than its true mean, TS will assign fewer participants to it and assign them to the other 'higher' arm"

### Zavaleta-Bernuy 2021

Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2021). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. [doi:10.1007/978-3-030-78270-2_75](https://doi.org/10.1007/978-3-030-78270-2_75)

`q1 · i?` · `causal · r2`

Authors' interpretation (type e) from the Discussion section of the case study, where the traditional uniform random experiment found no difference between arms. The article notes TS minimizes regret, so with equivalent arms any could be presented, but "this can be problematic for scientiﬁc inference and statistical analysis".

> "We illustrate how TS may randomly favour an arm, even when giving this arm more frequently has no consequences for participants."

## Discussion



## Related Claims

- [The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses](bandit-inference-issues-persist-across-tests.md) — related
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](classroom-ts-deployment-uneven-allocation.md) — a narrower finding that bears on this claim
- [Instructors valued adaptive experiments using Thompson Sampling for rapidly directing students to better interventions but were concerned about generalizable conclusions](instructors-value-adaptive-experiments-but-worry-about-inference.md) — related
- [The adaptive trial design reallocates more study subjects to more promising treatment arms as evidence accumulates](adaptive-allocation-to-promising-arms.md) — related
- [Bayesian adaptive design benefits study subjects by allocating them to more effective treatment arms](bayesian-adaptive-benefits-study-subjects.md) — related
- [Thompson Sampling and TS† exploit a single arm even when no significant difference exists among arm means](bandit-exploitation-without-significant-arm-difference.md) — a narrower finding that bears on this claim
- [No statistically significant difference exists among the three email subject-line arms' mean open rates under any of the three allocation policies](no-significant-difference-email-subject-line-arm-means.md) — a narrower finding that bears on this claim
- [Weekly open-rate estimates hinted at non-stationary arm means, meaning the optimal subject line could change each week](non-stationary-weekly-email-open-rates.md) — related
- [Thompson Sampling drastically shifted assignment toward a favoured arm with minimal exploration room, but the favoured arm varied across weeks](ts-drastic-shift-inconsistent-favoured-arm.md) — a narrower finding that bears on this claim
- [Students shown a self-explanation prompt scored higher on the next problem than students shown no prompt in a traditional CS1 experiment](self-explanation-prompt-improves-subsequent-cs1-accuracy.md) — related
- [An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome](adaptive-bandit-reallocates-majority-to-better-condition.md) — related
- [Random reviewer assignment produces inconsistent grading and fairness concerns, though calibration and dynamic allocation can mitigate specific problems](random-assignment-fairness-and-accuracy-problems.md) — related
