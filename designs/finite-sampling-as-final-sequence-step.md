---
type: design
id: finite-sampling-as-final-sequence-step
title: Treat finite sampling as the final step of the physics sequence rather than a separate statistics topic
description: "The article embeds finite sampling as the last step of the instructional sequence: students first obtain theoretical probabilities from eigenstate amplitudes, then compare them with frequencies from a finite number of..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: boris-kiefer-2026
    resource: "https://arxiv.org/abs/2609.36401"
    title: "Boris Kiefer. (2026). From Two-Level Hamiltonians to Quantum Superposition and Measurement: A Traceable Classroom Module. arXiv. https://arxiv.org/abs/2609.36401"
    author: Boris Kiefer
---

# Treat finite sampling as the final step of the physics sequence rather than a separate statistics topic

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article embeds finite sampling as the last step of the instructional sequence: students first obtain theoretical probabilities from eigenstate amplitudes, then compare them with frequencies from a finite number of simulated measurements. This makes explicit that Born-rule probabilities describe the underlying distribution while counts fluctuate across finite realizations even when the Hamiltonian and state are unchanged. The optional binomial standard-error estimate gives the fluctuation scale.

## Design Implications

### Context
#### Requirements
- A simulator panel displaying theoretical probabilities and sampled frequencies together, allowing the number of trials and random realization to vary independently of the Hamiltonian
#### Constraints
- The module deliberately focuses on static eigensystems and computational-basis measurement; it does not treat density matrices, mixed states, continuous-variable systems, multi-qubit entanglement, or sequential projective measurement with state update

### Target Learners
- undergraduate quantum-mechanics students

### Learning Goals
- distinguishing theoretical probabilities from finite-sample frequencies and explaining how increasing trials affects fluctuations without changing the state

### Claims
- [Four Quantum Superposition Measurement Difficulties](../claims/four-quantum-superposition-measurement-difficulties.md) [+M]

## Related Designs

- [Five-activity predict-observe-explain sequence from Hamiltonian structure to finite measurement statistics](hamiltonian-to-sampling-activity-sequence.md)

## Examples
-

## Key Sources
- Boris Kiefer. (2026). From Two-Level Hamiltonians to Quantum Superposition and Measurement: A Traceable Classroom Module. arXiv. https://arxiv.org/abs/2609.36401
