---
type: design
id: publication-gated-qa-workflow
title: "Structurally embedded quality assurance: publication gated behind completed test-correct-verify cycles"
description: This pattern embeds quality assurance structurally in the authoring workflow rather than relying on voluntary compliance.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: miina-koyama-2026
    resource: "https://arxiv.org/abs/2605.16605"
    title: "Miina Koyama, Ruiwei Xiao, and John Stamper. (2026). PromptDecipher: Supporting AI Tutor Authoring Through Editable Simulated Interactions. https://arxiv.org/abs/2605.16605"
    author: Miina Koyama, Ruiwei Xiao, and John Stamper
---

# Structurally embedded quality assurance: publication gated behind completed test-correct-verify cycles

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This pattern embeds quality assurance structurally in the authoring workflow rather than relying on voluntary compliance. Publication is blocked until all test cases are marked as passed, and "publication is gated behind at least one completed cycle" of testing, correcting, and verification. The article states this "enforces QA as a first-class activity and scaffolds teachers in roles they would otherwise skip," addressing the finding that teachers rarely test bots before deployment.

## Design Implications

### Context
#### Requirements
- A suite of pre-defined test scenarios with simulated student profiles, and a mechanism that blocks publication until test cases pass
#### Constraints
- The article reports the pattern as designed and demonstrated; whether it increases testing rates at scale is a planned future analysis

### Target Learners
- teachers and higher-education instructors authoring AI tutors

### Learning Goals
- systematic pre-deployment testing of AI tutoring chatbots

### Claims
- [Teachers Rarely Test Ai Tutor Bots Before Publication](../claims/teachers-rarely-test-ai-tutor-bots-before-publication.md) [+M]

## Related Designs
- Promptdecipher Authoring System

## Examples
-

## Key Sources
- Miina Koyama, Ruiwei Xiao, and John Stamper. (2026). PromptDecipher: Supporting AI Tutor Authoring Through Editable Simulated Interactions. https://arxiv.org/abs/2605.16605
