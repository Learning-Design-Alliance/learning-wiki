---
type: design
id: episode-memory-versioned-erd-states
title: Episode memory linking feedback episodes to versioned ERD states
description: Each feedback request creates a session history containing stages shown, student answers, generated feedback, follow-up questions, credit use, and next actions, allowing later stages to condition on what has already o...
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

# Episode memory linking feedback episodes to versioned ERD states

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Each feedback request creates a session history containing stages shown, student answers, generated feedback, follow-up questions, credit use, and next actions, allowing later stages to condition on what has already occurred. "Episodes are linked to saved artifact states through the student, environment, selected relationship, feedback identifier, and ERD version." Returning to the editor ends the episode, and a later request reproceses the current ERD as a new episode rather than assuming the previous diagnosis remains valid. These records support analysis of progression, disclosure, repetition, and subsequent target-level changes, and are not treated as a persistent model of student knowledge.

## Design Implications

### Context
#### Requirements
- Saved artifact states and logged interactions so episodes can be linked to ERD versions and analyzed
#### Constraints
- Records coordinate the current episode and are explicitly not a persistent student-knowledge model; a new request after revision creates a new diagnosis

### Target Learners
- Students requesting feedback in an ERD editor

### Learning Goals
- Revising conceptual database designs based on staged feedback

### Claims
- [Erd Agent Target Incorporation Rate](../claims/erd-agent-target-incorporation-rate.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sara Riazi and Pedram Rooshenas. (2026). An Educator-Guided LLM Pedagogical Agent for Scaffolded Feedback in Conceptual Database Design. https://arxiv.org/abs/2610.00870v1
