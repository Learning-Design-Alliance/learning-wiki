---
type: strategy
id: session-state-features-cross-course-intervention
title: Use course-independent session-state features to enable cross-course prediction and personalized intervention
description: The article recommends representing clickstreams as graphical-model session states rather than raw clicks when prediction must transfer to other courses.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: yohan-jo-2018
    resource: "https://arxiv.org/abs/1809.04177"
    title: "Yohan Jo, Keith Maki, Gaurav Tomar. (2018). Time Series Analysis of Clickstream Logs from Online Courses. https://arxiv.org/abs/1809.04177"
    author: Yohan Jo, Keith Maki, Gaurav Tomar
---

# Use course-independent session-state features to enable cross-course prediction and personalized intervention

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article recommends representing clickstreams as graphical-model session states rather than raw clicks when prediction must transfer to other courses. Raw clicks were most informative within a course but are "incorporated with course-speciﬁc information", while session states are "almost course-independent and thus the most generalizable among the three feature sets". Instructors could use early-course predictions to "provide personalized support to different supports in form of adaptive interventions".

## Design Implications

### Context
#### Requirements
- States for a new course must be inferred via maximum likelihood estimation for MMM states and the Viterbi algorithm for HMM states
#### Constraints
- Click category features predicted final grades poorly even within the training course, so generalizability alone is insufficient

### Target Learners
- MOOC students, particularly struggling students identified early in a course

### Target Learning Goals
- Early identification of students at risk of low grades to support adaptive interventions

## Claims

- [LSTM with HMM session-state features transfers to a different course, significantly outperforming SVM for a majority of configurations](../claims/lstm-hmm-features-generalize-across-courses.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yohan Jo, Keith Maki, Gaurav Tomar. (2018). Time Series Analysis of Clickstream Logs from Online Courses. https://arxiv.org/abs/1809.04177
