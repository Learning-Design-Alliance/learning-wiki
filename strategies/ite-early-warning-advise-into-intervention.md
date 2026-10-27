---
type: strategy
id: ite-early-warning-advise-into-intervention
title: Use individualized treatment effect estimates as an early warning system to advise students into an intervention at the start of a course
description: The article recommends using ITE predictions early in a course to identify and advise students who would likely benefit from an intervention such as supplemental instruction.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: beemer-2018
    resource: "https://doi.org/10.1007/s40593-017-0148-x"
    title: "Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A. (2018). Ensemble Learning for Estimating Individualized Treatment Effects in Student Success Studies. International Journal of Artificial Intelligence in Education, 28, 315–335. https://doi.org/10.1007/s40593-017-0148-x"
    author: "Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A"
---

# Use individualized treatment effect estimates as an early warning system to advise students into an intervention at the start of a course

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends using ITE predictions early in a course to identify and advise students who would likely benefit from an intervention such as supplemental instruction. It states that "the ITE may be used, say at the beginning of a course, to flag students that may benefit from the supplemental instruction course", with at-risk characteristics drawn from demographic and educational markers such as weaker preparation and first-generation or low-income status. Predicted grade-letter improvements for individual students can then guide advising into the intervention.

## Design Implications

### Context
#### Requirements
- A trained ensemble learner capable of producing ITE predictions from student information system and learning management system data available early in the term
#### Constraints
- ITE estimates may be biased by unobserved confounders such as motivation or attitudes, which were not measured in this study

### Target Learners
- students at the beginning of a bottleneck course
- at-risk subgroups such as EOP, first-generation, and low-income students

### Target Learning Goals
- early identification and advising of students likely to benefit from an intervention to improve course success

### Affordances
- [Individualized Treatment Effects Framework](../research-methods/individualized-treatment-effects-ite-framework-for-student-success-analytics.md)

## Claims

- [Enrollment in the supplemental instruction section is associated with significantly positive average individualized treatment effects on final exam score and course grade](../claims/si-positive-average-ite-exam-grade.md) [+W]
- [Underrepresented minority students in the course showed significantly positive individualized treatment effects from supplemental instruction](../claims/si-urm-subgroup-positive-ite.md) [+W]

## Related Strategies

- [Integrate background grade-prediction models into early alert advising systems](grade-prediction-early-alert-integration.md)

## Examples
-

## Key Sources
- Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A. (2018). Ensemble Learning for Estimating Individualized Treatment Effects in Student Success Studies. International Journal of Artificial Intelligence in Education, 28, 315–335. https://doi.org/10.1007/s40593-017-0148-x
