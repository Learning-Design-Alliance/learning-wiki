---
type: research-method
id: correct-variance-estimation-for-cace-in-clustered-education-rcts
title: Correct variance estimation for CACE in clustered education RCTs
description: "The report's methodological contribution is to work out the correct variance formulas for the CACE estimator under clustered designs and to compare them with \"those that are typically used in practice\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
sources:
  - id: peter-z-schochet-2009
    resource: "https://www.mathematica.org/publications/technical-methods-report-estimation-and-identification-of-the-complier-average-causal-effect-parameter-in-education-rcts"
    title: "Peter Z. Schochet, Hanley Chiang. (2009). Technical Methods Report: Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org/publications/technical-methods-report-estimation-and-identification-of-the-complier-average-causal-effect-parameter-in-education-rcts"
    author: Peter Z. Schochet, Hanley Chiang
  - id: peter-z-schochet-2011
    resource: "https://eric.ed.gov/?q=Estimation"
    title: "Peter Z. Schochet, Hanley S. Chiang. (2011). Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Journal of Educational and Behavioral Statistics, vol. 36, no. 3. https://eric.ed.gov/?q=Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs"
    author: Peter Z. Schochet, Hanley S. Chiang
---

# Correct variance estimation for CACE in clustered education RCTs

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 5 studies (3 causal, 2 theoretical), `q1`–`q2` · 0 of 5 report an effect size · 5 claims rest on one study

## Description
The report's methodological contribution is to work out the correct variance formulas for the CACE estimator under clustered designs and to compare them with "those that are typically used in practice". Analysts estimating CACE in education RCTs should apply the correct variance formulas when assessing significance of the estimator, measured in nominal and standard deviation units.

## Accounts
<!-- How each source describes or uses the method -->
- **Use correct variance formulas when estimating the CACE parameter in education RCTs**: The report's methodological contribution is to work out the correct variance formulas for the CACE estimator under clustered designs and to compare them with "those that are typically used in practice". Analysts estimating CACE in education RCTs should apply the correct variance formulas when assessing significance of the estimator, measured in nominal and standard deviation units. (Peter Z. Schochet (2009))
- **Report CACE significance findings using correct variance formulas, but simplified formulas may suffice for similar conclusions**: The article's comparison implies that analysts estimating CACE in clustered education RCTs should base significance findings on correct variance formulas that account for the relevant sources of error. Because the commonly used simplified formulas "lead to very similar significance findings" across the 10 RCTs examined, the practical stakes of formula choice may be limited, though correct formulas remain the benchmark. (Peter Z. Schochet (2011))
- **CACE parameter framework for clustered education RCTs**: The report presents the complier average causal effect (CACE) parameter as an estimand for education RCTs: it is "the average impact of intervention services on those who comply with their treatment assignments". The framework addresses identification and estimation of this parameter specifically "under clustered RCT designs that are typically used in the education field", extending causal estimation methods beyond the default intention-to-treat analysis to clustered designs. (Peter Z. Schochet (2009))
- **Causal inference and instrumental variables framework for identifying and estimating CACE in two-level clustered RCTs**: The article uses "a causal inference and instrumental variables framework to examine the identification and estimation of the CACE parameter for two-level clustered RCTs." This framework treats random assignment as an instrument for treatment receipt, addressing identification of the complier average causal effect in clustered education designs where students are nested within schools or similar units. (Peter Z. Schochet (2011))

### Claims
- [Variance correction terms matter little for CACE significance findings in education RCTs](../claims/cace-variance-correction-terms-matter-little.md) [+M]
- [CACE estimators based on correct variance formulas and commonly used simplified formulas yield very similar significance findings across 10 education RCTs](../claims/cace-variance-formulas-similar-significance-findings.md) [+M]
- [Control-group noncompliance makes experimental and nonexperimental estimands diverge (CACE vs. all treated subjects)](../claims/noncompliance-estimand-divergence-cace-itt.md) [+W]
- [Identifying and estimating the CACE parameter in the multi-armed context requires complex assumptions](../claims/multi-armed-cace-complex-assumptions.md) [+W]
- [CACE estimators based on correct variance formulas and commonly used simplified formulas yield very similar significance findings across 10 education RCTs](../claims/cace-variance-formulas-similar-significance-findings.md) [+W]
- [Standard errors sometimes differ across estimators, so policy conclusions from clustered education RCTs could be sensitive to the choice of estimator](../claims/rct-policy-conclusions-sensitive-to-estimator-choice.md) [~W]

## Related Research Methods
-

