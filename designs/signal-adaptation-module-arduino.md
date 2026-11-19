---
type: design
id: signal-adaptation-module-arduino
title: "Signal adaptation module: Arduino interpreting the analog force signal and triggering the shooting module"
description: "The third module's entry signal comes from the force interaction module and its output allows current to circulate around the coil in the shooting module."
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

# Signal adaptation module: Arduino interpreting the analog force signal and triggering the shooting module

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The third module's entry signal comes from the force interaction module and its output allows current to circulate around the coil in the shooting module. "A programable interpreter needs to be used to manipulate the analog input signal and produce an output signal, this interpreter is commonly an Arduino." The Arduino lights the red, yellow, or green LED for the force category, keeps a blue standby LED lit until a hit is detected, and then triggers the shooting module. The Arduino code is provided in supplementary material Section A.

## Design Implications

### Context
#### Requirements
- A programmable interpreter (commonly an Arduino) to manipulate the analog input signal and produce an output signal
#### Constraints
- 

### Target Learners
- undergraduate students in an introductory electromagnetism physics course

### Learning Goals
- signal interpretation and interfacing between sensor and actuator

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Arturo Pazmino, Luis Pabón, Esther Desiree Gutiérrez M., Erick Lamilla, and Eduardo Montero. (2022). Learning Electromagnetism through a playful fair-game project. Submitted to The Physics Teacher. https://www.espol.edu.ec
