---
type: design
id: square-koch-fractal-drum-numerical-experiment
title: Square Koch fractal drum numerical experiment for computational physics students
description: A numerical experiment in which students construct a square Koch pre-fractal drum, discretize the Helmholtz equation with a five-point stencil, classify lattice points as internal, external, or boundary, build and sol...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: veronica-p-simonsen-2023
    resource: "https://arxiv.org/abs/2309.13613"
    title: "Veronica P. Simonsen, Nathan Hale, and Ingve Simonsen. (2023). Eigenmodes of fractal drums: A numerical student experiment. https://arxiv.org/abs/2309.13613"
    author: Veronica P. Simonsen, Nathan Hale, and Ingve Simonsen
---

# Square Koch fractal drum numerical experiment for computational physics students

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A numerical experiment in which students construct a square Koch pre-fractal drum, discretize the Helmholtz equation with a five-point stencil, classify lattice points as internal, external, or boundary, build and solve a sparse eigensystem, and visualize the eigenmodes. At generation level ℓ = 4 the eigensystem has M4 = 57 345 internal lattice points and is over 99.9% sparse; "The calculation of the first 21 eigenmodes of the square Koch drum took only a few minutes on a typical desktop computer". It was used in the Computational Physics course at NTNU and is suitable for introductory or upper-level courses.

## Design Implications

### Context
#### Requirements
- Students must generate the fractal structure, map the unorganized portion of a matrix of unknowns into a vector for the eigensolver, and define the associated coefficient matrix
- Sparse matrix eigensolvers are needed for higher generation levels, since students typically lack memory for dense storage when ℓ ≥ 4
#### Constraints
- Drums used are technically pre-fractals at finite generation level ℓ, not true fractals
- Dense matrix storage is infeasible on typical student laptops for ℓ ≥ 4; sparse storage is needed until ℓ ≥ 6

### Target Learners
- advanced undergraduate physics students

### Learning Goals
- understanding vibrations and eigenmodes of fractal drums
- numerical solution of large eigenvalue problems
- scientific numerical modeling and software engineering skills

### Claims
- Fractal Drum Fundamental Frequency Ratio 2 1225 [+M]
- Square Koch Drum Eigenmode Degeneracy [+M]
- Fractal Drum Eigenmode Rotational Symmetry [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Veronica P. Simonsen, Nathan Hale, and Ingve Simonsen. (2023). Eigenmodes of fractal drums: A numerical student experiment. https://arxiv.org/abs/2309.13613
