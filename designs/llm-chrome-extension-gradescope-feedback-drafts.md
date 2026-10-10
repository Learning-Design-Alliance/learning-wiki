---
type: design
id: llm-chrome-extension-gradescope-feedback-drafts
title: LLM-backed Chrome extension surfacing AI feedback drafts within Gradescope
description: A lightweight, LLM-backed Chrome extension integrated into the Gradescope grading platform, powered by o4-mini (selected via Bradley-Terry analysis of TA rankings).
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: mahinpei-2026
    resource: "https://arxiv.org/abs/2606.03095"
    title: "Mahinpei, R., Dean, V., Fong, R., Liu, L. T., & Ribeiro, M. H. (2026). AI Assistance for Discretionary Work: Increasing Feedback Provision in Higher Education. arXiv. https://arxiv.org/abs/2606.03095"
    author: "Mahinpei, R., Dean, V., Fong, R., Liu, L. T., & Ribeiro, M. H"
---

# LLM-backed Chrome extension surfacing AI feedback drafts within Gradescope

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A lightweight, LLM-backed Chrome extension integrated into the Gradescope grading platform, powered by o4-mini (selected via Bradley-Terry analysis of TA rankings). After grading, TAs click a "Done Grading" button inserted by the extension; in treatment submissions a personalized AI feedback draft is shown, which TAs "can use the feedback draft as-is, edit it, or ignore it." The extension also logs behavioral data (provision, length, time) and embeds in-situ surveys on draft usage and helpfulness.

## Design Implications

### Context
#### Requirements
- Integration with an existing grading platform (Gradescope)
- A prompt incorporating problem description, instructor solution, grading rubric, and student submission
#### Constraints
- Drafts shown only after grading to reduce over-reliance, per instructor and formative-study input

### Target Learners
- teaching assistants grading written assessments in higher education

### Learning Goals
- increasing personalized feedback provision on student submissions

### Claims
- [Ai Drafts Increase Discretionary Feedback Provision](../claims/ai-drafts-increase-discretionary-feedback-provision.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Mahinpei, R., Dean, V., Fong, R., Liu, L. T., & Ribeiro, M. H. (2026). AI Assistance for Discretionary Work: Increasing Feedback Provision in Higher Education. arXiv. https://arxiv.org/abs/2606.03095
