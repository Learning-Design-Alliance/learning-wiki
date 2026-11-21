---
type: strategy
id: qiskit-qpu-job-submission-sequence
title: Sequence Qiskit instruction from environment setup through real-QPU job submission with multi-platform examples
description: "For teaching Qiskit, the article prescribes a sequence: prepare the environment for the Qiskit SDK and simulations with Qiskit backends, then explain how to submit jobs to real quantum devices such as IBM quantum comp..."
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

# Sequence Qiskit instruction from environment setup through real-QPU job submission with multi-platform examples

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For teaching Qiskit, the article prescribes a sequence: prepare the environment for the Qiskit SDK and simulations with Qiskit backends, then explain how to submit jobs to real quantum devices such as IBM quantum computers. Instructors introduce a local QPU (Finland's HELMI quantum computer), cover access and account setup, frameworks and APIs, the job submission process (writing a compatible program, selecting the device, submitting, monitoring, retrieving and interpreting results), and practical examples. This shows students "the variability between different quantum platforms".

## Design Implications

### Context
#### Requirements
- Access to QPUs, including account creation and credentials; the article notes QPUs are usually available free for teaching purposes for universities
#### Constraints
- The strategy is illustrated with Finland's HELMI and IBM quantum computers; instructors are expected to adapt to their own local quantum computer examples

### Target Learners
- M.Sc./Ph.D. students in a quantum computer programming course

### Target Learning Goals
- Submitting and interpreting jobs on real quantum hardware
- Adapting skills to different quantum platforms

## Related Strategies

- [Teach Ocean SDK via account setup, Leap/SAPI authentication, and job submission to D-Wave QPUs](ocean-sdk-dwave-teaching-sequence.md)
- [Teach PennyLane through a Docker-based environment and the Xanadu Codebook with in-class codercises](pennylane-xanadu-codebook-strategy.md)
- [Teach quantum computing through reproducible code boxes that students run locally and on real quantum hardware](reproducible-code-boxes-quantum-teaching-strategy.md)
- [Introduce quantum software engineering and the hybrid classical-quantum SDLC alongside programming frameworks](quantum-sdlc-curriculum-component.md)
- [Design quantum courses around cloud-based platforms and simulators where hardware access is limited](cloud-based-quantum-platforms-course-design.md)
- [Use cloud-accessible quantum computing platforms so students run circuits on real quantum hardware](cloud-quantum-platforms-school-use.md)

## Examples
-

## Key Sources
- Majid Haghparast, Enrique Moguel, Jose Garcia-Alonso, Tommi Mikkonen, Juan Manuel Murillo. (2024). Innovative Approaches to Teaching Quantum Computer Programming and Quantum Software Engineering. https://arxiv.org/abs/2501.01446
