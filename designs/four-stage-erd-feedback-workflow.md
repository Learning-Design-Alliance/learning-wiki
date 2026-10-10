---
type: design
id: four-stage-erd-feedback-workflow
title: "Four-stage learner-controlled workflow: concept check, guided application, guided feedback, and guided Q&A"
description: The deployed workflow implements graduated prompting under learner control in an ERD editor.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: sara-riazi-and-pedram-rooshenas-2026
    resource: "https://arxiv.org/abs/2610.00870v1"
    title: "Sara Riazi and Pedram Rooshenas. (2026). An Educator-Guided LLM Pedagogical Agent for Scaffolded Feedback in Conceptual Database Design. https://arxiv.org/abs/2610.00870v1"
    author: Sara Riazi and Pedram Rooshenas
---

# Four-stage learner-controlled workflow: concept check, guided application, guided feedback, and guided Q&A

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The deployed workflow implements graduated prompting under learner control in an ERD editor. "The deployed workflow follows graduated prompting under learner control [3, 11, 33]. Each accessed stage consumes one feedback credit." Stage 1 uses an educator-authored question pool the LLM selects from without modifying; Stage 2 fills template slots from the selected ERD component and evaluates responses against a reference rubric; Stage 3 gives concise artifact-grounded feedback while withholding the localized correction; Stage 4 supports multi-turn requirement-grounded clarification without generating the complete ERD. After every interaction, students may revise the ERD or request more explicit assistance, so each stage can be a stopping point.

## Design Implications

### Context
#### Requirements
- Educator-defined stage sequence, question pools, templates with reference rubrics, and feedback credits; the diagnostic pipeline from a prior requirement-grounded ERD feedback system
#### Constraints
- Progression is learner-controlled rather than automatic; the agent does not modify the ERD; each accessed stage consumes one credit

### Target Learners
- Undergraduate database systems students revising ER diagrams

### Learning Goals
- Applying modeling concepts such as identifying relationships, weak entities, cardinality, and participation constraints to specific requirements

### Claims
- [Early Stage Exit Incorporation](../claims/early-stage-exit-incorporation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sara Riazi and Pedram Rooshenas. (2026). An Educator-Guided LLM Pedagogical Agent for Scaffolded Feedback in Conceptual Database Design. https://arxiv.org/abs/2610.00870v1
