---
type: element
id: propensity-score-ipw-school-tier-design
title: Propensity-score inverse-probability-weighting design with publicly reported school-quality tiers
description: "The study classifies all Chicago high schools into selective, top-tier, mid-tier, and bottom-tier groups using publicly available average ACT scores and 4-year graduation rates, combined \"via principal components anal..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: allensworth-2017
    resource: "https://doi.org/10.3102/0162373716672039"
    title: "Allensworth, E. M., Moore, P. T., Sartain, L., & de la Torre, M. (2017). The Educational Benefits of Attending Higher Performing Schools: Evidence From Chicago High Schools. Educational Evaluation and Policy Analysis. https://doi.org/10.3102/0162373716672039"
    author: "Allensworth, E. M., Moore, P. T., Sartain, L., & de la Torre, M"
---

# Propensity-score inverse-probability-weighting design with publicly reported school-quality tiers

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The study classifies all Chicago high schools into selective, top-tier, mid-tier, and bottom-tier groups using publicly available average ACT scores and 4-year graduation rates, combined "via principal components analysis into terciles" for nonselective schools. It then estimates treatment effects with propensity scores and inverse probability weights, comparing each higher tier against lower-performing tiers with cohort fixed effects and school-cohort clustered standard errors. The design covers all schools in a large district, not only those with lotteries or explicit admission criteria, and includes extensive pretreatment covariates such as middle-grades grades, test scores, attendance, suspensions, survey measures, and neighborhood characteristics.

## Design Implications

### Context
#### Requirements
- Requires publicly available school performance measures (average ACT scores and 4-year graduation rates) from years before students make enrollment decisions
- Requires extensive pretreatment student-level covariates, particularly prior test scores and course grades, to justify the conditional independence assumption
#### Constraints
- The authors state estimates remain subject to bias if covariates correlated with both school quality and outcomes are insufficiently controlled, and that attainment and some nonacademic outcomes without lagged controls are more subject to bias

### Target Learners
- First-time ninth-grade students in a large urban public school district

### Target Learning Goals
- Academic achievement, high school graduation, course taking, college enrollment and persistence, and nonacademic school experiences

## Related Elements
- 

## Examples
-

## Key Sources
- Allensworth, E. M., Moore, P. T., Sartain, L., & de la Torre, M. (2017). The Educational Benefits of Attending Higher Performing Schools: Evidence From Chicago High Schools. Educational Evaluation and Policy Analysis. https://doi.org/10.3102/0162373716672039
