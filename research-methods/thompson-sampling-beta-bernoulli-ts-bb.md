---
type: research-method
id: thompson-sampling-beta-bernoulli-ts-bb
title: Thompson Sampling Beta-Bernoulli (TS-BB)
description: "The article describes TS-BB, a Multi-Armed Bandit algorithm in which Thompson Sampling \"learns how effective each of the conditions is\" from rewards such as \"correct or incorrect answer on the following task\", learning \"from every interaction of participants with the algorithm without the need to ga"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Thompson Sampling Beta-Bernoulli (TS-BB)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size

## Description
The article describes TS-BB, a Multi-Armed Bandit algorithm in which Thompson Sampling "learns how effective each of the conditions is" from rewards such as "correct or incorrect answer on the following task", learning "from every interaction of participants with the algorithm without the need to gather all evidence in advance" by updating Beta distributions over each arm's success probability and deploying the arm with the maximal sampled expected reward.

## Accounts
<!-- How each source describes or uses the method -->
- **Thompson Sampling Beta-Bernoulli (TS-BB): a Multi-Armed Bandit algorithm for adaptive experiments**: The article describes TS-BB, a Multi-Armed Bandit algorithm in which Thompson Sampling "learns how effective each of the conditions is" from rewards such as "correct or incorrect answer on the following task", learning "from every interaction of participants with the algorithm without the need to gather all evidence in advance" by updating Beta distributions over each arm's success probability and deploying the arm with the maximal sampled expected reward. (Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Scienc)

### Claims
- [An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome](../claims/adaptive-bandit-reallocates-majority-to-better-condition.md) [+M]

## Related Research Methods
-

## Key Sources
- Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659
