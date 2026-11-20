---
type: strategy
id: ur-ts-hybrid-design
title: Use a UR-TS hybrid so uniform-random data is retained for analysis while also improving TS assignment
description: The article describes a hybrid design in which, with epsilon = 0.5 probability, arms are assigned using uniform randomization while TS updating uses data from the UR participants too.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: zavaleta-bernuy-2022
    resource: "https://arxiv.org/abs/2208.05092"
    title: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2022). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. https://arxiv.org/abs/2208.05092"
    author: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J"
---

# Use a UR-TS hybrid so uniform-random data is retained for analysis while also improving TS assignment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (6 for, 1 mixed) · 4 studies (4 causal), `q1`–`q2` · 0 of 4 report an effect size · 6 claims rest on one study

## Description
The article describes a hybrid design in which, with epsilon = 0.5 probability, arms are assigned using uniform randomization while TS updating uses data from the UR participants too. The authors motivate it because "scientists may want to get the beneﬁts of obtaining data under UR (in case TS introduces biases) for analysis, while also then using that data to improve the performance of the TS algorithm". This takes inspiration from epsilon-greedy and top-two TS algorithms.

## Design Implications

### Context
#### Requirements
- Running a parallel uniform-random assignment stream alongside the adaptive assignments so unbiased data remains available for analysis
#### Constraints
- The article notes TS may introduce biases, which is the motivation for retaining UR data

### Target Learners
- students in digital educational environments participating in field experiments

### Target Learning Goals
- rapidly identifying and assigning more effective instructional conditions while preserving scientific inference

### Affordances
- [Thompson Sampling Mab Adaptive Assignment](../research-methods/multi-armed-randomized-trial-analysis.md)

## Claims

- [Thompson Sampling drastically shifted assignment toward a favoured arm with minimal exploration room, but the favoured arm varied across weeks](../claims/ts-drastic-shift-inconsistent-favoured-arm.md) [+W]
- [When arms are equally effective, TS may randomly favour an arm, which is problematic for scientific inference](../claims/ts-misallocates-participants-equal-reward.md) [+W]
- [The FPR inflation and Power reduction from Thompson Sampling persist across Welch's t-test and Bayes factor analyses](../claims/bandit-inference-issues-persist-across-tests.md) [+W]
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](../claims/classroom-ts-deployment-uneven-allocation.md) [+W]
- [Instructors valued adaptive experiments using Thompson Sampling for rapidly directing students to better interventions but were concerned about generalizable conclusions](../claims/instructors-value-adaptive-experiments-but-worry-about-inference.md) [~W]
- [Thompson Sampling and TS† exploit a single arm even when no significant difference exists among arm means](../claims/bandit-exploitation-without-significant-arm-difference.md) [+W]
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](../claims/mab-overestimates-effect-sizes.md) [+W]

## Related Strategies

- [Personalize adaptive experiments with Contextual Thompson Sampling to discover what works best for which student groups](contextual-ts-personalization-cs1.md)
- [Apply adaptive experiments in CS1 to rapidly improve motivational supports and alternative forms of feedback and explanation](adaptive-experiments-for-cs1-motivation-and-feedback.md)

## Examples
-

## Key Sources
- Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2022). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. https://arxiv.org/abs/2208.05092
