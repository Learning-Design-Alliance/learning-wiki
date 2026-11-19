---
type: design
id: progression-based-four-exercise-pde-course
title: "Progression-based short course: four exercises of increasing complexity, each laying groundwork for the next"
description: "The course is organised around progression as its guiding philosophy: \"Four exercises of increasing complexity were developed\", moving from the Laplace equation, through transient diffusion (with reaction), to a conve..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: pavan-inguva-2020
    resource: "https://arxiv.org/abs/2008.10931"
    title: "Pavan Inguva, Vijesh J. Bhute, Thomas N.H. Cheng, Pierre J. Walker. (2020). Introducing students to research codes: A short course on solving partial differential equations in Python. Preprint submitted to Education for Chemical Engineers. https://arxiv.org/abs/2008.10931"
    author: Pavan Inguva, Vijesh J. Bhute, Thomas N.H. Cheng, Pierre J. Walker
---

# Progression-based short course: four exercises of increasing complexity, each laying groundwork for the next

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The course is organised around progression as its guiding philosophy: "Four exercises of increasing complexity were developed", moving from the Laplace equation, through transient diffusion (with reaction), to a convection-diffusion-reaction system, and finally a modified Cahn–Hilliard equation modelling polymer blend demixing. "Each exercise was designed to simultaneously introduce the necessary content at that stage and also lay the groundwork for students to progress to the next exercise to enable students to progress to more complex problems." Exercises are further divided into parts with clear goals so students can see which code corresponds to which change in the equation.

## Design Implications

### Context
#### Requirements
- Students should have prior conceptual familiarity with the problem context (transport phenomena was chosen because students had completed an introductory transport processes class)
- Extensive commented code and annotated notes are needed so students can treat code as boilerplate and modify it
#### Constraints
- Due to the introductory nature of the course, due care in terms of set-up and the design of learning activities during the course is essential

### Target Learners
- undergraduate engineering students with little Python experience

### Learning Goals
- numerical solution of PDEs
- concepts from numerical methods such as time stepping, stability, and coupling

### Claims
- [Fipy Short Course Improved Pde Self Efficacy](../claims/fipy-short-course-improved-pde-self-efficacy.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Pavan Inguva, Vijesh J. Bhute, Thomas N.H. Cheng, Pierre J. Walker. (2020). Introducing students to research codes: A short course on solving partial differential equations in Python. Preprint submitted to Education for Chemical Engineers. https://arxiv.org/abs/2008.10931
