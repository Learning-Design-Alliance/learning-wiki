---
type: element
id: medical-exam-mcq-difficulty-response-time-dataset
title: Dataset of approximately 18,000 multiple-choice questions from a high-stakes medical exam
description: "The study's data are approximately 18,000 multiple-choice questions from a high-stakes medical exam, each with difficulty and response time parameters used as prediction targets."
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

# Dataset of approximately 18,000 multiple-choice questions from a high-stakes medical exam

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The study's data are approximately 18,000 multiple-choice questions from a high-stakes medical exam, each with difficulty and response time parameters used as prediction targets. The paper states it examines "the prediction of the difficulty and response time parameters for ≈ 18,000 multiple-choice questions from a high-stakes medical exam." The dataset serves as the testbed for the transfer learning experiments and the signal-type comparisons.

## Design Implications

### Context
#### Requirements
- Items must have difficulty and response time parameters available as prediction targets
#### Constraints
- The sample is drawn from a single high-stakes medical exam

### Target Learners
- medical exam candidates

### Target Learning Goals
- predicting item difficulty and response time for assessment items

## Claims

- [All parts of the item were important for predicting response time](../claims/all-item-parts-important-response-time-prediction.md) [+W]
- [Item difficulty was best predicted using signal from the item stem](../claims/difficulty-best-predicted-from-item-stem.md) [+W]
- [Transfer learning improves prediction of item difficulty when response time is used as an auxiliary task, but not the other way around](../claims/transfer-learning-difficulty-prediction-auxiliary-response-time.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/
