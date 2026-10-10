---
type: research-method
id: multi-armed-randomized-trial-analysis
title: Multi-armed randomized trial analysis
description: "The report's guidance is that analysts running studies with several intervention arms should not simply reuse two-group methods: estimators \"need to be modified for the multi-armed design,\" hypothesis tests across pairwise contrasts require multiple comparison adjustments, and CACE estimation demand"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
sources:
  - id: peter-z-schochet-2018
    resource: "https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts"
    title: "Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts"
    author: Peter Z. Schochet
---

# Multi-armed randomized trial analysis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (2 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
The report's guidance is that analysts running studies with several intervention arms should not simply reuse two-group methods: estimators "need to be modified for the multi-armed design," hypothesis tests across pairwise contrasts require multiple comparison adjustments, and CACE estimation demands attention to its complex identifying assumptions. The principle directs evaluation design and analysis choices in multi-armed education studies.

## Accounts
<!-- How each source describes or uses the method -->
- **Researchers conducting multi-armed RCTs should adapt estimation, multiplicity testing, and CACE methods from two-group practice**: The report's guidance is that analysts running studies with several intervention arms should not simply reuse two-group methods: estimators "need to be modified for the multi-armed design," hypothesis tests across pairwise contrasts require multiple comparison adjustments, and CACE estimation demands attention to its complex identifying assumptions. The principle directs evaluation design and analysis choices in multi-armed education studies. (Peter Z. Schochet (2017))
- **Design-based estimation framework extended from two-group RCTs to multi-armed RCTs**: The article develops design-based estimators for average treatment effects in randomized controlled trials with multiple research groups, building on an existing framework for single treatment-control designs. As the abstract states, "This article builds on this framework to develop design-based estimators for evaluations with multiple research groups." The framework addresses how two-group estimators must be adjusted when analysis involves pairwise contrasts across research groups. (Peter Z. Schochet (2018))

### Claims
- [Design-based estimators for two-group designs require modification for multi-armed designs when comparing pairs of research groups](../claims/multi-armed-estimators-modify-two-group-estimators.md) [+W]
- [Multiple comparison adjustments are needed when conducting hypothesis tests across pairwise contrasts to identify the most effective interventions](../claims/multi-armed-multiple-comparison-adjustments.md) [+W]
- [Identifying and estimating the CACE parameter in the multi-armed context requires complex assumptions](../claims/multi-armed-cace-complex-assumptions.md) [+W]
- [The developed estimators apply to a wide range of education research designs, including clustered and blocked designs](../claims/design-based-estimators-clustered-blocked-designs.md) [+W]
- [Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision](../claims/variance-adjustment-reduces-precision-multi-armed.md) [+W]
- [In multi-armed trials seeking the most effective treatments, each pairwise contrast sample is representative of the full set of randomized units](../claims/pairwise-contrast-samples-represent-full-randomized-set.md) [+W]
- [Blocks must be weighted to reflect the full randomized sample within the block, or biases result](../claims/block-weighting-full-randomized-sample-avoids-bias.md) [+W]

## Related Research Methods
-

## Key Sources
- Peter Z. Schochet. (2017). Multi-Armed RCTs: A Design-Based Framework. Washington, DC: U.S. Department of Education, Institute of Education Sciences, National Center for Education Evaluation and Regional Assistance. https://ies.ed.gov
- Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts

<!-- merged 2026-10-10 from theories/design-based-estimators-multi-armed-rcts ("Design-based estimation framework extended from two-group RCTs to multi-armed RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Design-based estimation framework extended from two-group RCTs to multi-armed RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article develops design-based estimators for average treatment effects in randomized controlled trials with multiple research groups, building on an existing framework for single treatment-control designs. As the abstract states, "This article builds on this framework to develop design-based estimators for evaluations with multiple research groups." The framework addresses how two-group estimators must be adjusted when analysis involves pairwise contrasts across research groups.

## Design Implications

### Context
#### Requirements
- Evaluations with multiple research groups analyzed via pairwise contrasts across the research groups
#### Constraints
- Builds on design-based methods previously developed for designs with a single treatment and control group

### Target Learners
- education researchers analyzing multi-armed RCT data

### Target Learning Objectives
- accurate estimation of average treatment effects in education evaluations

### Claims

- [Design-based estimators for two-group designs require modification for multi-armed designs when comparing pairs of research groups](../claims/multi-armed-estimators-modify-two-group-estimators.md) [+W]
- [The developed estimators apply to a wide range of education research designs, including clustered and blocked designs](../claims/design-based-estimators-clustered-blocked-designs.md) [+W]
- [Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision](../claims/variance-adjustment-reduces-precision-multi-armed.md) [+W]
- [In multi-armed trials seeking the most effective treatments, each pairwise contrast sample is representative of the full set of randomized units](../claims/pairwise-contrast-samples-represent-full-randomized-set.md) [+W]
- [Blocks must be weighted to reflect the full randomized sample within the block, or biases result](../claims/block-weighting-full-randomized-sample-avoids-bias.md) [+W]

## Related Theories

- [Multi-armed RCT design-based framework for examining multiple interventions in a single study](../theories/multi-armed-rct-design-based-framework.md)
- [Multisite randomized trials as a design for estimating both average effects and cross-site variation](../theories/multisite-rct-design-average-and-variation.md)

## Examples

- [Empirical example using data from a multi-armed education RCT](../elements/empirical-example-multi-armed-education-rct.md)

## Key Sources
- Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts
-->
