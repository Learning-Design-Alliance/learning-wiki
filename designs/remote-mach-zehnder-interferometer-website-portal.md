---
type: design
id: remote-mach-zehnder-interferometer-website-portal
title: Remotely triggered Mach-Zehnder interferometer laboratory with motorized optical mount
description: The fourth portal of the website lets students conduct a real-time Mach-Zehnder interferometer experiment from any web browser.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: singh-2011
    resource: "http://202.3.77.50/~opticalv/interferometry/"
    title: "Singh, V., Dubey, R., Panigrahi, P.K., and Muralidhar, K. (2011). An Educational Website on Interferometry. Laser Technology Programme, Indian Institute of Technology Kanpur. http://202.3.77.50/~opticalv/interferometry/"
    author: Singh, V., Dubey, R., Panigrahi, P.K., and Muralidhar, K
---

# Remotely triggered Mach-Zehnder interferometer laboratory with motorized optical mount

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The fourth portal of the website lets students conduct a real-time Mach-Zehnder interferometer experiment from any web browser. Hardware includes a motorized optical mount with inner and outer rings on fine-thread screws, driven by a DC stepper motor and Easy Driver board (Allegro A3967 chip), with control executed in a LabVIEW environment. 'Once the web server is enabled, LabVIEW generates front panel images of the VI and a URL that can be accessed from any web browser to link to the experiment.'

## Design Implications

### Context
#### Requirements
- Electric DC stepper motor with motor driver applying short pulses of torque
- LabVIEW environment with built-in web server and a PWM DAQ card plus motor and driver circuit at the control point
#### Constraints
- The remote laboratory is intended by the authors for use in a limited way and does not replace hands-on laboratories

### Target Learners
- 4th year undergraduate and 1st year postgraduate engineering students

### Learning Goals
- Aligning and operating a Mach-Zehnder interferometer remotely
- Experimental competence in laser-based optical measurement

### Claims
- 

## Related Designs
- [Interferometry Educational Website Four Panes](interferometry-educational-website-four-panes.md)

## Examples
-

## Key Sources
- Singh, V., Dubey, R., Panigrahi, P.K., and Muralidhar, K. (2011). An Educational Website on Interferometry. Laser Technology Programme, Indian Institute of Technology Kanpur. http://202.3.77.50/~opticalv/interferometry/
