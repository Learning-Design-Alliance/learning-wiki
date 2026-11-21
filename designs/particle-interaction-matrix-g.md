---
type: design
id: particle-interaction-matrix-g
title: Interaction matrix G encoding type-pair forces, including asymmetric relations
description: "A T×T matrix whose element Gij defines the interaction force between particle types: positive values attract, negative values repel, and zero leaves only short-range repulsion."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: dr-hernández-rodríguez-2025
    resource: "https://arxiv.org/abs/2503.07659"
    title: "Dr. Hernández Rodríguez, Matías Ezequiel. (2025). Desarrollo de competencias STEM mediante la programación de modelos de auto-organización. arXiv:2503.07659 [physics.ed-ph]. https://arxiv.org/abs/2503.07659"
    author: Dr. Hernández Rodríguez, Matías Ezequiel
---

# Interaction matrix G encoding type-pair forces, including asymmetric relations

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A T×T matrix whose element Gij defines the interaction force between particle types: positive values attract, negative values repel, and zero leaves only short-range repulsion. The article stresses that "La matriz no necesita ser sim´ etrica, permitiendo a los estudiantes modelar relaciones asim´ etri- cas, como depredador-presa o par´ asito-hu´ esped". Students generate random matrices to observe diverse emergent behaviors, design matrices for desired behaviors such as grouping, segregation or pursuit, and analyze how matrix structure relates to resulting patterns.

## Design Implications

### Context
#### Requirements
- In the didactic implementation, matrix values lie between −1 and 1, representing the intensity of the attraction or repulsion force between types.
#### Constraints
- A zero element leaves no specific interaction between the two types beyond short-distance repulsion.

### Target Learners
- advanced secondary students
- higher education students

### Learning Goals
- linear algebra and matrix representation
- design of rule-based systems for specific behaviors
- analysis of emergent patterns

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Dr. Hernández Rodríguez, Matías Ezequiel. (2025). Desarrollo de competencias STEM mediante la programación de modelos de auto-organización. arXiv:2503.07659 [physics.ed-ph]. https://arxiv.org/abs/2503.07659
