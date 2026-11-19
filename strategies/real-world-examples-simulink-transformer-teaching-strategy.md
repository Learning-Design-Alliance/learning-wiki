---
type: strategy
id: real-world-examples-simulink-transformer-teaching-strategy
title: Use real-world application examples with Matlab/Simulink simulations to teach transformer behavior
description: The article recommends grounding the magnetic-circuit derivation of the transformer model in real-world application examples, each analyzed theoretically and then verified by simulation.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: saeed-lotfifard-2020
    resource: "https://arxiv.org/abs/2103.17257"
    title: "Saeed Lotfifard, Senior Member, IEEE. (2020). Teaching Electrical Model of Power Transformers to Undergraduate Students: Magnetic Circuit Approach. s.lotfifard@wsu.edu. https://arxiv.org/abs/2103.17257"
    author: Saeed Lotfifard, Senior Member, IEEE
---

# Use real-world application examples with Matlab/Simulink simulations to teach transformer behavior

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends grounding the magnetic-circuit derivation of the transformer model in real-world application examples, each analyzed theoretically and then verified by simulation. It states that 'Three examples are provided that explain how the behavior of power transformers can be explained in real-world applications using magnetic circuits' and that 'Simulation results using Matlab/Simulink, which is a widely available software for studying electrical circuits [12], are also presented.' The examples cover open-secondary current transformers, winding resistance measurement, and peaking transformers.

## Design Implications

### Context
#### Requirements
- Access to Matlab/Simulink, described as 'a widely available software for studying electrical circuits'
- Realistic transformer parameters (turn ratios, winding resistances, B-H characteristics) for the examples
#### Constraints
- The simulations simplify by ignoring the hysteresis loop in Examples 1 and 3, and Example 2's source is set for implementation simplicity

### Target Learners
- undergraduate power engineering students

### Target Learning Goals
- applying transformer electrical models to real-world scenarios
- understanding the impact of core B-H curve nonlinearity on transformer response

### Affordances
- [Unified Magnetic Circuit Transformer Model Teaching](../designs/unified-magnetic-circuit-transformer-model-teaching.md)

## Related Strategies

- [Combine low-fidelity theoretical training with high-fidelity real-world application to prepare teams for complex tasks.](combine-low-and-high-fidelity-sbt.md)
- [Use representative optical system simulations alongside geometric and physical optics to teach Fourier optics](representative-optical-simulations-teaching-strategy.md)
- [Use dusty plasma images and DC glow discharge time-series data to teach image processing and time-series data analysis techniques with ImageJ, MATLAB, and Python](dusty-plasma-image-time-series-analysis-learning.md)

## Examples
-

## Key Sources
- Saeed Lotfifard, Senior Member, IEEE. (2020). Teaching Electrical Model of Power Transformers to Undergraduate Students: Magnetic Circuit Approach. s.lotfifard@wsu.edu. https://arxiv.org/abs/2103.17257
