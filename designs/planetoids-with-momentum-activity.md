---
type: design
id: planetoids-with-momentum-activity
title: "STEMcoding Planetoids with Momentum! activity assessing CT through a buggy inelastic-collision code"
description: "A STEMcoding project activity in which \"students take an asteroids-like code and modify it until the ship can collide and stick to a circle which is like a blob of goo drifting through space,\" illustrating a 2D perfec..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: orban-2019
    resource: "https://arxiv.org/abs/1907.08079"
    title: "Orban, C. M. and Teeling-Smith, R. M. (2019). Computational Thinking in Introductory Physics. https://arxiv.org/abs/1907.08079"
    author: Orban, C. M. and Teeling-Smith, R. M
---

# STEMcoding Planetoids with Momentum! activity assessing CT through a buggy inelastic-collision code

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A STEMcoding project activity in which "students take an asteroids-like code and modify it until the ship can collide and stick to a circle which is like a blob of goo drifting through space," illustrating a 2D perfectly inelastic collision. Students implement the momentum-conservation final-velocity code, measure the final velocity, and check it against expectation. Near the end they are given a subtly wrong version that recomputes vx2 from the updated vx1, run it, and must explain why it gives a different, wrong answer, engaging sense making and code verification.

## Design Implications

### Context
#### Requirements
- Students need the provided starter code and directions including the correct final-velocity code
#### Constraints
- The buggy code looks essentially identical to the mathematical solution, so the assessment depends on students actually running and measuring the simulation output

### Target Learners
- high school physics students
- early college introductory physics students

### Learning Goals
- perfectly inelastic collisions
- momentum conservation
- debugging and code verification

### Claims
- Math World Vs Computer World Verification [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Orban, C. M. and Teeling-Smith, R. M. (2019). Computational Thinking in Introductory Physics. https://arxiv.org/abs/1907.08079
