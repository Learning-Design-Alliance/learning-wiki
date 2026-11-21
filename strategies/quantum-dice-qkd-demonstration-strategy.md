---
type: strategy
id: quantum-dice-qkd-demonstration-strategy
title: Demonstrating quantum key distribution (BB84 and E91) with Quantum Dice
description: The Dice support simplified quantum key distribution protocols.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: b-folkers-2025
    resource: "https://arxiv.org/abs/2510.04931"
    title: "B. Folkers, A. van Rossum, A. Brinkman and H. K. E. Stadermann. (2025). Visualising Quantum Entanglement Using Interactive Electronic Quantum Dice. https://arxiv.org/abs/2510.04931"
    author: B. Folkers, A. van Rossum, A. Brinkman and H. K. E. Stadermann
---

# Demonstrating quantum key distribution (BB84 and E91) with Quantum Dice

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The Dice support simplified quantum key distribution protocols. With a single die (BB84), users A and B take turns rolling, record basis colour and outcome, share bases (not outcomes), discard mismatched-colour measurements, and use matching outcomes as a shared key "without explicitly transmitting the key values". With two entangled Dice (E91), the anti-correlation lets both users derive the other's value; a third person (Eve) can demonstrate how measurement disturbs the state and reveals interception.

## Design Implications

### Context
#### Requirements
- For the E91 protocol, re-entanglement is required between rounds to prepare new entangled states; a 'Quantum Mode' button resets the single die to superposition between measurements
#### Constraints
- The article describes this as a simplified demonstration of quantum key distribution protocols, not an authentic cryptographic implementation

### Target Learners
- secondary school students
- undergraduate physics students

### Target Learning Goals
- understanding quantum key distribution
- understanding how measurement disturbs quantum states and enables eavesdropper detection

## Related Strategies

- [Adapt Dice versions and basis orientations across educational levels, and develop teaching guides and expanded protocols](quantum-dice-differentiation-and-future-development-strategy.md)
- [Follow the demonstration with a qualitative discussion encoding a shared encryption key in measurement outcomes and detecting an eavesdropper via Bell test failure](post-demo-qkd-encryption-discussion.md)
- [E91 entanglement-based key distribution game with CHSH test as eavesdropping check](e91-entanglement-key-game.md)
- [BB84 classroom activity with eavesdropper roles and a security test on part of the key](bb84-classroom-eavesdropping-activity.md)
- [Play the BB84 quantum cryptography protocol using only part 1 of the game](entangle-game-bb84-extension.md)

## Examples
-

## Key Sources
- B. Folkers, A. van Rossum, A. Brinkman and H. K. E. Stadermann. (2025). Visualising Quantum Entanglement Using Interactive Electronic Quantum Dice. https://arxiv.org/abs/2510.04931
