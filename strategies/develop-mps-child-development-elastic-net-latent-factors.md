---
type: strategy
id: develop-mps-child-development-elastic-net-latent-factors
title: Develop methylation profile scores of child development by training DNAm on latent within-person developmental change factors
description: The article proposes a concrete recipe for its forward pathway (pathway B in Fig.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
sources:
  - id: raffington-2024
    resource: "https://doi.org/10.1038/s41539-024-00239-5"
    title: "Raffington, L. (2024). Utilizing epigenetics to study the shared nature of development and biological aging across the lifespan. npj Science of Learning. https://doi.org/10.1038/s41539-024-00239-5"
    author: Raffington, L
---

# Develop methylation profile scores of child development by training DNAm on latent within-person developmental change factors

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article proposes a concrete recipe for its forward pathway (pathway B in Fig. 1): deriving methylation profile scores that reflect child development rather than adult aging. It states that "studies aiming to develop new MPSs of child development couldﬁrst generate latent factors of within-person change across physiological systems early in life and then use elastic net regression models to train DNAm on this latent factor". The resulting algorithm would be applied in separate target samples, with repeated measures used to disentangle stability and change in development across time.

## Design Implications

### Context
#### Requirements
- Prospective birth cohorts across multiple developmental systems (e.g., physiological, motoric, cognitive) measured at repeated time points starting at birth or earlier; discovery samples of several thousands of diverse individuals
#### Constraints
- The article notes these datasets are immensely expensive, effortful, and slow to generate, and sample sizes for MPS computation are typically several orders of magnitude smaller than needed for DNA-based summary scores

### Target Learners
- children from birth through adolescence, including children with developmental delay and acceleration

### Target Learning Goals
- quantifying the multi-system pace of child development and testing how it relates to later biological aging, health, and cognition

## Claims

- [An adult-derived methylation profile score of cognitive performance explains 11% of the variance in children's in-laboratory math performance](../claims/epigenetic-g-explains-child-math-variance.md) [+W]
- [Biological aging can be quantified early in the life course via methylation profile scores applied to child and adolescent samples](../claims/mps-biological-aging-quantified-early-life-course.md) [+W]
- [Cross-tissue correspondence of methylation profile scores is acceptable for saliva but lower for cheek samples, a major methodological concern](../claims/mps-cross-tissue-correspondence-saliva-cheek.md) [~W]
- [Children from underserved families show methylation profiles indicating advanced biological age, faster aging, higher inflammation, higher BMI, and lower cognitive health](../claims/underserved-children-advanced-biological-aging-mps.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Raffington, L. (2024). Utilizing epigenetics to study the shared nature of development and biological aging across the lifespan. npj Science of Learning. https://doi.org/10.1038/s41539-024-00239-5
