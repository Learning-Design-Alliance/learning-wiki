---
type: design
id: simple-school-digital-weather-station
title: "Simple school-based digital weather station in three hardware versions (Arduino Uno, BBC micro:bit, Coach/VinciLab)"
description: "A low-cost digital weather station built at the authors' workplace that students use to measure temperature, pressure, air humidity, and light intensity during school activities."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: m-hruška-and-m-plesch-2025
    resource: "https://doi.org/10.1088/1742-6596/3155/1/012015"
    title: "M Hruška and M Plesch. (2025). The use of a simple digital weather station (not only) in teaching physics. Journal of Physics: Conference Series 3155 (2025) 012015. https://doi.org/10.1088/1742-6596/3155/1/012015"
    author: M Hruška and M Plesch
---

# Simple school-based digital weather station in three hardware versions (Arduino Uno, BBC micro:bit, Coach/VinciLab)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A low-cost digital weather station built at the authors' workplace that students use to measure temperature, pressure, air humidity, and light intensity during school activities. Three parallel versions were built on Arduino Uno, BBC micro:bit, and the Coach system with a VinciLab data logger, so comparable results can be achieved depending on the school's equipment and educational goals. The authors state the design reasons were "simplicity, affordability, and didactic flexibility", deliberately focusing on a few key physical quantities rather than a wide meteorological range.

## Design Implications

### Context
#### Requirements
- Sensors connect via an I²C bus with a shared 3.3 V supply; data is stored to a computer via USB serial port or transferred by USB flash drive after measurement
#### Constraints
- Classroom usability has not yet been empirically verified; qualitative verification in real classroom settings is planned for the end of 2025 within the DiTEdu national project

### Target Learners
- secondary school students
- high school students of physics, computer science and electrical engineering

### Learning Goals
- measuring fundamental physical quantities
- data collection, analysis and interpretation
- microcontroller programming and algorithmization

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- M Hruška and M Plesch. (2025). The use of a simple digital weather station (not only) in teaching physics. Journal of Physics: Conference Series 3155 (2025) 012015. https://doi.org/10.1088/1742-6596/3155/1/012015
