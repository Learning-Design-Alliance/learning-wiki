---
type: strategy
id: initialize-bandits-with-personalized-difficulty-ranking
title: Initialize multi-armed bandit sequencing with personalized difficulty rankings instead of human expert input
description: "This strategy uses offline learning from students' past interactions to initialize the online behavior of a bandit-based sequencing algorithm."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: avi-segal-2018
    resource: "https://arxiv.org/abs/1804.05212"
    title: "Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom. (2018). Combining Difficulty Ranking with Multi-Armed Bandits to Sequence Educational Content. https://arxiv.org/abs/1804.05212"
    author: Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom
---

# Initialize multi-armed bandit sequencing with personalized difficulty rankings instead of human expert input

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
This strategy uses offline learning from students' past interactions to initialize the online behavior of a bandit-based sequencing algorithm. Where prior work used human experts' knowledge to initialize bandits, this approach instead "use[s] personalized difﬁculty rankings to guide the initial exploitation and update steps of our algorithm". The ranking provides initial estimates of learning gains and is updated over time from student responses.

## Design Implications

### Context
#### Requirements
- Historical data of students' past interactions (grades and retries) from which a personalized difficulty ranking can be computed
#### Constraints
- 

### Target Learners
- students in e-learning systems with varied backgrounds and needs

### Target Learning Goals
- personalized sequencing of practice questions to maximize learning gains

### Affordances
- [Maple Difficulty Ranking Bandit Sequencing](../products/maple-multi-armed-bandits-based-personalization-for-learning-environments.md)

## Claims

- [MAPLE exhibited adaptive sequencing behavior, starting with easy questions and progressively proposing harder ones, unlike the comparison algorithms](../claims/maple-adaptive-sequencing-behavior-simulation.md) [+W]
- [In a classroom field trial, 7th-grade students sequenced by MAPLE achieved higher post-test grades than students sequenced by the Ascending or YBKT algorithms](../claims/maple-field-trial-higher-posttest-grades.md) [+W]
- [Students reported significantly higher satisfaction with questions posed by MAPLE than with the Ascending and YBKT sequencing approaches](../claims/maple-higher-student-satisfaction-field-trial.md) [+W]
- [MAPLE's adaptation needs improvement for weak simulated students, whose estimated skill declined after initial progress](../claims/maple-weak-students-needs-tuning.md) [-W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom. (2018). Combining Difficulty Ranking with Multi-Armed Bandits to Sequence Educational Content. https://arxiv.org/abs/1804.05212
