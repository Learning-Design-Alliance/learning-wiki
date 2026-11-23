---
type: strategy
id: ibm-quantum-experience-classroom-experiments-strategy
title: Use the free cloud-accessible IBM quantum computers to run simple classroom experiments illustrating nonclassical features of quantum mechanics
description: "The article recommends that teachers use IBM quantum experience — quantum computers \"placed in the cloud and can be accessed freely from your class room\" via internet-connected devices — to let students experimentally..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: anirban-pathak-2018
    resource: "https://arxiv.org/abs/1805.06275"
    title: "Anirban Pathak. (2018). Experimental quantum mechanics in the class room: Testing basic ideas of quantum mechanics and quantum computing using IBM quantum computer. https://arxiv.org/abs/1805.06275"
    author: Anirban Pathak
---

# Use the free cloud-accessible IBM quantum computers to run simple classroom experiments illustrating nonclassical features of quantum mechanics

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that teachers use IBM quantum experience — quantum computers "placed in the cloud and can be accessed freely from your class room" via internet-connected devices — to let students experimentally test features of quantum mechanics that are otherwise taught purely theoretically, such as collapse on measurement, probabilistic outcomes, and entanglement. It provides step-by-step registration and Composer/QASM instructions, three worked experiments, and applications linking each experiment to real quantum technologies.

## Design Implications

### Context
#### Requirements
- Internet access in the classroom
- Registration for an IBM Q Experience account
- Familiarity with basic quantum mechanics and the gate library (Clifford group gates and T gate) available on the platform
#### Constraints
- Arbitrary gates cannot be implemented; only the platform's gate library is available
- CNOT application positions are restricted by each architecture's coupling map
- Jobs on real devices may be queued

### Target Learners
- undergraduate physics students
- students learning quantum computing

### Target Learning Goals
- understand wavefunction collapse and measurement probabilities
- understand superposition via interference
- understand entanglement and its applications

## Related Strategies

- [Measure arbitrary spin directions on quantum hardware by applying rotation gates that map the desired eigenvectors onto the computational basis](rotation-gate-basis-change-measurement-strategy.md)

## Examples
-

## Key Sources
- Anirban Pathak. (2018). Experimental quantum mechanics in the class room: Testing basic ideas of quantum mechanics and quantum computing using IBM quantum computer. https://arxiv.org/abs/1805.06275
