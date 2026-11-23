---
type: design
id: software-lock-in-led-distance-lab-apparatus
title: "Software-based lock-in student laboratory apparatus: modulated LED source, photodetector, and National Instruments USB-6210 data acquisition with LabView"
description: A student laboratory setup in which a red LED source is modulated by an optical chopper wheel and detected by a PASCO CI-6504A Light Sensor at its 100× gain setting (maximum illuminance of 5 lux).
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: david-t-chuss-2017
    resource: "https://arxiv.org/abs/1711.00997"
    title: "David T. Chuss. (2017). A Software-Based Lock-In Measurement for Student Laboratories. https://arxiv.org/abs/1711.00997"
    author: David T. Chuss
---

# Software-based lock-in student laboratory apparatus: modulated LED source, photodetector, and National Instruments USB-6210 data acquisition with LabView

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A student laboratory setup in which a red LED source is modulated by an optical chopper wheel and detected by a PASCO CI-6504A Light Sensor at its 100× gain setting (maximum illuminance of 5 lux). The sensor output and chopper reference are connected to "an National Instruments USB-6210 interface", and a LabView VI acquires 20,000 samples at 600 Hz (33.3 s integration) at each source-detector distance, which is varied between 5.7 cm and 270 cm. Data sets are taken with the chopper on and off to demonstrate the difference between modulated and non-modulated techniques.

## Design Implications

### Context
#### Requirements
- A chopper wheel to modulate the LED source and a reference signal from the chopper synchronized with the data stream
- Time streams of both the reference and detector signals stored for software demodulation
#### Constraints
- The detector's limited temporal response acts as a low-pass filter, concentrating power in the fundamental
- In a noisier environment or with a larger-bandwidth detector, a low-pass Nyquist filter can be placed in the signal path prior to digitization

### Target Learners
- undergraduate physics students

### Learning Goals
- understanding the lock-in measurement technique
- frequency-domain analysis of time-stream data
- computational techniques for large data sets

### Claims
- Lock In Sensitivity Orders Of Magnitude Improvement [+M]
- Modulated Power Law Distance Fit [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- David T. Chuss. (2017). A Software-Based Lock-In Measurement for Student Laboratories. https://arxiv.org/abs/1711.00997
