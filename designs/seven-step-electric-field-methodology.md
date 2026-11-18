---
type: design
id: seven-step-electric-field-methodology
title: Seven-step algorithmic methodology for solving electric-field problems independent of charge positions
description: "The article defines a general solution strategy for electric-field problems: after board-class discussion, \"an algorithm or strategy to provide the solution on 7 steps was defined, independently from electric charges..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: k-l-cristiano-2019
    resource: "https://arxiv.org/abs/1901.08670"
    title: "K L Cristiano, D A Triana, A. Estupiñán. (2019). Python script used as simulator for the teaching of electric field in electromagnetism course. https://arxiv.org/abs/1901.08670"
    author: K L Cristiano, D A Triana, A. Estupiñán
---

# Seven-step algorithmic methodology for solving electric-field problems independent of charge positions

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article defines a general solution strategy for electric-field problems: after board-class discussion, "an algorithm or strategy to provide the solution on 7 steps was defined, independently from electric charges position on the space". The steps are: define the reference system in rectangular coordinates; draw position vectors of charges and of the field point; compute relative position vectors; find their magnitudes; find unit vectors; apply Coulomb's law to each charge; and combine by superposition. The Python method was written to include these steps.

## Design Implications

### Context
#### Requirements
- board class discussion to generate discussion about the appropriate way to solve electric-field problems
- vector analysis with rectangular coordinates, which the authors say is more intuitive for students
#### Constraints
- the methodology is stated to be independent of the charges' positions in space, but is developed for point charges

### Target Learners
- university electromagnetism students

### Learning Goals
- solving electric-field problems systematically
- combining vector analysis with the physics description of the electric field

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- K L Cristiano, D A Triana, A. Estupiñán. (2019). Python script used as simulator for the teaching of electric field in electromagnetism course. https://arxiv.org/abs/1901.08670
