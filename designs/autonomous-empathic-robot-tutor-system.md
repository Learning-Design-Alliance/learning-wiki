---
type: design
id: autonomous-empathic-robot-tutor-system
title: Autonomous empathic robot tutor with hybrid behavior controller for group learning
description: The robotic tutor comprises perception, memory, task management, student modeling, rapport, game AI, and hybrid behavior controller modules.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: patrícia-alves-oliveira-2019
    resource: "https://doi.org/10.1145/3300188"
    title: "Patrícia Alves-Oliveira, Pedro Sequeira, Francisco S. Melo, Ginevra Castellano, and Ana Paiva. 2019. Empathic Robot for Group Learning: A Field Study. ACM Trans. Hum.-Robot Interact. 1, 1, Article 1 (January 2019), 36 pages. https://doi.org/10.1145/3300188"
    author: Patrícia Alves-Oliveira, Pedro Sequeira, Francisco S. Melo, Ginevra Castellano, and Ana Paiva
---

# Autonomous empathic robot tutor with hybrid behavior controller for group learning

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The robotic tutor comprises perception, memory, task management, student modeling, rapport, game AI, and hybrid behavior controller modules. The article states the "Hybrid Behavior Controller" is "the core module controlling the robot's social interaction behavior," deciding game actions and structuring dialogue informed by emotional climate. It uses interaction strategy rules encoding expert domain knowledge plus a machine-learning mapping function trained from Restricted-Perception Wizard-of-Oz studies.

## Design Implications

### Context
#### Requirements
- Audio-visual sensing devices for perceiving student states
- Interaction strategy rules and an ML mapping function trained on wizard demonstrations
- Restricted-Perception WoZ methodology limiting expert access to the same perceptual features available to the autonomous robot
#### Constraints
- The robot's behavior depends on the same processed perceptual observations that drive its autonomous behavior

### Target Learners
- Children learning in groups of two or three

### Learning Goals
- Collaborative learning about sustainable development

### Claims
- [Empathic Robot Fosters Sustainability Discussions](../claims/empathic-robot-fosters-sustainability-discussions.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Patrícia Alves-Oliveira, Pedro Sequeira, Francisco S. Melo, Ginevra Castellano, and Ana Paiva. 2019. Empathic Robot for Group Learning: A Field Study. ACM Trans. Hum.-Robot Interact. 1, 1, Article 1 (January 2019), 36 pages. https://doi.org/10.1145/3300188
