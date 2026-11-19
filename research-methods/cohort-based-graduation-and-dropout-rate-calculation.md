---
type: research-method
id: cohort-based-graduation-and-dropout-rate-calculation
moved_from: [element/cohort-tracking-graduation-rate-method]
aliases: [consortium-cohort-dropout-rate-calculation-procedure-for-cps]
title: Cohort-based graduation and dropout rate calculation
description: The report calculates graduation and dropout rates by following student cohorts over multiple years using two cohort types.
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: allensworth-2005
    resource: "https://consortium.uchicago.edu/publications/graduation-and-dropout-trends-chicago-look-cohorts-students-1991-2004"
    title: "Allensworth, E. (2005). Graduation and Dropout Trends in Chicago: A look at cohorts of students from 1991 through 2004, Report Highlights. Consortium on Chicago School Research, University of Chicago. https://consortium.uchicago.edu/publications/graduation-and-dropout-trends-chicago-look-cohorts-students-1991-2004"
    author: Allensworth, E
  - id: elaine-allensworth-and-john-q-easton-2001
    resource: "https://consortium.uchicago.edu/publications/calculating-cohort-dropout-rate-chicago-public-schools"
    title: "Elaine Allensworth and John Q. Easton. (2001). Calculating a Cohort Dropout Rate for the Chicago Public Schools: A Technical Research Report. Consortium on Chicago School Research. https://consortium.uchicago.edu/publications/calculating-cohort-dropout-rate-chicago-public-schools"
    author: Elaine Allensworth and John Q. Easton
---

# Cohort-based graduation and dropout rate calculation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 7 claims (6 for, 1 mixed) · 3 studies (3 associational), `q2` · 0 of 3 report an effect size · 7 claims rest on one study

## Description
The report calculates graduation and dropout rates by following student cohorts over multiple years using two cohort types. Freshman cohorts track first-time ninth graders and permit school comparisons; age-13 cohorts are followed until age 19, a method the report states "is not affected by changes in grade progression, and thus provides a consistent comparison over time." The methods are described as very similar to those recently recommended by the National Center on Education Statistics, with term definitions based on No Child Left Behind Act requirements and CPS characteristics.

## Accounts
<!-- How each source describes or uses the method -->
- **Cohort-based calculation of graduation and dropout rates following age-13 cohorts to age 19 and freshman cohorts four years**: The report calculates graduation and dropout rates by following student cohorts over multiple years using two cohort types. Freshman cohorts track first-time ninth graders and permit school comparisons; age-13 cohorts are followed until age 19, a method the report states "is not affected by changes in grade progression, and thus provides a consistent comparison over time." The methods are described as very similar to those recently recommended by the National Center on Education Statistics, with term definitions based on No Child Left Behind Act requirements and CPS characteristics. (Allensworth (2005))
- **Consortium cohort dropout rate calculation procedure for CPS (age-13 cohorts, six-year follow-up, Master Files)**: A documented statistical procedure for computing comparable cohort dropout rates from administrative records. It defines cohorts as students aged 13 by September 1, follows them six years to age 19, uses student Master Files rather than drop files, updates classifications yearly, and classifies specific leave codes as dropouts. The report states it follows "cohorts for six years, calculating the percentage of students that dropped out at each age from 13 to 19." (Elaine Allensworth et al. (2001))
- **First-order Markov chain model of student academic states for estimating six-year graduation rates**: The article constructs a Markov chain model in which the state space comprises six year-enrolled states plus two absorbing states, Drop-Out and Graduation. As the article defines it, "A (first-order) Markov model is one in which the probability of the system transitioning from one state to another is conditionally independent of all previous states of the system, given the current state." Transition probabilities are estimated from student counts, and the six-year graduation rate estimate is the row-1, column-G entry of the sixth power of the transition matrix. Combining cohorts via pooled transition probabilities lets partially observed cohorts contribute current year-to-year transition information. (Tedeschi MN et al. (2021))

