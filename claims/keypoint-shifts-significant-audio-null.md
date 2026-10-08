---
type: claim
title: Mixed-effects models showed significant shifts in pose keypoints emphasized by the detector before-to-during and before-to-after interactions, while no audio features changed significantly
description: Mixed-effects models showed significant shifts in pose keypoints emphasized by the detector before-to-during and before-to-after interactions, while no audio features changed significantly
id: keypoint-shifts-significant-audio-null
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
    kind: design
    rigour: 2
---

# Mixed-effects models showed significant shifts in pose keypoints emphasized by the detector before-to-during and before-to-after interactions, while no audio features changed significantly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In the before vs. during comparison, 11 keypoint coordinates changed significantly (e.g., nose y β = 11.13, p < .001), and five changed in the before vs. after comparison, while no audio features showed significant changes in either comparison. [→ Hur 2026](#hur-2026)

## Evidence

### Hur 2026

Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030

`q2 · i?` · `design · r2`

Linear mixed-effects models with random intercepts per group recording compared before, during, and after segments. Significant shifts occurred in head and body keypoints the detector privileged (nose, eyes, ears), e.g., nose y β = 11.13, t = 3.86, p < .001; audio features were "essentially flat across segments".

> "In the before vs. during comparison, 11 keypoint coordinates changed significantly, and five keypoint coordinates for the before vs. after comparison. No statistically significant changes were found for any of the audio features in either comparison."

## Discussion


## Related Claims
- [The pose-based detector surfaced 317 teacher–group interaction events across 21 student groups, averaging 15.10 events per group with mean duration 32.73 seconds](detector-surfaced-317-interaction-events.md) — related
- [Computer-led exploration set the decision boundary for what counted as an interaction, shaping which events became detectable and how interpretation proceeded](computer-led-exploration-shaped-detectable-events.md) — related
- [LLM-detected confusion in student dialogue decreased after teacher–group interactions (β = −0.061, p = .049)](confusion-decreased-after-interactions.md) — related
- [Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured](detector-recall-55-percent-visual-constraints.md) — related
