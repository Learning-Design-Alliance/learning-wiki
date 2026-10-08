---
type: claim
title: Computer-led exploration set the decision boundary for what counted as an interaction, shaping which events became detectable and how interpretation proceeded
description: Computer-led exploration set the decision boundary for what counted as an interaction, shaping which events became detectable and how interpretation proceeded
id: computer-led-exploration-shaped-detectable-events
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: hur-2026
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    title: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    author: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Computer-led exploration set the decision boundary for what counted as an interaction, shaping which events became detectable and how interpretation proceeded

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`

## Subclaims
`q2 i?` In the case study, the detection tool rather than the researcher set the decision boundary for what counted as an interaction, and pose feature extraction further influenced hard decision boundaries. [→ Hur 2026](#hur-2026)

## Evidence

### Hur 2026

Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030

`q2 · i?` · `theoretical · r2`

Authors' discussion-section interpretation of their case study through the analytic agency framework, viewing the pose-based detector's vertical dominance and proximity criteria, 10s smoothing window, and 10s minimum episode length as computer-set decision boundaries, with OpenPose's pretrained keypoint assumptions also shaping what surfaced.

> "In other words, the tool, rather than t he researcher, set the decision boundary for what counted as an “interaction.” Similarly, it could be argued that some of the hard decision boundaries were also influenced by the computer, through the sheer process of pose feature extraction on the video using OpenPose."

## Discussion


## Related Claims
- [Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured](detector-recall-55-percent-visual-constraints.md) — a narrower finding that bears on this claim
- [A tool's effectiveness results from the whole configuration of events, activities, and contexts in which it is used](tool-effectiveness-depends-on-context-configuration.md) — a broader claim this one bears on
- [The pose-based detector surfaced 317 teacher–group interaction events across 21 student groups, averaging 15.10 events per group with mean duration 32.73 seconds](detector-surfaced-317-interaction-events.md) — related
- [Mixed-effects models showed significant shifts in pose keypoints emphasized by the detector before-to-during and before-to-after interactions, while no audio features changed significantly](keypoint-shifts-significant-audio-null.md) — related
