---
type: design
id: ober-plug-in-recommender-architecture
title: OBER plug-in service architecture with swappable recommendation methods
description: "OBER is deployed as a service consisting of business and data layers, with the recommender existing outside the client application; 'the recommendation engine is a separate module', which the authors say makes it easi..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: nursultan-askarbekuly-2025
    resource: "https://arxiv.org/abs/2509.18186v1"
    title: "Nursultan Askarbekuly, Timur Fayzrakhmanov, Sladjan Babarogi´c, Ivan Lukovi´c. (2025). An Outcome-Based Educational Recommender System. https://arxiv.org/abs/2509.18186v1"
    author: Nursultan Askarbekuly, Timur Fayzrakhmanov, Sladjan Babarogi´c, Ivan Lukovi´c
---

# OBER plug-in service architecture with swappable recommendation methods

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
OBER is deployed as a service consisting of business and data layers, with the recommender existing outside the client application; 'the recommendation engine is a separate module', which the authors say makes it easier to have a variety of recommendation methods. In NamazApp they implemented a fixed expert trajectory, collaborative filtering, and knowledge-based filtering that leverages promotes-type alignment mappings.

## Design Implications

### Context
#### Requirements
- The recommendation system runs as an API service outside the client application.
#### Constraints
- 

### Target Learners
- learners of the NamazApp mobile e-learning application

### Learning Goals
- personalized delivery of learning items aligned to intended outcomes

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Nursultan Askarbekuly, Timur Fayzrakhmanov, Sladjan Babarogi´c, Ivan Lukovi´c. (2025). An Outcome-Based Educational Recommender System. https://arxiv.org/abs/2509.18186v1
