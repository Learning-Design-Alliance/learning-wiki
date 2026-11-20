---
type: design
id: clapeyron-jl-computational-thermodynamics-short-course
title: Openly available short course on computational thermodynamics built on Clapeyron.jl and Pluto.jl notebooks
description: A three-section short course introducing computational thermodynamics to advanced undergraduate and graduate students, built on the open-source Julia package Clapeyron.jl and delivered through reactive Pluto notebooks...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: luc-t-paoli-2023
    resource: "https://arxiv.org/abs/2310.13234"
    title: "Luc T. Paoli, Pavan K. Inguva, Andrew J. Haslam, and Pierre J. Walker. (2023). Confronting the thermodynamics knowledge gap: A short course on computational thermodynamics in Julia. https://arxiv.org/abs/2310.13234"
    author: Luc T. Paoli, Pavan K. Inguva, Andrew J. Haslam, and Pierre J. Walker
---

# Openly available short course on computational thermodynamics built on Clapeyron.jl and Pluto.jl notebooks

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A three-section short course introducing computational thermodynamics to advanced undergraduate and graduate students, built on the open-source Julia package Clapeyron.jl and delivered through reactive Pluto notebooks integrating lecture text and code. The course covers fundamentals, implementing thermodynamic models (ideal-gas, activity-coefficient, cubic, SAFT, and empirical equations of state), and deployment methods (volume solvers, saturation solvers, stability analysis, flash algorithms). All course notes and code are openly available: "All the course notes and code can be found at the following repository: https://github.com/ClapeyronThermo/introduction-to-computational-thermodynamics".

## Design Implications

### Context
#### Requirements
- Students should already be familiar with thermodynamics fundamentals and some thermodynamic models, with the first course section providing a refresher; only minimal coding is required of students
#### Constraints
- The course was designed to be modular so self-directed learners and educators can adapt specific components for their own needs

### Target Learners
- advanced undergraduate students
- graduate students
- self-directed learners

### Learning Goals
- computational thermodynamics
- implementing and deploying thermodynamic models
- numerical methods for thermodynamic problems

### Claims
- [Progression Principle Well Received](../claims/progression-principle-well-received.md) [+M]
- [Computational Thermodynamics Course Confidence Increase](../claims/computational-thermodynamics-course-confidence-increase.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Luc T. Paoli, Pavan K. Inguva, Andrew J. Haslam, and Pierre J. Walker. (2023). Confronting the thermodynamics knowledge gap: A short course on computational thermodynamics in Julia. https://arxiv.org/abs/2310.13234
