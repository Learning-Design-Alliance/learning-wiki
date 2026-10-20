---
type: product
id: ktst
moved_from: [element/ktst-code-repository]
title: KTST
description: An open-source code repository released by Kai Neubauer and colleagues implementing knowledge tracing set transformers, their set-based interaction embeddings, and learnable ALiBi attention for research in knowledge tracing and intelligent tutoring systems.
product_kind: software
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: kai-neubauer-2026
    resource: "https://github.com/kainbr/kt_set_transformers"
    title: "Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers"
    author: Kai Neubauer, Yannick Rudolph, and Ulf Brefeld
---

# KTST

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 mixed) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size

## Description
An open-source code repository released by Kai Neubauer and colleagues implementing knowledge tracing set transformers, their set-based interaction embeddings, and learnable ALiBi attention for research in knowledge tracing and intelligent tutoring systems.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **KTST released code repository**: The authors released implementation code for knowledge tracing set transformers. The article states: "Code is available at github.com/kainbr/kt_set_transformers." The repository accompanies the KTST model class, its three set-based interaction embeddings, and the learnable ALiBi attention mechanism, and is intended to support the article's position that KTSTs are easy to implement and may serve as a foundation for future research in knowledge tracing and intelligent tutoring systems. (Kai Neubauer et al. (2026))

### Claims

- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](../claims/ablation-metadata-embeddings-largest-accuracy-drop.md) [~W]

## Related Products and Programmes
-

## Key Sources
- Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers

<!-- merged 2026-10-10 from elements/ktst-code-repository ("KTST released code repository"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

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


## Related Elements
- 

## Examples
-

## Key Sources
- Kai Neubauer, Yannick Rudolph, and Ulf Brefeld. (2026). Principled Transformers for Predictive Performance in Knowledge Tracing. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/kainbr/kt_set_transformers
-->
