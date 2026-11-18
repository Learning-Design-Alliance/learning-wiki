---
type: design
id: arduino-low-cost-sensor-kit-open-projects
title: Low-cost Arduino sensor kit for open physics projects
description: "A set of low-cost sensors and Arduino boards serving as the data-acquisition backbone of the open projects, specified in the article's Table 1: voltage inputs, thermocouple with MAX31855 amplifier, Hall sensors and ma..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: f-bouquet-2015
    resource: "http://www.PhysicsReImagined.com"
    title: "F. Bouquet, J. Bobroff, M. Fuchs-Gallezot, and L. Maurines. (2015). Project-based physics labs using low-cost open-source hardware. http://www.PhysicsReImagined.com"
    author: F. Bouquet, J. Bobroff, M. Fuchs-Gallezot, and L. Maurines
---

# Low-cost Arduino sensor kit for open physics projects

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A set of low-cost sensors and Arduino boards serving as the data-acquisition backbone of the open projects, specified in the article's Table 1: voltage inputs, thermocouple with MAX31855 amplifier, Hall sensors and magnetometer, thermistors, light sensors, electret microphone, accelerometers, and force/strain sensors, most costing less than $10. The authors state "the diversity of the projects is obviously linked to the variety of sensors available", and that the total material cost per project was less than $100, allowing a lab for about 20 students with a total budget under $2000.

## Design Implications

### Context
#### Requirements
- An Arduino Uno board (about $20) with free open-source coding interface software and a USB port so students can use their own laptops
- Only basic coding skill is required, as many code snippets for various sensors are available on the Internet
#### Constraints
- These sensors don't have the sensitivity of lab-quality equipment, though they offer a wide range of measurable physics phenomena
- The setup's low cost meant one or two Arduino boards were fried during the projects

### Target Learners
- third-year university physics students

### Learning Goals
- measuring physical quantities with sensors
- designing and building experimental setups

### Claims
- [Arduino Low Cost Sensor Kit Open Projects](arduino-low-cost-sensor-kit-open-projects.md) [+M]

## Related Designs

- [Low-budget Arduino-based sensor kit with datasheet calibration for CanSat atmospheric measurement](cansat-arduino-low-budget-sensor-kit.md)

## Examples
-

## Key Sources
- F. Bouquet, J. Bobroff, M. Fuchs-Gallezot, and L. Maurines. (2015). Project-based physics labs using low-cost open-source hardware. http://www.PhysicsReImagined.com
