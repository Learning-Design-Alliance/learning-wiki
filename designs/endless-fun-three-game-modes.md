---
type: design
id: endless-fun-three-game-modes
title: "Three game modes with distinct learning objectives: competitive, cooperative, and single-player guided riddles"
description: The game implements a multi-mode design pattern in which each mode addresses different learning objectives.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: lea-kopf-2022
    resource: "https://arxiv.org/abs/2107.12007"
    title: "Lea Kopf, Markus Hiekkamäki, Shashi Prabhakar and Robert Fickler. (2022). Endless Fun in high dimensions - A Quantum Card Game. https://arxiv.org/abs/2107.12007"
    author: Lea Kopf, Markus Hiekkamäki, Shashi Prabhakar and Robert Fickler
---

# Three game modes with distinct learning objectives: competitive, cooperative, and single-player guided riddles

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The game implements a multi-mode design pattern in which each mode addresses different learning objectives. In the competitive mode players oppose each other; in the cooperative mode "the goal is not to win against the other players but to reach the highest possible values summed up over all qudits as a group"; in the single-player mode, six ready-made riddles of graduated difficulty guide players to discover specific quantum effects, with the significance of each effect discussed along with its solution. Instructors can extend the riddle set with their own.

## Design Implications

### Context
#### Requirements
- Riddle cards with instructions and solutions, and the evaluation software for checking outcomes; in cooperative mode players cannot show their cards or discuss strategies
#### Constraints
- The regular multiplayer setup and gameplay rules do not apply in the single-player mode

### Target Learners
- small groups of students (1-7 players) in courses or outreach
- individual learners using the riddle mode

### Learning Goals
- learning quantum interference effects, entanglement and gate composition through guided riddles
- collaborative group optimization of a shared quantum state

### Claims
- 

## Related Designs
- Endless Fun Card Game Element

## Examples
-

## Key Sources
- Lea Kopf, Markus Hiekkamäki, Shashi Prabhakar and Robert Fickler. (2022). Endless Fun in high dimensions - A Quantum Card Game. https://arxiv.org/abs/2107.12007
