---
type: design
id: quantum-circuits-thought-experiment-framework
title: Translating quantum thought experiments into quantum circuits as an explanatory and educational framework
description: The article proposes representing quantum thought experiments as quantum circuits built from Hadamard and CNOT gates, with observers, detectors and environments modelled as qubits.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: maria-violaris-2023
    resource: "https://arxiv.org/abs/2312.07840"
    title: "Maria Violaris. (2023). A physics lab inside your head: Quantum thought experiments as an educational tool. https://arxiv.org/abs/2312.07840"
    author: Maria Violaris
---

# Translating quantum thought experiments into quantum circuits as an explanatory and educational framework

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article proposes representing quantum thought experiments as quantum circuits built from Hadamard and CNOT gates, with observers, detectors and environments modelled as qubits. The author states this "provides new insights into the fundamental concepts behind each thought experiment; novel, interesting activities to implement on near-term quantum devices; and a compelling storytelling-based entry point" for newcomers. Worked examples in Qiskit demonstrate the approach across six thought experiments.

## Design Implications

### Context
#### Requirements
- Learners or instructors need familiarity with quantum circuit formalism (qubits, Hadamard and CNOT gates); the article notes its tutorial content "assumes basic knowledge of quantum circuits, which needs to be introduced separately in a workshop for new quantum learners".
#### Constraints
- The validity of universal quantum theory remains a topic of debate, per the article's conclusion.

### Target Learners
- beginners new to quantum information
- school students as young as 11
- university quantum learners

### Learning Goals
- understanding superposition, entanglement, measurement and decoherence
- resolving apparent quantum paradoxes
- coding quantum circuits

### Claims
- Wigner Friend Observers As Quantum Systems Resolves Paradox [+M]
- Double Slit Entanglement Decoherence No Classical Measurement [+M]

## Related Designs

- [Entanglement extension of QTris via the Controlled-X card and triangular-tile Bell states](qtris-controlled-x-entanglement-extension.md)

## Examples
-

## Key Sources
- Maria Violaris. (2023). A physics lab inside your head: Quantum thought experiments as an educational tool. https://arxiv.org/abs/2312.07840
