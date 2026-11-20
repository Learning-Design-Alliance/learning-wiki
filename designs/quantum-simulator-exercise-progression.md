---
type: design
id: quantum-simulator-exercise-progression
title: "Three-tier exercise progression: probabilistic gates, equivalent-circuit simplification, and unknown-gate identification"
description: The article demonstrates three exercise types used in its online courses, forming a progression from basic gate behavior to circuit reasoning.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: juha-reinikainen-2024
    resource: "https://arxiv.org/abs/2404.10328"
    title: "Juha Reinikainen, Vlad Stirbu, Teiko Heinosaari, Vesa Lappalainen, Tommi Mikkonen. (2024). Quantum Computing for All: Online Courses Built Around Interactive Visual Quantum Circuit Simulator. https://arxiv.org/abs/2404.10328"
    author: Juha Reinikainen, Vlad Stirbu, Teiko Heinosaari, Vesa Lappalainen, Tommi Mikkonen
---

# Three-tier exercise progression: probabilistic gates, equivalent-circuit simplification, and unknown-gate identification

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article demonstrates three exercise types used in its online courses, forming a progression from basic gate behavior to circuit reasoning. First, students explore that Hadamard and square-root-X gates "lead to random outcomes, but two similar gates to deterministic outcomes". Second, students find equivalent circuits with fewer gates, with automatic evaluation recognizing all correct answers from input-output behavior. Third, students identify an unknown gate by composing it with others, which the authors describe as almost like entertaining puzzles that force review of previously learned material.

## Design Implications

### Context
#### Requirements
- Requires the simulator's automatic answer checking, which compares a model circuit to the student's circuit over all 2^nQubits input combinations, and the ability for instructors to create arbitrary labeled gates
#### Constraints
- A typical exercise does not have a unique answer, so evaluation must rely on input-output behavior rather than exact circuit match

### Target Learners
- Novice quantum computing students with no prior quantum physics knowledge
- Students from diverse study tracks

### Learning Goals
- Understanding the probabilistic nature of quantum gates
- Recognizing circuits with equivalent performance
- Reviewing previously learned gate material

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Juha Reinikainen, Vlad Stirbu, Teiko Heinosaari, Vesa Lappalainen, Tommi Mikkonen. (2024). Quantum Computing for All: Online Courses Built Around Interactive Visual Quantum Circuit Simulator. https://arxiv.org/abs/2404.10328
