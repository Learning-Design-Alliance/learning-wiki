---
type: element
id: multimodal-teacher-group-interaction-pipeline
title: Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video
description: "A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS a..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: hur-2026
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    title: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    author: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N"
---

# Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk.

## Design Implications

### Context
#### Requirements
- Videos with sufficient visibility of target groups; group-level audio recorders placed at table centers; groups of at least three students mostly unobscured and discrete from other groups
#### Constraints
- The detector's heuristic assumes teachers stand while students sit; it systematically missed interactions where the teacher stood outside the group boundary box or was visually obscured or crouching

### Target Learners
- High school mathematics students in small groups (data context); education researchers as pipeline users

### Target Learning Goals
- Detecting and analyzing teacher–student group interactions to understand responsive pedagogy

### Affordances
- [Analytic Agency Framework Three Stages](../theories/analytic-agency-framework-three-stages.md)

## Claims

- [Computer-led exploration set the decision boundary for what counted as an interaction, shaping which events became detectable and how interpretation proceeded](../claims/computer-led-exploration-shaped-detectable-events.md) [+W]
- [LLM-detected confusion in student dialogue decreased after teacher–group interactions (β = −0.061, p = .049)](../claims/confusion-decreased-after-interactions.md) [+W]
- [Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured](../claims/detector-recall-55-percent-visual-constraints.md) [~W]
- [The pose-based detector surfaced 317 teacher–group interaction events across 21 student groups, averaging 15.10 events per group with mean duration 32.73 seconds](../claims/detector-surfaced-317-interaction-events.md) [+W]
- [Qualitative coding of detected clips found students most often gazed at task materials (47.6%), overt help-seeking was nearly absent (1.6%), and the teacher was present in 49.2% of segments](../claims/gaze-coding-detected-clips.md) [+W]
- [Mixed-effects models showed significant shifts in pose keypoints emphasized by the detector before-to-during and before-to-after interactions, while no audio features changed significantly](../claims/keypoint-shifts-significant-audio-null.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030
