---
type: design
id: classroom-proof-assistant-design-criteria
title: Eight learner-centered design criteria for classroom proof assistants, organized under learning and usability goals
description: "The article proposes a framework of two broad goals — \"learning: the tool should help students refine and improve their mathematical proof skills; and usability: the tool should not create unnecessary frictions in wri..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: matthew-keenan-2026
    resource: "https://arxiv.org/abs/2608.23309"
    title: "Matthew Keenan, Nishant Kheterpal, Jean-Baptiste Jeannin, Cyrus Omar. (2026). Hazel Prover: A Classroom Proof Assistant for Learning Structural Induction. https://arxiv.org/abs/2608.23309"
    author: Matthew Keenan, Nishant Kheterpal, Jean-Baptiste Jeannin, Cyrus Omar
---

# Eight learner-centered design criteria for classroom proof assistants, organized under learning and usability goals

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes a framework of two broad goals — "learning: the tool should help students refine and improve their mathematical proof skills; and usability: the tool should not create unnecessary frictions in writing proofs" — expanded into eight numbered criteria: supporting active exploration, consistent model, requiring engagement, notation similar to written proofs, engagement similar to written proofs, easy setup, minimal training, and minimal tedium. The criteria were synthesized from prior classroom deployments and a workshop survey, and the authors believe they are transferable to classroom proof assistants for other domains.

## Design Implications

### Context
#### Requirements
- The assistant must require genuine cognitive engagement with the mathematical ideas in order to complete exercises, and feedback should be provided for partial proofs, not just once a proof is complete.
#### Constraints
- The final two learning criteria apply specifically to settings where students are expected to write proofs on paper, since in many but not all classroom settings transfer to pen-and-paper is expected.

### Target Learners
- undergraduate and graduate programming languages students

### Learning Goals
- equational reasoning
- structural induction
- transfer of proof skills to pen-and-paper

### Claims
- [Manual Evaluation Steps Improve Exam Transfer](../claims/manual-evaluation-steps-improve-exam-transfer.md) [+M]
- Manual Steps Reduce Random Clicking [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Matthew Keenan, Nishant Kheterpal, Jean-Baptiste Jeannin, Cyrus Omar. (2026). Hazel Prover: A Classroom Proof Assistant for Learning Structural Induction. https://arxiv.org/abs/2608.23309
