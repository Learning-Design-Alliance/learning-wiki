---
type: strategy
id: attention-aware-post-lecture-quiz-strategy
title: Generate post-lecture quiz questions targeting the lecture sections where individual learners paid least attention
description: The strategy converts eye-tracking attention metrics collected during a VR lecture into personalized post-lecture quizzes on a mobile assistant.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: shi-liu-2026
    resource: "https://doi.org/10.1145/3772318.3790667"
    title: "Shi Liu, Martin Feick, Linus Bierhoff, and Alexander Maedche. 2026. AttentiveLearn: Personalized Post-Lecture Support for Gaze-Aware Immersive Learning. In Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). ACM, New York, NY, USA. https://doi.org/10.1145/3772318.3790667"
    author: Shi Liu, Martin Feick, Linus Bierhoff, and Alexander Maedche
---

# Generate post-lecture quiz questions targeting the lecture sections where individual learners paid least attention

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 2 studies (2 causal), `q2` · 2 of 2 report an effect size · 3 claims rest on one study

## Description
The strategy converts eye-tracking attention metrics collected during a VR lecture into personalized post-lecture quizzes on a mobile assistant. "LectureQuiz provides learners with LLM-generated questions focusing on sections with low AOI coverage and ADI", delivering the quizzes immediately after the lecture and before the subsequent lecture, following the principle of test-enhanced learning. This moves attention-aware support out of the lecture, avoiding in-lecture interventions that participants described as disruptive.

## Design Implications

### Context
#### Requirements
- In-lecture gaze data must be processed into section-level attention metrics and transferred to the mobile assistant after the lecture
#### Constraints
- Participants reported that in-lecture attention support such as warnings would have been disruptive, so personalization is delivered only post-lecture

### Target Learners
- university students in lecture-based courses

### Target Learning Goals
- reviewing and reinforcing lecture content where attention lapsed

## Claims

- [Attentive-group participants rated attention-aware LectureQuiz as significantly more accurate at revealing attention gaps than non-attentive participants, and perceived accuracy correlated negatively with section-level ADI only in the attentive group](../claims/attentive-quiz-perceived-accuracy-higher.md) [+M]
- [LectureQuiz scores did not differ significantly between the attentive and non-attentive groups across the three weeks](../claims/lecturequiz-scores-no-group-difference.md) [-W]
- [Exploratory evidence suggests low-attention learners in the attentive group showed a greater ADI increase from week 1 to week 3 than non-attentive counterparts, but the difference was not statistically significant](../claims/low-attention-adi-increase-not-significant.md) [+W]
- [Learners' attention distribution index in VR lectures changed over weeks, with a significant increase from week 2 to week 3, but did not differ between attentive and non-attentive support groups](../claims/adi-changed-over-weeks-no-group-effect.md) [+W]

## Related Strategies

- Attentivelearn Learning Ecosystem
- [Interactive Video Quizzing](interactive-video-quizzing.md)

## Examples
-

## Key Sources
- Shi Liu, Martin Feick, Linus Bierhoff, and Alexander Maedche. 2026. AttentiveLearn: Personalized Post-Lecture Support for Gaze-Aware Immersive Learning. In Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). ACM, New York, NY, USA. https://doi.org/10.1145/3772318.3790667
