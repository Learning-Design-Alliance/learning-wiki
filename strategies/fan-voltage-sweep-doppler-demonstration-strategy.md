---
type: strategy
id: fan-voltage-sweep-doppler-demonstration-strategy
title: Run the fan Doppler demonstration across supply voltages from 4 to 12 V and read rotation rate from the rpm wire
description: "A concrete teaching-laboratory recipe: with the fan off a sharp 40 kHz peak is recorded, then \"the spectrum collected for power supply voltages of 4, 6, 8, 10 and 12 V\", allowing about 20 seconds for each spectrum to..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: stephen-w-hughes-2016
    resource: "http://dx.doi.org/10.1088/1361-6404/aa5446"
    title: "Stephen W. Hughes, Michael Cowley. (2016). Teaching the Doppler Effect in Astrophysics. European Journal of Physics (author-created version). http://dx.doi.org/10.1088/1361-6404/aa5446"
    author: Stephen W. Hughes, Michael Cowley
---

# Run the fan Doppler demonstration across supply voltages from 4 to 12 V and read rotation rate from the rpm wire

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
A concrete teaching-laboratory recipe: with the fan off a sharp 40 kHz peak is recorded, then "the spectrum collected for power supply voltages of 4, 6, 8, 10 and 12 V", allowing about 20 seconds for each spectrum to stabilise before freezing and storing the trace as csv. The fan's three-wire motor drives a CRO via the yellow rpm wire, one pulse per revolution, so students measure the temporal separation of rpm pulses to obtain rotation rate for each voltage and relate it to the observed spectral widening.

## Design Implications

### Context
#### Requirements
- A DrDAQ ADC with spectrum mode (512-bin averaging), 40 kHz transmitter/receiver pair in tubes aimed down at the fan on a rubber mouse pad, and a CRO for the rpm pulse train
#### Constraints
- The DrDAQ has only a single CRO input, so the rpm trace is displayed on a conventional digital oscilloscope

### Target Learners
- undergraduate physics students in a teaching laboratory

### Target Learning Goals
- measuring Doppler shift as a function of source speed
- analysing spectra quantitatively by integrating area and deriving equivalent triangle base

## Related Strategies

- [Extend the fan Doppler experiment to an audible sound source, or reuse it to teach ultrasound fundamentals in medical physics](audible-doppler-variant-and-medical-physics-reuse-strategy.md)

## Examples
-

## Key Sources
- Stephen W. Hughes, Michael Cowley. (2016). Teaching the Doppler Effect in Astrophysics. European Journal of Physics (author-created version). http://dx.doi.org/10.1088/1361-6404/aa5446
