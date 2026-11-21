---
type: strategy
id: examples-and-anti-examples-prompt-strategy
title: Prompt misconception generation with positive examples and verbose anti-examples plus explicit length constraints
description: For closed-source LLM misconception generation, the article systematically evaluated six prompting strategies on 20 conversations.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: joshua-mitton-2026
    resource: "https://arxiv.org/abs/2602.02414"
    title: "Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. https://arxiv.org/abs/2602.02414"
    author: Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead
---

# Prompt misconception generation with positive examples and verbose anti-examples plus explicit length constraints

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
For closed-source LLM misconception generation, the article systematically evaluated six prompting strategies on 20 conversations. The best strategy, "With Examples", constrains output to 5-12 words, provides positive example labels, and supplies negative anti-examples of the verbose explanatory style LLMs naturally produce. It "achieved a mean similarity of 0.615 (12% improvement over baseline) while reducing output length from 56.8 to 9.1 words (84% reduction)". The authors found explicit length constraints alone insufficient and recommend incorporating such constraints and examples into fine-tuning objectives rather than relying solely on inference-time prompting.

## Design Implications

### Context
#### Requirements
- Access to representative expert-authored misconception labels to use as positive examples and verbose outputs to use as anti-examples
#### Constraints
- Evaluated only on Claude Sonnet 4.5 over a sample of 20 conversations with MiniLM-L6-v2 similarity as the measure

### Target Learners
- school mathematics students on an online tutoring platform

### Target Learning Goals
- generating concise, retrieval-friendly misconception hypotheses from student-tutor dialogue

## Claims

- [LoRA fine-tuning improves generated misconception style and raises cosine similarity with expert labels, letting small open-source models rival larger closed-source ones](../claims/lora-finetuning-improves-misconception-generation-style.md) [+W]
- [Qwen 2.5 7B performs comparably to Claude Sonnet 4.5 for dialogue-based misconception diagnosis despite being much smaller](../claims/qwen-7b-comparable-to-claude-misconception-diagnosis.md) [+W]
- [Semantic similarity between predicted and true misconceptions does not guarantee mathematical coherence](../claims/semantic-similarity-not-mathematical-coherence.md) [-W]

## Related Strategies

- [Calibrate LMM danmaku generation with explicit length, frequency, count, and highlight constraints derived from prior danmaku research](calibrated-danmaku-generation-constraints.md)
- [Constrain an LLM to inquiry-only questioning via negative system-prompt constraints plus strict JSON schemas](negative-constraint-prompting-inquiry-only-llm.md)

## Examples
-

## Key Sources
- Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. https://arxiv.org/abs/2602.02414
