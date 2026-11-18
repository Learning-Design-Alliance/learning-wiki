---
type: design
id: single-diode-multi-spectroscopy-lab-sequence
title: A single grating-feedback laser diode setup supporting multiple complementary high-resolution spectroscopy experiments for advanced undergraduates
description: This pattern organizes an advanced undergraduate atomic-physics laboratory around one commercial grating-feedback laser diode (Toptica DL100) used successively for Doppler-broadened absorption, saturated absorption, a...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: v-jacques-2009
    resource: "https://arxiv.org/abs/0902.3115"
    title: "V Jacques, B Hingant, A Allafort, M Pigeard and J F Roch. (2009). Non-linear spectroscopy of rubidium: An undergraduate experiment. https://arxiv.org/abs/0902.3115"
    author: V Jacques, B Hingant, A Allafort, M Pigeard and J F Roch
---

# A single grating-feedback laser diode setup supporting multiple complementary high-resolution spectroscopy experiments for advanced undergraduates

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
This pattern organizes an advanced undergraduate atomic-physics laboratory around one commercial grating-feedback laser diode (Toptica DL100) used successively for Doppler-broadened absorption, saturated absorption, and two-photon spectroscopy of rubidium. As the authors write, "All experiments are performed with the same grating-feedback laser diode, providing an opportunity to compare diﬀerent high resolution spectroscopy methods using a single experimental setup." The two non-linear methods are complementary because single-photon transitions obey Δl = ±1 while two-photon transitions obey Δl = 0,±2, letting students compare methods and encounter selection rules, atomic spectra and the Zeeman effect.

## Design Implications

### Context
#### Requirements
- A temperature-stabilized grating-feedback diode laser in Littrow configuration with mode-hop free tuning (around 20 GHz with the DL100), an optical isolator, a Fabry-Perot interferometer frequency reference, and a rubidium vapor cell
#### Constraints
- For the two-photon experiment the fluorescence signal is efficient only above 80 °C and saturates around 130 °C, decreasing at higher temperature because of self-absorption of the 6P3/2→5S1/2 transition
- The measured two-photon linewidths (~2 MHz) are limited by the laser diode spectral bandwidth; evidencing the natural width would require a laser with less than 300 kHz bandwidth

### Target Learners
- advanced undergraduate laboratory students

### Learning Goals
- quantum mechanics selection rules
- atomic hyperfine spectra
- Zeeman effect
- high-resolution spectroscopy techniques

### Claims

## Related Designs

- [Detector-as-common-thread course design: students progress through all stages of a real particle physics experiment](detector-common-thread-experiment-stages.md)

## Examples
-

## Key Sources
- V Jacques, B Hingant, A Allafort, M Pigeard and J F Roch. (2009). Non-linear spectroscopy of rubidium: An undergraduate experiment. https://arxiv.org/abs/0902.3115
