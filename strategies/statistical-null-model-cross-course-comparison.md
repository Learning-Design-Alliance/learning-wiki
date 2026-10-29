---
type: strategy
id: statistical-null-model-cross-course-comparison
title: Analyze communication and relational networks statistically against null models rather than comparing raw descriptive SNA metrics across courses
description: This strategy addresses the methodological challenge that descriptive SNA metrics from different courses cannot be compared directly.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
sources:
  - id: poquet-2024
    resource: "https://doi.org/10.1007/s11423-023-10262-9"
    title: "Poquet, O., Trenholm, S., & Santolini, M. (2024). Forum posts, communication patterns, and relational structures: A multi-level view of discussions in online courses. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10262-9"
    author: "Poquet, O., Trenholm, S., & Santolini, M"
---

# Analyze communication and relational networks statistically against null models rather than comparing raw descriptive SNA metrics across courses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
This strategy addresses the methodological challenge that descriptive SNA metrics from different courses cannot be compared directly. The article notes that "current work over-relies on the use of descriptive metrics from SNA used for cross-course comparisons" and states its framework addresses this because both communication metrics and relational structures are analyzed statistically. Analysts simulate null distributions of posting activity, project them to learner-to-learner networks, and compare observed metrics via Z-scores, then fit ERGMs to filtered relational structures.

## Design Implications

### Context
#### Requirements
- Construct post-to-post networks and simulate null distributions keeping per-learner post counts and out-degree constant
#### Constraints
- Statistical analysis of networks may be difficult to integrate into dashboards
- The example null model is limited; temporal aspects and discourse properties need integration

### Target Learners
- learning analysts and researchers studying online courses

### Target Learning Goals
- valid cross-course comparison of learner interaction patterns

## Claims

- [The posting-activity null model reproduces learner degree but is not sufficient to explain clustering in communication networks](../claims/posting-null-model-degree-not-clustering.md) [+W]
- [Only the high-participation high-interactivity course D showed significant reciprocity, cyclical-tie, and Simmelian-tie patterns, indicating group-formation processes](../claims/ergm-relational-structures-course-d.md) [+W]
- [Courses with higher posting participation show more subgroups and more unequal communication than expected by chance, while high-interactivity courses show more equal participation](../claims/participation-unequal-communication-interactivity-equal.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Poquet, O., Trenholm, S., & Santolini, M. (2024). Forum posts, communication patterns, and relational structures: A multi-level view of discussions in online courses. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10262-9