## Key Sources
- Peter Z. Schochet, Hanley Chiang. (2009). Technical Methods Report: Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org
- Peter Z. Schochet, Hanley S. Chiang. (2011). Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Journal of Educational and Behavioral Statistics, vol. 36, no. 3. https://eric.ed.gov/?q=Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs
- Peter Z. Schochet, Hanley Chiang. (2009). Technical Methods Report: Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org/publications/technical-methods-report-estimation-and-identification-of-the-complier-average-causal-effect-parameter-in-education-rcts

<!-- merged 2026-10-10 from theories/cace-parameter-clustered-education-rcts ("CACE parameter framework for clustered education RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# CACE parameter framework for clustered education RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 theoretical), `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The report presents the complier average causal effect (CACE) parameter as an estimand for education RCTs: it is "the average impact of intervention services on those who comply with their treatment assignments". The framework addresses identification and estimation of this parameter specifically "under clustered RCT designs that are typically used in the education field", extending causal estimation methods beyond the default intention-to-treat analysis to clustered designs.

## Design Implications

### Context
#### Requirements
- Estimating CACE requires information on treatment compliance among assigned participants in a clustered RCT design
#### Constraints
- The framework is developed for clustered RCT designs as typically used in the education field

### Target Learners
- students in education RCT studies

### Target Learning Objectives
- estimating intervention effects on compliers in education randomized trials

### Claims

- [Control-group noncompliance makes experimental and nonexperimental estimands diverge (CACE vs. all treated subjects)](../claims/noncompliance-estimand-divergence-cace-itt.md) [+W]
- [Identifying and estimating the CACE parameter in the multi-armed context requires complex assumptions](../claims/multi-armed-cace-complex-assumptions.md) [+W]

## Related Theories

- [CACE as a policy-relevant parameter for intervention effects on students receiving a meaningful dose of treatment](../theories/cace-policy-relevant-parameter-education-rcts.md)
- [Causal inference and instrumental variables framework for identifying and estimating CACE in two-level clustered RCTs](correct-variance-estimation-for-cace-in-clustered-education-rcts.md)

## Examples
-

## Key Sources
- Peter Z. Schochet, Hanley Chiang. (2009). Technical Methods Report: Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Washington, DC: National Center for Education Evaluation and Regional Assistance, Institute of Education Sciences, U.S. Department of Education. https://www.mathematica.org/publications/technical-methods-report-estimation-and-identification-of-the-complier-average-causal-effect-parameter-in-education-rcts
-->

<!-- merged 2026-10-10 from theories/iv-framework-cace-two-level-clustered-rcts ("Causal inference and instrumental variables framework for identifying and estimating CACE in two-level clustered RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Causal inference and instrumental variables framework for identifying and estimating CACE in two-level clustered RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 2 studies (1 causal, 1 theoretical), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article uses "a causal inference and instrumental variables framework to examine the identification and estimation of the CACE parameter for two-level clustered RCTs." This framework treats random assignment as an instrument for treatment receipt, addressing identification of the complier average causal effect in clustered education designs where students are nested within schools or similar units.

## Design Implications

### Context
#### Requirements
- A two-level clustered RCT design with random assignment serving as an instrument for treatment receipt
#### Constraints
- Developed specifically for two-level clustered RCTs in education

### Target Learners
- Students in clustered education RCTs

### Target Learning Objectives
- Identification and estimation of intervention effects for compliers

### Claims

- [CACE estimators based on correct variance formulas and commonly used simplified formulas yield very similar significance findings across 10 education RCTs](../claims/cace-variance-formulas-similar-significance-findings.md) [+W]
- [Standard errors sometimes differ across estimators, so policy conclusions from clustered education RCTs could be sensitive to the choice of estimator](../claims/rct-policy-conclusions-sensitive-to-estimator-choice.md) [~W]

## Related Theories

- [CACE as a policy-relevant parameter for intervention effects on students receiving a meaningful dose of treatment](../theories/cace-policy-relevant-parameter-education-rcts.md)
- [Neyman causal inference framework distinguishing finite-population and super-population models for clustered education RCTs](../theories/neyman-framework-clustered-rct-causal-models.md)
- [CACE parameter framework for clustered education RCTs](../research-methods/correct-variance-estimation-for-cace-in-clustered-education-rcts.md)

## Examples
-

## Key Sources
- Peter Z. Schochet, Hanley S. Chiang. (2011). Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs. Journal of Educational and Behavioral Statistics, vol. 36, no. 3. https://eric.ed.gov/?q=Estimation and Identification of the Complier Average Causal Effect Parameter in Education RCTs
-->
