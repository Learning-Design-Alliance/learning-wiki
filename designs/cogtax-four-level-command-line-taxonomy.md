---
type: design
id: cogtax-four-level-command-line-taxonomy
title: "CogTax: a four-level cognitive taxonomy integrating cognitive complexity and operational impact via a maximum rule"
description: "CogTax is a four-level cognitive taxonomy for command-line computing education that integrates two dimensions: cognitive complexity C, derived from Bloom's Revised Taxonomy, and operational impact O, the degree to whi..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.00140"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140"
    author: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L"
---

# CogTax: a four-level cognitive taxonomy integrating cognitive complexity and operational impact via a maximum rule

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
CogTax is a four-level cognitive taxonomy for command-line computing education that integrates two dimensions: cognitive complexity C, derived from Bloom's Revised Taxonomy, and operational impact O, the degree to which commands modify system state and the reversibility of those modifications. The article states that "The taxonomy explicitly considers whether actions are observational (read-only, zero risk), reversible (modifiable, low risk), structural (altering logical organization, moderate risk), or administrative (system-wide impact, high complexity)." The taxonomy level is the maximum of the two dimensions, ensuring both conceptual understanding and operational awareness are addressed. It was developed and validated in a second-year undergraduate Linux system administration course.

## Design Implications

### Context
#### Requirements
- Commands must be classifiable along both a cognitive-complexity dimension and an operational-impact dimension; the framework targets command-line domains such as Linux/bash system administration
#### Constraints
- Developed and validated in the context of a second-year undergraduate Linux system administration course; the reviewed literature identifies no prior taxonomy jointly modelling the two dimensions for command-based domains

### Target Learners
- second-year undergraduate Computer Engineering students in an Operating Systems course

### Learning Goals
- command-line and system administration competence spanning read-only inspection through advanced system management

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., & Otero-Cerdeira, L. (2026). CogTax: A Four-Level Cognitive Taxonomy for Command-Line Computing Education. arXiv. https://arxiv.org/abs/2607.00140
