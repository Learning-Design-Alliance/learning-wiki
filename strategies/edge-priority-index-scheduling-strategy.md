---
type: strategy
id: edge-priority-index-scheduling-strategy
title: Schedule practice by a priority index over topics and run sessions with a difficulty ramp
description: The EdgeScheduler computes, for each topic, an expected one-step gain, a time cost, and a hazard term equal to the negative derivative of retention, then selects the B topics with the largest priority index under a da...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: ananda-prakash-verma-2025
    resource: "https://arxiv.org/abs/2508.07224"
    title: "Ananda Prakash Verma. (2025). EDGE: A Theoretical Framework for Misconception-Aware Adaptive Learning. arXiv:2508.07224. https://arxiv.org/abs/2508.07224"
    author: Ananda Prakash Verma
---

# Schedule practice by a priority index over topics and run sessions with a difficulty ramp

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The EdgeScheduler computes, for each topic, an expected one-step gain, a time cost, and a hazard term equal to the negative derivative of retention, then selects the B topics with the largest priority index under a daily budget. Sessions interleave selected topics by concept distance and execute a difficulty ramp from easy through on-level and slightly hard items to cross-topic work and recap. This operationalizes the Exercise stage of EDGE.

## Design Implications

### Context
#### Requirements
- Per-topic learner state (ability, variance, retention, misconception posteriors) and a daily practice budget B
#### Constraints
- Near-optimality of the index policy holds only under the separability assumptions of Theorem 1

### Target Learners
- learners preparing for high-stakes exams under time budgets

### Target Learning Goals
- jointly maximizing mastery and retention of topics

### Affordances
- Edge Misconception Aware Adaptive Framework

## Claims

- [The EDGE index policy is a near-optimal (1/(1+ϵ))-approximation to the optimal budgeted scheduling policy under separable gains](../claims/edge-index-policy-near-optimal-scheduling.md) [+W]
- [EdgeScore is monotone nondecreasing in its mastery, retention, pace, and confidence components and Lipschitz continuous (proven)](../claims/edgescore-monotone-lipschitz-guarantee.md) [+W]
- [Selecting 2PL items near ability equal to difficulty maximizes Fisher information, which EDGE respects while adding misconception-corrective gains](../claims/item-selection-near-ability-maximizes-information.md) [+W]

## Related Strategies

- [Spaced Practice Scheduling](spaced-practice-scheduling.md)

## Examples
-

## Key Sources
- Ananda Prakash Verma. (2025). EDGE: A Theoretical Framework for Misconception-Aware Adaptive Learning. arXiv:2508.07224. https://arxiv.org/abs/2508.07224
