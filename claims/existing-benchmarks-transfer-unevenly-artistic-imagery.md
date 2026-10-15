---
type: claim
title: Performance on existing benchmarks transfers unevenly to artistic educational imagery
description: Performance on existing benchmarks transfers unevenly to artistic educational imagery
id: existing-benchmarks-transfer-unevenly-artistic-imagery
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: luyao-zhu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.19088"
    title: "Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)"
    author: Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Performance on existing benchmarks transfers unevenly to artistic educational imagery

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Spearman correlations between six external benchmarks and the 12 MUSE tasks show uneven transfer: MMBench and AI2D correlate strongly with several MUSE tasks, BLINK shows inconsistent correlations, and AICA-Bench Emotion Reasoning aligns only moderately with MUSE's affective tasks, supporting MUSE's complementary coverage. [→ Luyao Zhu 2026](#luyao-zhu-2026)

## Evidence

### Luyao Zhu 2026

Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)

`q2 · i?` · `design · r2`

Cross-benchmark correlation analysis using pairwise-available model scores between the 12 MUSE tasks and 6 external benchmarks (Figure 7). The article reports that "existing benchmarks explain only part of the model variation on MUSE," and that Activity Description and Relative Position assess capabilities underrepresented in existing benchmarks.

> "AICA-Bench Emotion Reasoning She et al. [2026] aligns moderately with MUSE’s affective tasks, suggesting that emotion reasoning on conventional visual content only partially transfers to stylized expressions and implicit narratives in artworks."

## Discussion


## Related Claims
- [VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities](vlm-performance-task-dependent-muse.md) — related
- [MUSE tasks form coherent but non-redundant capability groups, with Jigsaw Puzzle a distinct compositional capability](muse-tasks-non-redundant-capability-groups.md) — related
