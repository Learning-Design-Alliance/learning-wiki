---
type: research-method
id: statistical-analysis-of-partially-nested-randomized-controlled-trials
title: Statistical analysis of partially nested randomized controlled trials
description: "Because PN-RCT treatment students are nested in intervention clusters while control students are not, analysis must use \"basic statistical models that adjust for the clustering of treatment students within intervention clusters\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-09
sources:
  - id: sharon-lohr-2014
    resource: "https://ies.ed.gov/ncer/"
    title: "Sharon Lohr, Peter Z. Schochet, Elizabeth Sanders. (2014). Partially Nested Randomized Controlled Trials in Education Research: A Guide to Design and Analysis. Washington, DC: U.S. Department of Education, Institute of Education Sciences, National Center for Education Research. https://ies.ed.gov/ncer/"
    author: Sharon Lohr, Peter Z. Schochet, Elizabeth Sanders
---

# Statistical analysis of partially nested randomized controlled trials

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
Because PN-RCT treatment students are nested in intervention clusters while control students are not, analysis must use "basic statistical models that adjust for the clustering of treatment students within intervention clusters". The guide supports this principle with "associated computer code for estimation" and worked examples interpreting model output.

## Accounts
<!-- How each source describes or uses the method -->
- **Analyze PN-RCT results with statistical models that adjust for the clustering of treatment students within intervention clusters**: Because PN-RCT treatment students are nested in intervention clusters while control students are not, analysis must use "basic statistical models that adjust for the clustering of treatment students within intervention clusters". The guide supports this principle with "associated computer code for estimation" and worked examples interpreting model output. (Sharon Lohr et al. (2014))
- **Partially nested regression model for matched-comparison designs with treatment-only clustering**: The partially nested (PN) RCT model of Lohr et al. (2014) handles designs in which treatment students are nested in groups (teachers or intervention clusters) but comparison students are not. Instead of treating the treatment-effect coefficient as fixed, the model treats it as a random effect with an error term, allowing additional variation at the cluster level for the treatment group only. The authors apply it to a quasi-experimental matched comparison design, including pretest scores as a covariate, suppressing the Level 2 random intercept, and modeling independent residual variances that differ by treatment condition. (Huang et al. (2025))
- **Technical appendixes covering advanced statistical topics for PN-RCTs**: Beyond the basic models, the guide includes "Chapter 4 and the technical appendixes" which "discuss more advanced statistical topics pertaining to PN-RCTs". These serve researchers with more advanced knowledge, complementing the introductory treatment aimed at applied education researchers. (Sharon Lohr et al. (2014))
- **Partially Nested RCTs: a design taxonomy distinguishing I-RCTs, C-RCTs, and PN-RCTs**: The guide defines three education experiment designs. In an I-RCT, "individual students are randomized directly to the treatment or control group"; in a C-RCT, "clusters of students (e.g., classrooms) are randomized". The PN-RCT is the hybrid: treatment students are nested in higher-level units while control students remain unclustered, making the design "partially nested". (Sharon Lohr et al. (2014))

### Claims
- [PN-RCTs arise when treatment students are clustered but control students receive the protocol individually](../claims/pn-rct-arises-from-clustered-treatment-individual-control.md) [+W]
- [PN-RCT design choices include random assignment possibilities, cluster formation, statistical power, and confounding factors](../claims/pn-rct-design-issues-random-assignment-power-confounding.md) [+W]
- [Sample size formulas for clustered designs with school- or teacher-level random assignment are derived using generalized estimating equation methods](../claims/gee-sample-size-formulas-clustered-school-rcts.md) [+W]

## Related Research Methods
-

## Key Sources
- Sharon Lohr, Peter Z. Schochet, Elizabeth Sanders. (2014). Partially Nested Randomized Controlled Trials in Education Research: A Guide to Design and Analysis. Washington, DC: U.S. Department of Education, Institute of Education Sciences, National Center for Education Research. https://ies.ed.gov/ncer/
- Huang, C.-W., Feng, M., & Li, L. (2025). Applying a partially nested regression model to evaluate the impact of ASSISTments on middle school students' math achievement. WestEd. https://www.wested.org

<!-- merged 2026-10-10 from elements/pn-rct-technical-appendices-advanced-topics ("Technical appendixes covering advanced statistical topics for PN-RCTs"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Technical appendixes covering advanced statistical topics for PN-RCTs

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
Beyond the basic models, the guide includes "Chapter 4 and the technical appendixes" which "discuss more advanced statistical topics pertaining to PN-RCTs". These serve researchers with more advanced knowledge, complementing the introductory treatment aimed at applied education researchers.

## Design Implications

### Context
#### Requirements
- Readers need more advanced knowledge of quantitative methods to benefit from the technical examples and appendices
#### Constraints
- 

### Target Learners
- education researchers with advanced knowledge of quantitative impact evaluation methods

### Target Learning Goals
- advanced design and analysis of partially nested randomized trials

## Related Elements
- 

## Examples
-

## Key Sources
- Sharon Lohr, Peter Z. Schochet, Elizabeth Sanders. (2014). Partially Nested Randomized Controlled Trials in Education Research: A Guide to Design and Analysis. Washington, DC: U.S. Department of Education, Institute of Education Sciences, National Center for Education Research. https://ies.ed.gov/ncer/
-->

<!-- merged 2026-10-10 from theories/pn-rct-design-taxonomy ("Partially Nested RCTs: a design taxonomy distinguishing I-RCTs, C-RCTs, and PN-RCTs"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Partially Nested RCTs: a design taxonomy distinguishing I-RCTs, C-RCTs, and PN-RCTs

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The guide defines three education experiment designs. In an I-RCT, "individual students are randomized directly to the treatment or control group"; in a C-RCT, "clusters of students (e.g., classrooms) are randomized". The PN-RCT is the hybrid: treatment students are nested in higher-level units while control students remain unclustered, making the design "partially nested".

## Design Implications

### Context
#### Requirements
- Treatment-group students must be nested in some higher-level unit such as a tutoring group or class, while control-group students are unclustered as part of the experimental design
#### Constraints
- 

### Target Learners
- students in educational intervention studies

### Target Learning Objectives
- rigorous impact evaluation of educational interventions

### Claims

- [PN-RCTs arise when treatment students are clustered but control students receive the protocol individually](../claims/pn-rct-arises-from-clustered-treatment-individual-control.md) [+W]
- [PN-RCT design choices include random assignment possibilities, cluster formation, statistical power, and confounding factors](../claims/pn-rct-design-issues-random-assignment-power-confounding.md) [+W]
- [Sample size formulas for clustered designs with school- or teacher-level random assignment are derived using generalized estimating equation methods](../claims/gee-sample-size-formulas-clustered-school-rcts.md) [+W]

## Related Theories

- [Opportunistic experiments: RCTs of planned interventions or policy changes with minimal added disruption and cost](../research-methods/systematic-screening-for-opportunistic-experiments.md)

## Examples

- [Follow a step-by-step estimation procedure with example-based computer code when analyzing PN-RCT data](../strategies/step-by-step-pn-rct-model-estimation-guide.md)

## Key Sources
- Sharon Lohr, Peter Z. Schochet, Elizabeth Sanders. (2014). Partially Nested Randomized Controlled Trials in Education Research: A Guide to Design and Analysis. Washington, DC: U.S. Department of Education, Institute of Education Sciences, National Center for Education Research. https://ies.ed.gov/ncer/
-->
