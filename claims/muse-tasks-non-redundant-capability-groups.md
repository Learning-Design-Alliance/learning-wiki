---
type: claim
title: MUSE tasks form coherent but non-redundant capability groups, with Jigsaw Puzzle a distinct compositional capability
description: MUSE tasks form coherent but non-redundant capability groups, with Jigsaw Puzzle a distinct compositional capability
id: muse-tasks-non-redundant-capability-groups
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
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

# MUSE tasks form coherent but non-redundant capability groups, with Jigsaw Puzzle a distinct compositional capability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Pairwise Spearman correlations across 30 models show coherent task groups (e.g., Object Count, Emotion Detection, and Scene Classification strongly correlated; Visual Clue Identification closely tracking Emotion Cause Inference), while Jigsaw Puzzle correlates weakly with most tasks, indicating MUSE captures related but non-redundant dimensions. [→ Luyao Zhu 2026](#luyao-zhu-2026)

## Evidence

### Luyao Zhu 2026

Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng. (2026). MUSE: Benchmarking Large Vision-Language Models on Multi-modal Understanding in Situated Education. arXiv preprint. https://arxiv.org/abs/2609.19088 [doi:10.48550/arxiv.2609.19088](https://doi.org/10.48550/arxiv.2609.19088)

`q2 · i?` · `design · r2`

Inter-task correlation analysis computing pairwise Spearman's ρ across the 30 evaluated models (Figure 6). The article reports that "Jigsaw Puzzle correlates weakly with most tasks, indicating a distinct compositional capability," and concludes MUSE captures related but non-redundant dimensions rather than a single underlying competence.

> "Object Count, Emotion Detection, and Scene Classification are strongly correlated, while Visual Clue Identification closely tracks Emotion Cause Inference, linking visual evidence grounding with affective reasoning."

## Discussion


## Related Claims
- [Performance on existing benchmarks transfers unevenly to artistic educational imagery](existing-benchmarks-transfer-unevenly-artistic-imagery.md) — related
- [A recognition-versus-reasoning divide: scene recognition is comparatively mature while affective interpretation and compositional reasoning lag](recognition-reasoning-divide-muse.md) — related
- [VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities](vlm-performance-task-dependent-muse.md) — related
- [Standardized benchmarks are often too generic to reflect the needs of innovative educational applications](standardized-benchmarks-too-generic-for-education.md) — related
- [Human performance forms the outer envelope on nearly all MUSE tasks, with the largest deficits in Relative Position, Emotion Detection, and Jigsaw Puzzle](human-vlm-gap-muse-tasks.md) — related
