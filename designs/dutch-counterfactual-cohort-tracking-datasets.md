---
type: design
id: dutch-counterfactual-cohort-tracking-datasets
title: Dutch counterfactual cohort design combining NCO register data, Cito LVS test scores, and the PRIMS survey
description: "The study merges three individual-level datasets: the Netherlands Cohort Study on Education (NCO) register data, the longitudinal standardized student monitoring system (LVS) tests in grades 4-5 from Cito, and the PRI..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
sources:
  - id: van-de-werfhorst-2024
    resource: "https://doi.org/10.1038/s41539-024-00283-1"
    title: "van de Werfhorst, H. G., Zwier, D., Geven, S., Bol, T. & Haelermans, C. (2024). Inequality in pandemic effects on school track placement and the role of social and academic embeddedness. npj Science of Learning 9:71. https://doi.org/10.1038/s41539-024-00283-1"
    author: "van de Werfhorst, H. G., Zwier, D., Geven, S., Bol, T. & Haelermans, C"
---

# Dutch counterfactual cohort design combining NCO register data, Cito LVS test scores, and the PRIMS survey

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 causal), `q3` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The study merges three individual-level datasets: the Netherlands Cohort Study on Education (NCO) register data, the longitudinal standardized student monitoring system (LVS) tests in grades 4-5 from Cito, and the PRIMS survey of 1,232 sixth graders in 66 Dutch schools fielded January/February 2020. The PRIMS data include student survey data and sociometric student and parental contact network measures. A replication package is available at https://osf.io/zf25j/.

## Design Implications

### Context
#### Requirements
- Register and survey data must be linkable at the student level; PRIMS was entropy-balanced to the LVS/NCO register data on prior scores, income, education, gender, and migration status
#### Constraints
- Analyses use non-public microdata from Statistics Netherlands; only statistical code, not data, is published
- Only the Cito student monitoring system was available for research in the register environment

### Target Learners
- Dutch sixth-grade students transitioning to tracked secondary education

### Learning Goals
- Track placement and enrollment outcomes at the primary-to-secondary transition

### Claims

- [The COVID-19 pandemic had small but statistically significant negative average effects on Dutch students' track recommendation (-0.068 levels) and seventh-grade track enrollment (-0.039 levels)](../claims/pandemic-small-negative-effects-track-recommendation-enrollment.md) [+W]
- [The pandemic had a slight positive average effect (+0.011 levels) on ninth-grade track level, unlike the negative effects on earlier outcomes](../claims/pandemic-positive-ninth-grade-track-effect.md) [+W]
- [The COVID-affected cohort caught up to the control cohort in reading fluency one year after the pandemic](../claims/covid-cohort-caught-up-control-cohort-end-grade-four.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- van de Werfhorst, H. G., Zwier, D., Geven, S., Bol, T. & Haelermans, C. (2024). Inequality in pandemic effects on school track placement and the role of social and academic embeddedness. npj Science of Learning 9:71. https://doi.org/10.1038/s41539-024-00283-1
