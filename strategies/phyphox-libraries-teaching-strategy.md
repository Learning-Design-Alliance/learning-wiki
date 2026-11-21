---
type: strategy
id: phyphox-libraries-teaching-strategy
title: Use the phyphox Arduino/MicroPython libraries so educators and learners with rudimentary programming knowledge can build app-connected experiments
description: "The article recommends that educators integrate custom sensors into teaching by loading the phyphox library from the Arduino IDE rather than learning BLE internals or the XML format, since the task \"became comparable..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: staacks-2023
    resource: "https://github.com/phyphox/phyphox-arduino"
    title: "Staacks, S., Dorsel, D., Krampe, A., Hagedorn, M., Leier, E., Heinke, H., & Stampfer, C. (2023). Bluetooth sensors in phyphox with Arduino and MicroPython – Paving the way from an idea to an experiment for teachers and learners. https://github.com/phyphox/phyphox-arduino"
    author: "Staacks, S., Dorsel, D., Krampe, A., Hagedorn, M., Leier, E., Heinke, H., & Stampfer, C"
---

# Use the phyphox Arduino/MicroPython libraries so educators and learners with rudimentary programming knowledge can build app-connected experiments

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends that educators integrate custom sensors into teaching by loading the phyphox library from the Arduino IDE rather than learning BLE internals or the XML format, since the task "became comparable to integrating one of the sensors themselves by simply loading and using the appropriate library." Learners starting with programming should use the MicroPython variant. Teachers can hand students a wiring scheme, a sensor-reading code snippet and the library examples, as done in the evaluated lab course.

## Design Implications

### Context
#### Requirements
- Basic interest in the Arduino platform for educators; moderate support for advanced learners; supported hardware per Table 1
#### Constraints
- Adding new device support to the generic BLE interface remains a highly technical task too inaccessible for most science educators

### Target Learners
- science educators without in-depth programming knowledge
- advanced learners
- programming novices

### Target Learning Goals
- building low-cost digital data acquisition experiments
- developing experimentation skills

## Claims

- [In a 36-participant lab course, all students including programming novices succeeded in creating a distance-time plot in phyphox with an ESP32 board and the MicroPython library](../claims/lab-course-36-participants-distance-time-plot-success.md) [+W]
- [Students with low prior microcontroller experience reported feeling confident to use the microcontroller in other projects after the lab course](../claims/self-reported-confidence-microcontroller-after-lab-course.md) [+W]

## Related Strategies

- [Implement collaborative network experiments in other courses using phyphox XML configurations plus a simple PHP server](phyphox-course-implementation-strategy.md)
- [Program micro:bit or Arduino sensor boards so students develop computational thinking while exploring kinematics](missionmotion-sensor-programming-computational-thinking.md)

## Examples
-

## Key Sources
- Staacks, S., Dorsel, D., Krampe, A., Hagedorn, M., Leier, E., Heinke, H., & Stampfer, C. (2023). Bluetooth sensors in phyphox with Arduino and MicroPython – Paving the way from an idea to an experiment for teachers and learners. https://github.com/phyphox/phyphox-arduino
