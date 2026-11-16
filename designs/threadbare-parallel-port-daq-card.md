---
type: design
id: threadbare-parallel-port-daq-card
title: Threadbare DAQ card based on the ADC0809 chip and the PC parallel port for undergraduate physics experiments
description: "A minimal data acquisition card built in an undergraduate class to interface with a computer's parallel port."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: sumit-ghambir-and-parun-2007
    resource: "http://www-server.bcc.ac.uk/~zcapl31/LptADC.html"
    title: "Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html"
    author: Sumit Ghambir and P.Arun
---

# Threadbare DAQ card based on the ADC0809 chip and the PC parallel port for undergraduate physics experiments

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A minimal data acquisition card built in an undergraduate class to interface with a computer's parallel port. The authors state it was developed "with the intention to enable students to do various physics experiments with the computer sparing them from knowing the details of the electronics required." It uses an eight-bit ADC0809 chip, an IC555 astable clock, a 74LS244 octal buffer to protect the computer, and a fabricated PCB of 9cm x5cm.

## Design Implications

### Context
#### Requirements
- The card requires a bi-directional (PS) parallel-port mode verified in the computer's BIOS, with the LPT base address noted for programming.
#### Constraints
- The article reports the circuit "can only work reliably in frequency ranges of Hz", so it is limited to slow-event experiments.

### Target Learners
- undergraduate physics students

### Learning Goals
- computer interfacing fundamentals
- physics experimentation with computer data acquisition

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html
