---
type: strategy
id: phase-specific-adaptivity-strategy
title: "Phase-specific adaptivity: strong AI guidance during critical procedural phases and lighter guidance during open-ended exploration"
description: "The article's third design recommendation is to vary adaptivity intensity across task phases."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: ka-hei-carrie-lau-2024
    resource: "https://arxiv.org/abs/2411.18438"
    title: "Ka Hei Carrie Lau, Sema Sen, Philipp Stark, Efe Bozkir, and Enkelejda Kasneci. (2024). Adaptive Gen-AI Guidance in Virtual Reality: A Multimodal Exploration of Engagement in Neapolitan Pizza-Making. arXiv. https://arxiv.org/abs/2411.18438"
    author: Ka Hei Carrie Lau, Sema Sen, Philipp Stark, Efe Bozkir, and Enkelejda Kasneci
---

# Phase-specific adaptivity: strong AI guidance during critical procedural phases and lighter guidance during open-ended exploration

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article's third design recommendation is to vary adaptivity intensity across task phases. "Procedural learning alternates between structured steps, requiring explicit guidance, and open-ended exploration, benefiting from greater autonomy." The authors recommend "dynamically varying adaptivity intensity: strong guidance during critical procedural phases (e.g., dough preparation) and lighter, more suggestive guidance during exploratory activities (e.g., ingredient selection)." A second recommendation is to leverage multimodal behavioural cues: eye-tracking and head-movement data can indicate confusion or loss of focus, and systems should integrate real-time multimodal triggers such as extended off-target gaze or rapid head movements to provide targeted assistance.

## Design Implications

### Context
#### Requirements
- Real-time multimodal triggers (e.g., extended off-target gaze or rapid head movements) to detect when learners need support
- Identification of which task phases are critical procedural steps versus open-ended exploration
#### Constraints
- The current prototype implements these recommendations in a simplified manner
- Participants reported insufficient interaction time with auxiliary cultural materials due to frequent interruptions from tutor dialogue

### Target Learners
- Adult learners using adaptive AI tutors in VR procedural learning environments

### Target Learning Goals
- Effective guidance during structured procedural steps while preserving autonomy during exploratory activities

## Claims

- [Moderate adaptivity, but not high adaptivity, significantly increases visual attention to the AI tutor avatar relative to a non-adaptive baseline](../claims/moderate-adaptivity-increases-avatar-dwell-time.md) [~W]
- [Moderate adaptivity significantly reduces exploratory head movement compared with a non-adaptive baseline](../claims/moderate-adaptivity-reduces-head-movement.md) [~W]

## Related Strategies

- [Discourage mental offloading to AI by balancing guidance depth and frequency with application opportunities](discourage-mental-offloading-balance-guidance-application.md)
- [Balance structure and open-endedness by scaffolding agency with modeling, coaching, and fading support](scaffold-agency-modeling-coaching-fading.md)
- [Adapt open-endedness to learner skill level and scaffold exploration with graduated guidance](adapt-open-endedness-to-skill-level.md)
- [Guided Inquiry](guided_inquiry.md)

## Examples
-

## Key Sources
- Ka Hei Carrie Lau, Sema Sen, Philipp Stark, Efe Bozkir, and Enkelejda Kasneci. (2024). Adaptive Gen-AI Guidance in Virtual Reality: A Multimodal Exploration of Engagement in Neapolitan Pizza-Making. arXiv. https://arxiv.org/abs/2411.18438
