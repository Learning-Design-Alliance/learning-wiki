---
type: strategy
id: simulate-then-test-intervention-screening
title: "Simulate-then-test workflow: use personalized computational models to screen interventions before running costly human experiments"
description: Intervention designers can use personalized computational models to run low-cost simulations evaluating many alternative training interventions, then run human studies only on the interventions the simulations suggest...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: christopher-james-maclellan-2022
    resource: "https://arxiv.org/abs/2408.13684"
    title: "Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2022). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. https://arxiv.org/abs/2408.13684"
    author: Christopher James MacLellan, Kimberly Stowers, Lisa Brady
---

# Simulate-then-test workflow: use personalized computational models to screen interventions before running costly human experiments

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
Intervention designers can use personalized computational models to run low-cost simulations evaluating many alternative training interventions, then run human studies only on the interventions the simulations suggest are most promising. The article frames this as analogous to bridge designers using parametric analysis to test designs computationally before real-world deployment, addressing the cost and one-size-fits-all limitations of A/B experiments.

## Design Implications

### Context
#### Requirements
- Evidence that counterfactual predictions approximate human performance is needed before designers can trust the model's predictions
#### Constraints
- Counterfactual predictions have no ground truth by definition, so their evaluation requires future human experiments

### Target Learners
- training intervention designers, teachers, and instructional designers

### Target Learning Goals
- selecting effective training interventions cost-effectively

### Affordances
- [Apprentice Learner Architecture Counterfactual](../products/apprentice-learner-architecture.md)

## Claims

- [For the low-performing student, the faded blocked-to-interleaved condition is predicted to yield lower error that decreases faster than either blocked or interleaved practice](../claims/faded-condition-faster-learning-low-performer.md) [+M]
- [For the high-performing student, predicted performance in the faded condition is almost identical to the blocked condition, and the choice of intervention matters little given ample prior knowledge](../claims/high-performer-intervention-insensitive.md) [+M]
- [Tuning Apprentice Learner agents to individual students with HyperOpt reduces prediction error relative to a generic baseline on the tutor problems used for tuning](../claims/hyperopt-tuned-agents-lower-error-same-data.md) [+M]
- [Personalized Apprentice Learner models counterfactually predict higher error during practice in the interleaved condition than the blocked condition for both high- and low-performing students](../claims/personalized-models-blocked-lower-error-than-interleaved.md) [+M]
- [HyperOpt tuning also improves predictions of target students' performance on unseen later problems (temporal cross-validation)](../claims/tuned-agents-better-unseen-data.md) [+M]
- [A computational model of learning reproduced the direction of two tutor A/B experiments without human training data, but not students' absolute performance](../claims/computational-learner-model-predicts-tutor-experiment-direction.md) [+M]

## Related Strategies

- [Evaluate LLM-based tutors with human-inspired methods such as simulated students and behavior analysis before classroom deployment](human-inspired-evaluation-of-llm-tutors.md)

## Examples
-

## Key Sources
- Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2022). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. https://arxiv.org/abs/2408.13684
