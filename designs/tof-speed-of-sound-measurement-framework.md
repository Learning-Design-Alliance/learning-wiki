---
type: design
id: tof-speed-of-sound-measurement-framework
title: Time-of-flight (TOF) measurement framework for classroom speed-of-sound experiments
description: "The time-of-flight approach treats sound speed as a travel-time problem: a short acoustic pulse passes two points and the known microphone spacing divided by the time delay yields the propagation speed."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: helio-takai-2025
    resource: "https://arxiv.org/abs/2507.21368"
    title: "Helio Takai, Tom Tomaszewski, Jeremy Tomaszewski, Joe Sundermier. (2025). Measuring Sound, One Ping at a Time. https://arxiv.org/abs/2507.21368"
    author: Helio Takai, Tom Tomaszewski, Jeremy Tomaszewski, Joe Sundermier
---

# Time-of-flight (TOF) measurement framework for classroom speed-of-sound experiments

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The time-of-flight approach treats sound speed as a travel-time problem: a short acoustic pulse passes two points and the known microphone spacing divided by the time delay yields the propagation speed. The article distinguishes "two-microphone systems that record the pulse at separate points along its path" from "single-microphone systems that capture the initial pulse and its echo from a reflective surface". It grounds the measurement in the ideal-gas relation v = √(γRT/M), connecting the measured speeds to temperature, molar mass, and adiabatic index.

## Design Implications

### Context
#### Requirements
- Known, precisely measured microphone spacing
- Waveform display on a computer with sufficient time resolution to read the delay between pulses
#### Constraints
- Both configurations achieve excellent precision when their waveforms are displayed on a computer; the 2 kHz ping's 17 cm wavelength was chosen as adequate for this tube length, with no attempt to optimize the signal frequency

### Target Learners
- high school and undergraduate physics students

### Learning Goals
- measuring wave propagation speed
- applying the ideal gas model to acoustic phenomena

### Claims
- Tof Measurements Agree Ideal Gas Predictions [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Helio Takai, Tom Tomaszewski, Jeremy Tomaszewski, Joe Sundermier. (2025). Measuring Sound, One Ping at a Time. https://arxiv.org/abs/2507.21368
