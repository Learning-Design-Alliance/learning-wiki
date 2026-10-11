---
type: strategy
id: question-level-partitioning-strategy
title: Partition at the question level or with grouped controls when evaluating transfer to unseen questions
description: The article recommends how researchers should construct training and evaluation partitions for this dataset.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: jahangir-alam-sm-2026
    resource: "https://arxiv.org/abs/2608.22346"
    title: "Jahangir Alam SM, Md Khalid Syfullaha, Saad Ahmed, Munira Akter Mou, A K Z Rasel Rahman, A.K.M. Masudur Rahman, Mohammed Sowket Ali. (2026). Multimodal examination answer data with expert-designed Outcome-Based Education rubrics for criterion-level assessment. arXiv. https://arxiv.org/abs/2608.22346"
    author: Jahangir Alam SM, Md Khalid Syfullaha, Saad Ahmed, Munira Akter Mou, A K Z Rasel Rahman, A.K.M. Masudur Rahman, Mohammed Sowket Ali
---

# Partition at the question level or with grouped controls when evaluating transfer to unseen questions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends how researchers should construct training and evaluation partitions for this dataset. It advises that "Training and evaluation partitions should be created at the question level or with grouped controls when the research objective involves transfer to unseen questions", because random answer-level splitting can place visually related responses to the same prompt in every partition. Criterion marks may be represented in original units or divided by criterion maxima, with question and subject labels kept for stratification.

## Design Implications

### Context
#### Requirements
- Question and subject labels should remain available for stratification
- Sampling plans and uncertainty estimates should reflect the subject imbalance
#### Constraints
- Any generated feedback should be treated as a research output and must not be presented as an official grade

### Target Learners
- document-AI and assessment researchers using the dataset

### Target Learning Goals
- cross-question generalization evaluation
- robust multimodal score prediction

## Related Strategies
- 

## Examples
-

## Key Sources
- Jahangir Alam SM, Md Khalid Syfullaha, Saad Ahmed, Munira Akter Mou, A K Z Rasel Rahman, A.K.M. Masudur Rahman, Mohammed Sowket Ali. (2026). Multimodal examination answer data with expert-designed Outcome-Based Education rubrics for criterion-level assessment. arXiv. https://arxiv.org/abs/2608.22346
