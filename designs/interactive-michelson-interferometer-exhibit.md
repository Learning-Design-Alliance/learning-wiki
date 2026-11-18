---
type: design
id: interactive-michelson-interferometer-exhibit
title: A working Michelson interferometer exhibit with arcade-button signal injection, live interference-pattern display, and touchscreen multimedia content for unsupervised museum use.
description: "The core element is a scaled-down working Michelson interferometer — \"a scaled-down version of the key technology used in gravitational-wave detectors\" — with a 60 cm aluminium base, He–Ne laser, 2-inch optics, and PZ..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: s-j-cooper-2020
    resource: "https://arxiv.org/abs/2004.03052"
    title: "S. J. Cooper, A. C. Green, H. R. Middleton, C. P. L. Berry, R. Buscicchio, E. Butler, C. J. Collins, C. Gettings, D. Hoyland, A. W. Jones, J. H. Lindon, I. Romero-Shaw, S. P. Stevenson, E. P. Takeva, S. Vinciguerra, A. Vecchio, C. M. Mow-Lowry, and A. Freise. (2020). An Interactive Gravitational-Wave Detector Model for Museums and Fairs. https://arxiv.org/abs/2004.03052"
    author: S. J. Cooper, A. C. Green, H. R. Middleton, C. P. L. Berry, R. Buscicchio, E. Butler, C. J. Collins, C. Gettings, D. Hoyland, A. W. Jones, J. H. Lindon, I. Romero-Shaw, S. P. Stevenson, E. P. Takeva, S. Vinciguerra, A. Vecchio, C. M. Mow-Lowry, and A. Freise
---

# A working Michelson interferometer exhibit with arcade-button signal injection, live interference-pattern display, and touchscreen multimedia content for unsupervised museum use.

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The core element is a scaled-down working Michelson interferometer — "a scaled-down version of the key technology used in gravitational-wave detectors" — with a 60 cm aluminium base, He–Ne laser, 2-inch optics, and PZT-driven mirror actuation. Four arcade-style buttons inject simulated gravitational-wave signals (two chirps, a continuous wave, and a burst) that move a mirror by up to 2 µm, producing visually distinct changes in a ringed interference pattern projected at ~3 cm. Custom JavaScript-based software on a Raspberry Pi provides a touchscreen menu of topics, videos under 90 s, text pages under 80 words, a four-question quiz, and live graphing of the photodiode signal alongside a webcam feed of the pattern.

## Design Implications

### Context
#### Requirements
- Durable, low-maintenance hardware and software suitable for unsupervised public use, with components encased in an acrylic dome and electronics built to withstand daily power cycling
- A class 1 laser with all beams contained within the base plate and restricted access via the dome for eye safety
#### Constraints
- The model cannot detect actual gravitational waves; it responds to room vibrations and injected signals
- Simulated signals are over a trillion times larger in amplitude than real signals and scaled below 25 Hz to be visually followable

### Target Learners
- general public including children and adults
- school groups aged 11 and above
- museum visitors without science backgrounds

### Learning Goals
- understanding what gravitational waves are and how they are detected
- awareness of LIGO and gravitational-wave astronomy
- understanding how interferometers sense tiny changes in distance

### Claims
- [Interactive Gw Detector Model Increased Visitor Interest](../claims/interactive-gw-detector-model-increased-visitor-interest.md) [+M]
- Exhibit Placement Affects Museum Engagement [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- S. J. Cooper, A. C. Green, H. R. Middleton, C. P. L. Berry, R. Buscicchio, E. Butler, C. J. Collins, C. Gettings, D. Hoyland, A. W. Jones, J. H. Lindon, I. Romero-Shaw, S. P. Stevenson, E. P. Takeva, S. Vinciguerra, A. Vecchio, C. M. Mow-Lowry, and A. Freise. (2020). An Interactive Gravitational-Wave Detector Model for Museums and Fairs. https://arxiv.org/abs/2004.03052
