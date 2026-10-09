---
type: theory
title: "Two adaptive item-selection architectures: sequential maximum-information selection (COLO) versus whole-test shadow-test assembly (CBE)"
description: The report contrasts two fundamentally different adaptive testing architectures operating under the Rasch model.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: hu-2021
    resource: "https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/"
    title: "Hu, A., Chien, M., & Meyer, P. (2021). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: A simulation study. NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/"
    author: "Hu, A., Chien, M., & Meyer, P"
---

# Two adaptive item-selection architectures: sequential maximum-information selection (COLO) versus whole-test shadow-test assembly (CBE)

> **Theory** · [All theories](index.md)
> **Evidence** · 8 claims (7 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 8 claims rest on one study

## Description
The report contrasts two fundamentally different adaptive testing architectures operating under the Rasch model. COLO employs the Kingsbury and Zara algorithm, selecting one item at a time based on maximum Fisher information with content balancing by item count and SEM; "COLO selects one item at a time quickly but does not look ahead at the remaining assessment, which can lead to constraint conflicts." The CBE instead leverages "a modified shadow test approach (van der Linden & Reese, 1998) and weighted penalty model (Segall & Davey, 1995)", constructing a student-specific plan (SSP) that guarantees content and other constraints are fulfilled before items are ordered. Constraints are must-haves; guidelines are nice-to-haves the engine may violate to meet more important rules.

## Design Implications

### Context
#### Requirements
- An item pool sufficient to assemble feasible student-specific plans meeting blueprint constraints
#### Constraints
- The shadow test approach was originally proposed for fixed-length tests; variable-length MAP Growth tests required new item ordering rules to prevent content constraint violations

### Target Learners
- K-12 students taking adaptive assessments

### Target Learning Objectives
- Accurate and content-valid adaptive measurement of student ability

### Claims

- [Cbe Colo Comparable Content Validity Theta Recovery](../claims/cbe-colo-comparable-content-validity-theta-recovery.md) [+M]
- [Cbe Better Adaptivity Extreme Achievers Shallow Banks](../claims/cbe-better-adaptivity-extreme-achievers-shallow-banks.md) [~M]
- [Across administrations, the CBE may re-administer an item to the same student before the longitudinal exposure window elapses when the item bank cannot fulfill test requirements, which COLO does not allow](../claims/cbe-allows-repeated-items-across-administrations.md) [+W]
- [Within a single administration, COLO administered more items and overexposed fewer items than the CBE, likely due to its randomesque exposure-control procedure](../claims/colo-better-within-administration-item-exposure.md) [+W]
- [CBE shows better engine adaptivity than COLO, especially for extremely low or high achievement students](../claims/cbe-better-adaptivity-extreme-achievers.md) [+W]
- [Item exposure rates are comparable across engines, with most items below 10%, and the CBE Reading item-use rate is lower than COLO's](../claims/cbe-colo-item-exposure-comparable.md) [+W]
- [Marginal reliabilities of MAP Growth winter scores are comparable across engines and all in the 0.90s, with CBE showing slightly higher precision (lower SEM)](../claims/cbe-colo-reliability-comparable-cbe-higher-precision.md) [+W]
- [Test lengths are comparable across engines, but CBE test durations are higher than COLO's in both terms and content areas, more prominently in Reading](../claims/cbe-longer-test-duration-comparable-length.md) [+W]

## Related Theories
- 

## Examples

- [CBE enhancements for MAP Growth delivery (Project Altair)](../elements/cbe-project-altair-enhancements.md)
- [Enhanced constraint-based engine (CBE) test models with guidelines and constraints for MAP Growth delivery](../elements/cbe-test-models-guidelines-constraints.md)

## Key Sources
- Hu, A., Chien, M., & Meyer, P. (2021). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: A simulation study. NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/
