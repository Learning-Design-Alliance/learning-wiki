---
type: strategy
id: limited-information-then-efficient-em-sequential-procedure
title: Explore candidate models with limited-information estimation first, then estimate the structured model with the efficient EM algorithm
description: For settings where researchers have not yet settled on a model structure, the article recommends a two-stage workflow.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: rijmen-2009
    resource: "http://www.ets.org/research/contact.html"
    title: "Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html"
    author: Rijmen, F
---

# Explore candidate models with limited-information estimation first, then estimate the structured model with the efficient EM algorithm

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For settings where researchers have not yet settled on a model structure, the article recommends a two-stage workflow. In the exploratory stage, full information MML is not crucial; several models can be screened quickly with limited-information estimation techniques. The article states: "Once a good candidate model is established that incorporates a simplified structure, the parameters of this model can be estimated using the efficient EM algorithm." This pairs the speed of limited information methods with the statistical adequacy of full information MML for the final model.

## Design Implications

### Context
#### Requirements
- A simplified conditional independence structure must eventually be imposed on the chosen model for the efficient EM algorithm to apply
#### Constraints
- Without imposed structure, full information MML is stated to remain infeasible with increasing dimensionality, so the second stage depends on finding a simplified structure

### Target Learners
- Psychometricians and educational measurement researchers analyzing high-dimensional item response data

### Target Learning Goals
- Selecting and estimating an appropriate multidimensional IRT model for assessment data

## Related Strategies
- 

## Examples
-

## Key Sources
- Rijmen, F. (2009). Efficient Full Information Maximum Likelihood Estimation for Multidimensional IRT Models. ETS Research Report RR-09-03. http://www.ets.org/research/contact.html
