---
type: strategy
id: task-based-quantum-programming-notebooks
title: Task-based quantum programming notebooks that withhold support libraries so participants compute matrix operations by hand
description: "The strategy organizes learning around notebooks combining explanations with small coding tasks, so that \"task-based programming approach helps participants to learn through experience\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: özlem-salehi-2021
    resource: "https://arxiv.org/abs/2010.13552"
    title: "Özlem Salehi, Zeki Seskir, and Ilknur Tepe. (2021). A Computer Science-Oriented Approach to Introduce Quantum Computing to a New Audience. https://arxiv.org/abs/2010.13552"
    author: Özlem Salehi, Zeki Seskir, and Ilknur Tepe
---

# Task-based quantum programming notebooks that withhold support libraries so participants compute matrix operations by hand

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The strategy organizes learning around notebooks combining explanations with small coding tasks, so that "task-based programming approach helps participants to learn through experience". Deliberately, "Any support library (such as Numpy) is not used for linear algebraic operations as a pedagogical strategy, scaffolding participants to perform matrix-vector multiplications by hand to understand the evolution of states through linear operators". Conceptual tasks include paper-based mathematical derivations, and the Qiskit library is introduced gradually as new concepts appear.

## Design Implications

### Context
#### Requirements
- reference notebooks containing sufficient information about Qiskit and Python
- instructors and mentors to assist participants in class
#### Constraints
- the material is quite dense for 3 days and participants sometimes struggle to complete the tasks

### Target Learners
- workshop participants with basic Python programming experience
- learners without a physics background

### Target Learning Goals
- quantum programming skills
- understanding of state evolution through linear operators

## Claims

- [Participants' basic knowledge of quantum computing concepts rose significantly from pre-test to post-test after a computer science-oriented quantum computing workshop, in one uncontrolled pre-post study](../claims/cs-oriented-quantum-workshop-significant-knowledge-gain.md) [+W]
- [Participants report high satisfaction with the workshop, with all statement means above 4.5 except workload adequacy](../claims/quantum-workshop-high-satisfaction-ratings.md) [+W]

## Related Strategies

- [Use a simple computational exercise that can be 'tweaked' with a few lines of code to solve a different, equally intensive problem almost for free](notebook-tweak-almost-for-free-strategy.md)
- [Use Python quantum code libraries such as Qiskit and Netsquid to deliver simulation-based exercises and support autonomous learning](python-quantum-libraries-simulation-exercises.md)

## Examples
-

## Key Sources
- Özlem Salehi, Zeki Seskir, and Ilknur Tepe. (2021). A Computer Science-Oriented Approach to Introduce Quantum Computing to a New Audience. https://arxiv.org/abs/2010.13552
