---
type: theory
title: The Legendre transform as an alternative encoding of the information in a function, forming a self-inverse conjugate pair
description: "The article frames a function as an encoding {F, x} relating a control parameter to a dependent value, and the Legendre transform as a second encoding {G, s} of the same information, where s is the derivative dF/dx."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: r-k-p-zia-2009
    resource: "https://arxiv.org/abs/0806.1147"
    title: "R. K. P. Zia, Edward F. Redish, and Susan R. McKay. (2009). Making Sense of the Legendre Transform. https://arxiv.org/abs/0806.1147"
    author: R. K. P. Zia, Edward F. Redish, and Susan R. McKay
---

# The Legendre transform as an alternative encoding of the information in a function, forming a self-inverse conjugate pair

> **Theory** · [All theories](index.md)

## Description
The article frames a function as an encoding {F, x} relating a control parameter to a dependent value, and the Legendre transform as a second encoding {G, s} of the same information, where s is the derivative dF/dx. It works only when the function is strictly convex and smooth and when the derivative is easier to measure or control than x itself. The authors write that the transform is its own inverse, displayed symmetrically as G(s) + F(x) = sx for a conjugate pair. This framework organizes their algebraic, geometric, and physical treatments.

## Design Implications

### Context
#### Requirements
- The function (or its negative) must be strictly convex and smooth so the slope is a one-to-one stand-in for the independent variable.
- It must be easier to measure, control, or think about the derivative of F than x itself.
#### Constraints
- If the restriction of convexity is relaxed, the statement that the transform is its own inverse must be revised; non-convex functions yield a multi-valued transform whose second transform is the convex hull.

### Target Learners
- upper-division undergraduate physics majors
- graduate physics students

### Target Learning Objectives
- understand the Legendre transform as a general mathematical tool
- connect Lagrangian and Hamiltonian formulations
- relate thermodynamic potentials

### Claims
- [Students Discomfort Legendre Transform General Tool](../claims/students-discomfort-legendre-transform-general-tool.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- R. K. P. Zia, Edward F. Redish, and Susan R. McKay. (2009). Making Sense of the Legendre Transform. https://arxiv.org/abs/0806.1147
