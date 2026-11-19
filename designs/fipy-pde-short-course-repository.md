---
type: design
id: fipy-pde-short-course-repository
title: FiPy PDE solver short course with publicly released notes and code repository
description: A two-session (two three-hour sessions over two days) remote short course introducing FiPy, an open-source finite-volume PDE solver in Python, to students with minimal coding experience.
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

# FiPy PDE solver short course with publicly released notes and code repository

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A two-session (two three-hour sessions over two days) remote short course introducing FiPy, an open-source finite-volume PDE solver in Python, to students with minimal coding experience. It includes a pre-course setup guide (Anaconda, Spyder IDE), four exercises, and ParaView post-processing in exercise 4. "All the course notes and code can be found at the following repository: https://github.com/pavaninguva/pde-Solver-Course". The authors state the extensive course notes and all code used in the course will be made publicly available, and intend to integrate parts into a second-year Engineering Mathematics module.

## Design Implications

### Context
#### Requirements
- A detailed step-by-step pre-course document for environment setup
- All code written with extensive comments explaining each line
#### Constraints
- The simulations of the modified Cahn–Hilliard equation tend to diverge at certain parameter values; for the symmetric system the article reports the simulation typically diverges at NAχAB ≥ ~6

### Target Learners
- second-year undergraduate chemical engineering students

### Learning Goals
- numerically solving PDEs in Python
- understanding concepts used in numerical analysis and PDEs

### Claims
- [Fipy Short Course Improved Pde Self Efficacy](../claims/fipy-short-course-improved-pde-self-efficacy.md) [+M]
- [Pde Visualisation Most Valued By Students](../claims/pde-visualisation-most-valued-by-students.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Pavan Inguva, Vijesh J. Bhute, Thomas N.H. Cheng, Pierre J. Walker. (2020). Introducing students to research codes: A short course on solving partial differential equations in Python. Preprint submitted to Education for Chemical Engineers. https://arxiv.org/abs/2008.10931
