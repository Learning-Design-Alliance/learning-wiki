---
type: theory
title: "ARLIS: Algorithm for Reward Listed Item Selection"
description: ARLIS is the enhanced MAP Growth item-selection algorithm introduced by the Content Proximity Project.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: j-patrick-meyer-2023
    resource: "https://www.nwea.org/research/publication/content-proximity-spring-2022-pilot-study-research-report/"
    title: "J. Patrick Meyer, Ann Hu, Sylvia Li. (2023). Content Proximity Spring 2022 Pilot Study Research Brief. Psychometric Solutions, NWEA. https://www.nwea.org/research/publication/content-proximity-spring-2022-pilot-study-research-report/"
    author: J. Patrick Meyer, Ann Hu, Sylvia Li
---

# ARLIS: Algorithm for Reward Listed Item Selection

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (4 for) · 3 studies (2 design, 1 causal), `q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
ARLIS is the enhanced MAP Growth item-selection algorithm introduced by the Content Proximity Project. It is "a compensatory version of the maximum priority index (Cheng & Chang, 2009) that borrows ideas from reinforcement learning," which may be thought of as reinforcement learning with a greedy policy and frequent deterministic rewards. An item-selection engine acts as the agent choosing items from the pool; a reward is assigned to each content feature, a total reward (a weighted average of functions representing statistical and content requirements) is computed per item, items are listed in descending order of total reward, and the highest-value item is selected, with ties broken randomly as a randomesque exposure control mechanism.

## Design Implications

### Context
#### Requirements
- Requires reward functions for statistical requirements (item information under the Rasch model) and for content features such as item grade and blueprint targets
- Requires the item pool to contain items matching desired content features, since missing features can force off-grade selection
#### Constraints
- The degree of off-grade adaptation depends on the configuration of the item grade reward and on the difference between the group mean and the item pool mean for an instructional area; greater differences produce more frequent off-grade selection

### Target Learners
- K-8 students taking MAP Growth assessments

### Target Learning Objectives
- Accurate measurement of student achievement with content aligned to grade-level standards

### Claims

- [Content Proximity More On Grade Items](../claims/content-proximity-more-on-grade-items.md) [+M]
- [Pilot Blueprint Fulfillment](../claims/pilot-blueprint-fulfillment.md) [+M]
- [The adaptive algorithm's item selection produces a significantly lower SEM than fixed-form tests](../claims/spanish-map-reading-adaptive-lower-sem.md) [+W]
- [The Content Proximity spring 2022 pilot study examined validity, reliability, and test score comparability of MAP Growth assessments using the new item-selection algorithm](../claims/content-proximity-pilot-validity-reliability-comparability.md) [+W]

## Related Theories
- 

## Examples

- [Content Proximity MAP Growth tests](../elements/content-proximity-map-growth-tests.md)

## Key Sources
- J. Patrick Meyer, Ann Hu, Sylvia Li. (2023). Content Proximity Spring 2022 Pilot Study Research Brief. Psychometric Solutions, NWEA. https://www.nwea.org/research/publication/content-proximity-spring-2022-pilot-study-research-report/
