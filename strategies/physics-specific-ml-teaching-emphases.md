---
type: strategy
id: physics-specific-ml-teaching-emphases
title: "Emphasize physics-specific content: literature searching, domain-knowledge-driven feature engineering, comparison of ML with inference-based solutions, and uncertainty estimation."
description: When teaching ML to physicists the author recommends four emphases.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: viviana-acquaviva-2021
    resource: "https://arxiv.org/abs/2108.08313"
    title: "Viviana Acquaviva. (2021). Teaching Machine Learning for the Physical Sciences: A summary of lessons learned and challenges. Proceedings of the 2nd Teaching in Machine Learning Workshop, PMLR. https://arxiv.org/abs/2108.08313"
    author: Viviana Acquaviva
---

# Emphasize physics-specific content: literature searching, domain-knowledge-driven feature engineering, comparison of ML with inference-based solutions, and uncertainty estimation.

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
When teaching ML to physicists the author recommends four emphases. Reading applied papers builds literature searching and skimming skills. Exercises that "rely on domain knowledge" — such as why photometric colors may be better redshift features than magnitudes — reinforce that "understanding the data before attempting feature engineering is very important". Class discussion can compare inference-based versus machine-learning approaches. Finally, in Physics we "never want to quote a result without stating some level of confidence in our estimate", so epistemic and aleatoric uncertainty estimation is discussed.

## Design Implications

### Context
#### Requirements
- Students must have domain knowledge of the physical science data (e.g., understanding spectra and colors) for the feature-engineering exercises to work.
#### Constraints
- The exemplar uncertainties discussion uses the epistemic/aleatoric classification from Kendall & Gal (2017), with the former referring to the data set as a whole and the latter characterizable on an object-by-object basis.

### Target Learners
- Physics and astronomy students

### Target Learning Goals
- Literature searching, domain-grounded feature engineering, method comparison, and uncertainty estimation

## Related Strategies

- [Design exercises that ask students to match or beat the performance of a published paper, and seed proposed solutions with deliberate poor choices for students to improve.](match-or-beat-published-paper-exercises.md)
- [Support teachers of measurement uncertainty with concept-based teaching, examples, exercises, software and exchange of good practices](support-uncertainty-teachers-concept-based-examples-exercises.md)

## Examples
-

## Key Sources
- Viviana Acquaviva. (2021). Teaching Machine Learning for the Physical Sciences: A summary of lessons learned and challenges. Proceedings of the 2nd Teaching in Machine Learning Workshop, PMLR. https://arxiv.org/abs/2108.08313
