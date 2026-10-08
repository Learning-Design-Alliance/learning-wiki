---
type: strategy
id: procedure-for-applying-l-star
title: "Recommended procedure for applying L* to sequences of affective states"
description: "The article outlines a step-by-step procedure (Algorithm 1) for computing L* on full affect sequences with transitions to A excluded."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: jeffrey-matayoshi-and-shamya-karumbaiah-2020
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478"
    title: "Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478"
    author: Jeffrey Matayoshi and Shamya Karumbaiah
---

# Recommended procedure for applying L* to sequences of affective states

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article outlines a step-by-step procedure (Algorithm 1) for computing L* on full affect sequences with transitions to A excluded. The algorithm explicitly handles special cases that would produce undefined values or division-by-zero errors, such as sequences consisting solely of transitions of the form Aprev→Bnext, where "L∗ is undeﬁned." After computing L* per student, the authors recommend "a two-tailed t-test can then be used on the entire sample of L∗ values" and a Benjamini-Yekutieli post hoc correction with an α value of 0.05 to control false positives under arbitrary dependence.

## Design Implications

### Context
#### Requirements
- Start with full affect sequences including all self-transitions
- Handle undefined cases explicitly (no transitions from A, or sequences solely of AB transitions when using individual base rates)
- Apply Benjamini-Yekutieli correction with α = 0.05 when testing multiple transition pairs
#### Constraints
- When base rates are computed individually, sequences with at most one transition in T_A fall into special cases where L* is undefined or zero

### Target Learners
- researchers analyzing affect dynamics data from students in digital learning environments

### Target Learning Goals
- valid analysis of affective state transitions when self-transitions are excluded

## Related Strategies
- 

## Examples
-

## Key Sources
- Jeffrey Matayoshi and Shamya Karumbaiah. (2020). Adjusting the L Statistic when Self-Transitions are Excluded in Affect Dynamics. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/478
