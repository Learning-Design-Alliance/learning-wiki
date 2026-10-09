---
type: element
id: post-stratification-raking-weighting-linking-studies
title: Post-stratification raking weighting procedure for linking study samples
description: "Because the linking study sample is voluntary and may differ from the state population, NWEA applies post-stratification weighting on race, sex, and performance level — variables \"known to be correlated with students'..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: ann-hu-2021
    resource: "https://www.nwea.org/resource/type/linking-studies/"
    title: "Ann Hu, NWEA Psychometric Solutions. (2021). MAP Growth Linking Studies: Intended Uses, Methodology, and Recent Studies. NWEA. https://www.nwea.org/resource/type/linking-studies/"
    author: Ann Hu, NWEA Psychometric Solutions
---

# Post-stratification raking weighting procedure for linking study samples

> **Element** · [All elements](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Because the linking study sample is voluntary and may differ from the state population, NWEA applies post-stratification weighting on race, sex, and performance level — variables "known to be correlated with students' academic achievement." A raking procedure using the survey package in R iteratively matches sample marginal distributions to known population margins, with weights outside 0.3 to 3.0 trimmed, so the weighted sample matches the target population on key demographics and performance characteristics and the derived RIT cuts generalize to the state population.

## Design Implications

### Context
#### Requirements
- State summative reports providing race, sex, and performance level distributions
- The rake function from the survey package in R
#### Constraints
- Weights outside the range of 0.3 to 3.0 are trimmed

### Target Learners
- Students in states with MAP Growth linking studies

### Target Learning Goals
- Generalizable prediction of state summative proficiency

### Affordances
- [Equipercentile Linking Conditional Growth Norms Methodology](../theories/equipercentile-linking-conditional-growth-norms-methodology.md)

## Claims

- [The 2025 MAP Growth norming sample showed no systematic differences from the U.S. public school target population on selected school-level correlates, with no standardized mean difference reaching the 0.2 threshold](../claims/map-growth-2025-norms-sample-representativeness-no-smd-above-02.md) [+W]

## Related Elements

- [MAP Growth linking study report with cut score tables, classification accuracy statistics, and proficiency projections](map-growth-linking-study-report.md)
- [Statistical matching and weighting procedure for the MAP Reading Fluency–Amira linking study](mrf-amira-linking-matching-procedure.md)

## Examples
-

## Key Sources
- Ann Hu, NWEA Psychometric Solutions. (2021). MAP Growth Linking Studies: Intended Uses, Methodology, and Recent Studies. NWEA. https://www.nwea.org/resource/type/linking-studies/
