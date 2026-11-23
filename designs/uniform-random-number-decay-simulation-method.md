---
type: design
id: uniform-random-number-decay-simulation-method
title: Uniform random-number method for simulating radioactive decay
description: The simulation method generates as many uniform random numbers as there are nuclides, each number representing a potential decaying nuclide.
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

# Uniform random-number method for simulating radioactive decay

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The simulation method generates as many uniform random numbers as there are nuclides, each number representing a potential decaying nuclide. From the uniform distribution the authors derive that any uniform random number greater than the threshold x0 = 1 - λΔt represents a decaying nuclide, so each generated number is checked against this condition to identify it as non-decaying or decaying and counted accordingly. The time step is controlled through the Labview interface.

## Design Implications

### Context
#### Requirements
- a uniform random number generator, as available through Matlab
#### Constraints
- 

### Target Learners
- undergraduate physics students

### Learning Goals
- connecting probability and statistics to physical decay processes

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Ihab F. Riad, Mohammed El Shazali Sir Elkatim. (2005). A radioactive decay simulation (for Education). arXiv. https://arxiv.org/abs/physics/0512274
