---
type: strategy
id: adaptive-experiments-for-cs1-motivation-and-feedback
title: Apply adaptive experiments in CS1 to rapidly improve motivational supports and alternative forms of feedback and explanation
description: "The article identifies natural application areas for rapid continuous improvement: \"Another prominent direction is to support students' motivation and participation, which is crucial to designing CS1 courses\", blendin..."
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

# Apply adaptive experiments in CS1 to rapidly improve motivational supports and alternative forms of feedback and explanation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 4 studies (4 causal), `q1`–`q2` · 0 of 4 report an effect size · 1 claim rests on one study

## Description
The article identifies natural application areas for rapid continuous improvement: "Another prominent direction is to support students' motivation and participation, which is crucial to designing CS1 courses", blending motivational support with performance feedback. It also notes adaptive experimentation is useful "when it is unclear which form of feedback is more efficient", where the form "could be alternative explanations or even direct vs. metacognitive vs. motivational feedback".

## Design Implications

### Context
#### Requirements
- Student action feedback that the algorithm can use for quick improvement, and instructor-researcher collaboration to imagine and evaluate the support types.
#### Constraints
- Transforming motivation theories into effective support interventions "may be non-trivial".

### Target Learners
- CS1 students

### Target Learning Goals
- Motivation, engagement, belonging, and self-worth
- Understanding via alternative explanations and feedback forms

## Claims

- [An adaptive experiment served the self-explanation prompt condition to 82.6% of its students, a more than 30% reallocation toward the better outcome](../claims/adaptive-bandit-reallocates-majority-to-better-condition.md) [+M]
- [Students shown a self-explanation prompt scored higher on the next problem than students shown no prompt in a traditional CS1 experiment](../claims/self-explanation-prompt-improves-subsequent-cs1-accuracy.md) [+W]
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](../claims/ts-misallocates-participants-equal-reward.md) [~M]

## Related Strategies

- [Personalize adaptive experiments with Contextual Thompson Sampling to discover what works best for which student groups](contextual-ts-personalization-cs1.md)
- [Use a UR-TS hybrid so uniform-random data is retained for analysis while also improving TS assignment](ur-ts-hybrid-design.md)
- [Conduct a smaller sequence of rapid-cycle studies that build on one another instead of planning a single large confirmatory study](sequence-of-smaller-rapid-cycle-dlp-studies.md)

## Examples
-

## Key Sources
- Ilya Musabirov, Angela Zavaleta Bernuy, Pan Chen, Michael Liut, and Joseph Jay Williams. 2024. Opportunities for Adaptive Experiments to Enable Continuous Improvement in Computer Science Education. In The 26th Western Canadian Conference on Computing Education (WCCCE '24). https://doi.org/10.1145/3660650.3660659
