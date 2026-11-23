---
type: design
id: parameter-choice-simulation-interface-pattern
title: Parameter-choice interface pattern for classroom simulation exercises
description: "The simulation exposes a small set of learner-chosen parameters through a friendly interface: the sample (each representing a different decay constant), the initial number of nuclides (small, medium, or large), the ti..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: ihab-f-riad-2005
    resource: "https://arxiv.org/abs/physics/0512274"
    title: "Ihab F. Riad, Mohammed El Shazali Sir Elkatim. (2005). A radioactive decay simulation (for Education). arXiv. https://arxiv.org/abs/physics/0512274"
    author: Ihab F. Riad, Mohammed El Shazali Sir Elkatim
---

# Parameter-choice interface pattern for classroom simulation exercises

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The simulation exposes a small set of learner-chosen parameters through a friendly interface: the sample (each representing a different decay constant), the initial number of nuclides (small, medium, or large), the time step, and the number of trials up to a thousand. Each trial's result is recorded to a .txt file of the user's choice, so learners can run repeated trials and analyse the exported data themselves.

## Design Implications

### Context
#### Requirements
- an interface module (Labview) over the simulation script so learners can make choices and start runs
#### Constraints
- The initial-nuclide choices were made for the limited computational power of the system used

### Target Learners
- school and undergraduate physics students

### Learning Goals
- designing and running repeated statistical trials
- estimating physical constants from simulated data

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Ihab F. Riad, Mohammed El Shazali Sir Elkatim. (2005). A radioactive decay simulation (for Education). arXiv. https://arxiv.org/abs/physics/0512274
