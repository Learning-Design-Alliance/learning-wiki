---
type: design
id: embedded-rs232-module-89c51-multimeter
title: Embedded RS-232 module capturing multimeter panel data with an 89C51 chip
description: Because most low-cost student multimeters lack serial communication with a computer, the study implements an Embedded RS-232 Module on an 8-bit 89C51 single chip and integrates it with the low-cost multimeter to repla...
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

# Embedded RS-232 module capturing multimeter panel data with an 89C51 chip

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Because most low-cost student multimeters lack serial communication with a computer, the study implements an Embedded RS-232 Module on an 8-bit 89C51 single chip and integrates it with the low-cost multimeter to replace a high-cost multimeter. It captures "the data shown on the panel of the multimeter and transfer it to the computer". The article lists the chip's advantages as easy-to-learn programming, low cost, simple circuit and small size, and details its CPU, memories, oscillator, 32 I/O pins and timer/counter.

## Design Implications

### Context
#### Requirements
- integration with a low-cost multimeter whose panel display is captured by the module
#### Constraints
- common low-cost multimeters cannot communicate with a computer, which motivated the module

### Target Learners
- students using low-cost multimeters in practical electronics learning

### Learning Goals
- real circuit measurement data shared within cooperative learning groups

### Claims

- [Misinterpretations of multimeter displays after building real circuits confused students and negatively affected performance, leading the author to reject the assumption that experimental skills need no explicit training](../claims/multimeter-misreading-hurts-real-experiment-performance.md) [+W]

## Related Designs

- [Embedded broker on an ARM7 board replacing an expensive server](embedded-broker-arm7-cooperative-learning.md)
- [Threadbare DAQ card based on the ADC0809 chip and the PC parallel port for undergraduate physics experiments](threadbare-parallel-port-daq-card.md)
- [Circuit-measuring cooperative learning system with 3D virtual instruments](circuit-measuring-3d-virtual-instrument-cooperative-learning-system.md)

## Examples
-

## Key Sources
- Kao, F.-C., Wang, S.-R. & Huang, T.-H. (2010). The Design of Circuit-Measuring Collaborative Learning System with Embedded Broker. IJCSI International Journal of Computer Science Issues, Vol. 7, Issue 1, No. 3. https://www.ijcsi.org
