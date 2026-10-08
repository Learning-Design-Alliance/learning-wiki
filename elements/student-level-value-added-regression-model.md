---
type: element
id: student-level-value-added-regression-model
title: Student-level value-added regression model with teacher dosage variables and student background controls
description: "The analysis uses a student-level regression model in which \"test score at the end of each year (post -test)\" is the outcome and \"test score at the end of the previous year (pre -test)\" is a key control, with teacher..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: steven-glazerman-and-jeffrey-max-2011
    resource: "http://ies.ed.gov/ncee/pubs/20114016/pdf/20114016.pdf"
    title: "Steven Glazerman and Jeffrey Max. (2011). Do Low-Income Students Have Equal Access to the Highest-Performing Teachers? NCEE Technical Appendix. http://ies.ed.gov/ncee/pubs/20114016/pdf/20114016.pdf"
    author: Steven Glazerman and Jeffrey Max
---

# Student-level value-added regression model with teacher dosage variables and student background controls

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 4 studies (4 associational), `q2` · 0 of 4 report an effect size · 5 claims rest on one study

## Description
The analysis uses a student-level regression model in which "test score at the end of each year (post -test)" is the outcome and "test score at the end of the previous year (pre -test)" is a key control, with teacher fixed effects as the object of interest. Teacher dosage variables equal the percentage of the year a student was taught by each teacher. Controls include special education status, FRL eligibility, English language learner status, over-age for grade, race/ethnicity, and a classroom-level control for student turnover. Measurement error in the pretest is addressed with an errors-in-variables two-stage procedure, and robust standard errors pool data across years.

## Design Implications

### Context
#### Requirements
- Student-level pre- and post-test scores in tested grades and subjects
- Test reliability information from the publisher or district for the errors-in-variables correction
#### Constraints
- The two-stage method underestimates the standard errors of the teacher coefficients because it treats the estimated pretest coefficient as its true value, though this is negligible if the coefficient is estimated precisely

### Target Learners
- Students in tested elementary and middle school grades

### Target Learning Goals
- Estimating each teacher's contribution to student achievement growth in ELA and math

## Claims

- [The working paper examines the sensitivity and precision of teacher value-added estimates under specifications differing in student-level, peer-level, and double-lagged achievement controls](../claims/vam-sensitivity-student-peer-controls-examined.md) [+W]
- [Omitting same-subject pre-tests affects value-added estimates more than excluding other student background characteristics](../claims/same-subject-pretest-omission-dominates-background-omission.md) [+W]
- [Teacher value-added estimates are highly correlated across model specifications that differ in student and peer control variables](../claims/vam-estimates-highly-correlated-across-specifications.md) [+W]
- [The paper tests two previously unevaluated VAM model variations: teacher-year level average peer characteristics and demographic variation in the lagged-achievement relationship](../claims/vam-two-novel-model-variations-tested.md) [+W]
- [Value-added teacher rankings are insensitive to correcting measurement error in the pretest, with correlations of 0.91–0.99 for elementary and 0.77–0.98 for middle school teachers](../claims/value-added-rankings-robust-to-eiv-correction.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Steven Glazerman and Jeffrey Max. (2011). Do Low-Income Students Have Equal Access to the Highest-Performing Teachers? NCEE Technical Appendix. http://ies.ed.gov/ncee/pubs/20114016/pdf/20114016.pdf
