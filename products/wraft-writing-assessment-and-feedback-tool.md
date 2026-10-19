---
type: product
id: wraft-writing-assessment-and-feedback-tool
title: WrAFT (Writing Assessment and Feedback Tool)
description: WrAFT is a deployable, modular LLM-powered automated writing evaluation and feedback system developed by Adnan Labib and colleagues for argumentative-essay writers.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# WrAFT (Writing Assessment and Feedback Tool)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
WrAFT is a deployable, modular LLM-powered automated writing evaluation and feedback system developed by Adnan Labib and colleagues for argumentative-essay writers.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **WrAFT: deployable modular AWE system with interactive UI for in-line corrective edits and anchored comments**: WrAFT (Writing Assessment and Feedback Tool) is a modular LLM-powered automated writing evaluation system for argumentative essays, combining a fine-tuned GPT-4o scoring module, a GPT-4o surface-level feedback module, and Claude 3.7 macro and micro deep-level feedback pipelines. Its interactive UI shows a predicted score, a surface-level tab with three display modes including track-changes, and a deep-level tab modeled after Microsoft Word's Comment feature with color-coded highlights. The article states "An interactive user interface has been developed for the system, publicly available and free to use", with a deployable code package on GitHub and a web application at wraft.net. (Adnan Labib et al. (2026))

### Claims

- [Fine-tuned GPT-4o achieves state-of-the-art scoring of TOEFL argumentative essays with QWK 0.84 and RMSE 0.44 against official scores](../claims/wraft-finetuned-gpt4o-scoring-qwk-084.md) [+M]
- [Directly prompted GPT-4o surface-level corrective edits were judged necessary and effective in 96.14% of 2049 identified edits](../claims/wraft-surface-feedback-96-percent-precision.md) [+M]
- [Directly prompted Claude 3.7 macro-level deep feedback was judged effective for 93.03% of 201 paragraph-level comments](../claims/wraft-macro-feedback-93-percent-effective.md) [+M]
- [Directly prompted Claude 3.7 micro-level deep feedback was judged both necessary and effective in 94.69% of 630 comments](../claims/wraft-micro-feedback-95-percent-necessary-effective.md) [+M]
- [Prompt-based scoring prompts developed on one year's test generalize to the next year's edition with only minor adjustments](../claims/prompt-scoring-generalizes-across-test-editions.md) [~W]

## Related Products and Programmes

- [FOXGLOVE](foxglove.md)
- [MALA (Modular Artificial Learning Assistance)](mala-modular-artificial-learning-assistance.md)

## Key Sources
- Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524
