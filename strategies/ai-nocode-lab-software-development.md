---
type: strategy
id: ai-nocode-lab-software-development
title: Use generative AI as a no-code development tool so instructors can design laboratory software around their own pedagogical objectives
description: The article demonstrates producing a customized measurement application entirely through natural-language prompting, with no manual coding, by refining the specification until the interface met requirements and then a...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: josep-ll-suñer-2026
    resource: "https://smartphysics.webs.upv.es/rotation-lab"
    title: "Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab"
    author: Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí
---

# Use generative AI as a no-code development tool so instructors can design laboratory software around their own pedagogical objectives

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article demonstrates producing a customized measurement application entirely through natural-language prompting, with no manual coding, by refining the specification until the interface met requirements and then asking the assistant for a consolidated prompt that regenerates the final version in one step. Instructors can thus design software around pedagogical objectives — presenting only relevant variables, simplifying the interface, removing unnecessary controls — which the authors say drastically reduces development time and eliminates the need for advanced programming skills.

## Design Implications

### Context
#### Requirements
- Refining the specification until the interface meets the instructor's requirements; only the block describing measured quantities is physics-specific, which makes the prompt reusable as a template
#### Constraints
- In the activity as implemented, the AI assistant intervenes before instruction rather than during it; students interact only with the resulting application, not with the assistant itself

### Target Learners
- physics instructors developing laboratory activities

### Target Learning Goals
- customized measurement interfaces aligned with specific physics activities

## Related Strategies

- Smartphysics Rotation Lab App
- [A proposed but not yet classroom-evaluated extension: have students write and refine the measurement-application prompt themselves](students-write-measurement-app-prompts.md)
- [Computing instructors should approach GenAI slide generation as programmers: work iteratively with coding assistants and text-based slide toolchains](instructors-as-programmers-genai-slides.md)
- [Use a natural-language strategy guideline in the generator prompt so tutoring strategy can be revised without code changes](collearn-natural-language-strategy-guideline.md)
- [Iterate the prompt in plain language and validate the simulation on technical, physical, and pedagogical levels](iterate-and-three-level-validation-ar-simulation-strategy.md)

## Examples
-

## Key Sources
- Josep Ll. Suñer, Francisco M. Muñoz-Pérez, Juan C. Castro-Palacio, Juan A. Monsoriu, Martín Monteiro, Cecilia Stari, and Arturo C. Martí. (2026). Uniform and Accelerated Circular Motion with a Smartphone: A No-Code, AI-Generated Browser Laboratory. https://smartphysics.webs.upv.es/rotation-lab
