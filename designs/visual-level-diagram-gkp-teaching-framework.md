---
type: design
id: visual-level-diagram-gkp-teaching-framework
title: "A geometric, visual-progression framework for teaching GKP qubits: from discrete level diagrams through padding and syndrome decoding to the continuous-variable code"
description: The article organises a two-hour session around a sequence of visual level diagrams that progressively transform a classical coding picture into the GKP code.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: richard-a-wolf-2025
    resource: "https://arxiv.org/abs/2507.06943"
    title: "Richard A. Wolf, Pavithran Iyer. (2025). No physics required! A visual-based introduction to GKP qubits for computer scientists. https://arxiv.org/abs/2507.06943"
    author: Richard A. Wolf, Pavithran Iyer
---

# A geometric, visual-progression framework for teaching GKP qubits: from discrete level diagrams through padding and syndrome decoding to the continuous-variable code

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article organises a two-hour session around a sequence of visual level diagrams that progressively transform a classical coding picture into the GKP code. Learners start with a two-level encoding of logical states, add padding levels for redundancy, extend to four levels for correction, move to a 2D grid distinguishing X and Z errors, and finally take the limit to a continuous real line where "the level diagram is replaced by a continuous real line, and displacements are parametrized by a continuous variable". Each stage reuses the same visual vocabulary of shaded active cells, code space, and syndrome questions.

## Design Implications

### Context
#### Requirements
- Learners must have undergraduate-level linear algebra, probability theory, classical coding theory basics, and basic familiarity with complex numbers
#### Constraints
- The session is introductory; the normalisation of GKP states is stated to fall outside its scope, and approximate GKP states are deferred to the cited literature

### Target Learners
- learners with an undergraduate computer science background
- professional learners from classical computing entering quantum computing

### Learning Goals
- understand the geometric intuition behind GKP qubits
- understand quantum error correction concepts: encoding, syndrome measurement, decoding, logical vs physical errors

### Claims
- [Gkp Session Cs Prerequisites Only](../claims/gkp-session-cs-prerequisites-only.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Richard A. Wolf, Pavithran Iyer. (2025). No physics required! A visual-based introduction to GKP qubits for computer scientists. https://arxiv.org/abs/2507.06943
