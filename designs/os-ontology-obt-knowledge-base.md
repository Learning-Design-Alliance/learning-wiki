---
type: design
id: os-ontology-obt-knowledge-base
title: Operating Systems ontology built for OBT (344 classes, 57 object properties, 10 data properties)
description: "Because no existing ontology was available for the Operating Systems course, one of the authors hand-built the domain ontology in Protégé over 25 to 30 days; \"In terms of size, this OS ontology comprises 57 object pro..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: praveen-kumar-2024
    resource: "https://doi.org/10.1007/s40593-023-00333-6"
    title: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6"
    author: "Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K"
---

# Operating Systems ontology built for OBT (344 classes, 57 object properties, 10 data properties)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Because no existing ontology was available for the Operating Systems course, one of the authors hand-built the domain ontology in Protégé over 25 to 30 days; "In terms of size, this OS ontology comprises 57 object properties, 10 data properties, and 344 classes." It models concepts such as 'Computer', 'Hardware', 'OperatingSystem', and 'Interrupt', with TBox axioms (subset and equivalence, e.g., 'MainMemory ≡ PhysicalMemory') and ABox axioms feeding the ITree-to-question transformation.

## Design Implications

### Context
#### Requirements
- Semi-automatic construction in Protégé with DL/SWRL rules added to extend semantics; a naming convention for classes and properties
#### Constraints
- Building the ontology took 25 to 30 days of expert effort, illustrating the semantic approach's upfront cost

### Target Learners
- students of the Operating Systems course

### Learning Goals
- Wh-type MCQ stem generation grounded in domain semantics

### Claims
- Hybrid Obt Mbt Mcq Generation Framework [+M]

## Related Designs

- [Structured autonomy: bounding generative agent behavior through layered pedagogical and domain constraints](structured-autonomy-agentic-learning-framework.md)

## Examples
-

## Key Sources
- Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6
