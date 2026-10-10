---
type: strategy
id: variant-problem-probe-the-gap-follow-ups
title: Generate targeted diagnostic follow-up questions using variant-problem and probe-the-gap strategies for ambiguous cases
description: For correct-answer cases the model routes to needs-clarification, the system generates a targeted diagnostic follow-up question using either a variant-problem strategy, presenting a near-transfer problem where the sus...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
---

# Generate targeted diagnostic follow-up questions using variant-problem and probe-the-gap strategies for ambiguous cases

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For correct-answer cases the model routes to needs-clarification, the system generates a targeted diagnostic follow-up question using either a variant-problem strategy, presenting a near-transfer problem where the suspected misconception would produce the wrong answer, or a probe-the-gap strategy, asking about the specific step the student omitted. The paper notes that in autonomous tutor mode, "asking a student to explain their reasoning is good formative practice regardless of whether a misconception is present", making false positives pedagogically benign while false negatives leave misconceptions unchallenged.

## Design Implications

### Context
#### Requirements
- A reasoning-capable LLM generating the follow-up question and a routed ambiguous case from the graduated assessment
#### Constraints
- The proof of concept generated follow-up questions for 7 TM instances from the test set; no student responses to these questions have been collected, and a classroom trial would be needed to validate the pipeline

### Target Learners
- school mathematics students whose explanations are too brief to diagnose

### Target Learning Goals
- eliciting evidence of student reasoning through formative follow-up questioning

## Related Strategies

- [Probing Questions](probing_questions.md)

## Examples
-

## Key Sources
- Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143
