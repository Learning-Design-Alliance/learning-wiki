---
type: design
id: sensor-embedded-bongo-drum-platform-dtw
title: Sensor-embedded bongo drum platform with DTW-based synchronization measurement
description: "A custom bongo drum platform embedded with thin-film pressure sensors was used to measure preschoolers' tapping."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: yunhee-kim-2026
    resource: "https://doi.org/10.1038/s41539-026-00443-5"
    title: "Yunhee Kim, Doyeon Chae, Jaehwan Jang, Kyeong Taek Oh, Byeong-Sun Park & Min-gu Kim. (2026). Does tapping in sync reflect cognitive control? Links between sensorimotor synchronization, social context, and executive function in early childhood. npj Science of Learning. https://doi.org/10.1038/s41539-026-00443-5"
    author: "Yunhee Kim, Doyeon Chae, Jaehwan Jang, Kyeong Taek Oh, Byeong-Sun Park & Min-gu Kim"
---

# Sensor-embedded bongo drum platform with DTW-based synchronization measurement

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A custom bongo drum platform embedded with thin-film pressure sensors was used to measure preschoolers' tapping. The article states this "intuitive and child-friendly interface facilitated consistent participation among young children and ensured reliable measurement across conditions". Synchronization was quantified with the Dynamic Time Warping (DTW) algorithm, which "flexibly compar[es] the overall flow and shape of the sequences", making it robust to occasional missed strikes unlike strict onset-to-onset asynchrony measures.

## Design Implications

### Context
#### Requirements
- Requires pressure-sensor bongo drums recording strike data in real time and DTW analysis of tapping sequences against reference rhythms.
#### Constraints
- Hand dominance was not directly assessed; data and code are available only upon request from the corresponding author because public repository consent was not obtained.
- The study's design and analysis were not preregistered.

### Target Learners
- Children aged 4-5 years in preschool settings

### Learning Goals
- Sensorimotor synchronization to rhythmic stimuli

### Claims
- [Social Scaffolding Sms Smt Aligned Contexts](../claims/social-scaffolding-sms-smt-aligned-contexts.md) [+M]
- [Slow Solo Tapping Executive Function Link](../claims/slow-solo-tapping-executive-function-link.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yunhee Kim, Doyeon Chae, Jaehwan Jang, Kyeong Taek Oh, Byeong-Sun Park & Min-gu Kim. (2026). Does tapping in sync reflect cognitive control? Links between sensorimotor synchronization, social context, and executive function in early childhood. npj Science of Learning. https://doi.org/10.1038/s41539-026-00443-5
