---
type: design
id: qtris-controlled-x-entanglement-extension
title: Entanglement extension of QTris via the Controlled-X card and triangular-tile Bell states
description: "Entanglement is introduced into QTris by the Controlled-X card (C X), \"analogous to the CNOT gate of quantum computers\"; it is the only card acting on two cells at once, with control and target roles."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: amabile-2026
    resource: "https://arxiv.org/abs/2608.09430"
    title: "Amabile, A., Bondani, M., De Simone, I., Nazzaro, M., Viscardi, M., Hamma, A. (2026). QTris: a pedagogical board game to teach Quantum Mechanics. https://arxiv.org/abs/2608.09430"
    author: Amabile, A., Bondani, M., De Simone, I., Nazzaro, M., Viscardi, M., Hamma, A
---

# Entanglement extension of QTris via the Controlled-X card and triangular-tile Bell states

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Entanglement is introduced into QTris by the Controlled-X card (C X), "analogous to the CNOT gate of quantum computers"; it is the only card acting on two cells at once, with control and target roles. Applying C X to certain control-target combinations generates four new two-cell entangled states represented by couples of signed triangular tiles, characterized by global properties of Alignment and Sign, whose color is completely unpredictable. Measurement rules give each possible result with probability 1/2, and X and Z operations change Alignment and Sign respectively.

## Design Implications

### Context
#### Requirements
- Rules for operations and color measurements on triangular states must be defined; the player must choose which cell acts as control when disentangling
#### Constraints
- A further extension introducing a third basis of Y eigenstates is deferred to a future work

### Target Learners
- high-school students

### Learning Goals
- understanding entanglement and its distinction from classical correlations

### Claims

- [Nearly all interviewed students correctly determined that two adjacent same-orientation CNOT gates cancel in the three-CNOT circuit](../claims/all-but-one-correct-three-cnot-cancellation.md) [+W]
- [Twelve students invoked the idea that CNOT does not change the control qubit in a superposition context, leading to incorrect conclusions that some maintained even against measurement correlation](../claims/resource-c-overrides-conflicting-information.md) [+W]

## Related Designs

- [Four-level structural analogy between QTris and qubit Quantum Mechanics: observables, states, unitary operations, measurement](qtris-qm-four-level-structural-analogy.md)
- [Translating quantum thought experiments into quantum circuits as an explanatory and educational framework](quantum-circuits-thought-experiment-framework.md)

## Examples
-

## Key Sources
- Amabile, A., Bondani, M., De Simone, I., Nazzaro, M., Viscardi, M., Hamma, A. (2026). QTris: a pedagogical board game to teach Quantum Mechanics. https://arxiv.org/abs/2608.09430. [doi:10.48550/arxiv.2608.09430](https://doi.org/10.48550/arxiv.2608.09430)
