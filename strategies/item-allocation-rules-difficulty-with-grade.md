---
type: strategy
id: item-allocation-rules-difficulty-with-grade
title: "Item allocation rules: start easy, increase difficulty with grade, and re-select past incorrect and old material with some probability"
description: "The article proposes implementing four item allocation rules within the system: \"select easy questions in the beginning\", \"increase item diﬃculty as the grade increases\", select with some probability questions the stu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
sources:
  - id: anna-helga-jonsdottir-2014
    resource: "https://arxiv.org/abs/1310.5552"
    title: "Anna Helga Jonsdottir, Gunnar Stefansson. (2014). From evaluation to learning: Some aspects of designing a cyber-university. https://arxiv.org/abs/1310.5552"
    author: Anna Helga Jonsdottir, Gunnar Stefansson
---

# Item allocation rules: start easy, increase difficulty with grade, and re-select past incorrect and old material with some probability

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article proposes implementing four item allocation rules within the system: "select easy questions in the beginning", "increase item diﬃculty as the grade increases", select with some probability questions the student has done incorrectly in the past, and select with some probability questions from old material to refresh memory. A probability mass function over item difficulty, varying with the student's grade, implements a personalized approach.

## Design Implications

### Context
#### Requirements
- An item database with items of varying difficulty linked to the student's dynamic ability
#### Constraints
- Simply increasing mean difficulty with grade is not enough: the mean item difficulty must be linked to ability so that the probability of a correct answer stays closer to 0.5

### Target Learners
- students using on-line drill systems

### Target Learning Goals
- incremental skill building in mathematics and statistics

## Claims

- [Student ability distribution lies far to the right of easy-item difficulty, so item design must give even the best students difficult items on their personalized scale](../claims/ability-distribution-right-of-item-difficulty.md) [+W]
- [Classical IRT models without learning terms do not fit tutor-web drill data; a logistic model with numseen and attempt terms is needed](../claims/irt-models-fail-learning-environment-fitted-logistic-model.md) [+W]
- [Repeated exposure to the same question shows clear evidence of learning, while many attempts predict lower grades consistent with guessing](../claims/repeated-exposure-learning-guessing-at-high-attempts.md) [+W]
- [Students report learning from tutor-web quizzes: 53 of 60 surveyed students found last questions easier than first](../claims/student-survey-learning-quizzes.md) [+W]

## Related Strategies

- [Sequence practice items with an ML algorithm that prioritizes questions by predicted recall probability rather than fixing the rate of study](ml-item-selection-strategy.md)

## Examples
-

## Key Sources
- Anna Helga Jonsdottir, Gunnar Stefansson. (2014). From evaluation to learning: Some aspects of designing a cyber-university. https://arxiv.org/abs/1310.5552
