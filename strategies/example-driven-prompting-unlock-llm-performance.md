---
type: strategy
id: example-driven-prompting-unlock-llm-performance
title: Provide diverse, representative examples in prompts to unlock latent LLM performance on discourse classification
description: "The article concludes that prompt engineering—\"specifically the inclusion of diverse examples without cognitive overload—can effectively unlock the latent pedagogical capabilities of large foundation models.\" Concrete..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: kirk-vanacore-and-rené-f-kizilcec-2025
    resource: "https://arxiv.org/abs/2512.19903"
    title: "Kirk Vanacore and René F. Kizilcec. (2025). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. https://arxiv.org/abs/2512.19903"
    author: Kirk Vanacore and René F. Kizilcec
---

# Provide diverse, representative examples in prompts to unlock latent LLM performance on discourse classification

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (2 for, 2 mixed, 1 against) · 4 studies (3 causal, 1 review), `q2` · 0 of 4 report an effect size · 5 claims rest on one study

## Description
The article concludes that prompt engineering—"specifically the inclusion of diverse examples without cognitive overload—can effectively unlock the latent pedagogical capabilities of large foundation models." Concretely, prompts should mirror what expert human annotators receive: code definitions, decision rules, and annotated examples drawn from the official coding manual. The strategy worked dramatically for Claude 4.5 Opus (κ 0.48→0.58) and Gemini 2.5 Pro (0.38→0.57) but yielded minimal gains for GPT-5 and o3, so model selection matters alongside prompt design.

## Design Implications

### Context
#### Requirements
- Access to a validated codebook with definitions, decision rules, and annotated examples aligned with the specific pedagogical context.
#### Constraints
- The benefit was not uniform across models; the article cautions that adding examples can sometimes degrade performance if examples are not perfectly aligned with the pedagogical context, and that more examples will not automatically reduce labeling error.

### Target Learners
- K–12 mathematics students whose classroom discourse is analyzed

### Target Learning Goals
- Accurate automated classification of instructional Talk Moves

## Claims

- [Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3](../claims/few-shot-prompting-gains-heterogeneous-llm.md) [~W]
- [Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts](../claims/llm-baseline-moderate-kappa-talk-moves.md) [+W]
- [In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner](../claims/icl-does-not-unlock-beyond-k5-reasoning.md) [-W]
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](../claims/curricular-cot-improves-accuracy-larger-models.md) [~W]
- [LLMs prompted with diverse strategies can analyze educational survey feedback and generate corrective tutor feedback at or above expert human performance in specific scenarios](../claims/llm-prompting-human-level-educational-feedback.md) [+W]

## Related Strategies

- [Select LLM mentor moves using three CogApp principles: global before local skills, increasing complexity, and increasing diversity](cogapp-three-move-selection-principles.md)
- [Future work should refine prompts, add past utterances for context, and use error analysis to improve label definitions](future-work-refine-prompts-add-context-improve-label-definitions.md)
- [Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)](structured-prompt-framework-inductive-coding.md)

## Examples
-

## Key Sources
- Kirk Vanacore and René F. Kizilcec. (2025). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. https://arxiv.org/abs/2512.19903
