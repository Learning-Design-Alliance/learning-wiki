---
type: design
id: ejs-learning-analytics-architecture
title: "EJS learning analytics scenario: simulations plus LMS plus Learning Record Store with a customizable _recorder"
description: "The article proposes an architecture in which EJS-generated simulations send real-time interaction data to an external repository: an LMS serves the simulation within a curricular unit, and a Learning Record Store (LR..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: francisco-esquembre-2019
    resource: "https://github.com/felixgarcia/ejss-moodle-plugin"
    title: "Francisco Esquembre, Félix J. García Clemente, Rafael Chicón, Lawrence Wee, Leong Tze Kwang & Darren Tan. (2019). Easy Java/JavaScript Simulations as a tool for Learning Analytics. Proceedings of the 27th International Conference on Computers in Education. https://github.com/felixgarcia/ejss-moodle-plugin"
    author: "Francisco Esquembre, Félix J. García Clemente, Rafael Chicón, Lawrence Wee, Leong Tze Kwang & Darren Tan"
---

# EJS learning analytics scenario: simulations plus LMS plus Learning Record Store with a customizable _recorder

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article proposes an architecture in which EJS-generated simulations send real-time interaction data to an external repository: an LMS serves the simulation within a curricular unit, and a Learning Record Store (LRS) stores all user interactions together with user context such as test grades. The EJS library captures three default interaction types — mouse and touch events, actions on view elements (e.g. OnClick and OnDrag), and actions on the model (play, pause, step, reset, initialize) — detailed enough to reproduce a user session like a video player. A built-in _recorder object lets researchers fine-tune which model variables are sent and when, so features can be matched to the pedagogic research question rather than following an all-the-information-we-can-get policy.

## Design Implications

### Context
#### Requirements
- A server must serve the simulation HTML page, and an LRS must be integrated into an LMS to store interactions and contextual user information
#### Constraints
- The full interaction record alone may be insufficient or overkill for some studies, and machine learning on every click risks overfitting and poor generalization

### Target Learners
- students using simulations in online or unsupervised courses

### Learning Goals
- understanding students' interaction strategies and learning procedures with simulations

### Claims
- 

## Related Designs
- Ejs Authoring Toolkit
- Ejs Moodle Plugin Learning Analytics

## Examples
-

## Key Sources
- Francisco Esquembre, Félix J. García Clemente, Rafael Chicón, Lawrence Wee, Leong Tze Kwang & Darren Tan. (2019). Easy Java/JavaScript Simulations as a tool for Learning Analytics. Proceedings of the 27th International Conference on Computers in Education. https://github.com/felixgarcia/ejss-moodle-plugin
