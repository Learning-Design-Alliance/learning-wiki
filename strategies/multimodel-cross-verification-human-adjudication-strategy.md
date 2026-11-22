---
type: strategy
id: multimodel-cross-verification-human-adjudication-strategy
title: Use multi-model cross-verification with human adjudication of disagreements to raise LLM accuracy on medical examinations
description: "The article proposes combining multiple LLMs on the same examination: adopt the models' answer when they agree and resort to human judgment when they disagree."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: yao-zhong-2025
    resource: "https://doi.org/10.2196/69485"
    title: "Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485"
    author: Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang
---

# Use multi-model cross-verification with human adjudication of disagreements to raise LLM accuracy on medical examinations

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes combining multiple LLMs on the same examination: adopt the models' answer when they agree and resort to human judgment when they disagree. Applied to the CNMLE, dual-model (Baichuan+ChatGPT) verification reached 94.17% accuracy and tri-model verification 96.33%, with the largest improvements on simple question types. The authors frame this as mitigating AI hallucination through cross-verification mechanisms.

## Design Implications

### Context
#### Requirements
- At least two LLMs whose error sets overlap only partially, so agreement signals correctness and disagreements can be escalated
#### Constraints
- The process remained semiautomated, requiring human judgment when models disagree; gains were most pronounced on simple question types

### Target Learners
- medical educators and assessment developers using LLMs in medical testing

### Target Learning Goals
- accurate automated answering and assessment of medical knowledge

## Claims

- [Multi-model cross-verification outperformed the single best model, reaching 94.17% accuracy with two models and 96.33% with three](../claims/multimodel-cross-verification-accuracy-gains.md) [+W]

## Related Strategies

- [Cross-verify LLM answers using multiple models to reduce the risk of overconfident misinformation](cross-verification-multiple-llm-models.md)

## Examples
-

## Key Sources
- Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485
