---
type: strategy
id: euler-method-spreadsheet-strategy-nonlinear-oscillator
title: Have students implement the Euler method in a spreadsheet to numerically solve a nonlinear equation of motion
description: "The article recommends having students numerically solve a nonlinear differential equation of motion with the Euler method programmed in a spreadsheet such as Excel: dividing the total time into steps, assuming consta..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: suárez-2019
    resource: "https://arxiv.org/abs/1903.11934"
    title: "Suárez, A. & Tornaría, F. (2019). Using the Euler method in a spreadsheet to study a nonlinear oscillator. Revista Mexicana de Física E. https://arxiv.org/abs/1903.11934"
    author: "Suárez, A. & Tornaría, F"
---

# Have students implement the Euler method in a spreadsheet to numerically solve a nonlinear equation of motion

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends having students numerically solve a nonlinear differential equation of motion with the Euler method programmed in a spreadsheet such as Excel: dividing the total time into steps, assuming constant acceleration within each step to update velocity, then constant velocity to update position, and iterating. The spreadsheet "facilita la implementación del algoritmo de Euler por parte de los estudiantes, aunque no posean conocimientos avanzados de programación", and lets them compare model predictions with experimental data and observe the effect of manually varying each parameter.

## Design Implications

### Context
#### Requirements
- Knowledge of the initial conditions of the motion and of the force terms in the equation of motion
- A spreadsheet application; no advanced programming knowledge required
#### Constraints
- The Euler method is not the most efficient solver; accuracy improves only partially by reducing the step size, which increases computation and rounding error, and results are reasonably good only for time intervals that are not very large

### Target Learners
- first-year university experimental physics students

### Target Learning Goals
- understanding that not all problems have an exact analytical solution
- learning numerical methods for differential equations
- comparing model predictions with experimental data

## Related Strategies

- [Use simple spreadsheet-based numerical simulation of orbital systems as an engaging team-based learning activity](spreadsheet-numerical-simulation-team-learning-strategy.md)
- [Guided Google Sheets laboratory exercise in which first-year physics students iteratively implement the Euler-method approximation](google-sheets-euler-iteration-lab.md)

## Examples
-

## Key Sources
- Suárez, A. & Tornaría, F. (2019). Using the Euler method in a spreadsheet to study a nonlinear oscillator. Revista Mexicana de Física E. https://arxiv.org/abs/1903.11934
