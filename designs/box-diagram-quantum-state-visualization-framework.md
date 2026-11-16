---
type: design
id: box-diagram-quantum-state-visualization-framework
title: Box-diagram representation of quantum states and measurements as a visualization framework
description: "The article introduces a pictorial framework in which states of multiple quantum coins are drawn as grids of boxes whose entries indicate \"how much\" is in that part of the state, and measurements act by preserving row..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: scott-m-cohen-2008
    resource: "https://arxiv.org/abs/0704.0051"
    title: "Scott M. Cohen. (2008). Visualizing Teleportation. https://arxiv.org/abs/0704.0051"
    author: Scott M. Cohen
---

# Box-diagram representation of quantum states and measurements as a visualization framework

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article introduces a pictorial framework in which states of multiple quantum coins are drawn as grids of boxes whose entries indicate "how much" is in that part of the state, and measurements act by preserving rows (⟨H|H⟩ = 1) or annihilating rows (⟨T|H⟩ = 0). The author writes that "The simple diagrams we will use to depict states of multiple quantum coins, held by two diﬀerent parties, are familiar to many researchers working in quantum information." The framework is then applied to walk through teleportation step by step.

## Design Implications

### Context
#### Requirements
- The reader accepts only that certain bracket expressions equal 1 or 0, per the four basic statements ⟨H|H⟩ = 1, ⟨T|T⟩ = 1, ⟨T|H⟩ = 0, ⟨H|T⟩ = 0.
#### Constraints
- Probabilities versus probability amplitudes are deliberately conflated for lay audiences; diagrams handle at most three coins here, with three parties handled by placing two systems on one vertical dimension.

### Target Learners
- non-scientists without much skill in mathematics
- physicists explaining quantum concepts to the public

### Learning Goals
- understanding the probabilistic nature of quantum measurement
- understanding how quantum teleportation works

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Scott M. Cohen. (2008). Visualizing Teleportation. https://arxiv.org/abs/0704.0051
