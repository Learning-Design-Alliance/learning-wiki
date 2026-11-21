---
type: research-method
id: multi-armed-and-contextual-bandit-assistance-selection-method-for-intelligent-tutoring-sys
title: Multi-armed and contextual bandit assistance-selection method for intelligent tutoring systems
description: The article formulates assistance selection as a bandit problem in which each practice question has its own policy over candidate assistance actions.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Multi-armed and contextual bandit assistance-selection method for intelligent tutoring systems

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article formulates assistance selection as a bandit problem in which each practice question has its own policy over candidate assistance actions. The multi-armed bandit policy selects the action that is "optimal on average across all students", while the contextual bandit framework "personalizes decision-making for students by considering their context features" such as ability estimates and response times. The system learned distinct question-specific policies for 10,210 questions across six science courses.

## Accounts
<!-- How each source describes or uses the method -->
- **Multi-armed and contextual bandit formulation of assistance selection in intelligent tutoring systems**: The article formulates assistance selection as a bandit problem in which each practice question has its own policy over candidate assistance actions. The multi-armed bandit policy selects the action that is "optimal on average across all students", while the contextual bandit framework "personalizes decision-making for students by considering their context features" such as ability estimates and response times. The system learned distinct question-specific policies for 10,210 questions across six science courses. (Schmucker et al. (2025))

### Claims
- [Bandit-optimized assistance policies significantly improve student outcomes over a randomized assistance policy in live use across 166,000 practice sessions](../claims/mab-assistance-policy-improves-outcomes-ab-test.md) [+M]
- [Assistance actions exhibit heterogeneous treatment effects across students, but effect sizes are often too small for contextual bandit policies to significantly outperform well-optimized MAB policies](../claims/hte-exists-but-cb-gains-limited.md) [~M]

## Related Research Methods
-

## Key Sources
- Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. https://arxiv.org/abs/2508.00270
