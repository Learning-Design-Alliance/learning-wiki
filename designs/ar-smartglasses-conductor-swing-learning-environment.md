---
type: design
id: ar-smartglasses-conductor-swing-learning-environment
title: AR smartglasses learning environment for the conductor swing experiment with real-time 3D magnetic field representations
description: An AR application written in Unity running on the Microsoft HoloLens 2 that overlays 3D field vector, field line, and right-hand rule representations on a physical conductor swing experiment.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: warkentin-2025
    resource: "https://arxiv.org/abs/2502.06421"
    title: "Warkentin, M., Altmeyer, K., Liang, Y., Steinmacher, B., Gränz, B., Lichtenberger, A., Küchemann, S., Kuhn, J. and Hoyer, C. (2025). Hands-on Experiment Supported by Augmented Reality Smartglasses for Learning the Lorentz Force. https://arxiv.org/abs/2502.06421"
    author: Warkentin, M., Altmeyer, K., Liang, Y., Steinmacher, B., Gränz, B., Lichtenberger, A., Küchemann, S., Kuhn, J. and Hoyer, C
---

# AR smartglasses learning environment for the conductor swing experiment with real-time 3D magnetic field representations

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An AR application written in Unity running on the Microsoft HoloLens 2 that overlays 3D field vector, field line, and right-hand rule representations on a physical conductor swing experiment. Real-time current and conductor displacement are measured by a circuit with a current sensor, rotary encoder, and Arduino microcontroller with Bluetooth, and the horseshoe magnet is tracked via object tracking with an attached color pattern. Learners interact through a restricted student menu while supervisors use a full supervisor menu.

## Design Implications

### Context
#### Requirements
- Real-time measurement of current and conductor displacement
- Object tracking of the horseshoe magnet using an attached non-symmetric color pattern
- Image tracking of a sticker on the conductor mounting to locate the conductor
#### Constraints
- Contemporary object tracking works reliably mostly for objects with a rich feature pattern, making the simple horseshoe magnet technically demanding to track
- Tracking quality can be diminished, e.g. in situations with inadequate light sources

### Target Learners
- High school students
- University physics students in laboratory courses

### Learning Goals
- Understanding how the Lorentz force depends on current and magnetic field orientation
- Representational competence with magnetic field representations

### Claims
- [Ar Lorentz Force Sus 80 Excellent Usability](../claims/ar-lorentz-force-sus-80-excellent-usability.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Warkentin, M., Altmeyer, K., Liang, Y., Steinmacher, B., Gränz, B., Lichtenberger, A., Küchemann, S., Kuhn, J. and Hoyer, C. (2025). Hands-on Experiment Supported by Augmented Reality Smartglasses for Learning the Lorentz Force. https://arxiv.org/abs/2502.06421
