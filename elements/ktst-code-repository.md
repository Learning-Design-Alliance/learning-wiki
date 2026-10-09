---
type: element
id: ktst-code-repository
title: KTST released code repository
description: The authors released implementation code for knowledge tracing set transformers.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: kai-neubauer-2026
    resource: "https://github.com/kainbr/kt_set_transformers"
    title: "Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers"
    author: Kai Neubauer, Yannick Rudolph, and Ulf Brefeld
---

# KTST released code repository

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors released implementation code for knowledge tracing set transformers. The article states: "Code is available at github.com/kainbr/kt_set_transformers." The repository accompanies the KTST model class, its three set-based interaction embeddings, and the learnable ALiBi attention mechanism, and is intended to support the article's position that KTSTs are easy to implement and may serve as a foundation for future research in knowledge tracing and intelligent tutoring systems.

## Design Implications

### Context
#### Requirements
- Users need sequences of student interactions with questions, knowledge components, and binary responses to train and apply the models
#### Constraints
- 

### Target Learners
- students interacting with intelligent tutoring systems

### Target Learning Goals
- knowledge tracing prediction of next-response correctness

### Affordances
- [Ktst Model Class](../theories/ktst-model-class.md)

## Claims

- [KTST performance gains over baselines using the expanded representation are most pronounced on datasets with high knowledge-component-to-question ratios](../claims/ktst-gains-largest-high-kc-ratio-datasets.md) [+W]
- [KTST models achieve state-of-the-art AUC results on pyKT benchmark datasets except Statics2011](../claims/ktst-state-of-the-art-auc-pykt-benchmark.md) [+W]
- [Learnable ALiBi with query equal to key in cross-attention is the best-performing attention configuration for KTSTs](../claims/learnable-alibi-best-attention-ktst-ablation.md) [+W]
- [Replacing Rasch embeddings with mean set embeddings under AKT's attention improves AUC on AS2009, evidence against the expanded representation](../claims/mean-embeddings-beat-rasch-embeddings-as2009.md) [-W]

## Related Elements
- 

## Examples
-

## Key Sources
- Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers
