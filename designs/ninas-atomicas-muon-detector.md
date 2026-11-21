---
type: design
id: ninas-atomicas-muon-detector
title: "Niñas Atómicas muon detector: plastic scintillators with SiPMs, custom PCB, and Arduino UNO with two-channel coincidence"
description: A portable classroom muon detector built by the participating girls, costing close to 300 USD per unit.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: giovanna-cottin-and-francisca-garay-2026
    resource: "https://arxiv.org/abs/2511.05754"
    title: "Giovanna Cottin and Francisca Garay. (2026). \"Niñas Atómicas\" (Atomic Girls): An initiative that generates opportunities for young girls in STEM. https://arxiv.org/abs/2511.05754"
    author: Giovanna Cottin and Francisca Garay
---

# Niñas Atómicas muon detector: plastic scintillators with SiPMs, custom PCB, and Arduino UNO with two-channel coincidence

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A portable classroom muon detector built by the participating girls, costing close to 300 USD per unit. It uses "two plastic scintillators, each equipped with a light-sensing silicon photomultiplier (SiPM)", wrapped in reflective foil, with 3D-printed black PLA casings to reduce light contamination. Signals pass through a custom PCB to an Arduino UNO that records counts with timestamps to an SD card. "In our muon detector design, we require a coincidence between two detector channels to declare a valid muon event", which suppresses noise and random single-detector triggers.

## Design Implications

### Context
#### Requirements
- A black, densely printed (or high-infill) PLA casing so the SiPMs are covered in a dark, non-reflective surface to reduce external light contamination
- A computer with the Arduino IDE software for recording data, or alternatively mains power with a transformer for use outside the lab
#### Constraints
- The estimated cost of each muon detector is close to 300 USD, an important budget consideration when scaling the initiative

### Target Learners
- High-school girls aged 15–16

### Learning Goals
- Particle physics concepts
- Electronics
- Data analysis and programming
- Scientific methodology

### Claims
- Muon Flux Altitude [+M]
- Muon Lifetime Classroom Estimate [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Giovanna Cottin and Francisca Garay. (2026). "Niñas Atómicas" (Atomic Girls): An initiative that generates opportunities for young girls in STEM. https://arxiv.org/abs/2511.05754