### Claims
- [About 54 percent of Chicago Public Schools students graduated from CPS by age 19 for the 1998 age-13 cohort and by the fourth year for the 1999 freshman cohort](../claims/cps-54-percent-graduated-by-age-19.md) [+W]
- [Over 40 percent of Chicago Public Schools students drop out by age 19, with a slight downward trend across the 1991–1994 cohorts](../claims/cps-cohort-dropout-over-40-percent-slight-decline.md) [+W]
- [The five-year dropout rate for the first cohort fully subject to the CPS promotion policy (1995) continued the slight downward trend, but pre-age-18 patterns do not clearly indicate a change](../claims/promotion-policy-cohort-five-year-rate-continued-trend.md) [+W]
- [Defining dropout cohorts by age 13 rather than by ninth-grade entry avoids composition bias from the CPS promotion policy's grade retentions](../claims/age-based-cohort-definition-avoids-retention-bias.md) [+W]
- [Including unverified transfers as dropouts yields dropout rates about 4 percent higher at age 19 and eliminates the downward trend](../claims/unverified-transfers-raise-rates-remove-trend.md) [~W]
- [A reduced-form Markov model using only full-data cohorts faithfully reproduces traditional six-year graduation rate estimates](../claims/markov-model-reproduces-traditional-sygr.md) [+M]
- [The full-form Markov model yields substantially tighter confidence intervals for six-year graduation rate estimates than the traditional calculation](../claims/markov-tighter-confidence-intervals-sygr.md) [+M]

## Related Research Methods
-

## Key Sources
- Allensworth, E. (2005). Graduation and Dropout Trends in Chicago: A look at cohorts of students from 1991 through 2004, Report Highlights. Consortium on Chicago School Research, University of Chicago. https://consortium.uchicago.edu/publications/graduation-and-dropout-trends-chicago-look-cohorts-students-1991-2004
- Elaine Allensworth and John Q. Easton. (2001). Calculating a Cohort Dropout Rate for the Chicago Public Schools: A Technical Research Report. Consortium on Chicago School Research. https://consortium.uchicago.edu/publications/calculating-cohort-dropout-rate-chicago-public-schools
<!-- merged 2026-10-10 from elements/cohort-tracking-graduation-rate-method ("Cohort-based calculation of graduation and dropout rates following age-13 cohorts to age 19 and freshman cohorts four years"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Tedeschi MN, Hose TM, Mehlman EK, Franklin S, Wong TE. (2021). Improving Models for Student Retention and Graduation using Markov Chains. https://github.com/tonyewong/LA_Markov_analysis

# Cohort-based calculation of graduation and dropout rates following age-13 cohorts to age 19 and freshman cohorts four years

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The report calculates graduation and dropout rates by following student cohorts over multiple years using two cohort types. Freshman cohorts track first-time ninth graders and permit school comparisons; age-13 cohorts are followed until age 19, a method the report states "is not affected by changes in grade progression, and thus provides a consistent comparison over time." The methods are described as very similar to those recently recommended by the National Center on Education Statistics, with term definitions based on No Child Left Behind Act requirements and CPS characteristics.

## Design Implications

### Context
#### Requirements
- Definitions of graduate, transfer, and dropout must be fixed, and the base population of potential graduates specified, since rates vary considerably depending on these choices
#### Constraints
- The freshman-cohort method is difficult to use for trend evaluation in Chicago because the eighth-grade promotion standard shifted students among freshman cohorts

### Target Learners
- Chicago Public Schools high school students

### Target Learning Goals
- Accurate measurement of high school graduation and dropout outcomes for policy and practice

## Claims

- [About 54 percent of Chicago Public Schools students graduated from CPS by age 19 for the 1998 age-13 cohort and by the fourth year for the 1999 freshman cohort](../claims/cps-54-percent-graduated-by-age-19.md) [+W]
- [Over 40 percent of Chicago Public Schools students drop out by age 19, with a slight downward trend across the 1991–1994 cohorts](../claims/cps-cohort-dropout-over-40-percent-slight-decline.md) [+W]
- [The five-year dropout rate for the first cohort fully subject to the CPS promotion policy (1995) continued the slight downward trend, but pre-age-18 patterns do not clearly indicate a change](../claims/promotion-policy-cohort-five-year-rate-continued-trend.md) [+W]
- [Defining dropout cohorts by age 13 rather than by ninth-grade entry avoids composition bias from the CPS promotion policy's grade retentions](../claims/age-based-cohort-definition-avoids-retention-bias.md) [+W]
- [Including unverified transfers as dropouts yields dropout rates about 4 percent higher at age 19 and eliminates the downward trend](../claims/unverified-transfers-raise-rates-remove-trend.md) [~W]

## Related Elements

- [Consortium cohort dropout rate calculation procedure for CPS (age-13 cohorts, six-year follow-up, Master Files)](cohort-based-graduation-and-dropout-rate-calculation.md)

## Examples
-

## Key Sources
- Allensworth, E. (2005). Graduation and Dropout Trends in Chicago: A look at cohorts of students from 1991 through 2004, Report Highlights. Consortium on Chicago School Research, University of Chicago. https://consortium.uchicago.edu/publications/graduation-and-dropout-trends-chicago-look-cohorts-students-1991-2004
-->

<!-- merged 2026-10-17 from research-methods/consortium-cohort-dropout-rate-calculation-procedure-for-cps ("Consortium cohort dropout rate calculation procedure for CPS"), thin research-method page folded into the method it is a variant of (maintainer, 2026-10-17): its body as it stood. Its bullets this page lacked were added above.

# Consortium cohort dropout rate calculation procedure for CPS

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
A documented statistical procedure for computing comparable cohort dropout rates from administrative records. It defines cohorts as students aged 13 by September 1, follows them six years to age 19, uses student Master Files rather than drop files, updates classifications yearly, and classifies specific leave codes as dropouts. The report states it follows "cohorts for six years, calculating the percentage of students that dropped out at each age from 13 to 19."

## Accounts
<!- - How each source describes or uses the method - ->
- **Consortium cohort dropout rate calculation procedure for CPS (age-13 cohorts, six-year follow-up, Master Files)**: A documented statistical procedure for computing comparable cohort dropout rates from administrative records. It defines cohorts as students aged 13 by September 1, follows them six years to age 19, uses student Master Files rather than drop files, updates classifications yearly, and classifies specific leave codes as dropouts. The report states it follows "cohorts for six years, calculating the percentage of students that dropped out at each age from 13 to 19." (Elaine Allensworth et al. (2001))

### Claims

## Related Research Methods
-

## Key Sources
- Elaine Allensworth and John Q. Easton. (2001). Calculating a Cohort Dropout Rate for the Chicago Public Schools: A Technical Research Report. Consortium on Chicago School Research. https://consortium.uchicago.edu/publications/calculating-cohort-dropout-rate-chicago-public-schools

<!- - merged 2026-10-10 from elements/consortium-cps-cohort-dropout-calculation-procedure ("Consortium cohort dropout rate calculation procedure for CPS (age-13 cohorts, six-year follow-up, Master Files)"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Consortium cohort dropout rate calculation procedure for CPS (age-13 cohorts, six-year follow-up, Master Files)

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
A documented statistical procedure for computing comparable cohort dropout rates from administrative records. It defines cohorts as students aged 13 by September 1, follows them six years to age 19, uses student Master Files rather than drop files, updates classifications yearly, and classifies specific leave codes as dropouts. The report states it follows "cohorts for six years, calculating the percentage of students that dropped out at each age from 13 to 19."

## Design Implications

### Context
#### Requirements
- Several years of longitudinal student record data; cohort rates for the most recent cohorts cannot be calculated until those cohorts age through the follow-up window
#### Constraints
- Students dropping out before age 13 (less than 1 percent of each cohort) are not included; rates depend on leave codes entered by school staff with no external validation of CSIS data

### Target Learners
- Chicago Public Schools students aged 13 to 19

### Target Learning Goals
- Accurate, comparable measurement of high school completion and dropout as an indicator of school and district performance

## Related Elements

- [Cohort-based calculation of graduation and dropout rates following age-13 cohorts to age 19 and freshman cohorts four years](../research-methods/cohort-based-graduation-and-dropout-rate-calculation.md)

## Examples
-

## Key Sources
- Elaine Allensworth and John Q. Easton. (2001). Calculating a Cohort Dropout Rate for the Chicago Public Schools: A Technical Research Report. Consortium on Chicago School Research. https://consortium.uchicago.edu/publications/calculating-cohort-dropout-rate-chicago-public-schools
- ->
-->
