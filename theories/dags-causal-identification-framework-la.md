---
type: theory
title: Directed acyclic graphs as a nonparametric framework for identifying causal effects in learning analytics
description: The article presents DAGs, pioneered by Pearl, as a way of visually encoding causal assumptions among variables of interest so researchers can reason about bias and identification.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: weidlich-2022
    resource: "https://doi.org/10.18608/jla.2022.7577"
    title: "Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577"
    author: Weidlich, J., Gašević, D., Drachsler, H
---

# Directed acyclic graphs as a nonparametric framework for identifying causal effects in learning analytics

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 1 claim rests on one study

## Description
The article presents DAGs, pioneered by Pearl, as a way of visually encoding causal assumptions among variables of interest so researchers can reason about bias and identification. Unlike SEMs, "DAGs are nonparametric in that they make no assumptions about distribution or functional form"; their primary function is graphical identification of causal effects rather than estimation. Constructing a valid DAG requires domain knowledge supplied from outside the data, such as theory and experience.

## Design Implications

### Context
#### Requirements
- Construction of a DAG relies on domain knowledge to convey causal assumptions from outside the data, e.g., experience and theory
#### Constraints
- The framework's usefulness depends on the DAG's degree of correctness; causal assumptions are unlikely to be correct in a binary sense

### Target Learners
- learning analytics researchers

### Target Learning Objectives
- drawing valid causal inferences about learning processes and intervention effects

### Claims

- [Confounding may explain the large retention effects reported for the Course Signals early warning system](../claims/course-signals-confounding-number-of-classes.md) [+M]
- [Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success](../claims/m-bias-gasevic-2016-lms-behaviour.md) [+M]

## Related Theories
- 

## Examples


## Key Sources
- Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577
