---
type: design
id: precompiled-plans-course-generation
title: Precompiled-plan planning and execution framework for course sequencing and delivery
description: The framework adapts the Procedural Reasoning System (PRS) control architecture, using a planning and execution module, a goal stack, and a knowledge base.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: michalowski-martin-2021
    resource: "https://doi.org/10.3390/ijerph18147355"
    title: "Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor. (2021). A Health eLearning Ontology and Procedural Reasoning Approach for Developing Personalized Courses to Teach Patients about Their Medical Condition and Treatment. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph18147355"
    author: "Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor"
---

# Precompiled-plan planning and execution framework for course sequencing and delivery

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The framework adapts the Procedural Reasoning System (PRS) control architecture, using a planning and execution module, a goal stack, and a knowledge base. Precompiled plans specify a goal, optional preconditions, and a procedural body, and are used to sequence lessons within a course, sequence BUKs within a lesson, and control interaction with the patient. The plans are grouped into four levels, with single plans at Levels 1, 2 and 4 and two plans at Level 3 for delivering content and Q&A BUKs. The authors argue this "offers more flexibility and allows for more complex course strategies for course development and delivery than only rule- or ontology-based approaches."

## Design Implications

### Context
#### Requirements
- Precompiled plans are processed by the planning and execution module and combined with knowledge-base content derived from the eLearning ontology
#### Constraints
- OWL does not natively support complex sequencing, which motivated the procedural reasoning approach

### Target Learners
- patients receiving generated personalized courses in an outpatient setting

### Learning Goals
- sequenced learning of condition and treatment knowledge matched to patient characteristics

### Claims
- 

## Related Designs

- [Multi-agent AI tutoring architecture with an orchestrating Tutor Agent and specialist agents](multi-agent-ai-math-tutor-architecture.md)
- [Four-module architecture for language-driven robot control in educational simulation](edusim-llm-four-module-architecture.md)
- [Intelligent tutoring systems as three-model architectures operationalizing formative assessment](its-three-core-components-architecture.md)

## Examples
-

## Key Sources
- Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor. (2021). A Health eLearning Ontology and Procedural Reasoning Approach for Developing Personalized Courses to Teach Patients about Their Medical Condition and Treatment. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph18147355
