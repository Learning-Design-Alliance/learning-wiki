---
type: research-method
id: precision-based-sample-size-planning-for-clustered-education-trials
moved_from: [element/empirical-icc-r2-inputs-education-power-calculations, theory/clustered-rd-power-framework-hlm, theory/power-formulas-mediator-linking-clustered-rcts, theory/unified-power-framework-multi-level-random-assignment]
title: Precision-based sample-size planning for clustered education trials
description: "The article recommends that evaluators discuss \"appropriate precision standards\" and then determine, for each random-assignment design, \"the required number of schools to achieve those standards\" using empirical parameter values."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
sources:
  - id: peter-z-schochet-2008
    resource: "https://www.mathematica.org/publications/journal-article-statistical-power-for-random-assignment-evaluations-of-education-programs"
    title: "Peter Z. Schochet. (2008). Statistical Power for Random Assignment Evaluations of Education Programs. Journal of Educational and Behavioral Statistics, vol. 33, no. 1. https://www.mathematica.org/publications/journal-article-statistical-power-for-random-assignment-evaluations-of-education-programs"
    author: Peter Z. Schochet
  - id: peter-z-schochet-2011
    resource: "https://www.mathematica.org/publications/ja-do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts"
    title: "Peter Z. Schochet. (2011). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? Journal of Educational and Behavioral Statistics, vol. 36, no. 4. https://www.mathematica.org/publications/ja-do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts"
    author: Peter Z. Schochet
  - id: peter-z-schochet-2005
    resource: "https://www.mathematica.org/publications/statistical-power-for-random-assignment-evaluations-of-education-programs"
    title: "Peter Z. Schochet. (2005). Statistical Power for Random Assignment Evaluations of Education Programs. Princeton, NJ: Mathematica Policy Research. https://www.mathematica.org/publications/statistical-power-for-random-assignment-evaluations-of-education-programs"
    author: Peter Z. Schochet
---

# Precision-based sample-size planning for clustered education trials

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 4 studies (4 theoretical), `q2` · 0 of 4 report an effect size · 3 claims rest on one study

## Description
The article recommends that evaluators discuss "appropriate precision standards" and then determine, for each random-assignment design, "the required number of schools to achieve those standards" using empirical parameter values. This makes precision targets, rather than convenience, drive sample planning in education experiments. The principle applies the article's unified framework to practical evaluation design.

## Accounts
<!-- How each source describes or uses the method -->
- **Set precision standards for education trials before determining required school samples**: The article recommends that evaluators discuss "appropriate precision standards" and then determine, for each random-assignment design, "the required number of schools to achieve those standards" using empirical parameter values. This makes precision targets, rather than convenience, drive sample planning in education experiments. The principle applies the article's unified framework to practical evaluation design. (Peter Z. Schochet (2008))
- **Plan evaluation sample sizes around the larger requirements of clustered RD designs before choosing between RD and experimental designs**: Because clustered RD designs typically demand substantially larger samples than clustered experiments for equivalent statistical precision, evaluators should assess power implications before committing to an RD design. The report finds that "three to four times larger samples are typically required under RD than experimental clustered designs to produce impacts with the same level of statistical precision." This principle directs researchers to weigh that power cost against RD's applicability when the assignment point, pretests, and research questions make RD feasible. (Peter Z. Schochet (2008))
- **Size RCT data collection for teacher practice mediators according to the power needed for mediator-achievement analyses**: Because teacher practice mediators are costly to obtain through classroom observations, videotaping, and coded protocols, the report argues power results "may have design implications for the scope of the data collection effort for obtaining costly teacher practice mediators." If power is low, mediator analyses reduce to a heuristic qualitative linking of outcomes. Designers should therefore decide the scope of mediator data collection in light of the school sample needed for precise mediator-achievement estimates. (Schochet (2009))
- **Empirical parameter inputs (intraclass correlations and regression R2 values) for education trial power calculations**: The article assembles empirical values of "intraclass correlations, regression R2 values, and other parameters" as inputs for computing the required number of schools under each random-assignment design. These parameter values, drawn for standardized test scores of elementary school students, ground the article's power calculations in real data rather than assumptions. They are used to derive design-specific school sample requirements. (Peter Z. Schochet (2008))
- **Causal inference and HLM modeling framework for statistical power under clustered regression discontinuity designs**: The report grounds its power analysis in a framework combining causal inference and hierarchical linear modeling (HLM) for clustered RD designs in education research. The theory is "grounded in the causal inference and HLM modeling literature", and the empirical work targets "commonly used designs in education research to test intervention effects on student test scores." Within this framework, clustering and the RD cutoff structure jointly determine the statistical precision of impact estimates, yielding the report's central finding that RD requires larger samples than randomized clustered designs. (Peter Z. Schochet (2008))
- **Statistical power formulas for linking teacher practice mediators to student outcomes in clustered school-based RCTs**: The article develops statistical power formulas for exploratory analyses that estimate associations between student achievement outcomes and mediating teacher practice outcomes in randomized controlled trials of education interventions. The formulas are derived "under clustered school-based RCTs using ordinary least squares and instrumental variable estimators" and are then applied in a simulated power analysis. The framework serves researchers designing RCTs who want to test whether data support a study's conceptual model. (Peter Z. Schochet (2011))
- **Unified analytic framework for statistical power across school, classroom, and student random assignment designs**: The article organizes power analysis for education experiments through a unified analytic framework that applies statistical methods from the literature across designs where "random assignment is conducted at the school, classroom, or student level". The framework lets the author compute required school samples for each design using "empirical values of intraclass correlations, regression R2 values, and other parameters". It serves as the organizing structure for the article's precision standards and design comparisons. (Peter Z. Schochet (2008))

