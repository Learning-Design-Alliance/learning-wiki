---
type: design
id: hybrid-physical-virtual-simulation-design
title: "Hybrid physical–virtual simulation design: physical anatomy constrains realistic trajectories while virtual models provide patient-specific, repeatable clipping and objective assessment"
description: "The article's organizing design account is that physical components (3D-printed skull, silicone brain lobes) provide realistic haptic boundaries — \"restricting trajectories to achievable real-world scenarios\" — while..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
sources:
  - id: gmeiner-m-2025
    resource: "https://doi.org/10.1007/s10143-025-03846-x"
    title: "Gmeiner M, Schrempf A, Thurner T, Fenz W, Sabrowsky-Hirsch B, Giretzlehner M, Prückl R, Schaffelhofer S, Major Z, Lämmermann S, Baumgartner M, Drabauer L, Nagy J, Esposito G, Colombo E, Stroh-Holly N, Gruber A. (2025). Development and external validation of a mixed-reality aneurysm clipping simulator. Neurosurgical Review. https://doi.org/10.1007/s10143-025-03846-x"
    author: Gmeiner M, Schrempf A, Thurner T, Fenz W, Sabrowsky-Hirsch B, Giretzlehner M, Prückl R, Schaffelhofer S, Major Z, Lämmermann S, Baumgartner M, Drabauer L, Nagy J, Esposito G, Colombo E, Stroh-Holly N, Gruber A
---

# Hybrid physical–virtual simulation design: physical anatomy constrains realistic trajectories while virtual models provide patient-specific, repeatable clipping and objective assessment

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's organizing design account is that physical components (3D-printed skull, silicone brain lobes) provide realistic haptic boundaries — "restricting trajectories to achievable real-world scenarios" — while virtual components allow patient-specific models, non-destructive interaction, and unlimited training iterations. Accurate real-time synchronization between the two realities via optical tracking is described as essential for a realistic simulation experience, and the virtual blood flow calculation permits objective assessment of the chosen clipping strategy.

## Design Implications

### Context
#### Requirements
- Accurate real-time synchronization and reliable registration of all physical components with their virtual counterparts
#### Constraints
- Purely virtual simulations might permit unrealistic clip trajectories, which the physical brain lobes and rigid skull constrain
- Achieving precise temporal and spatial synchronization is technically demanding

### Target Learners
- neurosurgery residents
- neurosurgeons

### Learning Goals
- surgical trajectory planning
- clip application
- clipping strategy assessment

### Claims
- [Medusa Blood Flow Simulation Highest Rated](../claims/medusa-blood-flow-simulation-highest-rated.md) [+M]

## Related Designs
- Medusa Mixed Reality Clipping Simulator

## Examples
-

## Key Sources
- Gmeiner M, Schrempf A, Thurner T, Fenz W, Sabrowsky-Hirsch B, Giretzlehner M, Prückl R, Schaffelhofer S, Major Z, Lämmermann S, Baumgartner M, Drabauer L, Nagy J, Esposito G, Colombo E, Stroh-Holly N, Gruber A. (2025). Development and external validation of a mixed-reality aneurysm clipping simulator. Neurosurgical Review. https://doi.org/10.1007/s10143-025-03846-x
