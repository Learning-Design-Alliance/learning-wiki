---
type: strategy
id: ocean-sdk-dwave-teaching-sequence
title: Teach Ocean SDK via account setup, Leap/SAPI authentication, and job submission to D-Wave QPUs
description: "The article proposes a sequence for teaching Ocean SDK to execute programs on D-Wave QPUs: set up the programming environment (Ocean Tools are \"essential for running any program on the D-Wave Quantum Processing Unit\")..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: majid-haghparast-2024
    resource: "https://arxiv.org/abs/2501.01446"
    title: "Majid Haghparast, Enrique Moguel, Jose Garcia-Alonso, Tommi Mikkonen, Juan Manuel Murillo. (2024). Innovative Approaches to Teaching Quantum Computer Programming and Quantum Software Engineering. https://arxiv.org/abs/2501.01446"
    author: Majid Haghparast, Enrique Moguel, Jose Garcia-Alonso, Tommi Mikkonen, Juan Manuel Murillo
---

# Teach Ocean SDK via account setup, Leap/SAPI authentication, and job submission to D-Wave QPUs

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes a sequence for teaching Ocean SDK to execute programs on D-Wave QPUs: set up the programming environment (Ocean Tools are "essential for running any program on the D-Wave Quantum Processing Unit"), create a D-Wave account, use Ocean Tools with Leap authentication and a Solver API (SAPI) token, submit jobs to real D-Wave devices, optionally connect via Google Colab for a cloud-based approach, and understand the D-Wave workflow of formulating problems as objective (cost) functions and finding solutions through sampling. Students then work through examples across research topics by sending jobs to the QPU and analyzing responses.

## Design Implications

### Context
#### Requirements
- A D-Wave website account and a SAPI token from the Leap account to authenticate and submit problems to Leap solvers
#### Constraints
- The workflow is specific to D-Wave quantum annealers and its Leap platform; problem formulation follows the annealing style of objective/cost functions and sampling rather than circuit-model programming

### Target Learners
- M.Sc./Ph.D. students learning quantum annealing programming

### Target Learning Goals
- Running programs on D-Wave QPUs
- Formulating problems as cost functions and finding solutions through sampling

## Related Strategies

- [Sequence Qiskit instruction from environment setup through real-QPU job submission with multi-platform examples](qiskit-qpu-job-submission-sequence.md)
- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)
- [Quantum hardware exploration assignments balancing authentic device access with simulator substitutes](quantum-hardware-exploration-assignments-strategy.md)
- [Teach PennyLane through a Docker-based environment and the Xanadu Codebook with in-class codercises](pennylane-xanadu-codebook-strategy.md)
- [Introduce quantum software engineering and the hybrid classical-quantum SDLC alongside programming frameworks](quantum-sdlc-curriculum-component.md)

## Examples
-

## Key Sources
- Majid Haghparast, Enrique Moguel, Jose Garcia-Alonso, Tommi Mikkonen, Juan Manuel Murillo. (2024). Innovative Approaches to Teaching Quantum Computer Programming and Quantum Software Engineering. https://arxiv.org/abs/2501.01446
