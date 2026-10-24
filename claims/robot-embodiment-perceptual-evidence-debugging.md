---
type: claim
title: "Robot embodiment changes verification and debugging: learners treat robot execution as perceptual evidence for hypothesis-driven revisions, while AI-Only learners rely on generic help-seeking"
description: "Robot embodiment changes verification and debugging: learners treat robot execution as perceptual evidence for hypothesis-driven revisions, while AI-Only learners rely on generic help-seeking"
id: robot-embodiment-perceptual-evidence-debugging
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-20
sources:
  - id: leyi-li-2026
    resource: "https://doi.org/10.1145/3800645.3813071"
    title: "Leyi Li, Chenyu Du, Jiafei Sun, Erick Purwanto, and Qing Zhang. (2026). RoboBlockly Studio: Conversational Block Programming with Embodied Robot Feedback for Computational Thinking. Designing Interactive Systems Conference (DIS '26). https://doi.org/10.1145/3800645.3813071"
    author: Leyi Li, Chenyu Du, Jiafei Sun, Erick Purwanto, and Qing Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: leyi-li-2026-2
    resource: "https://doi.org/10.1145/3800645.3813071"
    title: "Leyi Li, Chenyu Du, Jiafei Sun, Erick Purwanto, and Qing Zhang. (2026). RoboBlockly Studio: Conversational Block Programming with Embodied Robot Feedback for Computational Thinking. Designing Interactive Systems Conference (DIS '26). https://doi.org/10.1145/3800645.3813071"
    author: Leyi Li, Chenyu Du, Jiafei Sun, Erick Purwanto, and Qing Zhang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Robot embodiment changes verification and debugging: learners treat robot execution as perceptual evidence for hypothesis-driven revisions, while AI-Only learners rely on generic help-seeking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person

## Subclaims
`q2 i?` In the AI+Robot condition, participants initiated robot execution early and used the robot's motion as a concrete trace to localize failures and ask the AI about specific steps. [→ Leyi Li 2026](#leyi-li-2026)
`q2 i?` In the AI-Only condition, help-seeking sometimes became generic and repetitive, and several students progressed with partially incorrect reasoning without a perceptual signal prompting revision. [→ Leyi Li 2026 (2)](#leyi-li-2026-2)

## Evidence

### Leyi Li 2026

Leyi Li, Chenyu Du, Jiafei Sun, Erick Purwanto, and Qing Zhang. (2026). RoboBlockly Studio: Conversational Block Programming with Embodied Robot Feedback for Computational Thinking. Designing Interactive Systems Conference (DIS '26). https://doi.org/10.1145/3800645.3813071

`q2 · i?` · `design · r2`

Qualitative observation and interviews in the counterbalanced study: in the AI+Robot condition, "students often watched the run to localize where a failure emerged" and then asked the AI about a specific step or block choice, followed by verbalized reasoning.

> "Rather than only asking whether a solution was "correct, " students often watched the run to localize where a failure emerged (e.g., an incorrect turn, a collision with an obstacle, or a missed target region), and then revised the corresponding block segment."

### Leyi Li 2026 (2)

Leyi Li, Chenyu Du, Jiafei Sun, Erick Purwanto, and Qing Zhang. (2026). RoboBlockly Studio: Conversational Block Programming with Embodied Robot Feedback for Computational Thinking. Designing Interactive Systems Conference (DIS '26). https://doi.org/10.1145/3800645.3813071

`q2 · i?` · `causal · r2`

In the AI-Only condition, learners verified programs through on-screen inspection and AI dialogue; the authors observed that "several students in the AI–Only condition progressed further with partially incorrect reasoning" without a salient failure signal.

> "we observed that several students in the AI–Only condition progressed further with partially incorrect reasoning, because there was no immediate, perceptually salient signal (e.g., a visible misstep or failed interaction) to prompt targeted revision."

## Discussion


## Related Claims
- [30 of 32 participants preferred the AI+Robot condition, describing the robot as making success and failure visible, though a minority found AI-Only useful for focusing on block construction](preference-ai-plus-robot-condition.md) — related
- [Embodied collaborative construction can build shared geometric reasoning](embodied-collaborative-construction-can-build-shared-geometric-reasoning.md) — a broader claim this one bears on
- [Within a single LLM session, students' help-seeking shifts toward answer- and verification-seeking while explicit self-regulation modestly increases](within-session-hs-shifts-toward-closure-srl-increases.md) — related
- [Students' help requests to the AI tutor were predominantly instrumental rather than executive, with procedural content and low verification](instrumental-help-seeking-procedural-low-verification.md) — related
- [Scaffolded task progression shifts novice reasoning from local completion toward diagnosis and systematic debugging as task demands increase](scaffolded-task-progression-diagnostic-shift.md) — related
- [A language-based AI facilitator has access only to verbal traces of embodied inquiry and steers inquiry toward what can be put into words](language-facilitator-verbal-channel-limit.md) — related
