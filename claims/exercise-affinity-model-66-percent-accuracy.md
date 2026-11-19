---
type: claim
title: "A logistic regression exercise affinity model predicted exercise outcomes with 66% cross-validated accuracy, above a 60% majority-class baseline, and was used to simulate unattempted exercises for bandit pre-training"
description: "A logistic regression exercise affinity model predicted exercise outcomes with 66% cross-validated accuracy, above a 60% majority-class baseline, and was used to simulate unattempted exercises for bandit pre-training"
id: exercise-affinity-model-66-percent-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: robert-belfer-2022
    resource: "https://doi.org/10.1007/978-3-031-11644-5_74"
    title: "Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)"
    author: Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# A logistic regression exercise affinity model predicted exercise outcomes with 66% cross-validated accuracy, above a 60% majority-class baseline, and was used to simulate unattempted exercises for bandit pre-training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The exercise affinity model, trained on approximately 129,000 examples and evaluated with 5-fold cross-validation, achieved 66% accuracy versus 60% for a majority-class baseline. [→ Robert Belfer 2022](#robert-belfer-2022)

## Evidence

### Robert Belfer 2022

Robert Belfer, Ekaterina Kochmar, and Iulian Vlad Serban. (2022). Raising Student Completion Rates with Adaptive Curriculum and Contextual Bandits. arXiv preprint. [doi:10.1007/978-3-031-11644-5_74](https://doi.org/10.1007/978-3-031-11644-5_74)

`q1 · i?` · `causal · r1`

Logistic regression model using student behavior and skills, exercise difficulty, and exercise type features, trained on historical attempt data from 1,977 students. It achieved "an accuracy of66%" under 5-fold cross-validation against a 60% majority-class baseline, and was used to predict 165,000 exercise attempts to simulate unattempted exercises.

> "We train the model on approximately129,000 examples and evaluate it using 5-fold cross-validation, observing an accuracy of66%. A baseline model that selects the majority class100% of the time achieves an accuracy of60%."

## Discussion


## Related Claims
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-user and customer cohorts](linucb-rct-higher-completion-lower-skip.md) — related
- [A logistic regression model using topic success and topic skip features predicts next-exercise success with 80% accuracy](logistic-regression-predicts-next-exercise-success-80-percent.md) — related
