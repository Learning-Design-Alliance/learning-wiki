---
type: design
id: escaramujo-cosmic-ray-detector
title: "Escaramujo cosmic ray detector: plastic scintillator plates read out by SiPMs with a QuarkNet DAQ card and Raspberry Pi"
description: "A modern, simple and cost-effective cosmic ray detector designed specifically for the courses, consisting of \"three plates of scintillator (EJ-200, Eljen Technology) coupled to SiPMs (MicroFC-60035-SMT, SensL)\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: federico-izraelevitch-2016
    resource: "https://arxiv.org/abs/1611.06205"
    title: "Federico Izraelevitch. (2016). The Escaramujo Project: instrumentation courses during a road trip across the Americas. Proceeding of the 38th International Conference on High Energy Physics. https://arxiv.org/abs/1611.06205"
    author: Federico Izraelevitch
---

# Escaramujo cosmic ray detector: plastic scintillator plates read out by SiPMs with a QuarkNet DAQ card and Raspberry Pi

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
A modern, simple and cost-effective cosmic ray detector designed specifically for the courses, consisting of "three plates of scintillator (EJ-200, Eljen Technology) coupled to SiPMs (MicroFC-60035-SMT, SensL)". Each 25 x 25 x 1 cm3 plate is read out by one SiPM coupled with adhesive tape and wrapped in Tyvek and black paper for light tightness. Readout uses a QuarkNet DAQ card version 6000 with a custom four-channel bias-T board for SiPM operation, connected via USB to a Raspberry Pi 2 Model B running Minicom; raw data is stored as plain text for analysis.

## Design Implications

### Context
#### Requirements
- Pre-tested electronic boards, cables and connectors prepared before shipping to minimize troubleshooting risk
- Local provision of a minimum of equipment such as an oscilloscope
#### Constraints
- Design was a trade-off: student assemblability, state-of-the-art technology, compactness for travel logistics, and simplicity and cost-effectiveness as "overarching principles"

### Target Learners
- advanced undergraduate and graduate STEM students

### Learning Goals
- hands-on detector construction
- detector characterization and operating-parameter optimization
- cosmic ray physics measurements

### Claims

- [After the courses, host sites sustained the project by running their own outreach, forming a data-sharing collaboration, and replicating the detector design](../claims/post-course-sites-sustain-escaramujo-network.md) [+W]
- [Building the threadbare DAQ card taught students the fundamentals of interfacing and enabled slow-event physics experiments](../claims/daq-card-taught-interfacing-fundamentals.md) [+W]

## Related Designs

- [Anthracene fluorescence module for Route.Net](anthracene-fluorescence-module-routenet.md)
- [HiSPARC school-based scintillator detection stations](hisparc-school-scintillator-stations.md)

## Examples
-

## Key Sources
- Federico Izraelevitch. (2016). The Escaramujo Project: instrumentation courses during a road trip across the Americas. Proceeding of the 38th International Conference on High Energy Physics. https://arxiv.org/abs/1611.06205
