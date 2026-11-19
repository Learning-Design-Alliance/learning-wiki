---
type: design
id: bci-mcq-p300-speller-framework
title: "BCI exam-evaluation framework: a special case of the P300 speller restricted to answers A–D with an LDA pipeline"
description: "The article proposes a framework for automatic exam evaluation in which the system \"can be considered as a special case of P300 speller accepting only letters from A to D\", the possible answers to multiple-choice ques..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: hameda-f-balat-2020
    resource: "http://www.ijcaonline.org"
    title: "Hameda F. Balat, M.A. El-dosuky, El-Saeed M. Abd El-Razek, Magdi Z. Rashed. (2020). Automatic Exam Evaluation based on Brain Computer Interface. International Journal of Computer Applications, Volume 175 – No. 25. http://www.ijcaonline.org"
    author: Hameda F. Balat, M.A. El-dosuky, El-Saeed M. Abd El-Razek, Magdi Z. Rashed
---

# BCI exam-evaluation framework: a special case of the P300 speller restricted to answers A–D with an LDA pipeline

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes a framework for automatic exam evaluation in which the system "can be considered as a special case of P300 speller accepting only letters from A to D", the possible answers to multiple-choice questions. The teacher authors exams and stores them in an exam database; enrolled students record brain signals that undergo low and high pass filtering, subsampling and segmentation, with the resulting features used as inputs to Linear Discriminant Analysis. The system works online and is based on a recorded brain signal dataset.

## Design Implications

### Context
#### Requirements
- Students must enroll into the system and record their brain signals
- A teacher-made exam database delivering multiple-choice questions with answers A to D
#### Constraints
- Restricted to multiple-choice questions with letter answers A to D; the article states future work may consider other question types

### Target Learners
- higher education students
- second-year Computer Teacher Preparation students

### Learning Goals
- measuring intended learning outcomes through automatic exam evaluation

### Claims
- Bci Mcq Exam System 91 Percent Accuracy [+M]
- [Bci Accuracy Degrades To Zero At 98 Percent Noise](../claims/bci-accuracy-degrades-to-zero-at-98-percent-noise.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hameda F. Balat, M.A. El-dosuky, El-Saeed M. Abd El-Razek, Magdi Z. Rashed. (2020). Automatic Exam Evaluation based on Brain Computer Interface. International Journal of Computer Applications, Volume 175 – No. 25. http://www.ijcaonline.org
