---
type: element
id: hstatg-administrative-data-eds
title: Early Detection System (EDS) built on standardized HStatG administrative student data
description: "An early detection system that predicts whether a bachelor student will drop out using only the standardized data German universities must collect under §3 HStatG: demographics, previous education, study program, and..."
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

# Early Detection System (EDS) built on standardized HStatG administrative student data

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An early detection system that predicts whether a bachelor student will drop out using only the standardized data German universities must collect under §3 HStatG: demographics, previous education, study program, and end-of-semester performance data. The authors state it "can be introduced and operationally maintained at low cost in German state and private universities as well as in universities of applied sciences," and that it provides "a good starting point for research on student attrition using administrative data." It was developed and tested at a state university with about 23,000 students and a private university of applied sciences with about 6,700 students.

## Design Implications

### Context
#### Requirements
- Only standardized data collected by legal mandate (§3 HStatG) is required, so the administrative data requirement must be met
#### Constraints
- Determinants such as student satisfaction, finances, motivation, integration, and health are not captured by administrative data, so the EDS knowingly uses incomplete data

### Target Learners
- Bachelor students at German universities and universities of applied sciences

### Target Learning Goals
- Early identification of students at risk of dropout to target support and intervention measures

## Claims

- [In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is controlled](../claims/logit-demographic-predictors-weaken-after-performance-controls.md) [+W]
- [Early-stage performance data is particularly important for predicting attrition, while demographic data has limited predictive value once performance data is available](../claims/performance-data-dominates-demographics-in-dropout-prediction.md) [+W]

## Related Elements

- [AdaBoost meta-algorithm combining logit regression, neural networks, and bagged random forests](adaboost-ensemble-of-logit-neural-network-brf.md)
- [Name-based imputation of student immigration background from first and surnames](name-based-immigration-background-imputation.md)

## Examples

- [Three-step attrition-combating process: identify at-risk students with administrative data, connect them to outreach programs, then evaluate the intervention](../strategies/identify-connect-evaluate-attrition-intervention-process.md)

## Key Sources
- Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389
