---
type: design
id: four-specialized-evaluation-agents-llm-problems
title: Four specialized evaluation agents for LLM-generated problems
description: "The system employs four agents that each evaluate a different dimension of generated problems: an Authenticity agent evaluating whether the context is age-appropriate and likely to be relatable for middle school learn..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: walkington-2025
    title: Walkington, C., Beauchamp, T., Ikram, F., Koçyiğit Gürbüz, M., Xia, F., Lee, M., Lan, A. (2025). Mathematics Teachers’ Interactions with a Multi-Agent System for Personalized Problem Generation.
    author: Walkington, C., Beauchamp, T., Ikram, F., Koçyiğit Gürbüz, M., Xia, F., Lee, M., Lan, A
---

# Four specialized evaluation agents for LLM-generated problems

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The system employs four agents that each evaluate a different dimension of generated problems: an Authenticity agent evaluating whether the context is age-appropriate and likely to be relatable for middle school learners; a Realism agent evaluating whether quantities, units, and contextual details are plausible for the chosen topic; a Reading-level agent evaluating whether vocabulary and sentence complexity match the intended reading level; and a Hallucination agent evaluating whether the problem is mathematically consistent with the original. Each agent returns a binary pass/fail decision, and failed cases return identified issues that are combined and provided to a refinement agent.

## Design Implications

### Context
#### Requirements
- Each agent has a specified role and prompt; issues from failed cases are combined and provided to a refinement agent
#### Constraints
- Each agent returns a binary pass/fail decision rather than a graded assessment

### Target Learners
- Middle school mathematics students (7th grade)

### Learning Goals
- Ensuring quality of LLM-generated personalized math problems across authenticity, realism, readability, and mathematical accuracy

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Walkington, C., Beauchamp, T., Ikram, F., Koçyiğit Gürbüz, M., Xia, F., Lee, M., Lan, A. (2025). Mathematics Teachers’ Interactions with a Multi-Agent System for Personalized Problem Generation.
