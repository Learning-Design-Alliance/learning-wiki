---
type: design
id: cogtax-four-level-bash-taxonomy
title: "CogTax: a four-level taxonomy for bash command assessment combining cognitive complexity and operational impact"
description: "CogTax classifies bash commands covered in a course by two integrated dimensions: \"cognitive complexity (C)\" and \"operational impact (O)\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.02432"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432"
    author: Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L
---

# CogTax: a four-level taxonomy for bash command assessment combining cognitive complexity and operational impact

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
CogTax classifies bash commands covered in a course by two integrated dimensions: "cognitive complexity (C)" and "operational impact (O)". Levels run from information query/observation (L1, read-only commands such as ls and cat) through basic modifications (L2), structural understanding (L3, pipelines and permissions), to advanced system management (L4). Integration follows L = max(C,O), so a command's level is set by whichever dimension is higher, ensuring instructors and students must address both conceptual mastery and operational awareness.

## Design Implications

### Context
#### Requirements
- Each examination question must be tagged with its taxonomy level so agreement can be analysed as a function of question complexity
#### Constraints
- The article notes the formula requires only at least level-L understanding or at least level-L effects, not necessarily both

### Target Learners
- second-year undergraduate Computer Engineering students in an Operating Systems course

### Learning Goals
- Linux/bash command-line proficiency across information retrieval, file manipulation, structural operations, and advanced system management

### Claims
- Human Scores Decline With Cogtax Level [+M]
- [Llm Scores Decline With Cogtax Level](../claims/llm-scores-decline-with-cogtax-level.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432
