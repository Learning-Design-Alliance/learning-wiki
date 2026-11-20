---
type: claim
title: Tuning Apprentice Learner agents to individual students with HyperOpt reduces prediction error relative to a generic baseline on the tutor problems used for tuning
description: Tuning Apprentice Learner agents to individual students with HyperOpt reduces prediction error relative to a generic baseline on the tutor problems used for tuning
id: hyperopt-tuned-agents-lower-error-same-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: christopher-james-maclellan-2024
    resource: "https://doi.org/10.48550/arXiv.2408.13684"
    title: "Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2024). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. Originally published 2022. [doi:10.48550/arXiv.2408.13684](https://doi.org/10.48550/arXiv.2408.13684)"
    author: Christopher James MacLellan, Kimberly Stowers, Lisa Brady
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Tuning Apprentice Learner agents to individual students with HyperOpt reduces prediction error relative to a generic baseline on the tutor problems used for tuning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Tuned models have lower error than the generic baseline and better approximate human learning trajectories when trained and tested on the same data. [→ Christopher James MacLellan 2024](#christopher-james-maclellan-2024)

## Evidence

### Christopher James MacLellan 2024

Christopher James MacLellan, Kimberly Stowers, Lisa Brady. (2024). Evaluating Alternative Training Interventions Using Personalized Computational Models of Learning. Advances in Cognitive Systems, 10. Originally published 2022. [doi:10.48550/arXiv.2408.13684](https://doi.org/10.48550/arXiv.2408.13684)

`q2 · i?` · `design · r2`

Simulation study tuning 24 Apprentice Learner agents to 24 students with 20 HyperOpt iterations each, simulating the first ten tutor problems; Figure 4(a) shows tuned agents had "lower error than the baseline". No effect size printed.

> "The main finding is that the tuned models have lower error than the baseline and better approximate the human learning trajectories."

## Discussion


## Related Claims
- [HyperOpt tuning also improves predictions of target students' performance on unseen later problems (temporal cross-validation)](tuned-agents-better-unseen-data.md) — a narrower finding that bears on this claim
- [Simulated learners can match human error rates overall while learning faster and making different kinds of errors than the students they model](simulated-learners-differ-from-humans-in-error-types.md) — related
- [A computational model of learning reproduced the direction of two tutor A/B experiments without human training data, but not students' absolute performance](computational-learner-model-predicts-tutor-experiment-direction.md) — related
