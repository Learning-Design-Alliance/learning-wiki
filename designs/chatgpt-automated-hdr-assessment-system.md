---
type: design
id: chatgpt-automated-hdr-assessment-system
title: ChatGPT-based automated HDR assessment system (problem generation, scoring, and feedback pipeline)
description: An LLM-based automated environment built with ChatGPT (GPT-4o) that integrates three prompts—problem generation, scoring, and feedback—into one system handling the full HDR assessment cycle.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: satoshi-takahashi-2026
    resource: "https://arxiv.org/abs/2609.25790"
    title: "Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790"
    author: Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada
---

# ChatGPT-based automated HDR assessment system (problem generation, scoring, and feedback pipeline)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
An LLM-based automated environment built with ChatGPT (GPT-4o) that integrates three prompts—problem generation, scoring, and feedback—into one system handling the full HDR assessment cycle. The scoring and feedback prompts are integrated into one prompt, with "Explanation" and "Good Points" sections outputting the score rationale and feedback. The system generates problems aligned with educational intentions and quickly assesses descriptive tasks focused on knowledge misuse, with reproducibility, immediacy, and low cost.

## Design Implications

### Context
#### Requirements
- A pretest collecting actual descriptive answers from learners to serve as the basis for scoring and feedback prompts
- Prompts designed for consistency, educational validity, and explainability
#### Constraints
- Some problem and answer data were collected in a previous study (Takahashi et al., 2025)
- Validated only with GPT-4o; behavior may differ across LLMs

### Target Learners
- Working adults in business education (MBA-style programs)

### Learning Goals
- Detection and explanation of knowledge misuse in practical cases

### Claims
- [Prompt Design With Role And Hints For Llm Assessment](../strategies/prompt-design-with-role-and-hints-for-llm-assessment.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790
