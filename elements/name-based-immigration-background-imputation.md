---
type: element
id: name-based-immigration-background-imputation
title: Name-based imputation of student immigration background from first and surnames
description: Because second-generation immigrants with German citizenship cannot be identified from administrative records, the authors impute immigration background and region of origin from first and family names using the Humpe...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: johannes-berens-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389"
    title: "Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389"
    author: Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff
---

# Name-based imputation of student immigration background from first and surnames

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
Because second-generation immigrants with German citizenship cannot be identified from administrative records, the authors impute immigration background and region of origin from first and family names using the Humpert and Schneiderheinze method, drawing on name databases of around 200,000 first names and 600,000 surnames across 145 countries aggregated into 11 regions. Validation showed "more than 94% of the first and surname combinations were correctly assigned" for known foreign citizens, and 82% correct labeling against GSOEP data using first names only. At both universities, 29% of students were identified as first or second-generation immigrants.

## Design Implications

### Context
#### Requirements
- Access to students' first and last names, and name databases mapping name-country combinations to origin probabilities
#### Constraints
- Using only the first name lowers imputation accuracy (94% to 88% in the citizenship test; 82% against GSOEP); some names are not in the databases (234 SU and 147 PUAS students non-identified)

### Target Learners
- University students in Germany with and without immigration background

### Target Learning Goals
- Identifying immigrant-background students at risk of dropout for targeted support

## Related Elements

- [Early Detection System (EDS) built on standardized HStatG administrative student data](hstatg-administrative-data-eds.md)

## Examples
-

## Key Sources
- Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389
