---
type: strategy
id: misconception-aware-contrastive-remediation-videos
title: Misconception-aware contrastive remediation videos triggered by incorrect quiz answers
description: "When a learner answers a quiz question incorrectly, the system generates \"a targeted explanatory video contrasting the incorrect reasoning with the correct solution\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: xinchen-ma-2026
    resource: "https://arxiv.org/abs/2609.24083"
    title: "Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian. (2026). From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning. https://arxiv.org/abs/2609.24083"
    author: Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian
---

# Misconception-aware contrastive remediation videos triggered by incorrect quiz answers

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
When a learner answers a quiz question incorrectly, the system generates "a targeted explanatory video contrasting the incorrect reasoning with the correct solution". Remediation generation is conditioned on the quiz question, candidate options, learner response, and correct answer, so feedback addresses the specific misconception. Quizzes are generated from the storyboard without reusing examples, equations, or numerical values from the video, to encourage conceptual understanding rather than memorization. Assessment results feed back into future instructional planning and scaffolded content generation.

## Design Implications

### Context
#### Requirements
- Quiz questions derived from the instructional storyboard to remain semantically aligned with the video and learning goals
- Learner response signals (question, options, incorrect answer, correct reasoning) available to condition remediation generation
#### Constraints
- Remediation is triggered by incorrect answers to storyboard-derived quiz questions; the article does not claim effectiveness beyond this interaction-level adaptation

### Target Learners
- STEM learners answering post-video formative assessment questions

### Target Learning Goals
- Correcting specific misconceptions
- Reinforcing conceptual understanding after instruction

## Related Strategies

- [Interactive Video Quizzing](interactive-video-quizzing.md)
- [Question Answering](question-answering.md)
- [Errors as Learning Opportunities](embrace_errors_as_learning_opportunities.md)
- [Remedial strategies using remedial SEMs to correct misconceptions](remedial-sem-misconception-correction.md)

## Examples
-

## Key Sources
- Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian. (2026). From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning. https://arxiv.org/abs/2609.24083
