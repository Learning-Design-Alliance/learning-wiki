---
type: theory
title: Deep Learning Knowledge Tracing Models
description: "The survey reviews deep learning KT in four sub-categories: deep knowledge tracing with recurrent networks, memory-aware tracing such as DKVMN with key and value matrices, attentive tracing such as SAKT, SAINT and AKT..."
canonical: true
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
---

# Deep Learning Knowledge Tracing Models

> **Theory** · [All theories](index.md)
> **Evidence** · 12 claims (3 for, 8 mixed, 1 against) · 9 studies (6 design, 1 causal, 1 review, 1 associational), `q1`–`q2` · 0 of 9 report an effect size · 12 claims rest on one study

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
- [Responsible-DKT outperforms a neural-symbolic baseline without knowledge injection and a fully data-driven PyTorch DKT in predictive accuracy across training ratios and sequence lengths](../claims/responsible-dkt-outperforms-baselines-predictive-accuracy.md) [+M] — attached 2026-10-11 from Hooshyar et al. (2026), which proposed "Responsible-DKT: a neural-symbolic deep knowledge tracing framework injecting symbolic educational knowledge into sequential neural architectures".
- Deep Knowledge Tracing substantially outperforms Bayesian Knowledge Tracing on knowledge tracing benchmarks [+W] — attached 2026-10-14 from Chris Piech et al. (2015), which proposed "Deep Knowledge Tracing: modeling latent student knowledge with recurrent neural networks"; tests this page's relationship.
- DKT matches an oracle on simulated data without concept labels, while BKT degrades as hidden concepts increase [+W] — attached 2026-10-14 from Chris Piech et al. (2015), which proposed "Deep Knowledge Tracing: modeling latent student knowledge with recurrent neural networks"; tests this page's relationship.
- [Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive](../claims/code-embeddings-inconsistent-under-rectified-settings.md) [~M]
- [Injecting the collaborative prior redistributes AKT's attention from local recency bias toward long-range dependencies](../claims/mbp-kt-attention-recency-to-long-range.md) [~W]
- [Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline](../claims/nonlinear-models-modest-auc-gains-over-logistic-baseline.md) [-W]
- [Sequential deep learning models outperform static models for concepts mapped to multiple post-test questions](../claims/sequential-models-outperform-static-multi-question-concepts.md) [+W]
- [Task-specific hyperparameter optimization substantially raises baseline DKT performance, indicating prior DKT-vs-PKT gaps partly reflect insufficient baseline tuning](../claims/task-specific-hyperparameter-tuning-raises-dkt-baseline.md) [~W]
- [DKT+ regularization addresses two DKT deficits: failure to reconstruct observed interactions and inconsistent knowledge-state transitions across time steps.](../claims/dkt-plus-regularization-addresses-reconstruction-and-transition-consistency.md) [~W]
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](../claims/knowledge-tracing-model-choice-depends-on-dataset.md) [~M] — deep knowledge tracing led on five of nine datasets and logistic regression on four
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](../claims/newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) [~M] — a benchmark of ten deep models on seven datasets under one protocol

## The evidence by question

- *How accurately does BKT predict a learner's next answers, compared with other knowledge-tracing models, and do its assumptions and fitted parameters hold up?* [The survey states that deep learning knowledge tracing models exhibit superior performance to Bayesian and logistic models but have significant room for improvement in interpretability.](../claims/deep-learning-knowledge-tracing-outperforms-but-lacks-interpretability.md) [~M]

## Related Theories

- [Knowledge Tracing Model Taxonomy](knowledge-tracing-model-taxonomy.md)
- [Adaptive G-UKT: a unified probabilistic knowledge tracing framework coupling Gaussian state representations, adaptive graph topology learning, Wasserstein attention, and uncertainty-gated contrastive regularization](../research-methods/adaptive-g-ukt.md)
- [Colearn: a multi-task memory-augmented deep learning model jointly predicting knowledge state and hint-taking](colearn-multi-task-hint-knowledge-model.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
