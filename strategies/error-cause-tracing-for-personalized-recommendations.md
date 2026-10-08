---
type: strategy
id: error-cause-tracing-for-personalized-recommendations
title: Use traced error causes as personalized intervention recommendations in online learning systems
description: "The article proposes that diagnosing the causes of a student's systematic errors can guide adapting education to individual needs: the SET model \"returns predicted probabilities for all considered causes, which may fu..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: savi-2021
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    title: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    author: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J"
---

# Use traced error causes as personalized intervention recommendations in online learning systems

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article proposes that diagnosing the causes of a student's systematic errors can guide adapting education to individual needs: the SET model "returns predicted probabilities for all considered causes, which may function as intervention recommendations for a tutor." Because a single observed error can have multiple possible causes that differ across individuals and over time, recommendations should be based on a student's own pattern of successive errors rather than on population-level error frequencies alone. The approach suits online learning systems where errors can be automatically detected and mapped to causes.

## Design Implications

### Context
#### Requirements
- An error-to-cause bigraph for the domain and software that can automatically detect errors
#### Constraints
- Error responses are not ubiquitous, not necessarily consistent, and their causes may change over time, so inference relies on limited data

### Target Learners
- individual students in online adaptive practice systems

### Target Learning Goals
- targeted remediation of systematic error causes, e.g., in arithmetic

### Affordances
- [Systematic Error Tracing Model](../theories/systematic-error-tracing-model.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382
