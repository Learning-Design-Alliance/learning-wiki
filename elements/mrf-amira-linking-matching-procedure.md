---
type: element
id: mrf-amira-linking-matching-procedure
title: Statistical matching and weighting procedure for the MAP Reading Fluency–Amira linking study
description: The linking study dataset was built by matching MAP Reading Fluency records to Amira records on student attributes (gender, ethnicity, English learner status, special education status, score percentile) and school att...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: nwea-psychometrics-and-analytics-2024
    resource: "https://www.nwea.org/research/publication/predicting-amira-reading-mastery-based-on-nwea-map-reading-fluency-benchmark-assessment-scores/"
    title: "NWEA Psychometrics and Analytics. (2024). Predicting Amira Reading Mastery Based on NWEA MAP Reading Fluency Benchmark Assessment Scores. https://www.nwea.org/research/publication/predicting-amira-reading-mastery-based-on-nwea-map-reading-fluency-benchmark-assessment-scores/"
    author: NWEA Psychometrics and Analytics
---

# Statistical matching and weighting procedure for the MAP Reading Fluency–Amira linking study

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The linking study dataset was built by matching MAP Reading Fluency records to Amira records on student attributes (gender, ethnicity, English learner status, special education status, score percentile) and school attributes using Euclidean distance and the Kuhn-Munkres algorithm, which "minimize the sum of distances between all pairs." Outliers were excluded via squared Mahalanobis distance with a threshold of 13.8, and an iterative raking procedure aligned sample gender and ethnicity margins to the MAP Reading Fluency population. Analyses used the weighted sample.

## Design Implications

### Context
#### Requirements
- Common student identifiers to match records, plus student- and school-level attribute variables for statistical matching.
#### Constraints
- Some MAP Reading Fluency records were dropped because no Amira counterpart was available before exhausting candidates.
- Spring 2023–2024 data were not yet available; spring results were to be appended later.

### Target Learners
- Students in grades 1–5 in U.S. schools (sample drawn from 49 states, 884 districts, and 2,803 schools)

### Target Learning Goals
- Accurate linking of oral reading benchmark scores to reading mastery scores for placement decisions

## Related Elements
- 

## Examples
-

## Key Sources
- NWEA Psychometrics and Analytics. (2024). Predicting Amira Reading Mastery Based on NWEA MAP Reading Fluency Benchmark Assessment Scores. https://www.nwea.org/research/publication/predicting-amira-reading-mastery-based-on-nwea-map-reading-fluency-benchmark-assessment-scores/
