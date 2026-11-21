---
type: strategy
id: grade-dependent-item-allocation-scheme
title: Grade-dependent item allocation that shifts quiz question difficulty upward as student grades rise
description: "The article proposes a four-part item allocation scheme for learning-oriented quizzes: select easy questions first and harder ones as grades rise, re-select questions answered incorrectly in the past, select questions..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: anna-helga-jonsdottir-2013
    resource: "https://arxiv.org/abs/1310.4667"
    title: "Anna Helga Jonsdottir, Gunnar Stefansson. (2013). Enhanced Learning with Web-Assisted Education. https://arxiv.org/abs/1310.4667"
    author: Anna Helga Jonsdottir, Gunnar Stefansson
---

# Grade-dependent item allocation that shifts quiz question difficulty upward as student grades rise

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a four-part item allocation scheme for learning-oriented quizzes: select easy questions first and harder ones as grades rise, re-select questions answered incorrectly in the past, select questions from old material to refresh memory, and select prerequisite-material questions when learning stalls. The first part is implemented via a probability mass function over difficulty ranks that depends on the student's grade, with question difficulty calculated as one minus the proportion of correct answers. When the grade equals a predefined constant the pmf is uniform; below it the mass sits at easy questions and above it at difficult questions.

## Design Implications

### Context
#### Requirements
- item banks must contain questions across a broad difficulty range, which the IRT analysis showed was not yet the case
- question difficulty estimates require tracking how often each question is allocated and answered correctly
#### Constraints
- CAT methods like Point Fisher Information target measuring ability, while tutor-web quizzes aim to increase learning, so they were judged not directly appropriate

### Target Learners
- tutor-web students in statistics and mathematics courses

### Target Learning Goals
- increasing learning through adaptive quiz practice rather than ability measurement

## Claims

- [IRT analysis showed the tutor-web item banks contained more easy than difficult questions](../claims/tutor-web-item-banks-skewed-easy.md) [+W]
- [The two-parameter logistic IRT model fit best only for the hypotheses-concerning-means bank; the one-parameter model sufficed for the other three banks](../claims/irt-model-fit-varies-by-item-bank.md) [~W]

## Related Strategies

- [Item allocation rules: start easy, increase difficulty with grade, and re-select past incorrect and old material with some probability](item-allocation-rules-difficulty-with-grade.md)
- [Mix new and previously solved questions in short mobile quizzes using weighted selection favoring less-recent, previously incorrect, and marked items](weighted-quiz-mixing-new-and-revisit-items.md)

## Examples
-

## Key Sources
- Anna Helga Jonsdottir, Gunnar Stefansson. (2013). Enhanced Learning with Web-Assisted Education. https://arxiv.org/abs/1310.4667
