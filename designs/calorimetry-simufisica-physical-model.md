---
type: design
id: calorimetry-simufisica-physical-model
title: "Physical model of the calorimetry simulation: sensible heat, latent heat, and Newton's law of cooling"
description: The simulator implements a classical thermodynamic model.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: marco-p-m-de-souza-and-alex-b-siqueira-2025
    resource: "https://arxiv.org/abs/2506.03289"
    title: "Marco P. M. de Souza and Alex B. Siqueira. (2025). Exploring Heat Exchanges with the Calorimetry Simulator – SimuFísica®. https://arxiv.org/abs/2506.03289"
    author: Marco P. M. de Souza and Alex B. Siqueira
---

# Physical model of the calorimetry simulation: sensible heat, latent heat, and Newton's law of cooling

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The simulator implements a classical thermodynamic model. In Heating mode, temperature rises linearly under constant flame power via Q = m0cΔT and Q = PΔt until the boiling point, after which mass evaporates as mvap(t) = P(t − tE)/L. In Thermal Equilibrium mode, coupled ordinary differential equations based on Newton's law of cooling govern sphere–liquid exchange until boiling, when energy goes exclusively to vaporization. The article states that "Equations (8) and (9) describe the system dynamics in Thermal Equilibrium mode and allow the simulator to faithfully reproduce the heat exchange process, with and without phase change."

## Design Implications

### Context
#### Requirements
- Configurable physical parameters: initial temperature, mass, specific heat, boiling point, latent heat of vaporization, and (for the sphere) mass, specific heat, and initial temperature.
#### Constraints
- The heat transfer rate constant k is adopted as 1 cal/(g·°C·s) in the simulator; thermal losses and container heat capacity are neglected.

### Target Learners
- High school physics students
- Introductory undergraduate physics students

### Learning Goals
- Connecting mathematical models of heat transfer to simulated phenomena

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Marco P. M. de Souza and Alex B. Siqueira. (2025). Exploring Heat Exchanges with the Calorimetry Simulator – SimuFísica®. https://arxiv.org/abs/2506.03289
