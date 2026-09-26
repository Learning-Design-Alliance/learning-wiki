---
type: theory
title: "Three multidimensional IRT models for testlet-based tests: bifactor, testlet, and second-order models"
description: The report describes three multidimensional IRT models that account for conditional dependence among items sharing a testlet stimulus by incorporating testlet-specific dimensions.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: rijmen-2009
    resource: "http://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2009). Three Multidimensional Models for Testlet-Based Tests: Formal Relations and an Empirical Comparison. ETS Research Report RR-09-37. http://www.ets.org/research/contact.html"
    author: Rijmen, F
---

# Three multidimensional IRT models for testlet-based tests: bifactor, testlet, and second-order models

> **Theory** · [All theories](index.md)

## Description
The report describes three multidimensional IRT models that account for conditional dependence among items sharing a testlet stimulus by incorporating testlet-specific dimensions. In the bifactor model, "each item measures a general dimension in addition to a testlet-specific dimension." The testlet model constrains specific loadings to be proportional to general loadings within each testlet, and in the second-order model items load only on testlet-specific factors whose correlations are modeled through a second-order factor. The report shows the latter two are formally equivalent and can be formulated as restricted bifactor models, and estimates all three within a common full-information maximum likelihood framework.

## Design Implications

### Context
#### Requirements
- Conditional independence of the specific dimensions given the general dimension, as assumed for the efficient EM algorithm
- Identification restrictions: locations and scales of dimensions fixed, plus K restrictions from rotational invariance
#### Constraints
- The formal equivalences hold under the stated identification and conditional-independence assumptions; a multivariate normal distribution is assumed for the latent variables in the application

### Target Learners
- test takers of standardized testlet-based assessments, such as the international English assessment test analyzed

### Target Learning Objectives
- accurate measurement of the general latent ability (e.g., reading ability) when items are organized in testlets

### Claims
- [Second Order Model Equivalent To Testlet Model](../claims/second-order-model-equivalent-to-testlet-model.md) [+M]
- [Bifactor Model Preferred Aic Bic Testlet Test](../claims/bifactor-model-preferred-aic-bic-testlet-test.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Rijmen, F. (2009). Three Multidimensional Models for Testlet-Based Tests: Formal Relations and an Empirical Comparison. ETS Research Report RR-09-37. http://www.ets.org/research/contact.html
