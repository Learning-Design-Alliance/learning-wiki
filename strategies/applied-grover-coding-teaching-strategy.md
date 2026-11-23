---
type: strategy
id: applied-grover-coding-teaching-strategy
title: "Teach quantum computing through applied coding of Grover's search with fully provided, replicable code"
description: "The article recommends introducing quantum computing via applied courses in which students implement Grover's search algorithm themselves in AQASM, because the search problem is tangible to a wide audience and the qua..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: maria-heloısa-fraga-da-silva-2023
    resource: "https://arxiv.org/abs/2304.06492"
    title: "Maria Helo´ısa Fraga da Silva, Gleydson Fernandes de Jesus, and Clebson Cruz. (2023). Eﬀect of pure dephasing quantum noise in the quantum search algorithm: an undergraduate approach using Atos Quantum Assembly. arXiv preprint. https://arxiv.org/abs/2304.06492"
    author: Maria Helo´ısa Fraga da Silva, Gleydson Fernandes de Jesus, and Clebson Cruz
---

# Teach quantum computing through applied coding of Grover's search with fully provided, replicable code

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article recommends introducing quantum computing via applied courses in which students implement Grover's search algorithm themselves in AQASM, because the search problem is tangible to a wide audience and the quadratic speed-up represents a clear advantage over the classical counterpart. The authors provide the programming code throughout the text "so that readers, even those with little scientiﬁc computing experience, can replicate them", and add an interactive user input step where the student types the item to search for, applying the corresponding oracle.

## Design Implications

### Context
#### Requirements
- A quantum software development environment such as myQLM with a Python interface
- Choice of an algorithm with a clear advantage over its classical counterpart, such as Grover's search
#### Constraints
- The current bibliography in quantum computing presents high technicality that is a common obstacle due to mathematical and physical prerequisites; early student preparation is beneficial because the laws of quantum mechanics are counter-intuitive

### Target Learners
- undergraduate students
- high school students

### Target Learning Goals
- quantum programming
- understanding quantum search and the quadratic speed-up
- active participation in building knowledge

## Claims

- [Qiskit-based exercises agree with theoretical predictions and support introducing quantum computing to undergraduates](../claims/qiskit-agrees-with-theory-classroom-effectiveness.md) [+W]

## Related Strategies

- [Teach multiple quantum algorithms on the same QUBO task so students learn to select a proper algorithm for a given computing task](same-qubo-multiple-algorithms-strategy.md)
- [Team projects in which students discover quantum concepts (teleportation presentation and engaging Grover-algorithm video)](team-discovery-projects-teleportation-grover.md)
- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)

## Examples
-

## Key Sources
- Maria Helo´ısa Fraga da Silva, Gleydson Fernandes de Jesus, and Clebson Cruz. (2023). Eﬀect of pure dephasing quantum noise in the quantum search algorithm: an undergraduate approach using Atos Quantum Assembly. arXiv preprint. https://arxiv.org/abs/2304.06492
