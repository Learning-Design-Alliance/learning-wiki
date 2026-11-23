---
type: design
id: gic-maxwell-wien-bridge-inductance-setup
title: GIC-realized large inductance measured by a Maxwell-Wien bridge — EPO7 experimental set-up
description: The EPO7 set-up is a large inductance implemented with a general impedance converter (two operational amplifiers in an 8-pin package powered by 9 V batteries, resistors and a capacitor) measured with a Maxwell-Wien br...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: todor-m-mishonov-2019
    resource: "https://arxiv.org/abs/1912.07368"
    title: "Todor M. Mishonov, Riste Popeski-Dimovski, Leonora Velkoska, Iglika M. Dimitrova, Vassil N. Gourev, Aleksander P. Petkov, Emil G. Petkov, Albert M. Varonov. (2019). The Day of the Inductance. Problem of the 7th Experimental Physics Olympiad, Skopje, 7 December 2019. https://arxiv.org/abs/1912.07368"
    author: Todor M. Mishonov, Riste Popeski-Dimovski, Leonora Velkoska, Iglika M. Dimitrova, Vassil N. Gourev, Aleksander P. Petkov, Emil G. Petkov, Albert M. Varonov
---

# GIC-realized large inductance measured by a Maxwell-Wien bridge — EPO7 experimental set-up

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The EPO7 set-up is a large inductance implemented with a general impedance converter (two operational amplifiers in an 8-pin package powered by 9 V batteries, resistors and a capacitor) measured with a Maxwell-Wien bridge, using the balance relation L = CR_C R_L. Students balance the bridge by minimizing the voltage U_ud between pins (u) and (d) with a potentiometer, then compute L from the potentiometer resistance. The article notes "The described set-up can be considered as a prototype for companies producing laboratory equipment." Component values are printed: a 10 µF nominal capacitor and a resistor close to 1 kΩ in the down-left bridge arm.

## Design Implications

### Context
#### Requirements
- 9 V batteries connected with correct polarity (orange label to orange label), or the operational amplifiers burn; external voltage below 5 V at home, frequency f ≤ 60 Hz; a multimeter or AC voltmeter.
#### Constraints
- Voltage above the 9 V battery supply is dangerous for the operational amplifiers; the article recommends not applying more than 6 V to the bridge.

### Target Learners
- high-school students (categories S, M, L)
- university students (XL)

### Learning Goals
- inductance measurement
- AC bridge balance
- impedance and operational-amplifier circuits

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Todor M. Mishonov, Riste Popeski-Dimovski, Leonora Velkoska, Iglika M. Dimitrova, Vassil N. Gourev, Aleksander P. Petkov, Emil G. Petkov, Albert M. Varonov. (2019). The Day of the Inductance. Problem of the 7th Experimental Physics Olympiad, Skopje, 7 December 2019. https://arxiv.org/abs/1912.07368
