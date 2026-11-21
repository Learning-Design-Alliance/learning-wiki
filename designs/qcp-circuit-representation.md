---
type: design
id: qcp-circuit-representation
title: "QCP: a deliberately simple text-file quantum circuit representation used to force gate-level thinking"
description: "QCP (Quantum Computing Practical) is the circuit representation used in the course: text files whose first line contains the number of qubits and each following line one gate in the format gateName[parameter][controlq..."
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

# QCP: a deliberately simple text-file quantum circuit representation used to force gate-level thinking

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
QCP (Quantum Computing Practical) is the circuit representation used in the course: text files whose first line contains the number of qubits and each following line one gate in the format gateName[parameter][controlqubit(s)] targetqubit. It "dispenses with advanced features such as multiple quantum registers, classical registers, and conditional gates". The authors avoided Qiskit, Cirq, and OpenQASM because existing software abstracts away underlying quantum computing concepts; the representation is kept simple so writing a parser in another language is not difficult. Reference implementations are provided in Python and C.

## Design Implications

### Context
#### Requirements
- A reference implementation in Python and C is provided to students; the simple format is intended to make writing a parser in another language feasible.
#### Constraints
- QCP omits registers, classical registers, and conditional gates, so it cannot express circuits relying on those features.

### Target Learners
- graduate computer science students in the practical

### Learning Goals
- thinking about quantum computing at the gate level
- understanding how a quantum state is represented and modified by unitaries

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Florian Krötz, Xiao-Ting Michelle To, Korbinian Staudacher, Dieter Kranzlmüller. (2025). Teaching quantum computing to computer science students: Review of a hands-on quantum circuit simulation practical. arXiv preprint. https://arxiv.org/abs/2511.17218
