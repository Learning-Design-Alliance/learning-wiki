---
type: theory
title: Deep Learning Knowledge Tracing Models
description: "The survey reviews deep learning KT in four sub-categories: deep knowledge tracing with recurrent networks, memory-aware tracing such as DKVMN with key and value matrices, attentive tracing such as SAKT, SAINT and AKT..."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
---

# Deep Learning Knowledge Tracing Models

> **Theory** · [All theories](index.md)

## Description
The survey reviews deep learning KT in four sub-categories: deep knowledge tracing with recurrent networks, memory-aware tracing such as DKVMN with key and value matrices, attentive tracing such as SAKT, SAINT and AKT built on self-attention, and graph-based tracing over knowledge-concept graphs. It argues deep learning is suited to "modeling complex learning processes, particularly when a significant amount of learning interaction data" is available.

## Design Implications

### Context
#### Requirements
- A significant amount of learning interaction data, since the survey says deep learning models are predominantly data-driven and benefit from large-scale student learning data
#### Constraints
- The survey reports DKT's lack of interpretability and two phenomena identified by Yeung and Yeung: inability to reconstruct observed input and inconsistent predicted knowledge states across time-steps

### Target Learners
- Students whose exercise-answering interactions are recorded by online learning systems such as ASSISTments, Junyi Academy, Eedi and EdNet's Santa tutor

### Target Learning Objectives
- Monitoring students' evolving knowledge states on knowledge concepts and predicting performance on future exercises

### Claims
- [Deep Learning Knowledge Tracing Outperforms But Lacks Interpretability](../claims/deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) [~W]
- [Attentive Knowledge Tracing Benefits From Repeated Interactions](../claims/attentive-knowledge-tracing-benefits-from-repeated-interactions.md) [~W]
- [Xai Interpretation Of Dkt Enhances Trust](../claims/xai-interpretation-of-dkt-enhances-trust.md) [+W]

## Related Theories
- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
