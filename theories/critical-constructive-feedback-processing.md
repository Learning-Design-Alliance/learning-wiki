---
type: theory
title: Critical Constructive Feedback Processing
description: A five-stage information-processing model of what has to happen — noticing, decoding, making sense, acting upon, and making progress — for feedback on a wrong answer to actually change performance, treating "feedback neglect" as a measurable drop-out at any stage rather than a single yes/no outcome.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
sources:
  - id: tarning-et-al-2020
    resource: "https://doi.org/10.1080/10508406.2020.1770092"
    title: "Tärning, B., Lee, Y. J., Andersson, R., Månsson, K., Gulz, A., & Haake, M. (2020). Assessing the black box of feedback neglect in a digital educational game for elementary school. Journal of the Learning Sciences, 29(4-5), 511-549."
    author: "Tärning, B., Lee, Y. J., Andersson, R., Månsson, K., Gulz, A., & Haake, M."
---

# Critical Constructive Feedback Processing

> **Theory** · [All theories](index.md)

## Description
Critical constructive feedback (CCF) is feedback given after a wrong or suboptimal answer that both signals the error and offers a way to correct it. This theory treats "did the student use the feedback?" not as one question but as five sequential, independently measurable stages a piece of feedback must survive: **noticing** (attention reaches the feedback), **decoding** (the text is actually read, not just glanced at), **making sense** (the meaning is understood), **acting upon** (the student follows the feedback's guidance), and **making progress** (the action produces real improvement on a later attempt). Framing feedback processing this way turns "feedback neglect" from a single failure mode into a diagnosable pipeline, where a design fix aimed at one stage (e.g., making feedback more noticeable) can succeed at that stage while leaving downstream stages untouched. The model draws on established error-handling stages from human-computer interaction (Nielsen 1994; Norman 1988) and on social-cueing and persona-effect research to motivate why an embodied, gazing pedagogical agent — rather than a generic visual cue like an arrow — can move a student through the earliest stages.

## Implications

### Context
- Applies to digital learning environments where feedback is delivered in-context after an error (e.g., an in-game teachable agent, a worked hint), not to summative or end-of-unit feedback
- Requires instrumentation (eye-tracking, interaction logs) to actually distinguish the stages in research; in ordinary classroom design, the stages instead function as a checklist of separate places a well-intentioned feedback design can fail
- Making-sense is the hardest stage to instrument directly and is often inferred rather than independently measured

### Target Learners
- Elementary-age students working independently in digital learning environments, where a teacher is not present to notice and repair feedback neglect in real time

### Target Learning Objectives
- Diagnosing where, specifically, a feedback design is failing (attention, comprehension, follow-through, or actual skill correction) rather than only measuring whether performance improved overall

## Claims
- [Critical constructive feedback is neglected at multiple, independently measurable processing stages](../claims/critical-constructive-feedback-is-neglected-at-multiple-stages.md) [~M]

## Related Theories
- [Self-Regulated Learning](self-regulated-learning.md) — acting upon feedback and monitoring progress overlap with SRL's monitoring and control phases, but this theory decomposes the pre-monitoring attentional and comprehension steps that SRL treats as already given

## Examples
- [Pedagogical Agent Signaling for Feedback Salience](../elements/pedagogical-agent-signaling.md) — a design element aimed specifically at the noticing and decoding stages of this model

## Key Sources
- Tärning, B., Lee, Y. J., Andersson, R., Månsson, K., Gulz, A., & Haake, M. (2020). Assessing the black box of feedback neglect in a digital educational game for elementary school. *Journal of the Learning Sciences, 29*(4-5), 511-549. [https://doi.org/10.1080/10508406.2020.1770092](https://doi.org/10.1080/10508406.2020.1770092)
- Nielsen, J. (1994). *Usability Engineering*. Morgan Kaufmann.
- Mayer, R. E., & DaPra, C. S. (2012). An embodiment effect in computer-based learning with animated pedagogical agents. *Journal of Experimental Psychology: Applied, 18*(3), 239-252.
