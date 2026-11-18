---
type: design
id: l-shaped-thrust-test-apparatus-element
title: Custom L-shaped thrust-measurement apparatus with piezoelectric load cell and LabView data acquisition at 2 kHz
description: "Students built an L-shaped apparatus in which \"The load was applied at one end of the arm and the measurement was taken at the other end of the arm\", measuring thrust by balancing the moment (F1R1 = F2R2)."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: campbell-jr-2016
    resource: "https://scholar.google.com/scholar?q=Model+Rocket+Project+for+Aerospace+Engineering+Course+Trajectory+Simulation+and+Propellant+Analysis"
    title: "Campbell Jr., T.A., & Okutsu, M. (2016). Model Rocket Project for Aerospace Engineering Course: Trajectory Simulation and Propellant Analysis. https://scholar.google.com/scholar?q=Model+Rocket+Project+for+Aerospace+Engineering+Course+Trajectory+Simulation+and+Propellant+Analysis"
    author: "Campbell Jr., T.A., & Okutsu, M"
---

# Custom L-shaped thrust-measurement apparatus with piezoelectric load cell and LabView data acquisition at 2 kHz

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Students built an L-shaped apparatus in which "The load was applied at one end of the arm and the measurement was taken at the other end of the arm", measuring thrust by balancing the moment (F1R1 = F2R2). A piezoelectric load cell fed a signal conditioner and data acquisition board; LabView scripts saved the digital signal at "a high sampling rate of 2 kHz" as a MATLAB data file used as trajectory-simulation input.

## Design Implications

### Context
#### Requirements
- The entire experiment had to be designed using materials and equipment already available in the lab
#### Constraints
- The piezoelectric crystal used in the load cell had an inherent problem of voltage discharge, making a recorded force appear to decay over time; students calibrated the data by measuring the decay constant and multiplying the recorded data by an exponential function

### Target Learners
- third- and fourth-year undergraduate aerospace engineering students

### Learning Goals
- measuring rocket motor thrust experimentally
- designing instrumentation and data acquisition under lab constraints
- configuring hardware and software to record usable data

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Campbell Jr., T.A., & Okutsu, M. (2016). Model Rocket Project for Aerospace Engineering Course: Trajectory Simulation and Propellant Analysis. https://scholar.google.com/scholar?q=Model+Rocket+Project+for+Aerospace+Engineering+Course+Trajectory+Simulation+and+Propellant+Analysis
