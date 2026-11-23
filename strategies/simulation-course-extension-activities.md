---
type: strategy
id: simulation-course-extension-activities
title: "Extension activities: building code from scratch, measuring runtime, the Verlet algorithm, and multi-body extensions"
description: "The article proposes extensions for different student levels: students can build the program from scratch instead of using a template, work out why motion can be treated in a plane, and play with parameters like masse..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: c-körber-2018
    resource: "https://arxiv.org/abs/1803.01678"
    title: "C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart. (2018). A primer to numerical simulations: The perihelion motion of Mercury. arXiv. https://arxiv.org/abs/1803.01678"
    author: C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart
---

# Extension activities: building code from scratch, measuring runtime, the Verlet algorithm, and multi-body extensions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes extensions for different student levels: students can build the program from scratch instead of using a template, work out why motion can be treated in a plane, and play with parameters like masses and starting velocities to get a better feeling for the physics. Performance extensions include measuring calculation time and implementing the Verlet algorithm instead of the simple Euler method; extended problems include a non-stationary Sun and a three-body problem.

## Design Implications

### Context
#### Requirements
- Building the code from scratch requires some basic knowledge in VPython, which students could acquire by working through introductory materials.
#### Constraints
- There is a limit to decreasing the time steps because the time needed for the calculation grows simultaneously.

### Target Learners
- ambitious and advanced high school students

### Target Learning Goals
- autonomous problem exploration
- understanding accuracy-performance trade-offs in simulation
- Newton's third law and planetary interactions

## Related Strategies

- [Per-solver student exploration exercises that modify or extend the solver to build deeper method understanding](pyro-student-exploration-extensions.md)
- [Teach performance measurement before parallelism and template-based alternatives](measure-performance-first-strategy.md)
- [Have students build simulators from scratch instead of using established frameworks that abstract away implementation details](build-simulators-from-scratch-strategy.md)
- [Flexible extensions: edge-geometry variables and slow-motion video for advanced course levels](teapot-activity-extensions-strategy.md)

## Examples
-

## Key Sources
- C. Körber, I. Hammer, J.-L. Wynen, J. Heuer, C. Müller and C. Hanhart. (2018). A primer to numerical simulations: The perihelion motion of Mercury. arXiv. https://arxiv.org/abs/1803.01678
