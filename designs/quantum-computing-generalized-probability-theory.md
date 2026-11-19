---
type: design
id: quantum-computing-generalized-probability-theory
title: "Computer science-oriented approach: quantum computing as a generalization of probabilistic computing taught through linear algebra"
description: "The framework presents quantum computing \"as a generalization of probabilistic and classical computing\", abstracting physical concepts through linear algebra so that a quantum state is a vector and quantum gates are u..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: özlem-salehi-2021
    resource: "https://arxiv.org/abs/2010.13552"
    title: "Özlem Salehi, Zeki Seskir, and Ilknur Tepe. (2021). A Computer Science-Oriented Approach to Introduce Quantum Computing to a New Audience. https://arxiv.org/abs/2010.13552"
    author: Özlem Salehi, Zeki Seskir, and Ilknur Tepe
---

# Computer science-oriented approach: quantum computing as a generalization of probabilistic computing taught through linear algebra

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The framework presents quantum computing "as a generalization of probabilistic and classical computing", abstracting physical concepts through linear algebra so that a quantum state is a vector and quantum gates are unitary matrices. Superposition is introduced "as a property of a unit vector in a Hilbert space" rather than via photon polarization or electron spin, and the material avoids complex numbers entirely, restricted to real numbers. Measurement is described as projection onto two orthogonal planes. This bypasses physics prerequisites, requiring only linear algebra and basic Python programming.

## Design Implications

### Context
#### Requirements
- basic knowledge in linear algebra and introductory programming experience in Python
#### Constraints
- the material is restricted to real numbers and does not involve complex numbers
- traditional topics such as Deutsch and Bernstein-Vazirani algorithms are purposefully omitted

### Target Learners
- undergraduate and graduate students from STEM-related departments
- high school students with programming and linear algebra prerequisites
- professionals from diverse backgrounds entering the quantum field

### Learning Goals
- basic quantum computing concepts such as qubits, quantum gates, superposition, entanglement
- basic quantum programming skills in Python and Qiskit

### Claims
- [Cs Oriented Quantum Workshop Significant Knowledge Gain](../claims/cs-oriented-quantum-workshop-significant-knowledge-gain.md) [+M]
- [No Background Difference Quantum Gain Scores](../claims/no-background-difference-quantum-gain-scores.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Özlem Salehi, Zeki Seskir, and Ilknur Tepe. (2021). A Computer Science-Oriented Approach to Introduce Quantum Computing to a New Audience. https://arxiv.org/abs/2010.13552
