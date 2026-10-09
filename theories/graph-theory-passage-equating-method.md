---
type: theory
title: Graph-theory-based method for selecting reference passages and passage pairs to equate WCPM scores at scale
description: The report introduces a method that models passages as nodes and same-student passage pairs as edges, then uses graph theory to choose a reference passage with the most edges, adequate sample sizes, and medium difficu...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: chen-2020
    resource: "https://www.nwea.org/research/publication/equating-words-correct-per-minute-wcpm-scores-across-passages-of-map-reading-fluency/"
    title: "Chen, J., & Simpson, M. A. (2020). Equating words-correct-per-minute (WCPM) scores across passages of MAP Reading Fluency. Portland, OR: NWEA. https://www.nwea.org/research/publication/equating-words-correct-per-minute-wcpm-scores-across-passages-of-map-reading-fluency/"
    author: "Chen, J., & Simpson, M. A"
---

# Graph-theory-based method for selecting reference passages and passage pairs to equate WCPM scores at scale

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The report introduces a method that models passages as nodes and same-student passage pairs as edges, then uses graph theory to choose a reference passage with the most edges, adequate sample sizes, and medium difficulty, and to define the "shortest path" from each passage to the reference passage so that "the least amount of equating error" is incurred. Cross-term scales are aligned through chain passage pairs administered in earlier terms. Equipercentile equating with loglinear pre-smoothing, using the equate R package, builds the equating relationships.

## Design Implications

### Context
#### Requirements
- A large sample is required: sample sizes of around 1,500 or more students with valid WCPM scores for each passage pair, following Kolen and Brennan (1995)
#### Constraints
- Equating relationships assume the relationship between passages' WCPM scores remains the same across grades
- Conversion tables were capped at 20 SWCPM at the low end and 170 SWCPM at the high end because very low scores are likely unreliable and to prevent over-interpretation

### Target Learners
- Students in Grades K-3

### Target Learning Objectives
- Oral reading fluency measurement and progress monitoring

### Claims

- [Equated Wcpm Higher Cross Passage Correlations](../claims/equated-wcpm-higher-cross-passage-correlations.md) [+M]
- [Equated Wcpm Consistent Progress Monitoring Differences](../claims/equated-wcpm-consistent-progress-monitoring-differences.md) [+M]
- [Equated WCPM scores generally correlate more highly with MAP Growth Reading RIT scores than raw WCPM scores, with one exception](../claims/equated-wcpm-higher-external-validity-correlations.md) [+W]
- [Equated WCPM scores show much less within-student variance than raw WCPM scores, indicating reduced passage-difficulty fluctuations](../claims/equated-wcpm-less-within-student-variance.md) [+W]
- [Equated WCPM scores from non-reference passages show smaller residuals against reference-passage scores than raw scores, with one passage exception](../claims/equated-wcpm-smaller-residuals-one-exception.md) [+W]

## Related Theories
- 

## Examples
-

## Key Sources
- Chen, J., & Simpson, M. A. (2020). Equating words-correct-per-minute (WCPM) scores across passages of MAP Reading Fluency. Portland, OR: NWEA. https://www.nwea.org/research/publication/equating-words-correct-per-minute-wcpm-scores-across-passages-of-map-reading-fluency/
