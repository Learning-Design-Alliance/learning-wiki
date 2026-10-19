---
type: strategy
id: three-step-ood-bloom-classifier-strategy
title: Three-step decision strategy for addressing model performance loss on novel OOD educational question datasets
description: The authors distill their findings into a decision rule for practitioners validating AI-assisted educational questions.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: michael-lawrence-castanares-2026
    resource: "https://arxiv.org/abs/2609.27749"
    title: "Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749"
    author: Michael Lawrence Castanares, Princess Ventures, and Allan Tan
---

# Three-step decision strategy for addressing model performance loss on novel OOD educational question datasets

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors distill their findings into a decision rule for practitioners validating AI-assisted educational questions. As printed: "First, if no access to annotated datasets, use BERT and LLMS which provide robust bloom classification performance. Second, if with access to sample OOD datasets with labels, explore feature engineering approaches (e.g., text splicing and addition of learning objectives) to transform OOD dataset to be similar to IID data. Third, if one has access to a large OOD labeled dataset (N > 1,000 samples), retrain the model."

## Design Implications

### Context
#### Requirements
- Access level to labeled OOD data determines which step applies; retraining requires a large labeled OOD dataset (N > 1,000 samples per the article)
#### Constraints
- Retraining requires a large dataset, particularly for complex models; splicing and learning-objective features helped on some datasets but not uniformly

### Target Learners
- K-12 and educational content developers validating AI-generated questions

### Target Learning Goals
- Scalable automated validation of pedagogical alignment of AI-generated educational materials

## Claims

- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](../claims/text-splicing-improves-ood-bloom-classification.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749
