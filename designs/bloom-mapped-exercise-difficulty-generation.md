---
type: design
id: bloom-mapped-exercise-difficulty-generation
title: Bloom-level mapping of exercise difficulty levels in AI exercise generation
description: "The exercise-generation tool maps its three difficulty levels directly onto Bloom's Taxonomy cognitive levels within the system prompt: easy prompts tasks focused on remembering and understanding, medium on applying a..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: gabelmann-2026
    resource: "https://arxiv.org/abs/2605.30187"
    title: "Gabelmann, J., Jahn, F., Baum, K., van Rossum, S., Wuenscher, E., Gros, T. P., Wolf, V. (2026). Modularizing Educational LLM-Agency for Fostering Responsible Learning Assistance. https://arxiv.org/abs/2605.30187"
    author: Gabelmann, J., Jahn, F., Baum, K., van Rossum, S., Wuenscher, E., Gros, T. P., Wolf, V
---

# Bloom-level mapping of exercise difficulty levels in AI exercise generation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The exercise-generation tool maps its three difficulty levels directly onto Bloom's Taxonomy cognitive levels within the system prompt: easy prompts tasks focused on remembering and understanding, medium on applying and analyzing, and hard on evaluating and creating. The authors state this 'ensures that the task's complexity is grounded in established theory', aligning generated exercises with the pedagogical goal of challenging students across cognitive levels.

## Design Implications

### Context
#### Requirements
- Users configure topic, exercise type, and difficulty parameters
#### Constraints
- 

### Target Learners
- students generating practice exercises

### Learning Goals
- exercising across all six Bloom taxonomy cognitive levels

### Claims
- 

## Related Designs

- [Hybrid micro-level personalization framework combining learner-driven preferences with system-driven Bloom's Taxonomy cognitive assessment](hybrid-micro-personalization-framework.md)
- [Six-phase assignment process mapped to BRT cognitive steps](brt-six-phase-assignment-process.md)

## Examples
-

## Key Sources
- Gabelmann, J., Jahn, F., Baum, K., van Rossum, S., Wuenscher, E., Gros, T. P., Wolf, V. (2026). Modularizing Educational LLM-Agency for Fostering Responsible Learning Assistance. https://arxiv.org/abs/2605.30187
