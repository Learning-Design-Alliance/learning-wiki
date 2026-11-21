---
type: strategy
id: e91-entanglement-key-game
title: E91 entanglement-based key distribution game with CHSH test as eavesdropping check
description: "In the E91 activity, entangled qubit pairs in the Bell state |ψ−⟩ are measured by Alice and Bob, who each randomly choose among three directions; coincident-direction outcomes, with anti-correlation converted to match..."
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

# E91 entanglement-based key distribution game with CHSH test as eavesdropping check

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
In the E91 activity, entangled qubit pairs in the Bell state |ψ−⟩ are measured by Alice and Bob, who each randomly choose among three directions; coincident-direction outcomes, with anti-correlation converted to matching bits, form the key. For non-coincident directions separated by π/4, the pair's outcomes are used to compute the CHSH quantity: if |⟨S⟩| exceeds 2 the qubits were still entangled and the key is secure, otherwise the key is discarded because eavesdropping broke the entanglement. The article notes real entangled particles can be arbitrarily separated, and suggests the two-Bloch-circles game variant to emphasize this.

## Design Implications

### Context
#### Requirements
- Entangled-pair game rules, measurement directions as in the article's Figure 8 with some separated by π/4, and agreed conventions for converting outcomes +1/−1 to bits 0/1.
#### Constraints
- If the CHSH inequality is fulfilled (S ≤ 2), Alice and Bob must create a new secure key.

### Target Learners
- high school students

### Target Learning Goals
- entanglement-based quantum key distribution
- Bell test as security check
- eavesdropping detection

### Affordances
- [Bloch Plane Body Orientation Representation](../designs/bloch-plane-body-orientation-representation.md)

## Related Strategies

- [BB84 classroom activity with eavesdropper roles and a security test on part of the key](bb84-classroom-eavesdropping-activity.md)
- [Mermin-style Bell-test alternative requiring less mathematical background but more measurements](mermin-bell-test-low-math-alternative.md)
- [Follow the demonstration with a qualitative discussion encoding a shared encryption key in measurement outcomes and detecting an eavesdropper via Bell test failure](post-demo-qkd-encryption-discussion.md)
- [Teach quantum entanglement via principle explanation in analogy to the standard special relativity introduction](principle-explanation-entanglement-strategy.md)
- [Use action-based, unplugged activities to introduce quantum information and quantum key distribution](action-based-quantum-informatics-introduction.md)
- [Represent entangled states with pairs of attached Bloch Cubes that rotate together](bloch-cube-pairs-entanglement-strategy.md)

## Examples
-

## Key Sources
- Andrea López-Incera, Andreas Hartmann, and Wolfgang Dür. (2019). Encrypt me! A game-based approach to Bell inequalities and quantum cryptography. https://arxiv.org/abs/1910.07845
