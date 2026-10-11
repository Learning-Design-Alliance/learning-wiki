---
type: research-method
id: three-pooling-formulations-for-bayesian-knowledge-tracing-standard-multi-and-hierarchical
title: Three pooling formulations for Bayesian Knowledge Tracing (standard, multi, and hierarchical)
description: StanBKT organizes BKT formulations into three pooling types.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Three pooling formulations for Bayesian Knowledge Tracing (standard, multi, and hierarchical)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
StanBKT organizes BKT formulations into three pooling types. Standard BKT shares a single parameter set across all students (full pooling, assuming homogeneous learning and response behavior). Multi BKT estimates a separate parameter set for each predefined group such as classrooms, treatment conditions, or individual students, enabling direct comparison across groups. Hierarchical BKT introduces partial pooling through hierarchical priors, decomposing each parameter into a global component and group-level deviations with a learned variance controlling shrinkage. The article states this formulation "stabilizes and regularizes estimates in sparse data contexts while preserving systematic differences across groups."

## Accounts
<!-- How each source describes or uses the method -->
- **Three pooling formulations for BKT: standard, multi (group-specific), and hierarchical (partial pooling)**: StanBKT organizes BKT formulations into three pooling types. Standard BKT shares a single parameter set across all students (full pooling, assuming homogeneous learning and response behavior). Multi BKT estimates a separate parameter set for each predefined group such as classrooms, treatment conditions, or individual students, enabling direct comparison across groups. Hierarchical BKT introduces partial pooling through hierarchical priors, decomposing each parameter into a global component and group-level deviations with a learned variance controlling shrinkage. The article states this formulation "stabilizes and regularizes estimates in sparse data contexts while preserving systematic differences across groups." (Siddhartha Pradhan et al. (2026))

### Claims
- [In a perceptual-cue intervention reanalysis, incongruent spacing and incongruent color conditions were associated with reduced guessing relative to neutral conditions](../claims/incongruent-perceptual-cues-reduce-guessing-bkt.md) [+M]

## Related Research Methods
-

## Key Sources
- Siddhartha Pradhan, Yanping Pei, Morgan Lee, Puyuan Zhang, Erin Ottmar, and Adam C. Sales. (2026). StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing. https://arxiv.org/abs/2605.23048
