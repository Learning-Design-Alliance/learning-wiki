---
type: design
id: tasd-teacher-authored-prompt-orchestration
title: "TASD: teacher-authored prompt layers as orchestration levers for configuring student-AI dialogue"
description: TASD (Colleague AI Classroom Teaching Aide) frames student-AI interaction as a configurable classroom routine rather than an autonomous tutor.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: alex-liu-2026
    resource: "https://arxiv.org/abs/2604.16738"
    title: "Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738"
    author: Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He
---

# TASD: teacher-authored prompt layers as orchestration levers for configuring student-AI dialogue

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
TASD (Colleague AI Classroom Teaching Aide) frames student-AI interaction as a configurable classroom routine rather than an autonomous tutor. It uses a three-layer structure: a foundational LLM, a researcher-designed system-level prompt, and a top layer of teacher-authored prompts encoding local goals, plus a student-facing opening instruction. The article treats teacher prompts as "interaction design artifacts" that specify what students work on, how the AI structures participation, and what boundaries preserve responsible use, positioning teacher-authored prompt layers as levers translating pedagogical intent into structured dialogue.

## Design Implications

### Context
#### Requirements
- Teachers must author both an AI-facing shared prompting layer and a student-facing opening instruction to launch the activity
#### Constraints
- The article notes the need for additional supports to reliably sustain higher-order reasoning during enactment, given the persistent DOK under-targeting gap

### Target Learners
- K-12 middle school (grades 6–8) and high school (grades 9–12) students across mathematics, science, ELA, social studies, world languages, and CTE

### Learning Goals
- Task-aligned classroom discussion
- higher-order thinking and cognitive demand realization
- responsible AI use

### Claims
- [Teacher Prompts Keep Conversations On Track](../claims/teacher-prompts-keep-conversations-on-track.md) [+M]
- [Dok Under Targeting Gap Ai Dialogue](../claims/dok-under-targeting-gap-ai-dialogue.md) [~M]
- [No Direct Answers Guardrail Reduces Ai Answers](../claims/no-direct-answers-guardrail-reduces-ai-answers.md) [+M]

## Related Designs

- [Teacher Interaction Layer: a web-based configuration surface for pedagogical intent, persona, and role](elevate-teacher-interaction-layer.md)

## Examples
-

## Key Sources
- Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738
