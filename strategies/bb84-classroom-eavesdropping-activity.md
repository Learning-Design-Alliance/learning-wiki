---
type: strategy
id: bb84-classroom-eavesdropping-activity
title: BB84 classroom activity with eavesdropper roles and a security test on part of the key
description: Students form groups with one Alice, one Bob, qubits, and Eavesdroppers.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: andrea-lópez-incera-2019
    resource: "https://arxiv.org/abs/1910.07845"
    title: "Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür. (2019). Encrypt me! A game-based approach to Bell inequalities and quantum cryptography. https://arxiv.org/abs/1910.07845"
    author: Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür
---

# BB84 classroom activity with eavesdropper roles and a security test on part of the key

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Students form groups with one Alice, one Bob, qubits, and Eavesdroppers. Alice prepares qubits in the four states {|0⟩,|1⟩,|0x⟩,|1x⟩}, Bob measures in randomly chosen x or z directions, bases are announced publicly, and coincident-basis outcomes form the key used for a one-time-pad encryption of a message. Part of the key is sacrificed as a security test: Alice and Bob compare a subset of bits publicly, and if they differ they abort and restart. Students playing Eavesdroppers devise interception strategies, and the article suggests several, including measuring before Bob, keeping Alice's qubit and substituting a random one, and guessing the key.

## Design Implications

### Context
#### Requirements
- Only two measurement directions (x and z) and the four corresponding states; Alice must prepare at least twice as many qubits as message digits since only half the directions coincide and part of the key is consumed by the security test.
#### Constraints
- Because measurement is stochastic, the Eavesdropper has some probability of going unnoticed; the checked key bits can no longer be used for encryption.

### Target Learners
- high school students

### Target Learning Goals
- quantum key distribution
- no-cloning-like disturbance detection
- one-time pad encryption
- probability

### Affordances
- [Bloch Plane Body Orientation Representation](../designs/bloch-plane-body-orientation-representation.md)

## Claims

- [Revised simulation and activity significantly improved introductory students' answers on actions Alice and Bob can take to detect Eve (78.0% vs 58.9% correct)](../claims/revised-sim-improved-detect-eve-answers.md) [+W]

## Related Strategies

- [Play the BB84 quantum cryptography protocol using only part 1 of the game](entangle-game-bb84-extension.md)
- [E91 entanglement-based key distribution game with CHSH test as eavesdropping check](e91-entanglement-key-game.md)
- [Debriefing session that reveals Eve and discusses why the setup deviates from ideal BB84](eve-reveal-debriefing-strategy.md)
- [Use action-based, unplugged activities to introduce quantum information and quantum key distribution](action-based-quantum-informatics-introduction.md)
- [Frame quantum error correction as a privacy constraint: treat detection and recovery operations as eavesdroppers that must never access the encoded information](eavesdropper-framing-quantum-decoding.md)
- [Demonstrating quantum key distribution (BB84 and E91) with Quantum Dice](quantum-dice-qkd-demonstration-strategy.md)
- [Implement the eavesdropper as a quarter-wave plate in a mount visually identical to Alice's and Bob's to keep its presence ambiguous](ambiguous-eavesdropper-quarter-wave-plate.md)

## Examples
-

## Key Sources
- Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür. (2019). Encrypt me! A game-based approach to Bell inequalities and quantum cryptography. https://arxiv.org/abs/1910.07845
