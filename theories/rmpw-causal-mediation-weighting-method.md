---
type: theory
title: Ratio-of-mediator-probability weighting (RMPW) for causal mediation analysis under treatment-by-mediator interaction
description: RMPW is a weighting-based approach to causal mediation analysis that decomposes a total effect into natural direct and indirect effects even when the mediator–outcome relationship depends on the treatment condition.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: guanglei-hong-2015
    resource: "https://www.mathematica.org/publications/ratioofmediatorprobability-weighting-for-causal-mediation-analysis-in-the-presence"
    title: "Guanglei Hong, Jonah Deutsch, Heather D. Hill. (2015). Ratio-of-Mediator-Probability Weighting for Causal Mediation Analysis in the Presence of Treatment-by-Mediator Interaction. Journal of Educational and Behavioral Statistics, vol. 40, no. 3. https://www.mathematica.org/publications/ratioofmediatorprobability-weighting-for-causal-mediation-analysis-in-the-presence"
    author: Guanglei Hong, Jonah Deutsch, Heather D. Hill
---

# Ratio-of-mediator-probability weighting (RMPW) for causal mediation analysis under treatment-by-mediator interaction

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
RMPW is a weighting-based approach to causal mediation analysis that decomposes a total effect into natural direct and indirect effects even when the mediator–outcome relationship depends on the treatment condition. The article gives "an intuitive explanation of the RMPW rationale, a mathematical proof, and simulation results for the parametric and nonparametric RMPW procedures." Unlike model-based alternatives, it relies on propensity score models for the mediator rather than a fully specified outcome model.

## Design Implications

### Context
#### Requirements
- Correct specification of the propensity score models for the mediator when parametric RMPW is applied
#### Constraints
- Causally valid results require that the sequential ignorability assumptions hold

### Target Learners
- education and behavioral science researchers conducting mediation analysis

### Target Learning Objectives
- decomposing total treatment effects into direct and indirect components in the presence of treatment-by-mediator interaction

### Claims

- [Conventional mediation methods generate biased results when the mediator–outcome relationship depends on treatment condition](../claims/conventional-mediation-biased-under-treatment-mediator-interaction.md) [+W]
- [Correct specification of the mediator propensity score models is crucial when parametric RMPW is applied](../claims/parametric-rmpw-depends-on-propensity-score-specification.md) [+W]
- [RMPW was applied to test whether employment mediated the effect of an experimental welfare-to-work program on maternal depression](../claims/rmpw-application-welfare-to-work-maternal-depression.md) [+W]
- [RMPW decomposes total effects into natural direct and indirect effects, with the indirect effect further split into a pure indirect effect and a natural treatment-by-mediator interaction effect](../claims/rmpw-decomposes-total-indirect-interaction-effects.md) [+W]
- [RMPW requires relatively few assumptions about outcome and mediator distributions and outcome-model functional form compared with model-based alternatives](../claims/rmpw-fewer-distributional-assumptions-than-sem-path-analysis.md) [+W]

## Related Theories
- 

## Examples

- [RMPW software program and online Stata code](../products/rmpw.md)

## Key Sources
- Guanglei Hong, Jonah Deutsch, Heather D. Hill. (2015). Ratio-of-Mediator-Probability Weighting for Causal Mediation Analysis in the Presence of Treatment-by-Mediator Interaction. Journal of Educational and Behavioral Statistics, vol. 40, no. 3. https://www.mathematica.org/publications/ratioofmediatorprobability-weighting-for-causal-mediation-analysis-in-the-presence
