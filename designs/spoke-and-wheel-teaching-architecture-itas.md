---
type: design
id: spoke-and-wheel-teaching-architecture-itas
title: "Spoke-and-Wheel teaching architecture: three quantum-specialist agents in parallel coordinated by a Synthesizer"
description: "ITAS's teaching architecture decomposes tutoring by task: three specialist agents (Video, Guidance, Code) analyze each student question in parallel, each reasoning only within its designated scope, and a Synthesizer A..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: iizalaarab-elhaimeur-and-nikos-chrisochoides-2026
    resource: "https://arxiv.org/abs/2604.24807"
    title: "Iizalaarab Elhaimeur and Nikos Chrisochoides. (2026). From Prototype to Classroom: An Intelligent Tutoring System for Quantum Education. https://arxiv.org/abs/2604.24807"
    author: Iizalaarab Elhaimeur and Nikos Chrisochoides
---

# Spoke-and-Wheel teaching architecture: three quantum-specialist agents in parallel coordinated by a Synthesizer

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
ITAS's teaching architecture decomposes tutoring by task: three specialist agents (Video, Guidance, Code) analyze each student question in parallel, each reasoning only within its designated scope, and a Synthesizer Agent integrates their outputs using a priority hierarchy with code errors first, then conceptual gaps, then video references. The design responds to the prototype's task-boundary hallucinations, which the authors attribute to cognitive overload of a single overloaded agent. Specialization is said to reduce hallucination via cognitive load reduction, task interference elimination, and synthesis filtering. The three-agent count "emerged empirically; two agents conflated code and concepts, while four added coordination overhead without reliability improvement."

## Design Implications

### Context
#### Requirements
- Each agent must carry quantum-specific domain knowledge, e.g. a timestamp-indexed concept map for the Video Agent and a hand-curated Qiskit error catalog for the Code Agent
#### Constraints
- A controlled, blinded comparison against the prototype on the same input set remains future work

### Target Learners
- graduate quantum information science students

### Learning Goals
- conceptual understanding of quantum information science
- Qiskit implementation skills
- video lecture comprehension

### Claims
- [Itas Specialization No Task Boundary Failures](../claims/itas-specialization-no-task-boundary-failures.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Iizalaarab Elhaimeur and Nikos Chrisochoides. (2026). From Prototype to Classroom: An Intelligent Tutoring System for Quantum Education. https://arxiv.org/abs/2604.24807
