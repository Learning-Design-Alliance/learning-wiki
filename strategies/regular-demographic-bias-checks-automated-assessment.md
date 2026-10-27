---
type: strategy
id: regular-demographic-bias-checks-automated-assessment
title: Run regular bias checks comparing model and human scoring across demographic groups when deploying automated assessment
description: "The authors operationalize bias as a situation where \"the model exhibits a higher error rate when transcribing speech of students from specific socio-economic or demographic groups compared to human raters,\" and recom..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: henkel-2025
    resource: "https://doi.org/10.1007/s40593-024-00435-9"
    title: "Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9"
    author: "Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J"
---

# Run regular bias checks comparing model and human scoring across demographic groups when deploying automated assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The authors operationalize bias as a situation where "the model exhibits a higher error rate when transcribing speech of students from specific socio-economic or demographic groups compared to human raters," and recommend that "these types of checks should be conducted regularly" when automated assessments are deployed. The check compares model-vs-human score discrepancies, not total error, across groups such as gender and home language.

## Design Implications

### Context
#### Requirements
- Demographic information linked to each response
- A human-rater gold standard for the same recordings
#### Constraints
- The authors note it can be challenging to determine whether an algorithm functions equally well for different groups given non-public training data; potential human-rater bias fell outside their study's scope

### Target Learners
- Students in linguistically and demographically diverse educational contexts

### Target Learning Goals
- Equitable automated assessment of foundational literacy skills

## Claims

- [No statistically significant evidence that the model scores Ghanaian students differently by gender or home language relative to human raters](../claims/no-significant-asr-bias-gender-home-language.md) [+W]
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](../claims/baseline-ml-models-biased-tpr-oulad.md) [+W]

## Related Strategies

- [Mitigating Racial Bias in Edtech Products](mitigating_racial_bias_in_edtech_products.md)

## Examples
-

## Key Sources
- Henkel, O., Horne-Robinson, H., Hills, L., Roberts, B., & McGrane, J. (2025). Supporting Literacy Assessment in West Africa: Using State-of-the-Art Speech Models to Assess Oral Reading Fluency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00435-9
