---
type: design
id: pediatric-laparoscopic-box-trainer-motion-grip-sensors
title: Custom instrumented pediatric laparoscopic box trainer with magnetic motion tracking and flex-sensor grip measurement
description: "A custom pediatric box trainer (\"35.6 cm wide by 35.6 cm long by 7.0 cm tall\") with rigid sides, a compliant arched top, 3D-printed trocars, and simulated bowel, designed to reproduce the ergonomic constraints of pedi..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-09
sources:
  - id: oquendo-yousi-a-2017
    resource: "https://doi.org/10.1007/s00464-017-5873-6"
    title: "Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6"
    author: Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J
---

# Custom instrumented pediatric laparoscopic box trainer with magnetic motion tracking and flex-sensor grip measurement

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A custom pediatric box trainer ("35.6 cm wide by 35.6 cm long by 7.0 cm tall") with rigid sides, a compliant arched top, 3D-printed trocars, and simulated bowel, designed to reproduce the ergonomic constraints of pediatric surgery. It is instrumented with an Ascension trakSTAR electromagnetic system tracking both tools and the endoscope at approximately 20 Hz, plus handle-mounted flex sensors measuring grip angle sampled by an Arduino Uno. The apparatus records trial video and sensor streams used to generate 280 motion analysis features for automated skill scoring.

## Design Implications

### Context
#### Requirements
- Requires calibration of tool-mounted sensors against a calibration rig and per-subject flex sensor calibration; metallic components near the transmitter must be removed or shielded to avoid signal interference
#### Constraints
- The design includes customized electrical and software components the authors state would be difficult for non-engineers to replicate; sensors attached externally on the tools cause some inevitable interference due to the small size of the box trainer and its tools

### Target Learners
- medical students
- surgical residents
- surgical fellows

### Learning Goals
- pediatric laparoscopic intracorporeal suturing skill
- objective technical skill assessment

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Oquendo Yousi A., Riddle Elijah W., Hiller Dennis, Blinman Thane A., Kuchenbecker Katherine J. (2017). Automatically rating trainee skill at a pediatric laparoscopic suturing task. Surgical Endoscopy. https://doi.org/10.1007/s00464-017-5873-6
