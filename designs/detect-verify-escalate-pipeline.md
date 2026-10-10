---
type: design
id: detect-verify-escalate-pipeline
title: Detect-verify-escalate pipeline with four pedagogically distinct routes
description: "The pipeline routes each student submission through an answer-key check and, for correct-answer cases, an LLM graduated assessment producing four routes: Red (wrong answer, automated correction), Green (clear reasonin..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
---

# Detect-verify-escalate pipeline with four pedagogically distinct routes

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The pipeline routes each student submission through an answer-key check and, for correct-answer cases, an LLM graduated assessment producing four routes: Red (wrong answer, automated correction), Green (clear reasoning, no action), Amber-1 (unclear reasoning, automated diagnostic follow-up question), and Amber-2 (misconception detected, verification then teacher escalation). Figure 1 shows approximate volumes per 1,000 submissions: 736 LLM calls and 64 teacher reviews. The design responds to the paper's findings that fine-tuned models cannot assess method validity and that precision is too low for direct teacher escalation.

## Design Implications

### Context
#### Requirements
- Reasoning-capable model, graduated output preserving the routing signal, and intermediate verification before teacher escalation
#### Constraints
- All findings come from 15 mathematics questions on one platform, with TM concentrated in 2 items; the diagnostic follow-up proof of concept generated questions for 7 TM instances with no student responses collected

### Target Learners
- school mathematics students and their teachers

### Learning Goals
- routing automated feedback according to reasoning validity and diagnostic certainty

### Claims
- [Reasoning Model Detection False Alarm Tradeoff](../claims/reasoning-model-detection-false-alarm-tradeoff.md) [+M]
- [Fine Tuned Classifiers Miss Correct Answer Misconceptions](../claims/fine-tuned-classifiers-miss-correct-answer-misconceptions.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143