### Claims
- [Clustering effects in education random-assignment trials vary by design but are typically large, requiring large school samples](../claims/clustering-effects-large-school-samples-education-trials.md) [+M]
- [Mediator-outcome association analyses can identify teacher practice mediators most associated with student learning](../claims/mediator-analyses-identify-key-teacher-practices.md) [+W]
- [Measurement error in the mediator reduces statistical power for mediator-achievement association estimates](../claims/mediator-measurement-error-reduces-power.md) [+W]
- [Classroom-level ICCs for elementary test score gains range from 0.02 to 0.15 and school-level ICCs from 0.05 to 0.20, so classroom effects explain about 15 percent of gain-score variance](../claims/icc-classroom-effects-gain-scores-15-percent.md) [+W]

## Related Research Methods

- [Power planning for mediator–outcome linkage analyses in clustered education RCTs](power-planning-for-mediatoroutcome-linkage-analyses-in-clustered-education-rcts.md)

## Key Sources
- Peter Z. Schochet. (2008). Statistical Power for Random Assignment Evaluations of Education Programs. Journal of Educational and Behavioral Statistics, vol. 33, no. 1. https://www.mathematica.org
- Peter Z. Schochet. (2008). Technical Methods Report: Statistical Power for Regression Discontinuity Designs in Education Evaluations. Washington, DC: U.S. Department of Education, Institute of Education Sciences. https://ies.ed.gov
- Schochet, Peter Z. (2009). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? (NCEE 2009-4065). Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. http://ncee.ed.gov
- Peter Z. Schochet. (2008). Statistical Power for Random Assignment Evaluations of Education Programs. Journal of Educational and Behavioral Statistics, vol. 33, no. 1. https://www.mathematica.org/publications/journal-article-statistical-power-for-random-assignment-evaluations-of-education-programs
- Peter Z. Schochet. (2008). Technical Methods Report: Statistical Power for Regression Discontinuity Designs in Education Evaluations. Washington, DC: U.S. Department of Education, Institute of Education Sciences. https://www.mathematica.org/publications/technical-methods-report-statistical-power-for-regression-discontinuity-designs-in-education-evaluations
- Peter Z. Schochet. (2011). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? Journal of Educational and Behavioral Statistics, vol. 36, no. 4. https://www.mathematica.org/publications/ja-do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts
- Peter Z. Schochet. (2005). Statistical Power for Random Assignment Evaluations of Education Programs. Princeton, NJ: Mathematica Policy Research. https://www.mathematica.org/publications/statistical-power-for-random-assignment-evaluations-of-education-programs

