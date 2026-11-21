---
type: design
id: reordered-java-teaching-sequence
title: "Reordered teaching sequence: Java-vs-C syntax differences first, then Java system classes, then object-oriented concepts through one evolving example"
description: "The article proposes replacing the conventional book order (history, syntax, then class/object/encapsulation/inheritance/polymorphism) with a sequence that starts from the \"difference of basic syntax between Java and..."
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

# Reordered teaching sequence: Java-vs-C syntax differences first, then Java system classes, then object-oriented concepts through one evolving example

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article proposes replacing the conventional book order (history, syntax, then class/object/encapsulation/inheritance/polymorphism) with a sequence that starts from the "difference of basic syntax between Java and C language", then demonstrates several Java system classes such as String and JFrame so students "know the benefits of object-oriented programming by the implementation of some small programs", and only then introduces object-oriented concepts. The authors argue this fits students who already hold a structured-programming mindset and that "it can achieve better result to adjust the order of teaching content".

## Design Implications

### Context
#### Requirements
- Students must already have a C-language foundation so that only syntax differences need to be taught
- A set of Java system classes (String, Frame/JFrame) available for demonstration before formal OO concepts
#### Constraints
- The article frames the sequence for schools whose first programming language is C; no evaluation of the sequence against the old order is printed

### Target Learners
- undergraduate computer science majors in the third semester

### Learning Goals
- transitioning from structured-programming thinking to object-oriented thinking
- understanding encapsulation, construction methods, static variables, inheritance and polymorphism

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Guowu Yuan, Bing Kong, Haiyan Ding, Jixian Zhang, Yang Zhao. (2021). Teaching Reform and Exploration on Object-Oriented Programming. https://doi.org/10.1109/TMI.2021.3068404
