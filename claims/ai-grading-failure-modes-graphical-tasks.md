---
type: claim
title: AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels
description: AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels
id: ai-grading-failure-modes-graphical-tasks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: jan-cvengros-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1007/s44163-026-01606-4"
    title: "Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4"
    author: Jan Cvengros and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jan-cvengros-and-gerd-kortemeyer-2026-2
    resource: "https://doi.org/10.1007/s44163-026-01606-4"
    title: "Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4"
    author: Jan Cvengros and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` AI sometimes assigned full points for a completely incorrect chemical equation (2 Na+ + H−2 −→ 2 NaH), a false positive that students would be unlikely to contest and that would remain undetected. [→ Jan Cvengros and Gerd Kortemeyer 2026](#jan-cvengros-and-gerd-kortemeyer-2026)
`q2 i?` In graphical tasks, AI misread a crystal-field sketch — interpreting the labeled energy axis as an electron — and assigned zero credit where the TA awarded full credit. [→ Jan Cvengros and Gerd Kortemeyer 2026 (2)](#jan-cvengros-and-gerd-kortemeyer-2026-2)

## Evidence

### Jan Cvengros and Gerd Kortemeyer 2026

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Qualitative comparison of TA-graded exam sheets against AI score sheets (Sect. 4.2). For the sodium-hydride formation equation, the article reports AI "assigned full points also for the equation" with disrupted charge balance, and notes students usually do not complain about receiving points from wrong answers.

> "AI, however assigned full points also for the equation 2 Na+ + H− 2 −→ 2 NaH, which is incorrect as the charge balance is disrupted"

### Jan Cvengros and Gerd Kortemeyer 2026 (2)

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Qualitative false-negative example (Fig. 6, problem 6-C-b): the leftmost arrow was actually the energy axis labeled E; interpreted correctly the answer matched the rubric and the TA awarded full credit. The article states such errors "very often occurred in graphical tasks".

> "AI misread the sketch. It detected three upward arrows in the higher-energy level and interpreted them as three electrons with identical spin, concluding that the student had indicated an incorrect electron count and therefore assigned zero credit"

## Discussion


## Related Claims
- [LLMs expressed unjustified confidence in recommendations based on visual inputs, asserting incorrect pin-connection diagnoses with high stated certainty](llm-unjustified-confidence-visual-recommendations.md) — related
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [All evaluated GenAI systems scored noticeably lower on graphics-related questions requiring interpretation of JavaFX output](genai-weak-visual-reasoning-javafx-questions.md) — related
- [Three recurring AI failure modes arose in this project-based learning context: plausible-but-incorrect code, missing specialized knowledge, and limited long-term context](three-ai-failure-modes-project-based-learning.md) — related
