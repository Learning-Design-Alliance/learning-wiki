---
type: theory
title: Transfer learning approach to predicting item difficulty and response time, varying representation abstraction and item component input
description: The paper frames item parameter prediction as a transfer learning problem in which a model trained on one task (e.g., response time) supports prediction of another (e.g., difficulty).
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: kang-xue-2020
    resource: "https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/"
    title: "Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/"
    author: Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin
---

# Transfer learning approach to predicting item difficulty and response time, varying representation abstraction and item component input

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The paper frames item parameter prediction as a transfer learning problem in which a model trained on one task (e.g., response time) supports prediction of another (e.g., difficulty). It also explores "the type of the signal that bestpredicts difficulty and response time ... both in terms of representation abstraction and item component used as input (e.g., whole item, answer options only, etc.)." This two-axis exploration — representation abstraction and input component — organizes the study's modeling comparisons.

## Design Implications

### Context
#### Requirements
- Models require item text components (e.g., whole item, answer options, stem) as input
- Auxiliary task labels (difficulty or response time) must be available for transfer
#### Constraints
- The reported benefit of transfer is limited to difficulty prediction with response time as the auxiliary task, for the authors' sample

### Target Learners
- assessment developers
- psychometric researchers

### Target Learning Objectives
- predicting item difficulty and response time parameters

### Claims
- [Transfer Learning Difficulty Prediction Auxiliary Response Time](../claims/transfer-learning-difficulty-prediction-auxiliary-response-time.md) [+M]
- [Difficulty Best Predicted From Item Stem](../claims/difficulty-best-predicted-from-item-stem.md) [+M]
- [All Item Parts Important Response Time Prediction](../claims/all-item-parts-important-response-time-prediction.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/
