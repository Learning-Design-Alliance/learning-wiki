---
type: strategy
id: local-deployment-flash-drive-pypi-distribution
title: Local deployment via PyPI installation or flash-drive distribution for regions with limited internet
description: To make the materials accessible where internet is slow or geographically limited, the authors recommend two offline distribution routes.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: gehua-tong-2022
    resource: "https://github.com/imr-framework/vs-tabletop"
    title: "Gehua Tong, Rishi Ananth, John Thomas Vaughan, Jr., Sairam Geethanath. (2022). Virtual Scanner Games: expanding access to Magnetic Resonance (MR) education through interactive web tutorials. https://github.com/imr-framework/vs-tabletop"
    author: Gehua Tong, Rishi Ananth, John Thomas Vaughan, Jr., Sairam Geethanath
---

# Local deployment via PyPI installation or flash-drive distribution for regions with limited internet

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
To make the materials accessible where internet is slow or geographically limited, the authors recommend two offline distribution routes. As printed: "Currently, local usage of Virtual Scanner Games is possible by installing through the PyPI index and copies of the codebase may be made and distributed with physical flash drives." Where central internet access exists, such as in schools and universities, students can use the hosted web application flexibly without installation.

## Design Implications

### Context
#### Requirements
- Local installation currently requires resolving Python versions and library dependencies
#### Constraints
- The flash-drive/PyPI procedure "can pose problems with Python versions and library dependencies and should be further optimized"

### Target Learners
- students in regions with limited or slow internet connectivity
- high schools and universities with central internet access

### Target Learning Goals
- access MRI education materials without reliable personal internet connectivity

## Claims

- [Students with low internet bandwidth could complete the course when offered offline video download and batch mode alternatives](../claims/low-bandwidth-mitigation-strategies.md) [+W]

## Related Strategies

- [Offer three free deployment routes (mybinder.org, dokku, institutional JupyterHub) matched to user needs](three-free-deployment-routes-notebooks.md)
- [Three solutions for data costs in mobile learning: avoid data, batch data, and transfer data locally](data-cost-mitigation-three-solutions.md)
- [Deploy quantized adapted small models offline with a teacher in the loop rather than as autonomous graders](teacher-in-the-loop-offline-small-model-deployment.md)
- [Platform Agnostic Design](platform_agnostic_design.md)

## Examples
-

## Key Sources
- Gehua Tong, Rishi Ananth, John Thomas Vaughan, Jr., Sairam Geethanath. (2022). Virtual Scanner Games: expanding access to Magnetic Resonance (MR) education through interactive web tutorials. https://github.com/imr-framework/vs-tabletop
