---
type: strategy
id: reliability-constraint-in-test-design-strategy
title: Incorporate test reliability as a constraint during test design using the sampling-based modelling paradigm
description: The authors propose extending their sampling-based modelling paradigm beyond scoring into test construction.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: yaman-kumar-singla-2022
    resource: "https://arxiv.org/abs/2111.08906"
    title: "Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. https://arxiv.org/abs/2111.08906"
    author: Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen
---

# Incorporate test reliability as a constraint during test design using the sampling-based modelling paradigm

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors propose extending their sampling-based modelling paradigm beyond scoring into test construction. They note that current test design "involves linguistic validity assessment studies" but "does not take into account the reliability of the ﬁnal test built", and argue that "Reliability of a test could be incorporated as another constraint easily through our modelling paradigm". This makes reliability an explicit design-time criterion alongside linguistic validity.

## Design Implications

### Context
#### Requirements
- The sampling-based estimation paradigm with a human budget and an AS model
#### Constraints
- Proposed as future research; not evaluated in this article

### Target Learners
- test developers and assessment designers of language proficiency tests

### Target Learning Goals
- designing tests whose final reliability is explicitly constrained and estimated

### Affordances
- [Reward Sampling Framework](../research-methods/reward-sampling.md)

## Claims

- [Reward sampling's advantage over baselines is largest at small human budgets (up to about 30% of the dataset) and narrows as the budget grows](../claims/reward-sampling-gains-largest-below-30-percent-budget.md) [+W]
- [Reward sampling with a limited human budget improves global accuracy and QWK of automated scoring systems more than random and uncertainty sampling baselines](../claims/reward-sampling-improves-automated-scoring-accuracy-qwk.md) [+W]
- [A confidence-based secondary sampling procedure estimates post-sampling accuracy and QWK with a 95% statistical guarantee using a sample of 200 candidates](../claims/sampling-based-estimation-accuracy-qwk-guarantees.md) [+W]
- [Uncertainty sampling performs similarly to random sampling on real AS models but approaches reward-sampling performance on a pseudo model with randomly generated predictions](../claims/uncertainty-sampling-gains-depend-on-model-error-structure.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yaman Kumar Singla, Sriram Krishna, Rajiv Ratn Shah, Changyou Chen. (2022). Using Sampling to Estimate and Improve Performance of Automated Scoring Systems with Guarantees. https://arxiv.org/abs/2111.08906
