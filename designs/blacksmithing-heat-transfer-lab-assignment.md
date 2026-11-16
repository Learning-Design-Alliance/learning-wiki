---
type: design
id: blacksmithing-heat-transfer-lab-assignment
title: Blacksmithing forge heat-transfer lab assignment for a calculus-based physics course
description: A lab/programming assignment in which students estimate the energy needed to heat an automotive leaf spring in a forge, compute the power input per unit area from the coals, and build a finite-difference VPython simul...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: nathan-moore-2009
    resource: "https://arxiv.org/abs/0904.3960"
    title: "Nathan Moore, Nicole Schoolmeesters. (2009). Computational Physics and Reality: Looking for Some Overlap at the Blacksmith Shop. https://arxiv.org/abs/0904.3960"
    author: Nathan Moore, Nicole Schoolmeesters
---

# Blacksmithing forge heat-transfer lab assignment for a calculus-based physics course

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A lab/programming assignment in which students estimate the energy needed to heat an automotive leaf spring in a forge, compute the power input per unit area from the coals, and build a finite-difference VPython simulation predicting the rod's surface temperature distribution after 15, 30, and 45 seconds of heating. At the forge, students measured temperatures at notched positions with an IR thermometer and observed the ferromagnetic/paramagnetic transition of iron at about 770°C using a magnet as a primitive thermometer. The student model used 48 chunks along the 12-inch axis with a timestep dt = 0.002 seconds.

## Design Implications

### Context
#### Requirements
- Students need prior exposure to programming, here via VPython exercises in the Matter and Interactions text
- A numerical heat-transfer scheme based on the heat equation, derived from calorimetry and heat conduction
- Access to a forge or equivalent heat source and an IR thermometer or magnet probe
#### Constraints
- The article notes the simulation took about 3 hours on a 2.16GHz MacBook to simulate 30 seconds of heating, and that material properties were held constant although they change with temperature

### Target Learners
- second-semester University Physics students, mainly engineering majors

### Learning Goals
- modeling energy flow in a real system
- estimating power density and uncertainty
- revising models against experimental data

### Claims
- [Simulation Overprediction Radiation Scheme Improves Fit](../claims/simulation-overprediction-radiation-scheme-improves-fit.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Nathan Moore, Nicole Schoolmeesters. (2009). Computational Physics and Reality: Looking for Some Overlap at the Blacksmith Shop. https://arxiv.org/abs/0904.3960
