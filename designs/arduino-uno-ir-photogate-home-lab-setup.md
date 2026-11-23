---
type: design
id: arduino-uno-ir-photogate-home-lab-setup
title: Low-cost Arduino UNO R3 datalogging setup with IR transmitter-receiver pair for home physics experiments
description: "This element is a home-laboratory measurement setup combining a mechanical pendulum (wood support, nylon string, spherical mass) with an electronic system: an \"Arduino UNO R3 board, an IR trasmitter-receiver pair sens..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: fausto-casaburo-2021
    resource: "https://arxiv.org/abs/2107.10792"
    title: "Fausto Casaburo. (2021). Teaching Physics by Arduino during COVID-19 Pandemic: Oscillation of a simple pendulum. arXiv preprint. https://arxiv.org/abs/2107.10792"
    author: Fausto Casaburo
---

# Low-cost Arduino UNO R3 datalogging setup with IR transmitter-receiver pair for home physics experiments

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
This element is a home-laboratory measurement setup combining a mechanical pendulum (wood support, nylon string, spherical mass) with an electronic system: an "Arduino UNO R3 board, an IR trasmitter-receiver pair sensors, a breadboard, Dupont cables, USB cable and one computer". The IR sensors on a hand-made U-shape support form a hand-made photogate positioned so the pendulum mass passes through the beam. Arduino is described as an open-source platform whose "versatility and low cost" make it ideal for constructing datalogging sensors for physics experiments.

## Design Implications

### Context
#### Requirements
- An Arduino board with IR pair sensors connected to a digital pin, a computer for data acquisition by USB cable, and free introductory on-line tutorials for beginners
#### Constraints
- The original board costs about few tens of euro and kits about 50-60 euro, which the article presents as an affordability feature rather than a limitation

### Target Learners
- high school students
- university students

### Learning Goals
- measuring the gravitational acceleration from pendulum oscillation
- acquiring coding and programming competences

### Claims
- Ir Pair Sensor Replaces Photogate Period Measurement [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Fausto Casaburo. (2021). Teaching Physics by Arduino during COVID-19 Pandemic: Oscillation of a simple pendulum. arXiv preprint. https://arxiv.org/abs/2107.10792
