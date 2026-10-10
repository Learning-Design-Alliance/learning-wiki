---
type: theory
title: Bayes factors as interpretable weight of evidence for competing scientific theories
description: The article frames the Bayes factor as a hypothesis-testing framework whose outcome is directly interpretable as evidence for competing theories.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: mulder-2021
    resource: "https://doi.org/10.18637/jss.v100.i18"
    title: "Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C. (2021). BFpack: Flexible Bayes factor testing of scientific theories in R. Journal of Statistical Software, 100(18), 1–63. https://doi.org/10.18637/jss.v100.i18"
    author: "Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C"
---

# Bayes factors as interpretable weight of evidence for competing scientific theories

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article frames the Bayes factor as a hypothesis-testing framework whose outcome is directly interpretable as evidence for competing theories. It cites "the interpretability of the outcome as the weight of evidence provided by the data in support of competing scientific theories." The framework's flexibility comes from testing multiple hypotheses simultaneously and testing complex hypotheses involving equality as well as order constraints on parameters of interest. BFpack operationalizes this framework in software for the social and behavioral sciences and related fields.

## Design Implications

### Context
#### Requirements
- Competing hypotheses must be expressible with equality and/or order constraints on the parameters of interest for confirmatory testing
#### Constraints
- The article notes methodological developments are situated in the social and behavioral sciences and related fields

### Target Learners
- Researchers in the social and behavioral sciences and related fields

### Target Learning Objectives
- Evaluating competing scientific theories through Bayesian hypothesis testing

### Claims
- [Bfpack Exploratory Confirmatory Testing Tools](../claims/bfpack-exploratory-confirmatory-testing-tools.md) [+M]

## Related Theories

- [Bayes factor testing of homogeneous within-person variance in hierarchical models](bayes-factor-homogeneous-within-person-variance-testing.md)
- [Membership model for classifying individuals into the common variance model](membership-model-common-variance-classification.md)

## Examples

- [BFpack: an R package for Bayes factor hypothesis testing of common statistical testing problems](../products/bfpack.md)
- [vICC R package for Bayesian testing of within-person variance homogeneity](../products/vicc-r-package.md)

## Key Sources
- Mulder, J., Williams, D., Gu, X., Tomarken, A., Böing-Messing, F., Olsson-Collentine, A., Meijerink-Bosman, M., Menke, J., van Aert, R., Fox, J.-P., Hoijtink, H., Rosseel, Y., Wagenmakers, E.-J., & van Lissa, C. (2021). BFpack: Flexible Bayes factor testing of scientific theories in R. Journal of Statistical Software, 100(18), 1–63. https://doi.org/10.18637/jss.v100.i18
