---
type: design
id: force-interaction-module-leds
title: "Force interaction module: hammer-and-target sensor with color-coded force LEDs"
description: "The first module is \"a hammer and a target\"; once the player hits the target, LEDs light by means of a mechanical-electrical transducer, with red indicating low force, yellow medium, and green high."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: arturo-pazmino-2022
    resource: "https://www.espol.edu.ec"
    title: "Arturo Pazmino, Luis Pabón, Esther Desiree Gutiérrez M., Erick Lamilla, and Eduardo Montero. (2022). Learning Electromagnetism through a playful fair-game project. Submitted to The Physics Teacher. https://www.espol.edu.ec"
    author: Arturo Pazmino, Luis Pabón, Esther Desiree Gutiérrez M., Erick Lamilla, and Eduardo Montero
---

# Force interaction module: hammer-and-target sensor with color-coded force LEDs

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The first module is "a hammer and a target"; once the player hits the target, LEDs light by means of a mechanical-electrical transducer, with red indicating low force, yellow medium, and green high. Students define the force ranges according to their tracks. Some solutions used a piezoelectric with a non-inverting amplifier (741 OpAmp) because students tend to hit too hard and might break the sensor, and a flex module on a plastic sheet cushions the impact.

## Design Implications

### Context
#### Requirements
- A mechanical-electrical transducer feeds the Arduino input signal
- A flex module adapted to a plastic sheet is used to cushion the impact because students tend to hit too hard
#### Constraints
- The force ranges for low, medium, and high depend on each prototype and are defined by students according to their tracks

### Target Learners
- undergraduate students in an introductory electromagnetism physics course

### Learning Goals
- transduction of mechanical force into electrical signal

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Arturo Pazmino, Luis Pabón, Esther Desiree Gutiérrez M., Erick Lamilla, and Eduardo Montero. (2022). Learning Electromagnetism through a playful fair-game project. Submitted to The Physics Teacher. https://www.espol.edu.ec
