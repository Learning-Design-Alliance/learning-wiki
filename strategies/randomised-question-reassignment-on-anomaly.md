---
type: strategy
id: randomised-question-reassignment-on-anomaly
title: Randomised question-set reassignment when suspicious IP addresses or abnormal behaviour are detected
description: "An implementable prevention mechanism for online examinations: candidates are randomly assigned one of several question sets at verification, and the system reassigns a different set when risk signals appear."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: leslie-ching-ow-tiong-and-heejeong-jasmine-lee-2021
    resource: "https://arxiv.org/abs/2101.09841"
    title: "Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. https://arxiv.org/abs/2101.09841"
    author: Leslie Ching Ow Tiong and HeeJeong Jasmine Lee
---

# Randomised question-set reassignment when suspicious IP addresses or abnormal behaviour are detected

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
An implementable prevention mechanism for online examinations: candidates are randomly assigned one of several question sets at verification, and the system reassigns a different set when risk signals appear. The article specifies that "If any abnormal behaviour is detected, the system changes the questions randomly to another Set (e.g., Set B)." Likewise, if a student logs in from an IP previously recorded as suspicious, the system generates a different question set for that student, and warning messages are sent to instructors.

## Design Implications

### Context
#### Requirements
- several sets of exam questions prepared in advance and an IP list of previously recorded suspicious addresses
#### Constraints
- the related eight-step model literature notes randomised approaches require teachers to change the questions every semester

### Target Learners
- students taking online examinations

### Target Learning Goals
- preventing cheating at online examinations

## Claims

- [DenseLSTM achieves the highest AUC values of 0.9972 (mid-term) and 0.9760 (final-term) for classifying normal and abnormal behaviour](../claims/denselstm-highest-auc-values.md) [+W]
- [DenseLSTM achieves the highest overall accuracy of 95.32% for detecting abnormal student behaviour at online examinations, outperforming LSTM, RNN and DNN benchmarks](../claims/denselstm-highest-overall-accuracy-95-32.md) [+W]
- [DenseLSTM accuracy exceeds 92% on both mid-term (97.77%) and final-term (92.86%) examinations](../claims/denselstm-midterm-finalterm-accuracies.md) [+W]
- [The DNN benchmark performs poorly, with 82.74% mid-term and 52.68% final-term accuracy, and its error rates are associated with false prevention from extremely slow answer selection](../claims/dnn-benchmark-low-accuracy-false-prevention.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Leslie Ching Ow Tiong and HeeJeong Jasmine Lee. (2021). E-cheating Prevention Measures: Detection of Cheating at Online Examinations Using Deep Learning Approach - A Case Study. https://arxiv.org/abs/2101.09841
