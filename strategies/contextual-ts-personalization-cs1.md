---
type: strategy
id: contextual-ts-personalization-cs1
title: Personalize adaptive experiments with Contextual Thompson Sampling to discover what works best for which student groups
description: "The article proposes extending Thompson Sampling to Contextual TS so instructors \"can personalize the improvement process for different groups of students or situations, automatically discovering what works best for w..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: ilya-musabirov-2024
    resource: "https://doi.org/10.1145/3660650.3660659"
    title: "Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659"
    author: Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams
---

# Personalize adaptive experiments with Contextual Thompson Sampling to discover what works best for which student groups

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (2 for, 3 mixed, 2 against) · 5 studies (4 causal, 1 theoretical), `q1`–`q2` · 0 of 5 report an effect size · 5 claims rest on one study

## Description
The article proposes extending Thompson Sampling to Contextual TS so instructors "can personalize the improvement process for different groups of students or situations, automatically discovering what works best for whom". It frames this as "another crucial opportunity for the modern classroom that is easy to implement with adaptive experimentation", though the paper itself did not cover it.

## Design Implications

### Context
#### Requirements
- An extension of TS to a contextual variant, and data on student groups or situations to condition the assignment.
#### Constraints
- The article states this direction was not covered in the paper and remains an opportunity for future work.

### Target Learners
- Different groups of students within a CS course

### Target Learning Goals
- Matching support conditions to each student group's needs

### Affordances
- [Thompson Sampling Beta Bernoulli Adaptive Experiments](../research-methods/thompson-sampling-beta-bernoulli-ts-bb.md)

## Claims

- [Instructors valued adaptive experiments using Thompson Sampling for rapidly directing students to better interventions but were concerned about generalizable conclusions](../claims/instructors-value-adaptive-experiments-but-worry-about-inference.md) [~W]
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](../claims/ts-misallocates-participants-equal-reward.md) [~M]
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](../claims/classroom-ts-deployment-uneven-allocation.md) [~W]
- [An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome](../claims/adaptive-bandit-reallocates-majority-to-better-condition.md) [+M]
- [The adaptive trial design reallocates more study subjects to more promising treatment arms as evidence accumulates](../claims/adaptive-allocation-to-promising-arms.md) [+M]
- [The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses](../claims/bandit-inference-issues-persist-across-tests.md) [-W]
- [Thompson Sampling drastically shifted assignment toward a favoured arm with minimal exploration room, but the favoured arm varied across weeks](../claims/ts-drastic-shift-inconsistent-favoured-arm.md) [-W]

## Related Strategies

- [Apply adaptive experiments in CS1 to rapidly improve motivational supports and alternative forms of feedback and explanation](adaptive-experiments-for-cs1-motivation-and-feedback.md)
- [Use a UR-TS hybrid so uniform-random data is retained for analysis while also improving TS assignment](ur-ts-hybrid-design.md)
- [Extend program subgroup analysis from individual characteristics to contextual settings (schools and neighborhoods)](extend-subgroup-analysis-to-contextual-settings.md)

## Examples
-

## Key Sources
- Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659
