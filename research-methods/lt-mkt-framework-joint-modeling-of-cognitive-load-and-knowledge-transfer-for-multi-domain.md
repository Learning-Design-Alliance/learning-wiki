---
type: research-method
id: lt-mkt-framework-joint-modeling-of-cognitive-load-and-knowledge-transfer-for-multi-domain
title: "LT-MKT framework: joint modeling of cognitive load and knowledge transfer for multi-domain knowledge tracing"
description: "LT-MKT is a knowledge tracing framework for multi-domain learning scenarios that jointly models two factors the authors argue are overlooked by single-domain methods: cognitive load and knowledge transfer."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# LT-MKT framework: joint modeling of cognitive load and knowledge transfer for multi-domain knowledge tracing

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
LT-MKT is a knowledge tracing framework for multi-domain learning scenarios that jointly models two factors the authors argue are overlooked by single-domain methods: cognitive load and knowledge transfer. It constructs a Multi-domain Hierarchical Graph with LLM-guided reasoning, models cognitive load via "question difficulty, domain transition, and domain coverage", updates knowledge states with a GRU, and applies intraGAT and interGAT layers for prerequisite-based within-domain and cross-domain semantic transfer, followed by state fusion and prediction.

## Accounts
<!-- How each source describes or uses the method -->
- **LT-MKT framework: joint modeling of cognitive load and knowledge transfer for multi-domain knowledge tracing**: LT-MKT is a knowledge tracing framework for multi-domain learning scenarios that jointly models two factors the authors argue are overlooked by single-domain methods: cognitive load and knowledge transfer. It constructs a Multi-domain Hierarchical Graph with LLM-guided reasoning, models cognitive load via "question difficulty, domain transition, and domain coverage", updates knowledge states with a GRU, and applies intraGAT and interGAT layers for prerequisite-based within-domain and cross-domain semantic transfer, followed by state fusion and prediction. (Haotian Zhang et al. (2026))

### Claims

- [LT-MKT achieves the best performance across all four datasets and all three evaluation metrics against eleven KT baselines](../claims/lt-mkt-outperforms-kt-baselines-four-datasets.md) [+M]
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](../claims/cognitive-load-module-largest-ablation-drop.md) [+M]
- [Modeling knowledge transfer within and across domains alleviates the cold-start problem on unseen concepts](../claims/knowledge-transfer-alleviates-cold-start-kt.md) [+M]
- [The cognitive load module encodes cross-domain learning burden into student state representations as a low-to-high load gradient](../claims/cognitive-load-module-shapes-representation-space.md) [+W]
- [A qualitative case study shows LT-MKT jointly captures beneficial knowledge transfer and load-induced learning friction](../claims/case-study-transfer-and-load-friction.md) [+W]

## Related Research Methods
-

## Key Sources
- Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005
