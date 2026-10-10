---
type: design
id: cotal-framework
title: "CoTAL: a three-phase framework unifying Evidence-Centered Design, human-in-the-loop prompt engineering, chain-of-thought prompting, and active learning for formative assessment scoring"
description: "CoTAL is an LLM-based approach to formative assessment scoring defined as an approach \"that(1)leveragesEvidence-CenteredDesign(ECD)toalignassessments andrubrics with curriculum goals, (2) applieshuman-in-the-looppromp..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: cohn-2026
    resource: "https://arxiv.org/abs/2504.02323"
    title: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323"
    author: "Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G"
---

# CoTAL: a three-phase framework unifying Evidence-Centered Design, human-in-the-loop prompt engineering, chain-of-thought prompting, and active learning for formative assessment scoring

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
CoTAL is an LLM-based approach to formative assessment scoring defined as an approach "that(1)leveragesEvidence-CenteredDesign(ECD)toalignassessments andrubrics with curriculum goals, (2) applieshuman-in-the-loopprompt engineering to automate responsescoring,and(3)incorporateschain-of-thought(CoT)promptingandteacherandstudent feedback to iteratively refine questions, rubrics, and LLM prompts." Phase I is human-driven assessment and rubric development; Phase II co-develops and optimizes prompts via response scoring with inter-rater reliability, prompt development with few-shot CoT exemplars, and active learning against a validation set; Phase III deploys the refined prompt in classrooms and uses teacher and student critique to refine questions, rubrics, and prompts.

## Design Implications

### Context
#### Requirements
- Human consensus scoring with Cohen's κ reaching at least 0.70 before prompt development, with disagreement 'sticking points' documented and used as few-shot exemplars
- Few-shot examples balanced across subscores, including at least one positive and one negative instance per subscore (multi-label) or one instance per score (multi-class)
#### Constraints
- The authors found the LLM tended to overfit when few-shot instances were numerous or CoT chains too granular, so they insert only a single instance during active learning
- Token limitations in GPT-4's context window prohibited active learning in the Debugging Task

### Target Learners
- K-12 STEM+C students (sixth-grade, ages 11-12 in the study)

### Learning Goals
- Formative assessment of cross-domain science, computing, and engineering understanding, including conservation of matter, computational modeling, and fair-test engineering reasoning

### Claims
- [Cotal Rules Task Qwk Gain](../claims/cotal-rules-task-qwk-gain.md) [+M]
- [Cotal Debugging Task Qwk Gain](../claims/cotal-debugging-task-qwk-gain.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Cohn, C., Ashwin T S, Mohammed, N., & Biswas, G. (2026). CoTAL: Human-in-the-Loop Prompt Engineering for Generalizable Formative Assessment Scoring and Feedback. arXiv preprint. https://arxiv.org/abs/2504.02323
