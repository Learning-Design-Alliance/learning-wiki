---
type: claim
title: The cognitive load module encodes cross-domain learning burden into student state representations as a low-to-high load gradient
description: The cognitive load module encodes cross-domain learning burden into student state representations as a low-to-high load gradient
id: cognitive-load-module-shapes-representation-space
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: haotian-zhang-2026
    resource: "https://arxiv.org/abs/2608.24005"
    title: "Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005"
    author: Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The cognitive load module encodes cross-domain learning burden into student state representations as a low-to-high load gradient

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` UMAP visualization of test-interaction representations shows LT-MKT produces a clearer low-to-high cognitive-load gradient than the variant without cognitive load modeling. [→ Haotian Zhang 2026](#haotian-zhang-2026)

## Evidence

### Haotian Zhang 2026

Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005

`q2 · i?` · `design · r2`

Representation-level analysis on test interactions grouped into low-, medium- and high-load tertiles by a cognitive load index built from question difficulty, domain transition and domain coverage; representations visualized with UMAP (Figure 3).

> "In contrast, LT-MKT produces a clearer and more continuous low-to-high load gradient in the representation space. This pattern indicates that the proposed cognitive load module helps encode cross-domain learning burden into the student state representation"

## Discussion


## Related Claims
- [A qualitative case study shows LT-MKT jointly captures beneficial knowledge transfer and load-induced learning friction](case-study-transfer-and-load-friction.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
