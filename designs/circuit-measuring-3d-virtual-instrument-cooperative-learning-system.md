---
type: design
id: circuit-measuring-3d-virtual-instrument-cooperative-learning-system
title: Circuit-measuring cooperative learning system with 3D virtual instruments
description: The article designs and implements a Web-based cooperative learning system for operating virtual instruments with circuit-measuring function.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-16
sources:
  - id: kao-2010
    resource: "https://www.ijcsi.org"
    title: "Kao, F.-C., Wang, S.-R. & Huang, T.-H. (2010). The Design of Circuit-Measuring Collaborative Learning System with Embedded Broker. IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 1, No. 3. https://www.ijcsi.org"
    author: "Kao, F.-C., Wang, S.-R. & Huang, T.-H"
---

# Circuit-measuring cooperative learning system with 3D virtual instruments

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article designs and implements a Web-based cooperative learning system for operating virtual instruments with circuit-measuring function. It integrates "Virtual Reality, Remote Control Parameter Transmission and embedded system techniques" so that group members jointly operate 3D virtual multimeters, power supplies and oscilloscopes, supported by instant messaging and 3D puzzles. The system infrastructure has four parts: the cooperative learning system, cooperative digital learning items, teaching material, and circuit measurement.

## Design Implications

### Context
#### Requirements
- Learners install the client from a portal website and connect to an embedded broker by entering its IP address and assigned port
#### Constraints
- Most existing network cooperative learning systems target theoretical courses rather than online operation of practical instruments, per the authors' framing

### Target Learners
- students in practical electronics courses

### Learning Goals
- operating electronic instruments and performing circuit measurement through group collaboration

### Claims

- [Learners rated the circuit-measuring cooperative system positively on a five-point Likert questionnaire](../claims/likert-questionnaire-positive-circuit-measuring-system.md) [+W]

## Related Designs

- [Embedded broker on an ARM7 board replacing an expensive server](embedded-broker-arm7-cooperative-learning.md)
- [Embedded RS-232 module capturing multimeter panel data with an 89C51 chip](embedded-rs232-module-89c51-multimeter.md)

## Examples
-

## Key Sources
- Kao, F.-C., Wang, S.-R. & Huang, T.-H. (2010). The Design of Circuit-Measuring Collaborative Learning System with Embedded Broker. IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 1, No. 3. https://www.ijcsi.org
