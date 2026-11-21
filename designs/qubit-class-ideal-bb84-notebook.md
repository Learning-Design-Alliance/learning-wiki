---
type: design
id: qubit-class-ideal-bb84-notebook
title: Qubit class Jupyter notebook for ideal BB84 implementation by novices
description: A Python Jupyter notebook in which students implement the ideal BB84 QKD protocol using a Qubit class with prepare and measure methods for polarization states.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: brian-r-la-cour-2025
    resource: "https://arxiv.org/abs/2507.13389"
    title: "Brian R. La Cour, Noah A. Davis. (2025). An Adversarial Quantum Key Distribution Project. arXiv. https://arxiv.org/abs/2507.13389"
    author: Brian R. La Cour, Noah A. Davis
---

# Qubit class Jupyter notebook for ideal BB84 implementation by novices

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A Python Jupyter notebook in which students implement the ideal BB84 QKD protocol using a Qubit class with prepare and measure methods for polarization states. Cells cover Alice, Eve, Bob, and key sifting; strings represent keys and bases. As the authors write, "Students can see the code but can only interact with the qubits using the prescribed methods, thereby providing a crude representation of their elusive quantum nature." Only random and numpy are required.

## Design Implications

### Context
#### Requirements
- Students interact with qubits only through prescribed methods so the quantum nature is preserved
#### Constraints
- The representation is deliberately simplified; photons are illustrated as pulses of classical light, which the authors note is incorrect

### Target Learners
- high school students
- first-year undergraduates with minimal programming experience

### Learning Goals
- understand the BB84 quantum key distribution protocol
- learn basic Python programming including loops and conditionals

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Brian R. La Cour, Noah A. Davis. (2025). An Adversarial Quantum Key Distribution Project. arXiv. https://arxiv.org/abs/2507.13389
