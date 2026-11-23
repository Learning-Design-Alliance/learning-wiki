---
type: design
id: eedi-task-4-personalized-question-selection
title: "Competition Task 4: adaptive personalized selection of ten questions to maximize prediction on held-out answers"
description: Task 4 requires a model to interactively choose a sequence of ten questions per previously unseen student, receiving each revealed answer before choosing the next question, and is then scored on accuracy of predicting...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: zichao-wang-2021
    resource: "https://arxiv.org/abs/2007.12061"
    title: "Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2021). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. https://arxiv.org/abs/2007.12061"
    author: Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang
---

# Competition Task 4: adaptive personalized selection of ten questions to maximize prediction on held-out answers

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Task 4 requires a model to interactively choose a sequence of ten questions per previously unseen student, receiving each revealed answer before choosing the next question, and is then scored on accuracy of predicting binary correctness for a held-out set of that student's answers. The article frames this as personalized dynamic decision making drawing on active learning, reinforcement learning, bandit algorithms, Bayesian experimental design and Bayesian optimization, requiring models to reason about their own uncertainty. Submitted models implement an API with init, select_questions, update_model and predict methods.

## Design Implications

### Context
#### Requirements
- Models must retrain or update after each revealed answer and must upload a pre-trained model, since evaluation workers impose time limits
#### Constraints
- Only ten questions may be queried per student, and the held-out test answers cannot be queried

### Target Learners
- individual students receiving personalized diagnostic assessment

### Learning Goals
- accurately diagnosing a student's understanding while asking the minimum number of questions
- efficient use of student and teacher time

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zichao Wang, Angus Lamb, Evgeny Saveliev, Pashmina Cameron, Yordan Zaykov, José Miguel Hernández-Lobato, Richard E. Turner, Richard G. Baraniuk, Craig Barton, Simon Peyton Jones, Simon Woodhead, Cheng Zhang. (2021). Instructions and Guide for Diagnostic Questions: The NeurIPS 2020 Education Challenge. https://arxiv.org/abs/2007.12061
