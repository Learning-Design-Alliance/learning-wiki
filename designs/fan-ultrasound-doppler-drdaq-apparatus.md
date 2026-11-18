---
type: design
id: fan-ultrasound-doppler-drdaq-apparatus
title: Fan-reflection 40 kHz acoustic Doppler apparatus with DrDAQ ADC and spectrum analysis
description: "A low-cost teaching-laboratory kit for demonstrating the acoustic Doppler effect via circular motion: \"two ultrasonic transducers, a transmitter and a receiver that operate optimally at 40 kHz\" are aimed at a spinning..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: stephen-w-hughes-2016
    resource: "http://dx.doi.org/10.1088/1361-6404/aa5446"
    title: "Stephen W. Hughes, Michael Cowley. (2016). Teaching the Doppler Effect in Astrophysics. European Journal of Physics (author-created version). http://dx.doi.org/10.1088/1361-6404/aa5446"
    author: Stephen W. Hughes, Michael Cowley
---

# Fan-reflection 40 kHz acoustic Doppler apparatus with DrDAQ ADC and spectrum analysis

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A low-cost teaching-laboratory kit for demonstrating the acoustic Doppler effect via circular motion: "two ultrasonic transducers, a transmitter and a receiver that operate optimally at 40 kHz" are aimed at a spinning computer fan (55 mm radius, nominal 3000 rpm). The receiver output feeds a Picotech DrDAQ 8-bit ADC sampling at 100 kHz, connected to a PC running PicoScope; spectra are averaged over 512 bins and exported as csv for analysis in Excel. The kit cost about A$30 from a local electronics store.

## Design Implications

### Context
#### Requirements
- A 0-15 VDC power supply with integral signal generator, a CRO for the fan rpm wire, and a computer fan with a three-wire rpm connection
#### Constraints
- The experiment uses the reflected-wave (factor-of-2) Doppler equation, so it demonstrates the astrophysical principle only at velocities much less than the speed of light where relativistic effects do not apply

### Target Learners
- second-year undergraduate astrophysics students

### Learning Goals
- understanding the Doppler shift of waves reflected from a moving object
- connecting acoustic Doppler measurements to astrophysical redshift measurements

### Claims
- 

## Related Designs

- [Off-the-shelf Doppler measurement apparatus: PC, directional microphone, digital voice recorder, and GNU Octave spectrum analysis](off-shelf-doppler-apparatus-kit.md)

## Examples
-

## Key Sources
- Stephen W. Hughes, Michael Cowley. (2016). Teaching the Doppler Effect in Astrophysics. European Journal of Physics (author-created version). http://dx.doi.org/10.1088/1361-6404/aa5446
