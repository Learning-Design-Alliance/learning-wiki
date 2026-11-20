---
type: strategy
id: match-synchrony-measure-to-video-dynamics
title: Choose the gaze synchrony measure according to the dynamic nature of the learning video, and protect learner privacy when applying eye tracking in real-world settings
description: "The article recommends that future research and applications match the synchrony measure to the stimulus: for static, slide-based stimuli KLD and MultiMatch perform comparably and KLD \"might be more computationally ef..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: babette-bühler-2024
    resource: "https://arxiv.org/abs/2404.00333"
    title: "Babette Bühler, Efe Bozkir, Hannah Deininger, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. 2024. On Task and in Sync: Examining the Relationship between Gaze Synchrony and Self-Reported Attention During Video Lecture Learning. Proceedings of ACM Symposium on Eye Tracking Research & Applications (ETRA '24). https://arxiv.org/abs/2404.00333"
    author: Babette Bühler, Efe Bozkir, Hannah Deininger, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci
---

# Choose the gaze synchrony measure according to the dynamic nature of the learning video, and protect learner privacy when applying eye tracking in real-world settings

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends that future research and applications match the synchrony measure to the stimulus: for static, slide-based stimuli KLD and MultiMatch perform comparably and KLD "might be more computationally efficient, especially for group-based comparisons", while for dynamic stimuli or longer time windows MultiMatch may be preferable, and hybrid approaches such as Normalized Scanpath Saliency may combine their insights. It further stresses that real-time attention-adaptive applications must "prioritize students' privacy" through robust securing and anonymization of eye movement data, careful consent, and avoidance of biases disadvantaging learner groups.

## Design Implications

### Context
#### Requirements
- Knowledge of the dynamic nature of the video or learning task; for real-time applications, attention to computational demands and data protection measures
#### Constraints
- The article notes findings may not directly apply to live online lectures where participants are visible via webcam, and that gaze synchrony as an attention indicator is not yet robust

### Target Learners
- online learners in video lecture settings

### Target Learning Goals
- real-time assessment of learner attention to guide instructional strategies and enhance engagement

### Affordances
- [Kld Multimatch Synchrony Measures](../research-methods/kld-and-multimatch-as-complementary-gaze-synchrony-measures-for-lecture-video-attention.md)

## Claims

- [Learners who self-report as attentive show significantly higher inter-subject correlation of gaze position and pupil diameter during video lecture viewing](../claims/attentive-self-reports-higher-isc-video-lecture.md) [+W]
- [Attentive self-reports predict higher MultiMatch scanpath similarity, strongest for fixation-position similarity, but not for saccade length similarity](../claims/attentive-self-reports-higher-multimatch-similarity.md) [+W]
- [Attentive self-reports predict significantly lower Kullback-Leibler divergence between gaze density maps, indicating greater gaze synchrony](../claims/attentive-self-reports-lower-kld-gaze-synchrony.md) [+W]
- [Gaze synchrony measures (KLD and MultiMatch similarity) do not significantly predict learning outcomes, failing to replicate prior findings](../claims/gaze-synchrony-does-not-predict-learning-outcomes.md) [-W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Babette Bühler, Efe Bozkir, Hannah Deininger, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. 2024. On Task and in Sync: Examining the Relationship between Gaze Synchrony and Self-Reported Attention During Video Lecture Learning. Proceedings of ACM Symposium on Eye Tracking Research & Applications (ETRA '24). https://arxiv.org/abs/2404.00333
