---
type: claim
title: Students shown a self-explanation prompt scored higher on the next problem than students shown no prompt in a traditional CS1 experiment
description: Students shown a self-explanation prompt scored higher on the next problem than students shown no prompt in a traditional CS1 experiment
id: self-explanation-prompt-improves-subsequent-cs1-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: ilya-musabirov-2024
    title: Ilya Musabirov 2024
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Students shown a self-explanation prompt scored higher on the next problem than students shown no prompt in a traditional CS1 experiment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the traditional uniform-random arm of the deployment, students who saw a self-explanation prompt scored higher on a follow-up problem than students who saw no prompt (M2 = 0.608 vs M1 = 0.512; Wald Z = 2.122). [→ Ilya Musabirov 2024](#ilya-musabirov-2024)

## Evidence

### Ilya Musabirov 2024

Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659

`q2 · i?` · `causal · r2`

Results from the traditional (uniform random) arm of a side-by-side deployment in a Fall 2021 CS1 homework system, where the prompt condition's mean was higher ("Condition 2 (self-explanation prompt)𝑀2 = 0.608") than the no-prompt condition's, with "Wald Z statistic = 2.122".

> "For the traditional experiment, there is a significant difference between the means with Condition 2 (self-explanation prompt)𝑀2 = 0.608(𝑆𝐸𝑀 = 0.032) and Condition 1 (no prompt)𝑀1 = 0.512(𝑆𝐸𝑀 = 0.032). Wald Z statistic = 2.122."

## Discussion


## Related Claims
- [An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome](adaptive-bandit-reallocates-majority-to-better-condition.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — related
