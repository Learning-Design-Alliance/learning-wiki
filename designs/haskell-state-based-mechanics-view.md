---
type: design
id: haskell-state-based-mechanics-view
title: State-based view of Newtonian mechanics expressed with Haskell types and an AccelerationFunction
description: "The article's organizing account of mechanics: a system's state is 'characterized by a type; initial conditions for the problem are speciﬁed by a value of that type,' and 'The key information is contained in what we c..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: scott-n-walck-2014
    resource: "https://doi.org/10.4204/EPTCS.170.5"
    title: "Scott N. Walck. (2014). Learn Physics by Programming in Haskell. EPTCS 170. https://doi.org/10.4204/EPTCS.170.5"
    author: Scott N. Walck
---

# State-based view of Newtonian mechanics expressed with Haskell types and an AccelerationFunction

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's organizing account of mechanics: a system's state is 'characterized by a type; initial conditions for the problem are speciﬁed by a value of that type,' and 'The key information is contained in what we call an AccelerationFunction.' Writing an acceleration function specifies a system of first-order differential equations; iterating a step function yields 'an inﬁnite list of State values' that students use for plotting or animation.

## Design Implications

### Context
#### Requirements
- Students must first learn a Haskell subset of types, functions and higher-order functions; the course budgets 'about seven weeks' for this.
#### Constraints
- The course intentionally avoids explicit recursion and omits 'the creation of new algebraic data types.'

### Target Learners
- second-year undergraduate physics students

### Learning Goals
- expressing Newtonian mechanics as types and functions
- solving equations of motion numerically

### Claims
- [Haskell Programming Deepens Physics Understanding](../claims/haskell-programming-deepens-physics-understanding.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Scott N. Walck. (2014). Learn Physics by Programming in Haskell. EPTCS 170. https://doi.org/10.4204/EPTCS.170.5
