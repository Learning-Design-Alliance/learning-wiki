---
type: product
id: promptdecipher
title: PromptDecipher
description: A web-based chatbot-authoring system developed by Miina Koyama and colleagues that lets educators create and refine AI tutoring chatbots by directly correcting simulated bot responses.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# PromptDecipher

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A web-based chatbot-authoring system developed by Miina Koyama and colleagues that lets educators create and refine AI tutoring chatbots by directly correcting simulated bot responses.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Reverse Prompting Pipeline: diff analysis, prompt rewrite, and regression verification triggered by teacher corrections**: The Reverse Prompting Pipeline is the automated mechanism at the core of PromptDecipher, triggered when a teacher submits an edit to a bot response. It runs three steps: "Diff analysis. An LLM compares the original and corrected responses to infer the teacher's pedagogical intent"; a targeted prompt rewrite proposed for teacher review; and "Regression verification. The revised prompt is automatically evaluated across all previously passed test cases." The test-correct-verify cycle continues until the teacher is satisfied. (Miina Koyama et al. (2026))

### Claims
- [Instructors authoring AI tutoring chatbots in a MOOC almost never systematically tested their bots before deploying them to students](../claims/teachers-rarely-test-ai-tutor-bots-before-publication.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Miina Koyama, Ruiwei Xiao, and John Stamper. (2026). PromptDecipher: Supporting AI Tutor Authoring Through Editable Simulated Interactions. https://arxiv.org/abs/2605.16605
