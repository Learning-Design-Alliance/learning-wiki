---
type: strategy
id: chatgpt-lab-prompting-strategies
title: Use specific, detailed, iterative and explicit prompts when directing ChatGPT Code Interpreter through laboratory tasks
description: "The article distils its three Approaches into four prompt strategies for laboratory use: \"Specificity Matters\", \"Iterative Questioning\", \"Explicit Instruction\", and \"Avoid Ambiguity and Assumptions\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: andrew-low-and-z-yasemin-kalender-2023
    resource: "https://arxiv.org/abs/2311.12415"
    title: "Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. https://arxiv.org/abs/2311.12415"
    author: Andrew Low and Z. Yasemin Kalender
---

# Use specific, detailed, iterative and explicit prompts when directing ChatGPT Code Interpreter through laboratory tasks

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article distils its three Approaches into four prompt strategies for laboratory use: "Specificity Matters", "Iterative Questioning", "Explicit Instruction", and "Avoid Ambiguity and Assumptions". Detailed initial prompts led to more comprehensive analysis, follow-up questioning identified mistakes, and clearly stating formats, axes and propagation methods prevented ChatGPT from making unstated assumptions such as calculating spring constants from value pairs instead of a line fit.

## Design Implications

### Context
#### Requirements
- Users must supply relevant detail such as required table column formats, which variables to plot on each axis, and how errors should be propagated
#### Constraints
- Without clear and specific instructions, ChatGPT is likely to make assumptions that are not explicitly stated or justified, as in Approach 1

### Target Learners
- undergraduate physics students
- STEM educators

### Target Learning Goals
- data generation and analysis in laboratory courses
- effective and critical use of AI tools

## Claims

- [The quality and accuracy of ChatGPT's output on a lab activity varies significantly with the detail and specificity of the prompts](../claims/prompt-detail-determines-chatgpt-lab-output-quality.md) [+M]
- [Novice learners may struggle to identify ChatGPT errors or provide the prompt detail needed for high-quality output](../claims/novice-learners-struggle-to-spot-chatgpt-errors.md) [~W]

## Related Strategies

- [Engineer LLM grading prompts with detailed, domain-specific evaluation criteria and band descriptors](prompt-llm-grading-with-detailed-band-descriptors.md)
- [Edit ambiguous student questions into clear, directive prompts before posing them to ChatGPT](edit-ambiguous-student-questions-into-directive-prompts.md)

## Examples
-

## Key Sources
- Andrew Low and Z. Yasemin Kalender. (2023). Data Dialogue with ChatGPT: Using Code Interpreter to Simulate and Analyse Experimental Data. https://arxiv.org/abs/2311.12415
