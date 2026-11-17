---
type: strategy
id: pyro-student-exploration-extensions
title: Per-solver student exploration exercises that modify or extend the solver to build deeper method understanding
description: "Each solver section closes with a set of open exercises the article frames as things \"students can perform to improve their understanding\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: zingale-2014
    resource: "https://arxiv.org/abs/1306.6883"
    title: "Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. https://arxiv.org/abs/1306.6883"
    author: Zingale, M
---

# Per-solver student exploration exercises that modify or extend the solver to build deeper method understanding

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Each solver section closes with a set of open exercises the article frames as things "students can perform to improve their understanding". Examples include comparing convergence with and without limiting, removing the transverse flux difference, implementing a dimensionally split advection version, adding passively advected species or a heating term, switching piecewise linear reconstruction to PPM, adding different Riemann solvers, running smoothing-only instead of multigrid, experimenting with bottom solvers, varying timesteps with discontinuous data, implementing a non-constant diffusion coefficient, and adding viscosity or a variable density system to the incompressible solver.

## Design Implications

### Context
#### Requirements
- Access to the pyro source code so students can modify solver internals and run the explorations
#### Constraints
- 

### Target Learners
- astrophysics graduate students
- new students to the field of computational astrophysics

### Target Learning Goals
- build deeper understanding of numerical methods for hyperbolic, elliptic, parabolic and incompressible systems

## Claims

- [The pyro compressible-hydrodynamics verification tests reproduce analytic reference solutions (Sod shock tube, Sedov-Taylor blast wave, single-mode Rayleigh-Taylor)](../claims/pyro-compressible-tests-match-analytic-solutions.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Zingale, M. (2014). pyro: A teaching code for computational astrophysical hydrodynamics. https://arxiv.org/abs/1306.6883. [doi:10.1016/j.ascom.2014.07.003](https://doi.org/10.1016/j.ascom.2014.07.003)
