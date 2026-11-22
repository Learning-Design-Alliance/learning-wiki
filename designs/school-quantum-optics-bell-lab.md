---
type: design
id: school-quantum-optics-bell-lab
title: School quantum optics laboratory for polarization-entangled photon Bell tests
description: "A quantum optics laboratory installed inside the Liceo Scientifico \"M."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-22
sources:
  - id: carlini-2026
    resource: "https://arxiv.org/abs/2610.29834"
    title: "Carlini, A., Lanza, A., Monti, D., Soso, A., Losero, E., Mari, M., Oñate Orozco, M., Bondani, M. (2026). Teaching quantum mechanics in secondary schools: A qubit-first learning path to Bell's inequalities. arXiv. https://arxiv.org/abs/2610.29834"
    author: Carlini, A., Lanza, A., Monti, D., Soso, A., Losero, E., Mari, M., Oñate Orozco, M., Bondani, M
---

# School quantum optics laboratory for polarization-entangled photon Bell tests

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A quantum optics laboratory installed inside the Liceo Scientifico "M. L. King" in Genoa through a collaboration between CNR-IFN, INRIM researchers and school teachers, funded through the Italian PNRR, and later reproduced at the University of Insubria. Based on Beck's undergraduate experiments and Kwiat's two-crystal entanglement scheme, it uses a 405 nm pump laser, BBO crystal pairs for Type-I SPDC, polarizers, SPAD detectors and an FPGA with a LabView interface adapted from Beck to compute the CHSH parameter. The design uses two SPADs with polarizers instead of four SPADs with polarizing beam splitters, which "significantly reduces the costs of the experimental realization, which is an important aspect in a public school context."

## Design Implications

### Context
#### Requirements
- Instructor-performed initial alignment of the apparatus; students then perform optimization, measurement-basis selection, data acquisition and analysis
#### Constraints
- Loophole problems were not addressed, as outside the didactic scope; the two-SPAD design multiplies measurement time by four; the lab lacked air conditioning and optical-table isolation frames

### Target Learners
- upper-secondary school students
- in-service secondary-school physics teachers

### Learning Goals
- authentic experimental investigation of quantum entanglement and Bell-inequality violation
- statistical analysis and comparison of theory with measurement

### Claims
- [School Bell Test Chsh Violation](../claims/school-bell-test-chsh-violation.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Carlini, A., Lanza, A., Monti, D., Soso, A., Losero, E., Mari, M., Oñate Orozco, M., Bondani, M. (2026). Teaching quantum mechanics in secondary schools: A qubit-first learning path to Bell's inequalities. arXiv. https://arxiv.org/abs/2610.29834. [doi:10.21203/rs.3.rs-11352498/v1](https://doi.org/10.21203/rs.3.rs-11352498/v1)
