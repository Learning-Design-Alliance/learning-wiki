---
type: claim
title: Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect
description: Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect
id: cognitive-load-module-largest-ablation-drop
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: haotian-zhang-2026
    resource: "https://doi.org/10.48550/arxiv.2608.24005"
    title: "Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005 [doi:10.48550/arxiv.2608.24005](https://doi.org/10.48550/arxiv.2608.24005)"
    author: Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In ablations, removing cognitive load features (w/o CL) hurts most, removing the transfer GAT layers (w/o TG) also drops performance, and removing state fusion (w/o SF) has the smallest effect. [→ Haotian Zhang 2026](#haotian-zhang-2026)

## Evidence

### Haotian Zhang 2026

Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005 [doi:10.48550/arxiv.2608.24005](https://doi.org/10.48550/arxiv.2608.24005)

`q3 · i?` · `design · r2`

Ablation study on four datasets (Table 3) comparing full LT-MKT with w/o CL, w/o TG and w/o SF variants; the article reports "the cognitive load effect significantly impacts model performance" and that the complete model achieved the best overall performance.

> "Secondly, the cognitive load effect significantly impacts model performance, emphasizing the importance of cross-domain features in multi-domain learning. Thirdly, knowledge transfer mainly affects cross-domain knowledge evolution, and its removal causes a performance drop, while state fusion has a smaller effect."

## Discussion


## Related Claims
- [A qualitative case study shows LT-MKT jointly captures beneficial knowledge transfer and load-induced learning friction](case-study-transfer-and-load-friction.md) — related
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
- [The cognitive load module encodes cross-domain learning burden into student state representations as a low-to-high load gradient](cognitive-load-module-shapes-representation-space.md) — related
- [Performance is best at moderate difficulty granularity and a limited recent window for domain transitions](moderate-difficulty-granularity-window-optimal.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement](federated-aggregation-primary-performance-driver.md) — related
- [Each pedagogical verification component contributes to a distinct quality dimension: layout verification most strongly](verification-components-ablation-contributions.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance](eduagent-ablation-contextual-memory-critical.md) — related
- [Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%](ablation-trust-module-largest-contribution.md) — related
- Removing unsupervised pre-training hurts performance across all tasks, causing a 14.8% decrease relative to the full model — related
- [Removing any ProPRL component reduces F1 on all three datasets, with multi-hop propagation having the largest overall impact](proprl-ablation-components-contribute.md) — related
