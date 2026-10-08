---
type: claim
title: "Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured"
description: "Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured"
id: detector-recall-55-percent-visual-constraints
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

# Ground-truth validation found the detector identified 55% of human-coded interactions, with misses driven by visual constraints such as teachers outside boundary boxes or obscured

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across three validation videos, the human coder identified 20 interactions and the detector found 11 (55%), with missed events attributable to spatial boundaries, visual obstruction, or crouching not accounted for in the verticality heuristic. [→ Hur 2026](#hur-2026)

## Evidence

### Hur 2026

Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030

`q2 · i?` · `design · r2`

Ground-truth validation using stratified random sampling of one full video per teacher, with manual coding of sustained teacher–group interactions. The detector performed well with clear visibility (5 of 7 events for Teacher 2) but "systematically filtered out specific types of interactions".

> "the human coder identified 20 distinct interactions for the chosen group, and the detector identified 11 (55%) of these events. We analyzed the 9 missed interactions, which revealed that the detector's performance was heavily dependent on visual constraints."

## Discussion


## Related Claims
- [Computer-led exploration set the decision boundary for what counted as an interaction, shaping which events became detectable and how interpretation proceeded](computer-led-exploration-shaped-detectable-events.md) — a broader claim this one bears on
- [The pose-based detector surfaced 317 teacher–group interaction events across 21 student groups, averaging 15.10 events per group with mean duration 32.73 seconds](detector-surfaced-317-interaction-events.md) — related
- [Mixed-effects models showed significant shifts in pose keypoints emphasized by the detector before-to-during and before-to-after interactions, while no audio features changed significantly](keypoint-shifts-significant-audio-null.md) — related
