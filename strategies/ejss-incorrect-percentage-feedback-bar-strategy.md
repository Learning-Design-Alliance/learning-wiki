---
type: strategy
id: ejss-incorrect-percentage-feedback-bar-strategy
title: Provide a visual percentage bar of incorrect answers per question so teachers can quickly identify which questions to discuss in class
description: The paper recommends a visual indicator showing the percentage of students who provided incorrect answers for each question, described as a commonly requested feature.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: wee-2021
    resource: "https://iwant2study.org/moodle402/"
    title: "Wee, L. K., Tan, D., Garcia Clemente, F. J., & Esquembre, F. (2021). Easy JavaScript Simulation (EJSS) Data Analytics for Singapore. https://iwant2study.org/moodle402/"
    author: "Wee, L. K., Tan, D., Garcia Clemente, F. J., & Esquembre, F"
---

# Provide a visual percentage bar of incorrect answers per question so teachers can quickly identify which questions to discuss in class

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (1 causal, 1 qualitative, 1 design), `q2`–`q3` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The paper recommends a visual indicator showing the percentage of students who provided incorrect answers for each question, described as a commonly requested feature. The authors state this indicator bar "is intuitive, obviating the necessity for teachers to scroll through and manually tally instances of incorrect responses, saving valuable classroom time and precious cognitive effort". In their implementation, a visual bar showing, for example, 15% of students awarded 0 marks helps teachers quickly identify which questions to discuss in class.

## Design Implications

### Context
#### Requirements
- The dashboard must automatically mark and tally student answers per question (grading criteria defined in assessment.json) to compute the percentage
#### Constraints
- The reported benefit is the authors' design rationale and teacher demand for the feature, not a measured effect on teaching quality or time

### Target Learners
- School classes using EJSS simulations through SLS

### Target Learning Goals
- Supporting teachers' whole-class feedback and selection of questions to review

### Affordances
- [Ejss Dashboard Five Design Considerations](../designs/ejss-dashboard-five-design-considerations.md)

## Claims

- [Online-related decreases in MCMR difficulty arise from students choosing incorrect responses in addition to correct ones, not from choosing no correct responses](../claims/mcmr-online-decrease-mixed-correct-incorrect-selection.md) [~W]
- [Even students who choose the wrong answer on a multiple-choice physics question can generate the correct explanation when prompted for alternatives](../claims/wrong-answer-students-generate-correct-explanations.md) [+W]
- [Asking students to draw a graph before showing multiple-choice options leads to a significantly higher percentage ultimately answering the clicker question correctly](../claims/draw-graph-first-improves-clicker-answers.md) [+W]

## Related Strategies

- [Embrace Errors as Learning Opportunities](embrace_errors_as_learning_opportunities.md)

## Examples
-

## Key Sources
- Wee, L. K., Tan, D., Garcia Clemente, F. J., & Esquembre, F. (2021). Easy JavaScript Simulation (EJSS) Data Analytics for Singapore. https://iwant2study.org/moodle402/
