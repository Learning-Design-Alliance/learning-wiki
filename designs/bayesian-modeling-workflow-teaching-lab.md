---
type: design
id: bayesian-modeling-workflow-teaching-lab
title: A five-step Bayesian modeling workflow for teaching-laboratory data analysis
description: "The article presents a reproducible Bayesian inference workflow progressing \"from explicitly deﬁning prior knowledge all the way to verifying that the ﬁnal inference reproduces expectations\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: matthew-heffernan-2022
    resource: "https://arxiv.org/abs/2104.08621"
    title: "Matthew Heffernan. (2022). How about that Bayes: Bayesian techniques and the simple pendulum. https://arxiv.org/abs/2104.08621"
    author: Matthew Heffernan
---

# A five-step Bayesian modeling workflow for teaching-laboratory data analysis

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article presents a reproducible Bayesian inference workflow progressing "from explicitly deﬁning prior knowledge all the way to verifying that the ﬁnal inference reproduces expectations". Its steps are: (1) defining a motivated prior, (2) prior predictive checks, (3) model validation via closure testing with pseudodata, (4) inference with real data, and (5) posterior predictive checks, followed by Bayesian model selection with the Bayes factor. Each step is described, motivated, and implemented before progressing to the next, and the workflow is offered as a general introduction to Bayesian techniques for the undergraduate physics curriculum.

## Design Implications

### Context
#### Requirements
- A well-designed step-by-step workflow so analysis can be broken into digestible, concrete steps and troubleshooting is straightforward
- Priors that are constraining but do not pre-determine or bias the result, since a prior that precludes the true result can never recover it
#### Constraints
- Generalizing the variance propagation to higher dimensions is beyond the scope of this work
- Only one parameter, g, is varied in the inference

### Target Learners
- undergraduate physics students in introductory teaching laboratories

### Learning Goals
- Bayesian statistical modeling and model selection
- systematic data analysis and model-to-data comparison in physics laboratories

### Claims
- Closure Testing Pendulum Models Self Consistent [+M]
- Posterior Predictive Reveals Small Angle Breakdown [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Matthew Heffernan. (2022). How about that Bayes: Bayesian techniques and the simple pendulum. https://arxiv.org/abs/2104.08621
