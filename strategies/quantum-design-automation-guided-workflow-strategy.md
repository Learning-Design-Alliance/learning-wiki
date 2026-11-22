---
type: strategy
id: quantum-design-automation-guided-workflow-strategy
title: "Teach quantum design automation through a guided workflow mirroring an engineering lifecycle: design, estimate, optimize, verify, then export"
description: "The article organizes instruction around a single running example circuit that students carry through successive design-automation stages: building the circuit in Scratch with color-coded quantum versus classical bloc..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: damian-rovara-2026
    resource: "https://arxiv.org/abs/2608.18206"
    title: "Damian Rovara, Robert Wille. (2026). Teaching Quantum Design Automation with Block-Based Programming. https://arxiv.org/abs/2608.18206"
    author: Damian Rovara, Robert Wille
---

# Teach quantum design automation through a guided workflow mirroring an engineering lifecycle: design, estimate, optimize, verify, then export

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article organizes instruction around a single running example circuit that students carry through successive design-automation stages: building the circuit in Scratch with color-coded quantum versus classical blocks, switching the run block from simulation to resource estimation, optimizing and routing with SWAP gates for a coupling map, verifying via inverse-circuit equivalence checks, and finally exporting to MLIR. Per the authors, "This workflow mirrors a realistic engineering lifecycle: moving from initial circuit design and resource estimation to optimization and verification." Integrated analysis removes the need for disjoint external tool export during learning.

## Design Implications

### Context
#### Requirements
- An environment where resource estimation and simulation are directly integrated so learners can modify circuits and immediately re-estimate costs
- Students should have basic prior quantum computing knowledge such as qubits and gate effects
#### Constraints
- The competence questionnaire covered only four questions selected to cover the most important exercise aspects
- Results may not generalize beyond post-graduate computer science and electrical engineering students

### Target Learners
- novices to quantum design automation with computer science backgrounds

### Target Learning Goals
- translating circuit diagrams into programs
- evaluating resource costs
- circuit optimization and routing
- equivalence-checking compiled circuits

### Affordances
- Scratch Quantum Framework

## Claims

- [Learning outcomes and usability did not differ between supervised in-person and remote take-home study modalities](../claims/scratch-quantum-modalities-no-difference.md) [+W]
- [Concepts learned with the framework were retained after one week, with pass rates equal or better except a 4.2% drop on compilation](../claims/scratch-quantum-one-week-retention.md) [+W]
- [Study participants had little prior experience with Scratch, resource estimation, or circuit verification](../claims/scratch-quantum-participants-limited-prior-experience.md) [~W]
- [Post-graduate students completing guided exercises in the Scratch-based quantum framework scored a median 3.5 of 4 on design-automation competence questions](../claims/scratch-quantum-study-competence-median-3-5.md) [+W]
- [Participants rated the block-based quantum design automation framework highly usable, with a median usability score of 4.3](../claims/scratch-quantum-study-usability-median-4-3.md) [+W]

## Related Strategies

- [Resource estimation assignments comparing the resources of alternative quantum algorithm implementations](resource-estimation-assignments-strategy.md)
- [Introduce quantum software engineering and the hybrid classical-quantum SDLC alongside programming frameworks](quantum-sdlc-curriculum-component.md)

## Examples
-

## Key Sources
- Damian Rovara, Robert Wille. (2026). Teaching Quantum Design Automation with Block-Based Programming. https://arxiv.org/abs/2608.18206
