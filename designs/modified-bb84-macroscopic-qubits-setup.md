---
type: design
id: modified-bb84-macroscopic-qubits-setup
title: "Modified BB84 QKD setup using macroscopic laser \"qubits\" with an intentional security loophole"
description: "A simplified BB84 quantum key distribution implementation for pre-university students in which polarization-encoded \"qubits\" are macroscopic laser pulses containing many photons, built from a laser diode, quarter-wave..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: adrian-nugraha-utama-2020
    resource: "https://arxiv.org/abs/1911.02565v2"
    title: "Adrian Nugraha Utama, Jianwei Lee, and Mathias Alexander Seidler. (2020). A Hands-On Quantum Cryptography Workshop For Pre-University Students. arXiv:1911.02565v2 [physics.ed-ph]. https://arxiv.org/abs/1911.02565v2"
    author: Adrian Nugraha Utama, Jianwei Lee, and Mathias Alexander Seidler
---

# Modified BB84 QKD setup using macroscopic laser "qubits" with an intentional security loophole

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A simplified BB84 quantum key distribution implementation for pre-university students in which polarization-encoded "qubits" are macroscopic laser pulses containing many photons, built from a laser diode, quarter-wave plate, motorized polarizers, silicon photodiodes, and IR transceiver circuits. The article states: "We intentionally introduce a subtle but critical simpliﬁcation to the original protocol, allowing the experiment to be assembled at the skill level appropriate for the students, at the cost of creating a security loophole." The loophole enables a student side-channel attack that exposes the role of the no-cloning theorem.

## Design Implications

### Context
#### Requirements
- Off-the-shelf optical and electronic components including a laser diode, QWP, motorized polarizers, Si-PIN photodiodes, and IR LEDs, with Arduino and Python control programs
#### Constraints
- Using macroscopic light rather than single photons compromises security, since "a fraction of the qubits can be intercepted and measured by an adversary"; the loophole is intentional and pedagogical, and the key-comparison step was omitted because Eve does not resend "qubits"

### Target Learners
- pre-university students aged 15 to 19

### Learning Goals
- understanding the BB84 quantum key distribution protocol
- understanding the no-cloning theorem and its role in quantum cryptography
- understanding how pulse sequences transmit information over a classical channel

### Claims
- [Cognitive Conflict Hacking Bb84](../claims/cognitive-conflict-hacking-bb84.md) [+M]

## Related Designs

- [AR-enhanced BB84 quantum cryptography experiment with real-time polarization visualizations on HoloLens 2](ar-bb84-quantum-cryptography-experiment.md)
- [Manual QKD analogy kit with 3D-printed components and classical-light polarization analogy](manual-qkd-analogy-kit-3d-printed.md)

## Examples
-

## Key Sources
- Adrian Nugraha Utama, Jianwei Lee, and Mathias Alexander Seidler. (2020). A Hands-On Quantum Cryptography Workshop For Pre-University Students. arXiv:1911.02565v2 [physics.ed-ph]. https://arxiv.org/abs/1911.02565v2
