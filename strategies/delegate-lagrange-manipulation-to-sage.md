---
type: strategy
id: delegate-lagrange-manipulation-to-sage
title: Delegate the mathematical manipulation of Lagrange equations to Sage so students focus on physical modeling
description: "For challenging problems such as the Wilberforce pendulum, students construct the Lagrangian from energy concepts while \"the mathematical manipulations, which are involved in formulating the Lagrange equations, can be..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: dominik-borovský-2023
    resource: "https://arxiv.org/abs/2308.07199"
    title: "Dominik Borovský, Jozef Hanč, and Martina Hančová. (2023). Scientific Computing with Open SageMath not only for Physics Education. https://arxiv.org/abs/2308.07199"
    author: Dominik Borovský, Jozef Hanč, and Martina Hančová
---

# Delegate the mathematical manipulation of Lagrange equations to Sage so students focus on physical modeling

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For challenging problems such as the Wilberforce pendulum, students construct the Lagrangian from energy concepts while "the mathematical manipulations, which are involved in formulating the Lagrange equations, can be left to Sage." The step is automated with a suitably created Python function (LagrangeEquations.sage) whose coding requires only basic novice Python knowledge, eliminating human-induced errors and allowing easy editing of results at any stage.

## Design Implications

### Context
#### Requirements
- Students able to describe the problem physically using classical energy concepts and construct the Lagrangian; a suitably created Python function for the equation derivation
#### Constraints
- A meaningful analytical solution of the motion equations is only obtainable under certain specific conditions; Sage additionally yields numerical solutions for general conditions

### Target Learners
- undergraduate physics students
- talented high school students with elementary single-variable calculus

### Target Learning Goals
- Lagrangian modeling of coupled oscillations
- symbolic and numerical solution of differential equations

## Related Strategies

- [Shift electrodynamics instruction toward interpretation of equations and graphical, qualitative exercises at the expense of algebraic manipulation](emphasize-interpretation-over-algebra-electrodynamics.md)
- [Automation and geodesic manipulation functions to shift learner focus from construction to physical significance](geodesic-automation-manipulation.md)

## Examples
-

## Key Sources
- Dominik Borovský, Jozef Hanč, and Martina Hančová. (2023). Scientific Computing with Open SageMath not only for Physics Education. https://arxiv.org/abs/2308.07199
