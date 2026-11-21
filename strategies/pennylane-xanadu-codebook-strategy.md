---
type: strategy
id: pennylane-xanadu-codebook-strategy
title: Teach PennyLane through a Docker-based environment and the Xanadu Codebook with in-class codercises
description: For PennyLane, the article recommends setting up a Docker container specifically for PennyLane to ensure a consistent, controlled environment, then following the Xanadu Codebook, which the authors advise lecturers to...
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

# Teach PennyLane through a Docker-based environment and the Xanadu Codebook with in-class codercises

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For PennyLane, the article recommends setting up a Docker container specifically for PennyLane to ensure a consistent, controlled environment, then following the Xanadu Codebook, which the authors advise lecturers to adhere to as it "provides a structured and detailed curriculum for teaching the package effectively". In-class solving of the codebook's "codercises" gives hands-on practice. Suggested topics range from qubits, circuits and gates through teleportation, Grover's algorithm, QFT, QPE, and Shor's algorithm, with quantum machine learning, VQE, QAOA, and Quantum Kernel as optional content depending on class level.

## Design Implications

### Context
#### Requirements
- A Docker container setup for PennyLane and use of the Xanadu Codebook (codebook.xanadu.ai) as the structured curriculum
#### Constraints
- Advanced content such as quantum machine learning, Hamiltonian simulation, VQE, QAOA, and Quantum Kernel is taught at the mentors' discretion based on course topics and class level

### Target Learners
- University students in quantum programming courses, with content depth adjusted to class level

### Target Learning Goals
- Programming with PennyLane
- Quantum circuits, algorithms, and optionally quantum machine learning

## Related Strategies

- [Teach Ocean SDK via account setup, Leap/SAPI authentication, and job submission to D-Wave QPUs](ocean-sdk-dwave-teaching-sequence.md)
- [Sequence Qiskit instruction from environment setup through real-QPU job submission with multi-platform examples](qiskit-qpu-job-submission-sequence.md)
- [Introduce quantum software engineering and the hybrid classical-quantum SDLC alongside programming frameworks](quantum-sdlc-curriculum-component.md)
- [Use a centrally administered hands-on platform with pre-installed software and real-time monitoring](wac-central-hands-on-platform-strategy.md)

## Examples
-

## Key Sources
- Majid Haghparast, Enrique Moguel, Jose Garcia-Alonso, Tommi Mikkonen, Juan Manuel Murillo. (2024). Innovative Approaches to Teaching Quantum Computer Programming and Quantum Software Engineering. https://arxiv.org/abs/2501.01446
