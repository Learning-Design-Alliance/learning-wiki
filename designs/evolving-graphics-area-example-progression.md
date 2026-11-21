---
type: design
id: evolving-graphics-area-example-progression
title: One evolving example introduces each object-oriented concept in a linked progression from encapsulation to polymorphism
description: "The article's theory teaching centres on a single graphics-area example that grows: a Circle class with public radius motivates making radius private and adding setRadius(), which introduces \"the concept of encapsulat..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: guowu-yuan-2021
    resource: "https://doi.org/10.1109/TMI.2021.3068404"
    title: "Guowu Yuan, Bing Kong, Haiyan Ding, Jixian Zhang, Yang Zhao. (2021). Teaching Reform and Exploration on Object-Oriented Programming. https://doi.org/10.1109/TMI.2021.3068404"
    author: Guowu Yuan, Bing Kong, Haiyan Ding, Jixian Zhang, Yang Zhao
---

# One evolving example introduces each object-oriented concept in a linked progression from encapsulation to polymorphism

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's theory teaching centres on a single graphics-area example that grows: a Circle class with public radius motivates making radius private and adding setRadius(), which introduces "the concept of encapsulation"; inconvenience of setting radius after each definition "derives" the construction method; object counting introduces static variables; the Cylinder class, whose "bottom surface of a cylinder is a circle", introduces inheritance; and triangles and rectangles with a unified getArea() under an abstract Graphics superclass introduce polymorphism. The same example later grounds a GUI assignment calculating all figures' areas.

## Design Implications

### Context
#### Requirements
- A base example rich enough that each new concept arises from a genuine limitation of the previous design
#### Constraints
- Printed only as the authors' design; the article reports no comparison of this progression with concept-by-concept teaching

### Target Learners
- undergraduates learning object-oriented programming with Java

### Learning Goals
- understanding encapsulation, constructors, static variables, inheritance and polymorphism as linked concepts

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Guowu Yuan, Bing Kong, Haiyan Ding, Jixian Zhang, Yang Zhao. (2021). Teaching Reform and Exploration on Object-Oriented Programming. https://doi.org/10.1109/TMI.2021.3068404
