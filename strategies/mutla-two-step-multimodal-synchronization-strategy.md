---
type: strategy
id: mutla-two-step-multimodal-synchronization-strategy
title: Two-step synchronization procedure aligning brainwave and video data to question-level user records via user id, session time, and submission timestamps
description: The paper describes a replicable procedure for aligning multimodal streams.
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

# Two-step synchronization procedure aligning brainwave and video data to question-level user records via user id, session time, and submission timestamps

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The paper describes a replicable procedure for aligning multimodal streams. Step one matches each student to their brainwave data using student user id, session time, and headset number; step two synchronizes brainwave data with the user record using an algorithm that assigns brainwave file paths to question items whose submission time (ctime) falls between class start and end times. The same algorithm syncs webcam video, after which "the data were segmented from each session into time phases representing the start and end of each question the student worked on".

## Design Implications

### Context
#### Requirements
- Requires user records with per-question ctime submission timestamps, class start and end times, and brainwave files with Unix timestamps converted to Beijing time for synchronization
#### Constraints
- Timestamps required conversion to Beijing time because data collection occurred in China, and the device event file records whether the headset was connected at each time point

### Target Learners
- students in after-school tutoring sessions using the SAIL system

### Target Learning Goals
- multimodal analytics of question-level learning behavior

## Related Strategies

- [Use real-world multimodal datasets to predict student engagement and improve adaptive learning selection](real-world-multimodal-data-for-engagement-prediction-strategy.md)

## Examples
-

## Key Sources
- Fangli Xu, Lingfei Wu, KP Thai, Carol Hsu, Wei Wang, Richard Tong. (2019). MUTLA: A Large-Scale Dataset for Multimodal Teaching and Learning Analytics. https://arxiv.org/abs/1910.06078
