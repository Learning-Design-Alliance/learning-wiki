---
type: design
id: fats-m100-bioharness-gift-sensor-suite
title: Instrumented FATS M100 marksmanship simulator with BioHarness breathing sensor and GIFT data logging
description: "The data-collection apparatus combines Meggitt's FATS M100 Advanced Reality Simulator—a simulated M4 carbine with embedded sensors—with a Zephyr BioHarness BT wireless breathing strap, all logged through GIFT on a syn..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: goldberg-2018
    resource: "https://doi.org/10.1007/s40593-017-0155-y"
    title: "Goldberg, B., Amburn, C., Ragusa, C., & Chen, D. (2018). Modeling Expert Behavior in Support of an Adaptive Psychomotor Training Environment: a Marksmanship Use Case. Int J Artif Intell Educ 28:194–224. https://doi.org/10.1007/s40593-017-0155-y"
    author: "Goldberg, B., Amburn, C., Ragusa, C., & Chen, D"
---

# Instrumented FATS M100 marksmanship simulator with BioHarness breathing sensor and GIFT data logging

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The data-collection apparatus combines Meggitt's FATS M100 Advanced Reality Simulator—a simulated M4 carbine with embedded sensors—with a Zephyr BioHarness BT wireless breathing strap, all logged through GIFT on a synced timestamp. The weapon was "designed with embedded sensors, including: point of aim through an infrared laser mounted in the barrel at a 6 Hz sampling rate, a trigger sensor that measures displacement during the execution of a shot, butt-stock pressure, and the weapon's cant angle". A custom GIFT Gateway plug-in received simulator data over TCP, and a GIFT plug-in received BioHarness data wirelessly via Bluetooth at approximately 18 Hz.

## Design Implications

### Context
#### Requirements
- Time-synced logging across sensor channels via GIFT for post-hoc merging
- Mechanical and digital zeroing of the weapon before data collection
#### Constraints
- Weapon cant and butt-stock pressure were not analyzed in this work
- Recoil was approximately 70% of a real weapon's intensity
- Automatic dispersion and wind effects were disabled

### Target Learners
- Soldiers training on rifle marksmanship in simulators

### Learning Goals
- Behavioral measurement of marksmanship functional elements (stability, trigger control, breath control)

### Claims

- [GIFT serves as a testbed for developing and validating expert models for psychomotor tasks such as rifle marksmanship](../claims/gift-testbed-psychomotor-expert-models.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Goldberg, B., Amburn, C., Ragusa, C., & Chen, D. (2018). Modeling Expert Behavior in Support of an Adaptive Psychomotor Training Environment: a Marksmanship Use Case. Int J Artif Intell Educ 28:194–224. https://doi.org/10.1007/s40593-017-0155-y
