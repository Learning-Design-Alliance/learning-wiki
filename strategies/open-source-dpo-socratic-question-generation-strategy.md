---
type: strategy
id: open-source-dpo-socratic-question-generation-strategy
title: Use open-source, preference-optimized LLMs as a cheaper, privacy-preserving alternative to proprietary models for Socratic question generation
description: The article recommends deploying preference-optimized open-source LLMs instead of proprietary rate-based API models for Socratic question generation.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: nischal-ashok-kumar-and-andrew-lan-2024
    resource: "https://arxiv.org/abs/2403.00199"
    title: "Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. https://arxiv.org/abs/2403.00199"
    author: Nischal Ashok Kumar and Andrew Lan
---

# Use open-source, preference-optimized LLMs as a cheaper, privacy-preserving alternative to proprietary models for Socratic question generation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (2 for, 3 mixed, 1 against) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article recommends deploying preference-optimized open-source LLMs instead of proprietary rate-based API models for Socratic question generation. The authors state their method "paves the way toward an open-source, accessible, cheaper, privacy-preserving, yet effective alternative to generating Socratic questions". Operationally, this means first fine-tuning Llama 2 with supervised fine-tuning on ground-truth dialogues, then applying DPO on a synthetic preference dataset of valid and invalid questions, decoding with nucleus sampling of multiple questions.

## Design Implications

### Context
#### Requirements
- An existing Socratic dialogue dataset with ground-truth questions from which a preference dataset of valid and invalid question pairs can be constructed
#### Constraints
- The article reports no systematic human evaluation of the generated questions; bias in the generated augmenting data was not formally analyzed

### Target Learners
- novice programmers in computer science education

### Target Learning Goals
- generating valid Socratic questions that guide students to debug code without revealing the solution

## Claims

- [GPT-4 consistency checking retains 72% of synthetically generated invalid questions, discarding 27% classified as good and 1% as incorrect](../claims/consistency-checking-retains-72-percent-invalid-questions.md) [~W]
- [A DPO-optimized Llama 2-7B model gives the best Rouge-L scores among all compared Socratic question generation methods, including GPT-3.5 and GPT-4 prompting baselines](../claims/dpo-llama2-best-rouge-l-socratic-question-generation.md) [+W]
- [DPO consistently outperforms supervised fine-tuning (SFT) for Socratic question generation with Llama 2](../claims/dpo-outperforms-sft-socratic-questions.md) [+W]
- [GPT-4 (CoT) prompting achieves the highest recall but the lowest F1 score among GPT baselines because most of its generated questions do not match ground truth](../claims/gpt4-cot-highest-recall-lowest-f1.md) [~W]
- [Sampling multiple Socratic questions (Sample-5) yields better performance than greedy decoding](../claims/sample-5-beats-greedy-decoding-socratic.md) [~W]
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](../claims/proprietary-llms-outperform-open-source-ebhs.md) [-W]

## Related Strategies

- [Use mismatched gold feedback for other incorrect answers to the same question as hard negatives when constructing feedback preference pairs](mismatched-feedback-hard-negatives-strategy.md)

## Examples
-

## Key Sources
- Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. https://arxiv.org/abs/2403.00199
