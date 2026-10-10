---
type: design
id: educator-guided-diagnosis-workflow-separation
title: Educator-guided architecture separating artifact-grounded diagnosis, pedagogical workflow control, and student-facing LLM generation
description: The architecture places a hidden, artifact-grounded diagnosis inside an explicit, stateful pedagogical workflow so the language model is not solely responsible for instructional strategy.
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

# Educator-guided architecture separating artifact-grounded diagnosis, pedagogical workflow control, and student-facing LLM generation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The architecture places a hidden, artifact-grounded diagnosis inside an explicit, stateful pedagogical workflow so the language model is not solely responsible for instructional strategy. As the article puts it, "The educator defines the stages, student actions, and disclosure limits, while the LLM selects or generates content within those constraints." The controller assembles the context available to the LLM from the ERD diagnosis, educator resources, and episode history, and logs stage, context, responses, and disclosed information for later review. This preserves student authorship while making the timing, specificity, and extent of automated assistance explicit and configurable.

## Design Implications

### Context
#### Requirements
- Educator-authored requirements, rubrics, concept-aligned questions and resources, and workflow definitions that express governance over disclosure and progression
#### Constraints
- Because the LLM may still produce content that exceeds stage limits, the system logs interactions for later review; staged disclosure cannot protect against wrong-relationship or wrong-concept selection, and the no-error route is unbuffered

### Target Learners
- Undergraduate and mixed-level database systems students

### Learning Goals
- Conceptual database design: translating requirements into entities, attributes, relationships, and semantic constraints in ER diagrams

### Claims
- [Staged Disclosure Diagnostic Error Patterns](../claims/staged-disclosure-diagnostic-error-patterns.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sara Riazi and Pedram Rooshenas. (2026). An Educator-Guided LLM Pedagogical Agent for Scaffolded Feedback in Conceptual Database Design. https://arxiv.org/abs/2610.00870v1
