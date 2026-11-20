---
type: research-method
id: hyperopt-based-tuning-of-apprentice-learner-agents
title: HyperOpt-based tuning of Apprentice Learner agents
description: This approach uses the HyperOpt toolkit to automatically tailor Apprentice Learner agents to specific students.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# HyperOpt-based tuning of Apprentice Learner agents

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This approach uses the HyperOpt toolkit to automatically tailor Apprentice Learner agents to specific students. Each agent is parameterized by initial skills (prior knowledge) and cognitive parameters such as disposition towards exploration; HyperOpt iteratively samples configurations, simulates the target student, evaluates step-level prediction accuracy, and uses Bayesian inference to update its sampling distribution until it converges toward a configuration that minimizes differences with the student. Unlike knowledge tracing, it estimates a student's initial knowledge state with an explicit, interpretable mechanistic model rather than an abstract probability of knowing.

## Accounts
<!-- How each source describes or uses the method -->
- **HyperOpt-based model tuning: automatically personalizing cognitive models to individual students from performance data**: This approach uses the HyperOpt toolkit to automatically tailor Apprentice Learner agents to specific students. Each agent is parameterized by initial skills (prior knowledge) and cognitive parameters such as disposition towards exploration; HyperOpt iteratively samples configurations, simulates the target student, evaluates step-level prediction accuracy, and uses Bayesian inference to update its sampling distribution until it converges toward a configuration that minimizes differences with the student. Unlike knowledge tracing, it estimates a student's initial knowledge state with an explicit, interpretable mechanistic model rather than an abstract probability of knowing. (Christopher James MacLellan et al. (2022))

### Claims
- [Tuning Apprentice Learner agents to individual students with HyperOpt reduces prediction error relative to a generic baseline on the tutor problems used for tuning](../claims/hyperopt-tuned-agents-lower-error-same-data.md) [+M]
- [HyperOpt tuning also improves predictions of target students' performance on unseen later problems (temporal cross-validation)](../claims/tuned-agents-better-unseen-data.md) [+M]

## Related Research Methods
-

## Key Sources
- Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2022). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. https://arxiv.org/abs/2408.13684
