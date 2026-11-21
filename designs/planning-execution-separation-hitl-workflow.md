---
type: design
id: planning-execution-separation-hitl-workflow
title: Two-stage planning-then-execution workflow with objective specifications and world-model constraints
description: "The curriculum \"separates problem solving into planning and execution phases\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: mark-dranias-and-adam-whitley-2025
    title: Mark Dranias and Adam Whitley. (2025). Human-in-the-Loop Control of Objective Drift in LLM-Assisted Computer Science Education.
    author: Mark Dranias and Adam Whitley
---

# Two-stage planning-then-execution workflow with objective specifications and world-model constraints

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The curriculum "separates problem solving into planning and execution phases". In the planning stage, before substantial AI code generation, students produce an objective specification (quality measures, acceptance criteria checklists) and world model constraints (task scope, libraries, architectures, permitted approaches), iteratively refined with instructor feedback into a project instruction file attached to the LLM context. In the execution stage, students implement with AI assistance within those bounds, monitor outputs against the artifacts, treat violations as control failures, and correct to produce a compliant deliverable.

## Design Implications

### Context
#### Requirements
- Planning artifacts must be produced and refined with instructor feedback before any substantial AI code generation
#### Constraints
- The workflow differs across study arms in instruction only, not in tasks or AI tool access

### Target Learners
- undergraduate computer science students

### Learning Goals
- specifying acceptance criteria and architectural constraints prior to code generation; monitoring AI outputs for specification compliance

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Mark Dranias and Adam Whitley. (2025). Human-in-the-Loop Control of Objective Drift in LLM-Assisted Computer Science Education.
