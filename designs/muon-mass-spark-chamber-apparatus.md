---
type: design
id: muon-mass-spark-chamber-apparatus
title: Muon-mass spark-chamber apparatus with coincidence/anticoincidence detection and triggered CCD image acquisition
description: "A four-component instructional laboratory system for observing cosmic-ray muon decays: \"spark chamber, particle-decay detection electronics, high-voltage pulsing electronics, and CCD-based image acquisition\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: benjamin-brau-2009
    resource: "https://arxiv.org/abs/0907.5461"
    title: "Benjamin Brau, Christopher May, Robert Ormond, and John Essick. (2009). Determining the Muon Mass in an Instructional Laboratory. https://arxiv.org/abs/0907.5461"
    author: Benjamin Brau, Christopher May, Robert Ormond, and John Essick
---

# Muon-mass spark-chamber apparatus with coincidence/anticoincidence detection and triggered CCD image acquisition

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A four-component instructional laboratory system for observing cosmic-ray muon decays: "spark chamber, particle-decay detection electronics, high-voltage pulsing electronics, and CCD-based image acquisition". A vertical stack of 21 disk-shaped aluminum plates separated by neon-filled spark gaps makes charged-particle trajectories visible; three plastic-scintillator detectors perform the X·Y·Z coincidence/anticoincidence operation that signals a muon decay within the chamber and triggers both the high-voltage pulser and a LabVIEW-controlled frame grabber that stores decay images. The experiment runs under computer control overnight, typically producing about 100 saved images per hour.

## Design Implications

### Context
#### Requirements
- A darkened room for overnight computer-controlled data acquisition
- Coincidence/anticoincidence logic (X·Y·Z) across three scintillation detectors to signal muon decay
#### Constraints
- Each spark gap can only produce a single spark, so upward-moving product electrons are not recorded
- Sparks form only for electron paths within roughly 30° of the chamber axis

### Target Learners
- undergraduate physics students in an instructional laboratory

### Learning Goals
- experimental methods of elementary particle physics
- measurement of the muon mass from decay-product energy distributions

### Claims
- [Spark Chamber Downward Electron Detection Artifact](../claims/spark-chamber-downward-electron-detection-artifact.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Benjamin Brau, Christopher May, Robert Ormond, and John Essick. (2009). Determining the Muon Mass in an Instructional Laboratory. https://arxiv.org/abs/0907.5461
