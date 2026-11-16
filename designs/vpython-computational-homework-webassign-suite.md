---
type: design
id: vpython-computational-homework-webassign-suite
title: VPython-based computational homework suite in introductory mechanics, deployed with randomized initial conditions via WebAssign
description: A suite of fourteen computational modeling homework questions delivered in WebAssign in a one-semester large lecture mechanics course, in which 1357 students solved problems using VPython.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-16
sources:
  - id: marcos-d-caballero-2011
    resource: "https://arxiv.org/abs/1112.5069"
    title: "Marcos D. Caballero, Matthew A. Kohlmyer and Michael F. Schatz. (2011). Fostering Computational Thinking In Introductory Mechanics. https://arxiv.org/abs/1112.5069"
    author: Marcos D. Caballero, Matthew A. Kohlmyer and Michael F. Schatz
---

# VPython-based computational homework suite in introductory mechanics, deployed with randomized initial conditions via WebAssign

> **Design** · [All designs](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 3 studies (2 design, 1 causal), `q2`–`q3` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
A suite of fourteen computational modeling homework questions delivered in WebAssign in a one-semester large lecture mechanics course, in which 1357 students solved problems using VPython. To create each problem, the authors "numerically integrated several hundred initial conditions" for the physical system and stored the solutions, and "each student was assigned a random set of initial conditions that ensured each student received a unique realization with high probability."

## Design Implications

### Context
#### Requirements
- WebAssign course management system for deployment and weekly grading; pre-integrated solution banks for randomized initial conditions
#### Constraints
- Only students' final results (numeric answers) were graded; uploaded code was not graded, so working programs could be distributed from student to student

### Target Learners
- undergraduate introductory calculus-based mechanics students, including those with no previous programming experience

### Learning Goals
- applying Newton's Second Law iteratively to predict motion
- constructing computational models of force and motion

### Claims

- [In a large introductory mechanics course, the majority of students (60.4%) successfully completed a proctored computational modeling evaluation on a novel central force problem after a semester of computational homework.](../claims/computational-evaluation-majority-success-intro-mechanics.md) [+M]
- [After computational homework, many introductory mechanics students could model a new physical situation they had no prior experience with](../claims/computational-homework-novel-situation-modeling.md) [+M]
- [Incorrect student VPython programs cluster into a few error patterns within three procedural areas: initial conditions, force calculation, and Newton's second law](../claims/student-program-errors-few-procedural-patterns.md) [+W]
- [Students solved analytic and computational homework problems with similar success rates (84.6% vs 85.8%)](../claims/analytic-vs-computational-homework-equal-success.md) [+M]
- [Prior programming experience did not predict success on the proctored computational evaluation.](../claims/prior-programming-experience-no-advantage.md) [~W]

## Related Designs

- [VPython computational modeling homework in introductory mechanics](vpython-computational-modeling-homework-mechanics.md)

## Examples
-

## Key Sources
- Marcos D. Caballero, Matthew A. Kohlmyer and Michael F. Schatz. (2011). Fostering Computational Thinking In Introductory Mechanics. https://arxiv.org/abs/1112.5069
