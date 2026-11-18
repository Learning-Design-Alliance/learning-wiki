---
type: product
id: maple-multi-armed-bandits-based-personalization-for-learning-environments
title: MAPLE (Multi-Armed Bandits based Personalization for Learning Environments)
description: An adaptive question-sequencing algorithm developed by Avi Segal and colleagues that combines personalized difficulty ranking with multi-armed-bandit exploration to select practice questions for e-learning students.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# MAPLE (Multi-Armed Bandits based Personalization for Learning Environments)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
An adaptive question-sequencing algorithm developed by Avi Segal and colleagues that combines personalized difficulty ranking with multi-armed-bandit exploration to select practice questions for e-learning students.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **MAPLE: combining personalized difficulty ranking with multi-armed bandits for sequencing educational content**: MAPLE (Multi-Armed Bandits based Personalization for Learning Environments) is a computational approach that sequences questions by maintaining a belief distribution over expected learning gains for each question, initialized with a personalized difficulty ranking. It uses an EXP4-like exploration policy: "When a student successfully solves a question, weights are adjusted to make harder questions more likely to be presented", and when a student fails, weights shift toward easier questions and exploration narrows. The algorithm draws on the zone of proximal development, presenting challenges slightly beyond current abilities. (Avi Segal et al. (2018))

### Claims

- [In a classroom field trial, 7th-grade students sequenced by MAPLE achieved higher post-test grades than students sequenced by the Ascending or YBKT algorithms](../claims/maple-field-trial-higher-posttest-grades.md) [+M]
- [MAPLE exhibited adaptive sequencing behavior, starting with easy questions and progressively proposing harder ones, unlike the comparison algorithms](../claims/maple-adaptive-sequencing-behavior-simulation.md) [+W]
- [Students reported significantly higher satisfaction with questions posed by MAPLE than with the Ascending and YBKT sequencing approaches](../claims/maple-higher-student-satisfaction-field-trial.md) [+W]
- [MAPLE's adaptation needs improvement for weak simulated students, whose estimated skill declined after initial progress](../claims/maple-weak-students-needs-tuning.md) [-W]

## Related Products and Programmes
-

## Key Sources
- Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom. (2018). Combining Difficulty Ranking with Multi-Armed Bandits to Sequence Educational Content. https://arxiv.org/abs/1804.05212
