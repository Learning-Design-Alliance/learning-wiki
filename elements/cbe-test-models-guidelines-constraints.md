---
type: element
id: cbe-test-models-guidelines-constraints
title: Enhanced constraint-based engine (CBE) test models with guidelines and constraints for MAP Growth delivery
description: The constraint-based engine (CBE), originally built for state summative assessments, was enhanced under Project Altair to deliver variable-length MAP Growth interim assessments multiple times a year.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: bo-2020
    resource: "https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/"
    title: "Bo, E., & Meyer, P. (2020). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: An engine evaluation study based on empirical data. Portland, OR: NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/"
    author: "Bo, E., & Meyer, P"
---

# Enhanced constraint-based engine (CBE) test models with guidelines and constraints for MAP Growth delivery

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The constraint-based engine (CBE), originally built for state summative assessments, was enhanced under Project Altair to deliver variable-length MAP Growth interim assessments multiple times a year. On CBE, "blueprint functionality was extended by defining test models in which both guidelines and constraints are used to optimize the content balance requirements and the maximization of ability score precisions." Guidelines are "nice-to-haves," and constraints are "must-haves." Enhancements included momentary ability estimation, a revised item selection algorithm, and longitudinal item exposure as a guideline rather than a constraint.

## Design Implications

### Context
#### Requirements
- Shared item pool and item parameters, student population, online adaptive administration, entry ability values, MLE with fencing rules, and test termination conditions held common with COLO
#### Constraints
- CBE test models were specified to ensure minimum differences from COLO test blueprints, so comparability results reflect near-equivalent blueprint specifications

### Target Learners
- K–8 students taking MAP Growth Reading and Mathematics interim assessments

### Target Learning Goals
- Accurate measurement of student achievement growth in Reading and Mathematics

## Claims

- [The Altair (engine) main effect is not significant for winter RIT scores in either content area, but an Altair-by-sex interaction is significant in Reading only](../claims/altair-effect-null-reading-sex-interaction.md) [+W]
- [CBE shows better engine adaptivity than COLO, especially for extremely low or high achievement students](../claims/cbe-better-adaptivity-extreme-achievers.md) [+W]
- [Item exposure rates are comparable across engines, with most items below 10%, and the CBE Reading item-use rate is lower than COLO's](../claims/cbe-colo-item-exposure-comparable.md) [+W]
- [Marginal reliabilities of MAP Growth winter scores are comparable across engines and all in the 0.90s, with CBE showing slightly higher precision (lower SEM)](../claims/cbe-colo-reliability-comparable-cbe-higher-precision.md) [+W]
- [Test lengths are comparable across engines, but CBE test durations are higher than COLO's in both terms and content areas, more prominently in Reading](../claims/cbe-longer-test-duration-comparable-length.md) [~W]
- [Growth-score differences between CBE and COLO are small, exceeding 0.2 only in Reading Grades K–1 (favoring CBE) and Mathematics Grade 8 (favoring COLO)](../claims/map-growth-cbe-colo-growth-effect-sizes-small.md) [+W]

## Related Elements

- [CBE enhancements for MAP Growth delivery (Project Altair)](cbe-project-altair-enhancements.md)
- [Enhanced CBE simulator in Assessment Integration Management (AIM)](cbe-aim-simulator-capacity.md)
- [NWEA MAP Growth interim assessments](nwea-map-growth-interim-assessments-element.md)

## Examples
-

## Key Sources
- Bo, E., & Meyer, P. (2020). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: An engine evaluation study based on empirical data. Portland, OR: NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-an-engine-evaluation-study-based-on-empirical-data/
