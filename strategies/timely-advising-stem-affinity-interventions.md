---
type: strategy
id: timely-advising-stem-affinity-interventions
title: Time advising interventions using predicted attrition risk and modeled STEM-affinity transitions
description: The article recommends using attrition prediction and STEM-affinity modeling to time university advising outreach.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: lovenoor-aulck-2017
    resource: "https://doi.org/10.475/123_4"
    title: "Lovenoor Aulck, Rohan Aras, Lysia Li, Coulter L'Heureux, Peter Lu, Jevin D. West. 2017. STEM-ming the Tide: Predicting STEM attrition using student transcript data. In Proceedings of Machine Learning for Education (ml4ed) Workshop at ACM Knowledge Discovery and Data Mining Conference, Halifax, Nova Scotia, Canada, August 2017 (KDD'17). https://doi.org/10.475/123_4"
    author: "Lovenoor Aulck, Rohan Aras, Lysia Li, Coulter L'Heureux, Peter Lu, Jevin D. West"
---

# Time advising interventions using predicted attrition risk and modeled STEM-affinity transitions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (4 for, 3 mixed) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article recommends using attrition prediction and STEM-affinity modeling to time university advising outreach. It argues that "Identifying students who are likely to change their academic interests provides a wealth of opportunity to develop interventions for identifying struggling students and preventing them from dropping out", and that knowing when students may attrite "can be crucial to providing students assistance in a timely manner".

## Design Implications

### Context
#### Requirements
- Routinely collected registrar transcript data plus a model of student STEM affinity or attrition risk to flag students and time outreach.
#### Constraints
- The graphical model is a proof of concept with modest precision (0.670), and the authors state that developing interventions with university administrators remains future work.

### Target Learners
- Undergraduate students at traditional university campuses, particularly those intending STEM majors

### Target Learning Goals
- Preventing dropout from STEM fields
- Providing timely advising assistance to struggling students

### Affordances
- Stem Affinity Hidden Markov Model

## Claims

- [STEM attrition is predictable from first-year registrar transcript data, with four ML models reaching AUROCs between 0.87 and 0.89 and logistic regression performing slightly better](../claims/first-year-transcript-data-predicts-stem-attrition.md) [+M]
- [Performance in math courses supplies five of the ten best single predictors of STEM attrition, including the four most predictive](../claims/math-course-performance-top-single-predictor.md) [+W]
- [High school performance and standardized test scores showed little signal for predicting STEM attrition, in contrast to previous research](../claims/pre-college-measures-weak-signal-stem-attrition.md) [~W]
- [Pre-engineering students tended to shift into economics rather than psychology, unlike most other graduating STEM non-completer groups](../claims/pre-engineering-students-favor-economics-business.md) [~W]
- [About 60% of STEM non-completers graduated with non-STEM degrees, most frequently in psychology, with social-science fields dominating](../claims/psychology-most-frequent-non-stem-degree-stem-ncs.md) [~W]
- [The STEM-affinity graphical model's final-quarter intention classification matches actual STEM graduation with accuracy 0.896, recall 0.999, and precision 0.670](../claims/stem-affinity-model-final-quarter-validation.md) [+W]
- [STEM intention switching concentrates early in students' careers, with the share of STEM-trajectory students sharply dropping during the second year and a switching spike after the fourth quarter](../claims/stem-intention-switching-peaks-second-year.md) [+M]

## Related Strategies

- [Deploy the predictive model as a mid-semester triage tool with capacity-aligned thresholds, recalibration, non-punitive governance, and bias auditing](mid-semester-triage-deployment-strategy.md)

## Examples
-

## Key Sources
- Lovenoor Aulck, Rohan Aras, Lysia Li, Coulter L'Heureux, Peter Lu, Jevin D. West. 2017. STEM-ming the Tide: Predicting STEM attrition using student transcript data. In Proceedings of Machine Learning for Education (ml4ed) Workshop at ACM Knowledge Discovery and Data Mining Conference, Halifax, Nova Scotia, Canada, August 2017 (KDD'17). https://doi.org/10.475/123_4
