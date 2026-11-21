---
type: design
id: four-part-robotics-pipeline-course-structure
title: Four-part course structure following the robotics pipeline with real-time deployment on a microcontroller
description: The course is organized in four sequential parts — simulation, controls, state estimation, and motion planning — following a standard robotics pipeline.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: wolfgang-hönig-2026
    resource: "https://arxiv.org/abs/2604.00032"
    title: "Wolfgang Hönig, Christoph Scherer, and Khaled Wahba. (2026). Rusty Flying Robots: Learning a Full Robotics Stack with Real-Time Operation on an STM32 Microcontroller in a 9 ECTS MS Course. https://arxiv.org/abs/2604.00032"
    author: Wolfgang Hönig, Christoph Scherer, and Khaled Wahba
---

# Four-part course structure following the robotics pipeline with real-time deployment on a microcontroller

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The course is organized in four sequential parts — simulation, controls, state estimation, and motion planning — following a standard robotics pipeline. In each part students learn "mathematical foundations and implementing their own major parts of a modern flight stack", with code written in embedded Rust that must be successfully deployed on an STM32 microcontroller computing control actions and state estimates in real-time. Assignments are graded on "the functionality, code quality, and ability for students to answer questions about their code".

## Design Implications

### Context
#### Requirements
- Each assignment is graded on functionality, code quality, and the ability for students to answer questions about their code, including in oral discussions where generative AI tools are allowed but code comprehension is required.
#### Constraints
- Each offering is limited to 10 students due to its practical nature with occasional 1-on-1 coaching.

### Target Learners
- masters students in Computer Science, Computer Engineering, or Electrical Engineering

### Learning Goals
- implementing dynamics, nonlinear control, state estimation, and motion planning for real-time flight on embedded hardware

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Wolfgang Hönig, Christoph Scherer, and Khaled Wahba. (2026). Rusty Flying Robots: Learning a Full Robotics Stack with Real-Time Operation on an STM32 Microcontroller in a 9 ECTS MS Course. https://arxiv.org/abs/2604.00032
