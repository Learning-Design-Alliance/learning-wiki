---
type: design
id: four-method-simulation-taxonomy
title: Four-method taxonomy of quantum circuit simulation with contrasting complexity and expressiveness tradeoffs
description: "The practical organizes classical quantum circuit simulation around four state-representation methods, each with stated tradeoffs: state vectors need memory growing exponential O(2^n) in qubit count n and illustrate n..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: florian-krötz-2025
    resource: "https://arxiv.org/abs/2511.17218"
    title: "Florian Krötz, Xiao-Ting Michelle To, Korbinian Staudacher, Dieter Kranzlmüller. (2025). Teaching quantum computing to computer science students: Review of a hands-on quantum circuit simulation practical. arXiv preprint. https://arxiv.org/abs/2511.17218"
    author: Florian Krötz, Xiao-Ting Michelle To, Korbinian Staudacher, Dieter Kranzlmüller
---

# Four-method taxonomy of quantum circuit simulation with contrasting complexity and expressiveness tradeoffs

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The practical organizes classical quantum circuit simulation around four state-representation methods, each with stated tradeoffs: state vectors need memory growing exponential O(2^n) in qubit count n and illustrate non-locality; density matrices need O(2^2n), quadratic more memory than a state vector, but allow noise modeling; the stabilizer formalism represents only stabilizer states but does so efficiently with O(n^2) via tableaux and Clifford gates; matrix product states have space complexity depending on the degree of entanglement. A central learning goal is "the understanding how a quantum state |ψ⟩ is represented, what are strength and weaknesses of this representation and how it is modified when applying a unitary U".

## Design Implications

### Context
#### Requirements
- Students first need the recap worksheet covering unitary operations, tensor products, gates in Dirac notation and as matrices, and density matrices; the MPS sheet requires introducing tensors, which most CS curricula omit.
#### Constraints
- The stabilizer formalism can represent only stabilizer states and applies only Clifford gates (H, S, CNOT); the density matrix sheet considers only pure states.

### Target Learners
- graduate computer science students

### Learning Goals
- informed choice of simulator for a use case
- intuition for the non-local, non-separable nature of quantum computing
- understanding of entanglement and noise

### Claims
- Qcp Circuit Representation [+M]
- [Method Selection Shifted 2023 2024](../claims/method-selection-shifted-2023-2024.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Florian Krötz, Xiao-Ting Michelle To, Korbinian Staudacher, Dieter Kranzlmüller. (2025). Teaching quantum computing to computer science students: Review of a hands-on quantum circuit simulation practical. arXiv preprint. https://arxiv.org/abs/2511.17218
