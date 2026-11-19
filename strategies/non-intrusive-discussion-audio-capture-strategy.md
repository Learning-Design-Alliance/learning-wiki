---
type: strategy
id: non-intrusive-discussion-audio-capture-strategy
title: Non-intrusive multi-recorder audio capture with similarity-based lecture/discussion separation for flipped classroom learning analytics
description: "The article demonstrates a capture strategy: small TASCAM DR-05 recorders are placed non-intrusively for each student group, adjacent recorders at least 1.5 meters apart, sampling at 44.1 kHZ."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: hang-su-2023
    resource: "https://arxiv.org/abs/2301.12399"
    title: "Hang Su, Borislav Dzodzo, Changlun Li, Danyang Zhao, Hao Geng, Yunxiang Li, Sidharth Jaggi, and Helen Meng. (2023). Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom. https://arxiv.org/abs/2301.12399"
    author: Hang Su, Borislav Dzodzo, Changlun Li, Danyang Zhao, Hao Geng, Yunxiang Li, Sidharth Jaggi, and Helen Meng
---

# Non-intrusive multi-recorder audio capture with similarity-based lecture/discussion separation for flipped classroom learning analytics

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article demonstrates a capture strategy: small TASCAM DR-05 recorders are placed non-intrusively for each student group, adjacent recorders at least 1.5 meters apart, sampling at 44.1 kHZ. Because lectures have high similarity across simultaneous recordings, recordings are synchronized by FFT convolution and windows are classified as lecture or discussion by normalized similarity histograms, eliminating broadcasted information so only discussion speech is analyzed.

## Design Implications

### Context
#### Requirements
- simultaneous recordings from multiple devices placed around the classroom, coarsely synchronized to a common start time
- consent from students, with the option to stop recording at any time
#### Constraints
- applied in one laboratory-style classroom with fixed groups of 3-4 members seated together; manual transcription was still required for the code-switched speech

### Target Learners
- student groups in a flipped classroom

### Target Learning Goals
- collecting group discussion dialog data for learning analytics on group learning processes and outcomes

## Claims

- [Machine learning on discussion-dialog indicators predicts group learning outcome as High, Mid, or Low with best accuracy of 78.9%](../claims/ml-prediction-group-outcome-78-9-percent.md) [+W]
- [Negative sentiment words are significantly greater in low learning outcome groups, and positive sentiment indicators higher in high learning outcome groups](../claims/sentiment-indicators-group-learning-outcome.md) [+W]
- [Topic relevance of group discussions is positively correlated with group learning outcome in the flipped classroom](../claims/topic-relevance-correlates-with-group-outcome.md) [+W]
- [Information exchange (number of dialog turns) and context cohesion are correlated with group learning outcome](../claims/turns-and-cohesion-group-outcome.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Hang Su, Borislav Dzodzo, Changlun Li, Danyang Zhao, Hao Geng, Yunxiang Li, Sidharth Jaggi, and Helen Meng. (2023). Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom. https://arxiv.org/abs/2301.12399
