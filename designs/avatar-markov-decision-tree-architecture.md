---
type: design
id: avatar-markov-decision-tree-architecture
title: "Interactive clinical avatar software architecture: Markov-model decision tree database, 3D graphic, and real-time linking system"
description: "The avatar software has three essential parts: \"The brain of the avatar is the electronic database based on a modified Markov model design [30], which uses a decision tree to map the progress of a case.\" As the user p..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: jessica-thompson-2020
    resource: "https://doi.org/10.2196/17146"
    title: "Jessica Thompson, Simon White, Stephen Chapman. (2020). Interactive Clinical Avatar Use in Pharmacist Preregistration Training: Design and Review. Journal of Medical Internet Research. https://doi.org/10.2196/17146"
    author: Jessica Thompson, Simon White, Stephen Chapman
---

# Interactive clinical avatar software architecture: Markov-model decision tree database, 3D graphic, and real-time linking system

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The avatar software has three essential parts: "The brain of the avatar is the electronic database based on a modified Markov model design [30], which uses a decision tree to map the progress of a case." As the user progresses, the database monitors the path through the decision tree and collates positive and negative feedback given at the end of the simulation. The body is a computer-generated 3D character modeled and animated in Maya, and the "heart" carries information from brain to body, allowing real-time immediate response. Simulations are stored online in standard HTML with JavaScript handling page logic; free-text input is processed by a server-hosted web service, while multiple-choice processing occurs client side.

## Design Implications

### Context
#### Requirements
- An electronic database of avatar responses, a computer-generated graphic, and a system to link the two together
- For free-text input, a web service hosted on the same server to process text and return codes determining animation and case progression
#### Constraints
- 

### Target Learners
- pharmacist preregistration trainees

### Learning Goals
- decision-making in simulated clinical scenarios

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Jessica Thompson, Simon White, Stephen Chapman. (2020). Interactive Clinical Avatar Use in Pharmacist Preregistration Training: Design and Review. Journal of Medical Internet Research. https://doi.org/10.2196/17146
