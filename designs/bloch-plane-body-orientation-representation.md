---
type: design
id: bloch-plane-body-orientation-representation
title: Bloch-plane body-orientation representation of qubits and measurements
description: "The framework represents quantum states as orientations of students' bodies on a circle painted on the floor, a reduced Bloch sphere restricted to the x−z plane so that complex coefficients are avoided."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: andrea-lópez-incera-2019
    resource: "https://arxiv.org/abs/1910.07845"
    title: "Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür. (2019). Encrypt me! A game-based approach to Bell inequalities and quantum cryptography. https://arxiv.org/abs/1910.07845"
    author: Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür
---

# Bloch-plane body-orientation representation of qubits and measurements

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The framework represents quantum states as orientations of students' bodies on a circle painted on the floor, a reduced Bloch sphere restricted to the x−z plane so that complex coefficients are avoided. A qubit-student rotates by the angle corresponding to the state, and measurement is stochastic: the student throws a biased die constructed so that probabilities follow Born's rule, then orients to the resulting eigenstate and announces the outcome. Entangled pairs are represented by two students holding hands and spinning, so outcomes are anti-correlated in any direction until measured. The article states that "the behavior of the quantum qubits is probabilistic, and depends on the relative orientation between the measurement axis ... and the quantum state".

## Design Implications

### Context
#### Requirements
- A Bloch plane painted on the floor, compass sticks to mark measurement directions and positive sides, and biased dice (or dice apps) matching the required probability distributions for each separation angle.
#### Constraints
- Only states in the x−z plane of the Bloch sphere are represented, with azimuthal angle fixed to 0 or π; the game as presented does not mimic spatial separation of entangled particles because entangled students hold hands.

### Target Learners
- high school students

### Learning Goals
- superposition
- measurement probabilism and state collapse
- entanglement
- Bell inequalities
- quantum cryptography

### Claims
- [Kinesthetic Qubit Game First Hand Experience](../claims/kinesthetic-qubit-game-first-hand-experience.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür. (2019). Encrypt me! A game-based approach to Bell inequalities and quantum cryptography. https://arxiv.org/abs/1910.07845
