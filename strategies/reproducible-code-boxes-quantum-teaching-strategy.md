---
type: strategy
id: reproducible-code-boxes-quantum-teaching-strategy
title: Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware
description: The article structures its entire treatment as a sequence of numbered code boxes — importing packages, registering qubits, initializing states, applying gates, measuring, and submitting jobs to IBM QE — so that reader...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: gleydson-fernandes-de-jesus-2021
    resource: "https://arxiv.org/abs/2101.11388"
    title: "Gleydson Fernandes de Jesus, Maria Helo´ısa Fraga da Silva, Teonas Gonc¸alves Dourado Netto, Lucas Queiroz Galv˜ao, Frankle Gabriel de Oliveira Souza, and Clebson Cruz. (2021). Quantum Computing: an undergraduate approach using Qiskit. https://arxiv.org/abs/2101.11388"
    author: Gleydson Fernandes de Jesus, Maria Helo´ısa Fraga da Silva, Teonas Gonc¸alves Dourado Netto, Lucas Queiroz Galv˜ao, Frankle Gabriel de Oliveira Souza, and Clebson Cruz
---

# Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article structures its entire treatment as a sequence of numbered code boxes — importing packages, registering qubits, initializing states, applying gates, measuring, and submitting jobs to IBM QE — so that readers can reproduce every program on any common laptop or desktop. This lets students progress from simulating circuits locally to executing them on real quantum processors through remote access, building understanding of qubits, gates, measurement and entanglement by doing.

## Design Implications

### Context
#### Requirements
- An Anaconda/Jupyter Notebook environment with Qiskit installed, and a free IBM Q Experience account with API token for real-hardware runs
#### Constraints
- The article's applications were all executed on the same 5-qubit ibmq_valencia processor, and the real processor allowed at most 8192 shots

### Target Learners
- undergraduate students with basic quantum mechanics knowledge and little or no scientific programming experience

### Target Learning Goals
- implementing simple quantum circuits and well-known quantum algorithms

## Claims

- [Qiskit-based exercises agree with theoretical predictions and support introducing quantum computing to undergraduates](../claims/qiskit-agrees-with-theory-classroom-effectiveness.md) [+W]
- [Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data](../claims/hardware-execution-did-not-eliminate-llm-assistance.md) [~W]

## Related Strategies

- [Teach multiple quantum algorithms on the same QUBO task so students learn to select a proper algorithm for a given computing task](same-qubo-multiple-algorithms-strategy.md)
- [Use Python quantum code libraries such as Qiskit and Netsquid to deliver simulation-based exercises and support autonomous learning](python-quantum-libraries-simulation-exercises.md)
- [Quantum hardware exploration assignments balancing authentic device access with simulator substitutes](quantum-hardware-exploration-assignments-strategy.md)
- [Use real-hardware experiment results that deviate from theory to motivate a discussion of quantum error correction](real-hardware-error-observation-strategy.md)
- [Use cloud-accessible quantum computing platforms so students run circuits on real quantum hardware](cloud-quantum-platforms-school-use.md)
- [Teach Ocean SDK via account setup, Leap/SAPI authentication, and job submission to D-Wave QPUs](ocean-sdk-dwave-teaching-sequence.md)
- [Sequence Qiskit instruction from environment setup through real-QPU job submission with multi-platform examples](qiskit-qpu-job-submission-sequence.md)
- [Design quantum courses around cloud-based platforms and simulators where hardware access is limited](cloud-based-quantum-platforms-course-design.md)
- [Teach quantum computing through applied coding of Grover's search with fully provided, replicable code](applied-grover-coding-teaching-strategy.md)
- [Measure arbitrary spin directions on quantum hardware by applying rotation gates that map the desired eigenvectors onto the computational basis](rotation-gate-basis-change-measurement-strategy.md)

## Examples
-

## Key Sources
- Gleydson Fernandes de Jesus, Maria Helo´ısa Fraga da Silva, Teonas Gonc¸alves Dourado Netto, Lucas Queiroz Galv˜ao, Frankle Gabriel de Oliveira Souza, and Clebson Cruz. (2021). Quantum Computing: an undergraduate approach using Qiskit. https://arxiv.org/abs/2101.11388
