---
type: strategy
id: nrm-partial-credit-scoring-strategy
title: Use NRM-based rankings of all response options to build data-driven partial-credit scoring and more formative score reports
description: The article proposes that ranking all response options to each item may lead to a data-driven model for assigning partial credit, and that combining these methods with multidimensional IRT analyses would give multiple...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: trevor-i-smith-2024
    resource: "https://arxiv.org/abs/2410.05231"
    title: "Trevor I. Smith, Mohammad A. Kazmi, Richard R. Sarles, III, Joshua A. Sbrana, Cody W. Soper, and Nasrine Bendjilali. (2024). Comparing item response theory models for ranking incorrect response options. https://arxiv.org/abs/2410.05231"
    author: Trevor I. Smith, Mohammad A. Kazmi, Richard R. Sarles, III, Joshua A. Sbrana, Cody W. Soper, and Nasrine Bendjilali
---

# Use NRM-based rankings of all response options to build data-driven partial-credit scoring and more formative score reports

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (5 for, 3 mixed) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 8 claims rest on one study

## Description
The article proposes that ranking all response options to each item may lead to a data-driven model for assigning partial credit, and that combining these methods with multidimensional IRT analyses would give multiple subtopic scores showing students their progress. The authors write that "A more formative score report could help to reduce the sense of exclusivity in physics by focusing on what students understand, not only on what they don't understand." Specific methods for assigning partial-credit values are left to future work.

## Design Implications

### Context
#### Requirements
- A consistent ranking representative of the introductory physics student population must first be achieved
- A sufficiently large data set: about 20 students for every response option (e.g., 500 students for a 5-item test with five response options per item)
#### Constraints
- The specific methods for assigning partial-credit values based on the rankings are beyond the scope of this paper
- The article's own results show rankings are not yet consistent across data sets for most items

### Target Learners
- introductory physics students
- students from populations traditionally underrepresented in physics

### Target Learning Goals
- formative feedback on progress across subtopics of Newtonian force and motion concepts

### Affordances
- [Nrm Ranking Incorrect Responses](../research-methods/item-response-theory-irt.md)

## Claims

- [Some items have incorrect responses ranked consistently highest across analyses that are not the most commonly chosen, suggesting some incorrect responses are better than the most common](../claims/consistent-highest-ranked-incorrect-not-most-common.md) [+W]
- [The most commonly chosen incorrect response ranks higher in DS2full than DS1full rankings for nearly all items](../claims/most-common-incorrect-ranked-higher-ds2.md) [~W]
- [NRM analyses without specifying the correct response unambiguously identify the correct response and generally agree with prior 2PL-NRM rankings](../claims/nrm-identifies-correct-response-consistent-with-2pl-nrm.md) [+W]
- [NRM rankings of incorrect responses differ noticeably between independent data sets for most FMCE items](../claims/nrm-rankings-inconsistent-across-datasets.md) [~W]
- [Rankings of incorrect responses appear stable across instruction, and students shift toward the highest-ranked incorrect response after instruction](../claims/rankings-stable-across-instruction.md) [+W]
- [Ranking discrepancies may result from response rates for less commonly chosen responses, whose parameters are more sensitive to individual students](../claims/rare-response-rates-explain-ranking-discrepancies.md) [~W]
- [A 2PL-NRM nested logit IRT model applied to over 7,000 students' FMCE responses yields a unique ak parameter for every incorrect response, enabling a quantitative ranking of incorrect answers](../claims/irt-nested-logit-ranks-incorrect-responses.md) [+W]
- [Students with above-average latent understanding (theta > 0) are more likely to choose both the correct response and the highest-ranked incorrect response on FMCE questions 14, 18, and 19](../claims/high-theta-students-choose-better-incorrect-responses.md) [+W]

## Related Strategies

- [Test and extend incorrect-response rankings using matched pre/post transitions and conditional probabilities](test-rankings-prepost-transitions-strategy.md)

## Examples
-

## Key Sources
- Trevor I. Smith, Mohammad A. Kazmi, Richard R. Sarles, III, Joshua A. Sbrana, Cody W. Soper, and Nasrine Bendjilali. (2024). Comparing item response theory models for ranking incorrect response options. https://arxiv.org/abs/2410.05231
