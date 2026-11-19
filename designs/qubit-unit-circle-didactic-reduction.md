---
type: design
id: qubit-unit-circle-didactic-reduction
title: Define the qubit as a real vector on the unit circle rather than via the Bloch sphere or complex Hilbert space
description: "The unit's central didactic reduction defines a qubit as a two-component real vector with α²+β²=1 on the unit circle, with |0⟩ and |1⟩ corresponding to the classical bit states."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: andreas-j-c-woitzik-2020
    resource: "https://arxiv.org/abs/2011.01029"
    title: "Andreas J. C. Woitzik. (2020). Quanteninformationsverarbeitung in der Gymnasialen Oberstufe. https://arxiv.org/abs/2011.01029"
    author: Andreas J. C. Woitzik
---

# Define the qubit as a real vector on the unit circle rather than via the Bloch sphere or complex Hilbert space

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The unit's central didactic reduction defines a qubit as a two-component real vector with α²+β²=1 on the unit circle, with |0⟩ and |1⟩ corresponding to the classical bit states. The article motivates this because "Für Schüler ist es allerdings verwirrend, dass orthogonale Zustände auf der Kugel Antipoden bilden, also linear abhängig erscheinen," and because the circle suffices for the central phenomena.

## Design Implications

### Context
#### Requirements
- Only real vectors with α²+β²=1 and the two basis states are introduced; no complex Hilbert-space formalism or global-phase discussion is needed.
#### Constraints
- The article limits the reduction to the central phenomena of quantum information processing; the Bloch sphere, the standard visualization in physics, is rejected for school use because orthogonal states appear as antipodes on it.

### Target Learners
- upper-secondary informatics students

### Learning Goals
- representing qubits geometrically and naming the states corresponding to classical bits

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Andreas J. C. Woitzik. (2020). Quanteninformationsverarbeitung in der Gymnasialen Oberstufe. https://arxiv.org/abs/2011.01029
