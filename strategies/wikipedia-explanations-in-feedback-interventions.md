---
type: strategy
id: wikipedia-explanations-in-feedback-interventions
title: Include automatically generated Wikipedia-based explanations in the intervention set for personalized feedback
description: "The article recommends including Wikipedia-based explanations among the pedagogical interventions an ITS uses to personalize feedback, because they \"provide alternative ways of helping students to understand and remem..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: kochmar-2020
    resource: "https://arxiv.org/abs/2005.02431"
    title: "Kochmar, E., Vu, D.D., Belfer, R., Gupta, V., Serban, I.V., Pineau, J. (2020). Automated Personalized Feedback Improves Learning Gains in an Intelligent Tutoring System. arXiv preprint. https://arxiv.org/abs/2005.02431"
    author: Kochmar, E., Vu, D.D., Belfer, R., Gupta, V., Serban, I.V., Pineau, J
---

# Include automatically generated Wikipedia-based explanations in the intervention set for personalized feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article recommends including Wikipedia-based explanations among the pedagogical interventions an ITS uses to personalize feedback, because they "provide alternative ways of helping students to understand and remember concepts" and are generated automatically from crawled Wikipedia articles. A Decision Tree classifier trained on positive and negative examples with linguistically-motivated features selects the most appropriate explanations among generated candidates.

## Design Implications

### Context
#### Requirements
- A crawled domain-specific Wikipedia dataset from which explanation sentences are extracted
- A trained classifier to evaluate explanation quality using linguistically-motivated features
#### Constraints
- Evaluated only in the machine learning domain on the Korbit platform

### Target Learners
- online students in data science and machine learning courses

### Target Learning Goals
- understanding and remembering concepts after incorrect solution attempts

## Claims

- [Automatically generated Wikipedia-based explanations produce learning gains comparable to personalized hints and are rated helpful by students](../claims/wikipedia-based-explanations-comparable-gains.md) [+W]
- [Students rate pairs of extracted and generated Wikipedia-based explanations as helpful 83.33% of the time, more than either type alone](../claims/wikipedia-explanations-both-types-preferred.md) [+W]
- [A Decision Tree classifier distinguishes high- from low-quality Wikipedia-based explanations with an F1 score of 80.32% on the validation set](../claims/decision-tree-explanation-quality-f1-80.md) [+W]
- [Wikipedia-based explanation success rates (17.65%) are far lower than personalized hints (60.47%), with no significant difference between extracted and generated types](../claims/wikipedia-explanations-low-success-rate.md) [-W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Kochmar, E., Vu, D.D., Belfer, R., Gupta, V., Serban, I.V., Pineau, J. (2020). Automated Personalized Feedback Improves Learning Gains in an Intelligent Tutoring System. arXiv preprint. https://arxiv.org/abs/2005.02431
