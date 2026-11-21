---
type: design
id: qiskit-hhl-ct-reconstruction-element
title: Qiskit-based HHL image-reconstruction implementation with released GitHub code
description: A small-scale, end-to-end implementation of the HHL algorithm for CT image reconstruction built in the IBM Qiskit environment in Python on a noiseless AerSimulator backend.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: nischal-binod-gautam-2025
    resource: "https://arxiv.org/abs/2508.21321"
    title: "Nischal Binod Gautam, Keith Evan Schubert, and Enrique P. Blair. (2025). Project-Based Learning in Introductory Quantum Computing Courses: A Case Study on Quantum Algorithms for Medical Imaging. https://arxiv.org/abs/2508.21321"
    author: Nischal Binod Gautam, Keith Evan Schubert, and Enrique P. Blair
---

# Qiskit-based HHL image-reconstruction implementation with released GitHub code

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A small-scale, end-to-end implementation of the HHL algorithm for CT image reconstruction built in the IBM Qiskit environment in Python on a noiseless AerSimulator backend. The article reports that "The problem was run on the IBM Qiskit environment in Python using a noiseless AerSimulator backend", reconstructing a 2x2 phantom via normal equations (ATA + I)x = ATb, and cites a released GitHub repository of the HHL Qiskit code as a project artifact.

## Design Implications

### Context
#### Requirements
- Solving the normal equations (ATA + I)x = ATb because A is neither Hermitian nor well-conditioned directly
#### Constraints
- The toy 2x2 study sidestepped output extraction by using a state-vector simulator granting direct access to the full wavefunction, which the article calls infeasible on current quantum hardware

### Target Learners
- students in introductory quantum computing courses

### Learning Goals
- gaining practical experience implementing quantum algorithms
- benchmarking quantum against classical solvers

### Claims
- Hhl Art 2X2 Phantom Reconstruction Accuracy [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Nischal Binod Gautam, Keith Evan Schubert, and Enrique P. Blair. (2025). Project-Based Learning in Introductory Quantum Computing Courses: A Case Study on Quantum Algorithms for Medical Imaging. https://arxiv.org/abs/2508.21321
