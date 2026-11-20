---
type: strategy
id: mismatched-feedback-hard-negatives-strategy
title: Use mismatched gold feedback for other incorrect answers to the same question as hard negatives when constructing feedback preference pairs
description: When constructing preference pairs for DPO training, the article pairs each gold feedback not only with lower-scoring generated feedback but also with feedback written for different incorrect answers to the same quest...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2403.01304"
    title: "Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. https://arxiv.org/abs/2403.01304"
    author: Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan
---

# Use mismatched gold feedback for other incorrect answers to the same question as hard negatives when constructing feedback preference pairs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
When constructing preference pairs for DPO training, the article pairs each gold feedback not only with lower-scoring generated feedback but also with feedback written for different incorrect answers to the same question. The authors observe that "these mis- matched feedback are excellent hard negatives since it is hard for algorithms to distinguish between them and good feedback", because such feedback shares many semantic features, variables, and numbers with the correct feedback. Including these pairs substantially increased the correctness of generated feedback in their experiments.

## Design Implications

### Context
#### Requirements
- A gold dataset with human-written feedback for each incorrect answer option, so mismatched feedback for the same question exists.
#### Constraints
- The article notes online RL algorithms such as PPO could also apply but would require training a reward model and introduce training instability issues.

### Target Learners
- middle school math students

### Target Learning Goals
- improving correctness of automatically generated feedback

## Claims

- [DPO training on GPT-4 rubric annotations with mismatched feedback significantly improves the correctness and alignment of Llama 2-generated math feedback compared to zero-shot and SFT baselines.](../claims/dpo-score-mismatch-improves-math-feedback.md) [+M]
- [DPO consistently outperforms supervised fine-tuning (SFT) for Socratic question generation with Llama 2](../claims/dpo-outperforms-sft-socratic-questions.md) [+M]

## Related Strategies

- [Use open-source, preference-optimized LLMs as a cheaper, privacy-preserving alternative to proprietary models for Socratic question generation](open-source-dpo-socratic-question-generation-strategy.md)

## Examples
-

## Key Sources
- Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. https://arxiv.org/abs/2403.01304
