---
type: design
id: fractal-drum-computational-project-sequence
title: Fractal drum project as a structured computational modeling exercise sequence
description: "The project is organized as a sequence of computational tasks: constructing the fractal boundary, discretizing the domain so all corners fall on the lattice, classifying lattice points, assembling the sparse coefficie..."
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

# Fractal drum project as a structured computational modeling exercise sequence

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The project is organized as a sequence of computational tasks: constructing the fractal boundary, discretizing the domain so all corners fall on the lattice, classifying lattice points, assembling the sparse coefficient matrix, solving the eigensystem, and mapping eigenvectors back onto the lattice for visualization. The article states "The numerical experiment allows students to construct a fractal drum, calculate its eigenmodes, and visualize the vibrational modes. The students can change boundary conditions, vary certain dimensions, and observe the results." This gives students agency to explore variations after the core pipeline is built.

## Design Implications

### Context
#### Requirements
- Students must master mapping an unorganized portion of a matrix of unknowns into a vector and defining the associated sparse coefficient matrix
- Every portion of the code must be optimized to yield a solution within a realistic time span because the coefficient matrix is very large
#### Constraints
- The assignment is designed for integration into a computational physics class; the article does not claim transfer to other course formats

### Target Learners
- undergraduate physics students in introductory or upper-level courses

### Learning Goals
- eigenvalue problems larger than typically encountered in studies
- numerical modeling of physical systems
- visualization of computed modes

### Claims
- Square Koch Fractal Drum Numerical Experiment [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Veronica P. Simonsen, Nathan Hale, and Ingve Simonsen. (2023). Eigenmodes of fractal drums: A numerical student experiment. https://arxiv.org/abs/2309.13613
