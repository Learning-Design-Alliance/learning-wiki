---
type: design
id: dsascratch-three-design-principles
title: "Three design principles for block-based data-structure abstractions: procedural abstraction, extensible blocks, and conversational block naming"
description: "The article organizes the DSAScratch design around three design ideas conforming to Scratch's core principles of being accessible and tinkerable."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: ashwin-jagadeesha-2023
    resource: "https://arxiv.org/abs/2302.11659"
    title: "Ashwin Jagadeesha, Pranathi Rayavaram, Justin Marwad, Sashank Narain, Claire Seungeun Lee. (2023). Integrating Data Structures and Algorithms in K-12 Education using Block-based Programming. https://arxiv.org/abs/2302.11659"
    author: Ashwin Jagadeesha, Pranathi Rayavaram, Justin Marwad, Sashank Narain, Claire Seungeun Lee
---

# Three design principles for block-based data-structure abstractions: procedural abstraction, extensible blocks, and conversational block naming

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article organizes the DSAScratch design around three design ideas conforming to Scratch's core principles of being accessible and tinkerable. First, procedural abstraction abstracts blocks "without losing sight of the core functions of a data structure or algorithm", e.g., a set intersection collapses to a single block. Second, extensible blocks bridge to Scratch's "Make a variable" feature so data structures can be created as Scratch variables. Third, conversational naming gives blocks names like "is set empty?" that resemble a conversation between friends, returning yes or no answers students can inspect.

## Design Implications

### Context
#### Requirements
- Blocks must balance technical detail and abstraction without losing their function, and new blocks must integrate with other Scratch block categories
#### Constraints
- The for each element in loop block was created to be compatible only with DSAScratch's data structures, to avoid interfering with Scratch's existing loop functionality

### Target Learners
- K-12 high school students learning introductory programming

### Learning Goals
- High-level abstraction abilities in Scratch programs
- Familiarity with data structure and algorithm operations

### Claims
- 

## Related Designs
- Dsascratch Scratch Extension Data Structures

## Examples
-

## Key Sources
- Ashwin Jagadeesha, Pranathi Rayavaram, Justin Marwad, Sashank Narain, Claire Seungeun Lee. (2023). Integrating Data Structures and Algorithms in K-12 Education using Block-based Programming. https://arxiv.org/abs/2302.11659
