---
type: design
id: strategy-selection-criteria-from-student-model-states
title: "Self-improving mechanism: learning strategy-selection criteria from student model states by concept learning from examples"
description: "The article's central mechanism account is that a tutor can improve itself by inducing selection criteria from its own experience."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-18
sources:
  - id: dillenbourg-1989
    resource: "https://doi.org/10.1007/BF00053359"
    title: "Dillenbourg, P. (1989). The design of a self-improving tutor: PROTO-TEG. Instructional Science, 18(3), 193–216. https://doi.org/10.1007/BF00053359"
    author: Dillenbourg, P
---

# Self-improving mechanism: learning strategy-selection criteria from student model states by concept learning from examples

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's central mechanism account is that a tutor can improve itself by inducing selection criteria from its own experience. Criteria "are expressed as characteristics of the student model" and are "elaborated by comparing student model states recorded when a strategy was effective and those recorded when the same strategy was not effective". The comparison is performed by machine learning methods, "more precisely, by learning concepts from examples", so each tutoring episode contributes a labelled example of strategy success or failure.

## Design Implications

### Context
#### Requirements
- Recorded student model states from episodes where a strategy was effective and where it was not effective
- Machine learning methods able to learn concepts from examples
#### Constraints
- Criteria are limited to characteristics expressible in the student model

### Target Learners
- geometry learners

### Learning Goals
- adaptive selection of didactic strategies during tutoring

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Dillenbourg, P. (1989). The design of a self-improving tutor: PROTO-TEG. Instructional Science, 18(3), 193–216. https://doi.org/10.1007/BF00053359
