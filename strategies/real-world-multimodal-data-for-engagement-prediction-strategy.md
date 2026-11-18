---
type: strategy
id: real-world-multimodal-data-for-engagement-prediction-strategy
title: Use real-world multimodal datasets to predict student engagement and improve adaptive learning selection
description: The authors propose analyzing real-world student learning activities, facial expressions, and brainwave patterns to predict engagement, which can then feed back into adaptive learning selection and outcomes.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: fangli-xu-2019
    resource: "https://arxiv.org/abs/1910.06078"
    title: "Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong. (2019). MUTLA: A Large-Scale Dataset for Multimodal Teaching and Learning Analytics. https://arxiv.org/abs/1910.06078"
    author: Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong
---

# Use real-world multimodal datasets to predict student engagement and improve adaptive learning selection

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The authors propose analyzing real-world student learning activities, facial expressions, and brainwave patterns to predict engagement, which can then feed back into adaptive learning selection and outcomes. They emphasize that the dataset was "gathered from the real-world educational activities versus those from a controlled lab environment" to benefit the educational learning community. As future work, they state they "will try to apply machine learning and deep learning techniques ourselves to this multimodal data".

## Design Implications

### Context
#### Requirements
- Requires time-synchronized multimodal records (logs, video, EEG) from authentic learning sessions so that engagement-related signals can be linked to learning actions
#### Constraints
- The engagement-prediction use is a stated aim and future direction; the paper reports no engagement prediction results yet

### Target Learners
- K-12 students using adaptive learning systems

### Target Learning Goals
- improving student engagement and adaptive learning selection

## Claims

- [The MUTLA dataset covers 156 students from two SAIL after-school centers in China working across 6 subjects](../claims/mutla-156-students-two-centers-six-subjects.md) [+W]
- [After filtering, the MUTLA video data contain 2170 question segments, with 61.54% having valid face tracking for at least 50% of frames and 18.30% fully tracked](../claims/mutla-2170-segments-valid-tracking-percentages.md) [+W]

## Related Strategies

- [Two-step synchronization procedure aligning brainwave and video data to question-level user records via user id, session time, and submission timestamps](mutla-two-step-multimodal-synchronization-strategy.md)

## Examples
-

## Key Sources
- Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong. (2019). MUTLA: A Large-Scale Dataset for Multimodal Teaching and Learning Analytics. https://arxiv.org/abs/1910.06078
