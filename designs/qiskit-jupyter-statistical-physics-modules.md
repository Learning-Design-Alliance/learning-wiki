---
type: design
id: qiskit-jupyter-statistical-physics-modules
title: Qiskit/Jupyter notebook modules for the quantum random walk and the Ising model
description: Two classroom-ready modules implemented in Qiskit within Jupyter notebooks, released as a GitHub repository, covering a quantum random walk (Hadamard coin, shift operator, binary position register, ancilla register fo...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: zihan-li-2025
    resource: "https://arxiv.org/abs/2511.03696"
    title: "Zihan Li, Dan A. Mazilu, Irina Mazilu. (2025). Introducing Quantum Computing into Statistical Physics: Random Walks and the Ising Model with Qiskit. https://arxiv.org/abs/2511.03696"
    author: Zihan Li, Dan A. Mazilu, Irina Mazilu
---

# Qiskit/Jupyter notebook modules for the quantum random walk and the Ising model

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Two classroom-ready modules implemented in Qiskit within Jupyter notebooks, released as a GitHub repository, covering a quantum random walk (Hadamard coin, shift operator, binary position register, ancilla register for conditional updates) and a quantum-circuit Ising model (1D and layered 2D). The notebooks are described as "essential pedagogical tools for instructors and students alike, and are not merely supplementary appendices". Students run circuits on the Aer simulator, collect outcome statistics, and compare classical and quantum histograms.

## Design Implications

### Context
#### Requirements
- Students need basic knowledge of quantum mechanics and Python programming
#### Constraints
- Full finite-temperature Metropolis dynamics are not implemented; the quantum Ising activity is a zero-temperature spin-flip protocol

### Target Learners
- undergraduate physics students

### Learning Goals
- understanding superposition, interference, and statistical distributions
- hands-on experience with quantum circuits, simulation, and analysis

### Claims
- Quantum Walk Ballistic Double Peaked Distribution [+M]
- Quantum Circuit Zero Temperature Ising Metropolis Like [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zihan Li, Dan A. Mazilu, Irina Mazilu. (2025). Introducing Quantum Computing into Statistical Physics: Random Walks and the Ising Model with Qiskit. https://arxiv.org/abs/2511.03696
