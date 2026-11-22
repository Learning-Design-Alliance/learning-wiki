---
type: design
id: ar-bb84-quantum-cryptography-experiment
title: AR-enhanced BB84 quantum cryptography experiment with real-time polarization visualizations on HoloLens 2
description: An adapted version of the Thorlabs quantum cryptography analogy experiment in which AR glasses overlay vectorial representations of single-photon polarization states onto the physical setup.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: atakan-coban-2024
    resource: "https://www.lmu.de"
    title: "Atakan Coban, David Dzsotjan, Stefan Küchemann, Jürgen Durst, Jochen Kuhn & Christoph Hoyer. (2024). AI Support Meets AR Visualization for Alice and Bob: Personalized Learning Based on Individual ChatGPT Feedback in an AR Quantum Cryptography Experiment for Physics Lab Courses. https://www.lmu.de"
    author: "Atakan Coban, David Dzsotjan, Stefan Küchemann, Jürgen Durst, Jochen Kuhn & Christoph Hoyer"
---

# AR-enhanced BB84 quantum cryptography experiment with real-time polarization visualizations on HoloLens 2

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 2 claims rest on one study

## Description
An adapted version of the Thorlabs quantum cryptography analogy experiment in which AR glasses overlay vectorial representations of single-photon polarization states onto the physical setup. QR codes anchor the visualizations, and "a microcontroller reads out the states of the lambda/2 plates in the setup in real time and sends this data to the AR glasses via Bluetooth", so the displayed polarization states update with the lab partners' actions. The application also integrates verbal ChatGPT interaction via speech-to-text and text-to-speech, and the ARETT toolkit for gaze data collection.

## Design Implications

### Context
#### Requirements
- HoloLens 2 AR glasses with QR-code anchoring of visualizations to the physical setup
- a microcontroller reading lambda/2 plate states and transmitting them via Bluetooth
- the ARETT toolkit integrated for eye-gaze data collection
#### Constraints
- The study used short-duration laser pulses instead of single photons, as in the Thorlabs analogy kit

### Target Learners
- university students in physics laboratory courses

### Learning Goals
- understanding the BB84 quantum key distribution protocol
- understanding photon polarization states and bases
- detecting eavesdropping in quantum communication

### Claims

- [Chatgpt Feedback Improves Ar Quantum Crypto Lab Scores](../claims/chatgpt-feedback-improves-ar-quantum-crypto-lab-scores.md) [+M]
- [An optics-based approach using classical light polarization provides a clear and accessible way to represent quantum states and gate operators and facilitates learning and transfer to other STEM skills in a high school quantum computing course](../claims/classical-optics-represents-quantum-states-high-school.md) [+W]

## Related Designs

- [Modified BB84 QKD setup using macroscopic laser \"qubits\" with an intentional security loophole](modified-bb84-macroscopic-qubits-setup.md)
- [Manual QKD analogy kit with 3D-printed components and classical-light polarization analogy](manual-qkd-analogy-kit-3d-printed.md)

## Examples
-

## Key Sources
- Atakan Coban, David Dzsotjan, Stefan Küchemann, Jürgen Durst, Jochen Kuhn & Christoph Hoyer. (2024). AI Support Meets AR Visualization for Alice and Bob: Personalized Learning Based on Individual ChatGPT Feedback in an AR Quantum Cryptography Experiment for Physics Lab Courses. https://www.lmu.de
