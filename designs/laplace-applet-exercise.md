---
type: design
id: laplace-applet-exercise
title: "Laplace applet: a relaxation-method exercise in which students implement the numerical solution of Laplace's equation"
description: "The Laplace applet is a homework exercise built on the fact that a solution of Laplace's equation equals the average of neighboring points."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-22
sources:
  - id: michael-e-peskin-2003
    resource: "https://arxiv.org/abs/physics/0302044"
    title: "Michael E. Peskin. (2003). Abstract Applets: a Method for Integrating Numerical Problem-Solving into the Undergraduate Physics Curriculum. https://arxiv.org/abs/physics/0302044"
    author: Michael E. Peskin
---

# Laplace applet: a relaxation-method exercise in which students implement the numerical solution of Laplace's equation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The Laplace applet is a homework exercise built on the fact that a solution of Laplace's equation equals the average of neighboring points. Students modify one line of Laplace.java to set each array element to the average of its neighbors, and the iterative equilibration yields the solution. The applet displays the phi array in greyscale, lets users paint cathode and ground boundary conditions with the mouse, measure voltage, and compute electrostatic energy via a student-written Energy() function.

## Design Implications

### Context
#### Requirements
- The student modifies only Laplace.java; the parent LaplaceGUI.java, PhysicsApplet.java and Laplace.html are supplied and not to be modified or opened
#### Constraints
- 

### Target Learners
- upper-division undergraduate physics students in electrodynamics

### Learning Goals
- numerical solution of Laplace's equation by relaxation
- qualitative understanding such as the Faraday cage principle
- quantitative estimates such as edge effects on capacitance

### Claims
- 

## Related Designs
- Physicsapplet Java Class Library

## Examples
-

## Key Sources
- Michael E. Peskin. (2003). Abstract Applets: a Method for Integrating Numerical Problem-Solving into the Undergraduate Physics Curriculum. https://arxiv.org/abs/physics/0302044
