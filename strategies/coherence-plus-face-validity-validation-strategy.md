---
type: strategy
id: coherence-plus-face-validity-validation-strategy
title: Validate unsupervised topic models with coherence scores plus expert face validity
description: "For unsupervised text analysis, the article recommends combining statistical and human validation: \"Our primary metric for evaluating our models was to compute the average coherence score based the top 20 words in eac..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: tor-ole-b-odden-2018
    resource: "https://github.com/uio-ccse/PERC_TopicModel"
    title: "Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero. (2018). Thematic Analysis of 18 Years of PERC Proceedings using Natural Language Processing. https://github.com/uio-ccse/PERC_TopicModel"
    author: Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero
---

# Validate unsupervised topic models with coherence scores plus expert face validity

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 associational, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
For unsupervised text analysis, the article recommends combining statistical and human validation: "Our primary metric for evaluating our models was to compute the average coherence score based the top 20 words in each topic", supplemented with face-validity judgments from community members familiar with the literature. This follows Grimmer and Stewart's principles that such models are imprecise, cannot replace human analysis, and require multi-method validation.

## Design Implications

### Context
#### Requirements
- Researchers must evaluate and validate results using a variety of methods, since unsupervised methods have no ground truth
- Human domain experts remain the most reliable evaluators of topic meaning
#### Constraints
- Perplexity was not used because it correlates poorly with human interpretability; qualitative comparison methods were left for future work

### Target Learners
- education researchers applying NLP to literature analysis

### Target Learning Goals
- rigorous, replicable automated thematic analysis of educational research corpora

### Affordances
- [Lda Topic Model Framework](../research-methods/lda-based-topic-modeling-for-educational-assessment-corpora.md)

## Claims

- [Random-initialization instability in LDA was addressed by clustering topics across 500 runs and selecting the most central model](../claims/clustering-aggregation-stabilizes-lda.md) [+W]
- [LDA topic modelling of free-text feedback yielded six topics consolidated into themes of ease, assessment, comprehension, interactivity, clarity and summary](../claims/lda-six-topics-course-feedback.md) [+W]

## Related Strategies

- [Validate LDA topic-model outcomes by combining thematic analysis with multilevel regression](validate-topics-thematic-analysis-multilevel-regression.md)

## Examples
-

## Key Sources
- Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero. (2018). Thematic Analysis of 18 Years of PERC Proceedings using Natural Language Processing. https://github.com/uio-ccse/PERC_TopicModel
