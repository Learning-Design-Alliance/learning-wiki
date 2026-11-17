---
type: design
id: euler-cromer-iterative-motion-prediction-pattern
title: Iterative Euler-Cromer motion-prediction algorithm as the shared computational core across force and motion models
description: "The article teaches a four-step algorithm applied locally in space and time: compute the net force, update velocity with Newton's 2nd law, update position with the new velocity, and repeat."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: caballero-2012
    resource: "http://www.vpython.org/"
    title: "Caballero, M.D.; Burk, J.B.; Aiken, J.M.; Thoms, B.D.; Douglas, S.S.; Scanlon, E.M.; Schatz, M.F. (2012). Integrating Numerical Computation into the Modeling Instruction Curriculum. http://www.vpython.org/"
    author: Caballero, M.D.; Burk, J.B.; Aiken, J.M.; Thoms, B.D.; Douglas, S.S.; Scanlon, E.M.; Schatz, M.F
---

# Iterative Euler-Cromer motion-prediction algorithm as the shared computational core across force and motion models

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article teaches a four-step algorithm applied locally in space and time: compute the net force, update velocity with Newton's 2nd law, update position with the new velocity, and repeat. Formally this is "explicit (Euler-Cromer) numerical integration" of the equations of motion. Because the models differ only in net force and initial conditions, changing initial conditions or net force produces qualitatively different simulations, highlighting commonality among the no-forces, balanced-forces, and unbalanced-forces models.

## Design Implications

### Context
#### Requirements
- Knowledge of the system's initial position and velocity and the net force on the system
- A computer to handle the labor-intensive iterative calculations
#### Constraints
- 

### Target Learners
- high school physics students in algebra-based or calculus-based courses

### Learning Goals
- predicting motion using Newton's second law and kinematics
- generalizing across force and motion models

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Caballero, M.D.; Burk, J.B.; Aiken, J.M.; Thoms, B.D.; Douglas, S.S.; Scanlon, E.M.; Schatz, M.F. (2012). Integrating Numerical Computation into the Modeling Instruction Curriculum. http://www.vpython.org/. [doi:10.48550/arxiv.1207.0844](https://doi.org/10.48550/arxiv.1207.0844)
