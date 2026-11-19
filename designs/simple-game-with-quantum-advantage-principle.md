---
type: design
id: simple-game-with-quantum-advantage-principle
title: Teach quantum computing with an algorithm that solves a simple, easily understandable problem while still providing a quantum advantage
description: "Because common quantum algorithms are complicated and \"often remain incomprehensible to learners\", the article recommends choosing an algorithm that solves \"a s imple and easily understandable problem while providing..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: rainer-müller-franziska-greinert-2021
    resource: "https://arxiv.org/abs/2108.06271"
    title: "Rainer Müller & Franziska Greinert. (2021). Playing with a Quantum Computer. https://arxiv.org/abs/2108.06271"
    author: "Rainer Müller & Franziska Greinert"
---

# Teach quantum computing with an algorithm that solves a simple, easily understandable problem while still providing a quantum advantage

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Because common quantum algorithms are complicated and "often remain incomprehensible to learners", the article recommends choosing an algorithm that solves "a s imple and easily understandable problem while providing a quantum advantage". The Quantum Penny Flip game fulfils both conditions: its rules are transparent, and the quantum strategy yields a clear winning advantage that has no counterpart in the classical game, making the advantage motivating rather than abstract.

## Design Implications

### Context
#### Requirements
- The chosen algorithm must address a problem whose meaning is immediately obvious to learners and must still offer a genuine quantum advantage.
#### Constraints
- Established algorithms with quantum advantage are difficult for learners: Deutsch-Jozsa solves a problem whose meaning is not immediately obvious, while Shor's and Grover's algorithms require difficult concepts such as modular arithmetic, the quantum Fourier transform, or amplitude amplification.

### Target Learners
- students in introductory courses on quantum physics
- high school students interested in the topic

### Learning Goals
- understanding superposition, measurement and quantum advantage

### Claims
- Quantum Penny Flip Hadamard Winning Strategy [+M]

## Related Designs
- [Quantum Penny Flip Introduction Strategy](../strategies/quantum-penny-flip-introduction-strategy.md)

## Examples
-

## Key Sources
- Rainer Müller & Franziska Greinert. (2021). Playing with a Quantum Computer. https://arxiv.org/abs/2108.06271
