---
type: principle
id: item-deletion-only-if-reliability-improves
title: Delete items only when test reliability improves upon deletion
description: "The article proposes a data-driven item-deletion procedure: identify candidate items via the k0 intersection acceptance region (k0 ± 2SD of item scores, difficulty or discriminating values), skewness of the parameter..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: chakrabartty-2021
    resource: "https://dx.doi.org/10.52380/ijpes.2021.8.3.190"
    title: "Chakrabartty, S. N. (2021). Assessment of item and test parameters: Cosine similarity approach. International Journal of Psychology and Educational Studies, 8(3), 28-38. https://dx.doi.org/10.52380/ijpes.2021.8.3.190"
    author: Chakrabartty, S. N
---

# Delete items only when test reliability improves upon deletion

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 for) · 1 study, `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a data-driven item-deletion procedure: identify candidate items via the k0 intersection acceptance region (k0 ± 2SD of item scores, difficulty or discriminating values), skewness of the parameter distributions, or marginal point-biserial item reliability, but it states plainly that "Deletion of items is advisable only when reliability of the test improves upon deletion." Deletion changes both test difficulty and discriminating values, so impact must be checked before removing items.

## Design Implications

### Context
#### Requirements
- Compute item difficulty and discriminating values and the k0 intersection point; recompute test reliability and error variance after any candidate deletion
#### Constraints
- (k0 ± 3SD) may result in discarding too few items; choice of ∆ may depend on original number of items, type of test, and whether the test measures single or multiple dimensions
- Items must not be deleted if test reliability gets reduced or error variance of the test gets increased

### Target Learners
- test developers and psychometricians assessing binary-item tests

### Target Learning Objectives
- improving test discrimination and reliability through item selection

### Claims
- [K0 Intersection Item Deletion Criterion](../claims/k0-intersection-item-deletion-criterion.md) [+M]
- [Point Biserial Negative Test Discrimination Relation](../claims/point-biserial-negative-test-discrimination-relation.md) [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Chakrabartty, S. N. (2021). Assessment of item and test parameters: Cosine similarity approach. International Journal of Psychology and Educational Studies, 8(3), 28-38. https://dx.doi.org/10.52380/ijpes.2021.8.3.190
