---
type: strategy
id: md-bonds-and-anchoring-enhancements
title: Extend basic molecular dynamics simulations with elastic bonds and anchored atoms for demonstrations beyond the pure Lennard-Jones system
description: Section VII describes enhancements that go beyond the pure Lennard-Jones system.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: daniel-v-schroeder-2015
    resource: "https://doi.org/10.1119/1.4901185"
    title: "Daniel V. Schroeder. (2015). Interactive molecular dynamics. Am. J. Phys. 83 (3), 210–218. https://doi.org/10.1119/1.4901185"
    author: Daniel V. Schroeder
---

# Extend basic molecular dynamics simulations with elastic bonds and anchored atoms for demonstrations beyond the pure Lennard-Jones system

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Section VII describes enhancements that go beyond the pure Lennard-Jones system. The accompanying software "allows the user to connect any two atoms together with an elastic "bond" that adds a spring-like force to the Lennard-Jones force," and can anchor an atom so it is fixed in space, enabling barriers and nano-scale machinery such as a Brownian ratchet. These crude bonds enable demonstrations such as measuring the heat capacity of a diatomic gas, watching Brownian motion of a large object bombarded by fast atoms, and observing friction between sliding solids.

## Design Implications

### Context
#### Requirements
- A simulation that adds a spring-like bond force to the Lennard-Jones force and supports anchoring atoms at fixed locations
#### Constraints
- The bond feature is not an accurate model of actual covalent bonds: there is no limit on the number of bonds per atom, no constraints on bond angles, and the bond stiffness is unrealistically low for computational reasons

### Target Learners
- undergraduate physics students

### Target Learning Goals
- diatomic gas heat capacity including vibrational potential energy
- Brownian motion
- friction
- how the nano-scale world differs from the macroscopic world

## Claims

- [Interactive Lennard-Jones simulations can demonstrate equilibrium phases, nonequilibrium evolution, and the arrow of time to students](../claims/md-simulations-demonstrate-equilibrium-nonequilibrium.md) [+W]
- [Two-dimensional molecular dynamics simulations with fixed-wall boundary conditions are preferable for many educational purposes](../claims/two-dimensional-md-preferred-education.md) [+W]

## Related Strategies

- [Use an interactive gas simulation to demonstrate statistical thermodynamics concepts without formal formulae](gas-simulation-statistical-concepts-strategy.md)

## Examples
-

## Key Sources
- Daniel V. Schroeder. (2015). Interactive molecular dynamics. Am. J. Phys. 83 (3), 210–218. https://doi.org/10.1119/1.4901185