<!-- merged 2026-10-10 from elements/empirical-icc-r2-inputs-education-power-calculations ("Empirical parameter inputs (intraclass correlations and regression R2 values) for education trial power calculations"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Peter Z. Schochet. (2008). Technical Methods Report: Statistical Power for Regression Discontinuity Designs in Education Evaluations. Washington, DC: U.S. Department of Education, Institute of Education Sciences. https://www.mathematica.org/publications/technical-methods-report-statistical-power-for-regression-discontinuity-designs-in-education-evaluations
- Peter Z. Schochet. (2011). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? Journal of Educational and Behavioral Statistics, vol. 36, no. 4. https://www.mathematica.org/publications/ja-do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts

# Empirical parameter inputs (intraclass correlations and regression R2 values) for education trial power calculations

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article assembles empirical values of "intraclass correlations, regression R2 values, and other parameters" as inputs for computing the required number of schools under each random-assignment design. These parameter values, drawn for standardized test scores of elementary school students, ground the article's power calculations in real data rather than assumptions. They are used to derive design-specific school sample requirements.

## Design Implications

### Context
#### Requirements
- Applies to standardized test score outcomes for elementary school students
#### Constraints
- Parameter values are empirical estimates and their applicability is bounded by the populations from which they were estimated

### Target Learners
- elementary school students

### Target Learning Goals
- planning statistically powered experimental evaluations of education programs

### Affordances
- [Unified Power Framework Multi Level Random Assignment](precision-based-sample-size-planning-for-clustered-education-trials.md)

## Claims

- [Clustering effects in education random-assignment trials vary by design but are typically large, requiring large school samples](../claims/clustering-effects-large-school-samples-education-trials.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Peter Z. Schochet. (2008). Statistical Power for Random Assignment Evaluations of Education Programs. Journal of Educational and Behavioral Statistics, vol. 33, no. 1. https://www.mathematica.org/publications/journal-article-statistical-power-for-random-assignment-evaluations-of-education-programs
-->

<!-- merged 2026-10-10 from theories/clustered-rd-power-framework-hlm ("Causal inference and HLM modeling framework for statistical power under clustered regression discontinuity designs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Causal inference and HLM modeling framework for statistical power under clustered regression discontinuity designs

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The report grounds its power analysis in a framework combining causal inference and hierarchical linear modeling (HLM) for clustered RD designs in education research. The theory is "grounded in the causal inference and HLM modeling literature", and the empirical work targets "commonly used designs in education research to test intervention effects on student test scores." Within this framework, clustering and the RD cutoff structure jointly determine the statistical precision of impact estimates, yielding the report's central finding that RD requires larger samples than randomized clustered designs.

## Design Implications

### Context
#### Requirements
- Application to clustered designs where treatment assignment follows a cutoff rule and outcomes are measured on students nested within clusters
#### Constraints
- The framework's empirical focus is on student test score outcomes in education research settings

### Target Learners
- Students in education evaluations analyzed under clustered RD designs

### Target Learning Objectives
- Estimating intervention effects on student test scores with adequate statistical precision

### Claims

## Related Theories

- [Unified analytic framework for statistical power across school, classroom, and student random assignment designs](precision-based-sample-size-planning-for-clustered-education-trials.md)

## Examples
-

## Key Sources
- Peter Z. Schochet. (2008). Technical Methods Report: Statistical Power for Regression Discontinuity Designs in Education Evaluations. Washington, DC: U.S. Department of Education, Institute of Education Sciences. https://www.mathematica.org/publications/technical-methods-report-statistical-power-for-regression-discontinuity-designs-in-education-evaluations
-->

<!-- merged 2026-10-10 from theories/power-formulas-mediator-linking-clustered-rcts ("Statistical power formulas for linking teacher practice mediators to student outcomes in clustered school-based RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Statistical power formulas for linking teacher practice mediators to student outcomes in clustered school-based RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 8 claims (8 for) · 3 studies (3 theoretical), `q2` · 0 of 3 report an effect size · 8 claims rest on one study

## Description
The article develops statistical power formulas for exploratory analyses that estimate associations between student achievement outcomes and mediating teacher practice outcomes in randomized controlled trials of education interventions. The formulas are derived "under clustered school-based RCTs using ordinary least squares and instrumental variable estimators" and are then applied in a simulated power analysis. The framework serves researchers designing RCTs who want to test whether data support a study's conceptual model.

## Design Implications

### Context
#### Requirements
- Clustered school-based RCT design with measured teacher practice mediators and student achievement outcomes
#### Constraints
- Formulas are for exploratory analyses of mediator-outcome associations, not confirmatory causal mediation claims

### Target Learners
- Education researchers and evaluators designing school-based RCTs

### Target Learning Objectives
- Assessing whether RCT data support a study's conceptual model linking teacher practice to student learning

### Claims

- [Mediator-outcome association analyses can identify teacher practice mediators most associated with student learning](../claims/mediator-analyses-identify-key-teacher-practices.md) [+W]
- [Measurement error in the mediator reduces statistical power for mediator-achievement association estimates](../claims/mediator-measurement-error-reduces-power.md) [+W]
- [Classroom-level ICCs for elementary test score gains range from 0.02 to 0.15 and school-level ICCs from 0.05 to 0.20, so classroom effects explain about 15 percent of gain-score variance](../claims/icc-classroom-effects-gain-scores-15-percent.md) [+W]

## Related Theories

- [Conceptual model of teacher practice mediation in education RCTs](causal-mediation-analysis-of-teacher-practice-in-education-randomized-trials.md)
- [Design-based estimators framework for analyzing grouped administrative data in RCTs](../research-methods/design-based-rct-analysis-with-grouped-administrative-data.md)
- [Unified analytic framework for statistical power across school, classroom, and student random assignment designs](precision-based-sample-size-planning-for-clustered-education-trials.md)

## Examples


## Key Sources
- Peter Z. Schochet. (2011). Do Typical RCTs of Education Interventions Have Sufficient Statistical Power for Linking Impacts on Teacher Practice and Student Achievement Outcomes? Journal of Educational and Behavioral Statistics, vol. 36, no. 4. https://www.mathematica.org/publications/ja-do-typical-rcts-of-education-interventions-have-sufficient-statistical-power-for-linking-impacts
-->

<!-- merged 2026-10-10 from theories/unified-power-framework-multi-level-random-assignment ("Unified analytic framework for statistical power across school, classroom, and student random assignment designs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Unified analytic framework for statistical power across school, classroom, and student random assignment designs

> **Theory** · [All theories](index.md)
> **Evidence** · 7 claims (7 for) · 3 studies (3 theoretical), `q2` · 0 of 3 report an effect size · 7 claims rest on one study

## Description
The article organizes power analysis for education experiments through a unified analytic framework that applies statistical methods from the literature across designs where "random assignment is conducted at the school, classroom, or student level". The framework lets the author compute required school samples for each design using "empirical values of intraclass correlations, regression R2 values, and other parameters". It serves as the organizing structure for the article's precision standards and design comparisons.

## Design Implications

### Context
#### Requirements
- Empirical parameter values such as intraclass correlations and regression R2 values are needed to compute required school samples
- Designs must use random assignment at the school, classroom, or student level
#### Constraints
- The framework is applied to standardized test scores of elementary school students

### Target Learners
- elementary school students

### Target Learning Objectives
- accurate estimation of program impacts on standardized test scores in experimental evaluations
- estimating program impacts on standardized test scores

### Claims

- [Clustering Effects Large School Samples Education Trials](../claims/clustering-effects-large-school-samples-education-trials.md) [+M]
- [Clustering effects vary by design but are typically large in education random-assignment evaluations](../claims/clustering-effects-large-school-samples-education-trials.md) [+W]

## Related Theories

- [Causal inference and HLM modeling framework for statistical power under clustered regression discontinuity designs](../research-methods/precision-based-sample-size-planning-for-clustered-education-trials.md)

## Examples
-

## Key Sources
- Peter Z. Schochet. (2008). Statistical Power for Random Assignment Evaluations of Education Programs. Journal of Educational and Behavioral Statistics, vol. 33, no. 1. https://www.mathematica.org/publications/journal-article-statistical-power-for-random-assignment-evaluations-of-education-programs
- Peter Z. Schochet. (2005). Statistical Power for Random Assignment Evaluations of Education Programs. Princeton, NJ: Mathematica Policy Research. https://www.mathematica.org/publications/statistical-power-for-random-assignment-evaluations-of-education-programs

<!- - merged 2026-10-09 from theories/unified-power-framework-multi-level-ra-designs ("Unified analytic framework for statistical power across school, classroom, and student random-assignment designs"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Unified analytic framework for statistical power across school, classroom, and student random-assignment designs

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 theoretical), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The paper presents "a unified analytic framework based on statistical methods from the literature" for computing statistical power in education experiments. It applies this framework across designs in which "random assignment is conducted at the school, classroom, or student level," allowing power requirements to be compared across assignment levels within one set of methods.

## Design Implications

### Context
#### Requirements
- Designs must use random assignment at the school, classroom, or student level
#### Constraints
- The framework is applied to standardized test scores of elementary school students

### Target Learners
- elementary school students

### Target Learning Objectives
- estimating program impacts on standardized test scores

### Claims

- [Clustering effects vary by design but are typically large in education random-assignment evaluations](../claims/clustering-effects-large-school-samples-education-trials.md) [+W]
- [Clustering effects in education random-assignment trials vary by design but are typically large, requiring large school samples](../claims/clustering-effects-large-school-samples-education-trials.md) [+W]

## Related Theories

- [Unified analytic framework for statistical power across school, classroom, and student random assignment designs](precision-based-sample-size-planning-for-clustered-education-trials.md)

## Examples
-

## Key Sources
- Peter Z. Schochet. (2005). Statistical Power for Random Assignment Evaluations of Education Programs. Princeton, NJ: Mathematica Policy Research. https://www.mathematica.org/publications/statistical-power-for-random-assignment-evaluations-of-education-programs
- ->
-->
