---
type: design
id: pyro-clarity-first-learning-by-modification
title: "Learning-by-code-modification: a simple, clarity-first codebase as the vehicle for learning computational methods"
description: "The article's pedagogical framework holds that \"the best way to learn computational methods for hydrodynamics is to code them up yourself, or to make substantial modifications to the internals of existing code\", and t..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: zingale-2014
    resource: "https://arxiv.org/abs/1306.6883"
    title: "Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. https://arxiv.org/abs/1306.6883"
    author: Zingale, M
---

# Learning-by-code-modification: a simple, clarity-first codebase as the vehicle for learning computational methods

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's pedagogical framework holds that "the best way to learn computational methods for hydrodynamics is to code them up yourself, or to make substantial modifications to the internals of existing code", and that for this "it helps to have a simple code as a starting point". pyro operationalizes this by choosing "a single method representative of those used in astrophysics" and stating that "Given the choice between clarity and performance, we take clarity", leaving variations and enhancements as exercises for students. Where NumPy slice-notation would hide the differencing from inspection, kernels are implemented in Fortran under a self-containment design rule.

## Design Implications

### Context
#### Requirements
- A simple code as a starting point with internals students can substantially modify; accompanying detailed lecture notes explaining the core methods
#### Constraints
- Clarity is favored over performance and breadth of options, which are the goals of production codes rather than teaching codes

### Target Learners
- astrophysics graduate students
- undergraduate researchers new to computational methods

### Learning Goals
- understanding the internals of finite-volume hydrodynamics solvers
- hands-on experience with numerical PDE methods

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. https://arxiv.org/abs/1306.6883
