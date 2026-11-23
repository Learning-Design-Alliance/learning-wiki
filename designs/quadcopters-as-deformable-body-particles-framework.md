---
type: design
id: quadcopters-as-deformable-body-particles-framework
title: Quadcopters-as-particles continuum deformation framework for demonstrating linear deformation, principal strains, and shear strains
description: The framework treats a team of N quadcopters as particles of a deformable body whose desired positions follow a homogeneous linear transformation r_i(t) = E(t) r_i0, where E(t) is a positive definite strain matrix spe...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: harshvardhan-uppaluru-and-hossein-rastgoftar-2022
    resource: "https://arxiv.org/abs/2201.08004"
    title: "Harshvardhan Uppaluru and Hossein Rastgoftar. (2022). Drones Practicing Mechanics. https://arxiv.org/abs/2201.08004"
    author: Harshvardhan Uppaluru and Hossein Rastgoftar
---

# Quadcopters-as-particles continuum deformation framework for demonstrating linear deformation, principal strains, and shear strains

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The framework treats a team of N quadcopters as particles of a deformable body whose desired positions follow a homogeneous linear transformation r_i(t) = E(t) r_i0, where E(t) is a positive definite strain matrix specifying axial strains and shear deformation angles. Because quadcopters are rigid rather than infinitesimal, realization of linear deformation requires constraining the lower bound of the principal strains (eigenvalues of E) so that "quadcopters, treated as particles of a deformable body, are rigid and cannot deform" without collision. The article uses this framework to plan and experimentally demonstrate deformation of a drone team in a 3-D motion space.

## Design Implications

### Context
#### Requirements
- Assumption that the material configuration equals the initial configuration and d(t0) = 0, so E(t0) = I3
- Every quadcopter can be enclosed by a ball of radius r and its trajectory tracking error is less than δ
#### Constraints
- Realization focuses on pure deformation: rigid-body displacement and rotation are both set to zero at any time

### Target Learners
- junior undergraduate engineering students

### Learning Goals
- strain and stress analysis
- axial and shear deformation
- continuum mechanics concepts

### Claims
- Quadcopter 2D Continuum Deformation Collision Avoidance [+M]
- Quadcopter 3D Continuum Deformation Collision Avoidance [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Harshvardhan Uppaluru and Hossein Rastgoftar. (2022). Drones Practicing Mechanics. https://arxiv.org/abs/2201.08004
