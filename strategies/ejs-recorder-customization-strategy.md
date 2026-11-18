---
type: strategy
id: ejs-recorder-customization-strategy
title: Customize recorded simulation data using the _recorder object to match the research question
description: The article recommends that LA and EDM researchers inspect an existing EJS simulation and use its _recorder object to fine-tune what interaction information is captured and when it is sent to the repository.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: francisco-esquembre-2019
    resource: "https://github.com/felixgarcia/ejss-moodle-plugin"
    title: "Francisco Esquembre, Félix J. García Clemente, Rafael Chicón, Lawrence Wee, Leong Tze Kwang & Darren Tan. (2019). Easy Java/JavaScript Simulations as a tool for Learning Analytics. Proceedings of the 27th International Conference on Computers in Education. https://github.com/felixgarcia/ejss-moodle-plugin"
    author: "Francisco Esquembre, Félix J. García Clemente, Rafael Chicón, Lawrence Wee, Leong Tze Kwang & Darren Tan"
---

# Customize recorded simulation data using the _recorder object to match the research question

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that LA and EDM researchers inspect an existing EJS simulation and use its _recorder object to fine-tune what interaction information is captured and when it is sent to the repository. Instead of collecting every click, researchers can record selected model variables on each interaction or add non-interaction-triggered records when a programmatic condition occurs. The article calls this customization perhaps the main advantage of using EJS simulations in learning analytics, since hundreds of existing simulations in public libraries can be repurposed this way.

## Design Implications

### Context
#### Requirements
- Access to the simulation source code with the EJS authoring tool so the model can be edited to call _recorder functions
#### Constraints
- The purpose and needs of the researcher must be guessed in advance; the authors state they will expand _recorder capabilities as new features are requested

### Target Learners
- students interacting with simulations in online courses

### Target Learning Goals
- capturing fine-grained evidence of inquiry-based learner strategies and learning procedures

### Affordances
- [Ejs Learning Analytics Architecture](../designs/ejs-learning-analytics-architecture.md)

## Related Strategies

- [Remix existing open source simulation models into inquiry learning environments matched to the local syllabus](remix-open-source-simulations-for-inquiry-strategy.md)
- [Teacher professional development through customizing Open Source Physics simulation templates](teacher-pd-customizing-osp-simulations.md)
- [Hands-on workshop sequence: study an existing model, modify it, then self-direct a personal customization project](ejs-hands-on-model-modification-workshop-strategy.md)

## Examples
-

## Key Sources
- Francisco Esquembre, Félix J. García Clemente, Rafael Chicón, Lawrence Wee, Leong Tze Kwang & Darren Tan. (2019). Easy Java/JavaScript Simulations as a tool for Learning Analytics. Proceedings of the 27th International Conference on Computers in Education. https://github.com/felixgarcia/ejss-moodle-plugin
