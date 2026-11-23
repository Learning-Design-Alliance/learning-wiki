---
type: strategy
id: ai-feedback-prototype-strengths-weaknesses
title: Prototype AI feedback system showing surgeons their skill strengths and weaknesses quantitatively
description: Based on the study, the authors developed a prototype AI model with a new concept (Figure 4) that displays skill assessment results quantitatively with a bar graph.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: uemura-munenori-2018
    resource: "https://doi.org/10.1155/2018/9873273"
    title: "Uemura Munenori, Tomikawa Morimasa, Miao Tiejun, Souzaki Ryota, Ieiri Satoshi, Akahoshi Tomohiko, Lefor Alan K., Hashizume Makoto. (2018). Feasibility of an AI-Based Measure of the Hand Motions of Expert and Novice Surgeons. Computational and Mathematical Methods in Medicine. https://doi.org/10.1155/2018/9873273"
    author: Uemura Munenori, Tomikawa Morimasa, Miao Tiejun, Souzaki Ryota, Ieiri Satoshi, Akahoshi Tomohiko, Lefor Alan K., Hashizume Makoto
---

# Prototype AI feedback system showing surgeons their skill strengths and weaknesses quantitatively

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Based on the study, the authors developed a prototype AI model with a new concept (Figure 4) that displays skill assessment results quantitatively with a bar graph. It compares a surgeon's hand-motion features, calculated by unstable periodic orbit analysis, against features of average experts' hand motions, yielding a resemblance ratio, and shows three fluctuation items from detrended fluctuation analysis (stability of COG, flexibility of maneuver, two-handed coordination) against an orange zone marking the proper amount of fluctuation calculated by averaging experts' results. "The program aims to clarify surgeons' skills in terms of what they have or have not mastered and their strengths and weaknesses, and the system provides feedback to surgeons to improve their skills, specifically and quantitatively."

## Design Implications

### Context
#### Requirements
- Expert-group data averaged to define the resemblance-ratio reference and the proper fluctuation zones
#### Constraints
- The authors describe this as a prototype and plan further development for higher classification accuracy; the article does not report testing of the prototype's feedback on learners

### Target Learners
- surgeons in training and education for laparoscopic surgery

### Target Learning Goals
- identifying mastered and unmastered surgical skills
- targeted improvement of surgical hand motions

## Claims

- [A trained chaos neural network correctly judged 79% of unseen surgeons as expert or novice from hand-motion parameters](../claims/ai-hand-motion-classifies-surgeon-expertise-79-percent.md) [+W]

## Related Strategies

- [Real-time fluctuation-index monitoring with a 1.4 cutoff for perioperative skill feedback](realtime-beta-monitoring-perioperative-feedback.md)
- [Use video-based, system-independent suture metrics to deliver intraoperative feedback in surgical training](vision-based-intraoperative-suture-feedback-strategy.md)

## Examples
-

## Key Sources
- Uemura Munenori, Tomikawa Morimasa, Miao Tiejun, Souzaki Ryota, Ieiri Satoshi, Akahoshi Tomohiko, Lefor Alan K., Hashizume Makoto. (2018). Feasibility of an AI-Based Measure of the Hand Motions of Expert and Novice Surgeons. Computational and Mathematical Methods in Medicine. https://doi.org/10.1155/2018/9873273
