---
type: design
id: oo-inheritance-separates-physics-from-interface
title: Object-oriented parent-daughter class inheritance as the mechanism separating student physics code from interface code
description: "The article's organizing framework is Java's object-oriented class structure: a daughter class inherits the variables and methods of a parent, and an abstract class defines methods in principle without implementing them."
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

# Object-oriented parent-daughter class inheritance as the mechanism separating student physics code from interface code

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's organizing framework is Java's object-oriented class structure: a daughter class inherits the variables and methods of a parent, and an abstract class defines methods in principle without implementing them. The chain Applet → PhysicsApplet → LaplaceGUI leaves only the physics methods solve() and Energy() undefined, so the student's Laplace class completes the structure while all interface methods remain hidden. The author states that "the hierarchial structure of the object-oriented Jav a programming language makes this system straightforward to implement."

## Design Implications

### Context
#### Requirements
- A language supporting parent-daughter inheritance and abstract classes with unimplemented methods
- The daughter class must define all required abstract methods before it can be instantiated
#### Constraints
- The method is presented for Java, though the author notes the strategy could be carried out in other languages with easy access to graphical user interface components, such as Visual Basic

### Target Learners
- upper-division undergraduate physics students

### Learning Goals
- writing numerical algorithms without mastering user-interface programming

### Claims
- 

## Related Designs
- Physicsapplet Java Class Library

## Examples
-

## Key Sources
- Michael E. Peskin. (2003). Abstract Applets: a Method for Integrating Numerical Problem-Solving into the Undergraduate Physics Curriculum. https://arxiv.org/abs/physics/0302044
