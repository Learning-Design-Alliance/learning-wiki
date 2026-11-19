---
type: design
id: la-conga-remote-lab-network-element
title: LA-CoNGA remote laboratory network with SiPM/APD, scintillator and water-Cherenkov detector equipment accessed via SSH
description: A network of remote laboratories operated by partner UIS in Bucaramanga, Colombia, letting students perform online remote measurements.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: jesús-peña-rodríguez-and-luis-a-núñez-2022
    resource: "https://arxiv.org/abs/2201.02256"
    title: "Jesús Peña-Rodríguez and Luis A. Núñez. (2022). LA-CoNGA physics: an Open Science Collaboration in Advanced Physics between Latin-America and Europe. Talk at EPS-HEP2021. https://arxiv.org/abs/2201.02256"
    author: Jesús Peña-Rodríguez and Luis A. Núñez
---

# LA-CoNGA remote laboratory network with SiPM/APD, scintillator and water-Cherenkov detector equipment accessed via SSH

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A network of remote laboratories operated by partner UIS in Bucaramanga, Colombia, letting students perform online remote measurements. Per the article, "LA-CoNGA remote lab facilities are accessed by using SSH protocol": students remotely control acquisition parameters (gain, voltages, temperature), take data, and analyse it, emulating calibration, measuring and data-analysis stages of a high energy physics experiment. Local technical staff configured and maintained the functioning detectors.

## Design Implications

### Context
#### Requirements
- Local technical staff to configure and maintain the functioning detectors
- Lab-side management tasks including experiment scheduling, user authentication, user interfaces and usage statistics
#### Constraints
- Connectivity requirements were simplified to the minimum bandwidth that could operate remote labs during lockdown

### Target Learners
- graduate physics master's students in Latin-American partner universities

### Learning Goals
- experimental instrumentation skills in nuclear and particle physics detectors
- remote data acquisition and analysis

### Claims
- [La Conga Remote Labs Low Bandwidth Proof Of Concept](../claims/la-conga-remote-labs-low-bandwidth-proof-of-concept.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Jesús Peña-Rodríguez and Luis A. Núñez. (2022). LA-CoNGA physics: an Open Science Collaboration in Advanced Physics between Latin-America and Europe. Talk at EPS-HEP2021. https://arxiv.org/abs/2201.02256
