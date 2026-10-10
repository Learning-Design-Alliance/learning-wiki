---
type: design
id: ai-driven-tutor-training-assessment-system
title: AI-driven tutor training and real-life assessment system linking scenario-based lessons to transcript-based evaluation
description: "The article introduces a pipeline that trains tutors on research-supported \"tutor moves\" via immersive scenario-based lessons, then uses generative AI (Gemini-2.5-pro) to evaluate real-life application in tutoring tra..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: thomas-2026
    resource: "https://arxiv.org/abs/2606.18617"
    title: "Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R. (2026). AI-Driven Assessment of Human Tutors: Linking Training Performance to Real-Life Practice. https://arxiv.org/abs/2606.18617"
    author: "Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R"
---

# AI-driven tutor training and real-life assessment system linking scenario-based lessons to transcript-based evaluation

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article introduces a pipeline that trains tutors on research-supported "tutor moves" via immersive scenario-based lessons, then uses generative AI (Gemini-2.5-pro) to evaluate real-life application in tutoring transcriptions. A two-stage prompting strategy first uses "an 'opportunity prompt' identified relevant moments where a tutor move was applicable (0/1)" and then "an 'evaluation prompt' scored the quality of the tutor action" (0-ineffective, 1-effective). The system maps three validity types to stages: content validity via expert judgment, predictive validity via training-to-transcript correlation, and construct validity via AI scoring accuracy. If proficiency is not met, a remediation loop of self-reflection or lesson retake is triggered.

## Design Implications

### Context
#### Requirements
- LLM prompts derived from expert-validated human scoring rubrics, with documented inter-rater reliability procedures
- Transcripts of authentic tutoring sessions (audio processed via Whisper and merged with chat logs)
#### Constraints
- The article states LLM prompts require continuous auditing given the wide range of IRR scores
- Manual session uploads may introduce selection bias where more confident tutors submitted more data

### Target Learners
- undergraduate volunteer and paraprofessional math tutors tutoring middle school students remotely

### Learning Goals
- pedagogical tutor moves such as praising, reacting to errors, determining what students know, affirming correct attempts, guiding thinking, and prompting explanation

### Claims
- [Training Performance Predicts Transcript Scores 025Sd](../claims/training-performance-predicts-transcript-scores-025sd.md) [+M]
- [Post Training Opportunity And Execution Gains](../claims/post-training-opportunity-and-execution-gains.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R. (2026). AI-Driven Assessment of Human Tutors: Linking Training Performance to Real-Life Practice. https://arxiv.org/abs/2606.18617
