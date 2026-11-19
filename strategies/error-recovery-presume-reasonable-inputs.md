---
type: strategy
id: error-recovery-presume-reasonable-inputs
title: Prefer error-recovery policies for teachable agents that assume learner inputs are reasonable and move to the next step
description: Based on the null correlations between misrecognition and learning or rapport, the authors recommend that an optimal error-recovery strategy for teachable agents should prefer moving to the next step, assuming learner...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: yuya-asano-2023
    resource: "https://arxiv.org/abs/2306.07302"
    title: "Yuya Asano, Diane Litman, Mingzhi Yu, Nikki Lobczowski, Timothy Nokes-Malach, Adriana Kovashka, and Erin Walker. (2023). Impact of Experiencing Misrecognition by Teachable Agents on Learning and Rapport. https://arxiv.org/abs/2306.07302"
    author: Yuya Asano, Diane Litman, Mingzhi Yu, Nikki Lobczowski, Timothy Nokes-Malach, Adriana Kovashka, and Erin Walker
---

# Prefer error-recovery policies for teachable agents that assume learner inputs are reasonable and move to the next step

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Based on the null correlations between misrecognition and learning or rapport, the authors recommend that an optimal error-recovery strategy for teachable agents should prefer moving to the next step, assuming learners give reasonable inputs, rather than expressing that it does not understand the input. They acknowledge this "may sound counterintuitive because it may deprive learners of opportuni-ties to realize their misunderstanding", but suggest this disadvantage may be canceled out by exposure to correct solutions and more problems. They also note the policy may aid inclusion by avoiding generic responses stemming from ASR's poor performance on accented speech and minoritized dialects.

## Design Implications

### Context
#### Requirements
- Future research is needed, as the authors state, to test how this policy affects rapport, learning, and other outcomes such as engagement
#### Constraints
- The recommendation rests on correlational evidence from a small sample (n = 38) with a pattern-matching dialogue system, not on a test of the policy itself

### Target Learners
- undergraduate students teaching a virtual agent

### Target Learning Goals
- learning by teaching
- rapport with teachable agents

## Claims

- [Overall dialogue misrecognition by a teachable agent is not significantly correlated with students' learning gains](../claims/misrecognition-not-correlated-learning-gains.md) [+W]
- [Overall dialogue misrecognition by a teachable agent is not significantly correlated with students' rapport with the agent](../claims/misrecognition-not-correlated-rapport.md) [+W]
- [None of the three subtypes of dialogue misrecognition (Prevented, Different, Proceeded) is significantly correlated with learning or rapport, though Prevented is marginally negatively correlated with rapport](../claims/misrecognition-subtypes-null-correlations.md) [+W]
- [ASR word error rates are not correlated with rapport, learning, or overall dialogue misrecognition in this teachable-agent study](../claims/word-error-rate-no-correlation-teachable-agent.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yuya Asano, Diane Litman, Mingzhi Yu, Nikki Lobczowski, Timothy Nokes-Malach, Adriana Kovashka, and Erin Walker. (2023). Impact of Experiencing Misrecognition by Teachable Agents on Learning and Rapport. https://arxiv.org/abs/2306.07302
