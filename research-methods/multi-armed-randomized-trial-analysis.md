---
type: research-method
id: multi-armed-randomized-trial-analysis
moved_from: [theory/design-based-estimators-multi-armed-rcts]
title: Multi-armed randomized trial analysis
description: "The report's guidance is that analysts running studies with several intervention arms should not simply reuse two-group methods: estimators \"need to be modified for the multi-armed design,\" hypothesis tests across pairwise contrasts require multiple comparison adjustments, and CACE estimation demand"
status: review
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
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The report's guidance is that analysts running studies with several intervention arms should not simply reuse two-group methods: estimators "need to be modified for the multi-armed design," hypothesis tests across pairwise contrasts require multiple comparison adjustments, and CACE estimation demands attention to its complex identifying assumptions. The principle directs evaluation design and analysis choices in multi-armed education studies.

## Accounts
<!-- How each source describes or uses the method -->
- **Researchers conducting multi-armed RCTs should adapt estimation, multiplicity testing, and CACE methods from two-group practice**: The report's guidance is that analysts running studies with several intervention arms should not simply reuse two-group methods: estimators "need to be modified for the multi-armed design," hypothesis tests across pairwise contrasts require multiple comparison adjustments, and CACE estimation demands attention to its complex identifying assumptions. The principle directs evaluation design and analysis choices in multi-armed education studies. (Peter Z. Schochet (2017))
- **Design-based estimation framework extended from two-group RCTs to multi-armed RCTs**: The article develops design-based estimators for average treatment effects in randomized controlled trials with multiple research groups, building on an existing framework for single treatment-control designs. As the abstract states, "This article builds on this framework to develop design-based estimators for evaluations with multiple research groups." The framework addresses how two-group estimators must be adjusted when analysis involves pairwise contrasts across research groups. (Peter Z. Schochet (2018))
- **Recurrent Individual Treatment Assignment (RITA) algorithm: sequential RCTs with rank-based probability updating that avoids explicit ITE estimation**: RITA is a longitudinal individual assignment algorithm based on sequential RCTs or A/B-tests. Rather than estimating ITEs, it ranks each individual's observed treatment response each period, updates individual mean ranks per intervention, and adjusts assignment probabilities using an exponential learning parameter. The article states RITA 'refrains from attempting to estimate ITE and focuses on individual treatment response and assignment instead.' It maintains a minimum exploration level to allow for dynamic treatment effects. (Ilja Cornelisz et al. (2022))
- **AI-controlled experimental sampling: multi-armed bandit and adaptive design optimization methods for running education experiments at scale**: The article frames the experimental process itself as an efficient search problem that AI can play a major role in. It notes that educational data mining research "has already started looking at dynamically assigning subjects to different learning conditions based on multi-armed bandit models," that cognitive model-comparison experiments have used adaptive design optimization, and that adaptive sampling is common in medical research. In the long term, automated experimentation may compare the effectiveness of different services or content modules by randomly selecting them from open repositories, allowing direct comparison of theories and exploration of interactions between theoretically-grounded constructs. (Nye (2016))

### Claims
- [Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision](../claims/variance-adjustment-reduces-precision-multi-armed.md) [+W]

## Related Research Methods

- [TAME (detecting treatment effects by training a model across multiple experiments and testing residuals)](tame-detecting-treatment-effects-by-training-a-model-across-multiple-experiments-and-testi.md)

## Key Sources
- Peter Z. Schochet. (2017). Multi-Armed RCTs: A Design-Based Framework. Washington, DC: U.S. Department of Education, Institute of Education Sciences, National Center for Education Evaluation and Regional Assistance. https://ies.ed.gov
- Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts
<!-- merged 2026-10-10 from theories/design-based-estimators-multi-armed-rcts ("Design-based estimation framework extended from two-group RCTs to multi-armed RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Ilja Cornelisz and Chris van Klaveren. (2022). Recurrent individual treatment assignment: a treatment policy approach to account for heterogeneous treatment effects. npj Science of Learning 7:3. https://doi.org/10.1038/s41539-021-00117-4
- Nye, B. D. (2016). ITS, The End of the World as We Know It: Transitioning AIED into a Service-Oriented Ecosystem. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0098-8

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

- [Variance terms in multi-armed RCT estimators need slight adjustment under the finite-population framework, which can reduce precision](../claims/variance-adjustment-reduces-precision-multi-armed.md) [+W]

## Related Theories

- [Multi-armed RCT design-based framework for examining multiple interventions in a single study](../theories/multi-armed-rct-design-based-framework.md)
- [Multisite randomized trials as a design for estimating both average effects and cross-site variation](../theories/multisite-rct-design-average-and-variation.md)

## Examples

- [Empirical example using data from a multi-armed education RCT](../elements/empirical-example-multi-armed-education-rct.md)

## Key Sources
- Peter Z. Schochet. (2018). Design-Based Estimators for Average Treatment Effects for Multi-Armed RCTs. Journal of Educational and Behavioral Statistics, vol. 43, issue 5. https://www.mathematica.org/publications/design-based-estimators-for-average-treatment-effects-for-multi-armed-rcts
-->
