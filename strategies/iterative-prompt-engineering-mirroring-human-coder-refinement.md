---
type: strategy
id: iterative-prompt-engineering-mirroring-human-coder-refinement
title: "Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts"
description: "The article describes an iterative prompt engineering process that mirrors human coders' labeling processes, where coders review and discuss utterances causing the most disagreement and refine their coding guidelines."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: spain-2024
    resource: "https://doi.org/10.21203/rs.3.rs-4565500/v1"
    title: "Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1"
    author: "Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J"
---

# Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (2 design), `q2`–`q3` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article describes an iterative prompt engineering process that mirrors human coders' labeling processes, where coders review and discuss utterances causing the most disagreement and refine their coding guidelines. The process progresses through four stages: starting with label definitions, adding category examples, adding scenario context and Command label clarification, and finally adding inter-class clarification for the most conflated labels. This strategy is described as "intuitive and effective" and proved to be "a potent strategy for enhancing classier performance with constrained datasets".

## Design Implications

### Context
#### Requirements
- Access to a GPT-3.5 or GPT-4 model with a temperature setting of 0.2 to minimize randomness
- A coding sheet or label definitions as the starting prompt
- Confusion matrix analysis to identify the most conflated label pairs for inter-class clarification
#### Constraints
- Few-shot learning with examples per class only marginally improved accuracy while significantly increasing prompt size, so the authors opted to focus on zero-shot learning

### Target Learners
- team members in military squad training exercises

### Target Learning Goals
- accurate dialogue act classification for adaptive team training feedback

## Claims

- [Zero-shot GPT-4 with iterative prompt engineering achieves 77.30% dialogue act recognition accuracy, outperforming fine-tuned T5, CRF, and BLSTM baselines on a held-out test set.](../claims/gpt4-zero-shot-dialogue-act-recognition-outperforms-t5-baselines.md) [+W]
- [Iterative prompt engineering stages progressively improve GPT-3.5 dialogue act recognition accuracy from 0.369 to 0.631 on the training set.](../claims/iterative-prompt-engineering-improves-gpt-dialogue-act-accuracy.md) [+W]
- [Prompt refinements targeting inter-label confusion yield superior recall rates for challenging dialogue act labels, including Command (F1 raised to 0.75) and Other (GPT-4 recall 0.67 vs. T5 0.54).](../claims/prompt-refinements-improve-recall-challenging-dialogue-acts.md) [+W]
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](../claims/gpt4-almost-perfect-irr-after-rubric-engineering.md) [+W]

## Related Strategies

- [Future work should refine prompts, add past utterances for context, and use error analysis to improve label definitions](future-work-refine-prompts-add-context-improve-label-definitions.md)
- [Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling](instruction-guided-llm-annotation-interaction-labels.md)
- [Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)](structured-prompt-framework-inductive-coding.md)
- [Incorporate an expert human in the loop to support LLM coding of difficult adjacent coding categories](expert-human-in-loop-for-llm-pck-coding.md)

## Examples
-

## Key Sources
- Spain, R., Min, W., Kumaran, V., Pande, V., Saville, J., & Lester, J. (2024). Applying Large Language Models to Enhance Dialogue and Communication Analysis for Adaptive Team Training. https://doi.org/10.21203/rs.3.rs-4565500/v1
