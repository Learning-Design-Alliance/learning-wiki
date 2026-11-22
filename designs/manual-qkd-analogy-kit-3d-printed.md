---
type: design
id: manual-qkd-analogy-kit-3d-printed
title: Manual QKD analogy kit with 3D-printed components and classical-light polarization analogy
description: A hands-on QKD analogy kit built from affordable, 3D-printed components that uses a green laser, polarizing film, half-wave-plate film rotators, a beam-splitter polarization analyzer, solar-panel detectors, and an Ard...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: john-m-donohue-2026
    resource: "https://arxiv.org/abs/2607.20738v1"
    title: "John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini. (2026). Interactive and accessible quantum key distribution modules for introducing students to quantum science and engineering. https://arxiv.org/abs/2607.20738v1"
    author: John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini
---

# Manual QKD analogy kit with 3D-printed components and classical-light polarization analogy

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A hands-on QKD analogy kit built from affordable, 3D-printed components that uses a green laser, polarizing film, half-wave-plate film rotators, a beam-splitter polarization analyzer, solar-panel detectors, and an Arduino Uno to mimic single-photon QKD statistics with bright classical light. The primary design considerations were "cost (to approach affordability for high-school educators), ease-of-use (to allow many kits to run in parallel with few facilitators), and interactivity (to allow significant hands-on experience for students)." The estimated manual kit cost is $205 CAD, rising to $211 with servo motors for automation.

## Design Implications

### Context
#### Requirements
- Access to a 3D printer for PLA filament components
- A green laser near 520 nm wavelength for compatibility with the wave-plate film
- Wave-plate polymer retarder film, for which only one reliable supplier was found
#### Constraints
- The analogy prohibits any sort of quantum-enabled secure key exchange, as it is vulnerable to attacks where the eavesdropper intercepts a small amount of the light energy
- The wiring to batteries and Arduino in the free-placement magnetic version is prone to disconnected wires and other errors

### Target Learners
- high-school students
- undergraduate students
- high-school teachers

### Learning Goals
- measurement bases
- superposition
- quantum key distribution protocol
- polarization of light

### Claims

- [The polarization apparatus lets students observe Malus's law and photoelastic stress patterns with 3D-printed rotating polarizer mounts](../claims/3d-polarization-malus-photoelasticity-observations.md) [+W]

## Related Designs

- [Dual manual-then-automated progression for hands-on quantum kits](dual-manual-automated-kit-progression.md)
- [Modified BB84 QKD setup using macroscopic laser \"qubits\" with an intentional security loophole](modified-bb84-macroscopic-qubits-setup.md)
- [AR-enhanced BB84 quantum cryptography experiment with real-time polarization visualizations on HoloLens 2](ar-bb84-quantum-cryptography-experiment.md)

## Examples
-

## Key Sources
- John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini. (2026). Interactive and accessible quantum key distribution modules for introducing students to quantum science and engineering. https://arxiv.org/abs/2607.20738v1
