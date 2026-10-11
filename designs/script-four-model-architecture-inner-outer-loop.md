---
type: design
id: script-four-model-architecture-inner-outer-loop
title: Four-model ITS architecture with inner and outer loop pedagogical model
description: "SCRIPT adopts the standard four-models ITS approach: \"a Pedagogical Model, a Learner Model, a Domain Model, and a User Interface.\" The pedagogical model follows VanLehn's inner/outer loop differentiation: \"The outer l..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: alina-deriyeva-2025
    resource: "https://doi.org/10.1007/978-3-031-99261-2_16"
    title: "Alina Deriyeva, Jesper Dannath, and Benjamin Paaßen. (2025). SCRIPT: Implementing an Intelligent Tutoring System for Programming in a German University Context. Artificial Intelligence in Education (Springer). https://doi.org/10.1007/978-3-031-99261-2_16"
    author: Alina Deriyeva, Jesper Dannath, and Benjamin Paaßen
---

# Four-model ITS architecture with inner and outer loop pedagogical model

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
SCRIPT adopts the standard four-models ITS approach: "a Pedagogical Model, a Learner Model, a Domain Model, and a User Interface." The pedagogical model follows VanLehn's inner/outer loop differentiation: "The outer loop is responsible for task selection and the inner loop is responsible for generating feedback to steps inside programming tasks." The domain model holds tasks, a competency model (Q-matrix), and difficulty information; the learner model derives competency states from UI actions via a knowledge tracing algorithm. Models are designed to be easily replaceable and can be randomly assigned for A/B-testing.

## Design Implications

### Context
#### Requirements
- A knowledge tracing algorithm to derive learner competency from UI actions
- Task-to-skill relations and task difficulty information from the domain model for outer-loop task selection
#### Constraints
- Only part of the features described in the outer and inner loop schemas are implemented; the system is in alpha stage

### Target Learners
- Advanced undergraduate and early postgraduate computer science students

### Learning Goals
- Python programming and data science skills

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Alina Deriyeva, Jesper Dannath, and Benjamin Paaßen. (2025). SCRIPT: Implementing an Intelligent Tutoring System for Programming in a German University Context. Artificial Intelligence in Education (Springer). https://doi.org/10.1007/978-3-031-99261-2_16
