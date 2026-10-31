---
type: strategy
id: cot-tot-prompting-mitigate-llm-hallucination
title: Use Chain-of-Thought and Tree-of-Thought prompting to mitigate hallucination and weak complex reasoning in LLMs used for learning
description: The article recommends prompting strategies that make LLMs show their reasoning as a way to reduce hallucination and support complex reasoning.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
sources:
  - id: vij-o-2024
    resource: "https://doi.org/10.1371/journal.pone.0307372"
    title: "Vij O, Calver H, Myall N, Dey M, Kouranloo K. (2024). Evaluating the competency of ChatGPT in MRCP Part 1 and a systematic literature review of its capabilities in postgraduate medical assessments. PLOS ONE. https://doi.org/10.1371/journal.pone.0307372"
    author: Vij O, Calver H, Myall N, Dey M, Kouranloo K
---

# Use Chain-of-Thought and Tree-of-Thought prompting to mitigate hallucination and weak complex reasoning in LLMs used for learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 against) · 5 studies (4 causal, 1 review), `q2`–`q3` · 1 of 5 report an effect size · 5 claims rest on one study

## Description
The article recommends prompting strategies that make LLMs show their reasoning as a way to reduce hallucination and support complex reasoning. Chain-of-Thought prompting instructs the model to "divide tasks into smaller reasoning steps", so incorrect responses become identifiable because they are "often accompanied by rationales with factual inaccuracies". Tree-of-Thoughts builds a tree of partial solutions evaluated by deliberative reasoning; the article reports it has been applied to tasks including sudoku and crosswords.

## Design Implications

### Context
#### Requirements
- Only GPT-4, not GPT-3.5, was able to imitate advanced clinical reasoning processes with diagnostic CoT prompts, so the strategy requires a capable model.
#### Constraints
- The article reports GPT-4 can imitate clinical reasoning thought processes but cannot apply clinical reasoning in a comparable way to a human.

### Target Learners
- medical students
- doctors using ChatGPT as an education adjunct

### Target Learning Goals
- clinical reasoning
- accurate use of LLM-generated medical information

## Claims

- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](../claims/curricular-cot-improves-accuracy-larger-models.md) [+M]
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](../claims/reasoning-prompting-improves-llm-distractor-match.md) [+M]
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](../claims/reasoning-variants-no-alignment-improvement.md) [-M]
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](../claims/cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) [+M]
- [Hallucination, fabrication and reduced explanation accuracy limit ChatGPT's potential as a medical learning tool](../claims/hallucination-and-explanation-accuracy-limit-chatgpt-learning-tool.md) [+M]

## Related Strategies

- [Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations](pre-delivery-llm-evaluation-mitigate-hallucinations.md)

## Examples
-

## Key Sources
- Vij O, Calver H, Myall N, Dey M, Kouranloo K. (2024). Evaluating the competency of ChatGPT in MRCP Part 1 and a systematic literature review of its capabilities in postgraduate medical assessments. PLOS ONE. https://doi.org/10.1371/journal.pone.0307372
