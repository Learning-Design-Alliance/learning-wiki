---
type: claim
title: "An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome"
description: "An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome"
id: adaptive-bandit-reallocates-majority-to-better-condition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
source_checked: 2026-11-20
sources:
  - id: ilya-musabirov-2024
    title: Ilya Musabirov 2024
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: ilya-musabirov-2024-2
    title: Ilya Musabirov 2024 (2)
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`
> **Currency** · no dated study recorded · checked against its sources 2026-11-20 (automated, 2 of 2 entries) · not reviewed by a person

## Subclaims
`q2 i?` In the adaptive arm, the algorithm served 262 (82.6%) students the self-explanation prompt condition, which the authors describe as more than a 30% reallocation toward a better outcome. [→ Ilya Musabirov 2024](#ilya-musabirov-2024)
`q2 i?` Accuracy estimates computed in the adaptive arm also favoured the self-explanation prompt (M2 = 0.599 vs M1 = 0.539). [→ Ilya Musabirov 2024 (2)](#ilya-musabirov-2024-2)

## Evidence

### Ilya Musabirov 2024

Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659

`q2 · i?` · `causal · r2`

Allocation outcome of the adaptive Thompson Sampling arm of the side-by-side CS1 deployment: "the algorithm served 262 (82.6%) students with a self-explanation prompt", which the authors call "more than a 30% reallocation toward a better outcome" relative to the almost equal assignments of the traditional arm.

> "That means that the algorithm served 262 (82.6%) students with a self-explanation prompt (Condition 2, the best option according to our analysis). This corresponds to more than a 30% reallocation toward a better outcome"

### Ilya Musabirov 2024 (2)

Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659

`q2 · i?` · `causal · r2`

Accuracy estimates computed in the adaptive arm of the same deployment: "the computed estimates were𝑀2 = 0.599 and 𝑀1 = 0.539, also favouring self-explanation prompts."

> "In the adaptive experiment, the computed estimates were𝑀2 = 0.599 and 𝑀1 = 0.539, also favouring self-explanation prompts."

## Discussion


## Related Claims
- [Students shown a self-explanation prompt scored higher on the next problem than students shown no prompt in a traditional CS1 experiment](self-explanation-prompt-improves-subsequent-cs1-accuracy.md) — related
- [Bayesian adaptive design benefits study subjects by allocating them to more effective treatment arms](bayesian-adaptive-benefits-study-subjects.md) — a broader claim this one bears on
- [The adaptive trial design reallocates more study subjects to more promising treatment arms as evidence accumulates](adaptive-allocation-to-promising-arms.md) — a broader claim this one bears on
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — related
