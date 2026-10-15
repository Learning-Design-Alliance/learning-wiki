---
type: research-method
id: multimodal-classroom-video-analysis-for-teacherstudent-interaction-detection
title: Multimodal classroom-video analysis for teacher–student interaction detection
description: "A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligne"
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: hur-2026
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    title: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    author: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N"
---

# Multimodal classroom-video analysis for teacher–student interaction detection

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk.

## Accounts
<!-- How each source describes or uses the method -->
- **Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video**: A computational pipeline combining three modalities from high school mathematics classroom videos: OpenPose pose estimation with Euclidean-distance tracking postprocessing and group boundary boxes, openSMILE eGeMAPS acoustic/prosodic features (88 features), and WhisperX word-level transcripts aligned to detected windows. A pose-based heuristic flags teacher–group interactions using vertical dominance and proximity with 10-second smoothing and a 10-second minimum episode length. An on-premises Mistral large language model classified transcript snippets for question-asking, confusion, need for help, and math talk. (Hur et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030

<!-- merged 2026-10-10 from elements/multimodal-teacher-group-interaction-pipeline ("Multimodal pipeline for detecting and analyzing teacher–student group interactions in classroom video"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Elements
- 

## Examples
-

## Key Sources
- Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030
-->
