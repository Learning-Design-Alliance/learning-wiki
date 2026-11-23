---
type: claim
title: "A trained chaos neural network correctly judged 79% of unseen surgeons as expert or novice from hand-motion parameters"
description: "A trained chaos neural network correctly judged 79% of unseen surgeons as expert or novice from hand-motion parameters"
id: ai-hand-motion-classifies-surgeon-expertise-79-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: uemura-munenori-2018
    resource: "https://doi.org/10.1155/2018/9873273"
    title: "Uemura Munenori, Tomikawa Morimasa, Miao Tiejun, Souzaki Ryota, Ieiri Satoshi, Akahoshi Tomohiko, Lefor Alan K., Hashizume Makoto. (2018). Feasibility of an AI-Based Measure of the Hand Motions of Expert and Novice Surgeons. Computational and Mathematical Methods in Medicine. https://doi.org/10.1155/2018/9873273"
    author: Uemura Munenori, Tomikawa Morimasa, Miao Tiejun, Souzaki Ryota, Ieiri Satoshi, Akahoshi Tomohiko, Lefor Alan K., Hashizume Makoto
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A trained chaos neural network correctly judged 79% of unseen surgeons as expert or novice from hand-motion parameters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a validation study with 29 surgeons whose skill level was unknown to the system, the AI system distinguished expert from novice surgeons with a correct judgment rate of 79%, with no human intervention during classification. [→ Uemura Munenori 2018](#uemura-munenori-2018)

## Evidence

### Uemura Munenori 2018

Uemura Munenori, Tomikawa Morimasa, Miao Tiejun, Souzaki Ryota, Ieiri Satoshi, Akahoshi Tomohiko, Lefor Alan K., Hashizume Makoto. (2018). Feasibility of an AI-Based Measure of the Hand Motions of Expert and Novice Surgeons. Computational and Mathematical Methods in Medicine. https://doi.org/10.1155/2018/9873273

`q2 · i?` · `design · r2`

Validation study (study 2): input factors from 29 participants (expert group 12, novice group 17) were entered into the optimized network; correct classification was the primary outcome. The article reports "a correct judgment rate of 79%"; no effect size or test statistic is printed.

> "The AI system had a correct judgment rate of 79% for distinguishing between expert and novice surgeons. Figure 3 shows the output of the neural network."

## Discussion


## Related Claims
- Machine-learning optimization of the network reached a correct judgment ratio of 0.99 on the training dataset by the seventh trial — related
- [In the narrative synthesis, deep learning models classify surgeon skill levels from kinematic data with accuracy up to 95.4%](deep-learning-skill-classification-up-to-95-percent.md) — a broader claim this one bears on
- [The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance](skill-assessment-network-56-percent-accuracy-failed.md) — related
- [Deep learning models trained on JIGSAWS kinematic and video data achieve high accuracy in predicting surgeon skill level and mOSATS scores](deep-learning-high-accuracy-skill-prediction-jigsaws.md) — related
