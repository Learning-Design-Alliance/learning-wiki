---
type: strategy
id: simulated-data-mode-remote-lab-participation
title: Incorporating simulated-data analysis into lab software to enable remote participation
description: "When physical lab access is impossible, add a simulation mode to the lab's analysis software so students can generate realistic quadrature datasets and complete the same reconstruction activity remotely."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: juan-rafael-álvarez-2023
    resource: "https://arxiv.org/abs/2310.17525"
    title: "Juan Rafael Álvarez, Andrés Martínez Silva, Alejandra Valencia. (2023). Measuring Wigner functions of quantum states of light in the undergraduate laboratory. arXiv. https://arxiv.org/abs/2310.17525"
    author: Juan Rafael Álvarez, Andrés Martínez Silva, Alejandra Valencia
---

# Incorporating simulated-data analysis into lab software to enable remote participation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
When physical lab access is impossible, add a simulation mode to the lab's analysis software so students can generate realistic quadrature datasets and complete the same reconstruction activity remotely. The article states the simulation feature "was introduced due to COVID restrictions that forbade student access to the laboratory," and that simulations "can be used to emulate the measurement of more exotic states of light which are not experimentally feasible to achieve in an educational laboratory with a HeNe laser." The virtual part also opens possibilities for distance learning beyond the emergency context.

## Design Implications

### Context
#### Requirements
- Analysis software that accepts formatted marginal-distribution input, whether measured or simulated
#### Constraints
- Simulated data does not include real experimental noise and detector imperfections, which future detector characterization would help students interpret

### Target Learners
- undergraduate and early graduate physics students in virtual or distance courses

### Target Learning Goals
- reconstructing Wigner functions of quantum states, including states not experimentally accessible in an educational lab

## Claims

- [Remote students reconstructed more exotic quantum states, including single-photon states and squeezed vacuum, from simulated data](../claims/remote-students-simulated-exotic-state-reconstruction.md) [+W]
- [The authors report the activity's virtual component proved highly valuable for distance learning in quantum optics](../claims/virtual-component-valuable-distance-learning-quantum-optics.md) [+W]

## Related Strategies

- [Future iterations should add maximum-likelihood reconstruction and detector characterization](maximum-likelihood-and-detector-characterization-improvements.md)
- [Provide remote students with sample data, video lecture, and virtual walkthrough when in-person access is impossible](remote-lab-sample-data-substitute-strategy.md)
- [Sequence learning from literature, through simulation, to authentication via real remote experiments](simulate-then-authenticate-with-remote-experiment.md)

## Examples
-

## Key Sources
- Juan Rafael Álvarez, Andrés Martínez Silva, Alejandra Valencia. (2023). Measuring Wigner functions of quantum states of light in the undergraduate laboratory. arXiv. https://arxiv.org/abs/2310.17525
