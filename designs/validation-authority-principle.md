---
type: design
id: validation-authority-principle
title: "Principle of validation authority: delegation is safe exactly where the delegator can validate outputs"
description: "The article introduces the principle of validation authority, grounded in a bespoke-versus-socially-validated distinction: a library routine is opaque but socially validated through published algorithms, testing, and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: larry-engelhardt-2026
    resource: "https://arxiv.org/abs/2607.15518"
    title: "Larry Engelhardt. (2026). A Tool-Invariant Framework for Teaching and Assessing Computational Methods in the Age of Agentic AI. https://arxiv.org/abs/2607.15518"
    author: Larry Engelhardt
---

# Principle of validation authority: delegation is safe exactly where the delegator can validate outputs

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article introduces the principle of validation authority, grounded in a bespoke-versus-socially-validated distinction: a library routine is opaque but socially validated through published algorithms, testing, and millions of users, while an AI-generated simulation is opaque and bespoke, "an artifact with a population of one, produced by a stochastic process whose competence boundary is jagged and invisible." The author's generalization is that "delegation is safe exactly where the delegator retains the ability to validate the outputs," which redefines a computational physics course as training validation authority over physical simulations.

## Design Implications

### Context
#### Requirements
- Courses adopting this framing must train disciplinary verification checks the user knows to demand, since a physics simulation's correctness is not observable in use.
#### Constraints
- The principle marks a boundary: anyone can delegate in domains like personal productivity apps where correctness is observable in use, but not where correctness must be established by disciplinary checks.

### Target Learners
- undergraduate physics students directing AI agents

### Learning Goals
- judgment about when delegation to computational tools is safe and how to validate outputs

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Larry Engelhardt. (2026). A Tool-Invariant Framework for Teaching and Assessing Computational Methods in the Age of Agentic AI. https://arxiv.org/abs/2607.15518
