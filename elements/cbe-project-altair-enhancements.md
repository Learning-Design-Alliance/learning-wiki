---
type: element
id: cbe-project-altair-enhancements
title: CBE enhancements for MAP Growth delivery (Project Altair)
description: As part of Project Altair, NWEA enhanced the constraint-based engine, originally built for state summative assessments, to deliver MAP Growth interim assessments comparably to COLO.
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

# CBE enhancements for MAP Growth delivery (Project Altair)

> **Element** · [All elements](index.md)
> **Evidence** · 9 claims (6 for, 3 mixed) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 9 claims rest on one study

## Description
As part of Project Altair, NWEA enhanced the constraint-based engine, originally built for state summative assessments, to deliver MAP Growth interim assessments comparably to COLO. New features were added "between 2018 and 2019 to accommodate requirements for administering MAP Growth tests in a comparable way to the current MAP Growth engine known as COLO." The enhancements include longitudinal item exposure control, historical-score entry conditions, user-defined fencing-item parameters, item ordering and content balance rules, test termination rules, and test invalidation rules. Users can select which rules to apply in their test models.

## Design Implications

### Context
#### Requirements
- Test models must specify which rules (constraints vs. guidelines) to use for item selection, exposure control, termination, and invalidation
#### Constraints
- Longitudinal item exposure control is a guideline rather than a constraint on the CBE, so repeated items can occur when the item bank cannot fulfill test requirements

### Target Learners
- K-12 students taking MAP Growth interim assessments

### Target Learning Goals
- Accurate measurement of student achievement and growth in reading, mathematics, language usage, and science

## Claims

- [Across administrations, the CBE may re-administer an item to the same student before the longitudinal exposure window elapses when the item bank cannot fulfill test requirements, which COLO does not allow](../claims/cbe-allows-repeated-items-across-administrations.md) [~W]
- [Adaptivity and score reliability of both engines depend on item-pool depth; the CBE often performed better than COLO for extreme low or high achievers when item banks were shallow](../claims/cbe-better-adaptivity-extreme-achievers-shallow-banks.md) [+W]
- [The CBE and COLO engines met content specifications and recovered true scores well for the nine simulated MAP Growth tests](../claims/cbe-colo-comparable-content-validity-theta-recovery.md) [+W]
- [Within a single administration, COLO administered more items and overexposed fewer items than the CBE, likely due to its randomesque exposure-control procedure](../claims/colo-better-within-administration-item-exposure.md) [~W]
- [Marginal reliabilities of MAP Growth winter scores are comparable across engines and all in the 0.90s, with CBE showing slightly higher precision (lower SEM)](../claims/cbe-colo-reliability-comparable-cbe-higher-precision.md) [+W]
- [Growth-score differences between CBE and COLO are small, exceeding 0.2 only in Reading Grades K–1 (favoring CBE) and Mathematics Grade 8 (favoring COLO)](../claims/map-growth-cbe-colo-growth-effect-sizes-small.md) [+W]
- [The Altair (engine) main effect is not significant for winter RIT scores in either content area, but an Altair-by-sex interaction is significant in Reading only](../claims/altair-effect-null-reading-sex-interaction.md) [+W]
- [CBE shows better engine adaptivity than COLO, especially for extremely low or high achievement students](../claims/cbe-better-adaptivity-extreme-achievers.md) [+W]
- [Test lengths are comparable across engines, but CBE test durations are higher than COLO's in both terms and content areas, more prominently in Reading](../claims/cbe-longer-test-duration-comparable-length.md) [~W]

## Related Elements

- [Enhanced constraint-based engine (CBE) test models with guidelines and constraints for MAP Growth delivery](cbe-test-models-guidelines-constraints.md)
- [Enhanced CBE simulator in Assessment Integration Management (AIM)](cbe-aim-simulator-capacity.md)

## Examples
-

## Key Sources
- Hu, A., Chien, M., & Meyer, P. (2021). Comparability of MAP Growth tests administered through different technology and psychometric infrastructure: A simulation study. NWEA. https://www.nwea.org/research/publication/comparability-of-map-growth-tests-administered-through-different-technology-and-psychometric-infrastructure-a-simulation-study/
