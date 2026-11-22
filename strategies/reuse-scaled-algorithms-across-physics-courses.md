---
type: strategy
id: reuse-scaled-algorithms-across-physics-courses
title: Reuse algorithms across physics courses by scaling equations into shared dimensionless forms
description: "A concrete teaching strategy: have students develop a numerical solver in one course, scale the equations to dimensionless form, and reuse the same algorithm in later courses on different physics."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: marcos-daniel-caballero-and-morten-hjorth-jensen-2018
    resource: "https://arxiv.org/abs/1802.08871"
    title: "Marcos Daniel Caballero and Morten Hjorth-Jensen. (2018). Integrating a Computational Perspective in Physics Courses. https://arxiv.org/abs/1802.08871"
    author: Marcos Daniel Caballero and Morten Hjorth-Jensen
---

# Reuse algorithms across physics courses by scaling equations into shared dimensionless forms

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
A concrete teaching strategy: have students develop a numerical solver in one course, scale the equations to dimensionless form, and reuse the same algorithm in later courses on different physics. The article states "The idea is that algorithms students develop and use in one course can be reused in other courses", citing the pendulum and RLC circuit yielding essentially the same scaled equations, and the buckling beam mapping to quantum eigenvalue problems by changing diagonal matrix elements.

## Design Implications

### Context
#### Requirements
- Properly scaled, dimensionless equations so different problems map onto the same algorithm
- Earlier courses (mechanics before electromagnetism) sequenced so the solver exists before reuse
#### Constraints
- The article notes main differences remain in scaling constants and, for the pendulum, a nonlinear term in the angle

### Target Learners
- undergraduate physics students in mechanics, electromagnetism, quantum mechanics and statistical physics courses

### Target Learning Goals
- abstraction and generalization
- algorithmic thinking
- recognizing shared structure across physics problems

## Related Strategies

- [Teaching sequence: discretize the evolution equations, implement the recurrences in a spreadsheet, and compare classical, stochastic and quantum solutions](spreadsheet-recurrence-teaching-sequence.md)
- [Incorporate computation into an existing classical mechanics course through in-class demonstrations followed by student projects that progress from template modification to independent construction](demonstration-template-to-independent-projects.md)
- [Relativity lab exercises in which students check whether other metrics fulfill the Einstein equations by modifying the given program sequences](relativity-lab-metric-checking-exercises.md)
- [Use a universal constant-acceleration plot so students can solve relativistic acceleration problems graphically without equations](universal-acceleration-plot-strategy.md)

## Examples
-

## Key Sources
- Marcos Daniel Caballero and Morten Hjorth-Jensen. (2018). Integrating a Computational Perspective in Physics Courses. https://arxiv.org/abs/1802.08871
